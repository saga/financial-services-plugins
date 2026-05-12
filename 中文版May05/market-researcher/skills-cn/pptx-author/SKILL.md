---
name: pptx-author
description: 在磁盘上生成 .pptx 文件（无头模式），而不是驱动实时 PowerPoint 文档 —— 适用于没有打开 Office 应用程序的托管智能体（managed-agent）会话。
---

# pptx-author

当在**无头（headless）**模式（托管智能体 / CMA 模式）下运行，且需要将 PowerPoint 演示文稿作为**文件产物（file artifact）**交付，而非通过 `mcp__office__powerpoint_*` 接口编辑实时文档时，请使用此技能。

## 输出契约 (Output contract)

- 写入到 `./out/<name>.pptx`。如果 `./out/` 目录不存在，请先创建。
- 在最终消息中返回相对路径，以便编排层（orchestration layer）进行收集。

## 如何构建演示文稿

编写一个简短的 Python 脚本并使用 Bash 运行。需调用 `python-pptx` 库：

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation("./templates/firm-template.pptx")  # 如果提供了模板
# 或者: prs = Presentation()

slide = prs.slides.add_slide(prs.slide_layouts[5])    # 仅标题布局
slide.shapes.title.text = "估值摘要 (Valuation Summary)"
# ... 添加表格 / 图表 / 文本框 ...

prs.save("./out/pitch-<target>.pptx")
```

## 惯例 (遵循实时 Office `pitch-deck` 技能规范)

- **每张幻灯片一个核心观点。** 标题阐述核心结论（Takeaway）；正文提供支撑论点。
- **所有数据均可追溯至模型。** 如果引用了 `./out/model.xlsx` 中的数据，请在脚注中注明具体的工作表及单元格。
- **优先使用公司模板。** 当 `./templates/` 目录挂载了模板文件时请优先使用；否则采用默认布局。
- **图表**：若对图形保真度有严格要求，相比 PPT 原生图表，优先建议嵌入从财务模型渲染生成的 PNG 图片。
- **严禁外部发送。** 此技能仅负责生成文件，绝不执行邮件发送或数据上传操作。

## 何时**不应**使用

如果 `mcp__office__powerpoint_*` 工具组可用（即处于 Cowork 插件模式），请优先使用这些工具 —— 它们可以驱动用户的实时文档并支持审查验证点。本技能仅作为无头运行模式下生成文件产物的备选方案。

> **💡 Appendix: 领域知识小贴士**
>
> - **估值摘要 (Valuation Summary)**：可以把它想象成一家公司的“身价报告”。分析师通过复杂的计算，算出这家公司到底值多少钱。在 PPT 里，这就是告诉投资人“这笔买卖值不值得做”的关键页。
>
> - **推介演示文稿 (Pitch Deck)**：这是金融圈的“商业敲门砖”。无论是创业者找投资人要钱，还是投行帮公司卖股票，都会准备这样一份逻辑严密的 PPT，用来讲清楚“我们是谁、我们要干什么、能赚多少钱”。
>
> - **财务模型 (Model)**：这通常是一个装满公式的 Excel 大表，是所有金融数据的“加工厂”。专业金融人的基本素养是：PPT 上的每一个数字，都必须能回溯到模型里的某一个格子，这叫“有据可查”。
>
> - **无头模式 (Headless)**：这是一种自动化黑科技。想象一个没有显示器、只有“大脑”在工作的机器人。它不需要像真人一样打开 PowerPoint 软件并在屏幕上点来点去，而是在后台默默地把文件直接“变”出来。
