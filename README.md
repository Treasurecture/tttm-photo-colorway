# TTTM-拾色成包

把印尼的风景，打包带走。

从火山晨光、瀑布水雾与大海的照片中提取色彩，为 Ticket To The Moon Mini Backpack XS 设计有层次的面料配色。编辑官方产品照片，保留真实包型，输出高清效果图、照片对比图和英文订单备注。

**Pack the scenery. Carry the memory.**

Turn travel photographs into personal colorways for the Ticket To The Moon Mini Backpack XS. Preserve the official product silhouette and create high-resolution previews, photo comparisons, and English ordering notes.

## 使用

将完整仓库作为 skill 资源包使用，让支持 skills 的助手读取 `SKILL.md`，然后提供参考照片。需要保留 `assets/` 和 `scripts/`，不能仅复制说明文件。

程序改色依赖 Python、Pillow 和 numpy：

```bash
pip install -r requirements.txt
python scripts/recolor_panels.py assets/backpack-xs-official-01.jpg '{"main_body":[174,115,75],"front_flap":[231,216,199],"side_panel":[88,100,120],"shoulder_straps":[61,49,43],"bottom_trim":[80,81,88],"top_handle":[157,195,226]}' -o mockup.png
```

示例 RGB 为照片衍生的渲染参数，不是官方布料色值。脚本蒙版仅适用随附官方产品图，必须核验分区边缘。

## 文件

- `SKILL.md`：完整工作流程和配色审美要求。
- `assets/backpack-xs-official-01.jpg`：1800 × 1200 官方底图。
- `scripts/recolor_panels.py`：保留原图纹理的分区改色工具。
- `requirements.txt`：程序依赖。

## 来源与适用范围

官方产品：https://ticketothemoon.com/products/backpack-xs-custom

产品照片属于其原权利方。本项目不是 Ticket To The Moon 官方项目。效果图是配色参考，不是官方布料色卡；Unique Edition 使用生产余料，实际颜色取决于可用面料与制作安排。
