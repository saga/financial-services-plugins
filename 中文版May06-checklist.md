# 中文版翻译 Checklist

> 对比日期：2026-05-09
> 源目录：`plugins/` (275个文件)
> 目标目录：`中文版May06/` (216个文件)
> 缺失文件总数：**256个**（plugins有但中文版May06缺失）

---

## 📊 统计摘要

| 类别 | 插件/模块数 | plugins文件数 | 中文版May06文件数 | 缺失文件数 |
|------|-------------|--------------|------------------|------------|
| **agent-plugins** | 10个 | ~90 | 0 | ❌ **90** |
| **partner-built** | 2个 | 31 | 0 | ❌ **31** |
| **vertical-plugins** | 7个 | ~154 | ~216* | ⚠️ 135 |
| **总计** | 19个 | **275** | **216** | ❌ **256** |

> *注：中文版May06包含部分已翻译文件及额外内容

---

## ❌ 【P0 - 紧急】整目录缺失

### agent-plugins (10个插件 - 约90个文件)

| # | 插件名称 | 描述 | 状态 |
|---|----------|------|------|
| 1 | **earnings-reviewer** | 财报审核代理 | ❌ 全部缺失 |
| 2 | **gl-reconciler** | 总账对账代理 | ❌ 全部缺失 |
| 3 | **kyc-screener** | KYC筛查代理 | ❌ 全部缺失 |
| 4 | **market-researcher** | 市场研究代理 | ❌ 全部缺失 |
| 5 | **meeting-prep-agent** | 会议准备代理 | ❌ 全部缺失 |
| 6 | **model-builder** | 模型构建代理 | ❌ 全部缺失 |
| 7 | **month-end-closer** | 月末结账代理 | ❌ 全部缺失 |
| 8 | **pitch-agent** | 推介材料代理 | ❌ 全部缺失 |
| 9 | **statement-auditor** | 报表审计代理 | ❌ 全部缺失 |
| 10 | **valuation-reviewer** | 估值审核代理 | ❌ 全部缺失 |

### partner-built (2个插件 - 31个文件)

| # | 插件名称 | 描述 | 状态 |
|---|----------|------|------|
| 1 | **lseg** | LSEG合作伙伴插件 | ❌ 全部缺失 (16文件) |
| 2 | **spglobal** | S&P Global合作伙伴插件 | ❌ 全部缺失 (15文件) |

---

## ⚠️ 【P1 - 高优先级】vertical-plugins 缺失内容

### 1. equity-research（股权研究）- 全部31个文件缺失

| # | 文件路径 |
|---|----------|
| 1 | `.claude-plugin/plugin.json` |
| 2 | `commands/catalysts.md` |
| 3 | `commands/earnings-preview.md` |
| 4 | `commands/earnings.md` |
| 5 | `commands/initiate.md` |
| 6 | `commands/model-update.md` |
| 7 | `commands/morning-note.md` |
| 8 | `commands/screen.md` |
| 9 | `commands/sector.md` |
| 10 | `commands/thesis.md` |
| 11 | `hooks/hooks.json` |
| 12 | `skills/catalyst-calendar/SKILL.md` |
| 13 | `skills/earnings-analysis/SKILL.md` |
| 14 | `skills/earnings-analysis/references/best-practices.md` |
| 15 | `skills/earnings-analysis/references/report-structure.md` |
| 16 | `skills/earnings-analysis/references/workflow.md` |
| 17 | `skills/earnings-preview/SKILL.md` |
| 18 | `skills/idea-generation/SKILL.md` |
| 19 | `skills/initiating-coverage/SKILL.md` |
| 20 | `skills/initiating-coverage/assets/quality-checklist.md` |
| 21 | `skills/initiating-coverage/assets/report-template.md` |
| 22 | `skills/initiating-coverage/references/task1-company-research.md` |
| 23 | `skills/initiating-coverage/references/task2-financial-modeling.md` |
| 24 | `skills/initiating-coverage/references/task3-valuation.md` |
| 25 | `skills/initiating-coverage/references/task4-chart-generation.md` |
| 26 | `skills/initiating-coverage/references/task5-report-assembly.md` |
| 27 | `skills/initiating-coverage/references/valuation-methodologies.md` |
| 28 | `skills/model-update/SKILL.md` |
| 29 | `skills/morning-note/SKILL.md` |
| 30 | `skills/sector-overview/SKILL.md` |
| 31 | `skills/thesis-tracker/SKILL.md` |

### 2. fund-admin（基金管理）- 全部7个文件缺失

| # | 文件路径 |
|---|----------|
| 1 | `.claude-plugin/plugin.json` |
| 2 | `skills/accrual-schedule/SKILL.md` |
| 3 | `skills/break-trace/SKILL.md` |
| 4 | `skills/gl-recon/SKILL.md` |
| 5 | `skills/nav-tieout/SKILL.md` |
| 6 | `skills/roll-forward/SKILL.md` |
| 7 | `skills/variance-commentary/SKILL.md` |

