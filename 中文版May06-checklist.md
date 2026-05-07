# 中文版翻译 Checklist

> 对比日期：2026-05-07
> 源目录：`plugins/`
> 目标目录：`中文版May06/`
> 缺失文件总数：**268个**

---

## 📊 统计摘要

| 类别 | 插件/模块数 | 总文件数 | 已翻译 | 缺失 |
|------|-------------|----------|--------|------|
| **agent-plugins** | 10个 | ~90 | 0 | ❌ **全部缺失** |
| **partner-built** | 2个 | ~35 | 0 | ❌ **全部缺失** |
| **vertical-plugins** | 6个 | ~150 | ~50 | ⚠️ ~100缺失 |
| **总计** | 18个 | ~275 | ~50 | ❌ **268个缺失** |

---

## ❌ 【紧急】整目录缺失 - agent-plugins (10个插件)

| # | 插件名称 | 描述 | 缺失文件数 |
|---|----------|------|------------|
| 1 | **earnings-reviewer** | 财报审核代理 | 11 |
| 2 | **gl-reconciler** | 总账对账代理 | 6 |
| 3 | **kyc-screener** | KYC筛查代理 | 5 |
| 4 | **market-researcher** | 市场研究代理 | 8 |
| 5 | **meeting-prep-agent** | 会议准备代理 | 5 |
| 6 | **model-builder** | 模型构建代理 | 14 |
| 7 | **month-end-closer** | 月末结账代理 | 6 |
| 8 | **pitch-agent** | 推介材料代理 | 25 |
| 9 | **statement-auditor** | 报表审计代理 | 4 |
| 10 | **valuation-reviewer** | 估值审核代理 | 5 |

---

## ❌ 【紧急】整目录缺失 - partner-built (2个插件)

| # | 插件名称 | 描述 | 缺失文件数 |
|---|----------|------|------------|
| 1 | **lseg** | LSEG合作伙伴插件 | ~10+ |
| 2 | **spglobal** | S&P Global合作伙伴插件 | 15 |

---

## ⚠️ 【高优先级】vertical-plugins 缺失内容

### 1. equity-research（股权研究）- 全部31个文件缺失

| 文件路径 | 类型 |
|----------|------|
| `.claude-plugin/plugin.json` | 配置 |
| `commands/catalysts.md` | 命令 |
| `commands/earnings-preview.md` | 命令 |
| `commands/earnings.md` | 命令 |
| `commands/initiate.md` | 命令 |
| `commands/model-update.md` | 命令 |
| `commands/morning-note.md` | 命令 |
| `commands/screen.md` | 命令 |
| `commands/sector.md` | 命令 |
| `commands/thesis.md` | 命令 |
| `hooks/hooks.json` | 配置 |
| `skills/catalyst-calendar/SKILL.md` | 技能 |
| `skills/earnings-analysis/SKILL.md` | 技能 |
| `skills/earnings-analysis/references/best-practices.md` | 参考 |
| `skills/earnings-analysis/references/report-structure.md` | 参考 |
| `skills/earnings-analysis/references/workflow.md` | 参考 |
| `skills/earnings-preview/SKILL.md` | 技能 |
| `skills/idea-generation/SKILL.md` | 技能 |
| `skills/initiating-coverage/SKILL.md` | 技能 |
| `skills/initiating-coverage/assets/quality-checklist.md` | 资源 |
| `skills/initiating-coverage/assets/report-template.md` | 资源 |
| `skills/initiating-coverage/references/task1-company-research.md` | 参考 |
| `skills/initiating-coverage/references/task2-financial-modeling.md` | 参考 |
| `skills/initiating-coverage/references/task3-valuation.md` | 参考 |
| `skills/initiating-coverage/references/task4-chart-generation.md` | 参考 |
| `skills/initiating-coverage/references/task5-report-assembly.md` | 参考 |
| `skills/initiating-coverage/references/valuation-methodologies.md` | 参考 |
| `skills/model-update/SKILL.md` | 技能 |
| `skills/morning-note/SKILL.md` | 技能 |
| `skills/sector-overview/SKILL.md` | 技能 |
| `skills/thesis-tracker/SKILL.md` | 技能 |

---

### 2. fund-admin（基金管理）- 全部7个文件缺失

| 文件路径 | 类型 |
|----------|------|
| `.claude-plugin/plugin.json` | 配置 |
| `skills/accrual-schedule/SKILL.md` | 技能 |
| `skills/break-trace/SKILL.md` | 技能 |
| `skills/gl-recon/SKILL.md` | 技能 |
| `skills/nav-tieout/SKILL.md` | 技能 |
| `skills/roll-forward/SKILL.md` | 技能 |
| `skills/variance-commentary/SKILL.md` | 技能 |

---

### 3. operations（运营）- 全部缺失

| 文件路径 | 类型 |
|----------|------|
| `.claude-plugin/plugin.json` | 配置 |

---

### 4. investment-banking（投资银行）- 缺失13个文件

**已存在（无需翻译）：**
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

**缺失文件：**

