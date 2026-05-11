---
name: funding-digest
description: "生成专业的单页 PowerPoint 幻灯片，总结用户关注的行业或公司近期融资轮次和重要资本市场活动的关键要点。当用户请求交易流程摘要、每周回顾、融资摘要、交易综述或资本市场简报时使用此技能。触发条件：'deal flow digest'、'weekly funding recap'、'deal roundup'、'transaction summary this week'、'what happened in [sector] this week'、'capital markets update'，或任何将近期融资活动汇编成简报幻灯片的请求。生成专业的单页 PPTX，包含关键要点、估值数据和 Capital IQ 交易链接。"
---

**AI 免责声明（强制性）：**
您必须在 PowerPoint 页脚中包含以下免责声明文本。这不是可选的 —— 报告不完整将无效：

> **"分析由 AI 生成 — 请确认所有输出"**

**页脚** — 在生成的幻灯片底部，作为突出的黄色横幅："分析由 AI 生成 — 请确认所有输出"

---

# 每周交易流程摘要

使用 S&P Global Capital IQ 数据生成分析师级别的**单页 PowerPoint**，总结关注行业或公司近期融资轮次的关键要点。每笔交易都链接回其 Capital IQ 资料，便于快速深入分析。

## 使用场景

在以下任何模式触发时使用：
- "Give me a deal flow digest for this week"（给我本周的交易流程摘要）
- "Weekly funding recap for [sector]"（[行业] 的每周融资回顾）
- "What deals closed in [sector/companies] recently?"（[行业/公司] 最近完成了哪些交易？）
- "Transaction roundup" 或 "deal roundup"（交易综述）
- "Capital markets update for my coverage universe"（我覆盖范围内的资本市场更新）
- "Summarize recent funding activity"（总结近期融资活动）
- 任何关于交易、融资或轮次的定期简报请求

## 嵌套技能

此技能生成单页 PPTX 简报：
- **阅读** `/mnt/skills/public/pptx/SKILL.md` 后再生成 PowerPoint（及其子参考 `pptxgenjs.md` 用于从头创建）

## 实体解析与工具健壮性

S&P Global 的标识符系统将公司名称解析为法律实体。这对大多数公司都有效，但存在已知的失败模式会导致空结果。**在整个工作流程中应用这些规则，避免静默数据丢失。**

### 规则 0：在查询融资前预验证所有标识符

**在**调用任何融资工具之前，通过 `get_info_from_identifiers` 运行每个标识符。这是尽早发现问题的最廉价、最可靠的方法。检查响应中的两件事：

1. **是否解析成功？** 如果标识符返回空/错误，说明该名称在 S&P Global 中不存在。尝试从 `references/sector-seeds.md` 获取别名、法律实体名称或直接使用 `company_id`。
2. **`status` 字段是什么？** 
   - `"Operating"` → 可以安全查询融资轮次。
   - `"Operating Subsidiary"` → 公司存在但为母公司所有。将返回**零融资轮次**。在摘要中注明此背景（例如，"被 [母公司] 收购"），但不要查询融资。
   - 任何其他状态（例如，closed、inactive）→ 公司不再运营。可能存在历史数据，但没有新活动。

**这单个预验证步骤可防止大多数空结果问题。** 将所有候选公司批量到单个 `get_info_from_identifiers` 调用中（它能很好地处理大批量），然后在继续之前进行分类。

### 规则 1：永远不要信任没有后备方案的空结果

如果 `get_rounds_of_funding_from_identifiers` 为您期望有数据的公司返回空结果：
1. **尝试法律实体名称或 company_id。** 品牌名称通常有效，但有些不行。有关已知不匹配，请参见 `references/sector-seeds.md` 中的别名表。常见模式："[品牌] AI" → "[法律名称], Inc."（例如，Together AI → "Together Computer, Inc."，Character.ai → "Character Technologies, Inc."，Runway ML → "Runway AI, Inc."）。
2. **验证公司是否存在于 S&P 中。** 如果跳过了规则 0，现在调用 `get_info_from_identifiers(identifiers=["Company"])` —— 如果这也返回空，则公司可能处于早期阶段或尚未被索引。

### 规则 2：子公司没有融资轮次

属于大公司的部门或全资子公司（例如，Alphabet 旗下的 DeepMind、Microsoft 旗下的 GitHub、Voodoo 旗下的 BeReal）将返回**零融资轮次**。它们的资本事件在母公司层面跟踪。

**如何检测：** `get_info_from_identifiers` 返回的 `status` 字段将显示 `"Operating Subsidiary"`。`references/sector-seeds.md` 文件也会用 ⚠️ 警告标记已知子公司。跳过这些公司的融资查询。

### 规则 3：使用 `get_rounds_of_funding_from_identifiers` 作为主要工具，而非 `get_funding_summary_from_identifiers`

