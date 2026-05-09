# 连接器

本插件连接到 **LFA MCP Server**，该服务器提供 LSEG（伦敦证券交易所集团）的金融分析工具。所有工具均由单一的 MCP 服务器提供，无需额外的连接器。

## 命令如何引用工具

本插件中的命令按其确切的工具名称引用 MCP 工具（例如 `bond_price`、`interest_rate_curve`）。为清晰起见，工具按以下类别组织：

## 工具分类

| 类别 | 占位符 | 工具 | 说明 |
|------|--------|------|------|
| 债券定价 | `~~bond-pricing` | `bond_price`、`bond_future_price` | 含完整分析功能的债券和期货定价 |
| 外汇定价 | `~~fx-pricing` | `fx_spot_price`、`fx_forward_price` | 外汇即期和远期汇率定价 |
| 利率曲线 | `~~ir-curves` | `interest_rate_curve`、`inflation_curve` | 国债收益率曲线和通胀盈亏平衡率 |
| 信用曲线 | `~~credit-curves` | `credit_curve` | 按发行人类型的信用利差曲线 |
| 外汇曲线 | `~~fx-curves` | `fx_forward_curve` | 外汇远期点数曲线 |
| 期权 | `~~options` | `option_value`、`option_template_list` | 含希腊字母的期权估值 |
| 互换 | `~~swaps` | `ir_swap` | 利率互换定价 |
| 波动率曲面 | `~~volatility` | `fx_vol_surface`、`equity_vol_surface` | 外汇和股票隐含波动率曲面 |
| 量化分析 | `~~qa` | `qa_ibes_consensus`、`qa_company_fundamentals`、`qa_historical_equity_price`、`qa_macroeconomic` | 分析师预测、基本面、股价、宏观数据 |
| 时间序列 | `~~time-series` | `tscc_historical_pricing_summaries` | 历史价格汇总（日间/日内） |
| 固收分析 | `~~yieldbook` | `yieldbook_bond_reference`、`yieldbook_cashflow`、`yieldbook_scenario`、`fixed_income_risk_analytics` | 债券参考数据、现金流、情景分析、OAS/久期 |

## 完整工具参考

### 债券域
- **`bond_price`** — 计算债券定价、估值和分析。接受 ISIN、RIC、CUSIP 或 AssetId。返回收益率、久期、凸性、DV01、应计利息。支持通过价格/收益率覆盖进行假设情景分析。
- **`bond_future_price`** — 计算债券期货定价和分析。返回公允价值、最便宜可交割债券识别、交割篮子、转换因子和合约 DV01。

### 外汇域
- **`fx_spot_price`** — ISO 货币对的外汇即期汇率定价。返回中间价/买价/卖价。
- **`fx_forward_price`** — 特定期限或日期的外汇远期汇率定价。返回远期点数、远期全价和利差。

### 曲线域
- **`interest_rate_curve`** — 国债收益率曲线。两阶段：列出可用曲线，然后计算曲线点。返回平价/零息利率、贴现因子、远期利率。
- **`credit_curve`** — 信用利差曲线。按国家和发行人类型（企业、主权、机构等）搜索，然后计算利差期限结构。
- **`inflation_curve`** — 通胀盈亏平衡曲线。按国家/货币搜索，然后计算盈亏平衡利率和实际收益率。
- **`fx_forward_curve`** — 外汇远期点数曲线。列出曲线，然后计算所有标准期限的远期点数。

### 互换域
- **`ir_swap`** — 利率互换定价。两阶段：按货币/指数列出模板，然后在指定期限定价互换。返回平价利率、DV01、NPV。

### 期权域
- **`option_value`** — 期权估值，支持普通、障碍、二元和亚式期权。返回权利金、全部希腊字母（delta、gamma、vega、theta、rho）和风险指标。
- **`option_template_list`** — 列出可用于定价的期权模板。

### 波动率域
- **`fx_vol_surface`** — 使用 SABR 模型生成外汇波动率曲面。返回各期限和 delta 行权价的波动率曲面。
- **`equity_vol_surface`** — 股票隐含波动率曲面。支持通过 RIC 查询股票/指数，通过 RICROOT 查询期货。

### 量化分析域
- **`qa_ibes_consensus`** — IBES 分析师一致预期（EPS、收入、EBITDA、DPS）。前瞻性预测，含分析师数量、离散度和最高/最低范围。
- **`qa_company_fundamentals`** — 已报告的公司财务数据（利润表、资产负债表指标）。历史财年数据。
- **`qa_historical_equity_price`** — 历史股价，含 OHLCV、总回报和 Beta。
- **`qa_macroeconomic`** — 宏观经济指标数据库。通过助记符或描述搜索，获取最新值或时间序列。

### 时间序列域
- **`tscc_historical_pricing_summaries`** — 任意 RIC 的历史价格汇总。支持日间（日、周、月）和日内（1分钟到1小时）间隔。

### 固收分析（YieldBook）域
- **`yieldbook_bond_reference`** — 债券参考数据：证券类型、行业、评级、票息、到期日、发行人。
- **`yieldbook_cashflow`** — 债券现金流预测：未来票息和本金支付时间表。
- **`yieldbook_scenario`** — 债券情景分析：在平行利率变动下的价格/收益率。
- **`fixed_income_risk_analytics`** — 债券风险分析：OAS、有效久期、关键利率久期、凸性。

---

## 📖 本篇金融知识小贴士

**RIC（Reuters Instrument Code）**：路透金融代码，标识特定金融产品的标准代码。如 AAPL.OQ 代表苹果在纳斯达克的股票。

**ISIN（International Securities Identification Number）**：国际证券识别码，全球唯一的证券标识码。每只债券、股票都有唯一的 ISIN。

**CUSIP**：北美证券识别码，美国和加拿大证券的 9 位标识码。

**OHLCV**：Open（开盘价）、High（最高价）、Low（最低价）、Close（收盘价）、Volume（成交量）的缩写。技术分析的基础数据。

**Beta（贝塔系数）**：衡量股票相对于大盘的波动程度。Beta=1 表示跟大盘同步，Beta=1.5 表示大盘涨1%时它平均涨1.5%。

**NPV（净现值，Net Present Value）**：未来所有现金流的现值总和减去初始投资。大于0说明项目值得投。

**SABR 模型**：一种广泛使用的波动率模型，用于拟合和预测期权波动率曲面的形状。

**OAS（期权调整利差）**：将债券中嵌入的期权价值剥离后，债券相对于无风险利率的真实利差。

**关键利率久期（Key Rate Duration）**：将久期拆解到不同期限（如2年、5年、10年），精确衡量各期限利率变动对债券价格的影响。
