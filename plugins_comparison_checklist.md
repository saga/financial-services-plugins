# Plugins vs 中文版 翻译进度Checklist

**生成日期**: 2026-06-07
**对比目录**: `plugins/` vs `中文版/plugins/`
**统计**: plugins目录共有228个.md文件，中文版有231个.md文件（中文版多出3个文件）

---

## 📊 总体状态

| 项目 | 数量 |
|------|------|
| plugins目录.md文件总数 | 228 |
| 中文版目录.md文件总数 | 231 |
| **plugins有但中文版缺失** | **228** |
| **中文版有多余文件** | **3** |

---

## 🚨 缺失文件总览

### 按类别统计

| 类别 | 缺失文件数 | 说明 |
|------|-----------|------|
| `vertical-plugins/` | 120 | 垂直行业插件 |
| `agent-plugins/` | 80 | 代理插件 |
| `partner-built/` | 28 | 合作伙伴构建插件 |
| **合计** | **228** | |

### 按子目录详细统计

| 子目录 | 缺失文件数 | 说明 |
|--------|-----------|------|
| `vertical-plugins/financial-analysis` | 30 | 财务分析插件 |
| `vertical-plugins/equity-research` | 29 | 股票研究插件 |
| `agent-plugins/pitch-agent` | 22 | Pitch代理 |
| `vertical-plugins/investment-banking` | 21 | 投资银行插件 |
| `vertical-plugins/private-equity` | 20 | 私募股权插件 |
| `partner-built/lseg` | 18 | LSEG合作伙伴 |
| `vertical-plugins/wealth-management` | 12 | 财富管理插件 |
| `agent-plugins/model-builder` | 11 | 模型构建器 |
| `partner-built/spglobal` | 10 | S&P Global合作伙伴 |
| `agent-plugins/earnings-reviewer` | 10 | 收益审查代理 |
| `agent-plugins/market-researcher` | 8 | 市场研究代理 |
| `vertical-plugins/fund-admin` | 6 | 基金管理插件 |
| `agent-plugins/month-end-closer` | 6 | 月末结算代理 |
| `agent-plugins/valuation-reviewer` | 5 | 估值审查代理 |
| `agent-plugins/meeting-prep-agent` | 5 | 会议准备代理 |
| `agent-plugins/gl-reconciler` | 5 | 总账对账代理 |
| `agent-plugins/statement-auditor` | 4 | 报表审计代理 |
| `agent-plugins/kyc-screener` | 4 | KYC筛选代理 |
| `vertical-plugins/operations` | 2 | 运营插件 |

---

## 🚨 优先级P0 - 待翻译文件（plugins有但中文版缺失）

### agent-plugins/earnings-reviewer/ 缺失文件 (10个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `agent-plugins/earnings-reviewer/agents/earnings-reviewer.md` | P0 | 收益审查代理定义 |
| `agent-plugins/earnings-reviewer/skills/audit-xls/SKILL.md` | P0 | 审计电子表格技能 |
| `agent-plugins/earnings-reviewer/skills/earnings-analysis/SKILL.md` | P0 | 收益分析技能 |
| `agent-plugins/earnings-reviewer/skills/earnings-analysis/references/best-practices.md` | P0 | 最佳实践参考 |
| `agent-plugins/earnings-reviewer/skills/earnings-analysis/references/report-structure.md` | P0 | 报告结构参考 |
| `agent-plugins/earnings-reviewer/skills/earnings-analysis/references/workflow.md` | P0 | 工作流参考 |
| `agent-plugins/earnings-reviewer/skills/earnings-preview/SKILL.md` | P0 | 收益预览技能 |
| `agent-plugins/earnings-reviewer/skills/model-update/SKILL.md` | P0 | 模型更新技能 |
| `agent-plugins/earnings-reviewer/skills/morning-note/SKILL.md` | P0 | 早间笔记技能 |
| `agent-plugins/earnings-reviewer/skills/xlsx-author/SKILL.md` | P0 | Excel生成技能 |

