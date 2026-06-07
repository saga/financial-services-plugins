# 行业种子公司参考表

当用户指定行业但未指定具体公司时，使用以下种子列表引导公司发现。这些只是起点——务必通过 `get_competitors_from_identifiers` 扩展，并通过 `get_info_from_identifiers` 验证。

> **以下所有种子已通过 S&P Global 标识符系统验证。** 如果种子无法解析，请先尝试括号中的别名再放弃。

## 科技 / 软件

### AI / 机器学习
种子：OpenAI、Anthropic、Databricks、Scale AI、Cohere、Hugging Face、Mistral AI、xAI、Perplexity AI、Runway ML（别名："Runway AI, Inc."）、Together AI（别名："Together Computer, Inc."）、Character.ai（别名："Character Technologies, Inc."）、Groq、Stability AI、Aleph Alpha、Magic AI

⚠️ **排除项（勿用作种子）：**
- *Inflection AI* — 核心团队被 Microsoft 吸收（2024年3月）。历史融资轮存在但已无新活动。
- *Adept AI* — 大部分被 Amazon 吸收（2024年）。同上。
- *DeepMind* — Alphabet 子公司。无独立融资轮。

### 网络安全
种子：CrowdStrike、Palo Alto Networks、Wiz、Snyk、SentinelOne、Abnormal Security、Netskope

### 云基础设施 / 开发工具
种子：Snowflake、HashiCorp、Datadog、Confluent、Vercel、Supabase、PlanetScale

### 金融科技（Fintech）
种子：Stripe、Plaid、Brex、Ramp、Mercury、Affirm、Marqeta、Navan

### 垂直 SaaS
种子：ServiceTitan、Toast、Procore、Veeva Systems、Blend Labs

## 医疗 / 生命科学

### 生物科技 / 制药
种子：Moderna、BioNTech、Recursion Pharmaceuticals、Tempus AI、Insitro、AbCellera

### 数字健康
种子：Teladoc、Hims & Hers、Ro、Noom、Color Health

⚠️ **排除项（勿用作种子）：**
- *Cerebral* — 仍在运营但面临重大监管问题；仅在用户特别要求时使用。

### 医疗设备
种子：Intuitive Surgical、Butterfly Network、Outset Medical

⚠️ **排除项（勿用作种子）：**
- *Shockwave Medical* — 被 Johnson & Johnson 收购（2024年5月）。现为子公司，无独立融资轮。

## 能源 / 气候

### 气候科技
种子：Redwood Materials、Form Energy、Commonwealth Fusion、Sila Nanotechnologies、Climeworks

### 清洁能源
种子：Enphase Energy、First Solar、Rivian、QuantumScape、Sunnova

## 消费

### 电商 / 交易市场
种子：Shopify、Faire、Whatnot、Fanatics

⚠️ **排除项（勿用作种子）：**
- *Temu（PDD Holdings）* — PDD Holdings 是大型上市公司，其融资活动通过股权市场而非风险融资。

### 社交 / 媒体
种子：Discord、Reddit、Substack

⚠️ **排除项（勿用作种子）：**
- *BeReal* — 被 Voodoo 收购（2024年6月）。现为子公司。
- *Lemon8* — 品牌名 "Lemon8" 在 S&P Global 中解析为一家小型荷兰公司（Lemon8 B.V.），**不是**字节跳动的社交应用。字节跳动的应用均为子公司，无独立融资轮。

## 工业 / 物流

### 物流 / 供应链
种子：Flexport、Samsara、Project44、FourKites

⚠️ **排除项（勿用作种子）：**
- *Convoy* — 停止运营（2023年10月）。标识符仍在且历史融资轮可用，但不会再出现新活动。

### 机器人 / 自动化
种子：Figure AI、Agility Robotics、Locus Robotics、Symbotic、Covariant

### 航天 / 航空
种子：SpaceX、Relativity Space、Rocket Lab、Planet Labs、Astra

## 标识符别名参考

一些知名品牌名称与 S&P Global 的法律实体名称不匹配。如果品牌名在 `get_info_from_identifiers` 中返回空结果，请尝试别名：

| 品牌名 | S&P Global 法律实体名 | company_id |
|---|---|---|
| Together AI | Together Computer, Inc. | C_1860042219 |
| Character.ai | Character Technologies, Inc. | C_1829047235 |
| Runway ML | Runway AI, Inc. | C_633706980 |
| Adept AI | Adept AI Labs Inc. | C_1780739313 |
| xAI | X.AI LLC | C_1863863313 |

> **提示：** 品牌名解析失败时，尝试使用法律实体名。如果仍然失败，该公司可能尚未被索引。最后手段是直接使用 `company_id` 作为标识符。

## 备注

- 这些列表偏向美国公司。对于地理筛选（欧洲、亚洲等），竞争对手扩展步骤尤为重要。
- 对于未在此列出的利基子行业，请用户提供 2-3 家示例公司作为种子。
- 始终验证种子是否仍然活跃/相关——公司会转型、合并或倒闭。
- **更新频率：** 这些种子应每季度审核一次。AI 行业的种子变化尤为迅速，因为并购和新进入者频繁。
- 标记为子公司或被收购的种子在 `get_info_from_identifiers` 中仍会解析（状态 = "Operating Subsidiary"），但返回的融资轮数为零。对融资查询跳过这些公司。

---

## 📖 本篇金融知识小贴士

**种子公司（Seed Companies）**：作为行业分析起点的代表性公司。比如分析"AI 行业"时，从 OpenAI、Anthropic 这些知名公司出发，再通过竞争对手扩展找到更多相关公司。

**S&P Global 标识符系统**：S&P Global 用 `company_id`（如 C_1860042219）等独特代码标识公司。品牌名和法律实体名可能不同——比如"Together AI"的法律名是"Together Computer, Inc."。

**尽职调查规则 0**：调用任何数据工具之前，先用 `get_info_from_identifiers` 确认公司标识符能正确解析。这步叫"预验证"，能避免绝大多数数据为空的问题。

