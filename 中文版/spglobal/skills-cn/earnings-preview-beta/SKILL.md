---
name: earnings-preview-single
description: 生成一份简洁的 4-5 页个股权益研究业绩前瞻报告。分析最新的业绩电话会议纪要、竞争格局、估值及近期新闻，产出专业的 HTML 报告。
---

# 个股业绩前瞻报告生成指南

生成一份简洁、专业的个股证券研究业绩前瞻报告。输出结果为独立的 HTML 文件，篇幅目标为 4-5 个打印页。报告应包含密集的数据与图表，叙述精炼，直击要点。

**数据来源（严禁例外）：** 仅允许使用 **Kensho Grounding MCP** (`search`) 和 **S&P Global MCP** (`kfinance`)。绝对禁止使用任何其他工具、数据源或网络访问。特别要求：
- 严禁使用 `WebSearch`、`WebFetch`、`web_search`、`brave_search`、`google_search` 或任何通用网页搜索工具——即使 Kensho 响应缓慢、无结果或暂时不可用。
- 严禁使用任何浏览器、URL 获取或网页抓取工具。
- 如果 Kensho Grounding 的查询没有返回结果，请尝试重新调整查询词，或在报告中注明“数据不可用”。**严禁转而使用网页搜索作为替代方案。**
- 报告中的每一项信息必须能够追溯到 `kfinance` MCP 函数调用或 Kensho `search` 调用。如果无法溯源至这两者之一，则不得在报告中出现。

**关键规则：** 在开始撰写报告的任何部分之前，必须完成所有研究和数据采集工作（阶段 1-5）。

**中间文件规则：** 每次 MCP 工具调用返回后，必须立即将所有原始数据写入 `/tmp/earnings-preview/` 目录下的文件，然后再进行下一次调用。这是为了防止上下文窗口压缩导致数据丢失。严禁仅在内存中保存数据。在阶段 1 开始时，运行 `mkdir -p /tmp/earnings-preview`。**在生成 HTML 报告（阶段 7）之前，必须使用 `cat` 命令将所有中间文件重新读入上下文中。文件（而非你对早前对话的记忆）是报告中每一个数字、引言和来源 URL 的唯一事实来源。如果跳过读取文件，报告将出现错误。**

**财季规则：** 严禁根据日历报告日期推断财季。许多公司的财政年度并非标准自然年（例如，沃尔玛的财年结束于 1 月 31 日，因此 2026 年 2 月的报告涵盖的是 2026 财年第四季度，而非 2025 年第四季度或 2026 年第一季度）。务必使用 `get_next_earnings_from_identifiers` 或 `get_earnings_from_identifiers` 返回的业绩会议名称中明确标注的财季和财年（例如，“Walmart Q4 FY2026 Earnings Call”表示该季度为 Q4 FY2026）。在报告标题、页眉、表格和所有引用中逐字使用该标注。如果会议名称含糊不清，请通过 `get_financial_line_item_from_identifiers` 的期间标签进行交叉核对。

**篇幅规则：** 报告必须简洁。目标打印篇幅为 4-5 页。不要撰写冗长的多段叙述。使用简练、有力的要点。每一句话都必须有其实际价值。如果能用更少的词表达清楚，就精简它。

**逐字引用规则：** 在 `<blockquote>` 标签中引用管理层言论时，文本必须**完全**从会议记录中复制——逐字逐句，包括口癖和句子碎片。严禁改述、重新排列、合并来自会议记录不同部分的句子或“美化”引言。如果在会议记录中找不到完全一致的短语，严禁将其作为直接引言展示，而应以你自己的叙述口吻进行改述（不使用 blockquote 格式），例如：“管理层指出，数据中心的需求依然强劲”。每一个块引用（blockquote）必须是可与会议记录核对的逐字复制片段。

**计算完整性规则：** 对于任何多步计算（从年度指引推算的季度数字、LTM P/E、同比增长率、分部同比变动），请显式写出每个步骤，并在进入下一步前验证中间结果。如果你阐述 A + B + C = X，请在后续公式使用 X 之前验证 X 的算术准确性。如果附录显示的总和与其构成部分不符，则报告是错误的。如有疑问，应从原始数据重新计算，而非重复使用之前计算的中间值。

**比率命名规则：** 所有估值倍数必须明确标注为 **LTM**（过去 12 个月/滚动）或 **NTM**（未来 12 个月/预测）。严禁使用“trailing”或“forward”——始终使用 LTM 或 NTM。LTM 比率使用最近报告的 4 个季度的总和。NTM 比率使用 `get_consensus_estimates_from_identifiers` 返回的**未来 4 个季度一致预期 EPS 均值之和**——而非单一的年度数字。在竞争对手对比表中，必须同时计算并展示 LTM 和 NTM P/E。