### 3. operations（运营）- 全部1个文件缺失

| # | 文件路径 |
|---|----------|
| 1 | `.claude-plugin/plugin.json` |

### 4. financial-analysis（财务分析）- 缺失38个文件

| # | 文件路径 |
|---|----------|
| 1 | `.claude-plugin/plugin.json` |
| 2 | `.mcp.json` |
| 3 | `commands/3-statement-model.md` |
| 4 | `commands/competitive-analysis.md` |
| 5 | `commands/comps.md` |
| 6 | `commands/dcf.md` |
| 7 | `commands/debug-model.md` |
| 8 | `commands/lbo.md` |
| 9 | `commands/ppt-template.md` |
| 10 | `hooks/hooks.json` |
| 11 | `skills/3-statement-model/SKILL.md` |
| 12 | `skills/3-statement-model/references/formatting.md` |
| 13 | `skills/3-statement-model/references/formulas.md` |
| 14 | `skills/3-statement-model/references/sec-filings.md` |
| 15 | `skills/audit-xls/SKILL.md` |
| 16 | `skills/clean-data-xls/SKILL.md` |
| 17 | `skills/competitive-analysis/SKILL.md` |
| 18 | `skills/competitive-analysis/references/frameworks.md` |
| 19 | `skills/competitive-analysis/references/schemas.md` |
| 20 | `skills/comps-analysis/SKILL.md` |
| 21 | `skills/dcf-model/SKILL.md` |
| 22 | `skills/dcf-model/TROUBLESHOOTING.md` |
| 23 | `skills/dcf-model/requirements.txt` |
| 24 | `skills/dcf-model/scripts/validate_dcf.py` |
| 25 | `skills/deck-refresh/SKILL.md` |
| 26 | `skills/ib-check-deck/SKILL.md` |
| 27 | `skills/ib-check-deck/references/ib-terminology.md` |
| 28 | `skills/ib-check-deck/references/report-format.md` |
| 29 | `skills/ib-check-deck/scripts/extract_numbers.py` |
| 30 | `skills/pptx-author/SKILL.md` |
| 31 | `skills/skill-creator/LICENSE.txt` |
| 32 | `skills/skill-creator/SKILL.md` |
| 33 | `skills/skill-creator/references/output-patterns.md` |
| 34 | `skills/skill-creator/references/workflows.md` |
| 35 | `skills/skill-creator/scripts/init_skill.py` |
| 36 | `skills/skill-creator/scripts/package_skill.py` |
| 37 | `skills/skill-creator/scripts/quick_validate.py` |
| 38 | `skills/xlsx-author/SKILL.md` |

### 5. investment-banking（投资银行）- 缺失24个文件

| # | 文件路径 |
|---|----------|
| 1 | `.claude-plugin/plugin.json` |
| 2 | `.claude/investment-banking.local.md.example` |
| 3 | `.gitignore` |
| 4 | `.mcp.json` |
| 5 | `README.md` |
| 6 | `commands/buyer-list.md` |
| 7 | `commands/cim.md` |
| 8 | `commands/deal-tracker.md` |
| 9 | `commands/merger-model.md` |
| 10 | `commands/one-pager.md` |
| 11 | `commands/process-letter.md` |
| 12 | `commands/teaser.md` |
| 13 | `hooks/hooks.json` |
| 14 | `skills/datapack-builder/SKILL.md` |
| 15 | `skills/deal-tracker/SKILL.md` |
| 16 | `skills/merger-model/SKILL.md` |
| 17 | `skills/pitch-deck/SKILL.md` |
| 18 | `skills/pitch-deck/reference/calculation-standards.md` |
| 19 | `skills/pitch-deck/reference/formatting-standards.md` |
| 20 | `skills/pitch-deck/reference/slide-templates.md` |
| 21 | `skills/pitch-deck/reference/xml-reference.md` |
| 22 | `skills/process-letter/SKILL.md` |
| 23 | `skills/strip-profile/SKILL.md` |
| 24 | `skills/teaser/SKILL.md` |

### 6. private-equity（私募股权）- 缺失23个文件

| # | 文件路径 |
|---|----------|
| 1 | `.claude-plugin/plugin.json` |
| 2 | `.mcp.json` |
| 3 | `commands/ai-readiness.md` |
| 4 | `commands/dd-checklist.md` |
| 5 | `commands/dd-prep.md` |
| 6 | `commands/ic-memo.md` |
| 7 | `commands/portfolio.md` |
| 8 | `commands/returns.md` |
| 9 | `commands/screen-deal.md` |
| 10 | `commands/source.md` |
| 11 | `commands/unit-economics.md` |
| 12 | `commands/value-creation.md` |
| 13 | `hooks/hooks.json` |
| 14 | `skills/ai-readiness/SKILL.md` |
| 15 | `skills/dd-checklist/SKILL.md` |
| 16 | `skills/dd-meeting-prep/SKILL.md` |
| 17 | `skills/deal-screening/SKILL.md` |
| 18 | `skills/deal-sourcing/SKILL.md` |
| 19 | `skills/ic-memo/SKILL.md` |
| 20 | `skills/portfolio-monitoring/SKILL.md` |
| 21 | `skills/returns-analysis/SKILL.md` |
| 22 | `skills/unit-economics/SKILL.md` |
| 23 | `skills/value-creation-plan/SKILL.md` |

