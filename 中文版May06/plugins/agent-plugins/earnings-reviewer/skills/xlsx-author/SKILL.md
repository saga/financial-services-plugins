---
name: xlsx-author
description: 在磁盘上生成一个.xlsx文件（无头模式），而不是驱动实时Excel工作簿 — 适用于没有打开Office应用程序的托管代理会话。
---

# xlsx-author

当运行**无头模式**（托管代理/CMA模式）且需要将Excel工作簿作为**文件制品**交付，而不是通过`mcp__office__excel_*`编辑实时工作簿时，使用此技能。

## 输出约定

- 写入 `./out/<name>.xlsx`。如果 `./out/` 不存在则创建。
- 在最终消息中返回相对路径，以便编排层可以收集它。

## 如何构建工作簿

编写一个简短的Python脚本并使用Bash运行。使用`openpyxl`库：

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

## 约定（镜像`audit-xls`）

- **蓝色/黑色/绿色。** 蓝色 = 硬编码输入，黑色 = 公式，绿色 = 链接到另一个工作表/文件。
- **计算单元格中无硬编码。** 每个计算单元格都是一个公式；每个输入都在Inputs标签上。
- **命名范围**用于从演示文稿或备忘录引用的任何值。
- **平衡检查。** 包含一个检查标签，用于核对（资产负债表平衡、现金流与现金匹配等）并显示TRUE/FALSE。
- **每个文件一个模型。** 除非明确要求，否则不要附加到现有工作簿。

## 何时不使用

如果`mcp__office__excel_*`工具可用（Cowork插件模式），请改用这些工具 — 它们驱动用户的实时工作簿并带有审核检查点。此技能是无头运行时生成文件的备选方案。

---

## 金融术语和知识解释

### 1. 无头模式 (Headless Mode)

无头模式是指在没有图形用户界面(GUI)的情况下运行软件程序。在金融领域，这常用于：
- 自动化报表生成
- 批量处理财务数据
- 服务器端模型计算

### 2. Excel工作簿结构 (Excel Workbook Structure)

典型的财务模型工作簿通常包含以下标签：
- **Inputs（输入）**：所有假设和硬编码值
- **计算表**：DCF、LBO、三表联动等模型计算
- **输出/报告**：汇总表格和图表
- **检查**：验证模型完整性的平衡检查

### 3. 硬编码 vs 公式 (Hardcode vs Formula)

- **硬编码(Hardcode)**：直接输入的固定值（如假设的增长率）
- **公式(Formula)**：基于其他单元格计算得出的值

良好的财务模型实践是将所有输入集中在Inputs标签，计算使用公式引用这些输入。

### 4. 命名范围 (Named Ranges)

命名范围是给单元格或单元格区域分配一个描述性名称，便于在公式和其他地方引用。例如，将包含"Revenue"的单元格命名为"Revenue_2024"。

### 5. 模型完整性检查 (Model Integrity Checks)

在财务模型中加入检查机制来验证：
- 资产负债表是否平衡
- 现金流量表是否与资产负债表现金匹配
- 关键计算是否正确

### 6. openpyxl

openpyxl是一个Python库，用于读取和写入Excel 2010+ .xlsx文件。它允许程序员通过代码创建、修改和保存Excel文件。

### 7. 编排层 (Orchestration Layer)

编排层是协调多个工具和服务执行的系统，负责：
- 管理工作流程
- 收集输出文件
- 处理错误和重试

### 8. 文件制品 (File Artifact)

文件制品是流程或任务的输出文件，如Excel模型、PDF报告、CSV数据文件等。

### 9. 托管代理 (Managed Agent)

托管代理是在受控环境中运行的自动化代理，通常用于企业环境中的自动化任务。

### 10. 财务模型最佳实践 (Financial Modeling Best Practices)

良好的财务模型应具备：
- 清晰的输入/计算分离
- 一致的颜色编码
- 完整性检查
- 文档说明
- 可审计的计算路径
