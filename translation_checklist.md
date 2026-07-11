# 中文翻译缺失文件清单

> 生成日期: 2026-07-01
> 对比范围: 最新 upstream/main 与 中文版/ 目录

---

## 统计摘要

| 模块 | 源文件数 | 中文版文件数 | 差额 |
|---|---|---|---|
| 根文档 | 3 | 0 | +3 |
| claude-for-msft-365-install | 20 | 13 | +7 |
| managed-agent-cookbooks | 61 | 11 | +50 |
| plugins | 274 | 274 | +0 |

---

## 需要翻译的文档（.md / .txt）—— 共 5 个

| # | 模块 | 文件路径 |
|---|------|----------|
| 1 | 根文档 | `AGENTS.md` |
| 2 | 根文档 | `CLAUDE.md` |
| 3 | 根文档 | `README.md` |
| 4 | claude-for-msft-365-install | `commands/entra-app.md` |
| 5 | plugins | `agent-plugins/pitch-agent/skills/dcf-model/requirements.txt` |

---

## 需要同步的配置/代码文件（可选）—— 共 59 个

> 这类文件通常不需要逐字翻译，但中文版目录里若需要完整镜像，可同步一份。

| # | 模块 | 文件路径 |
|---|------|----------|
| 1 | claude-for-msft-365-install | `.claude-plugin/plugin.json` |
| 2 | claude-for-msft-365-install | `scripts/build-manifest.mjs` |
| 3 | claude-for-msft-365-install | `scripts/clear-addin-cache.ps1` |
| 4 | claude-for-msft-365-install | `scripts/clear-addin-cache.sh` |
| 5 | claude-for-msft-365-install | `scripts/sideload-addin.ps1` |
| 6 | claude-for-msft-365-install | `scripts/sideload-addin.sh` |
| 7 | managed-agent-cookbooks | `earnings-reviewer/agent.yaml` |
| 8 | managed-agent-cookbooks | `earnings-reviewer/steering-examples.json` |
| 9 | managed-agent-cookbooks | `earnings-reviewer/subagents/model-updater.yaml` |
| 10 | managed-agent-cookbooks | `earnings-reviewer/subagents/note-writer.yaml` |
| 11 | managed-agent-cookbooks | `earnings-reviewer/subagents/transcript-reader.yaml` |
| 12 | managed-agent-cookbooks | `gl-reconciler/agent.yaml` |
| 13 | managed-agent-cookbooks | `gl-reconciler/steering-examples.json` |
| 14 | managed-agent-cookbooks | `gl-reconciler/subagents/critic.yaml` |
| 15 | managed-agent-cookbooks | `gl-reconciler/subagents/reader.yaml` |
| 16 | managed-agent-cookbooks | `gl-reconciler/subagents/resolver.yaml` |
| 17 | managed-agent-cookbooks | `kyc-screener/agent.yaml` |
| 18 | managed-agent-cookbooks | `kyc-screener/steering-examples.json` |
| 19 | managed-agent-cookbooks | `kyc-screener/subagents/doc-reader.yaml` |
| 20 | managed-agent-cookbooks | `kyc-screener/subagents/escalator.yaml` |
| 21 | managed-agent-cookbooks | `kyc-screener/subagents/rules-engine.yaml` |
| 22 | managed-agent-cookbooks | `market-researcher/agent.yaml` |
| 23 | managed-agent-cookbooks | `market-researcher/steering-examples.json` |
| 24 | managed-agent-cookbooks | `market-researcher/subagents/comps-spreader.yaml` |
| 25 | managed-agent-cookbooks | `market-researcher/subagents/note-writer.yaml` |
| 26 | managed-agent-cookbooks | `market-researcher/subagents/sector-reader.yaml` |
| 27 | managed-agent-cookbooks | `meeting-prep-agent/agent.yaml` |
| 28 | managed-agent-cookbooks | `meeting-prep-agent/steering-examples.json` |
| 29 | managed-agent-cookbooks | `meeting-prep-agent/subagents/news-reader.yaml` |
| 30 | managed-agent-cookbooks | `meeting-prep-agent/subagents/pack-writer.yaml` |
| 31 | managed-agent-cookbooks | `meeting-prep-agent/subagents/profiler.yaml` |
| 32 | managed-agent-cookbooks | `model-builder/agent.yaml` |
| 33 | managed-agent-cookbooks | `model-builder/steering-examples.json` |
| 34 | managed-agent-cookbooks | `model-builder/subagents/auditor.yaml` |
| 35 | managed-agent-cookbooks | `model-builder/subagents/builder.yaml` |
| 36 | managed-agent-cookbooks | `model-builder/subagents/data-puller.yaml` |
| 37 | managed-agent-cookbooks | `month-end-closer/agent.yaml` |
| 38 | managed-agent-cookbooks | `month-end-closer/steering-examples.json` |
| 39 | managed-agent-cookbooks | `month-end-closer/subagents/ledger-reader.yaml` |
| 40 | managed-agent-cookbooks | `month-end-closer/subagents/poster.yaml` |
| 41 | managed-agent-cookbooks | `month-end-closer/subagents/rollforward.yaml` |
| 42 | managed-agent-cookbooks | `pitch-agent/agent.yaml` |
| 43 | managed-agent-cookbooks | `pitch-agent/steering-examples.json` |
| 44 | managed-agent-cookbooks | `pitch-agent/subagents/deck-writer.yaml` |
| 45 | managed-agent-cookbooks | `pitch-agent/subagents/modeler.yaml` |
| 46 | managed-agent-cookbooks | `pitch-agent/subagents/researcher.yaml` |
| 47 | managed-agent-cookbooks | `statement-auditor/agent.yaml` |
| 48 | managed-agent-cookbooks | `statement-auditor/steering-examples.json` |
| 49 | managed-agent-cookbooks | `statement-auditor/subagents/flagger.yaml` |
| 50 | managed-agent-cookbooks | `statement-auditor/subagents/reconciler.yaml` |
| 51 | managed-agent-cookbooks | `statement-auditor/subagents/statement-reader.yaml` |
| 52 | managed-agent-cookbooks | `valuation-reviewer/agent.yaml` |
| 53 | managed-agent-cookbooks | `valuation-reviewer/steering-examples.json` |
| 54 | managed-agent-cookbooks | `valuation-reviewer/subagents/package-reader.yaml` |
| 55 | managed-agent-cookbooks | `valuation-reviewer/subagents/publisher.yaml` |
| 56 | managed-agent-cookbooks | `valuation-reviewer/subagents/valuation-runner.yaml` |
| 57 | plugins | `agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py` |
| 58 | plugins | `agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py` |
| 59 | plugins | `vertical-plugins/equity-research/hooks/hooks.json` |

---

## 中文版中多余/已不存在的文件—— 共 4 个

> upstream 已删除或路径变更，中文版里仍可保留，但建议复核。

| # | 模块 | 文件路径 |
|---|------|----------|
| 1 | plugins | `partner-built/spglobal/skills/earnings-preview-beta/references/earnings-preview-framework.md` |
| 2 | plugins | `vertical-plugins/investment-banking/.claude/investment-banking.local.md.example` |
| 3 | plugins | `vertical-plugins/financial-analysis/commands/ib-check-deck.md` |
| 4 | plugins | `vertical-plugins/financial-analysis/skills/check-model/SKILL.md` |

---

## 结论

排除代码/配置文件后，当前还有 **5 个文件需要翻译/补中文版本**。
