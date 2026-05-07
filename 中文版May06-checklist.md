# 中文版翻译 Checklist

> 对比日期：2026-05-07
> 源目录：`plugins/`
> 目标目录：`中文版May06/`

---

## 📊 统计摘要

| 类别 | 总数 (plugins) | 已翻译 (中文版May06) | 缺失 |
|------|----------------|---------------------|------|
| **agent-plugins** | 10个插件 | 0 | ❌ **全部缺失** |
| **partner-built** | 2个插件 | 0 | ❌ **全部缺失** |
| **vertical-plugins** | 6个模块 | 部分 | ⚠️ 部分缺失 |
| **总计** | 约280+文件 | 约50个文件 | ❌ 约230+文件缺失 |

---

## ❌ 【严重】完全缺失的插件（整目录缺失）

### agent-plugins (10个插件全部缺失)

| # | 插件名称 | 描述 | 缺失文件数 |
|---|----------|------|------------|
| 1 | **earnings-reviewer** | 财报审核代理 | 11个文件 |
| 2 | **gl-reconciler** | 总账对账代理 | 6个文件 |
| 3 | **kyc-screener** | KYC筛查代理 | 5个文件 |
| 4 | **market-researcher** | 市场研究代理 | 8个文件 |
| 5 | **meeting-prep-agent** | 会议准备代理 | 5个文件 |
| 6 | **model-builder** | 模型构建代理 | 14个文件 |
| 7 | **month-end-closer** | 月末结账代理 | 6个文件 |
| 8 | **pitch-agent** | 推介材料代理 | 25个文件 |
| 9 | **statement-auditor** | 报表审计代理 | 4个文件 |
| 10 | **valuation-reviewer** | 估值审核代理 | 5个文件 |

### partner-built (2个插件全部缺失)

| # | 插件名称 | 描述 | 缺失文件数 |
|---|----------|------|------------|
| 1 | **lseg** | LSEG 合作伙伴插件 | 约10+文件 |
| 2 | **spglobal** | S&P Global 合作伙伴插件 | 15个文件 |

---

## ⚠️ 【高优先级】vertical-plugins 缺失内容

### equity-research（股权研究）- 全部缺失

| # | 文件路径 | 状态 |
|---|----------|------|
| 1 | `.claude-plugin/plugin.json` | ❌ 缺失 |
| 2 | `commands/catalysts.md` | ❌ 缺失 |
| 3 | `commands/earnings-preview.md` | ❌ 缺失 |
| 4 | `commands/earnings.md` | ❌ 缺失 |
| 5 | `commands/initiate.md` | ❌ 缺失 |
| 6 | `commands/model-update.md` | ❌ 缺失 |
| 7 | `commands/morning-note.md` | ❌ 缺失 |
| 8 | `commands/screen.md` | ❌ 缺失 |
| 9 | `commands/sector.md` | ❌ 缺失 |
| 10 | `commands/thesis.md` | ❌ 缺失 |
| 11 | `hooks/hooks.json` | ❌ 缺失 |
| 12 | `skills/catalyst-calendar/SKILL.md` | ❌ 缺失 |
| 13 | `skills/earnings-analysis/SKILL.md` | ❌ 缺失 |
| 14 | `skills/earnings-analysis/references/best-practices.md` | ❌ 缺失 |
| 15 | `skills/earnings-analysis/references/report-structure.md` | ❌ 缺失 |
| 16 | `skills/earnings-analysis/references/workflow.md` | ❌ 缺失 |
| 17 | `skills/earnings-preview/SKILL.md` | ❌ 缺失 |
| 18 | `skills/idea-generation/SKILL.md` | ❌ 缺失 |
| 19 | `skills/initiating-coverage/SKILL.md` | ❌ 缺失 |
| 20 | `skills/initiating-coverage/assets/quality-checklist.md` | ❌ 缺失 |
| 21 | `skills/initiating-coverage/assets/report-template.md` | ❌ 缺失 |
| 22 | `skills/initiating-coverage/references/task1-company-research.md` | ❌ 缺失 |
| 23 | `skills/initiating-coverage/references/task2-financial-modeling.md` | ❌ 缺失 |
| 24 | `skills/initiating-coverage/references/task3-valuation.md` | ❌ 缺失 |
| 25 | `skills/initiating-coverage/references/task4-chart-generation.md` | ❌ 缺失 |
| 26 | `skills/initiating-coverage/references/task5-report-assembly.md` | ❌ 缺失 |
| 27 | `skills/initiating-coverage/references/valuation-methodologies.md` | ❌ 缺失 |
| 28 | `skills/model-update/SKILL.md` | ❌ 缺失 |
| 29 | `skills/morning-note/SKILL.md` | ❌ 缺失 |
| 30 | `skills/sector-overview/SKILL.md` | ❌ 缺失 |
| 31 | `skills/thesis-tracker/SKILL.md` | ❌ 缺失 |