### agent-plugins/gl-reconciler/ 缺失文件 (5个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `agent-plugins/gl-reconciler/agents/gl-reconciler.md` | P0 | 总账对账代理定义 |
| `agent-plugins/gl-reconciler/skills/audit-xls/SKILL.md` | P0 | 审计电子表格技能 |
| `agent-plugins/gl-reconciler/skills/break-trace/SKILL.md` | P0 | 断点追踪技能 |
| `agent-plugins/gl-reconciler/skills/gl-recon/SKILL.md` | P0 | 总账对账技能 |
| `agent-plugins/gl-reconciler/skills/xlsx-author/SKILL.md` | P0 | Excel生成技能 |

### agent-plugins/kyc-screener/ 缺失文件 (4个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `agent-plugins/kyc-screener/agents/kyc-screener.md` | P0 | KYC筛选代理定义 |
| `agent-plugins/kyc-screener/skills/kyc-doc-parse/SKILL.md` | P0 | KYC文档解析技能 |
| `agent-plugins/kyc-screener/skills/kyc-rules/SKILL.md` | P0 | KYC规则技能 |
| `agent-plugins/kyc-screener/skills/xlsx-author/SKILL.md` | P0 | Excel生成技能 |

### agent-plugins/market-researcher/ 缺失文件 (8个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `agent-plugins/market-researcher/agents/market-researcher.md` | P0 | 市场研究代理定义 |
| `agent-plugins/market-researcher/skills/competitive-analysis/SKILL.md` | P0 | 竞争分析技能 |
| `agent-plugins/market-researcher/skills/competitive-analysis/references/frameworks.md` | P0 | 分析框架参考 |
| `agent-plugins/market-researcher/skills/competitive-analysis/references/schemas.md` | P0 | 数据架构参考 |
| `agent-plugins/market-researcher/skills/comps-analysis/SKILL.md` | P0 | 可比公司分析技能 |
| `agent-plugins/market-researcher/skills/idea-generation/SKILL.md` | P0 | 创意生成技能 |
| `agent-plugins/market-researcher/skills/pptx-author/SKILL.md` | P0 | PPT生成技能 |
| `agent-plugins/market-researcher/skills/sector-overview/SKILL.md` | P0 | 行业概览技能 |

### agent-plugins/meeting-prep-agent/ 缺失文件 (5个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `agent-plugins/meeting-prep-agent/agents/meeting-prep-agent.md` | P0 | 会议准备代理定义 |
| `agent-plugins/meeting-prep-agent/skills/client-report/SKILL.md` | P0 | 客户报告技能 |
| `agent-plugins/meeting-prep-agent/skills/client-review/SKILL.md` | P0 | 客户审查技能 |
| `agent-plugins/meeting-prep-agent/skills/investment-proposal/SKILL.md` | P0 | 投资建议技能 |
| `agent-plugins/meeting-prep-agent/skills/pptx-author/SKILL.md` | P0 | PPT生成技能 |

### agent-plugins/model-builder/ 缺失文件 (11个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `agent-plugins/model-builder/agents/model-builder.md` | P0 | 模型构建器代理定义 |
| `agent-plugins/model-builder/skills/3-statement-model/SKILL.md` | P0 | 三表模型技能 |
| `agent-plugins/model-builder/skills/3-statement-model/references/formatting.md` | P0 | 格式标准参考 |
| `agent-plugins/model-builder/skills/3-statement-model/references/formulas.md` | P0 | 公式参考 |
| `agent-plugins/model-builder/skills/3-statement-model/references/sec-filings.md` | P0 | SEC文件提取参考 |
| `agent-plugins/model-builder/skills/audit-xls/SKILL.md` | P0 | 审计电子表格技能 |
| `agent-plugins/model-builder/skills/comps-analysis/SKILL.md` | P0 | 可比公司分析技能 |
| `agent-plugins/model-builder/skills/dcf-model/SKILL.md` | P0 | DCF模型技能 |
| `agent-plugins/model-builder/skills/dcf-model/TROUBLESHOOTING.md` | P0 | DCF故障排除 |
| `agent-plugins/model-builder/skills/lbo-model/SKILL.md` | P0 | LBO模型技能 |
| `agent-plugins/model-builder/skills/xlsx-author/SKILL.md` | P0 | Excel生成技能 |

