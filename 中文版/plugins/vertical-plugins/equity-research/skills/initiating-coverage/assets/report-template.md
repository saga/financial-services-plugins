# 股票研究首次覆盖报告模板

该模板用于指导撰写一份完整的首次覆盖股票研究报告。它定义了建议的章节结构、页面布局、图表要求和格式标准。最终正式交付物应为 Word 文档，而不是 Markdown 文件。

**注意：** 最终报告必须使用 DOCX / DOC 技能生成，不要直接把 Markdown 当作成品交付。

## 核心要求

1. 在生成 Word 文档之前，先用 Python 生成 **20-30 张以上图表图片**。
2. 使用 DOCX 技能创建正式报告，并保证样式、页眉页脚、目录和分页符合专业研究报告标准。
3. 图表必须以真实 PNG / JPG 文件形式嵌入文档，而不是仅保留“图表占位符”文字。
4. 整体报告应保持高信息密度，避免大面积空白、单独悬空的章节标题，或一整页只有一张图。
5. 所有图表和表格都必须使用连续的 **Figure 编号**，并附带 **Source 来源行**。

## 总体排版原则

- **高密度信息呈现**：每页通常应同时包含文字、图表、表格中的至少两类元素。
- **避免孤立内容**：不要让章节标题单独占一页，也不要让单张图表独占整页。
- **图文交错排布**：图表应该嵌入分析叙述之中，而不是全部堆放在文末。
- **统一视觉体系**：标题层级、字号、表格样式、图例风格与配色要在全文保持一致。
- **数据优先**：能用数字说明，就不要用空泛描述。

---

## 第 1 页：Investment Update（最关键页面）

第 1 页不是传统意义上的“执行摘要”，而应是专业股票研究报告中常见的 **Investment Update / Company Update** 页面。

### 页面结构

**左上角：评级框**

```text
Rating:             [OUTPERFORM / NEUTRAL / UNDERWEIGHT / ...]
Price ([Date]):     $[XX.XX]
Target Price:       $[XX.XX]
52-Week Range:      $[XX.XX] - $[XX.XX]
Market Cap:         $[XX.X]B
Enterprise Value:   $[XX.X]B
```

**左上角补充：分析师信息**

```text
[分析师姓名], [资质]
[邮箱] | [电话]

[第二分析师姓名], [资质]
[邮箱] | [电话]
```

**右上角：股价表现图**

```text
Figure 1 - [Company Name] Stock Price Performance
[展示过去 12-24 个月股价与基准指数对比]
Source: Company data, [Firm Name] estimates.
```

**中部：推荐栏**

```text
[OUTPERFORM / NEUTRAL / ...] RECOMMENDATION / COMPANY UPDATE
```

**主体：3-4 条详细投资要点**

建议使用 `■` 作为项目符号。每一条都应采用以下结构：

```text
■ **[加粗主题句，直接点明核心结论]。** 后接 3-5 句展开说明，尽量包含关键数字、同比 / 环比对比、业务含义和估值影响。
```

每条重点建议覆盖以下内容中的至少两项：

- 业务进展或经营表现
- 市场空间 / TAM
- 竞争优势或壁垒
- 利润率、增长率、现金流等量化指标
- 未来 12 个月的催化剂

**底部：关键财务与估值表**

```text
                            [Year-3]A   [Year-2]A   [Year-1]A   [Year]E   [Year+1]E
Revenue ($M)                [X]         [X]         [X]         [X]       [X]
Revenue Growth (%)          X.X%        X.X%        X.X%        X.X%      X.X%
Gross Margin (%)            X.X%        X.X%        X.X%        X.X%      X.X%
EBITDA ($M)                 [X]         [X]         [X]         [X]       [X]
EBITDA Margin (%)           X.X%        X.X%        X.X%        X.X%      X.X%
EPS ($)                     X.XX        X.XX        X.XX        X.XX       X.XX
P/E (x)                     XX.Xx       XX.Xx       XX.Xx       XX.Xx      XX.Xx
EV/Revenue (x)              X.Xx        X.Xx        X.Xx        X.Xx       X.Xx
EV/EBITDA (x)               XX.Xx       XX.Xx       XX.Xx       XX.Xx      XX.Xx
```

其中：

- `A` 表示实际值（Actual）
- `E` 表示预测值（Estimate）

---

## 图表编号规范

全文所有图表、表格和可视化对象都必须采用连续编号：