摘要工具速度更快但不太可靠 —— 即使存在详细轮次数据，它也可能返回错误或不完整数据。始终使用详细轮次工具作为主要数据源。摘要工具仅适用于快速汇总检查（总融资额、轮次数），如果结果看起来偏低，应与轮次工具进行验证。

### 规则 4：分批处理并验证

处理大型公司群组（50+ 家公司）时，分批处理，每组 15-20 家。每批处理后，检查返回空结果的公司，并在继续之前通过规则 1 中的后备步骤运行它们。

### 规则 5：`role` 参数至关重要

- `company_raising_funds` → "X 进行了哪些轮次融资？"（公司视角）
- `company_investing_in_round_of_funding` → "投资者 Y 投资了什么？"（投资者视角）

使用错误的角色会静默返回空结果。对于交易流程摘要，您几乎总是需要 `company_raising_funds`。只有在专门分析投资者的投资组合活动时才使用投资者角色。

### 规则 6：标识符解析不区分大小写但区分拼写

S&P Global 处理大小写变体（"openai" = "OpenAI"），但对拼写和标点符号严格。"Character AI" 可能失败，而 "Character.ai" 可能成功。如有疑问，使用 `company_id`（例如，`C_1829047235`），保证能解析成功。

## 工作流程

### 步骤 1：确定覆盖范围和时间段

确定摘要应覆盖的内容。有两种设置：

**回访用户（有观察列表）：**
如果用户之前定义了要跟踪的行业或公司，使用该列表。检查对话历史中的先前观察列表。

**新用户：**
询问：

| 参数 | 默认值 | 备注 |
|-----------|---------|-------|
| **行业** | *(至少一个)* | 例如，"AI、金融科技、生物科技" |
| **特定公司** | 可选 | 补充行业级覆盖 |
| **时间段** | 最近 7 天 | "本周"、"过去 2 周"、"本月" |

从时间段计算确切的 `start_date` 和 `end_date`。

### 步骤 2：构建公司群组

对于指定的每个行业，使用经过验证的引导方法构建公司群组：

1. **来自领域知识的种子公司**（参见 `references/sector-seeds.md`）
   - 注意种子文件中的 ⚠️ 警告和别名说明 —— 一些知名公司是子公司、已被收购或需要特定法律名称才能解析。
   - 种子文件包含已知别名不匹配的 `company_id` 值。如果品牌名称失败，直接使用这些值。

2. **立即预验证所有种子**（规则 0）：
   ```
   get_info_from_identifiers(identifiers=[all_seeds_for_this_sector])
   ```
   将结果分类到两个桶中：
   - ✅ **已解析且运营中** (`status` = "Operating") → 继续竞争对手扩展
   - ❌ **未解析或子公司** → 使用种子文件中的别名/法律名称重试；子公司会被记录背景但排除在融资查询之外

3. **通过竞争对手扩展**（仅使用 ✅ 已解析的种子）：
   ```
   get_competitors_from_identifiers(identifiers=[resolved_seeds], competitor_source="all")
   ```

4. **验证扩展后的群组：**
   ```
   get_info_from_identifiers(identifiers=[new_competitors])
   ```
   应用相同的分类。按 `simple_industry` 匹配目标行业进行过滤。删除任何未解析的名称或子公司。

如果用户提供特定公司，直接添加它们，但仍需通过预验证分类。永远不要跳过验证 —— 即使是知名品牌名称也可能静默失败。

保持群组可管理 —— 每个行业目标为 15-40 家**已解析、运营中**的公司。对于多行业摘要，这可能总共 50-100+ 家公司。

### 步骤 3：获取融资轮次

对于群组中的所有公司：

```
get_rounds_of_funding_from_identifiers(
    identifiers=[batch],
    role="company_raising_funds",
    start_date="YYYY-MM-DD",
    end_date="YYYY-MM-DD"
)
```

如果群组很大，分批处理，每组 15-20 家。

**每批处理后，识别返回空结果的公司。** 对于任何预期有活动的公司：
1. 使用法律实体名称或备用标识符重试（参见上面的实体解析规则）。
2. 仅在用尽后备方案后才将公司记录为"无数据"。

收集成功结果中的所有 `transaction_id` 值，然后用详细轮次信息丰富：

```
get_rounds_of_funding_info_from_transaction_ids(
    transaction_ids=[all_funding_ids]
)
```

将所有交易 ID 一次性传入（或少量调用），而不是每次交易调用一次 —— 该工具能高效处理批量请求。

**从每轮融资中提取以下信息（对幻灯片至关重要）：**
- `transaction_id` — 需要用于 Capital IQ 交易链接
- **公告日期** — 轮次公开宣布的日期
- **完成日期** — 轮次正式完成的日期
- 融资金额
- **投前估值**（如披露）
- **投后估值**（如披露）
- 领投方
- 轮次类型（A轮、B轮、C轮等）
- 证券条款
- 顾问
- 定价趋势（上涨/下跌/持平）

