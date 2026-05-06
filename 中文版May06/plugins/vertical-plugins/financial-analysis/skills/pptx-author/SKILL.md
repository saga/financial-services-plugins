---
name: pptx-author
description: 在磁盘上生成 .pptx 文件（无头模式），而非操作实时 PowerPoint 文档——适用于未打开 Office 应用程序的托管代理 (CMA) 会话。
---

# pptx-author

当在**无头模式**（托管代理 / CMA 模式）下运行，且需要将 PowerPoint 演示文稿作为**文件产出物**交付，而非通过 `mcp__office__powerpoint_*` 编辑实时文档时，请使用此技能。

## 输出契约

- 写入至 `./out/<name>.pptx`。如果 `./out/` 目录不存在，请先创建。
- 在最终消息中返回相对路径，以便编排层可以统一提取。

## 如何构建演示文稿

编写一段简短的 Python 脚本并使用 Bash 运行。使用 `python-pptx` 库：

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation("./templates/firm-template.pptx")  # 如果提供了公司模板
# 或者: prs = Presentation()

slide = prs.slides.add_slide(prs.slide_layouts[5])    # 仅含标题的布局
slide.shapes.title.text = "估值摘要"
# ... 添加表格 / 图表 / 文本框 ...

prs.save("./out/pitch-<target>.pptx")
```

## 操作规范（参考实时 Office 环境下的 `pitch-deck` 技能）

- **每张幻灯片传达一个核心观点。** 标题应当陈述结论；正文内容负责支撑该结论。
- **所有数据必须可溯源至模型。** 如果数字源自 `./out/model.xlsx`，请在脚注中注明对应的工作表（Sheet）和单元格（Cell）。
- **优先使用公司模板。** 当 `./templates/` 目录中挂载了模板时请务必使用；否则采用默认布局。
- **图表处理**：当对画面精准度（Fidelity）有较高要求时，相比于 pptx 原生图表，优先选择嵌入从模型渲染生成的 PNG 图片。
- **禁止外部发送。** 此技能仅负责本地文件的写入，严禁进行电子邮件发送或云端上传。

## 何时**不**适用

如果 `mcp__office__powerpoint_*` 相关工具可用（协作插件模式），请优先使用这些工具——它们可以直接驱动用户的实时文档，并支持设置人工审阅检查点。本技能仅作为无头运行环境下的文件生成后备方案。

> **💡 Appendix: 领域知识小贴士**
>
> 1. **无头模式 (Headless Mode)**：通俗地说，就是“没有界面的操作”。就像一个隐形人在后台帮你写 PPT，你看不见 PowerPoint 软件被打开的过程，但最终文件夹里会直接出现一个完美的文件。这在 AI 自动化处理时非常高效。
> 2. **托管代理 (Managed Agent)**：你可以把它理解为一个在云端服务器上全职为你工作的“AI 小秘书”。因为它运行在云端，可能并没有安装或打开普通的 Office 窗口，所以需要专门的工具来生成文件。
> 3. **数据溯源 (Data Traceability)**：在金融行业，专业性体现在每一个数字的“出处”。如果 PPT 上的利润率写错了，可能会导致投资决策失误。要求数据溯源，就是为了确保 PPT 上的每一个数字都能在背后的 Excel 算账模型里找到出处。
> 4. **估值摘要 (Valuation Summary)**：这是金融分析中最关键的内容之一，用来告诉投资者一个公司到底值多少钱。它通常把复杂的财务模型简化为几张直观的图表，是投行、券商等机构最常用的演示文件之一。