- `Figure 1`
- `Figure 2`
- `Figure 3`
- ...

统一格式如下：

```text
Figure X - [描述性标题]
[图表或表格]
Source: Company data, [Firm Name] estimates.
```

如数据来源不止一个，可写为：

```text
Source: Company filings, FactSet, [Firm Name] estimates.
```

编号规则：

- 按正文出现顺序编号
- 第 1 张通常是股价图或营收增长图
- 图题应紧邻图表
- 来源行建议使用较小字号并放在图表底部

---

## 第 2 页：目录

目录应覆盖主要章节与页码，例如：

```text
Investment Update....................................................1
Investment Thesis & Risks...........................................3
Company Overview....................................................6
Growth Outlook & Drivers...........................................13
Financial Analysis & Performance..................................16
Industry Overview & Competitive Landscape........................21
Valuation Analysis.................................................27
Appendices & Disclosures..........................................31
```

---

## 第 3-5 页：投资逻辑与风险

### Investment Thesis

建议拆分为 3-5 个核心支柱，每个支柱包含以下四部分：

1. **一句话结论**：清晰点明该逻辑的核心。
2. **现状与证据**：例如客户表现、增长速度、市场份额、留存率等。
3. **为什么能赢**：说明产品、渠道、品牌、技术、监管、规模等方面的优势。
4. **财务映射**：说明该逻辑将如何体现在营收增长、利润率扩张或估值提升上。

每个支柱之间建议穿插 1 张图表，例如：

- TAM 增长图
- 竞争定位矩阵
- 利润率扩张路径图
- 客户分层 / 产品渗透率图

### Risks

建议将风险分为两类：

**公司特有风险**

- 客户集中度
- 产品路线图执行风险
- 商业化节奏不及预期
- 管理层依赖

**行业 / 市场风险**

- 监管变化
- 竞争加剧
- 宏观需求疲软
- 定价压力

每条风险建议控制在 2-4 句，并尽量附带量化说明或缓释因素。

---

## 第 6-12 页：Company 101 / 公司基础画像

### 公司描述

用 3-4 段文字清晰回答：

- 公司做什么
- 主要产品或服务是什么
- 如何赚钱
- 客户是谁
- 地域覆盖如何
- 当前体量多大

建议配图：

- 商业模式示意图
- 收入结构图
- 业务流程图

### 公司历史

建议包括：

- 创立背景
- 关键融资节点
- 产品上线节点
- 战略转折点
- 当前阶段定位

可使用时间轴图呈现。

### 管理层与股权结构

对关键管理层逐一说明：

- 当前职位与职责
- 过往经历
- 关键成就
- 教育 / 资质背景

如披露充分，还应补充：

- 董事会结构
- 股权持有情况
- 主要投资方
- Insider ownership 趋势

### 核心产品与技术

对每个主要产品说明：

- 产品功能
- 目标客户
- 定价方式
- 竞争定位
- 当前业务进展 / 采用情况

推荐图表：

- 产品组合矩阵
- 技术平台结构图
- 产品路线图时间轴

### 客户与渠道

建议覆盖：

- 客户数量与客户分层
- 地域分布
- 主要行业或终端市场
- 销售模式（直销 / 渠道 / 合作伙伴）
- 客户留存、扩张率、LTV/CAC 等关键指标

---

## 第 13-15 页：增长前景（Growth Outlook）

从短期（1-2 年）与中期（3-5 年）拆解增长驱动：

- 新产品放量
- 老产品渗透率提升
- 地理扩张
- 定价提升
- 渠道扩张
- 行业景气上行

每个增长驱动建议采用如下结构：

1. 当前状态
2. 机会空间
3. 路径与里程碑
4. 风险与限制条件

推荐图表：

- Revenue Bridge
- 市场份额变化图
- 产品路线图
- 地域扩张图
- Bull / Base / Bear 场景图

---

## 第 16-20 页：财务分析与业绩表现

这是报告中最需要高密度呈现的部分之一，建议每页都包含多个元素。

### 历史财务分析

至少展示 3-5 年历史数据：

- Revenue
- Gross Profit / Gross Margin
- EBITDA / EBITDA Margin
- Net Income
- Free Cash Flow

### 关键图表（必须重点覆盖）