### financial-analysis（财务分析）- 部分缺失

**已存在的文件：**
- [x] `commands/lbo.md`
- [x] `commands/ppt-template.md`
- [x] `skills/3-statement-model/SKILL.md`
- [x] `skills/3-statement-model/references/formatting.md`
- [x] `skills/3-statement-model/references/formulas.md`
- [x] `skills/3-statement-model/references/sec-filings.md`
- [x] `skills/audit-xls/SKILL.md`
- [x] `skills/clean-data-xls/SKILL.md`
- [x] `skills/competitive-analysis/SKILL.md`
- [x] `skills/comps-analysis/SKILL.md`
- [x] `skills/dcf-model/SKILL.md`
- [x] `skills/dcf-model/TROUBLESHOOTING.md`
- [x] `skills/deck-refresh/SKILL.md`
- [x] `skills/ib-check-deck/SKILL.md`
- [x] `skills/ib-check-deck/references/ib-terminology.md`
- [x] `skills/ib-check-deck/references/report-format.md`
- [x] `skills/pptx-author/SKILL.md`
- [x] `skills/skill-creator/SKILL.md`
- [x] `skills/skill-creator/references/output-patterns.md`
- [x] `skills/skill-creator/references/workflows.md`
- [x] `skills/xlsx-author/SKILL.md`

**缺失的文件：**

| # | 文件路径 | 状态 |
|---|----------|------|
| 1 | `.claude-plugin/plugin.json` | ❌ 缺失 |
| 2 | `.mcp.json` | ❌ 缺失 |
| 3 | `commands/3-statement-model.md` | ❌ 缺失 |
| 4 | `commands/competitive-analysis.md` | ❌ 缺失 |
| 5 | `commands/comps.md` | ❌ 缺失 |
| 6 | `commands/dcf.md` | ❌ 缺失 |
| 7 | `commands/debug-model.md` | ❌ 缺失 |
| 8 | `hooks/hooks.json` | ❌ 缺失 |
| 9 | `skills/competitive-analysis/references/frameworks.md` | ❌ 缺失 |
| 10 | `skills/competitive-analysis/references/schemas.md` | ❌ 缺失 |
| 11 | `skills/dcf-model/requirements.txt` | ❌ 缺失 |
| 12 | `skills/dcf-model/scripts/validate_dcf.py` | ❌ 缺失 |
| 13 | `skills/ib-check-deck/scripts/extract_numbers.py` | ❌ 缺失 |
| 14 | `skills/skill-creator/LICENSE.txt` | ❌ 缺失 |
| 15 | `skills/skill-creator/scripts/init_skill.py` | ❌ 缺失 |
| 16 | `skills/skill-creator/scripts/package_skill.py` | ❌ 缺失 |
| 17 | `skills/skill-creator/scripts/quick_validate.py` | ❌ 缺失 |

### fund-admin（基金管理）- 全部缺失

