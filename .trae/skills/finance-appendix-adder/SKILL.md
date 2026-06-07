---
name: "finance-appendix-adder"
description: "Adds a detailed, beginner-friendly 'Appendix: 金融背景知识' section to translated Chinese finance articles. Invoke when user requests supplementing/adding/updating financial knowledge appendix to a translated file, or when 'missing_appendix_list.json' shows files with status '缺失附录'. The appendix MUST be written in plain conversational Chinese (讲人话、深入浅出、结合实际), NOT as a vocabulary list or table of terms. Common financial knowledge is extracted into a shared knowledge base under '中文版/金融知识学习/' and is referenced (not duplicated) from each file's appendix."
---

# Finance Appendix Adder (讲人话版 · 知识库联动)

This skill appends a **Appendix: 金融背景知识** section to translated Chinese markdown files in the `中文版/` directory. The appendix is written for **金融领域的小白 (financial beginners)**, assuming the reader knows essentially nothing about finance. The dominant writing style is **讲故事 (storytelling) + 打比方 (analogies) + 举真实例子 (real-world examples)**, NOT a glossary or table dump.

## 核心架构：共享知识库 + 文件级附录

```
中文版/
├── 金融知识学习/                  # 共享金融知识库（按主题拆分）
│   ├── INDEX.md                   # 总索引
│   ├── 投资银行.md                # 投行/IB/卖方/买方
│   ├── 估值方法.md                # DCF/Comps/Precedent/倍数
│   ├── 并购.md                    # M&A 流程/类型/反垄断
│   ├── 股权研究.md                # Equity Research / 评级
│   ├── 财报分析.md                # 三大报表/GAAP/现金流
│   ├── SaaS与科技公司.md          # ARR/NRR/Rule of 40
│   ├── 销售与业务拓展.md          # Sales/BD/漏斗/ICP
│   ├── 资本市场.md                # IPO/债券/信用评级
│   ├── 风险投资.md                # VC 融资轮次/估值
│   ├── 私募股权与LBO.md           # PE/杠杆收购
│   ├── 公司战略与企发.md          # Corp Dev / M&A
│   └── 信用与固定收益.md          # Credit / Fixed Income
└── plugins/.../各文件末尾的 Appendix: 金融背景知识
        ↓
    通过相对路径引用知识库文件，并补充"本文件专属"内容
```

## 核心原则

| Principle | Implementation |
|-----------|---------------|
| **共享 ≠ 复制** | 多个文件涉及的"通用金融知识"放在 `金融知识学习/` 目录下独立成文，每个附录只引用，不重复 |
| **本文件专属** | 附录里只讲这份文件**独有的**概念和"如何应用于本模板"。通用部分指向知识库链接 |
| **讲故事，不要背字典** | 用一个具体故事或场景切入概念 |
| **打比方** | 把抽象概念类比成读者熟悉的事物 |
| **举真实例子** | 真实公司、真实数据：苹果、英伟达、微软、Anthropic、Stripe、Datadog、Synopsys |
| **白话优先** | "扣掉所有开销后真金白银剩多少"代替"净利润" |
| **6-10 节讲透** | 不追求节数堆砌 |

## Anti-Patterns (绝对不要做)

| ❌ 错误做法 | ✅ 正确做法 |
|------------|------------|
| 在每个附录里重新讲一遍"什么是 DCF"、"什么是 M&A" | 在 `估值方法.md` 讲一次，所有附录用相对路径引用 `../../金融知识学习/估值方法.md` |
| 罗列几十个术语表 | 把术语融入故事；通用术语放进知识库对应文件 |
| 多个附录里出现几乎相同的"投行是什么"段落 | 投行知识统一在 `投资银行.md` |
| 一句话定义后立刻跳到下一个概念 | 讲完概念一定说"这意味着什么 / 实际中怎么用" |
| 用学术腔 | 用聊天腔 |
| 把所有销售术语罗列成"100 词速查表" | 用一段话讲"销售这个工作到底是干嘛的" |

## Required Workflow

### Step 1: Read the Target File

Read the full translated file. Identify **topic context**: VC, M&A, fixed income, FX, SaaS, regulatory, AI, sales, etc.

### Step 2: 列出本文件涉及的主题关键词

从文件中提取**所有**金融主题词，例如对 `tear-sheet/ib-ma.md`：
- 投资银行 / 投行
- 并购 / M&A
- 估值 / DCF / Comps / Precedent
- LBO / 杠杆收购
- IPO
- 反垄断 / 监管
- 信用评级
- 商誉 / Earn-out
- Sources & Uses

### Step 3: 检查知识库覆盖情况

对每个主题词，检查 `中文版/金融知识学习/` 目录下是否已有对应文件。

**判断规则**：

| 知识库现状 | 动作 |
|-----------|------|
| 文件**不存在** | **新建**该主题文件（先创建内容，再回到本文件引用） |
| 文件**存在但内容单薄** | **更新**该文件，补充本文件涉及的概念（去重、合并） |
| 文件**存在且内容充足** | 直接在附录中**引用**：`[估值方法](../../金融知识学习/估值方法.md)` |
| 概念**跨多个主题** | 选择"主归属文件"，其他文件给出交叉引用 |

### Step 4: 必要时检索/更新知识库

对**新建或更新**的知识库文件：
- 用 `WebSearch` 验证真实数据
- 遵循"故事 + 比喻 + 真实例子 + 现实意义"四步走
- 4-8 节，每节讲透
- 真实公司、真实数据
- 避免术语堆砌

### Step 5: 写本文件专属附录

本文件附录的**结构**：

