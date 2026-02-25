# SEC 申报文件数据提取指南

**使用场景：** 仅当模型模板明确要求从 SEC 申报文件（10-K, 10-Q）中提取数据时参考。若数据已直接提供或来自其他数据源，则无需此指南。

---

## 提取步骤

### 第一步：定位文件
1. 访问 SEC EDGAR 搜索公司代码。
2. `10-K` 用于年度数据，`10-Q` 用于季度数据。

### 第二步：确认报表币种与单位
- 查看封面或报表表头（例如："In thousands of U.S. dollars"）。
- 确认单位是千位、百万位还是原值。

### 第三步：导航至财务报表
在 10-K 中查找 **Item 8**，在 10-Q 中查找 **Item 1**。

### 第四步：科目映射表

**利润表 (Consolidated Statements of Operations)**
| 申报文件科目 | 模型对应科目 |
|--------------|--------------|
| Net revenues / Net sales | 营业收入 |
| Cost of goods sold | 营业成本 (COGS) |
| Selling, general and administrative | 销售及管理费用 (SG&A) |
| Depreciation and amortization | 折旧与摊销 (D&A) |
| Net income | 净利润 |

**资产负债表 (Consolidated Balance Sheets)**
| 申报文件科目 | 模型对应科目 |
|--------------|--------------|
| Cash and cash equivalents | 货币资金/现金 |
| Accounts receivable, net | 应收账款 |
| Inventories | 存货 |
| Total assets | 资产总计 |
| Total stockholders' equity | 股东权益合计 |

**现金流量表 (Consolidated Statements of Cash Flows)**
| 申报文件科目 | 模型对应科目 |
|--------------|--------------|
| Net income | 净利润 |
| Changes in accounts receivable | 应收账款变动 (ΔAR) |
| Capital expenditures | 资本开支 (CapEx) |
| Dividends paid | 已付股利 |

### 第五步：从附注中提取明细
- **债务附注 (Note: Debt)**：提取到期计划、利率和契约条款。
- **固定资产附注 (Note: PP&E)**：提取原值、累计折旧和折旧年限。

### 历史数据要求
- 至少提取 3 年历史数据。10-K 通常提供 3 年利润表/现金流量表，但仅有 2 年资产负债表。第 3 年的资产负债表需查阅前一年的 10-K。
