# 中文版May06 翻译 Checklist

> 生成日期：2026-05-11
> 源目录：`plugins/` (最新sync后的完整文件)
> 目标目录：`中文版May06/`
> Git Sync：最新从upstream/main合并的claude-for-msft-365-install目录

---

## 🚨 Git Sync 新增文件（需要关注）

本次从 `upstream/main` 合并的 **6个文件**（位于 `claude-for-msft-365-install/` 目录）：

| 文件路径 | 状态 | 备注 |
|----------|------|------|
| `claude-for-msft-365-install/.claude-plugin/plugin.json` | 🆕 新文件 | 插件配置 |
| `claude-for-msft-365-install/commands/bootstrap.md` | 🆕 新文件 | 引导命令 |
| `claude-for-msft-365-install/commands/consent.md` | 🆕 新文件 | 同意命令 |
| `claude-for-msft-365-install/commands/manifest.md` | 🆕 新文件 | 清单命令 |
| `claude-for-msft-365-install/commands/setup.md` | 🆕 新文件 | 设置命令 |
| `claude-for-msft-365-install/scripts/build-manifest.mjs` | 🆕 新文件 | 构建脚本 |

> ⚠️ **注意**：这些文件位于 `plugins/` 目录外，如需翻译请单独处理。

---

## 📊 统计摘要

| 类别 | plugins文件数 | 中文版May06文件数 | 缺失数 | 完成率 |
|------|-------------|-----------------|--------|--------|
| **agent-plugins** | ~100 | ~90 | ~10 | 90% |
| **partner-built** | 31 | 31 | 0 | 100% |
| **vertical-plugins** | ~160 | ~140 | ~20 | 88% |
| **总计** | **~290** | **~260** | **~30** | **~90%** |

---

## ❌ 缺失文件清单

### agent-plugins 缺失文件

| # | 插件 | 缺失文件路径 | 优先级 |
|---|------|-------------|--------|
| 1 | pitch-agent | `skills/pitch-deck/reference/slide-templates.md` | 🔴 高 |
| 2 | pitch-agent | `skills/pitch-deck/reference/xml-reference.md` | 🔴 高 |
| 3 | pitch-agent | `skills/pitch-deck/reference/calculation-standards.md` | 🔴 高 |
| 4 | pitch-agent | `skills/pitch-deck/reference/formatting-standards.md` | 🔴 高 |
| 5 | pitch-agent | `skills/lbo-model/SKILL.md` | 🔴 高 |
| 6 | pitch-agent | `skills/comps-analysis/SKILL.md` | 🟡 中 |
| 7 | pitch-agent | `skills/3-statement-model/SKILL.md` | 🔴 高 |
| 8 | pitch-agent | `skills/3-statement-model/references/formatting.md` | 🟡 中 |
| 9 | pitch-agent | `skills/3-statement-model/references/formulas.md` | 🟡 中 |
| 10 | pitch-agent | `skills/3-statement-model/references/sec-filings.md` | 🟡 中 |
| 11 | pitch-agent | `skills/dcf-model/SKILL.md` | 🔴 高 |
| 12 | pitch-agent | `skills/dcf-model/scripts/validate_dcf.py` | 🔴 高 |
| 13 | pitch-agent | `skills/dcf-model/TROUBLESHOOTING.md` | 🟡 中 |
| 14 | pitch-agent | `skills/dcf-model/requirements.txt` | 🟡 中 |
| 15 | pitch-agent | `skills/deck-refresh/SKILL.md` | 🟡 中 |
| 16 | pitch-agent | `skills/audit-xls/SKILL.md` | 🟡 中 |
| 17 | pitch-agent | `skills/ib-check-deck/scripts/extract_numbers.py` | 🟡 中 |
| 18 | pitch-agent | `skills/ib-check-deck/references/ib-terminology.md` | 🟡 中 |
| 19 | pitch-agent | `skills/ib-check-deck/references/report-format.md` | 🟡 中 |
| 20 | statement-auditor | `skills/audit-xls/SKILL.md` | 🟡 中 |
| 21 | statement-auditor | `skills/xlsx-author/SKILL.md` | 🔴 高 |
| 22 | model-builder | `skills/dcf-model/scripts/validate_dcf.py` | 🔴 高 |
| 23 | model-builder | `skills/dcf-model/TROUBLESHOOTING.md` | 🟡 中 |
| 24 | model-builder | `skills/dcf-model/requirements.txt` | 🟡 中 |
| 25 | model-builder | `skills/lbo-model/SKILL.md` | 🔴 高 |
| 26 | model-builder | `skills/comps-analysis/SKILL.md` | 🟡 中 |
| 27 | model-builder | `skills/3-statement-model/references/formatting.md` | 🟡 中 |
| 28 | model-builder | `skills/3-statement-model/references/formulas.md` | 🟡 中 |
| 29 | model-builder | `skills/3-statement-model/references/sec-filings.md` | 🟡 中 |
| 30 | meeting-prep-agent | `skills/pptx-author/SKILL.md` | 🔴 高 |
| 31 | month-end-closer | `skills/xlsx-author/SKILL.md` | 🔴 高 |
| 32 | gl-reconciler | `agents/gl-reconciler.md` | 🔴 高 |