**超链接规则（严格执行）：** 报告中的每一项断言——无论是数字还是非数字——都必须包裹在指向附录中相应条目的 `<a href="#ref-N" class="data-ref">` 超链接中。**这并非可选要求。报告中的每一个数字都必须是可点击的链接。** 这包括：营收数据、每股收益 (EPS)、利润率、增长率、市值、市盈率 (P/E)、股价回报率、目标价、分部营收以及任何其他财务指标。这也包括来自会议纪要或 Kensho 搜索的定性断言。只要你将其表述为事实，就必须链接到来源。为每个唯一的断言分配一个顺序参考 ID（`ref-1`, `ref-2` 等）。超链接样式应保持克制——海军蓝色、无下划线、悬停时显示虚线下划线。**严禁在报告正文中书写任何不带 `<a>` 标签的数字。** 例如：书写 `<a href="#ref-1" class="data-ref">$152.3B</a>`，绝不能写成纯文本 `$152.3B`。

---

## 阶段 1：公司概况与准备工作

1. 从 `$ARGUMENTS` 中解析个股代码（去除空格）。
2. 运行 `mkdir -p /tmp/earnings-preview` 创建工作目录。
3. 调用 `get_latest()` 以建立当前的报告期背景。
4. 调用 `get_info_from_identifiers` —— 记录市值、行业。
5. 调用 `get_company_summary_from_identifiers` —— 记录业务描述。
6. 调用 `get_next_earnings_from_identifiers` —— 记录即将到来的业绩发布日期和财季名称。

**立即写入** `/tmp/earnings-preview/company-info.txt`:
```
TICKER: [代码]
COMPANY: [全称]
INDUSTRY: [行业]
MARKET_CAP: [数值] (截至 [日期])
NEXT_EARNINGS_DATE: [日期]
NEXT_EARNINGS_QUARTER: [完全沿用 API 返回的 Q# FY####]
BUSINESS_DESCRIPTION: [2-3 句业务摘要]
```

---

## 阶段 2：业绩会议纪要分析（强制要求 —— 撰写前完成）

1. 调用 `get_latest_earnings_from_identifiers` 获取最近一次已完成业绩会议的 `key_dev_id`。
2. 调用 `get_transcript_from_key_dev_id` 获取该会议纪要。
3. **立即写入** `/tmp/earnings-preview/transcript-extracts.txt` 并包含以下部分。务必在纪要在上下文中时完成此操作：

```
TRANSCRIPT_SOURCE: [会议名称，例如 "Q3 2025 Earnings Call"]
KEY_DEV_ID: [key_dev_id]
CALL_DATE: [日期]
FISCAL_QUARTER: [Q# FY####]

=== 逐字引用 (原文复制 —— 严禁改述) ===
QUOTE_1: "[来自纪要的精确文本]"
SPEAKER_1: [姓名], [职位]
CONTEXT_1: [1 句话说明出现场景 —— 准备发言或问答环节]

QUOTE_2: "[来自纪要的精确文本]"
SPEAKER_2: [姓名], [职位]
CONTEXT_2: [上下文]

QUOTE_3: "[来自纪要的精确文本]"
SPEAKER_3: [姓名], [职位]
CONTEXT_3: [上下文]

QUOTE_4: "[来自纪要的精确文本]"
SPEAKER_4: [姓名], [职位]
CONTEXT_4: [上下文]

=== 业绩指引 (仅限定量数据) ===
- [指标]: [管理层阐述的范围或点估计]
- [指标]: [范围或点估计]

=== 关键驱动因素 ===
- [驱动因素 1 及其支撑数据点]
- [驱动因素 2 及其支撑数据点]
- [驱动因素 3 及其支撑数据点]

=== 逆风与风险 ===
- [风险 1 及其量化数据（如有）]
- [风险 2]

=== 分析师问答主题 ===
- [主题 1: 分析师关注的焦点]
- [主题 2]
- [主题 3]

=== 综合研判: 下季度关注点 ===
- [要点 1]
- [要点 2]
- [要点 3]
```

---

## 阶段 3：竞争对手分析

1. 调用 `get_competitors_from_identifiers`，设置 `competitor_source="all"`。
2. 筛选 **5-7 家最相关的上市竞争对手**。
3. 为目标公司及选定的所有竞争对手收集：
   - `get_prices_from_identifiers`，设置 `periodicity="day"`，获取过去 12 个月数据
   - `get_financial_line_item_from_identifiers` 获取 `diluted_eps`，`period_type="quarterly"`，`num_periods=8`
   - `get_capitalization_from_identifiers` 获取 `capitalization="market_cap"` (最新)
   - `get_consensus_estimates_from_identifiers` 获取 `period_type="quarterly"`，`num_periods_forward=4` —— 这将返回未来 4 个季度的一致预期 EPS 均值，这些值的总和即为 NTM EPS

**每次工具调用返回后，立即将原始数据追加到相应的中间文件中：**

