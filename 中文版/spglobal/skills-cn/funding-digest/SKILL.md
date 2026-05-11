---
name: funding-digest
description: "生成一份精炼的一页式 PowerPoint 幻灯片，汇总用户关注行业或公司的近期融资轮次和显著的资本市场活动核心要点。当用户要求提供交易流汇总、每周回顾、融资摘要、交易综述或资本市场简报时，请使用此技能。触发词包括：'deal flow digest'、'weekly funding recap'、'deal roundup'、'transaction summary this week'、'what happened in [sector] this week'、'capital markets update'，或任何将近期融资活动汇编成简报幻灯片的请求。该技能会产出一份专业的单页 PPTX，包含核心要点、估值数据以及 Capital IQ 交易链接。"
---

**AI 免责声明（强制性）：**
你必须在 PowerPoint 页脚中包含以下免责声明文本。这是强制性的——没有此文本报告将不完整：

> **"Analysis is AI-generated — please confirm all outputs"**

**页脚** —— 在生成的幻灯片底部，作为一个显眼的黄色横幅："Analysis is AI-generated — please confirm all outputs"

---

# 每周交易流摘要 (Weekly Deal Flow Digest)

利用 S&P Global Capital IQ 数据，生成一份分析师级别的**单页 PowerPoint 幻灯片**，汇总关注行业或公司的近期融资轮次核心要点。每笔交易均附带 Capital IQ 档案链接，以便快速深入查看。

## 适用场景

在出现以下任何模式时触发：
- "给我这周的交易流摘要"
- "[行业] 的每周融资回顾"
- "最近 [行业/公司] 有哪些交易结束了？"
- "交易综述 (Transaction roundup)" 或 "交易汇总 (deal roundup)"
- "我关注领域的资本市场更新"
- "汇总近期的融资活动"
- 任何关于交易、融资或轮次的定期简报请求

## 嵌套技能

此技能产出一份单页 PPTX 简报：
- 在生成 PowerPoint 之前**阅读** `/mnt/skills/public/pptx/SKILL.md`（及其子参考 `pptxgenjs.md` 以便从零开始创建）

## 实体识别与工具稳健性

S&P Global 的标识符系统可将公司名称解析为法律实体。这在大多数情况下运行良好，但已知存在会导致返回空结果的失败模式。**在整个工作流程中应用以下规则，以避免静默数据丢失。**

### 规则 0：在查询融资前，预验证所有标识符

在调用任何融资工具**之前**，先通过 `get_info_from_identifiers` 运行所有标识符。这是及早发现问题最廉价且最可靠的方法。检查响应中的两点：

1. **是否解析成功？** 如果标识符返回空值或错误，说明该名称在 S&P Global 中不存在。尝试使用 `references/sector-seeds.md` 中的别名、法律实体名称或直接使用 `company_id`。
2. **`status` 字段是什么？** 
   - `"Operating"`（营运中）→ 可以安全查询融资轮次。
   - `"Operating Subsidiary"`（营运子公司）→ 公司存在但由母公司所有。它将返回**零个融资轮次**。在摘要中将其注明为背景信息（例如，“由 [母公司] 收购”），但不要查询其融资。
   - 任何其他状态（如关闭、非活跃）→ 公司已不再运营。可能存在历史数据，但不会有新活动。

**这一预验证步骤可防止大多数空结果问题。** 将所有候选者合并到单个 `get_info_from_identifiers` 调用中（该工具处理大批量任务表现出色），并在继续操作前进行分类筛选。

### 规则 1：绝不轻信空结果，需有备选方案

如果 `get_rounds_of_funding_from_identifiers` 对你预期有数据的公司返回空值：
1. **尝试法律实体名称或 company_id。** 品牌名称通常有效，但有些则不然。请参阅 `references/sector-seeds.md` 中的别名表以查找已知的匹配问题。常见模式："[品牌] AI" → "[法律名称], Inc."（例如，Together AI → "Together Computer, Inc."，Character.ai → "Character Technologies, Inc."，Runway ML → "Runway AI, Inc."）。
2. **验证公司是否存在于 S&P 中。** 如果跳过了规则 0，现在请调用 `get_info_from_identifiers(identifiers=["Company"])` —— 如果这也返回空值，则该公司可能处于极其早期阶段或尚未被收录。

