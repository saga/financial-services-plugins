# SEC报表数据提取参考指南

**使用场景：** 仅当模型模板明确要求从SEC报表（10-K, 10-Q）中提取数据时参考此文件。对于直接提供数据或使用其他数据源的模板，无需参考此指南。

---

## 从SEC报表（10-K / 10-Q）中提取数据

在将上市公司数据录入模型模板时，应直接从SEC报表中提取财务数据。

### 第一步：定位报表

1. 使用 SEC EDGAR 系统：`https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[TICKER]&type=10-K`
2. 如需季度数据，请搜索 `type=10-Q`

### 第二步：识别报表货币单位

在提取数据之前，必须确认报告货币：
- 检查封面或页眉中的报告货币信息。
- 查看报表标题（例如，“单位：千美元”）。
- 审阅附注1（重要会计政策摘要）。

**常见货币标识**

| 标识 | 货币 |
|-----------|----------|
| $, USD | 美元 |
| €, EUR | 欧元 |
| £, GBP | 英镑 |
| ¥, JPY | 日元 |
| ¥, CNY, RMB | 人民币 |
| CHF | 瑞士法郎 |
| CAD, C$ | 加元 |

设置模型货币以匹配报表，并在“假设（Assumptions）”页签中记录。

### 第三步：导航至财务报表

在10-K或10-Q中，定位以下部分：
- **第8项 (Item 8)** (10-K) 或 **第1项 (Item 1)** (10-Q)：财务报表
- 需提取的核心报表：
  - 合并利润表 / 损益表 (Consolidated Statements of Operations / Income Statement)
  - 合并资产负债表 (Consolidated Balance Sheets)
  - 合并现金流量表 (Consolidated Statements of Cash Flows)
  - 财务报表附注 (Notes to Financial Statements，用于获取明细表细节)

### 第四步：数据提取映射

**利润表（源自合并利润表）**

| 报表行项目 | 模型行项目 |
|------------------|-----------------|
| 净收入 / 净销售额 (Net revenues / Net sales) | 营收 (Revenue) |
| 销货成本 (Cost of goods sold) | COGS |
| 销售、一般及行政费用 (Selling, general and administrative) | SG&A |
| 折旧与摊销 (Depreciation and amortization) | D&A |
| 利息费用净额 (Interest expense, net) | 利息费用 (Interest Expense) |
| 所得税费用 (Income tax expense) | 税收 (Taxes) |
| 净利润 (Net income) | 净利润 (Net Income) |

**资产负债表（源自合并资产负债表）**

| 报表行项目 | 模型行项目 |
|------------------|-----------------|
| 现金及现金等价物 (Cash and cash equivalents) | 现金 (Cash) |
| 应收账款净额 (Accounts receivable, net) | AR |
| 存货 (Inventories) | 存货 (Inventory) |
| 不动产、厂房及设备净额 (Property, plant and equipment, net) | PP&E（净额） |
| 总资产 (Total assets) | 总资产 |
| 应付账款 (Accounts payable) | AP |
| 短期债务 / 长期债务的流动部分 (Short-term debt / Current portion of LT debt) | 流动债务 |
| 长期债务 (Long-term debt) | 长期债务 (LT Debt) |
| 留存收益 (Retained earnings) | 留存收益 |
| 股东权益总额 (Total stockholders' equity) | 总权益 |

**现金流量表（源自合并现金流量表）**

| 报表行项目 | 模型行项目 |
|------------------|-----------------|
| 净利润 (Net income) | 净利润 (Net Income) |
| 折旧与摊销 (Depreciation and amortization) | D&A |
| 应收账款变动 (Changes in accounts receivable) | ΔAR |
| 存货变动 (Changes in inventories) | ΔInventory |
| 应付账款变动 (Changes in accounts payable) | ΔAP |
| 资本支出 (Capital expenditures) | 资本支出 (CapEx) |
| 发行普通股收到的现金 (Proceeds from issuance of common stock) | 股权融资 |
| 债务的取得 / 归还 (Proceeds from / Repayments of debt) | 债务活动 |
| 已支付股利 (Dividends paid) | 股利 (Dividends) |

### 第五步：从附注中提取辅助细节

对于相关细分表，请从财务报表附注中提取：
- **附注：债务 (Debt)** → 到期计划、利率、限制性条款
- **附注：不动产、厂房及设备 (PP&E)** → 固定资产原值、累计折旧、使用年限
- **附注：收入 (Revenue)** → 业务板块拆解、地理区域分布
- **附注：租赁 (Leases)** → 经营租赁与融资租赁义务

### 第六步：历史数据要求

提取至少3年的历史数据：
- 10-K通常提供3年的利润表/现金流量表数据，以及2年的资产负债表数据。
- 如需第3年的资产负债表数据，请查阅前一年度的10-K。
- 如有需要，可使用10-Q填补季度级别的颗粒度。

### 数据提取检查表

- 确认报告货币及计量单位（千、百万）。
- 提取连续3年的历史利润表。
- 提取连续3年的历史现金流量表。
- 提取连续3年的历史资产负债表。
- 验证：利润表的净利润 = 现金流量表起点的净利润（每年核对）。
- 验证：资产负债表的现金 = 现金流量表的期末现金（每年核对）。
- 从附注中提取债务到期计划表。
- 提取折旧与摊销（D&A）明细或折旧年限假设。
- 记录并剔除任何非经常性/一次性项目以进行“规范化（Normalization）”。

### 常见报表差异处理

| 差异情况 | 处理方法 |
|-----------|---------------|
| D&A 嵌入在销货成本/管理费用中 | 从现金流量表中提取 D&A 金额 |
| “其他”行项目金额重大 | 检查附注中的明细拆解 |
| 报表重述 (Restatements) | 使用重述后的新数据，并在假设中注明 |
| 财年 ≠ 日历年 | 标注财年截止日期（例如：FYE 2025年1月） |
| 非美元报告货币 | 调整模型货币以匹配原始报表 |

> **💡 Appendix: 领域知识小贴士**
>
> 欢迎来到华尔街的“数据藏宝图”世界！如果你是第一次接触这些名词，别担心，我们用大白话来拆解一下：
>
> 1. **SEC 与 EDGAR 是什么？**
>    SEC 就是“美国证监会”，它是证券市场的警察。EDGAR 是他们家的“超级图书馆”，所有在美国上市的公司都必须把他们的账本（报表）公开透明地存在这里供全球股民查阅。
>
> 2. **10-K 和 10-Q 的