### agent-plugins/month-end-closer/ 缺失文件 (6个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `agent-plugins/month-end-closer/agents/month-end-closer.md` | P0 | 月末结算代理定义 |
| `agent-plugins/month-end-closer/skills/accrual-schedule/SKILL.md` | P0 | 应计计划技能 |
| `agent-plugins/month-end-closer/skills/audit-xls/SKILL.md` | P0 | 审计电子表格技能 |
| `agent-plugins/month-end-closer/skills/roll-forward/SKILL.md` | P0 | 滚动预测技能 |
| `agent-plugins/month-end-closer/skills/variance-commentary/SKILL.md` | P0 | 差异分析技能 |
| `agent-plugins/month-end-closer/skills/xlsx-author/SKILL.md` | P0 | Excel生成技能 |

### agent-plugins/pitch-agent/ 缺失文件 (22个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `agent-plugins/pitch-agent/agents/pitch-agent.md` | P0 | Pitch代理定义 |
| `agent-plugins/pitch-agent/skills/audit-xls/SKILL.md` | P0 | 审计电子表格技能 |
| `agent-plugins/pitch-agent/skills/dcf-model/SKILL.md` | P0 | DCF模型技能 |
| `agent-plugins/pitch-agent/skills/dcf-model/TROUBLESHOOTING.md` | P0 | DCF故障排除 |
| `agent-plugins/pitch-agent/skills/dcf-model/requirements.txt` | P1 | Python依赖清单 |
| `agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py` | P1 | DCF验证脚本 |
| `agent-plugins/pitch-agent/skills/deck-refresh/SKILL.md` | P0 | Deck刷新技能 |
| `agent-plugins/pitch-agent/skills/ib-check-deck/SKILL.md` | P0 | 投行检查技能 |
| `agent-plugins/pitch-agent/skills/ib-check-deck/references/ib-terminology.md` | P0 | 投行术语参考 |
| `agent-plugins/pitch-agent/skills/ib-check-deck/references/report-format.md` | P0 | 报告格式参考 |
| `agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py` | P1 | 数字提取脚本 |
| `agent-plugins/pitch-agent/skills/pitch-deck/SKILL.md` | P0 | Pitch演示技能 |
| `agent-plugins/pitch-agent/skills/pitch-deck/reference/calculation-standards.md` | P0 | 计算标准参考 |
| `agent-plugins/pitch-agent/skills/pitch-deck/reference/formatting-standards.md` | P0 | 格式标准参考 |
| `agent-plugins/pitch-agent/skills/pitch-deck/reference/slide-templates.md` | P0 | 幻灯片模板参考 |
| `agent-plugins/pitch-agent/skills/pitch-deck/reference/xml-reference.md` | P1 | XML参考 |
| `agent-plugins/pitch-agent/skills/sector-overview/SKILL.md` | P0 | 行业概览技能 |
| `agent-plugins/pitch-agent/skills/xlsx-author/SKILL.md` | P0 | Excel生成技能 |
| `agent-plugins/pitch-agent/skills/pptx-author/SKILL.md` | P0 | PPT生成技能 |
| `agent-plugins/pitch-agent/skills/lbo-model/SKILL.md` | P0 | LBO模型技能 |
| `agent-plugins/pitch-agent/skills/comps-analysis/SKILL.md` | P0 | 可比公司分析技能 |
| `agent-plugins/pitch-agent/skills/3-statement-model/SKILL.md` | P0 | 三表模型技能 |

### agent-plugins/statement-auditor/ 缺失文件 (4个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `agent-plugins/statement-auditor/agents/statement-auditor.md` | P0 | 报表审计代理定义 |
| `agent-plugins/statement-auditor/skills/audit-xls/SKILL.md` | P0 | 审计电子表格技能 |
| `agent-plugins/statement-auditor/skills/statement-review/SKILL.md` | P0 | 报表审查技能 |
| `agent-plugins/statement-auditor/skills/xlsx-author/SKILL.md` | P0 | Excel生成技能 |

### agent-plugins/valuation-reviewer/ 缺失文件 (5个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `agent-plugins/valuation-reviewer/agents/valuation-reviewer.md` | P0 | 估值审查代理定义 |
| `agent-plugins/valuation-reviewer/skills/audit-xls/SKILL.md` | P0 | 审计电子表格技能 |
| `agent-plugins/valuation-reviewer/skills/valuation-analysis/SKILL.md` | P0 | 估值分析技能 |
| `agent-plugins/valuation-reviewer/skills/variance-commentary/SKILL.md` | P0 | 差异分析技能 |
| `agent-plugins/valuation-reviewer/skills/xlsx-author/SKILL.md` | P0 | Excel生成技能 |

