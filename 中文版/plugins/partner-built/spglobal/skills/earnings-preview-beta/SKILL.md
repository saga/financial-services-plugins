---
name: earnings-preview-single
description: 为单个公司生成一份简洁的 4-5 页股票研究财报预览报告。分析最新财报电话会议记录、竞争格局、估值和近期新闻，生成专业的 HTML 报告。
---

# 单公司财报预览

为单个公司生成一份简洁、专业的股票研究财报预览报告。输出是一个自包含的 HTML 文件，目标为 4-5 打印页。报告内容密集，包含大量数据和图表，叙述简洁直接。

**数据来源（零例外）**：唯一允许的数据来源是 **Kensho Grounding MCP** (`search`) 和 **S&P Global MCP** (`kfinance`)。绝对不允许使用任何其他工具、数据源或任何形式的网络访问。具体而言：
- 不要使用 `WebSearch`、`WebFetch`、`web_search`、`brave_search`、`google_search` 或任何通用网络/互联网搜索工具——即使 Kensho 速度慢、没有返回结果或暂时不可用。
- 不要使用任何浏览器、URL 获取或网页抓取工具。
- 如果 Kensho Grounding 对某个查询没有返回结果，请尝试重新表述查询或在报告中注明"数据不可用"。**绝不使用网络搜索作为替代方案。**
- 报告中的每一条信息都必须能够追溯到 `kfinance` MCP 函数调用或 Kensho `search` 调用。如果无法追溯到这两者之一，则不得出现在报告中。

**关键规则**：您必须在撰写报告的任何部分**之前**完成所有研究和数据收集（阶段 1-5）。

**中间文件规则**：来自 MCP 工具调用的所有原始数据必须在**每次工具调用返回后立即**写入 `/tmp/earnings-preview/` 目录中的文件——然后再进行下一次调用。这可以保护数据免受上下文窗口压缩的影响。不要只在内存中保存数据。在阶段 1 开始时，运行 `mkdir -p /tmp/earnings-preview` 创建目录。**在生成 HTML 报告（阶段 7）之前，您必须使用 `cat` 命令将所有中间文件读回上下文。这些文件——而不是您对早期对话的记忆——是报告中每个数字、引用和源 URL 的唯一真实来源。如果跳过读取文件，报告**将会**包含错误。**

**财季规则**：切勿从日历报告日期推断财季。许多公司的财年不是标准的（例如，沃尔玛的财年末为 1 月 31 日，因此 2026 年 2 月的报告涵盖的是 FY2026 第四季度，而不是 2025 年第四季度或 2026 年第一季度）。始终使用 `get_next_earnings_from_identifiers` 或 `get_earnings_from_identifiers` 返回的财报电话会议名称中所示的确切财季和财年（例如，"Walmart Q4 FY2026 Earnings Call" 表示季度为 Q4 FY2026）。在报告标题、页眉、表格和所有引用中逐字使用该名称。如果会议名称不明确，请与 `get_financial_line_item_from_identifiers` 期间标签进行交叉引用。

**长度规则**：报告必须简洁。目标为打印时 4-5 页。不要写长的多段落叙述。使用简洁有力的项目符号。每个句子都必须有其存在的价值。如果能用更少的词表达，就用更少的词。

**逐字引用规则**：在 `<blockquote>` 标签中引用管理层发言时，文本必须**完全**从会议记录中复制——逐字逐句，包括填充词和句子片段。不要释义、重新排列、合并来自会议记录不同部分的句子，或"清理"引用。如果在会议记录中找不到确切的短语，请勿将其作为直接引用呈现。相反，用您自己的叙述声音释义，不使用块引用格式（例如，"管理层指出数据中心需求仍然很大"）。每个块引用必须是逐字复制粘贴的摘录，可以对照会议记录进行验证。

**计算完整性规则**：对于任何多步骤计算（从年度指导得出的隐含季度数据、LTM P/E、同比增长率、部门同比变化），请明确写出每个步骤，并在下一步使用之前验证中间结果。如果您声明 A + B + C = X，请在后续公式中使用 X 之前验证 X 在算术上是否正确。如果附录显示的总和不等于其声明的组成部分，则报告有误。如有疑问，请从原始数据重新计算，而不是重用先前计算的中间值。

**比率命名规则**：所有估值比率必须明确标记为 **LTM**（过去十二个月）或 **NTM**（未来十二个月）。切勿使用"trailing"或"forward"——始终使用 LTM 或 NTM。LTM 比率使用最近 4 个报告季度的总和。NTM 比率使用来自 `get_consensus_estimates_from_identifiers` 的**未来 4 个季度共识平均每股收益估计的总和**——而不是单个年度数字。LTM 和 NTM P/E 都必须计算并显示在竞争对手比较表中。

**超链接规则（严格执行）**：报告中的每一项声明——数字和非数字——都必须包裹在 `<a href="#ref-N" class="data-ref">` 超链接中，指向附录中相应的条目。**这不是可选的。报告中的每个数字都必须是可点击的链接。** 这包括：收入数字、每股收益、利润率、增长率、市值、市盈率、股票回报、目标价、部门收入以及任何其他财务指标。它还包括来自会议记录或 Kensho 搜索的定性声明。如果您将其声明为事实，则必须链接到来源。为每个独特的声明分配一个连续的参考 ID（`ref-1`、`ref-2` 等）。超链接样式很微妙——深蓝色，无下划线，悬停时显示点状下划线。**不要在报告正文中写任何未包裹在 `<a>` 标签中的数字。** 例如：写 `<a href="#ref-1" class="data-ref">$152.3B</a>`，永远不要写 `$152.3B` 作为纯文本。

---

## 阶段 1：公司概况与设置

1. 从 `$ARGUMENTS` 中解析单个公司股票代码（去除空格）。
2. 运行 `mkdir -p /tmp/earnings-preview` 创建工作目录。
3. 调用 `get_latest()` 建立当前报告期背景。
4. 调用 `get_info_from_identifiers` —— 记录市值、行业。
5. 调用 `get_company_summary_from_identifiers` —— 记录业务描述。
6. 调用 `get_next_earnings_from_identifiers` —— 记录即将到来的财报日期和财季名称。

**立即写入** `/tmp/earnings-preview/company-info.txt`：
```
TICKER: [股票代码]
COMPANY: [全名]
INDUSTRY: [行业]
MARKET_CAP: [价值] (截至 [日期])
NEXT_EARNINGS_DATE: [日期]
NEXT_EARNINGS_QUARTER: [API 返回的 Q# FY#### 格式]
BUSINESS_DESCRIPTION: [2-3 句摘要]
```