### 规则 2：子公司没有融资轮次

作为大型公司部门或全资子公司的公司（例如，Alphabet 旗下的 DeepMind、微软旗下的 GitHub、Voodoo 旗下的 BeReal）将返回**零个融资轮次**。它们的资本事件是在母公司层面进行追踪的。

**如何检测：** `get_info_from_identifiers` 返回的 `status` 字段将显示为 `"Operating Subsidiary"`。`references/sector-seeds.md` 文件也标注了已知的子公司并附带 ⚠️ 警告。融资查询时应跳过这些公司。

### 规则 3：首选 `get_rounds_of_funding_from_identifiers` 而非 `get_funding_summary_from_identifiers`

摘要工具速度更快但可靠度较低 —— 即使存在详细的轮次数据，它也可能返回错误或不完整的数据。务必始终将详细融资轮次工具作为主要数据源。摘要工具仅适用于快速的总量检查（总融资金额、轮次计数），如果结果看起来偏低，应与轮次工具进行核对。

### 规则 4：谨慎分批并验证

处理大型公司群体（50 家以上公司）时，按 15–20 家一组进行分批。每批处理后，检查返回空结果的公司，并在继续之前按照规则 1 中的备选方案步骤运行。

### 规则 5：`role` 参数至关重要

- `company_raising_funds` → “X 公司融了多少钱？”（公司视角）
- `company_investing_in_round_of_funding` → “投资者 Y 投了什么？”（投资者视角）

使用错误的角色会导致静默返回空结果。对于交易流摘要，几乎总是需要使用 `company_raising_funds`。仅在专门分析投资者的投资组合活动时才使用投资者角色。

### 规则 6：标识符解析不区分大小写，但对拼写敏感

S&P Global 可以处理大小写变化（"openai" = "OpenAI"），但对拼写和标点符号要求严格。"Character AI" 可能会失败，而 "Character.ai" 则可能成功。如有疑问，请使用 `company_id`（例如 `C_1829047235`），这可以确保成功解析。

## 工作流程

### 步骤 1：确定覆盖范围与时间跨度

确定摘要应涵盖的内容。有两种设定：

**老用户（已有关注列表）：**
如果用户之前定义过要追踪的行业或公司，请使用该列表。检查对话历史记录以获取之前的关注列表。

**新用户：**
询问以下参数：

| 参数 | 默认值 | 备注 |
|-----------|---------|-------|
| **行业 (Sectors)** | *(至少一个)* | 例如，“人工智能、金融科技、生物技术” |
| **特定公司** | 可选 | 补充行业层面的覆盖范围 |
| **时间跨度** | 过去 7 天 | “本周”、“过去 2 周”、“本月” |

以此计算时间段的具体 `start_date`（开始日期）和 `end_date`（结束日期）。

### 步骤 2：构建公司全集 (Company Universe)

针对指定的每个行业，使用经过验证的“自举 (bootstrapping)”法构建公司全集：

1. **从领域知识中获取种子公司**（参见 `references/sector-seeds.md`）
   - 注意种子文件中的 ⚠️ 警告和别名注释——一些知名公司是子公司、已被收购，或需要特定的法律名称才能解析。
   - 种子文件包含已知别名不匹配的 `company_id`。如果品牌名称解析失败，请直接使用这些 ID。

2. **立即预验证所有种子**（规则 0）：
   ```
   get_info_from_identifiers(identifiers=[该行业所有种子])
   ```
   将结果分为两类：
   - ✅ **已解析且营运中** (`status` = "Operating") → 继续进行竞争对手扩张
   - ❌ **未解析或子公司** → 使用种子文件中的别名/法律名称重试；子公司注明