### partner-built/lseg/ 缺失文件 (18个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `partner-built/lseg/skills/data-analytics/SKILL.md` | P0 | 数据分析技能 |
| `partner-built/lseg/skills/data-retrieval/SKILL.md` | P0 | 数据检索技能 |
| `partner-built/lseg/skills/earnings-preview/SKILL.md` | P0 | 收益预览技能 |
| `partner-built/lseg/skills/market-data/SKILL.md` | P0 | 市场数据技能 |
| `partner-built/lseg/skills/news-analysis/SKILL.md` | P0 | 新闻分析技能 |
| `partner-built/lseg/skills/portfolio-analysis/SKILL.md` | P0 | 投资组合分析技能 |
| `partner-built/lseg/skills/quote-retrieval/SKILL.md` | P0 | 报价检索技能 |
| `partner-built/lseg/skills/research-report/SKILL.md` | P0 | 研究报告技能 |
| `partner-built/lseg/skills/risk-analysis/SKILL.md` | P0 | 风险分析技能 |
| `partner-built/lseg/skills/screening/SKILL.md` | P0 | 筛选技能 |
| `partner-built/lseg/skills/sentiment-analysis/SKILL.md` | P0 | 情感分析技能 |
| `partner-built/lseg/skills/technical-analysis/SKILL.md` | P0 | 技术分析技能 |
| `partner-built/lseg/skills/trading-signals/SKILL.md` | P0 | 交易信号技能 |
| `partner-built/lseg/skills/trend-analysis/SKILL.md` | P0 | 趋势分析技能 |
| `partner-built/lseg/skills/valuation/SKILL.md` | P0 | 估值技能 |
| `partner-built/lseg/skills/volatility-analysis/SKILL.md` | P0 | 波动率分析技能 |
| `partner-built/lseg/skills/wealth-management/SKILL.md` | P0 | 财富管理技能 |
| `partner-built/lseg/skills/yield-analysis/SKILL.md` | P0 | 收益率分析技能 |

### partner-built/spglobal/ 缺失文件 (10个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `partner-built/spglobal/skills/earnings-preview-beta/SKILL.md` | P0 | 收益预览测试版技能 |
| `partner-built/spglobal/skills/earnings-preview-beta/report-template.md` | P1 | 报告模板 |
| `partner-built/spglobal/skills/funding-digest/SKILL.md` | P0 | 融资摘要技能 |
| `partner-built/spglobal/skills/market-intelligence/SKILL.md` | P0 | 市场情报技能 |
| `partner-built/spglobal/skills/sector-analysis/SKILL.md` | P0 | 行业分析技能 |
| `partner-built/spglobal/skills/tear-sheet/SKILL.md` | P0 | Tear Sheet技能 |
| `partner-built/spglobal/skills/valuation/SKILL.md` | P0 | 估值技能 |
| `partner-built/spglobal/skills/credit-analysis/SKILL.md` | P0 | 信用分析技能 |
| `partner-built/spglobal/skills/esg-analysis/SKILL.md` | P0 | ESG分析技能 |
| `partner-built/spglobal/skills/risk-assessment/SKILL.md` | P0 | 风险评估技能 |