> **日期是必需的。** 公告日期和完成日期必须始终出现在最终幻灯片的交易表中。如果只有一个日期可用，显示该日期并将另一个标记为"—"。

### 步骤 4：获取重大交易的公司背景

对于参与重大交易（大型轮次、显著估值变化）的任何公司，获取简要描述：

```
get_company_summary_from_identifiers(identifiers=[notable_companies])
```

这为叙述添加背景（例如，"该公司是一家成立于 2021 年的 AI 基础设施初创公司，正在扩展到..."）。

### 步骤 5：识别亮点与趋势

在设计幻灯片之前，分析数据以呈现故事：

**标记为"值得关注"：**
- 轮次 ≥ 1亿美元
- 下跌轮次（定价趋势 = 下跌）
- 新独角兽（投后估值突破 10亿美元）
- 显著估值跃升（投后 ≥ 上一次已知估值的 2 倍）
- 重复融资者（同一公司在 6 个月内再次融资）
- 异常庞大的投资者联盟

**识别趋势：**
- 本期部署的总资本 vs 典型情况（如有历史数据）
- 哪些子行业最热门（轮次最多、资本最多）
- 轮次阶段分布（早期阶段还是后期阶段占主导？）
- 摘要中最活跃的投资者
- 地理集中度
- 估值趋势（投前估值是在压缩还是扩大？）

**选择关键要点（3-5个）：**
将最重要的信号提炼成 3-5 个简洁的项目符号式要点。这些是幻灯片的核心。每个要点应为一句话，简洁有力，并有数据支持。

示例：
- "AI 行业在 8 轮融资中筹集了 24 亿美元 —— 是上周的 3 倍，由 [公司] 的 8 亿美元大型轮次引领，投后估值达 120 亿美元。"
- "[公司] 完成 2 亿美元 D 轮融资，投前估值 35 亿美元，高于其 C 轮的 18 亿美元 —— 表明 AI 开发者工具需求强劲。"
- "下跌轮次活动有所增加：6 轮后期轮次中有 2 轮定价低于先前估值。"

### 步骤 6：生成公司标志

对于关键要点或重大交易中出现的每家公司，使用两层本地管道生成标志。**不要使用 Clearbit**（`logo.clearbit.com`）—— 它已弃用且持续失败。外部标志 CDN（Brandfetch、logo.dev、Google Favicons）需要 API 密钥或被网络限制阻止。相反，使用以下方法：

#### 第一层：`simple-icons` npm 包（3,300+ 品牌 SVG，无需网络）

`simple-icons` 包捆绑了数千个知名品牌的高质量 SVG 图标。它完全离线工作 —— 不需要 API 密钥，不需要网络调用。与 `sharp` 一起安装用于 SVG → PNG 转换：

```bash
npm install simple-icons sharp
```

**查找策略：**

```javascript
const si = require('simple-icons');
const sharp = require('sharp');

// 通过精确标题匹配查找图标（不区分大小写）
function findSimpleIcon(companyName) {
    // 首先尝试精确匹配
    for (const [key, val] of Object.entries(si)) {
        if (!key.startsWith('si') || !val || !val.title) continue;
        if (val.title.toLowerCase() === companyName.toLowerCase()) return val;
    }
    // 尝试去除常见后缀（AI、Inc.、Corp.）
    const stripped = companyName.replace(/\s*(AI|Inc\.?|Corp\.?|Ltd\.?)$/i, '').trim();
    if (stripped !== companyName) {
        for (const [key, val] of Object.entries(si)) {
            if (!key.startsWith('si') || !val || !val.title) continue;
            if (val.title.toLowerCase() === stripped.toLowerCase()) return val;
        }
    }
    return null;
}

// 使用品牌的官方颜色将 SVG 转换为 PNG
async function simpleIconToPng(icon, outputPath) {
    const coloredSvg = icon.svg.replace('<svg', `<svg fill="#${icon.hex}"`);
    await sharp(Buffer.from(coloredSvg))
        .resize(128, 128, { fit: 'contain', background: { r: 255, g: 255, b: 255, alpha: 0 } })
        .png()
        .toFile(outputPath);
}
```

**覆盖率：** 约 43% 的典型交易流程公司（对于 Stripe、Anthropic、Databricks、Snowflake、Discord、Shopify、SpaceX、Mistral AI、Hugging Face 等主要科技品牌很强；对于利基金融科技、生物科技或早期公司较弱）。

#### 第二层：通过 `sharp` 生成基于首字母的后备图标（100% 覆盖率）

对于 `simple-icons` 中找不到的公司，生成一个简洁的基于首字母的标志作为 PNG：

```javascript
async function generateInitialLogo(companyName, outputPath) {
    const initial = companyName.charAt(0).toUpperCase();
    const svg = `
    <svg width="128" height="128" xmlns="http://www.w3.org/2000/svg">
        <circle cx="64" cy="64" r="64" fill="#BDBDBD"/>
        <text x="64" y="64" font-family="Arial, Helvetica, sans-serif"
              font-size="56" font-weight="bold" fill="#FFFFFF"
              text-anchor="middle" dominant-baseline="central">${initial}</text>
    </svg>`;
    await sharp(Buffer.from(svg)).png().toFile(outputPath);
}
```