---

## 阶段 2：财报会议记录分析（强制性 — 写作前完成）

1. 调用 `get_latest_earnings_from_identifiers` 获取最近完成的财报电话会议的 `key_dev_id`。
2. 调用该会议记录的 `get_transcript_from_key_dev_id`。
3. **立即写入** `/tmp/earnings-preview/transcript-extracts.txt`，包含以下部分。在会议记录仍在上下文中时写入此文件 — 不要等待：

```
TRANSCRIPT_SOURCE: [会议名称，例如 "Q3 2025 Earnings Call"]
KEY_DEV_ID: [key_dev_id]
CALL_DATE: [日期]
FISCAL_QUARTER: [Q# FY####]

=== 逐字引用（完全复制粘贴 — 不要释义）===
QUOTE_1: "[来自会议记录的确切文本]"
SPEAKER_1: [姓名], [职位]
CONTEXT_1: [1 句话说明出现位置 — 准备发言或问答环节]

QUOTE_2: "[来自会议记录的确切文本]"
SPEAKER_2: [姓名], [职位]
CONTEXT_2: [上下文]

QUOTE_3: "[来自会议记录的确切文本]"
SPEAKER_3: [姓名], [职位]
CONTEXT_3: [上下文]

QUOTE_4: "[来自会议记录的确切文本]"
SPEAKER_4: [姓名], [职位]
CONTEXT_4: [上下文]

=== 指导（仅限定量）===
- [指标]: [管理层声明的范围或点估计]
- [指标]: [范围或点估计]

=== 关键驱动因素 ===
- [驱动因素 1 及支持数据点]
- [驱动因素 2 及支持数据点]
- [驱动因素 3 及支持数据点]

=== 不利因素与风险 ===
- [风险 1，如有可用的量化数据]
- [风险 2]

=== 分析师问答主题 ===
- [主题 1：分析师关注的问题]
- [主题 2]
- [主题 3]

=== 综合分析：下一季度需要关注的主题 ===
- [主题 1]
- [主题 2]
- [主题 3]
```

---

## 阶段 3：竞争对手分析

1. 使用 `competitor_source="all"` 调用 `get_competitors_from_identifiers`。
2. 选择**最相关的 5-7 家公开竞争对手**。
3. 对于公司**和**所有选定的竞争对手，收集：
   - `get_prices_from_identifiers`，参数为 `periodicity="day"`，最近 12 个月
   - `get_financial_line_item_from_identifiers`，参数为 `diluted_eps`、`period_type="quarterly"`、`num_periods=8`
   - `get_capitalization_from_identifiers`，参数为 `capitalization="market_cap"`（最新）
   - `get_consensus_estimates_from_identifiers`，参数为 `period_type="quarterly"`、`num_periods_forward=4` —— 返回未来 4 个季度的共识平均每股收益估计，用于计算 NTM EPS

**每次工具调用返回后，立即将原始数据追加到相应的中间文件：**

**写入** `/tmp/earnings-preview/prices.csv` —— 每行一个（股票代码、日期、收盘价）。包括 `source` 列，包含确切的 MCP 函数调用。先写入目标公司的价格，然后在获取时写入每个竞争对手的价格：
```
ticker,date,close,source
D,2025-02-19,55.67,get_prices_from_identifiers(identifier='D',periodicity='day')
D,2025-02-20,55.82,get_prices_from_identifiers(identifier='D',periodicity='day')
...
DUK,2025-02-19,111.79,get_prices_from_identifiers(identifier='DUK',periodicity='day')
...
```
注意：`source` 值对于来自单个调用的所有行都是相同的 —— 在每行上写入它以便随时可用。

**写入** `/tmp/earnings-preview/peer-eps.csv` —— 每行一个（股票代码、期间、每股收益）。每次 `diluted_eps` 调用后立即写入：
```
ticker,period,diluted_eps,source
D,Q4 2024,1.09,get_financial_line_item_from_identifiers(identifier='D',line_item='diluted_eps',period_type='quarterly')
D,Q1 2025,-0.11,get_financial_line_item_from_identifiers(identifier='D',line_item='diluted_eps',period_type='quarterly')
...
DUK,Q4 2024,1.52,get_financial_line_item_from_identifiers(identifier='DUK',line_item='diluted_eps',period_type='quarterly')
...
```

**写入** `/tmp/earnings-preview/peer-market-caps.csv` —— 每行一个股票代码。每次 `market_cap` 调用后立即写入：
```
ticker,market_cap,retrieval_date,source
D,55900000000,2026-02-19,get_capitalization_from_identifiers(identifier='D',capitalization='market_cap')
DUK,98300000000,2026-02-19,get_capitalization_from_identifiers(identifier='DUK',capitalization='market_cap')
...
```

**写入** `/tmp/earnings-preview/consensus-eps.csv` —— 每行一个（股票代码、期间、共识平均每股收益）。每次 `get_consensus_estimates_from_identifiers` 调用后立即写入：
```
ticker,period,consensus_mean_eps,num_estimates,source
D,Q4 2025,0.88,12,get_consensus_estimates_from_identifiers(identifier='D',period_type='quarterly',num_periods_forward=4)
D,Q1 2026,0.72,10,get_consensus_estimates_from_identifiers(identifier='D',period_type='quarterly',num_periods_forward=4)
D,Q2 2026,0.91,9,get_consensus_estimates_from_identifiers(identifier='D',period_type='quarterly',num_periods_forward=4)
D,Q3 2026,1.05,8,get_consensus_estimates_from_identifiers(identifier='D',period_type='quarterly',num_periods_forward=4)
DUK,Q4 2025,1.48,14,get_consensus_estimates_from_identifiers(identifier='DUK',period_type='quarterly',num_periods_forward=4)
...
```

4. **现在不要计算市盈率或回报。** 原始数据现在已存储在磁盘上。计算在阶段 6（验证）中进行，从这些文件读取数据。

**日期一致性规则（股票回报）**：计算比较股票回报（年初至今百分比、1 年百分比、30 天百分比、90 天百分比）时，**所有股票代码必须使用完全相同的开始和结束日期**。将所有价格数据写入 `prices.csv` 后，找出所有股票代码数据中出现的第一个交易日期，并将其用作共同基准日期。不要对不同的股票代码使用不同的基准日期（例如，目标公司从 2 月 19 日开始，同行从 2 月 28 日开始）。如果某个股票代码的数据比其他股票代码晚开始，请对所有计算使用第一个重叠日期。在附录中注明每次回报计算的共同基准日期。