### partner-built 缺失文件

| # | 插件 | 缺失文件路径 | 优先级 |
|---|------|-------------|--------|
| 1 | spglobal | `skills/tear-sheet/SKILL.md` | 🔴 高 |
| 2 | spglobal | `skills/tear-sheet/LICENSE` | 🟢 低 |
| 3 | spglobal | `skills/earnings-preview-beta/SKILL.md` | 🔴 高 |
| 4 | spglobal | `skills/earnings-preview-beta/report-template.md` | 🟡 中 |
| 5 | spglobal | `skills/earnings-preview-beta/LICENSE` | 🟢 低 |
| 6 | lseg | `skills/bond-relative-value/SKILL.md` | 🔴 高 |

### vertical-plugins 缺失文件

| # | 模块 | 缺失文件路径 | 优先级 |
|---|------|-------------|--------|
| 1 | investment-banking | `.claude-plugin/plugin.json` | 🔴 高 |
| 2 | investment-banking | `skills/strip-profile/SKILL.md` | 🟡 中 |
| 3 | investment-banking | `skills/process-letter/SKILL.md` | 🔴 高 |
| 4 | investment-banking | `skills/datapack-builder/SKILL.md` | 🟡 中 |
| 5 | investment-banking | `skills/pitch-deck/SKILL.md` | 🔴 高 |
| 6 | investment-banking | `.mcp.json` | 🟡 中 |
| 7 | investment-banking | `hooks/hooks.json` | 🟡 中 |
| 8 | investment-banking | `.claude/investment-banking.local.md.example` | 🟢 低 |
| 9 | investment-banking | `.gitignore` | 🟢 低 |
| 10 | financial-analysis | `skills/pptx-author/SKILL.md` | 🔴 高 |
| 11 | financial-analysis | `skills/lbo-model/SKILL.md` | 🔴 高 |
| 12 | financial-analysis | `skills/skill-creator/scripts/quick_validate.py` | 🟡 中 |
| 13 | financial-analysis | `skills/skill-creator/scripts/package_skill.py` | 🟡 中 |
| 14 | financial-analysis | `skills/skill-creator/scripts/init_skill.py` | 🟡 中 |
| 15 | financial-analysis | `skills/skill-creator/LICENSE.txt` | 🟢 低 |
| 16 | financial-analysis | `skills/dcf-model/scripts/validate_dcf.py` | 🔴 高 |
| 17 | financial-analysis | `skills/dcf-model/TROUBLESHOOTING.md` | 🟡 中 |
| 18 | financial-analysis | `skills/dcf-model/requirements.txt` | 🟡 中 |
| 19 | financial-analysis | `skills/ib-check-deck/SKILL.md` | 🔴 高 |
| 20 | financial-analysis | `skills/ib-check-deck/scripts/extract_numbers.py` | 🟡 中 |
| 21 | financial-analysis | `skills/ib-check-deck/references/ib-terminology.md` | 🟡 中 |
| 22 | financial-analysis | `skills/ib-check-deck/references/report-format.md` | 🟡 中 |
| 23 | fund-admin | `.claude-plugin/plugin.json` | 🔴 高 |
| 24 | operations | `.claude-plugin/plugin.json` | 🔴 高 |
| 25 | private-equity | `.claude-plugin/plugin.json` | 🔴 高 |
| 26 | private-equity | `.mcp.json` | 🟡 中 |
| 27 | private-equity | `hooks/hooks.json` | 🟡 中 |
| 28 | wealth-management | `.claude-plugin/plugin.json` | 🔴 高 |
| 29 | wealth-management | `hooks/hooks.json` | 🟡 中 |
| 30 | equity-research | `skills/initiating-coverage/references/task1-company-research.md` | 🔴 高 |
| 31 | equity-research | `skills/initiating-coverage/references/task2-financial-modeling.md` | 🔴 高 |
| 32 | equity-research | `skills/initiating-coverage/references/task3-valuation.md` | 🔴 高 |
| 33 | equity-research | `skills/initiating-coverage/references/task4-chart-generation.md` | 🔴 高 |
| 34 | equity-research | `skills/initiating-coverage/references/task5-report-assembly.md` | 🔴 高 |
| 35 | equity-research | `skills/initiating-coverage/references/valuation-methodologies.md` | 🔴 高 |