**子公司（Subsidiary）**：被其他公司全资控股的公司。如 DeepMind 是 Alphabet 的子公司。它们没有独立的融资数据——融资事件记录在母公司层面。

**状态字段（status）**：`get_info_from_identifiers` 返回的一个重要字段。"Operating"= 可以查询。"Operating Subsidiary"= 子公司，融资轮数为零。

**用户指定 vs 自动扩展**：用户可以亲自指定想看的公司，也可以让工具从行业种子自动扩展找到更多公司。两种方式都在这个流程中支持。

---

## Appendix: 金融背景知识

本文件是 S&P Global Funding Digest 技能的行业种子列表，覆盖 AI、网络安全、金融科技、生物科技、清洁能源、电商、机器人等 14+ 个热门赛道。本附录将系统介绍风险投资行业、融资轮次、公司生命周期、估值方法、退出机制等核心概念。

---

### 1. 风险投资（VC）行业全景

#### 1.1 什么是风险投资

**定义**：风险投资（Venture Capital，VC）是一种私募股权融资形式，VC 基金向具有高增长潜力的初创公司提供资金，交换公司股权，期待未来通过 IPO 或并购退出获得高额回报。

**VC 的本质特点**：

| 特点 | 说明 |
|------|------|
| **高风险高回报** | 90% 的初创公司失败，10% 的成功案例需覆盖整体损失 |
| **长期持有** | 通常 5-10 年，耐心资本 |
| **主动参与** | 不只是给钱，还提供战略、人才、客户资源 |
| **分阶段投资** | 分轮次投资，根据进展决定是否继续 |
| **股权稀释** | 创业者让出部分股权换取资金 |
| **优先清算权** | 退出时 VC 优先于普通股股东获得回报 |

#### 1.2 VC 行业生态

```
创业者（Founder）
   ↓
种子投资人（Angel / Seed VC）
   ↓
早期 VC（A/B 轮）
   ↓
成长期 VC（C 轮+）
   ↓
Pre-IPO 投资人
   ↓
二级市场（IPO 上市）
   ↓
散户 / 机构投资者
```

**主要参与方**：

| 类型 | 英文 | 角色 | 典型机构 |
|------|------|------|---------|
| **天使投资人** | Angel Investor | 个人早期投资人 | 创业者、富豪、Super Angel |
| **种子基金** | Seed Fund | 种子轮专业基金 | Y Combinator、500 Startups |
| **早期 VC** | Early-stage VC | A/B 轮投资 | Sequoia、a16z、Accel |
| **成长期基金** | Growth Fund | C 轮及以后 | General Atlantic、Tiger Global |
| **企业风投** | CVC | 大公司战投部门 | Google Ventures、Salesforce Ventures |
| **超级加速器** | Accelerator | 批量孵化+小额投资 | Y Combinator、Techstars |
| **政府基金** | Sovereign Fund | 主权财富基金 | GIC、淡马锡、PIF |

**美国 VC 第一梯队（"TOP 10"）**：
- **Sequoia Capital**（红杉）——投资过苹果、Google、WhatsApp、PayPal
- **Andreessen Horowitz (a16z)** —— Marc Andreessen 创立，AI 重仓
- **Accel** —— Facebook、Slack 早期投资人
- **Benchmark** —— eBay、Twitter、Uber
- **Greylock Partners** —— LinkedIn、Facebook
- **Kleiner Perkins** —— Google、Amazon、Twitter
- **Founders Fund** —— Peter Thiel 创立，PayPal 黑帮
- **Lightspeed Venture Partners** —— Snap、AppDynamics
- **General Catalyst** —— Stripe、Airbnb
- **NEA (New Enterprise Associates)** —— Salesforce、Tableau

#### 1.3 VC 的盈利模式

**核心公式**：
```
基金收益 = Σ(退出项目回报 × 持股比例 × 成功率)
```

**关键指标**：

| 指标 | 全称 | 含义 | 优秀标准 |
|------|------|------|---------|
| **IRR** | Internal Rate of Return | 内部收益率 | > 20% |
| **TVPI** | Total Value to Paid-In | 总价值倍数 | > 2x |
| **DPI** | Distributed to Paid-In | 已分配倍数 | > 1x |
| **MOIC** | Multiple on Invested Capital | 投资倍数 | > 3x |
| **Hit Rate** | 命中率 | 成功项目占比 | 5-10% 即可 |

**VC 收益分布（典型情况）**：
- 50% 项目：完全亏损（-100%）
- 30% 项目：部分回报（0-2x）
- 15% 项目：中等回报（2-5x）
- 4% 项目：高回报（5-10x）
- 1% 项目：超额回报（10x+，如 Facebook、Google）

**Power Law（幂律法则）**：VC 行业最核心的规律——少数项目贡献绝大部分收益。错过 1 个 Uber = 整个基金白干。

---

### 2. 融资轮次详解

#### 2.1 完整融资生命周期

| 轮次 | 投资阶段 | 典型金额 | 估值范围 | 主要投资人 |
|------|---------|---------|---------|----------|
| **Pre-seed** | 想法/原型 | $50K-$500K | $500K-$3M | 创始人、朋友、天使 |
| **Seed（种子轮）** | 产品 MVP | $500K-$3M | $3M-$15M | 种子基金、加速器、天使 |
| **Series A** | 产品市场匹配（PMF） | $3M-$15M | $15M-$50M | 早期 VC |
| **Series B** | 规模化扩张 | $15M-$50M | $50M-$150M | 成长期 VC |
| **Series C** | 跨区域/品类扩张 | $50M-$100M+ | $150M-$500M | 成长期基金、PE |
| **Series D+** | 后期成熟 | $100M+ | $500M+ | PE、主权基金、Crossover |
| **Pre-IPO** | 上市前 | $50M-$500M+ | $1B+ | Crossover、Pre-IPO 基金 |
| **IPO** | 公开市场 | 视情况 | 公开市值 | 散户、机构、对冲基金 |