**写入** `/tmp/earnings-preview/prices.csv` —— 每行包含 (ticker, date, close)。包含 `source` 列，记录具体的 MCP 函数调用。首先写入目标公司的价格，然后是各竞争对手的价格：
```
ticker,date,close,source
D,2025-02-19,55.67,get_prices_from_identifiers(identifier='D',periodicity='day')
D,2025-02-20,55.82,get_prices_from_identifiers(identifier='D',periodicity='day')
...
DUK,2025-02-19,111.79,get_prices_from_identifiers(identifier='DUK',periodicity='day')
...
```
注意：同一个调用的所有行 `source` 值相同 —— 每行都写，确保随时可用。

**写入** `/tmp/earnings-preview/peer-eps.csv` —— 每行包含 (ticker, period, eps)。在每次 `diluted_eps` 调用后立即写入：
```
ticker,period,diluted_eps,source
D,Q4 2024,1.09,get_financial_line_item_from_identifiers(identifier='D',line_item='diluted_eps',period_type='quarterly')
D,Q1 2025,-0.11,get_financial_line_item_from_identifiers(identifier='D',line_item='diluted_eps',period_type='quarterly')
...
DUK,Q4 2024,1.52,get_financial_line_item_from_identifiers(identifier='DUK',line_item='diluted_eps',period_type='quarterly')
...
```

**写入** `/tmp/earnings-preview/peer-market-caps.csv` —— 每行一个 ticker。在每次 `market_cap` 调用后立即写入：
```
ticker,market_cap,retrieval_date,source
D,55900000000,2026-02-19,get_capitalization_from_identifiers(identifier='D',capitalization='market_cap')
DUK,98300000000,2026-02-19,get_capitalization_from_identifiers(identifier='DUK',capitalization='market_cap')
...
```

**写入** `/tmp/earnings-preview/consensus-eps.csv` —— 每行包含 (ticker, period, consensus mean EPS)。在每次 `get_consensus_estimates_from_identifiers` 调用后立即写入：
```
ticker,period,consensus_mean_eps,num_estimates,source
D,Q4 2025,0.88,12,get_consensus_estimates_from_identifiers(identifier='D',period_type='quarterly',num_periods_forward=4)
D,Q1 2026,0.72,10,get_consensus_estimates_from_identifiers(identifier='D',period_type='quarterly',num_periods_forward=4)
D,Q2 2026,0.91,9,get_consensus_estimates_from_identifiers(identifier='D',period_type='quarterly',num_periods_forward=4)
D,Q3 2026,1.05,8,get_consensus_estimates_from_identifiers(identifier='D',period_type='quarterly',num_periods_forward=4)
DUK,Q4 2025,1.48,14,get_consensus_estimates_from_identifiers(identifier='DUK',period_type='quarterly',num_periods_forward=4)
...
```

4. **暂时不要计算 P/E 或回报率。** 原始数据已存储在磁盘上。计算将在阶段 6（验证）中通过读取这些文件完成。

**日期一致性规则（股票回报率）：** 计算对比股票回报率（年初至今 %、1 年 %、30 天 %、90 天 %）时，所有代码**必须使用完全相同的起始和结束日期**。在将所有价格数据写入 `prices.csv` 后，找出所有代码数据中共同出现的第一个交易日，并将其作为公共基准日期。严禁由不同代码使用不同的基准日期。如果某个代码的数据开始时间晚于其他代码，则所有计算均使用重叠后的第一个日期。在附录中注明每次回报率计算所使用的公共基准日期。

**市盈率币种规则 (LTM P/E)：** 计算每家公司的 LTM P/E 时，应从 `peer-eps.csv` 中选取该公司**最近报告的 4 个季度**数据 —— 而不是统一的日历窗口。如果某个竞争对手已经报告了 2025 年 Q4，而目标公司仅报告到 2025 年 Q3，则该竞争对手的 LTM EPS 应包含 2025 年 Q4。核对每家公司最新报告的期间，并使用每家公司各自最近的 4 个周期。在附录中注明每个 P/E 计算所使用的 4 个财季。

**市值时间戳：** 报告市值时，使用 `peer-market-caps.csv` 中的 `retrieval_date`。如果该日期与报告日期不同，请在附录中注明。

---

## 阶段 4：新闻、预测与行业情报 (通过 Kensho Grounding)

针对以下**每个**类别运行 `search` 查询。严禁跳过。

**关键点 —— 记录来源 URL：** 每一个 Kensho `search` 结果都包含底层文章、报告或数据页面的**来源 URL**。你必须随带每项发现记录该 URL。

**每次 search 调用后，立即使用以下格式将结果追加到** `/tmp/earnings-preview/kensho-findings.txt`。不要等待所有搜索完成：

