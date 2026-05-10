# SEC 申报文件数据提取参考指南

**适用场景：** 仅当模型模板明确要求从 SEC 申报文件（10-K、10-Q）中提取数据时，才参考此文件。对于直接提供数据或使用其他数据源的模板，无需此参考指南。

---

## 从 SEC 申报文件（10-K / 10-Q）提取数据

在向模型模板中录入上市公司数据时，应直接从 SEC 申报文件中提取财务数据。

### 第一步：定位申报文件

1. 使用 SEC EDGAR 系统：`https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=10-K`
2. 如需季度数据，请使用 `type=10-Q`

### 第二步：识别列报货币

在提取数据之前，请先确认报表的列报货币：
- 查看封面页或页眉中的列报货币说明
- 查看报表标题（例如，“单位：千美元”）
- 查阅附注 1（重要会计政策摘要）

**常见货币符号及代码**

| 标识符 | 货币 |
|-----------|----------|
| $, USD | 美元 |
| €, EUR | 欧元 |
| £, GBP | 英镑 |
| ¥, JPY | 日元 |
| ¥, CNY, RMB | 人民币 |
| CHF | 瑞士法郎 |
| CAD, C$ | 加元 |

将模型货币设置为与申报文件一致，并在“假设（Assumptions）”选项卡中记录。

### 第三步：查阅财务报表

在 10-K 或 10-Q 文件中，定位以下内容：
- **Item 8** (10-K) 或 **Item 1** (10-Q)：财务报表
- 需提取数据的核心板块：
  - 合并营运报表（损益表）/ Consolidated Statements of Operations (Income Statement)
  - 合并资产负债表 / Consolidated Balance Sheets
  - 合并现金流量表 / Consolidated Statements of Cash Flows
  - 财务报表附注 / Notes to Financial Statements（用于查阅明细表细节）

### 第四步：数据提取映射

**损益表（源自合并营运报表）**

| 申报文件科目 (Filing Line Item) | 模型对应科目 (Model Line Item) |
|------------------|-----------------|
| Net revenues / Net sales | 营业收入 (Revenue) |
| Cost of goods sold | 营业成本 (COGS) |
| Selling, general and administrative | 销售及管理费用 (SG&A) |
| Depreciation and amortization | 折旧与摊销 (D&A) |
| Interest expense, net | 利息支出净额 (Interest Expense) |
| Income tax expense | 所得税费用 (Taxes) |
| Net income | 净利润 (Net Income) |

**资产负债表（源自合并资产负债表）**

| 申报文件科目 (Filing Line Item) | 模型对应科目 (Model Line Item) |
|------------------|-----------------|
| Cash and cash equivalents | 现金及现金等价物 (Cash) |
| Accounts receivable, net | 应收账款净额 (AR) |
| Inventories | 存货 (Inventory) |
| Property, plant and equipment, net | 固定资产净额 (PP&E (Net)) |
| Total assets | 总资产 (Total Assets) |
| Accounts payable | 应付账款 (AP) |
| Short-term debt / Current portion of LT debt | 短期债务 (Current Debt) |
| Long-term debt | 长期债务 (LT Debt) |
| Retained earnings | 留存收益 (Retained Earnings) |
| Total stockholders' equity | 股东权益合计 (Total Equity) |

**现金流量表（源自合并现金流量表）**

| 申报文件科目 (Filing Line Item) | 模型对应科目 (Model Line Item) |
|------------------|-----------------|
| Net income | 净利润 (Net Income) |
| Depreciation and amortization | 折旧与摊销 (D&A) |
| Changes in accounts receivable | 应收账款变动 (ΔAR) |
| Changes in inventories | 存货变动 (ΔInventory) |
| Changes in accounts payable | 应付账款变动 (ΔAP) |
| Capital expenditures | 资本开支 (CapEx) |
| Proceeds from issuance of common stock | 发行股票收到的现金 (Equity Issuance) |
| Proceeds from / Repayments of debt | 债务融资活动 (Debt activity) |
| Dividends paid | 已付股利 (Dividends) |

### 第五步：从附注中提取支持性细节

如需获取细分计划表，请查阅财务报表附注：
- **债务附注 (Note: Debt)** → 偿还期限计划、利率、限制性条款
- **固定资产附注 (Note: Property, Plant & Equipment)** → 固定资产原值、累计折旧、使用年限
- **收入附注 (Note: Revenue)** → 板块细分、地理区域细分
- **租赁附注 (Note: Leases)** → 经营租赁与融资租赁义务

### 第六步：历史数据要求

至少提取 3 年的历史数据：
- 10-K 提供 3 年的损益表（IS）和现金流量表（CF），以及 2 年的资产负债表（BS）
- 第三年的资产负债表数据需从前一年的 10-K 中提取
- 如需季度维度的颗粒度，请使用 10-Q 补充数据

### 数据提取核对清单

- 确认列报货币及单位（千、百万）
- 3 年历史损益表
- 3 年历史现金流量表
- 3 年历史资产负债表
- 核对损益表“净利润”= 现金流量表起始“净利润”（逐年核对）
- 核对资产负债表“现金”= 现金流量表期末“现金”（逐年核对）
- 从附注提取债务偿还期限表
- 提取折旧与摊销 (D&A) 细节或折旧年限假设
- 记录任何非经常性/一次性项目以进行规范化调整 (Normalization)

### 常见申报变体处理

| 变体情况 | 处理方法 |
|-----------|---------------|
| D&A 嵌入在营业成本/销售管理费中 | 从现金流量表中提取 D&A 数据 |
| “其他”科目金额重大 | 查阅附注以获取细分明细 |
| 报表重报 (Restatements) | 使用重报后的数字，并在假设中注明 |
| 财年 ≠ 日历年 | 标注财年结束日期（例如：FYE Jan 2025） |
| 非美元列报货币 | 保持模型货币与申报文件一致 |

> **💡 Appendix: 领域知识小贴士**
>
> 欢迎来到华尔街的数据后花园！如果你是第一次接触这些文件，别担心，这里有几个简单的小窍门：
>
> 1.  **10-K 与 10-Q 有什么区别？**
>     可以把 **10-K** 想象成公司的“年度大体检”，内容超级详细，一年一次；而 **10-Q** 则是“季度小测验”，没那么详细，主要是看看近三个月的近况。
> 2.  **“三大表”说的是啥？**
>     *   **资产负债表 (Balance Sheet)**：公司的“资产家底”，看看它有多少钱、欠多少债。
>     *   **损益表 (Income Statement)**：公司的“成绩单”，看看它这段时间卖了多少货，赚了还是亏了。
>     *   **现金流量表 (Cash Flow Statement)**：公司的“钱包流水”，重点看钱到底是从哪儿来的，又花到哪儿去了。
> 3.  **为什么“附注 (Notes)”很重要？**
>     如果三大表是书的“目录”，那么附注就是书的“正文”。很多模糊不清的项目，比如“钱到底欠谁了”、“固定资产还能用几年”，在附注里都有藏宝图式的详细说明。
> 4.  **注意“单位”！**
>     申报文件里经常会写着 "in thousands"（以千为单位）或 "in millions"（以百万为单位）。如果看漏了一个 0，那在模型里可就是天差地别了！
