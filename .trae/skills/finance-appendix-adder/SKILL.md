---
name: "finance-appendix-adder"
description: "Adds a detailed 'Appendix: 金融背景知识' section to translated Chinese finance articles. Invoke when user requests supplementing/adding/updating financial knowledge appendix to a translated file, or when 'missing_appendix_list.json' shows files with status '缺失附录'."
---

# Finance Appendix Adder

This skill appends a comprehensive **Appendix: 金融背景知识** section to translated Chinese markdown files in the `中文版/` directory. The appendix is designed for financial beginners and explains every financial term, concept, framework, and industry context that appears in the file.

## When to Invoke

- User explicitly asks to "补充/添加/更新金融知识附录" for a specific file
- User points to a file in `中文版/` and asks for an "Appendix: 金融背景知识" section
- `missing_appendix_list.json` contains a file with `"status": "缺失附录"` that needs to be resolved
- User asks to "继续更新缺失金融知识附录的文件" (batch mode)

## Inputs

The skill needs:
1. **Target file path** — absolute or relative path under `中文版/`
2. **Optional batch** — multiple files in one call
3. **Optional context** — what the file is about (skill, plugin, topic)

## Core Principles (信达雅 + 初学者友好)

| Principle | Implementation |
|-----------|---------------|
| **越详细越好** | Aim for **8-16 sections**, each with multiple subsections, tables, and formulas |
| **零基础可懂** | Assume reader knows nothing about finance; explain every acronym, every ratio |
| **术语中英对照** | Every term has Chinese name, English name, and abbreviation |
| **公式具体化** | All math formulas written out with variable definitions |
| **真实案例** | Use real companies (Apple, Tesla, MSFT, NVDA, etc.) and real market data |
| **表格密集** | Prefer markdown tables for comparisons, lists, ranges |
| **网络检索** | If unsure about a term/company/regulation, use WebSearch to confirm |

## Required Workflow (Step-by-Step)

### Step 1: Read the Target File

```
Read the full translated file
```

- Note: the file may be HTML/CSS template code (like `report-template.md`) — the appendix still goes at the end
- Identify **topic context**: VC, M&A, fixed income, FX, SaaS, regulatory, AI, etc.

### Step 2: Read Current JSON Status (if applicable)

```
Read missing_appendix_list.json
```

- Find the target file's entry
- Note current `"status"` for later update

### Step 3: Search Web When Needed (Optional but Recommended)

For specialized topics (specific products, regulations, valuation methods), use:
```
WebSearch query: "<topic> financial concept explanation"
WebFetch on official sources: SEC.gov, IFRS.org, S&P Global docs
```

### Step 4: Compose the Appendix

Append the following block to the END of the target file:

```markdown


---

## Appendix: 金融背景知识

<1-2 sentence intro explaining why this appendix is relevant>

---

### 1. <Section 1 Title>
#### 1.1 <Subsection>
**定义**：<term>（<English>，<abbreviation>）is...

| Col1 | Col2 | Col3 |
|------|------|------|
| ... | ... | ... |

#### 1.2 <Subsection>
...
```

#### Minimum Section Coverage (8-16 sections)

Choose sections from these standard buckets, tailored to the file topic:

1. **Topic 基础概念** — core definitions, history, participants
2. **核心术语表** — glossary with Chinese/English/abbreviation
3. **分类与对比** — types, comparison tables
4. **计算公式** — formulas with variable definitions
5. **生命周期/阶段** — stages, rounds, phases
6. **估值方法** — DCF, Comps, Precedents, multiples
7. **关键指标** — KPIs, ratios, benchmarks
8. **参与者/玩家** — major companies, investors, regulators
9. **监管机构** — SEC, FINRA, FCA, CSRC, etc.
10. **风险与红旗** — risk types, fraud signals
11. **行业框架** — Porter's 5 Forces, PESTEL, TAM/SAM/SOM
12. **案例研究** — real company examples
13. **会计基础** — 3 statements, accounting identities
14. **可视化/报告** — chart types, design rules (if file is about reports)
15. **操作流程** — day-in-the-life, checklists
16. **速查表** — 50+ term cheat sheet at the end

#### Style Requirements

- Use `**定义**：` for definitions
- Use tables for ALL comparisons
- Use code blocks for formulas: ` ```\n公式\n``` `
- Use blockquotes for warnings: `> **提示**：...`
- Include real numbers (e.g., "$4.5-4.7B", "10-K", "EPS $2.15")
- Add Chinese-English bilingual term pairs

### Step 5: Edit the File (Append at End)

Use the `Edit` tool:
- Find the last meaningful line/closing of original content
- Append the appendix after a `---` separator
- Do NOT modify the original translated content
- For files that are pure code (HTML templates), still append the appendix AFTER the code block (close the code block first with ` ``` ` if needed)

### Step 6: Update missing_appendix_list.json

For each file completed:
1. Change `"status": "缺失附录"` → `"status": "已完成 (YYYY-MM-DD)"`
2. Update the `summary` section:
   - `has_appendix` += number of files completed
   - `missing_appendix` -= same amount
   - `appendix_coverage_rate` = has_appendix / total_files * 100 (rounded to 2 decimals)

### Step 7: Report to User

Briefly summarize:
- Files updated
- Key topics covered in the appendix
- Updated coverage stats

## Batch Mode

When user says "继续更新 N 个缺失金融知识附录的文件":

1. Read `missing_appendix_list.json` to identify candidates
2. Pick the **top N** files (usually ordered as in the JSON)
3. For each file, run Steps 1-6 sequentially
4. Update the todo list with `TodoWrite` to track progress
5. Update the JSON once at the end (or after each file)

## Quality Checklist (Self-Review Before Reporting Done)

- [ ] 8-16 sections in the appendix
- [ ] Every term has Chinese + English + abbreviation
- [ ] At least 3 comparison tables
- [ ] At least 1 formula with variable definitions
- [ ] Real company/regulator examples included
- [ ] JSON status updated
- [ ] Original file content NOT modified
- [ ] File still parses as valid markdown

## Output Template

```
已完成 [N] 个文件的金融知识附录补充：

1. [file1]
   - 涵盖：[topic1, topic2, ...]
   - X 节详细内容

2. [file2]
   - 涵盖：[topic1, topic2, ...]
   - X 节详细内容

📊 整体进度：已补充 110/253，覆盖率 43.48% → 112/253，覆盖率 44.27%
```

## Common Pitfalls to Avoid

- ❌ Adding only 1-2 sections (user wants **越详细越好**)
- ❌ One-sentence definitions (always expand with examples, formulas, tables)
- ❌ Forgetting to update JSON status
- ❌ Modifying original translated content
- ❌ Skipping the English/Chinese bilingual term pairs
- ❌ Using vague language like "等等" (be specific)
- ❌ Adding appendix to wrong file path
- ❌ Breaking markdown structure (unclosed code blocks, broken tables)

## Reference Files

- Target directory: `中文版/`
- Status file: `missing_appendix_list.json` (project root)
- Completed examples:
  - `中文版/plugins/partner-built/spglobal/README.md` (16 sections)
  - `中文版/plugins/partner-built/spglobal/skills/funding-digest/references/sector-seeds.md` (14 sections)
  - `中文版/plugins/partner-built/spglobal/skills/earnings-preview-beta/report-template.md` (14 sections)