**市盈率货币规则（LTM P/E）**：计算每家公司的 LTM P/E 时，使用该公司来自 `peer-eps.csv` 的**最近 4 个报告季度**——而不是对所有公司应用固定的日历窗口。如果同行已经报告了 2025 年第四季度，而目标公司只报告到 2025 年第三季度，则同行的 LTM EPS 应包括 2025 年第四季度。检查每家公司的最新报告期，并使用每家公司最近的 4 个期间。在附录中注明每次市盈率计算使用了哪 4 个季度。

**市值日期戳**：报告市值时，使用 `peer-market-caps.csv` 中的 `retrieval_date`。如果与报告日期不同，请在附录中注明。

---

## 阶段 4：新闻、估计与行业情报（通过 Kensho Grounding）

为以下**每个**类别运行这些 `search` 查询。不要跳过任何一个。

**关键 — 捕获源 URL**：每个 Kensho `search` 结果都包含底层文章、报告或数据页面的**源 URL**。您必须记录每个发现的 URL。

**每次搜索调用后，立即将结果追加到** `/tmp/earnings-preview/kensho-findings.txt`，使用以下格式。不要等到所有搜索完成后再写入 —— 每次搜索后立即写入：

```
=== SEARCH: "[使用的查询]" ===
DATE_RUN: [今天的日期]
CATEGORY: [estimates|analyst_ratings|risks|news|sector]

FINDING_1: [关键发现或摘录]
URL_1: [搜索结果中的源 URL]
SOURCE_1: [出版物名称，如有可用日期]

FINDING_2: [关键发现或摘录]
URL_2: [源 URL]
SOURCE_2: [出版物名称，日期]

[...继续此搜索的所有相关结果...]
```

**财报估计与分析师情绪**：
1. `search` 查询 "[TICKER] earnings estimates consensus EPS revenue upcoming quarter"
   - 记录：共识每股收益、共识收入、过去 90 天的估计修正方向。
   - **立即追加到 kensho-findings.txt。**
2. `search` 查询 "[TICKER] analyst ratings price target upgrades downgrades"
   - 记录：最近的升级/降级、目标价范围、多头/空头论点摘要。
   - **立即追加到 kensho-findings.txt。**
3. `search` 查询 "[TICKER] risks bear case concerns investors"
   - 记录：关键辩论、空头论点、即将发布财报的关键变数。
   - **立即追加到 kensho-findings.txt。**

**近期新闻（强制性 — 不要跳过）**：
4. `search` 查询 "[TICKER] [company name] recent news developments"
   - 记录：过去 60 天的重大新闻 — 并购、产品发布、高管变动、监管行动、合作伙伴关系、法律进展、关税或任何可能影响即将到来的财报发布或未来指导的事件。
   - 对于每个项目，注明日期、标题、潜在的财报影响。
   - **立即追加到 kensho-findings.txt。**

**行业背景**：
5. `search` 查询 "[company industry/sector] sector outlook trends"
   - 记录：行业层面的有利/不利因素、宏观数据、竞争动态。
   - **立即追加到 kensho-findings.txt。**

---

## 阶段 5：财务数据收集

**季度财务数据（最近 8 个季度）**：
使用 `period_type="quarterly"`、`num_periods=8` 调用 `get_financial_line_item_from_identifiers` 获取：
`revenue`、`gross_profit`、`operating_income`、`ebitda`、`net_income`、`diluted_eps`

**每次行项目调用返回后，立即追加到** `/tmp/earnings-preview/financials.csv`。按返回的原样写入原始值 —— 不要四舍五入或转换。包括 `source` 列，包含确切的 MCP 函数调用和参数：
```
ticker,period,line_item,value,source
D,Q4 2024,revenue,3941000000,get_financial_line_item_from_identifiers(identifier='D',line_item='revenue',period_type='quarterly')
D,Q1 2025,revenue,3400000000,get_financial_line_item_from_identifiers(identifier='D',line_item='revenue',period_type='quarterly')
D,Q2 2025,revenue,4076000000,get_financial_line_item_from_identifiers(identifier='D',line_item='revenue',period_type='quarterly')
D,Q3 2025,revenue,3810000000,get_financial_line_item_from_identifiers(identifier='D',line_item='revenue',period_type='quarterly')
D,Q4 2024,diluted_eps,1.09,get_financial_line_item_from_identifiers(identifier='D',line_item='diluted_eps',period_type='quarterly')
D,Q1 2025,diluted_eps,-0.11,get_financial_line_item_from_identifiers(identifier='D',line_item='diluted_eps',period_type='quarterly')
...
```

**现在不要计算利润率或增长率。** 只写入原始数据。计算在阶段 6 中进行。

**部门数据**：
- 使用 `segment_type="business"`、`period_type="quarterly"`、`num_periods=8` 调用 `get_segments_from_identifiers`
- 您需要 8 个季度（不是 4 个），以便有去年同期季度进行同比比较。要计算 2025 年第三季度的同比，您需要 2024 年第三季度 —— 这是倒数第 5 个季度。**如果 API 响应中没有上一年季度的部门数据，不要估算或编造数据。在报告中注明"同比不可用"。**

**立即写入** `/tmp/earnings-preview/segments.csv`：
```
ticker,period,segment_name,revenue,source
D,Q3 2024,Dominion Energy Virginia,2762000000,get_segments_from_identifiers(identifier='D',segment_type='business',period_type='quarterly')
D,Q3 2024,Dominion Energy South Carolina,848000000,get_segments_from_identifiers(identifier='D',segment_type='business',period_type='quarterly')
D,Q3 2024,Contracted Energy,260000000,get_segments_from_identifiers(identifier='D',segment_type='business',period_type='quarterly')
D,Q3 2025,Dominion Energy Virginia,3311000000,get_segments_from_identifiers(identifier='D',segment_type='business',period_type='quarterly')
D,Q3 2025,Dominion Energy South Carolina,945000000,get_segments_from_identifiers(identifier='D',segment_type='business',period_type='quarterly')
D,Q3 2025,Contracted Energy,297000000,get_segments_from_identifiers(identifier='D',segment_type='business',period_type='quarterly')
...
```