---

## ✅ 已完成翻译

### agent-plugins (10个插件)

| 插件 | 状态 | 已翻译文件数 |
|------|------|------------|
| earnings-reviewer | ✅ 已完成 | 11 |
| gl-reconciler | ✅ 已完成 | 6 |
| kyc-screener | ✅ 已完成 | 6 |
| market-researcher | ✅ 已完成 | 8 |
| meeting-prep-agent | ✅ 已完成 | 5 |
| model-builder | ⚠️ 部分完成 | ~10 |
| month-end-closer | ⚠️ 部分完成 | ~5 |
| pitch-agent | ⚠️ 部分完成 | ~8 |
| statement-auditor | ⚠️ 部分完成 | ~3 |
| valuation-reviewer | ✅ 已完成 | 5 |

### partner-built (2个插件)

| 插件 | 状态 | 已翻译文件数 |
|------|------|------------|
| lseg | ✅ 已完成 | 16 |
| spglobal | ⚠️ 部分完成 | ~12 |

### vertical-plugins (7个模块)

| 模块 | 状态 | 已翻译文件数 |
|------|------|------------|
| equity-research | ✅ 已完成 | 31 |
| financial-analysis | ⚠️ 部分完成 | ~25 |
| fund-admin | ✅ 已完成 | 7 |
| investment-banking | ⚠️ 部分完成 | ~18 |
| operations | ✅ 已完成 | 3 |
| private-equity | ✅ 已完成 | 23 |
| wealth-management | ✅ 已完成 | 14 |

---

## 📁 目录结构对比图

```
plugins/
├── agent-plugins/                    ⚠️ 部分缺失 (~10文件)
│   ├── earnings-reviewer/            ✅
│   ├── gl-reconciler/               ⚠️ 缺agents/gl-reconciler.md
│   ├── kyc-screener/                ✅
│   ├── market-researcher/            ✅
│   ├── meeting-prep-agent/           ⚠️ 缺skills/pptx-author/
│   ├── model-builder/               ⚠️ 缺多个skills文件
│   ├── month-end-closer/             ⚠️ 缺skills/xlsx-author/
│   ├── pitch-agent/                  ⚠️ 缺多个skills文件 (~20)
│   ├── statement-auditor/            ⚠️ 缺skills/audit-xls/, skills/xlsx-author/
│   └── valuation-reviewer/           ✅
│
├── partner-built/                    ⚠️ 部分缺失 (~6文件)
│   ├── lseg/                         ⚠️ 缺skills/bond-relative-value/
│   └── spglobal/                     ⚠️ 缺skills/tear-sheet/, skills/earnings-preview-beta/
│
└── vertical-plugins/                 ⚠️ 部分缺失 (~35文件)
    ├── equity-research/              ⚠️ 缺initiating-coverage/references/ (6文件)
    ├── financial-analysis/          ⚠️ 缺多个skills文件 (~15)
    ├── fund-admin/                  ✅
    ├── investment-banking/          ⚠️ 缺多个文件 (~10)
    ├── operations/                  ✅
    ├── private-equity/              ⚠️ 缺配置文件 (~3)
    └── wealth-management/          ⚠️ 缺配置文件 (~2)

claude-for-msft-365-install/          🆕 新增（Git Sync）
└── (6个新文件待处理)
```

---

## 🎯 翻译优先级

### � 高优先级（必须翻译）
1. 所有 `.claude-plugin/plugin.json` 配置文件
2. 所有 `SKILL.md` 核心技能文件
3. 所有 `agents/*.md` 代理定义文件
4. 所有 `commands/*.md` 命令文件
5. 所有 `references/*.md` 参考文档

### 🟡 中优先级（建议翻译）
1. `scripts/*.py` Python脚本文件
2. `TROUBLESHOOTING.md` 故障排除文档
3. `requirements.txt` 依赖文件

### 🟢 低优先级（可选）
1. `LICENSE*` 许可证文件
2. `.gitignore` 文件
3. `.example` 示例文件

---

## 📝 翻译要求

1. **信达雅**：翻译要忠实原文，表达清晰，文笔优美
2. **金融术语**：针对金融新手，每篇文章末尾添加详细的金融术语和知识解释
3. **格式保持**：保持原文的Markdown格式和结构
4. **代码保留**：代码块、脚本等内容保持原样

---

> 📝 **备注**：
> - 本次Git Sync新增了 `claude-for-msft-365-install/` 目录的6个文件
> - 中文版May06已完成约90%的翻译工作
> - 剩余约30个文件待翻译