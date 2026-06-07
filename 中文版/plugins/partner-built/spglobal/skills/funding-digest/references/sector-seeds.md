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

## Appendix: 金融背景知识

这份文件是 S&P Global Funding Digest 技能的"行业种子列表"——14+ 个热门赛道各列出 3-8 家代表性公司，作为融资分析的起点。读完这个附录，你会搞懂：**为什么需要"种子"、怎么从种子扩展到整个行业、融资轮次到底在说什么、以及 S&P Global 的数据工具怎么跟这些概念配合**。

> **通用金融知识已抽离到独立知识库，按需阅读：**
>
> - [风险投资](../../../../../../金融知识学习/风险投资.md) — VC 融资轮次 / 估值方法 / 退出机制 / 关键条款
> - [SaaS与科技公司](../../../../../../金融知识学习/SaaS与科技公司.md) — ARR / NRR / Rule of 40 / CAC Payback
> - [并购](../../../../../../金融知识学习/并购.md) — M&A 类型 / 流程 / 反垄断
>
> 下面只讲**本文件模板独有**的内容。

---

### 1. 为什么需要"种子公司"——从一棵树看到整片森林

**想象一个场景**：老板让你"分析一下 AI 行业的融资情况"。AI 行业有上千家公司，你不可能一家一家查。怎么办？

**答案是：先找 3-5 家最有代表性的公司作为"种子"**，然后用 S&P Global 的"竞争对手"工具，从每颗种子扩展出它的同行。就像你认识了一个朋友圈的核心人物，通过他就能认识整个圈子。

**真实例子**：你想了解 AI 大模型赛道的融资。你从 OpenAI 开始（种子），用竞争对手工具找到 Anthropic、Cohere、Mistral、xAI——5 颗种子扩展出 20+ 家公司，覆盖了这个赛道 80% 的融资活动。

**所以这意味着什么**：种子不是随便选的。好的种子应该是该赛道**融资最活跃、最被关注**的公司。如果种子选错了（比如选了一家已经倒闭的公司），扩展出来的结果也会偏。

---

### 2. S&P Global 标识符——公司的"身份证号"

**想象一下**：你搜索"Together AI"，但 S&P Global 数据库里它的法律名是"Together Computer, Inc."。如果你直接用品牌名查，可能查不到。

**S&P Global 用 `company_id`（如 C_1860042219）来唯一标识每家公司**，就像身份证号一样。品牌名和法律实体名可能不同——这是数据查询中最常见的坑。

**尽职调查规则 0**：调用任何数据工具之前，**先用 `get_info_from_identifiers` 确认公司标识符能正确解析**。这步叫"预验证"，能避免绝大多数数据为空的问题。

**真实例子**：
- 你想查 DeepMind 的融资数据 → 但 DeepMind 是 Alphabet 的子公司 → `get_info_from_identifiers` 返回 status = "Operating Subsidiary" → 融资轮数为零（因为融资记录在母公司 Alphabet 层面）
- 你想查 Stripe 的融资 → status = "Operating" → 可以正常查询

**所以这意味着什么**：看到 status 字段，你就知道这家公司能不能查到融资数据。"Operating"= 可以查，"Operating Subsidiary"= 子公司，融资数据在母公司那里。

---

### 3. 用户指定 vs 自动扩展——两种找公司的方式

本文件支持两种找公司的方式：

1. **用户指定**：用户自己说"我想看 OpenAI、Anthropic、Mistral"——直接查这三家
2. **自动扩展**：用户说"我想看 AI 赛道"——从种子列表里取 AI 种子，用竞争对手工具扩展

**两种方式各有优劣**：

| 方式 | 优点 | 缺点 |
|------|------|------|
| 用户指定 | 精准，不会查到不相关的公司 | 可能遗漏重要玩家 |
| 自动扩展 | 覆盖面广，不容易漏 | 可能包含不太相关的公司 |

**实际操作建议**：先用自动扩展拿到大列表，再让用户确认或删减。这比让用户从零开始想公司名要高效得多。

---

### 4. 子公司 vs 独立运营——为什么有些公司查不到融资

**想象一下**：你想查 YouTube 的融资轮次。但 YouTube 早在 2006 年就被 Google 收购了——它现在是 Alphabet 的子公司，不再独立融资。

**S&P Global 的数据逻辑**：
- 子公司（Subsidiary）= 被其他公司控股的公司
- 子公司没有独立的融资数据——融资事件记录在**母公司**层面
- 标记为子公司或被收购的种子在 `get_info_from_identifiers` 中仍会解析（status = "Operating Subsidiary"），但返回的融资轮数为零

**所以这意味着什么**：当你在种子列表里看到一家公司返回零融资数据，先检查它的 status 字段。如果是子公司，那不是数据缺失，而是正常的——融资在母公司层面。

---

### 5. 种子列表的维护——为什么需要每季度更新

**AI 行业变化有多快？** 2023 年还独立的 Inflection AI，2024 年就被微软"收编"了。2024 年还独立的 Adept AI，同年就被亚马逊收购了。

**种子列表需要每季度审核**，因为：
- 公司会被收购（变成子公司，融资数据归零）
- 公司会转型（从 AI 转向其他方向）
- 新玩家会冒出来（比如 2024 年的 xAI）
- 有些公司会倒闭

**本文件中的种子列表**覆盖 AI、网络安全、金融科技、生物科技、清洁能源、电商、机器人等 14+ 个热门赛道。AI 行业的种子变化尤为迅速，需要最频繁的更新。

> **给小白的一句话**：这个种子列表就像一张"行业地图的起点标记"——你不需要记住每家公司的名字，但要知道**从哪里出发、怎么扩展、什么时候该更新**。融资分析的本质就是"从已知推未知"——种子是你已知的起点，竞争对手工具是你扩展的桥梁，status 字段是你避坑的指南针。

### 1. 风险投资（VC）行业全景
