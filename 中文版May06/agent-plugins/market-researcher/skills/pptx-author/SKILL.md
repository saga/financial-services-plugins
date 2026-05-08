---
name: pptx-author
description: 在磁盘上生成 .pptx 文件（无界面运行），而非驱动实时 PowerPoint 文档 —— 适用于没有打开 Office 应用程序的托管代理 (Managed-agent) 会话。
---

# PPT 生成助手 (pptx-author)

当你在**无界面模式**（托管代理 / CMA 模式）下运行，且需要交付一个 PowerPoint 幻灯片作为**文件产出**（而非通过 `mcp__office__powerpoint_*` 编辑实时文档）时，请使用此技能。

## 输出契约

- 写入到 `./out/<名称>.pptx`。如果 `./out/` 目录不存在，请先创建。
- 在你的最终回复中返回相对路径，以便编排层能够收集该文件。

## 如何构建幻灯片

编写一个简短的 Python 脚本并通过 Bash 运行。使用 `python-pptx` 库：

```python
from pptx import Presentation
from pptx.util import Inches, Pt

# 如果提供了模板：
prs = Presentation("./templates/firm-template.pptx") 
# 或者创建新文档：
# prs = Presentation()

slide = prs.slides.add_slide(prs.slide_layouts[5])    # 仅标题布局
slide.shapes.title.text = "估值摘要"
# ... 添加表格 / 图表 / 文本框 ...

prs.save("./out/pitch-<目标>.pptx")
```

## 规范（镜像自实时 Office 的 `pitch-deck` 技能）

- **一页一个观点。** 标题表述核心结论；正文提供支持。
- **每个数字都要溯源至模型。** 如果数字来自 `./out/model.xlsx`，请在脚注中注明工作表和单元格。
- **使用公司模板**：如果 `./templates/` 中挂载了模板，请优先使用；否则使用默认布局。
- **图表**：当对还原度要求很高时，优先选择嵌入从模型渲染生成的 PNG 图片，而非使用 pptx 原生图表。
- **严禁外部发送**：本技能仅负责写入文件；绝不发送电子邮件或执行上传操作。

## 何时不使用

如果 `mcp__office__powerpoint_*` 工具可用（Cowork 插件模式），请优先使用这些工具 —— 它们可以驱动用户的实时文档并带有审核检查点。本技能仅作为无界面运行时的文件生成备选项。

---

### 🏮 金融小白附录：重点词汇详解

1. **Headless (无界面/后台运行)**：通俗讲就是“没人盯着看”。AI 在服务器后台默默地把 PPT 做好了直接塞进文件夹，而不是在你电脑屏幕上一页一页地跳出来。
2. **Artifact (产出物/工件)**：在金融办公中，这就是你最终干活的成果，比如一份做好的 Excel 或者一个 PPT。
3. **Template (模板)**：大投行和基金公司都有自己的一套“皮肤”——固定的配色、Logo 和排版。AI 必须穿上这身“制服”，做出来的幻灯片才显得专业。
4. **Takeaway (核心结论)**：这一页 PPT 到底想说什么。金融圈节奏快，老板喜欢一眼就能看到结论。