#### 完整管道

```javascript
async function fetchLogo(companyName, outputDir) {
    const fileName = companyName.toLowerCase().replace(/[\s.]+/g, '-') + '.png';
    const outPath = path.join(outputDir, fileName);

    // 第一层：尝试 simple-icons
    const icon = findSimpleIcon(companyName);
    if (icon) {
        await simpleIconToPng(icon, outPath);
        return { path: outPath, source: 'simple-icons' };
    }

    // 第二层：生成基于首字母的后备图标
    await generateInitialLogo(companyName, outPath);
    return { path: outPath, source: 'initial-fallback' };
}
```

**标志指南：**
- 将所有标志保存到 `/home/claude/logos/[company-name].png`
- 所有标志均为 128×128 PNG，带透明背景
- 在幻灯片上，标志显示高度为 0.35"–0.5" —— 它们是装饰，不是焦点
- 首字母后备圆圈使用灰色（`BDBDBD`）填充，白色文本 —— 与单色调色板一致
- 不要随机混合标志样式 —— 如果大多数公司解析为品牌图标，少数后备图标应自然融入

### 步骤 7：生成单页 PPTX

在创建幻灯片之前，阅读 `/mnt/skills/public/pptx/SKILL.md` 和 `/mnt/skills/public/pptx/pptxgenjs.md`。

使用 `pptxgenjs` 创建**单页** PowerPoint。幻灯片应信息密集但视觉清晰 —— 就像"执行仪表板"而不是"文字墙"。

#### 幻灯片布局

```
┌─────────────────────────────────────────────────────────────┐
│  DEAL FLOW DIGEST                                           │
│  [Period] · [Sectors]                           [Date]      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│  │  $X.XB  │  │  N      │  │  $X.XB  │  │  $X.XB  │       │
│  │ Raised  │  │ Rounds  │  │ 平均投前估值 │  │ Largest │       │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘       │
│                                                             │
│  KEY TAKEAWAYS                                              │
│  ─────────────────────────────────────────────────          │
│  [Logo] Takeaway 1 text goes here...                        │
│  [Logo] Takeaway 2 text goes here...                        │
│  [Logo] Takeaway 3 text goes here...                        │
│  [Logo] Takeaway 4 text goes here...                        │
│                                                             │
│  TOP DEALS                                                  │
│  ┌──────────────────────────────────────────────────────────┐│
│  │Company│Type │Announced│Closed│Amount│Pre-$│Post-$│Lead│🔗││
│  │───────│─────│─────────│──────│──────│─────│──────│────│──││
│  │ ...   │ ... │  ...    │ ...  │ ...  │ ... │ ...  │... │🔗││
│  └──────────────────────────────────────────────────────────┘│
│                                                             │
│  [Footer: Deal Flow Digest · Sources: S&P Global Capital IQ]│
│  [Footer: AI Disclaimer]                                    │
└─────────────────────────────────────────────────────────────┘
```

#### 设计规范

**颜色理念：简约、单色优先。** 幻灯片应像高端财务简报 —— 黑色、白色和灰色为主。颜色仅在承载意义时使用（例如，下跌轮次用红色指示，突出指标用绿色）或读者自然期望的地方（公司标志）。永远不要将颜色用于纯粹装饰目的，如背景填充、装饰条或渐变效果。

**颜色调色板 — 单色执行：**
- 主背景：`FFFFFF`（白色）—— 干净、开放的幻灯片背景
- 页眉栏：`1A1A1A`（近黑色）—— 标题区域形成强烈对比
- 主文本：`1A1A1A`（近黑色）—— 所有正文、统计数字、要点
- 次要文本：`6B6B6B`（中灰色）—— 标签、标题、页脚、日期戳
- 边框和分隔线：`D0D0D0`（浅灰色）—— 微妙的结构线、卡片轮廓、表格边框
- 卡片背景：`F5F5F5`（灰白色/极浅灰色）—— 统计卡片填充、表格交替行
- 链接文本：`2B5797`（深蓝色）—— 表格中的 Capital IQ 交易链接（幻灯片上唯一的蓝色）
- **语义颜色（谨慎使用）：**
  - 下跌轮次或负面信号：`C0392B`（深红色）—— 仅用作小点、标签或单字高亮，永远不要作为填充或背景
  - 突出的正面指标（新独角兽、超大轮次）：`2E7D32`（深绿色）—— 同样最小使用：一个点、一个小标签或一个高亮数字
  - 如果没有数据点需要颜色指示，**完全不使用颜色**。完全单色的幻灯片是完全正确的。

