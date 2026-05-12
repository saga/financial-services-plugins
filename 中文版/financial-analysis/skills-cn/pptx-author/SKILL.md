---
name: pptx-author
description: 在磁盘上生成 .pptx 文件（无头模式），而非操作实时 PowerPoint 文档——适用于未开启 Office 应用程序的托管代理（Managed-Agent）会话。
---

# pptx-author

当处于 **无头（Headless）** 运行模式（托管代理 / CMA 模式）且需要将 PowerPoint 演示文稿作为 **文件产出（File Artifact）** 交付，而非通过 `mcp__office__powerpoint_*` 编辑实时文档时，请执行此项技能。

## 输出规范

- 写入至 `./out/<name>.pptx`。若 `./out/` 目录不存在则需先行创建。
- 在最终消息中返回相对路径，以便编排层进行收集。

## 如何构建演示文稿

编写一段简草的 Python 脚本并通过 Bash 运行。请使用 `python-pptx` 库：

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation("./templates/firm-template.pptx")  # 若提供模板
# 或：prs = Presentation()

slide = prs.slides.add_slide(prs.slide_layouts[5])    # 仅标题布局
slide.shapes.title.text = "估值摘要"
# ... 添加表格 / 图表 / 文本框 ...

prs.save("./out/pitch-<target>.pptx")
```

## 编写惯例（镜像实时 Office `pitch-deck` 技能）

- **一页一核心。** 标题阐明核心观点（Takeaway），正文提供支撑证据。
- **数据必有据。** 每一个数字都应可追溯至模型。若数据源自 `./out/model.xlsx`，请在脚注中注明工作表及单元格。
- **优先使用模板。** 若 `./templates/` 中挂载了公司模板，请优先使用；否则采用默认布局。
- **图表处理：** 当对还原度有较高要求时，相比于原生 pptx 图表，更推荐嵌入从模型渲染生成的 PNG 图片。
- **禁止外发。** 此技能仅生成本地文件，严禁进行邮件发送或上传操作。

## 何时禁用

若 `mcp__office__powerpoint_*` 工具可用（Cowork 插件模式），请优先使用这些工具——它们可以直接操作用户的实时文档并包含审核检查点。本技能仅作为无头模式下生成文件的备选方案。

> **💡 Appendix: 领域知识小贴士**
>
> *   **无头模式 (Headless Mode):** 想象一下你有一台没有显示器的电脑，程序在后台默默运行，你看不到窗口弹出。在金融自动化中，这意味着 AI 直接在服务器上处理文件，不需要人工打开 PowerPoint 软件。
> *   **估值 (Valuation):** 简单来说，就是给一家公司“算算值多少钱”。金融专家会分析公司的收入、利润和风险，给出一个合理的市场价格。
> *   **路演文稿 (Pitch Deck):** 这是创业者或投资银行家用来向投资人推销项目的 PPT。它不仅需要漂亮，更需要数据支撑，因为每一个百分点的变动都可能涉及上亿的资金。
> *   **金融模型 (Financial Model):** 它是金融人的“实验室”，通常是一个复杂的 Excel 表格。模型通过公式预测未来的财务状况。文稿中的每个数字（如“预计明年收入增长 20%”）都必须从这个模型里通过严谨逻辑推导出来。