**"Crossover" 基金**：既投私募又投公开市场，主要在 IPO 前后投资，代表有 Tiger Global、Coatue、Altimeter。

#### 2.2 各轮次深度解析

**Pre-seed（种子前）**：
- 通常由创始人、家人、朋友出资（FFF：Family, Friends, Fools）
- 金额较小（$50K-$500K）
- 主要用于产品原型、初步市场验证
- 公司估值通常 $500K-$3M

**Seed（种子轮）**：
- 第一笔"机构化"融资
- 投资人：种子基金、加速器、天使投资人
- 资金用途：完成 MVP、获取首批用户
- 估值：$3M-$15M
- 著名种子轮：Uber 2009 年种子轮 $20 万（估值 $500 万，IPO 时回报 5,000 倍）

**Series A**：
- 寻找产品市场匹配（Product-Market Fit，PMF）
- 投资人主导早期 VC
- 资金用途：扩大团队、加速增长
- 估值：$15M-$50M
- 通常领投 + 跟投，领投方占董事会席位

**Series B**：
- 已证明 PMF，进入扩张阶段
- 资金用途：销售/营销、国际化、产品线扩展
- 估值：$50M-$150M
- 单位经济学（Unit Economics）开始健康

**Series C+**：
- 后期融资，巩固市场地位
- 投资人：Crossover、PE、主权基金
- 资金用途：并购、跨地区扩张、垂直整合
- 估值：$150M-$1B+
- 接近独角兽（$1B+ 估值）

**独角兽（Unicorn）**：
- 估值 $10 亿以上的未上市公司
- 2013 年 Cowboy Ventures 的 Aileen Lee 创造此词
- 全球独角兽数量从 2013 年的 39 家增长到 2024 年的 1,200+ 家
- 主要集中在美国、中国、印度、英国

#### 2.3 估值方法

**早期估值方法**：

| 方法 | 公式 | 适用 |
|------|------|------|
| **Berkus Method** | 5 大要素各值 $500K-$2M（合计 $2.5M-$10M） | 极早期 |
| **Scorecard Method** | 行业平均 × 6 大要素权重 | 种子/A 轮 |
| **Risk Factor Summation** | 基础估值 ± 风险调整 | 种子/A 轮 |
| **Comparables** | 类似公司最近融资估值 | 有可比公司 |
| **VC Method** | 退出时估值 × 概率 × 折现 | 早期 VC |

**Berkus Method 详解**（5 大要素各 $500K-$2M）：
1. 优秀想法（Sound Idea）：$500K-$2M
2. 原型/产品（Prototype）：$500K-$2M
3. 质量管理团队（Quality Management Team）：$500K-$2M
4. 战略关系（Strategic Relationships）：$500K-$2M
5. 产品发布/销售（Product Rollout/Sales）：$500K-$2M
- **最高估值：$10M**

**VC Method 详解**：
```
目标：10x 回报
步骤：
1. 预测 5 年后退出估值（如 $1B）
2. 计算所需股权比例（10% for 10x）
3. 投后估值 = 退出时市场价值 / 目标回报
4. 投前估值 = 投后估值 - 本轮投资额
```

**后期估值方法**：
- **可比公司分析**：看同行业类似公司的最近融资
- **DCF**：现金流折现（但早期公司现金流难预测）
- **可比交易分析**：参考类似公司被收购/上市的价格
- **Revenue Multiple**：Revenue × 行业倍数（如 SaaS 10-20x ARR）

#### 2.4 关键融资条款

**Liquidation Preference（清算优先权）**：
- VC 退出时优先于普通股股东获得回报
- 通常 1x 非参与（最常见），2x-3x 在热门赛道
- "参与型"：VC 先拿优先清算额，再按比例分剩余

**Anti-dilution（反稀释）**：
- 后续轮估值下降（down round）时保护 VC 利益
- 常见方式：加权平均（Weighted Average）、完全棘轮（Full Ratchet）
- 完全棘轮对创始人最不利（按最低价重新计算）

**Board Composition（董事会组成）**：
- 通常 5 人：2 创始人 + 1 共同投资人 + 1 领投 + 1 独立
- 重大事项（融资、并购、章程修改）需董事会批准
- 创始人需保留关键决策权

**Vesting（归属期）**：
- 创始人股权通常 4 年归属，1 年悬崖（cliff）
- 1 年悬崖：1 年内离职 = 0；1 年后开始按月归属
- 4 年后全部归属
- 保护：若创始人提前离开，剩余股权收回

**Pro-rata Rights（同比例增资权）**：
- VC 在后续轮次中有权按比例追加投资
- 保护 VC 持股不被稀释
- 后续轮若 VC 不想跟投，可放弃此权利

---

### 3. 行业赛道深度分析

#### 3.1 AI / 机器学习

**市场规模**：
- 2024 年全球 AI 市场约 $2,000 亿
- 预计 2030 年达 $1.8 万亿（CAGR 35%+）
- 主要细分：基础模型、应用层、基础设施

**AI 产业链**：

| 层级 | 代表公司 | 商业模式 |
|------|---------|---------|
| **基础模型** | OpenAI、Anthropic、Google DeepMind | API 调用收费、订阅 |
| **模型平台** | Hugging Face、Replicate | 平台费、托管费 |
| **训练算力** | NVIDIA、Cerebras、Groq | 硬件销售、云算力 |
| **数据服务** | Scale AI、Surge AI | 数据标注、合成数据 |
| **应用层** | Jasper、Harvey、Runway | 订阅、API 收费 |
| **AI 安全** | Anthropic、Anthropic Constitutional AI | 合规服务 |

**AI 关键术语**：