### 7. wealth-management（财富管理）- 缺失14个文件

| # | 文件路径 |
|---|----------|
| 1 | `.claude-plugin/plugin.json` |
| 2 | `commands/client-report.md` |
| 3 | `commands/client-review.md` |
| 4 | `commands/financial-plan.md` |
| 5 | `commands/proposal.md` |
| 6 | `commands/rebalance.md` |
| 7 | `commands/tlh.md` |
| 8 | `hooks/hooks.json` |
| 9 | `skills/client-report/SKILL.md` |
| 10 | `skills/client-review/SKILL.md` |
| 11 | `skills/financial-plan/SKILL.md` |
| 12 | `skills/investment-proposal/SKILL.md` |
| 13 | `skills/portfolio-rebalance/SKILL.md` |
| 14 | `skills/tax-loss-harvesting/SKILL.md` |

---

## 🎯 翻译优先级排序

### P0 - 紧急（立即处理）
| 优先级 | 模块 | 缺失文件数 |
|--------|------|------------|
| 1 | agent-plugins (全部10个插件) | ~90 |
| 2 | partner-built/spglobal | 15 |
| 3 | partner-built/lseg | 16 |
| 4 | vertical-plugins/equity-research | 31 |

### P1 - 高优先级
| 优先级 | 模块 | 缺失文件数 |
|--------|------|------------|
| 5 | vertical-plugins/financial-analysis | 38 |
| 6 | vertical-plugins/investment-banking | 24 |
| 7 | vertical-plugins/private-equity | 23 |
| 8 | vertical-plugins/wealth-management | 14 |

### P2 - 中优先级
| 优先级 | 模块 | 缺失文件数 |
|--------|------|------------|
| 9 | vertical-plugins/fund-admin | 7 |
| 10 | vertical-plugins/operations | 1 |

---

## ✅ 翻译进度追踪

### agent-plugins
| 插件 | 文件数 | 进度 |
|------|--------|------|
| earnings-reviewer | 11 | [ ] 0% |
| gl-reconciler | 6 | [ ] 0% |
| kyc-screener | 2 | [ ] 0% |
| market-researcher | 3 | [ ] 0% |
| meeting-prep-agent | 5 | [ ] 0% |
| model-builder | 14 | [ ] 0% |
| month-end-closer | 7 | [ ] 0% |
| pitch-agent | 25 | [ ] 0% |
| statement-auditor | 5 | [ ] 0% |
| valuation-reviewer | 5 | [ ] 0% |

### partner-built
| 插件 | 文件数 | 进度 |
|------|--------|------|
| lseg | 16 | [ ] 0% |
| spglobal | 15 | [ ] 0% |

### vertical-plugins
| 模块 | 文件数 | 进度 |
|------|--------|------|
| equity-research | 31 | [ ] 0% |
| financial-analysis | 38 | [ ] 0% |
| fund-admin | 7 | [ ] 0% |
| investment-banking | 24 | [ ] 0% |
| operations | 1 | [ ] 0% |
| private-equity | 23 | [ ] 0% |
| wealth-management | 14 | [ ] 0% |

---

## 📁 目录结构对比图

```
plugins/
├── agent-plugins/                    ❌ 中文版May06缺失 (10个插件)
│   ├── earnings-reviewer/            ❌
│   ├── gl-reconciler/                ❌
│   ├── kyc-screener/                 ❌
│   ├── market-researcher/            ❌
│   ├── meeting-prep-agent/           ❌
│   ├── model-builder/                ❌
│   ├── month-end-closer/             ❌
│   ├── pitch-agent/                  ❌
│   ├── statement-auditor/            ❌
│   └── valuation-reviewer/           ❌
│
├── partner-built/                    ❌ 中文版May06缺失 (2个插件)
│   ├── lseg/                         ❌
│   └── spglobal/                     ❌
│
└── vertical-plugins/                 ⚠️ 部分缺失
    ├── equity-research/             ❌ 全部缺失 (31文件)
    ├── financial-analysis/          ❌ 缺失38个文件
    ├── fund-admin/                  ❌ 全部缺失 (7文件)
    ├── investment-banking/          ❌ 缺失24个文件
    ├── operations/                  ❌ 全部缺失 (1文件)
    ├── private-equity/              ❌ 缺失23个文件
    └── wealth-management/           ❌ 缺失14个文件
```

---

> 📝 **备注**：此checklist基于2026-05-09的目录对比。
> - plugins目录：275个文件
> - 中文版May06目录：216个文件
> - 缺失文件：256个（plugins有但中文版May06缺失）