### vertical-plugins/equity-research/ 缺失文件 (29个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `vertical-plugins/equity-research/README.md` | P0 | 股票研究插件说明 |
| `vertical-plugins/equity-research/commands/earnings-review.md` | P0 | 收益审查命令 |
| `vertical-plugins/equity-research/commands/initiation.md` | P0 | 启动报告命令 |
| `vertical-plugins/equity-research/commands/model-update.md` | P0 | 模型更新命令 |
| `vertical-plugins/equity-research/commands/morning-note.md` | P0 | 早间笔记命令 |
| `vertical-plugins/equity-research/commands/sector-note.md` | P0 | 行业笔记命令 |
| `vertical-plugins/equity-research/skills/earnings-analysis/SKILL.md` | P0 | 收益分析技能 |
| `vertical-plugins/equity-research/skills/earnings-preview/SKILL.md` | P0 | 收益预览技能 |
| `vertical-plugins/equity-research/skills/financial-model/SKILL.md` | P0 | 财务模型技能 |
| `vertical-plugins/equity-research/skills/idea-generation/SKILL.md` | P0 | 创意生成技能 |
| `vertical-plugins/equity-research/skills/initiation-report/SKILL.md` | P0 | 启动报告技能 |
| `vertical-plugins/equity-research/skills/morning-note/SKILL.md` | P0 | 早间笔记技能 |
| `vertical-plugins/equity-research/skills/sector-analysis/SKILL.md` | P0 | 行业分析技能 |
| `vertical-plugins/equity-research/skills/sector-note/SKILL.md` | P0 | 行业笔记技能 |
| `vertical-plugins/equity-research/skills/valuation/SKILL.md` | P0 | 估值技能 |
| `vertical-plugins/equity-research/skills/xlsx-author/SKILL.md` | P0 | Excel生成技能 |
| `vertical-plugins/equity-research/skills/pptx-author/SKILL.md` | P0 | PPT生成技能 |
| `vertical-plugins/equity-research/skills/comps-analysis/SKILL.md` | P0 | 可比公司分析技能 |
| `vertical-plugins/equity-research/skills/dcf-model/SKILL.md` | P0 | DCF模型技能 |
| `vertical-plugins/equity-research/skills/technical-analysis/SKILL.md` | P0 | 技术分析技能 |
| `vertical-plugins/equity-research/skills/fundamental-analysis/SKILL.md` | P0 | 基本面分析技能 |
| `vertical-plugins/equity-research/skills/risk-analysis/SKILL.md` | P0 | 风险分析技能 |
| `vertical-plugins/equity-research/skills/esg-analysis/SKILL.md` | P0 | ESG分析技能 |
| `vertical-plugins/equity-research/skills/sentiment-analysis/SKILL.md` | P0 | 情感分析技能 |
| `vertical-plugins/equity-research/skills/news-analysis/SKILL.md` | P0 | 新闻分析技能 |
| `vertical-plugins/equity-research/skills/portfolio-analysis/SKILL.md` | P0 | 投资组合分析技能 |
| `vertical-plugins/equity-research/skills/market-data/SKILL.md` | P0 | 市场数据技能 |
| `vertical-plugins/equity-research/skills/screening/SKILL.md` | P0 | 筛选技能 |
| `vertical-plugins/equity-research/skills/quote-retrieval/SKILL.md` | P0 | 报价检索技能 |

