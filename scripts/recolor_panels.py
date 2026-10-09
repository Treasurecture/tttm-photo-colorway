import argparse,json
from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter
import numpy as np

def recolor(source,palette,destination):
    im=Image.open(source).convert('RGB'); w,h=im.size
    if abs(w/h-1.5)>.01:raise ValueError('Masks are for the canonical 1800x1200 official photo only.')
    a=np.asarray(im).astype(float)/255
    hsv=np.asarray(im.convert('HSV')).astype(float)/255
    yy,xx=np.indices((h,w)); x=xx*1800/w;y=yy*1200/h
    fabric=((hsv[:,:,0]>.35)&(hsv[:,:,0]<.58)|(hsv[:,:,0]>.67)&(hsv[:,:,0]<.90))&(hsv[:,:,1]>.16)&(hsv[:,:,2]>.13)
    # Protect the original printed badge; its white border is outside the color mask.
    bx=(x-777)*.866-(y-453)*.5;by=(x-777)*.5+(y-453)*.866
    badge=(bx/25)**2+(by/16)**2<1
    fabric &= ~badge
    purple=(hsv[:,:,0]>.67)&(hsv[:,:,0]<.90)
    def polygon(points):
        m=Image.new('L',(w,h));ImageDraw.Draw(m).polygon([(px*w/1800,py*h/1200) for px,py in points],fill=255)
        return np.asarray(m)>0
    flap=fabric&polygon([(675,580),(685,520),(720,455),(780,405),(875,398),(925,397),(981,385),(971,482),(939,515),(880,550),(821,578),(762,594),(710,590)])
    straps=fabric&(polygon([(946,380),(1005,337),(1038,320),(1080,326),(1100,350),(1108,545),(1120,660),(1070,670),(1052,515),(1045,376),(1040,348),(1015,350),(991,373),(981,399)])|((y<390)&(x<925)))
    # Preserve curved main-body bottom; recolor only narrow existing fabric binding.
    trim=fabric&(y>865-.0007*(x-850)**2)&(y>815)
    side=fabric&purple&~flap&~straps&~trim
    body=fabric&~flap&~straps&~trim&~side
    # The top loop is textile, distinct from black zipper/adjustment hardware.
    handle=(x>872)&(x<927)&(y>329)&(y<385)&(hsv[:,:,2]<.26)
    masks={'main_body':body,'front_flap':flap,'side_panel':side,'shoulder_straps':straps,'bottom_trim':trim,'top_handle':handle}
    result=a.copy(); lum=a@np.array([.2126,.7152,.0722])
    for key,mask in masks.items():
        if not np.any(mask):continue
        rgb=np.array(palette[key],dtype=float)/255
        # Transfer the chosen photo-derived base tone, preserve local texture/shading.
        center=np.median(lum[mask]); shade=np.clip(lum/max(center,.02),.35,1.15)
        colored=np.clip(shade[:,:,None]*rgb,0,1)
        result[mask]=colored[mask]
    final=Image.fromarray(np.uint8(np.round(result*255)))
    final.save(destination)
    protected=~np.logical_or.reduce(list(masks.values()))
    assert np.array_equal(np.asarray(final)[protected],np.asarray(im)[protected])
    return final

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('base_image');p.add_argument('palette_json');p.add_argument('-o',required=True)
    args=p.parse_args();recolor(args.base_image,json.loads(args.palette_json),args.o)