| 文件路径 | 类型 |
|----------|------|
| `.claude-plugin/plugin.json` | 配置 |
| `.claude/investment-banking.local.md.example` | 配置 |
| `.gitignore` | 配置 |
| `.mcp.json` | 配置 |
| `README.md` | 文档 |
| `hooks/hooks.json` | 配置 |
| `skills/deal-tracker/SKILL.md` | 技能 |
| `skills/merger-model/SKILL.md` | 技能 |
| `skills/pitch-deck/reference/calculation-standards.md` | 参考 |
| `skills/pitch-deck/reference/formatting-standards.md` | 参考 |
| `skills/pitch-deck/reference/slide-templates.md` | 参考 |
| `skills/pitch-deck/reference/xml-reference.md` | 参考 |
| `skills/teaser/SKILL.md` | 技能 |

---

### 5. private-equity（私募股权）- 缺失12个文件

**已存在（无需翻译）：**
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

**缺失文件：**

| 文件路径 | 类型 |
|----------|------|
| `.claude-plugin/plugin.json` | 配置 |
| `.mcp.json` | 配置 |
| `commands/ic-memo.md` | 命令 |
| `hooks/hooks.json` | 配置 |
| `skills/ai-readiness/SKILL.md` | 技能 |
| `skills/dd-checklist/SKILL.md` | 技能 |
| `skills/dd-meeting-prep/SKILL.md` | 技能 |
| `skills/deal-screening/SKILL.md` | 技能 |
| `skills/ic-memo/SKILL.md` | 技能 |
| `skills/portfolio-monitoring/SKILL.md` | 技能 |
| `skills/unit-economics/SKILL.md` | 技能 |
| `skills/value-creation-plan/SKILL.md` | 技能 |

---

### 6. financial-analysis（财务分析）- 缺失17个文件

**已存在（无需翻译）：**
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

**缺失文件：**

| 文件路径 | 类型 |
|----------|------|
| `.claude-plugin/plugin.json` | 配置 |
| `.mcp.json` | 配置 |
| `commands/3-statement-model.md` | 命令 |
| `commands/competitive-analysis.md` | 命令 |
| `commands/comps.md` | 命令 |
| `commands/dcf.md` | 命令 |
| `commands/debug-model.md` | 命令 |
| `hooks/hooks.json` | 配置 |
| `skills/competitive-analysis/references/frameworks.md` | 参考 |
| `skills/competitive-analysis/references/schemas.md` | 参考 |
| `skills/dcf-model/requirements.txt` | 配置 |
| `skills/dcf-model/scripts/validate_dcf.py` | 脚本 |
| `skills/ib-check-deck/scripts/extract_numbers.py` | 脚本 |
| `skills/skill-creator/LICENSE.txt` | 配置 |
| `skills/skill-creator/scripts/init_skill.py` | 脚本 |
| `skills/skill-creator/scripts/package_skill.py` | 脚本 |
| `skills/skill-creator/scripts/quick_validate.py` | 脚本 |

---

### 7. wealth-management（财富管理）- 缺失3个文件

**已存在（无需翻译）：**
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

**缺失文件：**

| 文件路径 | 类型 |
|----------|------|
| `.claude-plugin/plugin.json` | 配置 |
| `hooks/hooks.json` | 配置 |
| `skills/investment-proposal/SKILL.md` | 技能 |

---

## 🎯 翻译优先级排序

### P0 - 紧急（立即处理）
1. **agent-plugins** - 10个完整插件（约90个文件）
2. **partner-built** - 2个合作伙伴插件（约35个文件）
3. **vertical-plugins/equity-research** - 全部31个文件

### P1 - 高优先级
4. **vertical-plugins/fund-admin** - 7个文件
5. **vertical-plugins/operations** - 配置文件
6. **vertical-plugins/investment-banking** - 13个文件
7. **vertical-plugins/private-equity** - 12个文件

### P2 - 中优先级
8. **vertical-plugins/financial-analysis** - 17个文件（主要是脚本）
9. **vertical-plugins/wealth-management** - 3个文件

---

## ✅ 翻译进度追踪

| 模块 | 文件数 | 进度 |
|------|--------|------|
| agent-plugins/earnings-reviewer | 11 | [ ] 0% |
| agent-plugins/gl-reconciler | 6 | [ ] 0% |
| agent-plugins/kyc-screener | 5 | [ ] 0% |
| agent-plugins/market-researcher | 8 | [ ] 0% |
| agent-plugins/meeting-prep-agent | 5 | [ ] 0% |
| agent-plugins/model-builder | 14 | [ ] 0% |
| agent-plugins/month-end-closer | 6 | [ ] 0% |
| agent-plugins/pitch-agent | 25 | [ ] 0% |
| agent-plugins/statement-auditor | 4 | [ ] 0% |
| agent-plugins/valuation-reviewer | 5 | [ ] 0% |
| partner-built/lseg | ~10 | [ ] 0% |
| partner-built/spglobal | 15 | [ ] 0% |
| vertical-plugins/equity-research | 31 | [ ] 0% |
| vertical-plugins/fund-admin | 7 | [ ] 0% |
| vertical-plugins/operations | 1 | [ ] 0% |
| vertical-plugins/investment-banking | 13 | [ ] 0% |
| vertical-plugins/private-equity | 12 | [ ] 0% |
| vertical-plugins/financial-analysis | 17 | [ ] 0% |
| vertical-plugins/wealth-management | 3 | [ ] 0% |

---

> 📝 **备注**：此checklist基于2026-05-07的目录对比，共发现**268个缺失文件**。
