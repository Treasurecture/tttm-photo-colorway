---
name: tttm-photo-colorway
description: Design photo-inspired fabric colorways for Ticket To Moon Mini Backpack XS, recolor its official product photo without redrawing, and deliver a high-resolution photo comparison plus ordering notes.
---

# TTTM-拾色成包

从参考照片提取有审美层次的色彩，并真实反映到官方 Mini Backpack XS 产品照片的不同面料区域。交付格式保持：左参考照片、右包体效果图，以及可复制英文订单备注的 Markdown 文件。

## 不变约束

- 禁止文生图画包、替换包型或手绘新包。允许编辑现有官方照片，也允许程序蒙版改色。
- 基图优先 `assets/backpack-xs-official-01.jpg`，否则用指定官网原图：
  `https://cdn.shopify.com/s/files/1/0693/7968/6678/files/tmbpxs_ecotic_ocean.jpg?v=1773764046&width=2048`
- 本原图原生尺寸 1800 × 1200。禁止放大低清缩略图并称为高清。其他底图不得冒用这些专用蒙版。
- 保留紧凑 6L 包型、17 × 30 × 8 cm 比例、弧形前袋及黑色拉链、圆形徽标、顶部拉链、两肩带、侧片、提手、尼龙纹理和白底。
- 黑色拉链、扣件、拉链头和调节织带保持黑色；面料肩带、面料包边、织物提手可以独立改色。徽标原样保留。

## 官网与色名

制作前访问 `https://ticketothemoon.com/products/backpack-xs-custom`，并尝试 `https://eu.ticketothemoon.com/en/collections/all` 或主站目录。检查照片与产品信息。实时颜色选择器可读时优先使用其色名；不可读时允许下表，但明确未完成实时库存核验。

| 色系 | 允许的色名 |
|---|---|
| 蓝 | Royal Blue, Navy Blue, Deep Blue, Exotic Ocean, Ice Blue |
| 绿 | Petrol Green, Leaf Green, Army Green, Forest Green, Emerald Green, Mint, Green Apple |
| 土色 | Copper, Sand, Beige, Dark Beige, Chocolate, Ice Brown |
| 红紫 | Burgundy, Plum, Light Purple |
| 中性 | Black, Dark Grey, Grey |

照片采样值、审美调整值可以用 RGB 或 HEX 作为渲染参数，但不得声称它们是品牌官方布料色值。每个面料区域必须有允许色名，近似匹配需解释。

## 配色审美：照片提取不等于机械复制

1. 在天空、水、植物、地面、服装或微小亮色中选 4–6 个能代表画面情绪的颜色。用 PIL/numpy 在紧凑局部窗口取中位数，避免混入阴影、反光和背景；记录来源。
2. 从这些颜色里构成主色、支持色、少量点缀。大面积优先 2–3 个有层次的颜色，深色用于收束、小面积亮色用于记忆点；不要让每块面料同样抢眼。
3. 可以降低过高饱和度、提亮阴影样本，或细调色相。解释调整与照片的关系。不能把六个机械采样值直接当成六个好看的设计色。
4. 不能把“和谐”理解为大面积雷同，也不能强制所有颜色同温度。照片里的冷天空与暖沙地可以构成克制的冷暖对照。
5. 同色系相邻面料允许小的明度、饱和度或色相差异；差异必须在实际包体预览尺寸可见。不要仅凭名字不同认定有层次。
6. 对主包身、前袋、侧片、肩带面料、底部面料边缘、提手面料分别分配颜色。黑色五金独立保护。色差应能对应照片来源或有依据的支持色。
7. 先看色卡，再看包上面积比例。若画面发灰、荧光、杂乱、主支持色雷同或点缀面积过大，先调整再交付。审美不要求六个毫不相关的色相。

## 改图路径与一致性

- 优先使用可用的现有照片编辑工具（例如 image_edit 或 Adobe image_instruct_edit）；按功能识别而非只认工具名称。提示词先列包型与五金保护，再列各区域色名和目标层次。禁止 image_generate / 文生图接口。
- 缺工具可尝试可用的工具发现功能；若不可用或服务失败，使用程序分区蒙版，不反复索要同一已提供素材。
- 附带 `scripts/recolor_panels.py` 仅适用本包官方原图，分离几何区域与原面料色域，保护白底、徽标、黑色五金。通过各区域亮度相对中位数传递纹理，同时匹配目标基色，避免只换色相造成浅蓝灰暗或深绿变浅。
- 调用示例：
  `python scripts/recolor_panels.py assets/backpack-xs-official-01.jpg '<palette JSON>' -o mockup.png`
- JSON 含 `main_body`, `front_flap`, `side_panel`, `shoulder_straps`, `bottom_trim`, `top_handle`；每项为照片来源并经过说明的 RGB 三元组。
- 脚本蒙版是近似设计分区，需要逐次视觉检查；不得把直线截断、漏色、溢色、徽标周围原色晕圈、硬件变色当作成品。新的底图或新姿态必须重建并核验蒙版。
- 全局两色域替换不是完整多区域方案。若只有两域改色，把它标为局部研究，不得作为完成六区要求的最终稿。图、色卡、区域表和订单备注必须对应。
- 不能对不可见的面料伪造渲染；说明视角限制。底部区域的示意分界不是生产缝线规格。

## 核验与交付

视觉核验轮廓、弧形前袋、黑色拉链、徽标、褶皱和面料区域。核验原生尺寸；程序处理验证所有蒙版外像素不变。检查相邻颜色在包体上可辨且有主次。必要时修改并重看，不交付未核验版本。

对比图维持左照片、右完整包体，匹配画格，白底与适当间隔；可以裁剪产品图白边，但不能裁切包体或为了填满画格生成新部件。交付原生高清效果图、对比图和 Markdown 说明。

说明含照片采样与审美调整、六区域映射、色名表、实际渲染限制、英文订单备注：

```text
Main body:         [official color name]
Front flap pocket: [official color name]
Side panel:        [official color name]
Shoulder straps:   [official color name; fabric only]
Bottom trim:       [official color name; fabric only]
Top handle:        [official color name; fabric only]
Hardware/zippers:  keep black
Logo badge:        keep original
```

产品事实：降落伞尼龙、110g、6L；Unique Edition 使用生产余料，由制作者决定组合。配色为愿望参考，不是颜色和订单执行保证。