**排版：**
- 标题：28–32pt，粗体，近黑色页眉栏上的白色
- 统计数字：36–44pt，粗体，近黑色
- 统计标签：10–12pt，中灰色（`6B6B6B`）
- 要点文本：12–14pt，近黑色，左对齐
- 表格文本：9–11pt，近黑色，次要列使用灰色（`6B6B6B`）
- 链接文本：9–10pt，深蓝色（`2B5797`）
- 页脚：8pt，中灰色

**统计卡片（顶行）：**
- 4 个关键指标作为大数字标注：总融资额、轮次数、平均投前估值、最大轮次
- 每张卡片使用 `F5F5F5` 填充和细 `D0D0D0` 边框 —— 无阴影、无颜色填充
- 如果某个统计数字令人惊讶或极端（例如，正常交易量的 3 倍，创纪录交易），可以在该单个数字旁边放置一个小色点或下划线 —— 否则保持完全单色
- 如果投前估值大多未披露，用其他指标替换（例如，中位轮次规模、新独角兽数量）

**关键要点（中间部分）：**
- 3–5 个一行要点，每个前缀为相关公司标志（小，约 0.35" 高）
- 如果没有标志，使用**灰色圆圈**和白色公司首字母 —— 不是彩色圆圈
- 左对齐，有足够的间距呼吸
- 下跌轮次或负面要点可以使用小红点前缀；否则不使用颜色
- 在可用的地方包含估值背景（例如，"投后估值达 50 亿美元"）

**顶级交易表（底部部分）：**
- 紧凑表格显示 4–6 个最值得关注的交易
- 列：公司、类型（系列 X）、公告（日期）、完成（日期）、金额（百万美元）、投前（百万美元）、投后（百万美元）、领投方、交易链接
- **公告**和**完成**列以 `MMM DD` 格式显示日期（例如，"Jan 15"）。这些列是必需的，必须始终存在。如果日期不可用，显示"—"。
- **交易链接**列包含可点击的"查看 →"文本，链接到 Capital IQ：
  ```
  https://www.capitaliq.spglobal.com/web/client?#offering/capitalOfferingProfile?id=<transaction_id>
  ```
  其中 `<transaction_id>` 是来自 `get_rounds_of_funding_from_identifiers` 的 `transaction_id`。
- 如果投前或投后估值未披露，在该单元格中显示"—"
- 表头行使用近黑色（`1A1A1A`）填充和白色文本；交替行使用 `F5F5F5` 和 `FFFFFF`
- **将表格水平居中**在幻灯片上。计算表格的总宽度，然后设置 `x` 使其在幻灯片宽度内居中：`x = (slideWidth - tableWidth) / 2`。对于 16:9 布局（13.33" 宽），如果表格宽 12"，使用 `x = 0.67`。永远不要将表格左对齐到幻灯片边缘。
- 保持紧凑 —— 这是参考，不是焦点
- 表格单元格中没有彩色填充。如果交易是下跌轮次，可以在金额旁边添加一个小红文本标签"(↓ down)" —— 这是表格中唯一允许的颜色。

**交易链接实现（pptxgenjs）：**
在 pptxgenjs 中，使用单元格对象上的 `options.hyperlink` 属性将超链接添加到表格单元格：
```javascript
// 带有 Capital IQ 交易链接的表格单元格
{
  text: "View →",
  options: {
    hyperlink: {
      url: `https://www.capitaliq.spglobal.com/web/client?#offering/capitalOfferingProfile?id=${transactionId}`
    },
    color: "2B5797",
    fontSize: 9,
    fontFace: "Arial"
  }
}
```

**表格居中（pptxgenjs）：**
始终将交易表格居中在幻灯片上。动态计算 x 位置：
```javascript
const SLIDE_W = 13.33; // 16:9 幻灯片宽度
const TABLE_W = 12.5;  // 表格总宽度（所有列宽之和）
const TABLE_X = (SLIDE_W - TABLE_W) / 2; // ≈ 0.42"

slide.addTable(tableRows, {
  x: TABLE_X,
  y: tableY,
  w: TABLE_W,
  colW: [1.8, 0.9, 0.9, 0.9, 1.0, 1.1, 1.2, 1.6, 0.7], // Company, Type, Announced, Closed, Amount, Pre-$, Post-$, Lead, Link
  // ... 其他选项
});
```
根据需要调整 `colW` 值，但始终从 `(SLIDE_W - sum(colW)) / 2` 重新计算 `TABLE_X` 以保持表格居中。

**页脚：**
- 中灰色的小文本："Deal Flow Digest · [Period] · Sources: S&P Global Capital IQ · Generated [Date]"

**通用颜色规则（严格执行）：**
- 公司标志是幻灯片上唯一的"全彩色"元素 —— 按来源原样显示。
- 交易链接使用深蓝色（`2B5797`）—— 这是除语义红/绿之外唯一的非单色文本颜色。
- 除标志和链接外，幻灯片在黑白打印机上打印时应看起来正确。
- 永远不要将颜色应用于背景、装饰条、装饰形状或分区线。
- 如有疑问，保持灰色。

#### 代码结构

```javascript
const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title = "Deal Flow Digest";