```markdown


---

## Appendix: 金融背景知识

<1-2 句开场：本文件是关于什么的 / 读完你会了解什么>

> **本附录的"通用金融知识"部分已抽离到独立知识库文件。** 你可以按需阅读：
>
> - [投资银行](../../金融知识学习/投资银行.md) — 投行本质、卖方/买方、顶尖机构
> - [并购](../../金融知识学习/并购.md) — M&A 流程、类型、反垄断
> - [估值方法](../../金融知识学习/估值方法.md) — DCF / Comps / Precedent
> - [资本市场](../../金融知识学习/资本市场.md) — IPO / 债券 / 信用评级
>
> 下面只讲**本文件模板独有**的内容。

---

### 1. <本文件模板的核心设计逻辑>

讲清"这页模板为什么这么设计、给谁看、怎么用"。

### 2. <本文件模板的字段/章节含义>

解释每个字段、每个章节的现实意义。

### 3. <本文件涉及但需要补充的独有概念>

这些概念可能没被知识库覆盖，或需要结合本文件做具体说明。

### N. <本文件的一句话总结>

> **给小白的一句话**：<鼓励性话语，针对本文件场景>
```

### Step 6: 写作风格硬性要求（本文件附录部分）

每节必须包含：
1. **一个生活化比喻**
2. **一个真实公司或真实事件的例子**
3. **一个"所以这意味着什么"的解释**

**严格禁止**：
- ❌ 把已经在 `金融知识学习/xxx.md` 写过的概念重新大段抄一遍
- ❌ 出现 50+ 行的"术语速查表"
- ❌ 一节里堆 3 个以上大表格

### Step 7: 编辑文件

用 Edit/Write 工具，在文件末尾追加 `---` 分隔符和附录。**不要修改原文**。

### Step 8: 更新知识库索引

如果新建/更新了知识库文件，更新 `金融知识学习/INDEX.md`：
- 在对应主题分类下添加文件名
- 如果是**新主题**（之前没在索引里），新增分类

### Step 9: 更新 JSON 状态

在 `missing_appendix_list.json` 中把对应文件状态改为 `"已完成 (YYYY-MM-DD)"`，更新 summary 统计。

## 知识库主题清单（持续扩展）

| 主题 | 文件 | 主要内容 |
|------|------|---------|
| 投资银行 | `投资银行.md` | 投行本质、卖方/买方、顶尖机构、收入来源 |
| 估值方法 | `估值方法.md` | DCF / Comps / Precedent / Football Field / 估值倍数 |
| 并购 | `并购.md` | M&A 类型/流程/友好 vs 恶意/反垄断 |
| 股权研究 | `股权研究.md` | 卖方研究 / 评级 / 目标价 / 共识预期 |
| 财报分析 | `财报分析.md` | 三大报表 / GAAP vs Non-GAAP / 现金流 |
| SaaS与科技 | `SaaS与科技公司.md` | ARR / NRR / Rule of 40 / CAC Payback |
| 销售与业务拓展 | `销售与业务拓展.md` | Sales vs BD / 漏斗 / ICP / Buyer Persona |
| 资本市场 | `资本市场.md` | IPO / 债券 / 信用评级 / 锁定期 |
| 风险投资 | `风险投资.md` | VC 融资轮 / 估值方法 / 关键条款 |
| 私募股权与LBO | `私募股权与LBO.md` | PE 模式 / 杠杆收购 / 2-3-4-5 法则 |
| 公司战略与企发 | `公司战略与企发.md` | Corp Dev / 并购整合 / 协同效应 |
| 信用与固定收益 | `信用与固定收益.md` | 信用评级 / 债券 / 利率 |

## Quality Checklist (自检)

- [ ] **不重复**：通用金融知识没有在本文件附录里重新讲一遍，而是引用了知识库文件
- [ ] **本文件专属**：本附录有至少 3 节"本文件模板独有"的内容（设计逻辑、字段含义、专属概念）
- [ ] **知识库同步**：如果新增了通用知识，已经在 `金融知识学习/xxx.md` 写好并更新了 `INDEX.md`
- [ ] **没有术语表**：不出现 50+ 行的速查表
- [ ] **真实案例**：至少 3 个真实公司/数据
- [ ] **聊天腔**：不出现学术腔
- [ ] **原文未改**：翻译原文保持不变

## Batch Mode

当用户说"继续更新 N 个缺失金融知识附录的文件"时：
1. 读 `missing_appendix_list.json` 找出候选
2. **先扫一遍所有候选文件涉及的主题**，确定需要新建/更新的知识库文件
3. **先建/更新知识库文件**（去重、合并、丰富内容）
4. **再批量生成附录**（每篇只写本文件专属部分 + 引用）
5. 用 TodoWrite 跟踪进度
6. 完成后批量更新 JSON 和 INDEX

## Reference Files

- Target directory: `中文版/`
- Status file: `missing_appendix_list.json`
- Knowledge base: `中文版/金融知识学习/`
- Knowledge base index: `中文版/金融知识学习/INDEX.md`

### 已完成示例（新风格 + 知识库联动目标）
- `中文版/plugins/partner-built/spglobal/README.md`
- `中文版/plugins/partner-built/spglobal/skills/earnings-preview-beta/references/earnings-preview-framework.md`
- `中文版/plugins/partner-built/spglobal/skills/tear-sheet/references/corp-dev.md`
- `中文版/plugins/partner-built/spglobal/skills/funding-digest/references/sector-seeds.md`
- `中文版/plugins/partner-built/spglobal/skills/earnings-preview-beta/report-template.md`

### 已按新风格重写（待链接到知识库）
- `中文版/plugins/partner-built/spglobal/skills/tear-sheet/references/equity-research.md`
- `中文版/plugins/partner-built/spglobal/skills/tear-sheet/references/sales-bd.md`
- `中文版/plugins/partner-built/spglobal/skills/tear-sheet/references/ib-ma.md`
