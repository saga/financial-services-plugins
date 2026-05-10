---
name: xlsx-author
description: 在磁盘上生成 .xlsx 文件（无界面模式），而非操作实时 Excel 工作簿——适用于无 Office 应用程序打开的托管代理 (Managed-agent) 会话。
---

# xlsx-author

当处于**无界面 (Headless)** 模式（托管代理 / CMA 模式）运行，且需要将 Excel 工作簿作为**文件交付物 (File Artifact)** 交付，而非通过 `mcp__office__excel_*` 编辑实时工作簿时，请使用此技能。

## 输出约定

- 写入 `./out/<name>.xlsx`。如果 `./out/` 目录不存在，请先创建。
- 在最终回复中返回相对路径，以便编排层 (Orchestration Layer) 进行收集。

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

## 建模约定（参照 `audit-xls`）

- **蓝 / 黑 / 绿。** 蓝色代表硬编码输入 (Hardcoded Input)，黑色代表公式 (Formula)，绿色代表指向其他工作表或文件的链接。
- **计算单元格严禁硬编码。** 所有计算单元格必须是公式逻辑；所有输入值应统一存放在 Inputs（输入）页签中。
- **命名区域 (Named Ranges)。** 对于任何在演示材料 (Pitch Deck) 或备忘录中引用的数值，请使用命名区域进行定义。
- **配平校验 (Balance Checks)。** 包含一个 Checks（校验）页签，用于核对钩稽关系（如资产负债表配平、现金流与现金的勾稽等），并明确显示 TRUE/FALSE。
- **一文件一模型。** 除非有明确要求，否则请勿在现有的工作簿中追加内容。

## 适用场景（不适用情况）

如果 `mcp__office__excel_*` 工具可用（即处于协作插件模式下），请优先使用这些工具——它们可以驱动用户实时打开的工作簿并支持审计记录。本技能仅作为无界面运行环境下的文件生产备选方案。

> **💡 Appendix: 领域知识小贴士**
>
> **1. 为什么要区分“蓝色”和“黑色”字？**
> 在专业的财务建模（如投资银行）中，这是全球通用的“着色规范”。**蓝色**代表是从外部输入的死数字，**黑色**代表是由公式算出来的。这样别人看你的表时，一眼就能知道哪里可以改动，哪里是核心逻辑，防止误改！
>
> **2. 什么是 DCF？**
> 全称是“现金流折现模型”。简单来说，就是根据一个公司未来能赚多少钱，把这些未来的钱按照一定的“折扣”折现到现在，来算出这个公司今天到底值多少钱。它是金融圈估值最常用的“金标准”。
>
> **3. 为什么要专门做“Checks（校验）”页签？**
> 金融模型就像一架复杂的机器，一个零件报错全盘皆错。**配平 (Balance)** 是指资产必须等于负债加股东权益。如果有一分钱对不上，模型就是无效的。校验页签就像监视器，确保模型逻辑严丝合缝，没有“爆雷”。