| 术语 | 解释 |
|------|------|
| **LLM** | 大语言模型（Large Language Model） |
| **GPT** | 生成式预训练 Transformer（Generative Pre-trained Transformer） |
| **Foundation Model** | 基础模型，通用大模型 |
| **Fine-tuning** | 在预训练模型上用特定数据继续训练 |
| **RAG** | 检索增强生成（Retrieval-Augmented Generation） |
| **Agent** | 能自主规划、执行多步骤任务的 AI |
| **MCP** | 模型上下文协议（Model Context Protocol） |
| **Token** | LLM 处理文本的最小单位 |
| **Embedding** | 文本转向量，捕捉语义 |
| **Hallucination** | AI 幻觉，编造不实信息 |

**AI 投资热点（2024-2026）**：
- **生成式 AI**：OpenAI、Anthropic、Midjourney
- **AI Agent**：Adept、Devin（Cognition AI）
- **AI 安全**：Anthropic、Scale AI
- **AI 基础设施**：Groq、Cerebras、Lambda
- **垂直 AI**：Harvey（法律）、Abridge（医疗）、Glean（企业搜索）
- **开源 AI**：Mistral、Hugging Face

**著名 AI 并购**：
- 2024-03：Microsoft 吸收 Inflection AI 核心团队（$6.5 亿）
- 2024：Amazon 吸收 Adept AI 核心团队
- 2024-08：Google 收购 Wiz（网络安全，$32B）
- 2024-06：Cisco 收购 Splunk（数据分析，$28B）

#### 3.2 网络安全（Cybersecurity）

**市场规模**：
- 2024 年全球网络安全市场约 $3,000 亿
- 预计 2030 年达 $7,000 亿（CAGR 15%+）
- 主要驱动：勒索软件、数据泄露、监管合规

**细分赛道**：

| 赛道 | 英文 | 代表公司 |
|------|------|---------|
| **终端安全** | Endpoint Security | CrowdStrike、SentinelOne |
| **网络安全** | Network Security | Palo Alto Networks、Fortinet |
| **云安全** | Cloud Security | Wiz、Lacework、Orca Security |
| **身份安全** | Identity Security | Okta、Auth0（被 Okta 收购） |
| **应用安全** | AppSec | Snyk、Veracode |
| **数据安全** | Data Security | BigID、Cyera |
| **零信任** | Zero Trust | Zscaler、BeyondTrust |
| **威胁情报** | Threat Intelligence | Recorded Future、Mandiant |

**著名收购**：
- 2019-02：Thoma Bravo 收购 Sophos（$3.9B）
- 2024-08：Google 宣布收购 Wiz（$32B，网络安全最大并购）

#### 3.3 金融科技（Fintech）

**市场规模**：
- 2024 年全球金融科技市场约 $3,000 亿
- 预计 2030 年达 $1.2 万亿（CAGR 25%+）

**细分赛道**：

| 赛道 | 代表公司 | 估值 |
|------|---------|------|
| **支付** | Stripe、Adyen、PayPal | Stripe $95B |
| **银行科技** | Mercury、Brex、Ramp | Mercury $1.2B |
| **借贷** | Affirm、SoFi、Upstart | Affirm $15B |
| **财富科技** | Robinhood、Wealthfront、IBKR | Robinhood $20B+ |
| **保险科技** | Lemonade、Root、Oscar | Lemonade $3B |
| **加密** | Coinbase、Anchorage | Coinbase $50B+ |
| **跨境支付** | Wise、Remitly | Wise $10B+ |
| **企业金融** | Plaid、Marqeta | Plaid $13B |
| **AI 金融** | Navan（差旅）、Klar、Wealthsimple | - |

**Stripe 案例**：
- 创始人：Patrick 和 John Collison（爱尔兰兄弟）
- 成立：2010 年
- 估值历史：$1.5B (2011) → $95B (2021) → 近期 $65B（2024 下调）
- 收入：2024 年约 $14B
- 上市：未上市，但部分员工股票二级交易活跃

#### 3.4 生物科技 / 制药（Biotech）

**细分赛道**：
- **传统药企**：Moderna、BioNTech、Vertex
- **AI 制药**：Recursion、Insitro、Insilico Medicine
- **基因编辑**：CRISPR Therapeutics、Editas、Beam
- **细胞治疗**：CAR-T（诺华、Kite/Gilead）
- **罕见病**：Alexion（被 AZ 收购）、Vertex CF 业务
- **数字健康**：Teladoc、Hims & Hers

**关键概念**：

| 术语 | 解释 |
|------|------|
| **IND** | 新药临床试验申请（Investigational New Drug） |
| **NDA/BLA** | 新药/生物制品上市申请 |
| **Phase I/II/III** | 临床试验三期（安全性→有效性→大规模） |
| **FDA** | 美国食品药品监督管理局 |
| **EMA** | 欧洲药品管理局 |
| **NMPA** | 中国国家药品监督管理局 |
| **Orphan Drug** | 罕见病药，享受 7 年独占期 |
| **Patent Cliff** | 专利悬崖，原研药专利到期仿制药冲击 |

**研发周期与成本**：
- 周期：10-15 年
- 成本：$2-10 亿一个新药
- 成功率：临床 I 期到上市 < 10%

#### 3.5 气候科技（Climate Tech）

**细分赛道**：

| 赛道 | 英文 | 代表公司 |
|------|------|---------|
| **电池储能** | Battery Storage | QuantumScape、Sila Nanotechnologies |
| **太阳能** | Solar | Enphase、First Solar、Sunrun |
| **电动车** | EV | Rivian、Lucid、Polestar |
| **氢能** | Hydrogen | Plug Power、Chart Industries |
| **碳捕集** | Carbon Capture | Climeworks、Carbon Engineering |
| **核聚变** | Fusion | Commonwealth Fusion、Helion |
| **电池回收** | Battery Recycling | Redwood Materials、Li-Cycle |
| **智能电网** | Smart Grid | EnergyHub、AutoGrid |

**关键概念**：

