# 连接器

本插件连接至 **LFA MCP 服务器**，该服务器提供了来自伦敦证券交易所集团（LSEG）的金融分析工具。所有工具均由单一 MCP 服务器提供，无需额外连接器。

## 命令如何引用工具

本插件中的命令通过精确的工具名称（例如 `bond_price`、`interest_rate_curve`）引用 MCP 工具。为了清晰起见，这些工具被划分为以下类别：

## 工具类别

| 类别 | 占位符 | 工具 | 描述 |
|----------|-------------|-------|-------------|
| 债券定价 | `~~bond-pricing` | `bond_price`, `bond_future_price` | 提供全面的分析工具，为债券及债券期货进行定价 |
| 外汇定价 | `~~fx-pricing` | `fx_spot_price`, `fx_forward_price` | 外汇即期及远期汇率定价 |
| 利率曲线 | `~~ir-curves` | `interest_rate_curve`, `inflation_curve` | 政府收益率曲线及通胀盈亏平衡率 |
| 信用曲线 | `~~credit-curves` | `credit_curve` | 按发行人类型划分的信用利差曲线 |
| 外汇曲线 | `~~fx-curves` | `fx_forward_curve` | 外汇远期点数曲线 |
| 期权 | `~~options` | `option_value`, `option_template_list` | 包含希腊字母（Greeks）的期权估值 |
| 掉期（互换） | `~~swaps` | `ir_swap` | 利率掉期定价 |
| 波动率曲面 | `~~volatility` | `fx_vol_surface`, `equity_vol_surface` | 外汇及股票隐含波动率曲面 |
| 量化分析 | `~~qa` | `qa_ibes_consensus`, `qa_company_fundamentals`, `qa_historical_equity_price`, `qa_macroeconomic` | 分析师预期、基本面、价格及宏观数据 |
| 时间序列 | `~~time-series` | `tscc_historical_pricing_summaries` | 历史价格摘要（日间/日内） |
| 固定收益分析 | `~~yieldbook` | `yieldbook_bond_reference`, `yieldbook_cashflow`, `yieldbook_scenario`, `fixed_income_risk_analytics` | 债券参考数据、现金流、情景分析、OAS/久期 |

## 完整工具参考

### 债券领域
- **`bond_price`** — 计算债券定价、估值及分析指标。支持 ISIN、RIC、CUSIP 或 AssetId。返回收益率（Yield）、久期（Duration）、凸性（Convexity）、DV01（利率变动基点价值）、应计利息。支持通过价格/收益率覆盖进行假设情景（What-if）分析。
- **`bond_future_price`** — 计算债券期货定价及分析指标。返回公允价值、最便宜可交割券（CTD）识别、交割篮子、转换因子以及合约 DV01。

### 外汇领域
- **`fx_spot_price`** — ISO 货币对的外汇即期汇率定价。返回中间价/买入价/卖出价。
- **`fx_forward_price`** — 特定期限或日期的外汇远期汇率定价。返回远期点数、直接汇率以及展期收益（Carry）。

### 曲线领域
- **`interest_rate_curve`** — 政府收益率曲线。分为两个阶段：列出可用曲线，随后计算曲线点。返回平价/零息利率、折现因子、远期利率。
- **`credit_curve`** — 信用利差曲线。按国家和发行人类型（企业、主权、机构债等）搜索，随后计算利差期限结构。
- **`inflation_curve`** — 通胀盈亏平衡曲线。按国家/货币搜索，随后计算盈亏平衡率和实际收益率。
- **`fx_forward_curve`** — 外汇远期点数曲线。列出曲线，随后计算所有标准期限的远期点数。

### 掉期领域
- **`ir_swap`** — 利率掉期定价。分为两个阶段：按货币/指数列出模板，随后对指定期限的掉期进行定价。返回平价利率、DV01、净现值（NPV）。

### 期权领域
- **`option_value`** — 支持欧式（标准）、障碍、二元和亚式期权的估值。返回期权费（Premium）、完整的希腊字母（Delta, Gamma, Vega, Theta, Rho）以及风险指标。
- **`option_template_list`** — 列出可供定价使用的期权模板。

### 波动率领域
- **`fx_vol_surface`** — 使用 SABR 模型生成外汇波动率曲面。返回各期限及 Delta 档位的波动率曲面。
- **`equity_vol_surface`** — 股票隐含波动率曲面。支持通过 RIC 查询股票/指数，通过 RICROOT 查询期货。

### 量化分析领域
- **`qa_ibes_consensus`** — IBES 分析师共识预期（EPS、营收、EBITDA、DPS）。提供包含分析师统计数量、离散度以及最高/最低范围的前瞻性预测。
- **`qa_company_fundamentals`** — 已公布的公司财务数据（利润表、资产负债表指标）。历史财年数据。
- **`qa_historical_equity_price`** — 包含 OHLCV（开高低收量）、总回报和 Beta 系数的历史股票价格。
- **`qa_macroeconomic`** — 宏观经济指标数据库。按助记符或描述搜索，检索最新数值或时间序列。

### 时间序列领域
- **`tscc_historical_pricing_summaries`** — 任何 RIC 代码的历史价格摘要。支持日间（日、周、月）和日内（1分钟至1小时）间隔。

### 固定收益分析 (YieldBook) 领域
- **`yieldbook_bond_reference`** — 债券参考数据：证券类型、行业、评级、票息、到期日、发行人。
- **`yieldbook_cashflow`** — 债券现金流预测：未来的票息和本金支付计划。
- **`yieldbook_scenario`** — 债券情景分析：平行利率漂移下的价格/收益率变动。
- **`fixed_income_risk_analytics`** — 债券风险分析：期权调整利差（OAS）、有效久期、关键利率久期、凸性。

> **💡 Appendix: 领域知识小贴士**
>
> **1. 什么是收益率曲线 (Yield Curve)？**
> 把它想象成一张“借钱的价目表”。它展示了在同一时间点，借钱期限的长短与利息高低之间的关系。通常借钱时间越长利息越高，但如果曲线变平甚至“倒挂”，通常是市场在预警经济可能要出问题了。
>
> **2. 期权里的希腊字母 (Greeks) 有什么用？**
> 它们是期权投资者的“驾驶仪表盘”。比如 **Delta** 告诉你标的价格变动时你的期权价值会跟跳多少；**Vega** 衡量的是市场“情绪”波动（波动率）对期权价格的影响。掌握了它们，你就能精准把控风险。
>
> **3. 为什么债券分析总提到久期 (Duration) 和凸性 (Convexity)？**
> 久期衡量的是债价对利率波动的“敏感程度”——利率升 1%，债价跌多少。而凸性则是久期的“高级修正版”，因为债价和利率的关系并不是一条直线而是一条弧线。凸性越好，利率下降时债价涨得更快，利率上升时跌得更慢，是债券的“护身符”。
>
> **4. IBES 共识 (Consensus) 为什么重要？**
> 投资讲究“群众的眼睛是雪亮的”。IBES 汇总了成百上千位顶尖分析师对公司业绩（如利润 EPS）的预测。如果公司实际交出的成绩单超过了这个“共识”，股价往往会迎来惊喜上涨。
>
> **5. 常用证券识别码简述：**
> - **ISIN**: 证券的“国际身份证号”。
> - **RIC**: 路透社专门给金融产品起的“昵称”，方便在终端直接搜到。
> - **CUSIP**: 主要是北美地区使用的证券识别代码。