**财报历史（用于股票图表注释）**：
- `get_earnings_from_identifiers` —— 收集 12 个月价格窗口内的过去财报日期。
- **立即写入** `/tmp/earnings-preview/earnings-dates.csv`：
```
ticker,earnings_date,call_name,source
D,2025-05-02,Q1 2025 Earnings Call,get_earnings_from_identifiers(identifier='D')
D,2025-08-01,Q2 2025 Earnings Call,get_earnings_from_identifiers(identifier='D')
D,2025-10-31,Q3 2025 Earnings Call,get_earnings_from_identifiers(identifier='D')
...
```

---

## 阶段 6：验证与计算（强制性 — 不要跳过）

在生成报告之前，读回所有中间文件并从干净数据执行计算。此阶段通过从文件而不是压缩的对话上下文工作来确保数据完整性。

1. **使用 bash `cat` 命令读取所有中间文件**：
   - `cat /tmp/earnings-preview/company-info.txt`
   - `cat /tmp/earnings-preview/transcript-extracts.txt`
   - `cat /tmp/earnings-preview/financials.csv`
   - `cat /tmp/earnings-preview/segments.csv`
   - `cat /tmp/earnings-preview/prices.csv`
   - `cat /tmp/earnings-preview/peer-eps.csv`
   - `cat /tmp/earnings-preview/peer-market-caps.csv`
   - `cat /tmp/earnings-preview/consensus-eps.csv`
   - `cat /tmp/earnings-preview/kensho-findings.txt`
   - `cat /tmp/earnings-preview/earnings-dates.csv`

2. **从当前上下文中的原始数据计算派生指标**：
   - 毛利率 % = gross_profit / revenue（每季度）
   - 营业利润率 % = operating_income / revenue（每季度）
   - 收入同比增长 % = (当前季度收入 - 去年同期季度收入) / 去年同期季度收入
   - 每股收益同比增长 % = 相同逻辑；如果基数为负，使用 "n.m."
   - 部门同比增长 % = 按名称匹配部门与去年同期季度；如果缺失，注明"同比不可用"
   - 每家公司的 LTM P/E = 最新价格 / 最近 4 个季度每股收益之和（使用 `peer-eps.csv` 检查每个股票代码有哪些季度可用）
   - 每家公司的 NTM P/E = 最新价格 / NTM EPS，其中 **NTM EPS = 来自 `consensus-eps.csv` 的未来 4 个季度共识平均每股收益估计之和**。为每个股票代码添加所有 4 个季度的 consensus_mean_eps 值。如果某个同行的未来季度少于 4 个可用，则将 NTM P/E 标记为"n/a"。在附录中注明汇总了哪 4 个季度。
   - 股票回报（年初至今、1 年、30 天、90 天）= 在 `prices.csv` 中找到所有股票代码的**共同首个日期**，然后从该日期计算回报

3. **交叉检查**：
   - 验证每个部门同比在 `segments.csv` 中都有实际的上年行。如果没有，标记"同比不可用"。
   - 验证所有股票回报基准日期在股票代码之间是否相同。
   - 通过重新汇总组件来验证任何多步骤计算（例如，LTM EPS 总和与 4 个季度值匹配）。
   - 验证 `transcript-extracts.txt` 中的所有逐字引用都是准确的复制粘贴（不是释义）。

4. **写入** `/tmp/earnings-preview/calculations.csv`，包含所有派生值：
```
ticker,metric,value,formula,components
D,gross_margin_Q3_2025,32.5%,gross_profit/revenue,"gross_profit=1238100000,revenue=3810000000"
D,revenue_yoy_Q3_2025,+9.3%,(Q3_2025-Q3_2024)/Q3_2024,"Q3_2025=3810000000,Q3_2024=3486000000"
D,ltm_pe,24.2x,price/ltm_eps,"price=65.46,ltm_eps=2.70,quarters=Q4_2024+Q1_2025+Q2_2025+Q3_2025"
D,ntm_pe,18.5x,price/ntm_eps,"price=65.46,ntm_eps=3.56,quarters=Q4_2025(0.88)+Q1_2026(0.72)+Q2_2026(0.91)+Q3_2026(1.05),source=get_consensus_estimates_from_identifiers"
D,yoy_return,+17.6%,(end-start)/start,"end=65.46,start=55.67,base_date=2025-02-19"
DUK,yoy_return,+13.0%,(end-start)/start,"end=126.32,start=111.79,base_date=2025-02-19"
...
```

此文件成为报告中所有数字的唯一真实来源。

---

## 阶段 7：生成 HTML 报告

**停止 — 在编写任何 HTML 之前，您必须读取所有中间文件。这是一个阻塞性的前提条件。**

这不是可选的。您必须将下面的每个 `cat` 命令作为**单独的 bash 工具调用**运行（不要合并为一个）。这确保每个文件的内容都被单独加载并在对话中可见。不要将它们合并成单个命令。不要跳过任何文件。

**一次运行一个命令，每个作为单独的 bash 调用：**

1. `cat /tmp/earnings-preview/company-info.txt`
2. `cat /tmp/earnings-preview/transcript-extracts.txt`
3. `cat /tmp/earnings-preview/financials.csv`
4. `cat /tmp/earnings-preview/segments.csv`
5. `cat /tmp/earnings-preview/prices.csv`
6. `cat /tmp/earnings-preview/peer-eps.csv`
7. `cat /tmp/earnings-preview/peer-market-caps.csv`
8. `cat /tmp/earnings-preview/consensus-eps.csv`
9. `cat /tmp/earnings-preview/kensho-findings.txt`
10. `cat /tmp/earnings-preview/earnings-dates.csv`
11. `cat /tmp/earnings-preview/calculations.csv`

**读取所有文件后，您必须向用户打印一条摘要消息**，列出每个文件及其状态。使用完全相同的格式：

```
--- DATA FILE VERIFICATION ---
1. company-info.txt        ✓ loaded ([N] lines)
2. transcript-extracts.txt ✓ loaded ([N] lines)
3. financials.csv          ✓ loaded ([N] rows)
4. segments.csv            ✓ loaded ([N] rows)
5. prices.csv              ✓ loaded ([N] rows)
6. peer-eps.csv            ✓ loaded ([N] rows)
7. peer-market-caps.csv    ✓ loaded ([N] rows)
8. consensus-eps.csv       ✓ loaded ([N] rows)
9. kensho-findings.txt     ✓ loaded ([N] lines)
10. earnings-dates.csv     ✓ loaded ([N] rows)
11. calculations.csv       ✓ loaded ([N] rows)

All intermediate data files loaded successfully.
Generating report using file data as the single source of truth.
---
```