const slide = pres.addSlide();
const SLIDE_W = 13.33; // 16:9 幻灯片宽度（英寸）

// 1. 深色页眉栏，带标题和时间段
// 2. 统计卡片行（4 张卡片：总融资额、轮次数、平均投前估值、最大轮次）
// 3. 带标志的关键要点部分（包含估值背景）
// 4. 顶级交易表，带公告、完成、投前、投后列和 Capital IQ 交易链接
//    - 居中表格：x = (SLIDE_W - tableWidth) / 2
// 5. 页脚

pres.writeFile({ fileName: "/home/claude/deal-flow-digest.pptx" });
```

根据 pptxgenjs 陷阱指南，对阴影和重复样式使用工厂函数（而非共享对象）。

### 步骤 8：幻灯片质量保证

遵循 PPTX 技能的质量保证流程：

1. **内容质量保证：** `python -m markitdown deal-flow-digest.pptx` —— 验证所有文本、数字、公司名称、估值数据和交易链接是否正确
2. **视觉质量保证：** 转换为图像并检查：
   ```bash
   python /mnt/skills/public/pptx/scripts/office/soffice.py --headless --convert-to pdf deal-flow-digest.pptx
   pdftoppm -jpeg -r 200 deal-flow-digest.pdf slide
   ```
   检查重叠元素、文本溢出、对齐问题、低对比度文本、标志尺寸问题以及交易链接文本是否可见。
3. **链接质量保证：** 验证表格中的 Capital IQ URL 是否使用正确的交易 ID 正确格式化。
4. **修复并重新验证** —— 在宣布完成之前至少进行一轮修复和验证。

### 步骤 9：呈现结果

1. 将最终 `.pptx` 复制到 `/mnt/user-data/outputs/`
2. 使用 `present_files` 共享幻灯片
3. 提供 2–3 句话的口头摘要：
   - "您的摘要涵盖 [行业] 的 X 轮融资，总计 Y 美元。"
   - 指出最值得关注的单笔交易及其估值
   - 标记任何令人担忧的趋势（下跌轮次、估值压缩等）

## 错误处理

### 实体解析失败
- **已知公司的空结果：** 首先检查 `get_info_from_identifiers` —— 如果失败，尝试来自 `references/sector-seeds.md` 的别名或直接使用 `company_id`。常见品牌→法律名称不匹配：Together AI → "Together Computer, Inc."，Character.ai → "Character Technologies, Inc."，Runway ML → "Runway AI, Inc."。
- **子公司：** DeepMind、GitHub、Instagram、WhatsApp、YouTube、BeReal 等是子公司 —— 它们没有独立的融资轮次。在背景中注明这些为"已收购/子公司"，但不要报告为"无活动"。
- **已停业公司：** 像 Convoy（2023 年 10 月关闭）这样的公司在 S&P Global 中仍能解析，但永远不会有新活动。`references/sector-seeds.md` 文件会标记这些 —— 在纳入公司之前检查它。
- **`get_funding_summary_from_identifiers` 错误或返回零：** 回退到 `get_rounds_of_funding_from_identifiers` —— 摘要工具不太可靠。永远不要依赖摘要工具作为唯一数据源。
- **错误的 `role` 参数：** 如果投资者视角查询返回空，验证您使用的是 `company_investing_in_round_of_funding`，而不是 `company_raising_funds`（反之亦然）。

### 数据质量问题
- **期间内无活动：** 如果某个行业没有融资轮次，在幻灯片上明确注明（"[行业] 期间内未记录交易"）—— 活动缺失本身就是信息。
- **估值数据稀疏：** 如果大多数交易的投前和投后估值未披露，在页脚注释中注明数据限制，并在表格中使用"—"。将统计卡片调整为显示其他指标（例如，中位轮次规模）而不是平均投前估值。
- **标志检索失败：** `simple-icons` npm 包为典型交易流程公司提供约 43% 的覆盖率。对于其余部分，使用 `sharp` 生成的基于首字母的后备图标。保持一致的图标风格 —— 不要混合随机方法。如果 `simple-icons` 或 `sharp` 安装失败，回退到 pptxgenjs 基于形状的首字母（灰色椭圆 + 白色文本叠加），不需要外部依赖。
- **一张幻灯片容纳不下太多交易：** 如果有超过 6 个值得关注的交易，在表格中显示前 6 个，并添加脚注："+N additional deals not shown."（+N 个其他交易未显示）。按交易规模优先级排序。
- **大型群组：** 对于多行业摘要，包含 100+ 家公司时，将所有 API 调用分批处理，每组 15–20 家。优先关注重大交易的深度，而非次要交易的完整性。
- **陈旧种子：** 如果竞争对手扩展为某个行业返回的结果很少，种子公司可能太局限。通过添加 2–3 个更知名的名称并重新扩展来扩大范围。
- **链接的无效交易 ID：** 如果融资工具返回的 `transaction_id` 无法生成有效的 Capital IQ URL，则省略该行的链接单元格，而不是包含损坏的链接。

## 示例提示

- "Give me a weekly deal flow digest for AI and fintech"（给我 AI 和金融科技的每周交易流程摘要）
- "Summarize this week's funding in biotech"（总结本周生物科技的融资情况）
- "Deal roundup for my coverage — cybersecurity, cloud infrastructure, and dev tools — last 2 weeks"（我覆盖范围的交易综述 —— 网络安全、云基础设施和开发工具 —— 过去 2 周）
- "What happened in venture this week across all sectors I follow?"（我关注的所有行业本周在风险投资领域发生了什么？）
- "Quick deal flow slide for climate tech this month"（本月气候科技的快速交易流程幻灯片）

---

## 金融术语解释

### 1. 融资轮次 (Funding Round)

**定义**：融资轮次是初创公司或成长型公司为筹集资金而进行的一轮融资。通常按字母顺序命名（A轮、B轮、C轮等）。

**轮次类型**：
- **种子轮 (Seed Round)**：最早阶段的融资，用于产品开发和团队组建
- **A轮 (Series A)**：产品已上线，用于扩大市场和用户规模
- **B轮 (Series B)**：公司有明确商业模式，用于加速增长
- **C轮及以后 (Series C+)**：成熟阶段，用于市场扩张、并购或上市准备

**投资者类型**：
- **天使投资者**：个人投资者，通常在早期阶段
- **风险投资 (VC)**：专业投资机构，投资于高增长潜力公司
- **私募股权 (PE)**：后期阶段投资，通常涉及杠杆收购
- **战略投资者**：行业内的大型公司进行战略投资

### 2. 投前估值 (Pre-money Valuation)

**定义**：投前估值是指在新一轮融资注入资金之前，公司的估值。

**计算公式**：
- 投前估值 = 投后估值 - 本轮融资金额

**重要性**：
- **股权稀释**：投前估值决定了新投资者获得的股权比例
- **创始人权益**：较高的投前估值意味着创始人股权稀释较少
- **融资谈判**：投前估值是融资谈判的核心议题

**影响因素**：
- 公司当前的收入和利润
- 市场规模和增长潜力
- 竞争优势和技术壁垒
- 团队素质和执行力

### 3. 投后估值 (Post-money Valuation)

**定义**：投后估值是指在新一轮融资完成后，公司的总估值。

**计算公式**：
- 投后估值 = 投前估值 + 本轮融资金额

**重要性**：
- **公司价值**：反映公司在融资后的总价值
- **独角兽地位**：投后估值达到 10 亿美元的公司被称为独角兽
- **后续融资**：影响下一轮融资的估值基准

**示例**：
- 公司投前估值 5000 万美元，融资 1000 万美元
- 投后估值 = 5000万 + 1000万 = 6000万美元
- 新投资者获得 1000万 / 6000万 = 16.67% 的股权

### 4. 下跌轮次 (Down Round)

**定义**：下跌轮次是指公司在新一轮融资中的估值低于上一轮融资的投后估值。

**原因**：
- **市场环境恶化**：宏观经济下行或行业估值调整
- **公司业绩不及预期**：增长放缓或亏损扩大
- **竞争加剧**：市场份额下降或竞争优势减弱

**影响**：
- **股权稀释加剧**：现有股东的股权价值缩水
- **员工期权价值下降**：期权行权价可能高于当前估值
- **信心危机**：可能影响员工士气和客户信任

**应对策略**：
- 优化成本结构，提高盈利能力
- 寻找战略投资者或并购机会
- 加强公司治理和透明度

### 5. 独角兽公司 (Unicorn)

**定义**：独角兽公司是指估值达到或超过 10 亿美元的初创公司。

**起源**：
- 该术语由风险投资家 Aileen Lee 在 2013 年创造
- 当时达到 10 亿美元估值的初创公司非常罕见，如同独角兽般稀有

**特点**：
- 通常处于高增长行业（科技、生物科技、金融科技等）
- 具有颠覆性的商业模式或技术
- 吸引大量风险投资

**现状**：
- 随着风险投资市场的发展，独角兽数量大幅增加
- 一些独角兽选择通过 SPAC（特殊目的收购公司）上市

### 6. 领投方 (Lead Investor)

**定义**：领投方是在融资轮次中投资金额最大、承担主要尽职调查责任的投资者。

**职责**：
- **牵头谈判**：主导投资条款的谈判
- **尽职调查**：对公司进行全面的尽职调查
- **设定估值**：确定投资估值和条款
- **协调其他投资者**：组织和协调其他参与投资者

**重要性**：
- **信誉背书**：知名投资者的参与增强公司信誉
- **资源支持**：领投方通常提供战略指导和资源
- **后续融资**：领投方可能参与后续轮次融资

### 7. 投资者联盟 (Investor Syndicate)

**定义**：投资者联盟是指共同参与某轮融资的多个投资者组成的团体。

**构成**：
- 领投方：牵头的主要投资者
- 跟投方：跟随领投方参与的其他投资者
- 战略投资者：行业内公司或战略合作伙伴

**优势**：
- **分散风险**：单个投资者的投资金额相对较小
- **资源互补**：不同投资者带来不同的资源和专业知识
- **估值支持**：多个投资者的参与增强对估值的信心

**挑战**：
- **协调困难**：多个投资者可能有不同的利益诉求
- **决策缓慢**：需要协调多个投资者的意见

### 8. 交易流程 (Deal Flow)

**定义**：交易流程是指投资机构在特定时间段内收到和处理的潜在投资机会的数量和质量。

**衡量指标**：
- **交易量**：收到的投资机会数量
- **质量**：投资机会的整体质量和可行性
- **转化率**：从机会到实际投资的比例

**重要性**：
- **投资组合构建**：持续的高质量交易流程是构建优秀投资组合的关键
- **市场情报**：交易流程反映市场趋势和投资热点
- **竞争优势**：强大的交易流程网络是投资机构的核心竞争力

### 9. 资本市场 (Capital Markets)

**定义**：资本市场是指企业和政府筹集长期资金的市场，包括股票市场、债券市场和私募股权市场。

**组成部分**：
- **一级市场**：新证券的发行市场（IPO、债券发行等）
- **二级市场**：已发行证券的交易市场（股票交易所、债券交易市场）
- **私募市场**：未上市证券的交易市场（风险投资、私募股权等）

**功能**：
- **资本配置**：将储蓄引导至最有生产力的用途
- **价格发现**：通过市场交易确定资产价格
- **风险管理**：提供对冲风险的工具和机制

### 10. 企业价值 (Enterprise Value)

**定义**：企业价值是衡量公司总价值的指标，考虑了股权和债务。

**计算公式**：
- 企业价值 = 市值 + 债务 - 现金及等价物

**用途**：
- **并购估值**：在并购交易中常用作定价基础
- **估值比较**：跨公司比较时更准确
- **财务建模**：企业估值模型的核心指标

**与市值的区别**：
- 市值仅考虑股权价值
- 企业价值考虑了公司的资本结构

### 11. 尽职调查 (Due Diligence)

**定义**：尽职调查是投资者在投资前对目标公司进行的全面调查和评估。

**类型**：
- **财务尽职调查**：审查财务报表和会计记录
- **法律尽职调查**：审查法律文件和合规性
- **商业尽职调查**：评估市场地位和竞争优势
- **技术尽职调查**：评估技术资产和知识产权

**目的**：
- **风险识别**：发现潜在的风险和问题
- **价值确认**：验证公司的价值和增长潜力
- **条款谈判**：为投资条款谈判提供依据

### 12. 股权稀释 (Equity Dilution)

**定义**：股权稀释是指公司发行新股导致现有股东持股比例下降的现象。

**计算示例**：
- 创始人持有 100% 股权
- A轮融资发行 25% 新股
- 创始人股权稀释至 75%

**影响**：
- **控制权**：股权稀释可能影响创始人的控制权
- **价值分配**：每股价值可能因稀释而下降
- **激励机制**：需要通过期权等方式激励团队

**管理策略**：
- 合理规划融资节奏
- 使用反稀释条款保护早期投资者
- 通过业绩增长抵消稀释影响

### 13. 估值倍数 (Valuation Multiples)

**定义**：估值倍数是用于评估公司价值的比率，通常基于财务指标。

**常用倍数**：
- **P/E 比率**：市盈率 = 股价 / 每股收益
- **EV/Revenue**：企业价值与收入比率
- **EV/EBITDA**：企业价值与 EBITDA 比率
- **Price/Sales**：市销率

**用途**：
- **相对估值**：与同行业公司比较
- **投资决策**：评估投资机会的吸引力
- **交易定价**：并购交易中的定价参考

**注意事项**：
- 需要结合行业特点和公司阶段
- 倍数本身不提供完整的估值画面
- 需要结合基本面分析

### 14. 首次公开募股 (IPO)

**定义**：首次公开募股是公司第一次向公众发行股票，在证券交易所上市交易。

**流程**：
- **准备阶段**：选择承销商、准备招股说明书
- **路演**：向潜在投资者展示公司
- **定价**：确定发行价格和发行数量
- **上市**：在交易所挂牌交易

**优势**：
- **筹集资金**：获得大规模资本
- **流动性**：股东可以在公开市场交易股票
- **品牌提升**：上市提高公司知名度和信誉

**挑战**：
- **监管要求**：严格的信息披露要求
- **成本高昂**：承销费用和合规成本
- **短期压力**：需要满足季度业绩预期