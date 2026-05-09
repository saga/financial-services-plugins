---
name: xlsx-author
description: 在磁盘上生成 .xlsx 文件（无头模式），而不是驱动实时 Excel 工作簿 — 用于没有打开 Office 应用的托管代理会话。
---

# xlsx-author

当运行在**无头模式**（托管代理/CMA模式）且需要将 Excel 工作簿作为**文件制品**交付，而不是通过 `mcp__office__excel_*` 编辑实时工作簿时，使用此技能。

## 输出约定

- 写入 `./out/<name>.xlsx`。如果 `./out/` 不存在则创建。
- 在最终消息中返回相对路径，以便编排层可以收集它。

## 如何构建工作簿

编写一个简短的 Python 脚本并用 Bash 运行。使用 `openpyxl`：

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

## 约定（镜像 `audit-xls`）

- **蓝色/黑色/绿色**。蓝色 = 硬编码输入，黑色 = 公式，绿色 = 链接到另一个工作表/文件。
- **计算单元格中无硬编码**。每个计算单元格都是公式；每个输入都在 Inputs 标签页上。
- **命名范围**用于从演示文稿或备忘录引用的任何值。
- **平衡检查**。包含一个 Checks 标签页，用于核对（资产负债表平衡、现金流量表与现金对账等）并显示 TRUE/FALSE。
- **每个文件一个模型**。除非明确要求，否则不要追加到现有工作簿。

## 何时不使用

如果 `mcp__office__excel_*` 工具可用（Cowork 插件模式），请改用这些工具 — 它们通过审查检查点驱动用户的实时工作簿。此技能是无头运行时生成文件的备用方案。

---

## 金融术语和知识解释

### 1. 无头模式 (Headless Mode)

无头模式是指在没有图形用户界面的环境中运行程序，常用于服务器端自动化任务。

### 2. 托管代理 (Managed Agent)

托管代理是在受控环境中运行的代理，通常用于企业内部部署。

### 3. 文件制品 (File Artifact)

文件制品是流程产生的输出文件，如报告、模型、数据文件等。

### 4. 编排层 (Orchestration Layer)

编排层负责协调多个任务和服务的执行流程。

### 5. openpyxl

openpyxl 是一个用于读写 Excel 2010 xlsx/xlsm/xltx/xltm 文件的 Python 库。

### 6. 命名范围 (Named Ranges)

命名范围是给单元格或单元格区域分配的名称，便于公式引用和代码访问。

### 7. 硬编码 (Hardcoded)

硬编码是指将值直接写在代码或公式中，而不是引用单元格或变量。

### 8. 工作簿 (Workbook)

工作簿是 Excel 文件，包含一个或多个工作表。

### 9. 工作表 (Worksheet)

工作表是工作簿中的单个表格页面。

### 10. 公式 (Formula)

公式是 Excel 中用于计算的表达式，以等号开头。
