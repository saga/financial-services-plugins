---
name: xlsx-author
description: 在磁盘上生成 .xlsx 文件（无界面模式），而非操作实时 Excel 工作簿 —— 适用于没有打开 Office 应用程序的托管代理 (Managed-agent) 会话。
---

# xlsx-author

当处于**无界面** (headless) 运行环境（托管代理 / CMA 模式），且需要交付 Excel 工作簿作为**文件产物**，而非通过 `mcp__office__excel_*` 编辑实时工作簿时，请使用此技能。

## 输出约定

- 写入到 `./out/<name>.xlsx`。如果 `./out/` 目录不存在，请先创建。
- 在最终消息中返回相对路径，以便编排层 (Orchestration Layer) 进行提取。

## 如何构建工作簿

编写一段短 Python 脚本并通过 Bash 运行。使用 `openpyxl`：

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

## 遵循惯例（参考 `audit-xls`）

- **蓝 / 黑 / 绿。** 蓝色 = 硬编码输入 (Hardcoded input)，黑色 = 公式 (Formula)，绿色 = 链接至其他工作表或文件。
- **计算单元格禁止硬编码。** 每一个计算单元格都必须是公式；所有输入变量应统一存放于 "Inputs" 标签页中。
- **命名区域 (Named ranges)。** 对于任何被 PPT 演示文稿或备忘录引用的数值，请务必定义命名区域。
- **平衡检查 (Balance checks)。** 包含一个 "Checks" 仪表盘标签页，用于进行勾稽检查（如资产负债表是否配平、现金流量表净增加额与资产负债表货币资金变动是否一致等），并清晰显示 TRUE/FALSE。
- **一档一模型。** 除非明确要求，否则不要向现有的工作簿追加内容。

## 何时**不**适用

如果 `mcp__office__excel_*` 相关工具可用（即 Cowork 插件模式），请优先使用这些工具 —— 它们可以直接驱动用户的实时工作簿并附带审核检查点。本技能仅作为无界面运行模式下生成文件的备选方案。

> **💡 Appendix: 领域知识小贴士**
>
> 1. **DCF (折现现金流)**：这是金融世界的“终极价值标尺”。简单来说，它就像是在预测一家公司未来能赚到的每一分钱，然后把这些未来的钱按照一定的“折扣率”折算成现在的价值。如果算出来的总数比现在的股价高，那这门生意可能就很划算。
> 2. **颜色编码 (Blue/Black/Green)**：在职业金融建模中，颜色就是程序员的语标。蓝色代表“手动输入的死数”，黑色代表“电脑计算的变数”。如果不小心在黑色区域手动改了一个数（硬编码），就像在钟表齿轮里塞了一粒沙子，整个模型的逻辑就会断裂。
> 3. **勾稽检查 (Balance Checks)**：这就是会计界的“对暗号”。资产负债表必须左右相等（资产=负债+所有者权益），三张表之间就像连环扣一样互相制约。在 Excel 里做一个 Checks 页面，是为了在模型出错的第一时间报警，确保你的金融分析不是海市蜃楼。
