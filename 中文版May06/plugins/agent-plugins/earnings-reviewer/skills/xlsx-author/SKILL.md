---
name: xlsx-author
description: 在磁盘上生成.xlsx文件（无头模式），而不是驱动实时Excel工作簿 — 用于没有打开Office应用的托管代理会话。
---

# xlsx-author

当运行**无头**（托管代理 / CMA模式）且需要交付Excel工作簿作为**文件工件**而不是通过`mcp__office__excel_*`编辑实时工作簿时使用此技能。

## 输出契约

- 写入`./out/<name>.xlsx`。如果`./out/`不存在，创建它。
- 在最终消息中返回相对路径，以便编排层可以收集它。

## 如何构建工作簿

编写一个简短的Python脚本并用Bash运行。使用`openpyxl`：

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

- **蓝 / 黑 / 绿。** 蓝色 = 硬编码输入，黑色 = 公式，绿色 = 链接到另一工作表/文件。
- **计算单元格中无硬编码。** 每个计算单元格都是公式；每个输入都放在输入选项卡上。
- **命名范围**用于从演示文稿或备忘录引用的任何值。
- **平衡检查。** 包含检查选项卡，结平（资产负债表平衡、现金流结平等）并显示TRUE/FALSE。
- **每个文件一个模型。** 除非明确要求，否则不要追加到现有工作簿。

## 何时不使用

如果`mcp__office__excel_*`工具可用（Cowork插件模式），请改用它们 — 它们通过审查检查点驱动用户的实时工作簿。本技能是无头运行的文件生成后备方案。

---

## Appendix: 金融背景知识

### 什么是无头模式（Headless Mode）？

无头模式指在没有图形用户界面（GUI）的环境中运行程序。在AI代理上下文中，这意味着：
- 没有打开的Excel应用程序
- 代理生成.xlsx文件而不是直接操作工作簿
- 文件保存在磁盘上供用户稍后打开

### 关键术语解释

**openpyxl**：用于读写Excel 2010+ xlsx/xlsm文件的Python库。

**工作簿（Workbook）**：Excel文件（.xlsx），包含一个或多个工作表。

**工作表（Worksheet）**：工作簿中的单个"标签页"，如"输入"、"DCF"、"资产负债表"等。

**命名范围（Named Range）**：为单元格或区域分配的名称，便于跨工作表引用。例如，将C5命名为"Revenue_2024"，然后可以在任何地方用`=Revenue_2024`引用它。

**检查选项卡（Checks Tab）**：财务模型中包含平衡检查和验证公式的选项卡，通常显示TRUE/FALSE，帮助快速识别错误。

**Cowork插件模式**：在Excel内部运行AI助手，可以直接操作打开的工作簿，实时与用户交互。

**CMA（Claude Managed Agent，Claude托管代理）**：由Claude直接管理和执行的自主代理，通常在无头环境中运行。

**输入选项卡（Inputs Tab）**：专门用于存放所有假设和硬编码输入的工作表，使模型结构清晰，便于敏感性和场景分析。

**颜色约定（Color Convention）**：
- **蓝色**：硬编码输入（用户可更改的假设）
- **黑色**：公式计算结果
- **绿色**：从其他工作表或文件链接的数据

**迭代计算（Iterative Calculation）**：Excel设置，允许循环引用通过多次迭代求解。LBO和三表模型通常需要启用此功能。