```
=== SEARCH: "[所使用的查询词]" ===
DATE_RUN: [当前日期]
CATEGORY: [estimates|analyst_ratings|risks|news|sector]

FINDING_1: [关键发现或摘录]
URL_1: [搜索结果中的来源 URL]
SOURCE_1: [出版物名称，如有日期则注明]

FINDING_2: [关键发现或摘录]
URL_2: [来源 URL]
SOURCE_2: [出版物名称，日期]

[...继续记录该搜索的所有相关结果...]
```

**业绩预测与分析师情绪：**
1. `search` 查询 "[TICKER] earnings estimates consensus EPS revenue upcoming quarter"
   - 记录：一致预期 EPS、一致预期营收、过去 90 天内的预测修订方向。
   - **立即追加到 kensho-findings.txt。**
2. `search` 查询 "[TICKER] analyst ratings price target upgrades downgrades"
   - 记录：近期的评级上调/下调、目标价范围、牛市/熊市逻辑摘要。
   - **立即追加到 kensho-findings.txt。**
3. `search` 查询 "[TICKER] risks bear case concerns investors"
   - 记录：核心争议点、空方论点、影响即将发布的财报的关键变量。
   - **立即追加到 kensho-findings.txt。**

**近期新闻 (强制要求 —— 严禁跳过)：**
4. `search` 查询 "[TICKER] [公司名称] recent news developments"
   - 记录：过去 60 天内的重大新闻 —— 并购、新产品发布、高管变动、监管行动、合作伙伴关系、法律进展、关税或任何可能影响即将发布的财报或业绩指引的事件。
   - 记录每项的日期、标题及潜在的业绩影响。
   - **立即追加到 kensho-findings.txt。**

**行业背景：**
5. `search` 查询 "[公司所属行业] sector outlook trends"
   - 记录：行业层面的利好/利空因素、宏观数据、竞争动态。
   - **立即追加到 kensho-findings.txt。**

---

## 阶段 5：财务数据收集

**季度财务数据 (过去 8 个季度)：**
针对以下指标调用 `get_financial_line_item_from_identifiers`，设置 `period_type="quarterly"`，`num_periods=8`：
`revenue` (营收), `gross_profit` (毛利), `operating_income` (营业利润), `ebitda`, `net_income` (净利润), `diluted_eps` (稀释每股收益)

**每次科目调用返回后，立即追加到** `/tmp/earnings-preview/financials.csv`。逐字写入返回的原始数值 —— 暂时不要进行舍入或单位转换。包含 `source` 列，记录具体的 MCP 函数调用及参数：
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

**暂时不要计算利润率或增长率。** 仅写入原始数据。计算将在阶段 6 进行。

**分部数据：**
- 调用 `get_segments_from_identifiers`，设置 `segment_type="business"`, `period_type="quarterly"`, `num_periods=8`
- 你需要 8 个季度（而非 4 个），以便获得去年同期数据用于同比 (y/y) 比较。计算 2025 年 Q3 的同比需要 2024 年 Q3 —— 即倒数第 5 个季度。**如果 API 响应中不提供去年同期的分部数据，严禁推测或捏造。在报告中注明“同比增长不可用”。**

**立即写入** `/tmp/earnings-preview/segments.csv`:
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

**业绩发布历史 (用于股价图表注释)：**
- 调用 `get_earnings_from_identifiers` —— 收集过去 12 个月股价窗口内的过往业绩发布日期。
- **立即写入** `/tmp/earnings-preview/earnings-dates.csv`:
```
ticker,earnings_date,call_name,source
D,2025-05-02,Q1 2025 Earnings Call,get_earnings_from_identifiers(identifier='D')
D,2025-08-01,Q2 2025 Earnings Call,get_earnings_from_identifiers(identifier='D')
D,2025-10-31,Q3 2025 Earnings Call,get_earnings_from_identifiers(identifier='D')
...
```

---

## 阶段 6：验证与计算（强制要求 —— 严禁跳过）

在生成报告之前，重新读取所有中间文件，并基于清晰的数据进行计算。此阶段通过基于文件工作（而非压缩后的对话上下文）来确保数据完整性。

1. **读取所有中间文件**（使用 bash `cat` 命令）：
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

2. **计算衍生指标**（基于当前上下文中读取的文件数据）：
   - 毛利率 % = 毛利 / 营收 (按季度计算)
   - 营业利润率 % = 营业利润 / 营收 (按季度计算)
   - 营收同比增长 % = (当前季度营收 - 去年同期营收) / 去年同期营收
   - 每股收益同比增长 % = 逻辑同上；如果基数为负则使用 "n.m."
   - 分部同比增长 % = 按名称匹配分部与其去年同期数值；如果缺失则标注“同比不可用”
   - 各公司 LTM P/E = 最新股价 / 最近 4 个季度报告的 EPS 之和（通过 `peer-eps.csv` 核对各代码可用的最近 4 个季度）
   - 各公司 NTM P/E = 最新股价 / NTM EPS，其中 **NTM EPS = 未来 4 个季度一致预期 EPS 均值之和**（来自 `consensus-eps.csv`）。将每个代码未来 4 个季度的 consensus_mean_eps 值相加。如果某个竞争对手可用的前瞻性季度不足 4 个，则将 NTM P/E 标注为 "n/a"。在附录中注明加总了哪 4 个季度。
   - 股票回报率 (年初至今, 1 年, 30 天, 90 天) = 找出 `prices.csv` 中**所有代码共同出现的第一个日期**，然后计算自该日期起的回报率。

