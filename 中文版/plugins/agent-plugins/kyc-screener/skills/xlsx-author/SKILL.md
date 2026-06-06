---
name: xlsx-author
description: 在磁盘上生成.xlsx文件（无界面模式），而非操作实时Excel工作簿——适用于没有打开Office应用的托管代理会话。
---

# xlsx-author

当运行在**无界面模式**（托管代理/CMA模式）下，且需要以**文件形式**交付Excel工作簿而非通过`mcp__office__excel_*`操作实时工作簿时使用本技能。

## 输出约定

- 写入`./out/<名称>.xlsx`。若`./out/`目录不存在则创建。
- 在最终消息中返回相对路径，以便编排层收集该文件。

## 如何构建工作簿

编写一个简短的Python脚本并用Bash运行。使用`openpyxl`库：

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

wb = Workbook()
ws = wb.active; ws.title = "输入页"
ws["B2"] = "营收"; ws["C2"] = 1_250_000_000
ws["C2"].font = Font(color="0000FF")           # 蓝色 = 硬编码输入值
calc = wb.create_sheet("DCF")
calc["C5"] = "=输入页!C2*(1+输入页!C3)"        # 黑色 = 公式
wb.save("./out/模型.xlsx")
```

## 约定（与`audit-xls`保持一致）

- **蓝/黑/绿配色。** 蓝色 = 硬编码输入值，黑色 = 公式，绿色 = 链接至其他工作表/文件。
- **计算单元格中无硬编码。** 每个计算单元格都是公式；所有输入值位于"输入页"工作表。
- **命名范围** —— 为演示文稿或备忘录中引用的任何值设置命名范围。
- **平衡检查。** 包含"检查"工作表，用于钩稽核对（资产负债表平衡、现金流量表与现金钩稽等），并显示TRUE/FALSE。
- **每文件一个模型。** 除非明确要求，否则不要追加到现有工作簿。

## 不使用场景

若`mcp__office__excel_*`工具可用（Cowork插件模式），请使用这些工具——它们可在用户检查点介入的情况下操作实时工作簿。本技能是无界面运行的文件生成备用方案。