### vertical-plugins/financial-analysis/ 缺失文件 (30个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `vertical-plugins/financial-analysis/README.md` | P0 | 财务分析插件说明 |
| `vertical-plugins/financial-analysis/commands/budget-vs-actual.md` | P0 | 预算对比实际命令 |
| `vertical-plugins/financial-analysis/commands/cash-flow-analysis.md` | P0 | 现金流分析命令 |
| `vertical-plugins/financial-analysis/commands/financial-health.md` | P0 | 财务健康命令 |
| `vertical-plugins/financial-analysis/commands/ratio-analysis.md` | P0 | 比率分析命令 |
| `vertical-plugins/financial-analysis/commands/trend-analysis.md` | P0 | 趋势分析命令 |
| `vertical-plugins/financial-analysis/skills/3-statement-model/SKILL.md` | P0 | 三表模型技能 |
| `vertical-plugins/financial-analysis/skills/audit-xls/SKILL.md` | P0 | 审计电子表格技能 |
| `vertical-plugins/financial-analysis/skills/budget-vs-actual/SKILL.md` | P0 | 预算对比实际技能 |
| `vertical-plugins/financial-analysis/skills/cash-flow-analysis/SKILL.md` | P0 | 现金流分析技能 |
| `vertical-plugins/financial-analysis/skills/comps-analysis/SKILL.md` | P0 | 可比公司分析技能 |
| `vertical-plugins/financial-analysis/skills/dcf-model/SKILL.md` | P0 | DCF模型技能 |
| `vertical-plugins/financial-analysis/skills/financial-health/SKILL.md` | P0 | 财务健康技能 |
| `vertical-plugins/financial-analysis/skills/ib-check-deck/SKILL.md` | P0 | 投行检查技能 |
| `vertical-plugins/financial-analysis/skills/ib-check-deck/references/ib-terminology.md` | P0 | 投行术语参考 |
| `vertical-plugins/financial-analysis/skills/ib-check-deck/references/report-format.md` | P0 | 报告格式参考 |
| `vertical-plugins/financial-analysis/skills/lbo-model/SKILL.md` | P0 | LBO模型技能 |
| `vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md` | P0 | PPT模板创建技能 |
| `vertical-plugins/financial-analysis/skills/pptx-author/SKILL.md` | P0 | PPT生成技能 |
| `vertical-plugins/financial-analysis/skills/skill-creator/SKILL.md` | P0 | 技能创建技能 |
| `vertical-plugins/financial-analysis/skills/skill-creator/references/output-patterns.md` | P0 | 输出模式参考 |
| `vertical-plugins/financial-analysis/skills/skill-creator/references/workflows.md` | P0 | 工作流参考 |
| `vertical-plugins/financial-analysis/skills/xlsx-author/SKILL.md` | P0 | Excel生成技能 |
| `vertical-plugins/financial-analysis/skills/ratio-analysis/SKILL.md` | P0 | 比率分析技能 |
| `vertical-plugins/financial-analysis/skills/trend-analysis/SKILL.md` | P0 | 趋势分析技能 |
| `vertical-plugins/financial-analysis/skills/variance-commentary/SKILL.md` | P0 | 差异分析技能 |
| `vertical-plugins/financial-analysis/skills/forecasting/SKILL.md` | P0 | 预测技能 |
| `vertical-plugins/financial-analysis/skills/scenario-analysis/SKILL.md` | P0 | 情景分析技能 |
| `vertical-plugins/financial-analysis/skills/sensitivity-analysis/SKILL.md` | P0 | 敏感性分析技能 |
| `vertical-plugins/financial-analysis/skills/monte-carlo/SKILL.md` | P0 | 蒙特卡洛模拟技能 |

### vertical-plugins/fund-admin/ 缺失文件 (6个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `vertical-plugins/fund-admin/skills/accrual-schedule/SKILL.md` | P0 | 应计计划技能 |
| `vertical-plugins/fund-admin/skills/break-trace/SKILL.md` | P0 | 断点追踪技能 |
| `vertical-plugins/fund-admin/skills/gl-recon/SKILL.md` | P0 | 总账对账技能 |
| `vertical-plugins/fund-admin/skills/nav-tieout/SKILL.md` | P0 | NAV核对技能 |
| `vertical-plugins/fund-admin/skills/roll-forward/SKILL.md` | P0 | 滚动预测技能 |
| `vertical-plugins/fund-admin/skills/variance-commentary/SKILL.md` | P0 | 差异分析技能 |

### vertical-plugins/investment-banking/ 缺失文件 (21个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `vertical-plugins/investment-banking/README.md` | P0 | 投资银行插件说明 |
| `vertical-plugins/investment-banking/commands/buyer-list.md` | P0 | 买方列表命令 |
| `vertical-plugins/investment-banking/commands/cim.md` | P0 | CIM命令 |
| `vertical-plugins/investment-banking/commands/deal-tracker.md` | P0 | 交易追踪命令 |
| `vertical-plugins/investment-banking/commands/merger-model.md` | P0 | 并购模型命令 |
| `vertical-plugins/investment-banking/commands/one-pager.md` | P0 | 单页摘要命令 |
| `vertical-plugins/investment-banking/commands/process-letter.md` | P0 | 流程信函命令 |
| `vertical-plugins/investment-banking/commands/teaser.md` | P0 | Teaser命令 |
| `vertical-plugins/investment-banking/skills/buyer-list/SKILL.md` | P0 | 买方列表技能 |
| `vertical-plugins/investment-banking/skills/cim-builder/SKILL.md` | P0 | CIM构建技能 |
| `vertical-plugins/investment-banking/skills/datapack-builder/SKILL.md` | P0 | 数据包构建技能 |
| `vertical-plugins/investment-banking/skills/deal-tracker/SKILL.md` | P0 | 交易追踪技能 |
| `vertical-plugins/investment-banking/skills/merger-model/SKILL.md` | P0 | 并购模型技能 |
| `vertical-plugins/investment-banking/skills/pitch-deck/SKILL.md` | P0 | Pitch演示技能 |
| `vertical-plugins/investment-banking/skills/pitch-deck/reference/calculation-standards.md` | P0 | 计算标准参考 |
| `vertical-plugins/investment-banking/skills/pitch-deck/reference/formatting-standards.md` | P0 | 格式标准参考 |
| `vertical-plugins/investment-banking/skills/pitch-deck/reference/slide-templates.md` | P0 | 幻灯片模板参考 |
| `vertical-plugins/investment-banking/skills/pitch-deck/reference/xml-reference.md` | P1 | XML参考 |
| `vertical-plugins/investment-banking/skills/process-letter/SKILL.md` | P0 | 流程信函技能 |
| `vertical-plugins/investment-banking/skills/strip-profile/SKILL.md` | P0 | Strip Profile技能 |
| `vertical-plugins/investment-banking/skills/teaser/SKILL.md` | P0 | Teaser技能 |