| 术语 | 解释 |
|------|------|
| **Net Zero** | 净零排放 |
| **Carbon Credit** | 碳信用，1 吨 CO2 排放权 |
| **ESG** | 环境、社会、治理 |
| **GHG Protocol** | 温室气体核算体系 |
| **Scope 1/2/3** | 直接排放/能源排放/价值链排放 |
| **Paris Agreement** | 巴黎协定，1.5°C 目标 |
| **IRA** | 美国《通胀削减法案》，$3690 亿气候投资 |

---

### 4. 资本市场与融资数据库

#### 4.1 主要融资数据源

| 数据源 | 数据覆盖 | 特点 |
|--------|---------|------|
| **PitchBook** | 全球 PE/VC 融资、并购、退出 | 数据最全 |
| **CB Insights** | 全球初创公司、融资、估值 | 趋势分析强 |
| **Crunchbase** | 全球初创公司融资 | 免费版可用 |
| **Preqin** | 基金数据、LP/GP 信息 | 基金行业首选 |
| **S&P Capital IQ** | 上市公司+融资 | 上市公司详细 |
| **DealStreetAsia** | 亚洲 PE/VC 数据 | 亚洲市场 |
| **IT桔子** | 中国一级市场 | 中国市场最全 |
| **清科** | 中国 PE/VC 数据库 | 中国市场 |

#### 4.2 关键融资事件字段

```json
{
  "company_id": "C_1860042219",  // 公司标识符
  "company_name": "Together AI",
  "round": "Series B",
  "announce_date": "2024-03-15",
  "amount_raised": "$106M",
  "pre_money_valuation": "$1.2B",
  "post_money_valuation": "$1.3B",
  "lead_investor": "Salesforce Ventures",
  "participants": ["Andreessen Horowitz", "Coatue"],
  "use_of_funds": "AI 基础设施扩张",
  "status": "Closed"
}
```

#### 4.3 退出方式（Exits）

**5 种主要退出方式**：

| 退出 | 英文 | 说明 | 典型回报 |
|------|------|------|---------|
| **IPO** | Initial Public Offering | 首次公开上市 | 5-50x |
| **战略并购** | Strategic M&A | 同行业公司收购 | 3-15x |
| **财务并购** | Financial M&A | PE 收购退出 | 2-8x |
| **二级转让** | Secondary Sale | 卖给其他 VC | 1-3x |
| **回购** | Buyback | 创始人或公司回购 | 1-2x |
| **清算** | Liquidation | 公司破产 | 0x |

**IPO 案例**：
- 2012：Facebook IPO（$104B 估值）
- 2019：Uber IPO（$82B）、Lyft IPO（$24B）
- 2021：Robinhood、Bumble、Affirm、Coinbase

**大型并购案例**：
- 2012：Facebook 收购 Instagram（$1B → 后估值 $100B+）
- 2014：Facebook 收购 WhatsApp（$19B）
- 2016：Microsoft 收购 LinkedIn（$26B）
- 2017：Intel 收购 Mobileye（$15B）
- 2021：Microsoft 收购 Nuance（$19B）
- 2022：Microsoft 收购 Activision（$69B，游戏史上最大）
- 2024：Google 收购 Wiz（$32B）

---

### 5. 公司标识符系统详解

#### 5.1 标识符种类

| 标识符 | 缩写 | 适用范围 | 示例 |
|--------|------|---------|------|
| **CUSIP** | - | 美国证券 | 037833100 (Apple) |
| **ISIN** | - | 全球证券 | US0378331005 (Apple) |
| **SEDOL** | - | 英国证券 | 2046251 (Apple) |
| **Ticker** | - | 股票代码 | AAPL |
| **CIK** | - | SEC 文件 | 0000320193 (Apple) |
| **LEI** | - | 法律实体 | HWUPKR0MPOU8FGXBT394 |
| **S&P Capital IQ ID** | company_id | S&P 内部 | C_000000001 |

#### 5.2 品牌名 vs 法律实体名

**为什么需要区分**：

| 类型 | 说明 | 示例 |
|------|------|------|
| **品牌名** | 营销用的名字，可能变化 | "Together AI" |
| **法律实体名** | 注册公司的法定名字 | "Together Computer, Inc." |
| **曾用名** | 历史曾用名 | "Facebook" → "Meta" |
| **产品名** | 产品名可能与公司名不同 | "ChatGPT" ≠ "OpenAI" |

**为什么会有差异**：
1. **公司改名**：如 Google → Alphabet
2. **品牌与公司分离**：如 "Pinduoduo" 母公司 "PDD Holdings"
3. **多品牌战略**：如字节跳动旗下 TikTok、抖音、Lemon8
4. **并购改名**：如 "Slack" → "Salesforce Slack"
5. **法律实体不统一**：母公司、子公司、孙公司层级

#### 5.3 子公司识别

**为什么子公司没有独立融资数据**：
- 子公司股权 100% 属于母公司
- 融资资金通常来自母公司而非外部 VC
- 财务数据合并到母公司报表
- 投资人面对的法律实体是母公司

**典型子公司案例**：
- **DeepMind**（Alphabet 子公司）
- **GitHub**（Microsoft 子公司）
- **YouTube**（Alphabet 子公司）
- **BeReal**（被 Voodoo 收购，Voodoo 子公司）
- **Shockwave Medical**（被 J&J 收购，J&J 子公司）

**S&P Global 中的状态字段**：
- "Operating"：独立运营公司 ✅
- "Operating Subsidiary"：子公司 ❌（无独立融资）
- "Defunct"：已停止运营 ❌
- "Acquired"：已被收购
- "Merged"：已合并

---

### 6. 估值与倍速

#### 6.1 ARR / Revenue 倍数

**SaaS 行业典型 ARR 倍数**：

| 增长率 | 毛利率 | 典型 ARR 倍数 |
|--------|--------|---------------|
| < 30% | > 75% | 5-10x |
| 30-50% | > 75% | 10-20x |
| 50-100% | > 75% | 20-40x |
| > 100% | > 75% | 40x+ |

