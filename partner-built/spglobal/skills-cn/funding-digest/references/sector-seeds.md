# 行业种子公司参考

当用户指定行业但未指定具体公司时，使用这些种子列表来启动公司范围。这些是起点——始终通过 `get_competitors_from_identifiers` 扩展并使用 `get_info_from_identifiers` 验证。

> **以下所有种子已针对S&P Global的标识符系统进行验证。** 如果种子无法解析，请尝试括号中列出的别名，然后再放弃。

## 科技 / 软件

### AI / 机器学习
种子：OpenAI, Anthropic, Databricks, Scale AI, Cohere, Hugging Face, Mistral AI, xAI, Perplexity AI, Runway ML（别名："Runway AI, Inc."）, Together AI（别名："Together Computer, Inc."）, Character.ai（别名："Character Technologies, Inc."）, Groq, Stability AI, Aleph Alpha, Magic AI

⚠️ **排除（不要用作种子）：**
- *Inflection AI* — 核心团队被Microsoft吸收（2024年3月）。存在历史轮融资但无新活动。
- *Adept AI* — 大部分被Amazon吸收（2024年）。同上。
- *DeepMind* — Alphabet子公司。无独立融资轮。

### 网络安全
种子：CrowdStrike, Palo Alto Networks, Wiz, Snyk, SentinelOne, Abnormal Security, Netskope

### 云基础设施 / 开发工具
种子：Snowflake, HashiCorp, Datadog, Confluent, Vercel, Supabase, PlanetScale

### 金融科技
种子：Stripe, Plaid, Brex, Ramp, Mercury, Affirm, Marqeta, Navan

### 垂直SaaS
种子：ServiceTitan, Toast, Procore, Veeva Systems, Blend Labs

## 医疗健康 / 生命科学

### 生物科技 / 制药
种子：Moderna, BioNTech, Recursion Pharmaceuticals, Tempus AI, Insitro, AbCellera

### 数字健康
种子：Teladoc, Hims & Hers, Ro, Noom, Color Health

⚠️ **排除（不要用作种子）：**
- *Cerebral* — 仍在运营但面临重大监管问题；仅在用户明确要求时包含。

### 医疗器械
种子：Intuitive Surgical, Butterfly Network, Outset Medical

⚠️ **排除（不要用作种子）：**
- *Shockwave Medical* — 被Johnson & Johnson收购（2024年5月）。现为子公司，无独立融资轮。

## 能源 / 气候

### 气候科技
种子：Redwood Materials, Form Energy, Commonwealth Fusion, Sila Nanotechnologies, Climeworks

### 清洁能源
种子：Enphase Energy, First Solar, Rivian, QuantumScape, Sunnova

## 消费

### 电商 / 市场
种子：Shopify, Faire, Whatnot, Fanatics

⚠️ **排除（不要用作种子）：**
- *Temu (PDD Holdings)* — PDD Holdings是大型上市集团；其融资活动通过股票市场捕获，而非风投轮。

### 消费社交 / 媒体
种子：Discord, Reddit, Substack

⚠️ **排除（不要用作种子）：**
- *BeReal* — 被Voodoo收购（2024年6月）。现为子公司。
- *Lemon8* — 品牌名"Lemon8"在S&P Global中解析为一家小型荷兰公司（Lemon8 B.V.），**不是**ByteDance的社交媒体应用。ByteDance的应用是子公司，没有独立融资轮。不要使用。

## 工业 / 物流

### 物流 / 供应链
种子：Flexport, Samsara, Project44, FourKites

⚠️ **排除（不要用作种子）：**
- *Convoy* — 停止运营（2023年10月）。标识符仍可解析，历史轮次可用，但不会出现新活动。

### 机器人 / 自动化
种子：Figure AI, Agility Robotics, Locus Robotics, Symbotic, Covariant

### 航天 / 航空
种子：SpaceX, Relativity Space, Rocket Lab, Planet Labs, Astra

## 标识符别名参考

一些知名品牌名称与S&P Global的法律实体名称不匹配。如果品牌名称从 `get_info_from_identifiers` 返回空结果，请尝试别名：

| 品牌名称 | S&P Global法律名称 | company_id |
|---|---|---|
| Together AI | Together Computer, Inc. | C_1860042219 |
| Character.ai | Character Technologies, Inc. | C_1829047235 |
| Runway ML | Runway AI, Inc. | C_633706980 |
| Adept AI | Adept AI Labs Inc. | C_1780739313 |
| xAI | X.AI LLC | C_1863863313 |

> **提示：** 当品牌名称失败时，尝试使用法律名称调用 `get_info_from_identifiers`。如果也失败，公司可能尚未被索引。作为最后手段，直接使用 `company_id` 作为标识符。

## 注意事项

- 这些列表偏向美国公司。对于地理筛选（欧洲、亚洲等），竞争对手扩展步骤尤为重要。
- 对于此处未列出的细分行业，请用户提供2-3个示例公司作为种子。
- 始终验证种子仍然活跃/相关——公司会转型、合并或关闭。
- **刷新频率：** 这些种子应每季度审查。AI行业种子由于收购和新进入者变化特别快。
- 标记为子公司或被收购的种子仍会在 `get_info_from_identifiers` 中解析（状态 = "Operating Subsidiary"）但会返回零融资轮。在融资查询中跳过这些。