| # | 文件路径 | 状态 |
|---|----------|------|
| 1 | `.claude-plugin/plugin.json` | ❌ 缺失 |
| 2 | `skills/accrual-schedule/SKILL.md` | ❌ 缺失 |
| 3 | `skills/break-trace/SKILL.md` | ❌ 缺失 |
| 4 | `skills/gl-recon/SKILL.md` | ❌ 缺失 |
| 5 | `skills/nav-tieout/SKILL.md` | ❌ 缺失 |
| 6 | `skills/roll-forward/SKILL.md` | ❌ 缺失 |
| 7 | `skills/variance-commentary/SKILL.md` | ❌ 缺失 |

### investment-banking（投资银行）- 部分缺失

**已存在的文件：**
- [x] `commands/buyer-list.md`
- [x] `commands/cim.md`
- [x] `commands/deal-tracker.md`
- [x] `commands/merger-model.md`
- [x] `commands/one-pager.md`
- [x] `commands/process-letter.md`
- [x] `commands/teaser.md`
- [x] `skills/datapack-builder/SKILL.md`
- [x] `skills/pitch-deck/SKILL.md`
- [x] `skills/process-letter/SKILL.md`
- [x] `skills/strip-profile/SKILL.md`

**缺失的文件：**

| # | 文件路径 | 状态 |
|---|----------|------|
| 1 | `.claude-plugin/plugin.json` | ❌ 缺失 |
| 2 | `.claude/investment-banking.local.md.example` | ❌ 缺失 |
| 3 | `.gitignore` | ❌ 缺失 |
| 4 | `.mcp.json` | ❌ 缺失 |
| 5 | `README.md` | ❌ 缺失 |
| 6 | `hooks/hooks.json` | ❌ 缺失 |
| 7 | `skills/deal-tracker/SKILL.md` | ❌ 缺失 |
| 8 | `skills/merger-model/SKILL.md` | ❌ 缺失 |
| 9 | `skills/pitch-deck/reference/calculation-standards.md` | ❌ 缺失 |
| 10 | `skills/pitch-deck/reference/formatting-standards.md` | ❌ 缺失 |
| 11 | `skills/pitch-deck/reference/slide-templates.md` | ❌ 缺失 |
| 12 | `skills/pitch-deck/reference/xml-reference.md` | ❌ 缺失 |
| 13 | `skills/teaser/SKILL.md` | ❌ 缺失 |

### operations（运营）- 全部缺失

| # | 文件路径 | 状态 |
|---|----------|------|
| 1 | `.claude-plugin/plugin.json` | ❌ 缺失 |

### private-equity（私募股权）- 部分缺失

**已存在的文件：**
- [x] `commands/ai-readiness.md`
- [x] `commands/dd-checklist.md`
- [x] `commands/dd-prep.md`
- [x] `commands/portfolio.md`
- [x] `commands/returns.md`
- [x] `commands/screen-deal.md`
- [x] `commands/source.md`
- [x] `commands/unit-economics.md`
- [x] `commands/value-creation.md`
- [x] `skills/deal-sourcing/SKILL.md`
- [x] `skills/returns-analysis/SKILL.md`

**缺失的文件：**

| # | 文件路径 | 状态 |
|---|----------|------|
| 1 | `.claude-plugin/plugin.json` | ❌ 缺失 |
| 2 | `.mcp.json` | ❌ 缺失 |
| 3 | `commands/ic-memo.md` | ❌ 缺失 |
| 4 | `hooks/hooks.json` | ❌ 缺失 |
| 5 | `skills/ai-readiness/SKILL.md` | ❌ 缺失 |
| 6 | `skills/dd-checklist/SKILL.md` | ❌ 缺失 |
| 7 | `skills/dd-meeting-prep/SKILL.md` | ❌ 缺失 |
| 8 | `skills/deal-screening/SKILL.md` | ❌ 缺失 |
| 9 | `skills/ic-memo/SKILL.md` | ❌ 缺失 |
| 10 | `skills/portfolio-monitoring/SKILL.md` | ❌ 缺失 |
| 11 | `skills/unit-economics/SKILL.md` | ❌ 缺失 |
| 12 | `skills/value-creation-plan/SKILL.md` | ❌ 缺失 |