如果任何文件缺失或为空，停止并告诉用户哪个文件失败。不要在数据缺失的情况下继续生成报告。

**HTML 报告中的每个数字、引用、源 URL 和 MCP 函数调用引用都必须来自这些文件 —— 而不是您对早期对话的记忆。** 文件是唯一的真实来源。早期对话上下文可能已被压缩或汇总，如果依赖它，**将会**包含错误。如果数据点不在文件中，则不应出现在报告中。

完整的 HTML 模板、CSS 和 Chart.js 配置请参见 [report-template.md](report-template.md)。

**强制性 — 对图表使用模板辅助函数：**
report-template.md 提供了预构建的、经过调试的 Chart.js 辅助函数。您必须使用这些确切的函数来创建图表。不要编写自定义的内联 Chart.js 代码。辅助函数包括：
- `createRevEpsChart(canvasId, labels, revenueData, epsData, revLabel)` — 用于图 1
- `createMarginChart(canvasId, labels, grossMargins, opMargins)` — 用于图 2
- `createRevGrowthChart(canvasId, labels, growthData)` — 用于图 3
- `createAnnotatedPriceChart(canvasId, labels, prices, earningsDates, ticker)` — 用于图 5
- `createCompPerfChart(canvasId, labels, datasets)` — 用于图 6
- `createPEChart(canvasId, companies)` — 用于图 7

每个图表调用必须在其自己的 `<script>` 标签中包装在 try-catch 块中。这确保一个图表中的错误不会阻止其他图表渲染。示例：
```html
<script>
try {
  createRevEpsChart('chart-rev-eps', [...], [...], [...], 'Revenue ($B)');
} catch(e) { console.error('Figure 1 error:', e); }
</script>
<script>
try {
  createMarginChart('chart-margins', [...], [...], [...]);
} catch(e) { console.error('Figure 2 error:', e); }
</script>
```

### 报告结构（共 4-5 页）

报告分为两部分：**叙述**（第 1-2 页）和**图表**（第 3-5 页）。保持紧密集成。

---

**AI 免责声明（强制性 — 必须出现在 3 个位置）：**
您必须在报告 HTML 中包含以下免责声明文本。这不是可选的 —— 没有它，报告不完整：

> **"分析由 AI 生成 — 请确认所有输出"**

它必须出现在以下 3 个位置：
1. **页眉横幅** — 在封面页眉之前，作为居中的黄色横幅：`<div class="ai-disclaimer">Analysis is AI-generated — please confirm all outputs</div>`
2. **页脚** — 在 page-footer div 内，作为突出的黄色横幅：`<div class="footer-disclaimer">Analysis is AI-generated — please confirm all outputs</div>`
3. **附录** — 作为附录部分的第一行，在表格之前：`<div class="ai-disclaimer">Analysis is AI-generated — please confirm all outputs</div>`

---

**第 1 页：封面与主题**

- **AI 免责声明横幅**（黄色，居中 — 见 AI 免责声明规则）
- **页眉**：公司名称（股票代码）| 行业 | 报告日期
- **标题**：主题性标题，具体到季度（例如，"Walmart Inc. (WMT) Q4 FY2026 Earnings Preview: Holiday Harvest — Can Furner's First Print Confirm the $1T Thesis?"）
- **执行摘要**（最多 2-3 个短段落，带项目符号）：
  - 用 1-2 句话说明您对本次财报发布的预期
  - 4-6 个项目符号涵盖：我们的每股收益估计 vs 共识、指导预期、需要关注的关键指标、什么会影响股价、关键辩论
  - 保持直接和有主见 —— 表达观点，不要含糊其辞
- **关键管理层引用**从最近的财报电话会议中自然融入叙述中相关位置。不要将这些放在单独的标题下。作为支持您主题观点的证据自然整合。格式化为缩进块引用。

---

**第 2 页：估计、主题与新闻**

- **共识估计表**（单个表格，标记为图表）：
  - 列：指标 | 共识 | 我们的估计 | 同比变化
  - 行：收入、每股收益、毛利率、营业收入，以及 2-3 个公司特定的关键绩效指标（例如，可比销售额、电商增长、会员收入 —— 华尔街关注这家公司的任何指标）
  - **颜色编码严格机械**：如果同比变化值为负，使用 `class="neg"`（红色）。如果为正，使用 `class="pos"`（绿色）。如果为零或 N/A，使用 `class="neutral"`。数字的符号决定类别 —— 不要根据解释覆盖。-1.1% 始终是红色，即使下降很小。
  - 这是唯一的指导/估计部分。不要在其他地方重复估计数据。

- **超越标题每股收益的关键指标**（项目符号列表，3-5 项）：
  - 除每股收益数字外，决定本季度好坏的特定指标
  - 对于每个指标：指标是什么、共识/管理层预期、为什么重要
  - 具体说明："Walmart Connect 广告收入增长（共识 ~30% 同比，第三季度为 33%）"

- **需要关注的主题**（3-5 个项目符号）：
  - 即将发布报告的前瞻性项目
  - 管理层需要交付的内容、可能令人惊讶的内容、空头关注的内容
  - 每个主题：最多 1-2 句话

- **近期新闻与发展**（3-5 个项目符号）：
  - 过去 60 天的重大新闻，每项一行
  - 日期 + 标题 + 简要影响评估
  - 仅包括可能影响即将发布的财报或指导的项目

---

**第 3-5 页：图表（所有图表和表格）**

所有图表按顺序编号。每个图表都有标题和来源行。

- **图 1：季度收入与摊薄每股收益** — 条形/折线组合图，8 个季度
- **图 2：利润率趋势（毛利率和营业利润率 %）** — 双折线图，8 个季度
- **图 3：收入同比增长 %** — 条形图，带绿色/红色条件着色。**仅包括当前和上年数据都存在的季度**（通常是获取的 8 个季度中最近的 4 个）。不要包括无法计算同比的季度 —— 图表应有 4 个条形，不是 8 个。
- **图 4：业务部门收入** — 表格：部门 | 最新季度收入（百万美元）| 占总额百分比 | 同比变化
- **图 5：1 年股票价格与财报日期** — 价格线，在财报日期有垂直注释线，标注季度和财报后 1 天变动
- **图 6：股票表现 vs 竞争对手（索引为 100）** — 多线图，目标公司为粗实线，竞争对手为细虚线
- **图 7：LTM P/E vs 竞争对手** — 水平条形图，目标公司以深蓝色高亮显示
- **图 8：竞争对手比较表** — 股票代码 | 公司 | 市值 | LTM P/E | NTM P/E | 年初至今 % | 1 年 %