**Rule of 40（40 法则）**：
- 定义：收入增长率 + 营业利润率 ≥ 40%
- 是 SaaS 公司的健康指标
- 低于 40%：估值打折
- 高于 40%：可享溢价

#### 6.2 AI 公司估值

**AI 公司的特殊估值**：
- 早期：基于团队、技术、数据
- 成长期：基于 ARR、毛利率、增长速度
- 后期：基于市场份额、客户留存

**著名 AI 估值案例**：
| 公司 | 最近估值 | 倍数 |
|------|---------|------|
| OpenAI | $157B (2024) | ~ 50x ARR |
| Anthropic | $60B (2024) | ~ 60x ARR |
| xAI | $50B (2024) | - |
| Perplexity | $9B (2024) | - |
| Mistral | $6B (2024) | - |
| Cohere | $5.5B (2024) | - |
| Hugging Face | $4.5B (2024) | - |
| Runway | $4.5B (2024) | - |
| Databricks | $62B (2024) | ~ 18x ARR |
| Scale AI | $13.8B (2024) | - |

#### 6.3 "Down Round" 下调估值融资

**定义**：新一轮估值低于上一轮估值，俗称"流血融资"。

**为什么会发生**：
- 市场环境恶化（如 2022-2023 科技股崩盘）
- 公司业绩不达预期
- 行业估值整体下调
- 创始人被迫接受现实

**Down Round 的影响**：
- 创始人股权被大幅稀释
- 触发反稀释条款，对创始人更不利
- 严重影响公司士气和招聘
- 通常伴随裁员和重组

**2022-2023 Down Round 案例**：
- Stripe：$95B → $65B（-32%）
- Klarna：$46B → $6.7B（-85%）
- Instacart：$39B → $13.7B（IPO 前）
- 大量 SaaS 公司估值腰斩

---

### 7. 投资协议关键条款

#### 7.1 Term Sheet 详解

**Term Sheet（条款清单）**：VC 投资协议的核心条款摘要，是投资意向的法律文件。

**关键条款**：

| 条款 | 英文 | 含义 |
|------|------|------|
| **Pre-money Valuation** | 投前估值 | 本轮投资前的公司估值 |
| **Post-money Valuation** | 投后估值 | 投前 + 本轮投资额 |
| **Liquidation Preference** | 清算优先权 | 退出时优先回报 |
| **Anti-dilution** | 反稀释 | 后续轮估值下降时的保护 |
| **Board Composition** | 董事会 | 决策权分配 |
| **Vesting** | 归属 | 创始人股权逐步释放 |
| **Pro-rata Rights** | 增资权 | 后续轮同比例投资权 |
| **Drag-along** | 强制随售 | 多数股东可强制少数股东出售 |
| **Tag-along** | 共同出售 | 少数股东可参与大股东出售 |
| **ROFR** | 优先购买权 | 优先购买其他股东股份 |
| **Redemption** | 赎回权 | VC 可要求公司回购股份 |
| **Put Option** | 卖回期权 | 类似赎回权 |
| **Conversion** | 转股 | 优先股转普通股的规则 |
| **Dividend** | 股息 | 优先股的股息规则 |
| **Information Rights** | 信息权 | VC 获取公司财务信息的权利 |

#### 7.2 SAFE 协议

**定义**：SAFE（Simple Agreement for Future Equity）是 Y Combinator 推出的简化版投资协议，比传统可转债更简单。

**核心特点**：
- **无利息**：不像可转债有利率
- **无到期日**：不设还款期限
- **转换为股权**：在公司下一轮融资时转换为优先股
- **折扣（Discount）**：转股时可享受 10-25% 估值折扣
- **估值上限（Valuation Cap）**：转股价基于较低估值（折扣前估值 vs 上限）
- **MFN 条款**：与后续投资人享有同等优惠

**典型结构**：
```
投资金额：$500K
估值上限：$10M
折扣：20%
后续轮：$20M 投后估值
转股价：min(20M × 80%, 10M) = $8M（按估值上限）
```

#### 7.3 可转债（Convertible Note）

**核心要素**：
- **本金**：投资额
- **利率**：通常 2-8%
- **到期日**：通常 18-24 个月
- **转换折扣**：10-25%
- **估值上限**：可选择
- **Maturity Default**：到期未转换，VC 可要求还款

**与 SAFE 区别**：
- SAFE：无利息、无到期日
- 可转债：有利息、有到期日
- 法律上：可转债是债务，SAFE 是未来股权承诺

---

### 8. 投资人类型详解

#### 8.1 战略投资人 vs 财务投资人

| 维度 | 战略投资人 (CVC) | 财务投资人 (VC/PE) |
|------|----------------|------------------|
| **身份** | 行业公司战投部门 | 专业投资基金 |
| **目标** | 战略协同、市场洞察、财务回报 | 主要是财务回报 |
| **估值容忍** | 较高（可接受战略溢价） | 严格（追求投资回报） |
| **附加价值** | 业务合作、客户引荐 | 经验、人才、后续融资 |
| **投后介入** | 通常较弱 | 通常较深 |
| **退出预期** | 战略并购为主 | IPO/并购退出 |
| **资金耐心** | 较长 | 受基金期限约束 |

**著名 CVC（企业战投）**：
- Google Ventures (GV)
- Salesforce Ventures
- Microsoft M12
- Intel Capital
- Comcast Ventures
- Bloomberg Beta
- Workday Ventures
- Stripe Capital

#### 8.2 超级天使投资人（Super Angel）

**定义**：个人投资者，但像基金一样投资多笔交易，金额较大。

**著名超级天使**：
- **Marc Andreessen**（后创立 a16z）
- **Ron Conway**（Google、Facebook 早期）
- **Peter Thiel**（PayPal、Palantir）
- **Chris Sacca**（Twitter、Instagram、Uber）
- **Reid Hoffman**（LinkedIn、Greylock）
- **Naval Ravikant**（AngelList 创始人）

#### 8.3 主权财富基金与 Crossover