3. **交叉核对**：
   - 验证每个分部同比计算是否在 `segments.csv` 中存在真实的去年同期数据。如不存在，标注“同比不可用”。
   - 验证所有代码的股票回报率基准日期是否完全一致。
   - 通过重新加总构成部分来验证任何多步计算（例如，LTM EPS 总和与 4 个季度数值之和相符）。
   - 验证 `transcript-extracts.txt` 中的所有逐字引用均为精确复制（非改述）。

4. **写入** `/tmp/earnings-preview/calculations.csv` 记录所有衍生数值：
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

该文件将成为报告中所有数字的唯一事实来源。

---

## 阶段 7：生成 HTML 报告

**注意 —— 在编写任何 HTML 之前，你必须读取所有中间文件。这是阻塞性的先决条件。**

这并非可选。你必须将以下每个 `cat` 命令作为**独立的 bash 工具调用**运行（严禁合并）。这确保了每个文件的内容都被单独加载并在对话中可见。严禁合并，严禁跳过任何文件。

**每次运行一个命令：**

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

**读取完所有文件后，你必须向用户打印一条摘要消息**，列出每个文件及其状态。必须使用以下精确格式：

```
--- DATA FILE VERIFICATION ---
1. company-info.txt        ✓ 已加载 ([N] 行)
2. transcript-extracts.txt ✓ 已加载 ([N] 行)
3. financials.csv          ✓ 已加载 ([N] 行)
4. segments.csv            ✓ 已加载 ([N] 行)
5. prices.csv              ✓ 已加载 ([N] 行)
6. peer-eps.csv            ✓ 已加载 ([N] 行)
7. peer-market-caps.csv    ✓ 已加载 ([N] 行)
8. consensus-eps.csv       ✓ 已加载 ([N] 行)
9. kensho-findings.txt     ✓ 已加载 ([N] 行)
10. earnings-dates.csv     ✓ 已加载 ([N] 行)
11. calculations.csv       ✓ 已加载 ([N] 行)

所有中间数据文件已成功加载。
正在以文件数据作为唯一事实来源生成报告。
---
```

如果任何文件缺失或为空，请停止操作并告知用户。严禁在缺少数据的情况下生成报告。

**HTML 报告中的每一个数字、引言、来源 URL 和 MCP 函数调用引用都必须来自这些文件 —— 而非来自你对早先对话的回忆。** 文件是唯一的事实来源。早前的对话上下文可能已被压缩或摘要，如果过度依赖将会产生错误。如果某个数据点不在文件中，它就不应出现在报告中。

完整的 HTML 模板、CSS 和 Chart.js 配置请参阅 [report-template.md](report-template.md)。

**强制要求 —— 使用模板辅助函数绘图：**
report-template.md 提供了预制的、经过调试的 Chart.js 辅助函数。你必须使用这些精确的函数来创建图表。严禁编写自定义的内联 Chart.js 代码。辅助函数包括：
- `createRevEpsChart(canvasId, labels, revenueData, epsData, revLabel)` —— 对应图表 1
- `createMarginChart(canvasId, labels, grossMargins, opMargins)` —— 对应图表 2
- `createRevGrowthChart(canvasId, labels, growthData)` —— 对应图表 3
- `createAnnotatedPriceChart(canvasId, labels, prices, earningsDates, ticker)` —— 对应图表 5
- `createCompPerfChart(canvasId, labels, datasets)` —— 对应图表 6
- `createPEChart(canvasId, companies)` —— 对应图表 7

每个图表调用必须放在独立的 `<script>` 标签中，并包裹在 try-catch 块中。这确保了某个图表的错误不会阻碍其他图表的渲染。示例：
```html
<script>
try {
  createRevEpsChart('chart-rev-eps', [...], [...], [...], '营收 ($B)');
} catch(e) { console.error('Figure 1 error:', e); }
</script>
<script>
try {
  createMarginChart('chart-margins', [...], [...], [...]);
} catch(e) { console.error('Figure 2 error:', e); }
</script>
```

### 报告结构 (共 4-5 页)

报告分为两部分：**核心逻辑与论述** (1-2 页) 和 **图表与数据** (3-5 页)。确保这两部分有机整合。

---

**AI 免责声明 (强制要求 —— 必须在 3 处显示)：**
你必须在报告 HTML 中包含以下免责说明文本。这是必选内容 —— 否则报告是不完整的：