---

**附录：数据来源与计算（强制性 — 不要跳过或缩写）**

附录必须以 AI 免责声明横幅开头：`<div class="ai-disclaimer">Analysis is AI-generated — please confirm all outputs</div>`

报告的最后一页（或几页）必须包含附录表格，记录报告中引用的**每一项声明** —— 数字和非数字。**报告正文中出现的每个数字必须在此附录中有对应的行，并且报告正文中的每个此类数字必须是可点击的 `<a href="#ref-N">` 超链接，滚动到其附录行。** 如果报告中的数字没有指向附录的超链接，则报告不完整。

- **表格列**：参考编号 | 事实 | 值 | 来源与推导
- **参考编号**：与报告正文中的超链接锚点匹配的顺序 ID（`ref-1`、`ref-2` 等）。每行都有 `id="ref-N"` 属性，以便超链接滚动到它。
- **事实**：人类可读标签（例如，"Q3 FY2026 收入"、"LTM P/E — WMT"、"管理层指出关税不利因素"、"巴克莱升级为增持"）
- **值**：报告中显示的确切数字（例如，"$152.3B"、"24.5%"、"28.1x"）。对于非数字事实，留空或写"N/A"。
- **来源与推导**：这是关键列。**每行必须有具体、详细的来源 —— 不仅仅是标签。** 严格遵循以下规则：

  **来自 S&P Capital IQ 的原始财务数据（收入、每股收益、毛利润、营业收入、净利润、EBITDA、价格、市值等）：**
  - 说明使用的 MCP 函数及其关键参数。格式：`S&P Capital IQ — [function_name](identifier='[TICKER]', line_item='[item]', period_type='[type]', period='[Q# FY####]')`
  - 示例：
    - `S&P Capital IQ — get_financial_line_item_from_identifiers(identifier='WMT', line_item='revenue', period_type='quarterly', period='Q3 FY2026')`
    - `S&P Capital IQ — get_financial_line_item_from_identifiers(identifier='WMT', line_item='diluted_eps', period_type='quarterly', period='Q3 FY2026')`
    - `S&P Capital IQ — get_prices_from_identifiers(identifier='WMT', periodicity='day')`
    - `S&P Capital IQ — get_capitalization_from_identifiers(identifier='WMT', capitalization='market_cap')`
  - **不要只写"S&P Capital IQ"而不提供详细信息。** 读者必须确切知道哪个数据点来自哪个工具调用。

  **计算值（利润率、增长率、市盈率、回报、同比变化）：**
  - 显示完整公式，包含**超链接组件** —— 每个组件必须是 `<a href="#ref-N">` 链接，返回到该原始数据点的附录行。这至关重要：读者必须能够从计算值点击到其每个输入。
  - 示例：`毛利率 = <a href='#ref-5'>毛利润 $37.2B</a> / <a href='#ref-1'>收入 $152.3B</a> = 24.4%. 来源：S&P Capital IQ（计算）`
  - 示例：`LTM P/E = <a href='#ref-20'>价格 $172.35</a> / (<a href='#ref-8'>Q1 EPS $1.47</a> + <a href='#ref-9'>Q2 EPS $1.84</a> + <a href='#ref-10'>Q3 EPS $1.53</a> + <a href='#ref-11'>Q4 EPS $1.80</a>) = $172.35 / $6.64 = 25.9x`
  - 示例：`收入同比增长 = (<a href='#ref-12'>Q3 FY26 收入 $165.8B</a> - <a href='#ref-3'>Q3 FY25 收入 $160.8B</a>) / <a href='#ref-3'>Q3 FY25 收入 $160.8B</a> = +3.1%`
  - **每个公式组件必须是可点击的超链接。** 不要用纯文本数字编写公式。

  **来自会议记录的声明（引用、管理层评论、指导）：**
  - 写出会议记录中的**逐字摘录句子**。
  - 通过其全名和用于获取它的 `key_dev_id` 引用会议记录。
  - 格式：`"[逐字引用]" — [发言人], [职位]. 来源：[Q# FY#### Earnings Call Transcript] (key_dev_id: [ID])`
  - 示例：`"We expect comp sales growth of 3-4% in Q4" — CEO John Furner. 来源：Q3 FY2026 Earnings Call Transcript (key_dev_id: 12345678)`

  **来自 Kensho Grounding 搜索结果（新闻、分析师评级、共识估计）：**
  - 写出搜索结果中的关键发现或摘录。
  - **强制性：包含来源 URL**，作为可点击的 `<a href="[URL]" target="_blank">` 超链接返回的 Kensho `search` 工具。这是最重要的部分 —— 读者必须能够点击到原始来源。
  - 格式：`"[发现/摘录]" — <a href="[URL]" target="_blank">[来源标题或出版物]</a>. 查询：search("[使用的查询]")`
  - 示例：`"Barclays upgraded WMT to Overweight with $210 price target on Jan 15, 2026." — <a href="https://www.investing.com/news/barclays-upgrades-wmt" target="_blank">Investing.com, Jan 15 2026</a>. 查询：search("WMT analyst ratings price target upgrades downgrades")`
  - 如果特定结果没有返回 URL，写"来源 URL 不可用"并仍包含搜索查询。

**完整性检查**：在完成报告之前，扫描报告正文中的每个数字。如果任何数字没有包裹在 `<a href="#ref-N" class="data-ref">` 中，请修复它。如果任何附录行的来源与推导只是一个简单标签如"S&P Capital IQ"而没有函数调用详细信息，请修复它。如果任何计算值的公式缺少超链接组件，请修复它。如果任何 Kensho 来源的声明缺少来源 URL，请修复它。

按部分（财务、估值、估计与共识、会议记录声明、新闻与分析师评论、股票表现）对附录行进行分组，并添加子标题。使用较小的字体大小（10-11px）。

---

## 阶段 8：输出

1. 将完整的 HTML 文件写入当前工作目录中的 `earnings-preview-[TICKER]-YYYY-MM-DD.html`。
2. 在浏览器中打开：`open earnings-preview-[TICKER]-YYYY-MM-DD.html`
3. 告诉用户文件已创建并总结关键发现。

---

## 写作指南