**主权财富基金**（Sovereign Wealth Fund，SWF）：
- 政府所有的投资基金
- 主要：中投公司（中国）、GIC（新加坡）、淡马锡（新加坡）、PIF（沙特）、Mubadala（阿联酋）、ADIA（阿布扎比）
- 通常投资后期、Pre-IPO、上市公司

**Crossover Fund（交叉基金）**：
- 既投一级市场（私募）又投二级市场（公开）
- 代表：Tiger Global、Coatue、Altimeter、D1 Capital
- 投未上市公司，后期为主
- 在 IPO 时通常会部分卖出获利

---

### 9. 公司成长阶段详解

#### 9.1 初创公司发展阶段

**PMF 前（Pre-PMF）**：
- 想法 → 原型 → MVP → 早期用户
- 烧钱，可能无收入或极少
- 主要指标：留存率（Retention）

**PMF 阶段**：
- Sean Ellis 测试：> 40% 用户"非常失望如果产品消失"
- 找到可复制增长模型
- 主要指标：NPS、增长曲线斜率

**扩张阶段**：
- 增长加速，单位经济学健康
- 开始追求规模经济
- 主要指标：CAC、LTV、回收期

**成熟阶段**：
- 增长放缓，转向盈利
- 多元化产品线
- 主要指标：营业利润率、ROIC

**上市阶段**：
- 准备 IPO
- 公司治理升级
- 财务披露规范化

#### 9.2 关键 SaaS 指标

| 指标 | 英文 | 公式 | 优秀标准 |
|------|------|------|---------|
| **MRR** | Monthly Recurring Revenue | 每月经常性收入 | - |
| **ARR** | Annual Recurring Revenue | MRR × 12 | - |
| **ARPU** | Average Revenue Per User | 收入 / 用户数 | - |
| **CAC** | Customer Acquisition Cost | 销售营销费 / 新增客户 | < LTV/3 |
| **LTV** | Lifetime Value | ARPU × 客户生命周期 | > 3× CAC |
| **回收期** | Payback Period | CAC / (ARPU × 毛利率) | < 12 月 |
| **NRR** | Net Revenue Retention | (起始 ARR + 扩张 - 流失) / 起始 ARR | > 110% |
| **GRR** | Gross Revenue Retention | (起始 ARR - 流失) / 起始 ARR | > 90% |
| **Churn** | 流失率 | 流失客户 / 起始客户 | 越小越好 |
| **Rule of 40** | 40 法则 | 增长率 + 利润率 | > 40% |

#### 9.3 单位经济学（Unit Economics）

**定义**：单客户/单交易的盈利模型，是 SaaS 公司最重要的健康指标。

**核心公式**：
```
LTV = ARPU × 客户生命周期 × 毛利率
LTV / CAC = 健康度指标
```

**示例**：
- ARPU = $100/月
- 客户生命周期 = 36 个月
- 毛利率 = 80%
- **LTV = $100 × 36 × 80% = $2,880**
- **CAC = $500**
- **LTV/CAC = 5.76x（优秀）**

---

### 10. AI 行业特别分析

#### 10.1 AI 公司商业模式

| 模式 | 说明 | 代表 |
|------|------|------|
| **基础模型 API** | 按 token 收费 | OpenAI、Anthropic |
| **订阅** | 月费/年费 | ChatGPT Plus、Claude Pro |
| **应用 SaaS** | 基于 AI 的应用 | Jasper、Harvey |
| **企业合同** | 大客户定制 | Anthropic Enterprise |
| **平台** | 模型市场 | Hugging Face |
| **硬件** | 芯片/服务器 | NVIDIA、Cerebras |
| **数据** | 数据服务 | Scale AI、Surge |

#### 10.2 AI 监管与合规

**主要监管**：
- **EU AI Act**：欧盟 AI 法案，分级监管
- **中国《生成式 AI 服务管理暂行办法》**：内容安全、备案
- **美国 EO 14110**：拜登 AI 行政令
- **NIST AI RMF**：美国 AI 风险管理框架
- **UK AI Safety Institute**：英国 AI 安全研究所

**AI 风险分级（EU AI Act）**：
| 风险等级 | 监管要求 | 示例 |
|---------|---------|------|
| **不可接受** | 禁止 | 社交评分、操纵性 AI |
| **高风险** | 严格合规 | 招聘、贷款、执法 |
| **有限风险** | 透明度 | 聊天机器人、深度伪造 |
| **最小风险** | 无需合规 | 游戏 AI、垃圾邮件过滤 |

#### 10.3 AI 算力经济学

**AI 训练成本**：
- GPT-3 训练：约 $5M
- GPT-4 训练：估计 $100M+
- Llama 3 训练：约 $50M
- Claude 3.5 Sonnet：未披露，估计 $30M+

**推理成本**：
- 单位：每百万 token
- Opus 4：$15 输入 / $75 输出
- Sonnet 4：$3 输入 / $15 输出
- Haiku：$0.25 输入 / $1.25 输出

**毛利率**：
- AI 推理毛利率：20-50%（受 GPU 成本影响）
- 规模效应：越大越便宜
- 边缘 AI（设备端）：未来趋势

---

### 11. 行业分析框架

#### 11.1 市场规模（Market Sizing）

**TAM / SAM / SOM 框架**：

| 概念 | 英文 | 含义 |
|------|------|------|
| **TAM** | Total Addressable Market | 总潜在市场，全球所有可能客户 |
| **SAM** | Serviceable Addressable Market | 可服务市场，公司能触达的部分 |
| **SOM** | Serviceable Obtainable Market | 实际可获得市场，公司短期内能拿下的 |

**示例**（Salesforce）：
- TAM：全球企业软件市场 $1T
- SAM：CRM 市场 $80B
- SOM：3 年内可达 $40B

#### 11.2 Porter 五力模型

**五力**：
1. **同业竞争**：行业竞争激烈程度
2. **新进入者**：进入门槛高低
3. **替代品威胁**：是否有替代方案
4. **供应商议价**：供应商是否强势
5. **客户议价**：客户是否强势