> **"分析由 AI 生成 —— 请核实所有输出结果"**

必须出现在以下 3 个精确位置：
1. **页眉横幅** —— 紧接封面标题之前，作为一个居中的黄色横幅：`<div class="ai-disclaimer">分析由 AI 生成 —— 请核实所有输出结果</div>`
2. **页脚** —— 在 page-footer div 内部，作为一个显著的黄色横幅：`<div class="footer-disclaimer">分析由 AI 生成 —— 请核实所有输出结果</div>`
3. **附录** —— 作为附录部分的第一行，表格之前：`<div class="ai-disclaimer">分析由 AI 生成 —— 请核实所有输出结果</div>`

---

**第 1 页: 封面与核心观点**

- **AI 免责声明横幅** (黄色, 居中 —— 见 AI 免责声明规则)
- **页眉**: 公司名称 (TICKER) | 行业 | 报告日期
- **标题**: 具有主题性，针对特定财季 (例如: "Walmart Inc. (WMT) Q4 FY2026 业绩前瞻: 节日丰收季 —— Furner 的首份财报能否证实 1 万亿美元市值论调？")
- **执行摘要/核心观点** (最多 2-3 个短段落，配合要点):
  - 用 1-2 句话阐述对本次财报的预期
  - 4-6 个要点，涵盖：我们的 EPS 预测 vs 一致预期、指引预期、关键监测指标、股价驱动因素、核心争议点
  - 风格直接且鲜明 —— 给出观点，不要模棱两可
- **管理层核心引言**: 从最近一次业绩会议中挑选 3-4 条核心引言，有机地穿插在论述中。不要单独设置标题。将它们作为支持你核心观点的证据自然融入。格式采用缩进的块引用 (blockquote)。

---

**第 2 页: 预测、主题与新闻**

- **一致预期表格** (单张表格，标注为图表):
  - 列: 指标 | 一致预期 | 我们的预测 | 同比变动
  - 行: 营收、EPS、毛利率、营业利润，以及 2-3 个该公司特有的关键 KPI (例如: 同店销售、电商增长、会员收入 —— 市场对该公司最关心的指标)
  - **颜色规则是机械化的:** 如果同比变动值为负，使用 `class="neg"` (红色)。如果为正，使用 `class="pos"` (绿色)。如果为零或不适用，使用 `class="neutral"`。数值符号直接决定类名 —— 严禁根据解读进行干预。-1.1% 永远是红色，即使降幅很小。
  - 这是报告中唯一的指引/预测部分。不要在其他地方重复预测数据。

- **超越 EPS 的关键指标** (列表, 3-5 项):
  - 除了 EPS 数字外，决定该季度表现优劣的特定指标
  - 对每一项: 说明该指标是什么、一致预期/管理层预期是多少、为什么它很重要
  - 表达要具体: "Walmart Connect 广告收入增长 (一致预期约 30% y/y, 三季度为 33%)"

- **近期重点关注主题** (3-5 个要点):
  - 针对即将发布的报告的前瞻性项目
  - 管理层需要兑现的内容、可能出现的惊喜、空方关注的焦点
  - 每个主题: 最多 1-2 句话

- **近期新闻与进展** (3-5 个要点):
  - 过去 60 天内的重大新闻，每条一行
  - 日期 + 标题 + 简述影响评估
  - 仅包含可能影响即将发布的财报或指引的项目

---

**第 3-5 页: 图表与表格 (所有图表和表格)**

所有图表依序编号。每个图表都有标题和来源说明。

- **图表 1: 季度营收与稀释每股收益 (EPS)** —— 柱状/折线组合图，展示 8 个季度数据
- **图表 2: 利润率趋势 (毛利率与营业利润率 %)** —— 双折线图，8 个季度
- **图表 3: 营收同比增速 %** —— 带有红绿条件变色的柱状图。**仅包含当前及去年同期数据均存在的季度** (通常是抓取的 8 个季度中的最近 4 个)。严禁包含无法计算同比的季度 —— 图表应显示 4 根柱子，而非 8 根。
- **图表 4: 业务分部营收** —— 表格: 分部名称 | 最新季度营收 ($M) | 占比 % | 同比变动
- **图表 5: 1 年期股价图与业绩发布日期标注** —— 股价曲线，在业绩发布日带有垂直标注线，注明财季及发布后首日的股价变动
- **图表 6: 与竞争对手的股票表现对比 (基准 100)** —— 多折线图，目标公司为粗实线，竞争对手为细虚线
- **图表 7: 滚动市盈率 (LTM P/E) 竞对比对** —— 横向柱状图，目标公司以海军蓝色突出显示
- **图表 8: 竞争对手对比全表** —— 代码 | 公司名称 | 市值 | LTM P/E | NTM P/E | 年初至今 % | 1 年 %