- **禁止表情符号**：不要在报告中的任何地方使用表情符号。这是一份专业研究文档。
- **简洁**：目标为 4-5 打印页。每个句子都必须有分量。尽可能使用项目符号，而不是段落。如果某个部分感觉太长，请删减。
- **数字要具体**："收入 $52.4B，同比增长 5.2%" 而不是"收入强劲增长"。
- **表达观点**：这是财报预览，不是摘要。说明您的预期、重要事项和原因。要有主见，但要有数据支持。
- **管理层引用无标题**：将最近一次电话会议中的 3-4 个关键管理层引用作为块引用直接融入叙述中。不要创建"关键管理层引用"部分标题 —— 让它们作为支持证据自然流动。
- **专业语气**：卖方股票研究风格 —— 分析性、直接、数据驱动。
- **图表必须使用真实数据**：每个图表都用实际 MCP 数据填充。切勿编造数据。
- **竞争对手背景**：相对于同行框定估值。没有知道同行交易于 20x 或 35x，25x P/E 毫无意义。
- **超链接声明**：每个事实声明 —— 数字或定性 —— 必须是 `<a class="data-ref">` 标签，链接到其附录条目。数字：`<a href="#ref-1" class="data-ref">$152.3B</a>`。定性：`<a href="#ref-25" class="data-ref">management flagged tariff headwinds as the primary margin risk</a>`。任何事实都不应没有附录中可追溯的来源。

---

## 金融术语解释

### 1. 股票研究 (Equity Research)

**定义**：股票研究是对上市公司进行的深入分析，旨在评估其投资价值。股票研究报告通常由卖方分析师（为投资银行工作）或买方分析师（为对冲基金、共同基金等机构投资者工作）撰写。

**核心内容**：
- **公司基本面分析**：包括财务状况、业务模式、竞争优势
- **估值分析**：使用各种估值方法确定股票的内在价值
- **投资建议**：买入、卖出或持有建议
- **目标价**：分析师对股票未来价格的预测

**报告类型**：
- **首次覆盖报告**：对公司进行全面的初始分析
- **财报预览**：在财报发布前的预测分析
- **财报点评**：财报发布后的分析和解读
- **行业报告**：对特定行业的整体分析

### 2. LTM（过去十二个月）

**定义**：LTM 是 "Last Twelve Months" 的缩写，指最近十二个月的财务数据。这是一个常用的财务指标，用于评估公司最近的经营业绩。

**计算方法**：
- LTM 数据通常通过将最近四个季度的财务数据相加得到
- 例如，LTM 收入 = 最近四个季度收入之和

**用途**：
- **估值**：LTM P/E（过去十二个月市盈率）是常用的估值指标
- **业绩比较**：用于比较同一公司不同时期或不同公司之间的业绩
- **财务建模**：在财务模型中用于计算比率和趋势

**优势**：
- 提供最新的财务状况快照
- 避免季节性波动的影响
- 便于跨时期比较

### 3. NTM（未来十二个月）

**定义**：NTM 是 "Next Twelve Months" 的缩写，指未来十二个月的财务预测数据。

**计算方法**：
- NTM 数据通常基于分析师的共识估计
- NTM EPS = 未来四个季度共识每股收益估计之和

**用途**：
- **估值**：NTM P/E 是前瞻性估值的关键指标
- **投资决策**：帮助投资者评估公司未来的增长潜力
- **预测分析**：用于预测公司未来的财务表现

**优势**：
- 反映市场对公司未来的预期
- 更适合评估成长型公司
- 有助于识别估值差异

### 4. 共识估计 (Consensus Estimates)

**定义**：共识估计是多位分析师对公司财务指标的平均预测值。这些估计通常包括收入、每股收益（EPS）、净利润等关键指标。

**数据来源**：
- 各大金融数据提供商（如 S&P Capital IQ、FactSet、Bloomberg）
- 卖方分析师报告
- 专业财经媒体

**类型**：
- **当前季度估计**：对当前财季的预测
- **年度估计**：对当前财年的预测
- **长期增长估计**：对未来几年增长率的预测

**影响**：
- **股价反应**：实际财报与共识估计的差异会影响股价
- **投资决策**：共识估计是投资分析的重要参考
- **市场预期**：反映市场对公司业绩的普遍看法

### 5. 市盈率 (P/E Ratio)

**定义**：市盈率是股价与每股收益的比率，是最常用的估值指标之一。

**计算公式**：
- P/E = 股价 / 每股收益

**类型**：
- **LTM P/E**：使用过去十二个月的每股收益
- **NTM P/E**：使用未来十二个月的预期每股收益

**解读**：
- **高 P/E**：市场对公司未来增长有较高预期，或公司被高估
- **低 P/E**：市场对公司未来增长预期较低，或公司被低估
- **行业比较**：需要与同行业公司的 P/E 进行比较

**局限性**：
- 不适合亏损公司
- 受会计政策影响
- 未考虑债务和现金

### 6. 财报电话会议 (Earnings Call)

**定义**：财报电话会议是公司管理层在发布季度或年度财务报告后举行的电话会议，向投资者和分析师介绍财务业绩并回答问题。

**参与者**：
- **管理层**：CEO、CFO、其他高管
- **投资者**：机构投资者、分析师、个人投资者

**会议内容**：
- **财务业绩回顾**：介绍收入、利润、现金流等关键指标
- **业务更新**：介绍公司业务进展和重大事件
- **未来展望**：提供未来的财务指导和战略方向
- **问答环节**：回答分析师和投资者的问题

**重要性**：
- **信息披露**：是公司向投资者传递信息的重要渠道
- **股价影响**：电话会议中的评论和指导会影响股价
- **透明度**：增加公司运营的透明度

### 7. 同比增长 (Year-over-Year Growth)

**定义**：同比增长是指与去年同期相比的增长率。这是评估公司业绩趋势的重要指标。

**计算公式**：
- 同比增长率 = (本期值 - 去年同期值) / 去年同期值 × 100%

**用途**：
- **业绩评估**：评估公司业务的增长趋势
- **趋势分析**：识别业务的季节性模式
- **预测未来**：基于历史趋势预测未来表现

**优势**：
- 消除季节性因素的影响
- 便于跨年度比较
- 反映真实的业务增长

### 8. 毛利率 (Gross Margin)

**定义**：毛利率是毛利润占收入的百分比，反映公司产品或服务的盈利能力。

**计算公式**：
- 毛利率 = 毛利润 / 收入 × 100%
- 毛利润 = 收入 - 销售成本

