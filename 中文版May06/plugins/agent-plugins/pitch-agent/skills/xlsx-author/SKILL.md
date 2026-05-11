---
name: xlsx-author
description: 在磁盘上生成.xlsx文件（无界面模式），而不是操作实时Excel工作簿——适用于没有打开Office应用的托管代理会话。
---

# xlsx-author

当运行在**无界面模式**（托管代理/CMA模式）时，且需要将Excel工作簿作为**文件产物**交付，而不是通过 `mcp__office__excel_*` 编辑实时工作簿时，使用此技能。

## 输出约定

- 写入到 `./out/<name>.xlsx`。如果 `./out/` 不存在则创建。
- 在最终消息中返回相对路径，以便编排层可以收集它。

## 如何构建工作簿

编写一个简短的Python脚本并通过Bash运行。使用 `openpyxl`：

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

- **蓝色/黑色/绿色。** 蓝色 = 硬编码输入，黑色 = 公式，绿色 = 链接到另一个工作表/文件。
- **计算单元格中无硬编码。** 每个计算单元格都是公式；每个输入都在Inputs标签页上。
- **命名范围** 用于从演示文稿或备忘录引用的任何值。
- **平衡检查。** 包含一个Checks标签页，用于核对（资产负债表平衡、现金流量与现金匹配等）并显示TRUE/FALSE。
- **每个文件一个模型。** 除非明确要求，否则不要追加到现有工作簿。

## 何时不使用

如果 `mcp__office__excel_*` 工具可用（Cowork插件模式），请改用这些工具——它们通过审查检查点操作用户的实时工作簿。此技能是无界面运行时生成文件的备选方案。

---

## 金融术语解释

### 1. DCF模型（折现现金流模型）

**定义**：DCF（Discounted Cash Flow）模型是一种估值方法，通过将未来现金流折现到当前价值来评估投资或公司的价值。

**核心原理**：
- 货币具有时间价值（今天的1元比未来的1元更有价值）
- 未来现金流需要按适当的折现率折现

**步骤**：
1. 预测未来自由现金流
2. 确定适当的折现率（WACC）
3. 计算终端价值
4. 将所有现金流折现到现值
5. 计算净现值（NPV）

**公式**：
```
DCF价值 = Σ [CF_t / (1 + r)^t] + TV / (1 + r)^n
```
其中：
- CF_t = 第t年的现金流
- r = 折现率
- TV = 终端价值
- n = 预测期数

### 2. 工作簿（Workbook）与工作表（Worksheet）

**定义**：
- **工作簿**：Excel文件本身，包含一个或多个工作表
- **工作表**：工作簿中的单个表格页面

**结构关系**：
```
工作簿 (.xlsx文件)
├── 工作表1 (Sheet1)
├── 工作表2 (Inputs)
├── 工作表3 (DCF)
└── 工作表4 (Checks)
```

**最佳实践**：
- 将输入数据集中在专门的Inputs工作表
- 计算逻辑放在单独的计算工作表
- 验证检查放在Checks工作表

### 3. 命名范围（Named Range）

**定义**：命名范围是为单元格或单元格区域赋予一个描述性名称，便于引用和公式编写。

**创建方法**：
```python
# 在openpyxl中创建命名范围
from openpyxl.workbook.defined_name import DefinedName

defined_name = DefinedName('Revenue', attr_text='Inputs!$C$2')
wb.defined_names.append(defined_name)
```

**优点**：
- 公式更易读（`=Revenue` vs `=Inputs!$C$2`）
- 便于维护和更新
- 减少错误

### 4. 单元格格式约定

**颜色编码系统**：
- **蓝色**：硬编码输入值（手动输入的数据）
- **黑色**：计算公式（由其他单元格派生）
- **绿色**：外部链接（引用其他工作表或文件）

**目的**：
- 提高模型可读性
- 便于审计和调试
- 快速识别数据来源

### 5. WACC（加权平均资本成本）

**定义**：WACC（Weighted Average Cost of Capital）是公司融资的平均成本，考虑了股权和债务的成本。

**计算公式**：
```
WACC = (E/V) × Re + (D/V) × Rd × (1 - Tc)
```
其中：
- E = 股权价值
- D = 债务价值
- V = E + D（总资本）
- Re = 股权成本
- Rd = 债务成本
- Tc = 税率

**用途**：
- 作为DCF模型的折现率
- 评估投资项目的门槛收益率
- 资本预算决策

### 6. 净现值（NPV）

**定义**：NPV（Net Present Value）是将未来现金流折现到当前时点后的总和减去初始投资。

**计算公式**：
```
NPV = Σ [CF_t / (1 + r)^t] - 初始投资
```

**决策规则**：
- NPV > 0：项目可行，增加股东价值
- NPV = 0：项目盈亏平衡
- NPV < 0：项目不可行

### 7. 终端价值（Terminal Value）

**定义**：终端价值是预测期结束后公司的剩余价值。

**计算方法**：
1. **永续增长法**：TV = FCF_n × (1 + g) / (r - g)
2. **退出倍数法**：TV = 最后一年EBITDA × 行业倍数

**关键假设**：
- 增长率（g）通常接近GDP增长率
- 折现率（r）必须大于增长率（g）

### 8. 自由现金流（FCF）

**定义**：自由现金流（Free Cash Flow）是公司在支付运营费用和资本支出后剩余的现金。

**计算公式**：
```
FCF = 经营活动现金流 - 资本支出
```
或
```
FCF = EBIT × (1 - 税率) + 折旧 - 资本支出 - 营运资金变化
```

**重要性**：
- 衡量公司的真实盈利能力
- 用于DCF估值
- 决定分红和回购能力

### 9. 资产负债表平衡检查（Balance Sheet Check）

**定义**：验证资产负债表基本等式是否成立的过程。

**基本等式**：
```
资产 = 负债 + 所有者权益
```

**检查方法**：
```python
# 在Checks工作表中添加平衡检查
ws_checks["A1"] = "Balance Sheet Check"
ws_checks["A2"] = "Total Assets"
ws_checks["B2"] = "=Assets!G50"
ws_checks["A3"] = "Total Liabilities + Equity"
ws_checks["B3"] = "=Liabilities!G50 + Equity!G50"
ws_checks["A4"] = "Balance?"
ws_checks["B4"] = "=IF(B2=B3, TRUE, FALSE)"
```

### 10. 现金流量匹配（Cash Flow Tie-out）

**定义**：验证现金流量表中的期末现金是否与资产负债表中的现金余额一致。

**检查逻辑**：
```
期初现金 + 经营活动现金流 + 投资活动现金流 + 筹资活动现金流 = 期末现金
```

**重要性**：
- 确保财务模型的一致性
- 发现计算错误
- 提高模型可信度