### vertical-plugins/operations/ 缺失文件 (2个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `vertical-plugins/operations/skills/kyc-doc-parse/SKILL.md` | P0 | KYC文档解析技能 |
| `vertical-plugins/operations/skills/kyc-rules/SKILL.md` | P0 | KYC规则技能 |

### vertical-plugins/private-equity/ 缺失文件 (20个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `vertical-plugins/private-equity/commands/ai-readiness.md` | P0 | AI就绪命令 |
| `vertical-plugins/private-equity/commands/dd-checklist.md` | P0 | 尽职调查清单命令 |
| `vertical-plugins/private-equity/commands/dd-prep.md` | P0 | 尽职调查准备命令 |
| `vertical-plugins/private-equity/commands/ic-memo.md` | P0 | IC备忘录命令 |
| `vertical-plugins/private-equity/commands/portfolio.md` | P0 | 投资组合命令 |
| `vertical-plugins/private-equity/commands/returns.md` | P0 | 收益命令 |
| `vertical-plugins/private-equity/commands/screen-deal.md` | P0 | 交易筛选命令 |
| `vertical-plugins/private-equity/commands/source.md` | P0 | 来源命令 |
| `vertical-plugins/private-equity/commands/unit-economics.md` | P0 | 单位经济命令 |
| `vertical-plugins/private-equity/commands/value-creation.md` | P0 | 价值创造命令 |
| `vertical-plugins/private-equity/skills/ai-readiness/SKILL.md` | P0 | AI就绪技能 |
| `vertical-plugins/private-equity/skills/dd-checklist/SKILL.md` | P0 | 尽职调查清单技能 |
| `vertical-plugins/private-equity/skills/dd-meeting-prep/SKILL.md` | P0 | 尽职调查会议准备技能 |
| `vertical-plugins/private-equity/skills/deal-screening/SKILL.md` | P0 | 交易筛选技能 |
| `vertical-plugins/private-equity/skills/deal-sourcing/SKILL.md` | P0 | 交易来源技能 |
| `vertical-plugins/private-equity/skills/ic-memo/SKILL.md` | P0 | IC备忘录技能 |
| `vertical-plugins/private-equity/skills/portfolio-monitoring/SKILL.md` | P0 | 投资组合监控技能 |
| `vertical-plugins/private-equity/skills/returns-analysis/SKILL.md` | P0 | 收益分析技能 |
| `vertical-plugins/private-equity/skills/unit-economics/SKILL.md` | P0 | 单位经济技能 |
| `vertical-plugins/private-equity/skills/value-creation-plan/SKILL.md` | P0 | 价值创造计划技能 |

### vertical-plugins/wealth-management/ 缺失文件 (12个)

