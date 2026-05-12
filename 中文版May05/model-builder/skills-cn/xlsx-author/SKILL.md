---
name: xlsx-author
description: 在磁盘上生成 .xlsx 文件（无头模式），而非操作实时 Excel 工作簿 —— 适用于未开启 Office 应用的托管智能体会话。
---

# xlsx-author

当处于**无头（headless）**运行模式（即托管智能体 / CMA 模式）且需要将 Excel 工作簿作为**文件产物**交付，而非通过 `mcp__office__excel_*` 系列工具编辑实时工作簿时，请使用此技能。

## 输出规范

- 写入路径：`./out/<name>.xlsx`。若 `./out/` 目录不存在，请先创建。
- 在最终回复中返回相对路径，以便编排层进行自动收集。

## 如何构建工作簿

编写一段简短的 Python 脚本并通过 Bash 运行。使用 `openpyxl` 库：

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

wb = Workbook()
ws = wb.active; ws.title = "Inputs"
ws["B2"] = "Revenue"; ws["C2"] = 1_250_000_000
ws["C2"].font = Font(color="0000FF")           # 蓝色 = 硬编码输入
calc = wb.create_sheet("DCF")
calc["C5"] = "=Inputs!C2*(1+Inputs!C3)"        # 黑色 = 公式
wb.save("./out/model.xlsx")
```

## 建模准则（参考 `audit-xls` 规范）

- **蓝/黑/绿颜色编码：** 蓝色代表硬编码输入（Hardcoded input），黑色代表公式（Formula），绿色代表指向其他工作表或文件的链接（Link）。
- **计算单元格严禁硬编码：** 所有进行计算的单元格必须使用公式；所有基础输入数据应集中存放在“Inputs”工作表中。
- **命名区域（Named ranges）：** 任何需要被演示文稿或备忘录引用的数值，均需创建命名区域。
- **平衡勾稽检查：** 必须包含一个“Checks”工作表，用于验证报表间的勾稽关系（如资产负债表平衡、现金流量表与现金余额对齐等），并直观显示 TRUE/FALSE。
- **一文件一模型：** 除非有明确指示，否则不要在现有工作簿中追加内容。

## 何时**不**使用

如果 `mcp__office__excel_*` 工具可用（即处于协同插件模式），请优先使用这些工具 —— 它们可以驱动用户的实时工作簿并支持人工复核回点。本技能仅作为无头运行环境下生成文件的备选方案。

> **💡 Appendix: 领域知识小贴士**
>
> 1. **无头模式 (Headless Mode)**：想象一下一个没有显示器、在后台默默工作的机器人。在金融自动化中，这意味着 AI 直接在服务器里处理数据并生成文件，而不需要在你的屏幕上真的“弹出”一个 Excel 窗口。
> 2. **硬编码 (Hardcoding)**：指直接输入单元格的死数字（比如去年的固定营收）。在顶级投行的财务模型中，有个不成文的规定：输入必须是蓝色的，公式必须是黑色的。这样接手你工作的人一眼就能看出哪些是假设，哪些是逻辑。
> 3. **勾稽关系 (Ties/Checks)**：会计学讲究“平”。资产负债表左右得相等，现金流得跟银行账对得上。在模型里做一个专门的“Checks”表，就像是给模型装了个自动报警器，逻辑一错，立马显示 FALSE。
