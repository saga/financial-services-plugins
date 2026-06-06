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