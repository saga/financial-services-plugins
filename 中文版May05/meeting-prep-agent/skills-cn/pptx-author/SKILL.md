---
name: pptx-author
description: 在磁盘上生成 .pptx 文件（无头模式），而非操作实时的 PowerPoint 窗口——适用于未打开 Office 应用的托管智能体 (Managed-agent) 会话。
---

# pptx-author

当在 **无头模式 (headless)** 下运行（即托管智能体 / CMA 模式），且需要将 PowerPoint 幻灯片作为 **文件产物 (file artifact)** 交付，而非通过 `mcp__office__powerpoint_*` 编辑实时文档时，请使用此技能。

## 输出规范 (Output contract)

- 写入至 `./out/<name>.pptx`。若 `./out/` 目录不存在，请先行创建。
- 在最终回复中返回相对路径，以便编排层 (orchestration layer) 进行文件收集。

## 如何构建幻灯片

编写一段简单的 Python 脚本并通过 Bash 执行。需使用 `python-pptx` 库：

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation("./templates/firm-template.pptx")  # 若提供机构模板
# 或: prs = Presentation()

slide = prs.slides.add_slide(prs.slide_layouts[5])    # 仅标题布局
slide.shapes.title.text = "估值摘要 (Valuation Summary)"
# ... 添加表格 / 图表 / 文本框 ...

prs.save("./out/pitch-<target>.pptx")
```

## 惯例 (镜像实时 Office 版 `pitch-deck` 技能)

- **一页一重点。** 标题陈述核心结论，正文提供支撑论据。
- **所有数据必须可溯源。** 若数字来源于 `./out/model.xlsx`，须在脚注中注明对应的工作表与单元格。
- **优先使用机构模板。** 当 `./templates/` 路径下挂载了模板时必须使用；否则使用默认布局。
- **图表处理**：当对还原度要求较高时，优先选择嵌入从模型渲染生成的 PNG 图片，而非使用 pptx 原生图表。
- **严禁对外发送。** 此技能仅负责本地文件写入，不涉及邮件发送或云端上传。

## 何时不可使用

若 `mcp__office__powerpoint_*` 工具可用（即 Cowork 插件模式），应优先使用前者——它们可以直接驱动用户的实时文档并支持审核检查点。本技能仅作为无头运行环境下的文件生成备选方案。

> **💡 Appendix: 领域知识小贴士**
>
> 1.  **无头模式 (Headless Mode)**：简单来说，就是程序在没有图形界面（看不到窗口、没有鼠标点击）的后台环境下运行。在金融自动化任务中，AI 经常直接在远程服务器通过代码生成报告，而不是像人类一样盯着屏幕操作软件。
> 2.  **文件产物 (Artifact)**：指任务完成后生成的实物成果。在金融咨询中，这通常指最终交付给客户的 PPT 幻灯片、Excel 模型或 PDF 合规文档。
> 3.  **数据溯源 (Data Tracing)**：这是金融从业者的基本素养。报告里的每一个数字都必须能找到出处（通常是 Excel 模型）。在 PPT 底部加上极其详尽的脚注（Footnote），是为了在面对审计或客户质疑时，能瞬间定位到数万行底稿中的源数据。
> 4.  **Python-pptx**：这是一种让程序员可以用“写脚本”的方式来画 PPT 的工具。它在批量生成几十份数据排版一致的投行演示稿（Pitch Deck）时，比人工复制粘贴要快得多，且能有效避免手滑填错数字。
