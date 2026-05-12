# SEC 备案文件数据提取指南

**适用场景：** 仅在模型模板明确要求从 SEC 备案文件（10-K、10-Q）中提取数据时参考此文件。如果模板直接提供数据或使用其他数据源，则无需阅读此参考指南。

---

## 从 SEC 备案文件 (10-K / 10-Q) 中提取数据

在利用上市公司数据填充模型模板时，需直接从其 SEC 备案文件中提取财务数据。

### 步骤 1：定位备案文件

1. 使用 SEC EDGAR 系统：`https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=10-K`
2. 提取季度数据时，请在 `type` 栏搜索 `10-Q`。

### 步骤 2：识别报表货币

在提取数据之前，必须确认报表所使用的货币：
- 查看首页（封面页）或页眉处注明的列报货币。
- 观察报表表头（例如，“单位：千美元”）。
- 审阅“附注 1”（重要会计政策摘要）。

**常见货币指标**

| 指标/符号 | 货币 |
|-----------|----------|
| $, USD | 美元 |
| €, EUR | 欧元 |
| £, GBP | 英镑 |
| ¥, JPY | 日元 |
| ¥, CNY, RMB | 人民币 |
| CHF | 瑞士法郎 |
| CAD, C$ | 加拿大元 |

将模型货币设置为与备案文件保持一致；并在“假设 (Assumptions)”选项卡中进行记录。

### 步骤 3：导航至财务报表

在 10-K 或 10-Q 文件中，定位以下项目：
- **第 8 项 (Item 8)** (10-K) 或 **第 1 项 (Item 1)** (10-Q)：财务状况及财务报表 (Financial Statements)
- 需提取的主要部分：
  - 合并营运报表 (Consolidated Statements of Operations，即损益表)
  - 合并资产负债表 (Consolidated Balance Sheets)
  - 合并现金流量表 (Consolidated Statements of Cash Flows)
  - 财务报表附注 (Notes to Financial Statements，用于获取明细表单细节)

### 步骤 4：数据提取映射

**损益表（源自合并营运报表）**

| 备案文件科目 | 模型科目 |
|------------------|-----------------|
| Net revenues / Net sales (净营收 / 净销售额) | Revenue (收入) |
| Cost of goods sold (销售成本) | COGS (销货成本) |
| Selling, general and administrative (销售、一般及行政费用) | SG&A (销售及管理费用) |
| Depreciation and amortization (折旧与摊销) | D&A (折旧与摊销) |
| Interest expense, net (利息支出净额) | Interest Expense (利息支出) |
| Income tax expense (所得税费用) | Taxes (税项) |
| Net income (净利润) | Net Income (净利润) |

**资产负债表（源自合并资产负债表）**

| 备案文件科目 | 模型科目 |
|------------------|-----------------|
| Cash and cash equivalents (现金及现金等价物) | Cash (现金) |
| Accounts receivable, net (应收账款净额) | AR (应收账款) |
| Inventories (存货) | Inventory (存货) |
| Property, plant and equipment, net (物业、厂房及设备净额) | PP&E (Net) (固定资产净额) |
| Total assets (总资产) | Total Assets (总资产) |
| Accounts payable (应付账款) | AP (应付账款) |
| Short-term debt / Current portion of LT debt (短期债务 / 一年内到期的长期债务) | Current Debt (短期债务) |
| Long-term debt (长期债务) | LT Debt (长期债务) |
| Retained earnings (留存收益) | Retained Earnings (留存收益) |
| Total stockholders' equity (股东权益合计) | Total Equity (权益合计) |

**现金流量表（源自合并现金流量表）**

| 备案文件科目 | 模型科目 |
|------------------|-----------------|
| Net income (净利润) | Net Income (净利润) |
| Depreciation and amortization (折旧与摊销) | D&A (折旧与摊销) |
| Changes in accounts receivable (应收账款变动) | ΔAR (应收账款变动) |
| Changes in inventories (存货变动) | ΔInventory (存货变动) |
| Changes in accounts payable (应付账款变动) | ΔAP (应付账款变动) |
| Capital expenditures (资本支出) | CapEx (资本开支) |
| Proceeds from issuance of common stock (发行普通股收到的现金) | Equity Issuance (股权发行) |
| Proceeds from / Repayments of debt (债务筹资 / 偿还活动) | Debt activity (债务活动) |
| Dividends paid (支付股利) | Dividends (股息) |

### 步骤 5：从附注中提取支持细节

对于细分表单，请从财务报表附注中溯源：
- **附注：债务 (Debt)** → 偿债计划表、利率、债务契约
- **附注：物业、厂房及设备 (
