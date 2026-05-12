---
name: pptx-author
description: 在磁盘上生成 .pptx 文件（无界面模式），而非操作实时 PowerPoint 文档 —— 适用于无 Office 运行环境的托管智能体会话。
---

# pptx-author

在 **无界面（headless）** 模式（托管智能体 / CMA 模式）下运行时，若需要将 PowerPoint 演示文稿作为 **文件产物** 交付，而非通过 `mcp__office__powerpoint_*` 在线编辑实时文档，请使用此技能。

## 输出契约 (Output contract)

- 写入路径：`./out/<name>.pptx`。如 `./out/` 目录不存在，请先创建。
- 在最终回复中返回相对路径，以便编排层（orchestration layer）进行文件收集。

## 如何构建演示文稿

编写简短的 Python 脚本并使用 Bash 运行。使用 `python-pptx`：

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation("./templates/firm-template.pptx")  # 如果提供了公司模板
# 或者使用默认模板：prs = Presentation()

slide = prs.slides.add_slide(prs.slide_layouts[5])    # 仅标题布局 (title-only)
slide.shapes.title.text = "估值摘要 (Valuation Summary)"
# ... 添加表格 / 图表 / 文本框 ...

prs.save("./out/pitch-<target>.pptx")
```

## 惯例规范 (参考实时 Office 环境下的 `pitch-deck` 技能)

- **一页一重点 (One idea per slide)。** 标题陈述核心结论，正文提供支撑细节。
- **所有数据严谨溯源。** 若数据源自 `./out/model.xlsx`，请在脚注中标注具体的工作表 (Sheet) 和单元格。
- **优先使用公司模板。** 若 `./templates/` 目录中挂载了模板文件，请优先使用；否则使用默认布局。
- **图表处理：** 相比原生 pptx 图表，当对数据精确度 (Fidelity) 有极高要求时，建议优先嵌入从模型生成的 PNG 渲染图。
- **严禁外部发送。** 此技能仅生成本地文件，严禁执行发送邮件或上传操作。

## 何时不用

如果 `mcp__office__powerpoint_*` 工具（Cowork 插件模式）可用，请优先使用——这些工具可以直接驱动用户的实时文档并支持设置评审检查点。本技能仅作为无界面运行环境下的文件产物回退方案。

> **💡 Appendix: 领域知识小贴士**
>
> 1. **Pitch Deck (项目推介书/路演幻灯片)**：这是投行或融资圈的“敲门砖”。它不仅是 PPT，更是向投资者展示公司核心竞争力、市场地位和财务前景的商业蓝图。专业感体现在结论先行和严谨的逻辑支撑。
> 2. **Valuation (估值)**：这就是在回答“这家公司值多少钱？”。金融分析师会通过复杂的 Excel 模型（如现金流折现模型）算出结论，而 PPT 中的“估值摘要”则是这些繁琐计算的高亮浓缩版。
> 3. **Headless Mode (无界面/无头模式)**：这听起来很酷，其实是指程序在后台默默运行，不需要弹出我们平时看到的软件窗口。AI 直接通过代码把文件“攒”出来，既快又准，非常适合大批量生成标准化的财务分析报告。