#### 11.3 SWOT 分析

- **S（Strengths）**：优势
- **W（Weaknesses）**：劣势
- **O（Opportunities）**：机会
- **T（Threats）**：威胁

---

### 12. 重要融资事件精选（2024）

**2024 年 AI 行业重大融资**：

| 公司 | 轮次 | 金额 | 估值 | 领投 |
|------|------|------|------|------|
| OpenAI | Secondary | $6.6B | $157B | Thrive Capital |
| Anthropic | Series F | $4B | $60B | Amazon |
| xAI | Series B | $6B | $50B | Valor, a16z, Sequoia |
| Databricks | Series J | $10B | $62B | JPMorgan |
| Mistral AI | Series B | $650M | $6B | General Catalyst |
| Perplexity | Series C | $500M | $9B | IVP, Bezos |
| Scale AI | Series F | $1B | $13.8B | Accel |
| Groq | Series D | $640M | $2.8B | BlackRock |

**2024 年其他大额融资**：
- Stripe：$694M（员工二级交易，$65B 估值）
- Reddit：IPO 2024-03（$31B 市值）
- Shein：拟上市（估值 $660B）❌ 待定
- Klarna：IPO 2024-09（$13.5B 估值，远低于巅峰）

---

### 13. 投行/分析师常用工具

#### 13.1 数据库对比

| 工具 | 覆盖 | 价格 | 用户 |
|------|------|------|------|
| **PitchBook** | 全球 PE/VC | $$$$ | PE/VC 必备 |
| **CB Insights** | 全球初创 | $$$ | 趋势分析 |
| **Crunchbase** | 全球初创 | $$ | 通用 |
| **Tracxn** | 全球初创 | $$ | 印度/亚洲 |
| **S&P Capital IQ** | 上市+私募 | $$$$ | 综合 |
| **Preqin** | 基金 | $$$$ | LP/GP |
| **Dealogic** | M&A/IPO | $$$$ | 投行 |

#### 13.2 投资研究工具

- **AlphaSense**：AI 驱动的金融搜索
- **Tegus**：专家访谈记录
- **Grata**：公司搜索
- **Source Global Research**：行业研究
- **Gartner**：技术研究
- **Forrester**：技术研究

---

### 14. 关键术语速查

| 中文 | 英文 | 缩写 | 解释 |
|------|------|------|------|
| 风险投资 | Venture Capital | VC | 高成长公司投资 |
| 私募股权 | Private Equity | PE | 成熟公司投资 |
| 种子轮 | Seed Round | - | 早期小额融资 |
| A/B/C 轮 | Series A/B/C | - | 不同阶段融资 |
| 首次公开募股 | Initial Public Offering | IPO | 公司上市 |
| 退出 | Exit | - | 投资人实现回报 |
| 估值 | Valuation | - | 公司价值 |
| 投资后估值 | Post-money | - | 投后公司价值 |
| 投资前估值 | Pre-money | - | 投前公司价值 |
| 稀释 | Dilution | - | 股权比例下降 |
| 清算优先权 | Liquidation Preference | LP | 退出优先权 |
| 反稀释 | Anti-dilution | - | 防止股权被稀释 |
| SAFE 协议 | Simple Agreement for Future Equity | SAFE | YC 推出的简化协议 |
| 可转债 | Convertible Note | - | 可转为股权的贷款 |
| 董事会 | Board of Directors | - | 公司决策机构 |
| 归属期 | Vesting | - | 股权分期获得 |
| 悬崖 | Cliff | - | 归属期起步阶段 |
| 投后估值倍数 | Post-money Multiple | - | 投后估值 / 投资额 |
| 单位经济学 | Unit Economics | - | 单客户盈利模型 |
| 经常性收入 | Recurring Revenue | RR | 重复发生的收入 |
| 客户获取成本 | Customer Acquisition Cost | CAC | 获取单个客户的成本 |
| 客户生命周期价值 | Lifetime Value | LTV | 客户一生贡献的价值 |
| 净收入留存 | Net Revenue Retention | NRR | 现有客户收入变化 |
| 商业级模型 | Business Model | - | 公司赚钱方式 |
| 战略投资人 | Corporate Venture Capital | CVC | 大公司战投 |
| 财务投资人 | Financial Investor | - | VC/PE 基金 |
| 加速器 | Accelerator | - | 短期孵化项目 |
| 卓越中心 | Center of Excellence | CoE | 内部专业团队 |
| 数据驱动 | Data-driven | - | 用数据决策 |
| 精益创业 | Lean Startup | - | MVP+迭代方法 |
| 增长黑客 | Growth Hacking | - | 快速增长方法 |
| 关键绩效指标 | Key Performance Indicator | KPI | 核心指标 |
| 商业级指标 | Business Metric | - | 商业表现指标 |
| 现金流 | Cash Flow | - | 现金流入流出 |
| 营业成本 | Operating Expenses | OpEx | 经营支出 |
| 销售成本 | Cost of Goods Sold | COGS | 直接成本 |
| 客户终身价值 | Customer Lifetime Value | CLV/LTV | 与 LTV 同义 |
| 净推荐值 | Net Promoter Score | NPS | 客户满意度 |
| 月经常性收入 | Monthly Recurring Revenue | MRR | SaaS 月收入 |
| 年经常性收入 | Annual Recurring Revenue | ARR | SaaS 年收入 |
| 烧钱率 | Burn Rate | - | 每月净现金消耗 |
| 现金跑道 | Runway | - | 现金可支撑月数 |
| 营运资金 | Working Capital | - | 短期资产-负债 |

---

> **提示**：本附录覆盖了风险投资、AI 行业、网络安全、金融科技、生物科技、气候科技等多个热门赛道的核心金融知识。种子公司列表中提到的公司估值、融资数据可能在数月内变化，请以最新数据库（PitchBook、CB Insights 等）为准。