---
name: xlsx-author
description: 在磁盘上生成 .xlsx 文件（无界面模式），而非操作实时 Excel 工作簿 —— 适用于没有开启 Office 应用的托管代理（CMA）会话。
---

# xlsx-author

当在**无界面**（Headless，即托管代理/CMA 模式）下运行，且需要将 Excel 工作簿作为**文件产物**交付，而非通过 `mcp__office__excel_*` 编辑实时工作簿时，请使用此技能。

## 输出约定

- 写入路径为 `./out/<name>.xlsx`。如果 `./out/` 目录不存在，请先创建。
- 在最终消息中返回相对路径，以便编排层（Orchestration Layer）进行文件采集。

## 如何构建工作簿

编写一段简短的 Python 脚本并使用 Bash 运行。推荐使用 `openpyxl` 库：

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

wb = Workbook()
ws = wb.active; ws.title = "Inputs"
ws["B2"] = "Revenue"; ws["C2"] = 1_250_000_000
ws["C2"].font = Font(color="0000FF")           # 蓝色 = 硬编码输入值
calc = wb.create_sheet("DCF")
calc["C5"] = "=Inputs!C2*(1+Inputs!C3)"        # 黑色 = 计算公式
wb.save("./out/model.xlsx")
```

## 建模规范（参考 `audit-xls`）

- **蓝/黑/绿 颜色标准。** 蓝色表示硬编码输入值（Hardcoded Input），黑色表示计算公式（Formula），绿色表示指向其他工作表或文件的链接。
- **计算单元格禁止硬编码。** 每一个计算单元格都必须是公式；所有输入变量必须统一存放在 “Inputs” 选项卡中。
- **命名区域（Named Ranges）。** 对于任何会被演示文稿（Deck）或备忘录（Memo）引用的数值，请务必定义命名区域。
- **平衡检查（Balance Checks）。** 必须包含一个 “Checks” 选项卡，用于核对各个维度的勾稽关系（如资产负债表平衡、现金流量表与期末现金的一致性等），并直观显示 TRUE/FALSE。
- **一档一型。** 除非有明确要求，否则不要向现有工作簿追加内容，请保持一个模型对应一个文件。

## 何时不适用

如果 `mcp__office__excel_*` 系列工具可用（即 Cowork 插件模式），请优先使用它们 —— 这些工具可以直接驱动用户的实时工作簿并支持人工审核。本技能仅作为无界面运行模式下生成文件的备选方案。

> **💡 Appendix: 领域知识小贴士**
>
> 1.  **无界面模式 (Headless):** 这就像是在后台运行的自动化工厂。程序不需要像人类一样打开 Excel 窗口、点击菜单，而是直接在计算机的内存和磁盘里“凭空”造出文件。这在处理大规模数据自动化时速度极快。
> 2.  **硬编码 (Hardcoding):** 指的是直接把死数字（比如 100 万）写在公式里。在财务建模中这是大忌！专业做法是把数字放在专门的“输入页”，其他地方通过公式链接。这样一旦改动一个假设（比如增长率），整个模型都会自动更新，不会出错。
> 3.  **DCF (现金流折现模型):** 财务里的“时空穿梭机”。它通过预测一家公司未来几年能赚多少钱，并把这些未来的钱按照一定的利率“折算”成现在的价值。它是衡量一家公司值不值钱的核心方法。
> 4.  **勾稽关系 (Ties/Checks):** 会计学里的“能量守恒定律”。比如你赚的钱（利润）最终必须能在资产负债表里找到去向。在 Excel 里设置 Checks 页面，就像给模型装了报警器，如果资产不等于负债加股东权益，模型就会通过“FALSE”提醒你哪里算错了。