### wealth-management（财富管理）- 部分缺失

**已存在的文件：**
- [x] `commands/client-report.md`
- [x] `commands/client-review.md`
- [x] `commands/financial-plan.md`
- [x] `commands/proposal.md`
- [x] `commands/rebalance.md`
- [x] `commands/tlh.md`
- [x] `skills/client-report/SKILL.md`
- [x] `skills/client-review/SKILL.md`
- [x] `skills/financial-plan/SKILL.md`
- [x] `skills/portfolio-rebalance/SKILL.md`
- [x] `skills/tax-loss-harvesting/SKILL.md`

**缺失的文件：**

| # | 文件路径 | 状态 |
|---|----------|------|
| 1 | `.claude-plugin/plugin.json` | ❌ 缺失 |
| 2 | `hooks/hooks.json` | ❌ 缺失 |
| 3 | `skills/investment-proposal/SKILL.md` | ❌ 缺失 |

---

## 🎯 翻译优先级排序

### P0 - 紧急（立即处理）
1. **agent-plugins** - 10个完整插件全部缺失（约90+文件）
2. **partner-built** - 2个合作伙伴插件全部缺失（约25+文件）
3. **vertical-plugins/equity-research** - 全部31个文件缺失

### P1 - 高优先级
4. **vertical-plugins/fund-admin** - 全部7个文件缺失
5. **vertical-plugins/operations** - 全部缺失
6. **vertical-plugins/investment-banking** - 缺失13个文件（含pitch-deck参考文件）
7. **vertical-plugins/private-equity** - 缺失12个文件（含IC备忘录）

### P2 - 中优先级
8. **vertical-plugins/financial-analysis** - 缺失17个文件（主要是scripts和配置）
9. **vertical-plugins/wealth-management** - 缺失3个文件

---

## ✅ 翻译完成追踪

### agent-plugins
- [ ] earnings-reviewer (11文件)
- [ ] gl-reconciler (6文件)
- [ ] kyc-screener (5文件)
- [ ] market-researcher (8文件)
- [ ] meeting-prep-agent (5文件)
- [ ] model-builder (14文件)
- [ ] month-end-closer (6文件)
- [ ] pitch-agent (25文件)
- [ ] statement-auditor (4文件)
- [ ] valuation-reviewer (5文件)

### partner-built
- [ ] lseg
- [ ] spglobal

### vertical-plugins
- [ ] equity-research (31文件)
- [ ] financial-analysis (17文件)
- [ ] fund-admin (7文件)
- [ ] investment-banking (13文件)
- [ ] operations
- [ ] private-equity (12文件)
- [ ] wealth-management (3文件)

---

## 📁 目录结构对比

```
plugins/
├── agent-plugins/                    ❌ 中文版May06缺失
│   ├── earnings-reviewer/
│   ├── gl-reconciler/
│   ├── kyc-screener/
│   ├── market-researcher/
│   ├── meeting-prep-agent/
│   ├── model-builder/
│   ├── month-end-closer/
│   ├── pitch-agent/
│   ├── statement-auditor/
│   └── valuation-reviewer/
├── partner-built/                    ❌ 中文版May06缺失
│   ├── lseg/
│   └── spglobal/
└── vertical-plugins/                 ⚠️ 部分缺失
    ├── equity-research/             ❌ 全部缺失
    ├── financial-analysis/           ✅ 部分存在
    ├── fund-admin/                  ❌ 全部缺失
    ├── investment-banking/          ✅ 部分存在
    ├── operations/                  ❌ 全部缺失
    ├── private-equity/              ✅ 部分存在
    └── wealth-management/           ✅ 部分存在
```

---

> 📝 **备注**：此checklist基于2026-05-07的目录对比。建议定期重新运行对比以更新状态。