| 文件路径 | 优先级 | 说明 |
|----------|--------|------|
| `vertical-plugins/wealth-management/commands/client-report.md` | P0 | 客户报告命令 |
| `vertical-plugins/wealth-management/commands/client-review.md` | P0 | 客户审查命令 |
| `vertical-plugins/wealth-management/commands/financial-plan.md` | P0 | 财务计划命令 |
| `vertical-plugins/wealth-management/commands/proposal.md` | P0 | 提案命令 |
| `vertical-plugins/wealth-management/commands/rebalance.md` | P0 | 再平衡命令 |
| `vertical-plugins/wealth-management/commands/tlh.md` | P0 | 税损收割命令 |
| `vertical-plugins/wealth-management/skills/client-report/SKILL.md` | P0 | 客户报告技能 |
| `vertical-plugins/wealth-management/skills/client-review/SKILL.md` | P0 | 客户审查技能 |
| `vertical-plugins/wealth-management/skills/financial-plan/SKILL.md` | P0 | 财务计划技能 |
| `vertical-plugins/wealth-management/skills/investment-proposal/SKILL.md` | P0 | 投资建议技能 |
| `vertical-plugins/wealth-management/skills/portfolio-rebalance/SKILL.md` | P0 | 投资组合再平衡技能 |
| `vertical-plugins/wealth-management/skills/tax-loss-harvesting/SKILL.md` | P0 | 税损收割技能 |

---

## 📋 Git Sync 变更记录

### 最近Sync时间点
- **Sync基准点**: commit `853f755` (upstream/main)
- **最新commit**: `b1ef740` (HEAD)

### Sync后新增/变更的plugins文件
> 自上次Merge后，plugins目录没有实质性文件变更。所有变更都在中文版相关目录。

**无实质性plugins文件变更**

### 当前HEAD vs upstream/main差异
| 文件 | 变更类型 |
|------|----------|
| `.claude/scheduled_tasks.json` | 配置变更 |
| `AGENTS.md` | 文档更新 |
| `plugins_comparison_checklist.md` | Checklist文档 |
| `run_translation.py` | 脚本 |
| `run_translation_serial.py` | 脚本 |
| `script.py` | 脚本 |
| `script_pe.py` | 脚本 |
| `translate_may05.py` | 翻译脚本 |
| `translation.pid` | PID文件 |

---

## 📝 翻译要求

1. **信达雅**：翻译准确、表达流畅、文辞优美
2. **金融知识解释**：每篇文章末尾添加详细的金融术语和金融知识解释部分，适合金融小白阅读
3. **格式保持**：保持原文的结构和格式
4. **术语统一**：使用统一的金融术语中文翻译

---

## 🎯 下一步行动

### 优先级P0（立即翻译）- 共228个文件

#### 第一阶段：核心代理插件 (80个文件)
1. `agent-plugins/earnings-reviewer/` - 10个文件
2. `agent-plugins/gl-reconciler/` - 5个文件
3. `agent-plugins/kyc-screener/` - 4个文件
4. `agent-plugins/market-researcher/` - 8个文件
5. `agent-plugins/meeting-prep-agent/` - 5个文件
6. `agent-plugins/model-builder/` - 11个文件
7. `agent-plugins/month-end-closer/` - 6个文件
8. `agent-plugins/pitch-agent/` - 22个文件
9. `agent-plugins/statement-auditor/` - 4个文件
10. `agent-plugins/valuation-reviewer/` - 5个文件

#### 第二阶段：合作伙伴插件 (28个文件)
11. `partner-built/lseg/` - 18个文件
12. `partner-built/spglobal/` - 10个文件

#### 第三阶段：垂直行业插件 (120个文件)
13. `vertical-plugins/equity-research/` - 29个文件
14. `vertical-plugins/financial-analysis/` - 30个文件
15. `vertical-plugins/fund-admin/` - 6个文件
16. `vertical-plugins/investment-banking/` - 21个文件
17. `vertical-plugins/operations/` - 2个文件
18. `vertical-plugins/private-equity/` - 20个文件
19. `vertical-plugins/wealth-management/` - 12个文件

---

## ⚠️ 重要说明

1. **中文版May06目录已不存在**：之前翻译到`中文版May06`的文件已经消失，所有翻译工作需要在`中文版`目录下重新进行。

2. **中文版目录已有231个文件**：但对比发现plugins目录下的228个文件在中文版中都没有对应翻译（路径和文件名不同）。

3. **建议**：
   - 确认`中文版`目录下的231个文件是否已经是翻译完成的文件
   - 如果是，需要检查这些文件是否对应plugins目录下的文件
   - 如果不是，需要重新进行翻译工作

4. **代码文件和.json文件**：根据要求，不需要翻译代码文件（.py, .txt等）和.json配置文件。