---

**附录: 数据来源与计算说明 (强制要求 —— 严禁跳过或简化)**

附录必须以 AI 免责声明横幅开始: `<div class="ai-disclaimer">分析由 AI 生成 —— 请核实所有输出结果</div>`

报告的最后一页必须包含一个附录表，记录报告中引用的**每一个断言** —— 无论是数值还是非数值。**报告正文中出现的每一个数字在附录中必须有对应的行，且报告正文中的每一个此类数字必须是一个可点击的 `<a href="#ref-N">` 超链接，点击后滚动至其附录行。** 如果报告中的数字没有链接到附录，报告则不完整。

- **表格列**: 参考号 (Ref #) | 事实说明 | 数值 | 来源与推导过程
- **参考号 (Ref #)**: 与报告正文超链接相匹配的顺序 ID (`ref-1`, `ref-2` 等)。每行带有一个 `id="ref-N"` 属性以便超链接跳转。
- **事实说明**: 易读的标签 (例如, "Q3 FY2026 营收", "LTM P/E —— WMT", "管理层指出关税逆风", "巴克莱银行上调至持股观望")
- **数值**: 报告中显示的精确数据 (例如, "$152.3B", "24.5%", "28.1x")。对于非数值事实，留空或填写 "N/A"。
- **来源与推导过程**: 这是最关键的一列。**每一行必须有具体的、详细的来源说明 —— 而不仅仅是一个标签。** 严格遵守以下规则：

  **对于来自 S&P Capital IQ 的原始财务数据 (营收、EPS、毛利、营业利润、净利润、EBITDA、价格、市值等):**
  - 说明所使用的 MCP 函数及其关键参数。格式：`S&P Capital IQ — [函数名](identifier='[代码]', line_item='[项目]', period_type='[类型]', period='[Q# FY####]')`
  - 示例：
    - `S&P Capital IQ — get_financial_line_item_from_identifiers(identifier='WMT', line_item='revenue', period_type='quarterly', period='Q3 FY2026')`
    - `S&P Capital IQ — get_financial_line_item_from_identifiers(identifier='WMT', line_item='diluted_eps', period_type='quarterly', period='Q3 FY2026')`
    - `S&P Capital IQ — get_prices_from_identifiers(identifier='WMT', periodicity='day')`
    - `S&P Capital IQ — get_capitalization_from_identifiers(identifier='WMT', capitalization='market_cap')`
  - **严禁仅写 "S&P Capital IQ" 而不提供详情。** 读者必须知道究竟是哪个工具调用的哪个数据点产出了这个数字。

  **对于计算出的数值 (利润率、增长率、P/E、回报率、同比变动):**
  - 显示完整公式，并包含**超链接构成的组件** —— 每个组件必须是一个指向该原始数据附录行的 `<a href="#ref-N">` 链接。这至关重要：读者必须能够从计算结果点击进入其每一项输入值。
  - 示例：`毛利率 = <a href='#ref-5'>毛利 $37.2B</a> / <a href='#ref-1'>营收 $152.3B</a> = 24.4%。来源: S&P Capital IQ (计算所得)`
  - 示例：`LTM P/E = <a href='#ref-20'>股价 $172.35</a> / (<a href='#ref-8'>Q1 EPS $1.47</a> + <a href='#ref-9'>Q2 EPS $1.84</a> + <a href='#ref-10'>Q3 EPS $1.53</a> + <a href='#ref-11'>Q4 EPS $1.80</a>) = $172.35 / $6.64 = 25.9x`
  - 示例：`营收同比增速 = (<a href='#ref-12'>Q3 FY26 营收 $165.8B</a> - <a href='#ref-3'>Q3 FY25 营收 $160.8B</a>) / <a href='#ref-3'>Q3 FY25 营收 $160.8B</a> = +3.1%`
  - **公式中的每一个构成组件都必须是可点击的超链接。** 严禁在公式中使用纯文本数字。

  **对于源自业绩会议纪要的断言 (引言、管理层评价、指引):**
  - 写下纪要中的**原话句子**。
  - 引用纪要的全称以及获取它所使用的 `key_dev_id`。
  - 格式：`"[逐字引用]" —— [发言人], [职位]. 来源: [Q# FY#### 业绩会议纪要] (key_dev_id: [ID])`
  - 示例：`"我们预计 Q4 的同店销售增长为 3-4%" —— 首席执行官 John Furner. 来源: Q3 FY2026 业绩会议纪要 (key_dev_id: 12345678)`

  **对于 Kensho Grounding 搜索结果 (新闻、分析师评级、一致预期):**
  - 写下搜索结果中的关键发现或摘要。
  - **强制要求: 包含 Kensho `search` 工具返回的来源 URL**，形式为可点击的 `<a href="[URL]" target="_blank">` 超链接。这是最重要的部分 —— 读者必须能够点击进入原始来源。
  - 格式：`"[发现/摘要]" —— <a href="[URL]" target="_blank">[来源标题或出版物名称]</a>. 查询词: search("[所用查询词]")`
  - 示例：`"巴克莱银行于 2026 年 1 月 15 日将 WMT 上调至增持评级，目标价 210 美元。" —— <a href="https://www.investing.com/news/barclays-upgrades-wmt" target="_blank">Investing.com, 2026 年 1 月 15 日</a>. 查询词: search("WMT analyst ratings price target upgrades downgrades")`
  - 如果特定结果没有返回 URL，请写上“来源 URL 不可用”，但仍需保留搜索查询词。

**完整性检查：** 在最终确定报告前，扫描报告正文中的每一个数字。如果有任何数字没有包裹在 `<a href="#ref-N" class="data-ref">` 中，请修正。如果任何附录行的“来源与推导过程”仅仅是一个简单的标签（如“S&P Capital IQ”）而没有函数调用详情，请修正。如果任何计算值的公式缺少超链接组件，请修正。如果任何源自 Kensho 的断言缺少来源 URL，请修正。

按板块对附录行进行分组（财务数据、估值、预测与一致预期、会议纪要断言、新闻与分析师评论、股票表现），并设置子标题。使用较小的字体（10-11px）。

---

## 阶段 8：输出

1. 将完整的 HTML 文件写入当前工作目录下的 `earnings-preview-[TICKER]-YYYY-MM-DD.html`。
2. 在浏览器中打开它：`open earnings-preview-[TICKER]-YYYY-MM-DD.html`
3. 告知用户文件已创建，并简要总结核心发现。

---

## 撰写规范

- **严禁使用表情符号**: 不在报告的任何地方使用表情符号。这是一份专业的深度研究文档。
- **精炼**: 目标为 4-5 个打印页。每一句话都必须有其实际价值。尽可能使用要点而非段落。如果某个章节显得冗长，请删减。
- **数据具体化**: 使用“营收 524 亿美元，同比增长 5.2%”，而非“营收增长强劲”。
- **给出观点**: 这是一份业绩前瞻报告，而不是摘要，说明你期望什么、什么最重要以及为什么。观点要鲜明，但必须有数据支撑。
- **管理层引言不设页眉**: 将最近一次会议的 3-4 条管理层引言直接作为块引用融入叙述中。不要创建“管理层关键引言”之类的章节标题 —— 让它们作为证明你核心观点的证据自然呈现。
- **专业口吻**: 采用卖方权益研究风格 —— 具分析性、直接、数据驱动。
- **图表必须使用真实数据**: 每个图表都必须填充真实的 MCP 数据。严禁捏造。
- **竞争对手语境**: 结合竞对情况来阐述估值。如果你不知道竞对的 P/E 是 20 倍还是 35 倍，那么 25 倍的 P/E 就没有任何参考意义。
- **带链接的断言**: 报告正文中的每一项事实断言 —— 无论是数值还是定性描述 —— 都必须是一个链接到其附录条目的 `<a class="data-ref">` 标签。数字：`<a href="#ref-1" class="data-ref">$152.3B</a>`。定性：`<a href="#ref-25" class="data-ref">管理层指出关税逆风是主要的利润率风险</a>`。附录中如果没有可溯源的来源，该事实就不应出现在报告中。

> **💡 Appendix: 领域知识小贴士**
>
> 欢迎来到专业的金融研究世界！如果你是第一次读这类报告，这里有几个核心概念可以帮你快速上手：
>
> 1.  **LTM vs NTM (过去与未来)**：这是投资者看公司估值时最常用的两个视角。**LTM (Last Twelve Months)** 是“往后看”，用公司过去一年实打实赚到的钱来计算市盈率；而 **NTM (Next Twelve Months)** 是“往前看”，用分析师们预测公司未来一年能赚多少钱来计算。通常 NTM 更重要，因为股票买的是公司的未来。
> 2.  **一致预期 (Consensus Estimate)**：你可以把它理解为市场上几十位专业分析师对公司业绩给出的“平均分”。如果公司的实际表现超过了这个平均分，股价通常会上涨；反之则可能下跌。
> 3.  **业绩指引 (Guidance)**：这是公司管理层亲自给出的预测。由于他们最了解公司，所以这份“自报家门”的预测往往被视为市场上最重要的参考坐标。
> 4.  **同比 (y/y)**：即“与去年同一时期相比”。在金融界，我们很少拿这季度和上季度比（因为有季节性因素，比如零售商冬天卖得总比夏天好），而是拿今年冬天和去年冬天比，这样才能看出公司是否真的在变强。
> 5.  **稀释每股收益 (Diluted EPS)**：这是最纯粹的盈亏指标。它告诉股东，如果公司所有的期权等潜在股份都变成了股票，你手里的每份股票到底能分到多少利润。