1. **Revenue Growth Trajectory**：历史与预测营收增长曲线
2. **Revenue by Product / Segment**：按产品或业务条线拆分的收入结构图
3. **Revenue by Geography**：按地区拆分的收入结构图
4. **Gross Margin Evolution**：毛利率演变
5. **Operating / EBITDA Margin Trend**：经营利润率或 EBITDA 利润率趋势
6. **Free Cash Flow Generation**：自由现金流与 FCF Margin
7. **Key Operating Metrics Dashboard**：客户数、ARPU、NRR、LTV/CAC 等

### 前瞻预测

展示未来 3-5 年的财务预测表，并列明关键假设：

- Revenue growth drivers
- Margin assumptions
- CapEx assumptions
- Working capital assumptions

如是私营公司，也可在这一节补充：

- 融资历史
- 估值演进
- 当前隐含倍数

---

## 第 21-26 页：行业概览与竞争格局

### 行业定义与市场空间

建议说明：

- 行业边界与定义
- 当前市场规模
- 历史增长率
- 长期驱动因素
- TAM / SAM / SOM

### 竞争格局

建议包括：

- 主要竞争对手对比表
- 竞争定位矩阵
- 市场份额图
- 市场份额演进趋势图

竞争分析应尽量回答：

- 公司相对竞争对手的强弱势
- 护城河来自哪里
- 是否存在份额提升逻辑
- 行业竞争是否趋于激烈

### 行业动态

可加入：

- Porter's Five Forces 框架
- 监管变化
- 技术趋势
- 客户采购行为变化

---

## 第 27-31 页：估值分析

### 估值方法总览

建议至少包含以下一种或多种方法：

- DCF
- Trading Comparables
- Precedent Transactions

### DCF 分析

建议展示：

- 核心假设（WACC、终值增长率、长期利润率等）
- DCF 敏感性分析表
- 估值桥图
- Bear / Base / Bull 三种情景

### 可比公司估值

建议使用两段式表格：

1. 同业公司逐项数据
2. Max / 75th / Median / 25th / Min 统计区间

常见指标包括：

- EV / Revenue
- EV / EBITDA
- P / E
- Revenue Growth
- EBITDA Margin

### Football Field

最终建议加入估值 football field，展示不同估值方法对应的区间，并标出当前股价。

---

## 第 32 页以后：附录与披露

建议包含：

- 详细模型补充
- 管理层补充资料
- 产品补充说明
- 行业数据来源
- 分析师认证
- 监管披露
- 法律披露

---

## 图表清单建议（目标 20-30+ 张）

### 第 1 页

- 股价表现图
- 关键经营指标摘要图
- 利润率 / 定位辅助图

### 投资逻辑页

- TAM 图
- 竞争定位图
- 利润率路径图

### 公司画像页

- 商业模式图
- 时间轴
- 组织结构图
- 产品矩阵图
- 客户分层图
- 地域分布图

### 增长展望页

- Revenue Bridge
- 产品路线图
- 市场份额变化图
- 场景分析图

### 财务页

- Revenue trajectory
- Revenue by segment
- Revenue by geography
- Gross margin evolution
- EBITDA margin trend
- FCF chart
- Operating metrics dashboard

### 行业页

- 市场规模演进图
- 市场份额图
- TAM 分层图
- 行业趋势图

### 估值页

- DCF sensitivity
- DCF waterfall
- Peer valuation chart
- Trading comps scatter
- Football field

---

## 图表风格建议

- 全文采用统一配色，建议 3-5 个主色
- 使用专业、清晰的字体，如 Arial / Calibri
- 图表必须有清晰标签、图例与单位
- 每张图底部都有来源说明
- 可适当添加标注文字，用于突出关键结论
- 在不牺牲可读性的前提下尽量提高信息密度

---

## 使用模板时的注意事项

1. **第 1 页最重要**：必须在一页内呈现投资建议、目标价、关键财务信息和核心逻辑。
2. **高密度胜于空泛**：报告应像专业卖方研究一样信息饱满。
3. **不要出现孤立章节**：标题之后必须紧跟内容。
4. **图表是核心，不是装饰**：整份报告至少应包含 20-30 张真实图表。
5. **图表必须嵌入正文**：不要把所有图表集中放到一两个附录页。
6. **优先使用具体数字**：例如增长率、市场规模、客户留存率、估值倍数。
7. **保持客观**：同时呈现正面与负面因素。
8. **执行摘要建议最后写**：虽然它放在第 1 页，但应在完成全文后再回写。
9. **所有数据都要有来源**：正文中的关键数据、表格、图表都应标注出处。
10. **最终文档必须复核**：尤其是财务模型、估值、图表编号和页码。