**解读**：
- **高毛利率**：公司产品定价能力强，成本控制好
- **低毛利率**：可能面临激烈竞争或成本压力
- **趋势变化**：毛利率的上升或下降反映盈利能力的变化

**行业差异**：
- **高毛利率行业**：软件、制药、奢侈品
- **低毛利率行业**：零售、航空、制造业

### 9. 营业利润率 (Operating Margin)

**定义**：营业利润率是营业利润占收入的百分比，反映公司核心业务的盈利能力。

**计算公式**：
- 营业利润率 = 营业利润 / 收入 × 100%
- 营业利润 = 毛利润 - 运营费用

**解读**：
- **高营业利润率**：公司运营效率高，成本控制好
- **低营业利润率**：运营成本过高或收入增长乏力
- **与毛利率对比**：两者差距反映运营费用的高低

### 10. EBITDA

**定义**：EBITDA 是 "Earnings Before Interest, Taxes, Depreciation, and Amortization" 的缩写，即利息、税项、折旧及摊销前利润。

**计算公式**：
- EBITDA = 营业利润 + 折旧 + 摊销

**用途**：
- **估值**：常用作企业价值（EV）计算的基础
- **盈利能力比较**：消除不同资本结构和税收政策的影响
- **现金流评估**：作为经营现金流的近似指标

**局限性**：
- 忽略资本支出需求
- 未考虑利息和税收
- 可能被滥用为业绩指标

### 11. 企业价值 (Enterprise Value, EV)

**定义**：企业价值是衡量公司总价值的指标，包括股权价值和债务价值。

**计算公式**：
- EV = 市值 + 债务 - 现金及等价物

**组成部分**：
- **市值**：流通股数量 × 股价
- **债务**：短期债务 + 长期债务
- **现金**：现金及现金等价物

**用途**：
- **并购估值**：确定收购目标的总价值
- **估值比较**：跨公司比较时更准确
- **财务建模**：企业估值模型的核心指标

### 12. 部门分析 (Segment Analysis)

**定义**：部门分析是对公司不同业务部门的财务表现进行单独评估。

**目的**：
- **识别强势部门**：找出贡献最大的业务部门
- **发现问题部门**：识别表现不佳的业务
- **资源配置**：优化资源在各部门间的分配
- **战略规划**：制定部门级别的发展战略

**关键指标**：
- 部门收入及占比
- 部门利润及利润率
- 部门增长率
- 部门资产及投资回报率

**披露要求**：
- 上市公司通常需要按部门披露财务信息
- 帮助投资者了解公司业务构成

### 13. 竞争对手分析 (Competitor Analysis)

**定义**：竞争对手分析是对公司主要竞争对手的全面评估，以了解竞争格局和市场定位。

**分析维度**：
- **财务表现**：收入、利润、增长率
- **市场份额**：在目标市场的占有率
- **竞争优势**：技术、品牌、成本等方面的优势
- **战略方向**：未来的发展计划和战略

**方法**：
- **定量分析**：比较财务指标和市场数据
- **定性分析**：评估品牌形象、客户满意度等
- **SWOT分析**：分析优势、劣势、机会和威胁

**用途**：
- **战略规划**：制定竞争策略
- **投资决策**：评估投资标的的竞争地位
- **市场定位**：确定公司在市场中的位置

### 14. 财务建模 (Financial Modeling)

**定义**：财务建模是使用数学模型和假设来预测公司未来财务表现的过程。

**模型类型**：
- **三表模型**：整合利润表、资产负债表、现金流量表
- **DCF模型**：贴现现金流模型，用于估值
- **敏感性分析**：评估关键变量变化对结果的影响
- **场景分析**：分析不同情景下的财务结果

**应用场景**：
- **估值**：确定公司的内在价值
- **投资决策**：评估投资项目的可行性
- **战略规划**：制定公司未来发展计划
- **融资决策**：评估融资方案的影响

**最佳实践**：
- 使用合理的假设
- 保持模型透明和可审计
- 定期更新和验证模型

---

## Appendix: 金融背景知识

这份文件是"单公司财报预览（Single Company Earnings Preview）"技能的详细说明。财报预览（Earnings Preview）是卖方研究（Equity Research）中最基础的工作之一——在一家公司发布季度财报前，分析师会提前预测业绩并发布报告。

---

### 1. 什么是 Earnings Preview？

**类比：**
想象你是一个足球评论员，比赛开始前你要预测"今天这场球谁会赢、比分多少、关键球员表现如何"。比赛结束后，你再看实际结果和你的预测差多少。

Earnings Preview 就是金融分析师的"赛前预测"——预测公司这个季度的收入、利润、EPS 等关键指标。

---

### 2. 为什么需要 Preview？

**核心逻辑：**
1. **市场预期管理**——让投资者提前知道"大概会是什么水平"
2. **偏差分析**——实际业绩和预测的差异是股价波动的关键
3. **投资建议**——如果预测大幅超预期，提前建议买入

---

### 3. Earnings Preview 的"四大预测指标"

| 指标 | 英文 | 重要性 |
|------|------|--------|
| 营收 | Revenue | 最重要 |
| 每股收益 | EPS | 最重要 |
| EBITDA | EBITDA | 重要 |
| 毛利率 | Gross Margin | 重要 |

---

### 4. Preview 的"三种结果"

| 结果 | 英文 | 股价反应 |
|------|------|---------|
| 超预期 | Beat | 通常涨 |
| 符合预期 | Inline | 通常平 |
| 不及预期 | Miss | 通常跌 |

**关键**：不是"超预期就一定涨"——要看"超预期的幅度"和"管理层的指引"。

---

### 5. 真实案例：特斯拉 2021 年 Q1

| 指标 | 市场预期 | 实际结果 | 差异 |
|------|---------|---------|------|
| 营收 | 104 亿美元 | 103.9 亿美元 | 基本符合 |
| EPS | 0.79 美元 | 0.93 美元 | 超预期 18% |
| 毛利率 | 20.5% | 21.3% | 超预期 |

结果：股价盘后涨 1.5%——虽然营收略低于预期，但 EPS 大幅超预期。

---

### 给小白的一句话

> Earnings Preview 就是金融分析师的"考试押题"——在正式财报发布前，分析师根据各种线索预测"公司这个季度大概能赚多少钱"。如果押对了，分析师名声大噪；如果押错了，客户就会质疑他的专业能力。对于投资者来说，Preview 最大的价值不是"预测准确"，而是"建立一个预期基准"——当实际财报发布时，你可以判断"是超预期还是不及预期"，从而决定"买还是卖"。
