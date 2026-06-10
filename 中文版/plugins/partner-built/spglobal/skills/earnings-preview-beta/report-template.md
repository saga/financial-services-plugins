# HTML 报告模板参考指南

使用此模板作为单体公司业绩摘要（Earnings Preview）HTML 报告的基础。根据第 1-5 阶段收集的研究数据，自定义数据、图表和叙事内容。

## HTML 结构

该报告是一个独立的 HTML 文件，具有以下特点：
- 内嵌 CSS（无外部样式表）
- 通过 CDN 加载 Chart.js 以实现交互式图表
- 通过 `@media print` 实现打印友好样式
- 适用于屏幕显示和打印的响应式布局
- 目标：4-5 个打印页面

## 完整模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>业绩前瞻 — [公司名称] ([股票代码]) — [日期]</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js" integrity="sha384-vsrfeLOOY6KuIYKDlmVH5UiBmgIdB1oEf7p01YgWHuqmOHfZr374+odEv96n9tNC" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@3.1.0/dist/chartjs-plugin-annotation.min.js" integrity="sha384-3N9GHhCtN3CQef6tNfqgZlv7sQLYIkcChN+uaTZ7xVdzKYp/SjBNPxa92+hM7EAY" crossorigin="anonymous"></script>
  <style>
    /* ── 重置与基础样式 ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { font-size: 15px; }
    body {
      font-family: 'Arial Narrow', Arial, 'Microsoft YaHei', sans-serif;
      color: #1a1a2e;
      background: #fff;
      line-height: 1.6;
    }

    /* ── 布局 ── */
    .page {
      max-width: 1100px;
      margin: 0 auto;
      padding: 40px 48px;
    }
    .page-break {
      page-break-before: always;
      border-top: 2px solid #1a1a4e;
      margin-top: 48px;
      padding-top: 32px;
    }

    /* ── 页眉 / 封面 ── */
    .cover-header {
      border-bottom: 3px solid #1a1a4e;
      padding-bottom: 16px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .cover-header .brand {
      font-size: 24px;
      font-weight: bold;
      color: #1a1a4e;
      letter-spacing: 2px;
      text-transform: uppercase;
    }
    .cover-header .sector {
      font-size: 13px;
      color: #555;
    }
    .cover-header .date {
      font-size: 14px;
      color: #333;
      text-align: right;
    }
    .report-title {
      font-size: 26px;
      font-weight: bold;
      color: #1a1a2e;
      margin: 20px 0 16px 0;
      line-height: 1.3;
    }

    /* ── 执行摘要 ── */
    .executive-summary {
      font-size: 14px;
      line-height: 1.65;
      color: #222;
      margin-bottom: 16px;
    }
    .executive-summary p {
      margin-bottom: 10px;
      text-align: justify;
    }
    .executive-summary ul {
      margin: 8px 0 10px 20px
```

---

## Appendix: 金融背景知识

本文件是 Earnings Preview Beta 技能的 HTML 报告模板参考指南，详细说明了如何构建单体公司业绩摘要的可视化报告。本附录将系统介绍财报预览涉及的核心金融概念、估值方法、HTML 报告设计与可视化等知识。

---

### 1. 财报（Earnings）基础知识

#### 1.1 什么是财报

**定义**：财报是上市公司按监管要求定期披露的财务报告，向投资者展示公司经营成果、财务状况和现金流量。

**美国三大财报**：

| 财报 | 英文 | 频率 | 内容 |
|------|------|------|------|
| **10-K** | Annual Report | 年度 | 完整年度财报，包含所有细节 |
| **10-Q** | Quarterly Report | 季度 | 季度财报，比 10-K 简略 |
| **8-K** | Current Report | 事件驱动 | 重大事件即时披露 |

**中国 A 股财报**：
- **年报**：财年结束后 4 个月内披露
- **半年报**：上半年结束后 2 个月内
- **一季报**、**三季报**：季度结束后 1 个月内

#### 1.2 财报结构

**标准 10-K 结构**：

| 章节 | 内容 |
|------|------|
| **Part I** | 业务、风险、物业、法律 |
| **Part II** | 财务数据、市场数据、MD&A |
| **Part III** | 董事、高管薪酬、关联交易 |
| **Part IV** | 财务报表、附注 |
| **Schedules** | 附表 |

**三大财务报表**：

```
利润表（Income Statement）
  收入 (Revenue)
  - 销售成本 (COGS)
  = 毛利 (Gross Profit)
  - 营业费用 (Operating Expenses)
  = 营业利润 (Operating Income)
  ± 非经常性损益
  - 利息、税费
  = 净利润 (Net Income)

资产负债表（Balance Sheet）
  资产 = 负债 + 股东权益
  
现金流量表（Cash Flow Statement）
  经营活动 + 投资活动 + 融资活动 = 现金净变动
```

#### 1.3 关键财报日期

| 日期类型 | 英文 | 说明 |
|---------|------|------|
| **财年结束日** | Fiscal Year End | 公司会计年度的最后一天 |
| **财报发布日期** | Earnings Date | 正式发布 10-K/10-Q 的日期 |
| **Pre-announcement** | 业绩预告 | 财报前的初步数据 |
| **Quiet Period** | 静默期 | 财报前 1-2 周，公司不能公开宣传 |
| **Blackout Period** | 禁售期 | 高管不能买卖公司股票 |
| **Earnings Call** | 电话会议 | 管理层与分析师讨论财报 |

**四季度财报发布密集期**：
- **Q4 年报**：1-3 月（最密集）
- **Q1 季报**：4-5 月
- **Q2 半年报**：7-8 月
- **Q3 季报**：10-11 月

---

### 2. Earnings Preview 深度解析

#### 2.1 什么是 Earnings Preview

**定义**：Earnings Preview 是公司在正式发布季度财报前，分析师提前编写的"预告性研究报告"，预测公司业绩、识别关键关注点、准备问答要点。

**目的**：
- 提前洞察市场预期
- 识别关键风险和机会
- 准备电话会议问答
- 调整投资策略
- 评估估值合理性

**Earnings Preview 与其他研报类型对比**：

| 类型 | 时点 | 长度 | 目的 |
|------|------|------|------|
| **Initiation** | 首次覆盖 | 30-50 页 | 全面分析公司 |
| **Earnings Preview** | 财报前 1-2 周 | 5-15 页 | 预测财报表现 |
| **Earnings Review** | 财报后 1-3 天 | 3-10 页 | 分析实际业绩 |
| **Flash Note** | 事件后立即 | 1-2 页 | 快速反应 |
| **Update Note** | 季度更新 | 3-5 页 | 跟踪公司动态 |

#### 2.2 Earnings Preview 的核心内容

**1. 投资摘要（Executive Summary）**：
- 投资评级（Buy/Hold/Sell）
- 目标价（12 个月）
- 关键论点（3-5 个 bullet points）
- 主要风险

**2. 关键财务预测**：

| 指标 | 共识预期 | 自家预测 | 差异 | 去年同期 |
|------|---------|---------|------|---------|
| 收入 | $X | $Y | Z% | $A |
| 毛利率 | X% | Y% | Z pp | A% |
| 营业利润 | $X | $Y | Z% | $A |
| EPS | $X | $Y | Z% | $A |

**3. 关键运营指标**（KPI）：

| 业务 | KPI | 说明 |
|------|-----|------|
| SaaS | ARR、NRR、CAC、LTV | 订阅指标 |
| 电商 | GMV、活跃买家、转化率 | 交易指标 |
| 广告 | DAU、ARPU、广告加载率 | 用户指标 |
| 银行 | NIM、NPL、存款增长 | 金融指标 |

**4. 关注要点**：
- 管理层近期指引
- 行业趋势
- 竞争格局
- 季节性因素
- 一次性事件

**5. 风险因素**：
- 收入增速放缓
- 利润率压力
- 监管风险
- 汇率影响
- 一次性损益

#### 2.3 共识预期（Consensus Estimates）

**定义**：共识预期是市场上覆盖该公司的所有卖方分析师对下季度/年度业绩预测的中位数或平均值，是市场对公司业绩的"集体智慧"。

**计算方法**：

| 方法 | 公式 | 优缺点 |
|------|------|--------|
| **中位数** | 所有预测值排序取中间 | 稳健，不受极端值影响 |
| **算术平均** | Σ预测值 / 数量 | 受极端值影响 |
| **加权平均** | 按历史准确度加权 | 最准确但需历史数据 |
| **Strip Adjustment** | 移除明显异常预测 | 标准化 |

**预测字段**：

| 字段 | 英文 | 说明 |
|------|------|------|
| **收入** | Revenue/Sales | 销售总额 |
| **毛利润** | Gross Profit | 收入 - COGS |
| **营业利润** | Operating Income | 毛利 - 营业费用 |
| **净利润** | Net Income | 最终利润 |
| **EPS** | Earnings Per Share | 每股收益 |
| **EBITDA** | - | 息税折旧摊销前利润 |
| **FCF** | Free Cash Flow | 自由现金流 |
| **GUIDANCE** | 管理层指引 | 公司给出的下季度指引 |

**数据时间维度**：
- **NTM**（Next Twelve Months）：未来 12 个月
- **NTQ**（Next Three Quarters）：未来 3 个季度
- **FY+1**：下个财年
- **FY+2**：下下个财年

#### 2.4 "Beat" 与 "Miss" 文化

**定义**：
- **Beat**：实际值 > 共识预期 = 超预期
- **In-line**：实际值 ≈ 共识预期 = 符合预期
- **Miss**：实际值 < 共识预期 = 不及预期

**华尔街对 Beat 的痴迷**：

| Beat 幅度 | 股价反应 |
|---------|---------|
| 重大 Beat（>+5%） | 股价通常上涨 5-15% |
| 小幅 Beat（+1-5%） | 股价微涨 1-3% |
| In-line | 股价基本不变 |
| 小幅 Miss（-1-5%） | 股价下跌 3-7% |
| 重大 Miss（>-5%） | 股价大幅下跌 10-20% |

**为什么 Beat 这么重要**：
1. **市场预期管理**：公司会给出保守指引
2. **投资者心理学**：Beat = 安全感
3. **短期主义**：分析师和基金经理看重季度
4. **股票回购**：超预期可能引发回购

**"Whisper Number"（非官方预期）**：
- 分析师私下交流的"真实"预期
- 通常高于官方共识
- 实际值超 whisper number 才会大幅上涨
- 实际值超共识但低于 whisper number，股价可能下跌

**Beat 后股价未必涨的原因**：
- 数字超预期但指引下调
- "好消息已 Price In"
- 行业整体下跌拖累
- 利率或宏观因素

---

### 3. 管理层指引（Guidance）

#### 3.1 什么是 Guidance

**定义**：管理层指引是公司在财报中或投资者会议上对未来季度/年度业绩的官方预测。

**形式**：
- **具体数字**：收入 $X-Y 亿，EPS $A-B
- **定性描述**：增长"超 10%"、毛利率"改善"
- **范围**：通常给一个区间，如收入 $4.5-4.7B
- **隐含范围**：用一句话暗示范围

#### 3.2 指引种类

| 类型 | 英文 | 说明 |
|------|------|------|
| **季度指引** | Quarterly Guidance | 下一个季度的指引 |
| **年度指引** | Annual Guidance | 全年指引 |
| **中期指引** | Mid-term Guidance | 2-3 年指引 |
| **长期目标** | Long-term Target | 5 年以上战略目标 |
| **撤回指引** | Withdrawn Guidance | 公司不再给具体数字 |

#### 3.3 指引的策略

**保守指引（Low Guidance）**：
- 故意给低预期
- 容易 Beat
- 短期股价表现好
- 长期可信度下降

**激进指引（Stretch Guidance）**：
- 给高预期
- 容易 Miss
- 短期股价压力大
- 提升管理层可信度

**撤回指引（Pull Guidance）**：
- 不给具体数字
- 避免 Beat/Miss 文化
- 给管理层灵活性
- 失去分析师关注

**典型案例**：

| 公司 | 风格 | 表现 |
|------|------|------|
| **Apple** | 保守 | 经常 Beat |
| **Tesla** | 激进 | 经常 Miss 早期目标 |
| **Nvidia** | 灵活 | 不断上调 |
| **Meta** | 灵活 | 转向 AI 后强劲 |
| **Amazon** | 灵活 | 历史常撤回具体数字 |

---

### 4. 电话会议（Earnings Call）

#### 4.1 Earnings Call 结构

**两个阶段**：

| 阶段 | 时长 | 内容 |
|------|------|------|
| **管理层陈述** | 20-30 分钟 | CEO/CFO 汇报业绩 |
| **Q&A 环节** | 30-60 分钟 | 分析师提问 |

**参与者**：
- **CEO（首席执行官）**：战略、愿景
- **CFO（首席财务官）**：财务、指引
- **COO（首席运营官）**：业务运营
- **IR（投资者关系）**：组织协调

**准备 Earnings Preview 时的关注点**：
1. **预读脚本（Prepared Remarks）**：管理层陈述稿
2. **预读 slides**：补充材料
3. **历史 Q&A**：以往问答模式
4. **重点关注问题**：可能敏感的话题

#### 4.2 Q&A 常见问题类型

| 类型 | 示例 |
|------|------|
| **增长动力** | "增长由什么驱动？可持续吗？" |
| **利润率** | "毛利率趋势？何时改善？" |
| **指引** | "为什么指引比预期低/高？" |
| **运营指标** | "DAU 增长？用户参与度？" |
| **竞争格局** | "竞争对手的动作？" |
| **并购** | "战略并购计划？" |
| **资本配置** | "现金如何使用？回购？派息？" |
| **监管** | "监管影响？" |
| **汇率** | "汇率波动的影响？" |
| **一次性事件** | "为什么有重组费用？" |

#### 4.3 重要语调分析

**语调分析（Sentiment Analysis）**：
- 比文本字面意思更重要的，是"怎么说"
- 通过 AI 分析管理层的语调、措辞

**正面信号**：
- "Strong momentum"（强劲势头）
- "Exceed expectations"（超预期）
- "Record revenue"（创纪录收入）
- "Broad-based growth"（全面增长）

**负面信号**：
- "Headwinds"（逆风）
- "Challenging environment"（艰难环境）
- "Macro uncertainty"（宏观不确定）
- "Realignment"（重组）
- "Cost optimization"（成本优化）= 裁员

**中性词陷阱**：
- "Realignment" = 裁员
- "Right-sizing" = 裁员
- "Optimization" = 效率提升 / 裁员
- "Restructuring" = 重组 / 裁员
- "Strategic review" = 可能在卖

---

### 5. 财报关键指标详解

#### 5.1 收入指标

| 指标 | 英文 | 公式 | 含义 |
|------|------|------|------|
| **收入** | Revenue | 销售总额 | 营业活动产生的总流入 |
| **收入增长率** | Revenue Growth | (本期-上期)/上期 | YoY 增长 |
| **收入多元化** | Revenue Mix | 各业务/地区收入占比 | 收入来源分布 |
| **客户集中度** | Customer Concentration | Top N 客户收入占比 | 收入风险 |
| **ARR** | Annual Recurring Revenue | 订阅年化 | SaaS 关键 |
| **Bookings** | 订单金额 | 已签订单 | 未来收入领先指标 |
| **Backlog** | 积压订单 | 未交付订单 | 未来收入保障 |
| **RPO** | Remaining Performance Obligations | 未履行履约义务 | ASC 606 概念 |
| **Billings** | 账单金额 | 客户已开账单 | ARR 变种 |

#### 5.2 利润率指标

| 指标 | 英文 | 公式 | 优秀标准 |
|------|------|------|---------|
| **毛利率** | Gross Margin | (收入-COGS)/收入 | > 40%（软件） |
| **营业利润率** | Operating Margin | 营业利润/收入 | > 15% |
| **净利润率** | Net Margin | 净利润/收入 | > 10% |
| **EBITDA Margin** | EBITDA/收入 | 现金盈利能力 | > 20% |
| **FCF Margin** | FCF/收入 | 自由现金流率 | > 15% |
| **Gross Retention** | 毛利率留存 | 1-流失率 | > 90% |
| **Net Retention** | 净留存 | (起始+扩张-流失)/起始 | > 110% |

#### 5.3 EPS 详解

**定义**：Earnings Per Share，每股收益 = 净利润 / 加权平均流通股数。

**EPS 类型**：

| 类型 | 英文 | 公式 | 说明 |
|------|------|------|------|
| **基本 EPS** | Basic EPS | 净利润 / 基本流通股 | 不含潜在稀释 |
| **稀释 EPS** | Diluted EPS | 净利润 / 稀释流通股 | 含期权、RSU 等 |
| **调整后 EPS** | Adjusted EPS | 调整后净利润 / 股 | 剔除一次性项目 |
| **GAAP EPS** | GAAP EPS | 严格会计准则下 EPS | 法定标准 |
| **Non-GAAP EPS** | Non-GAAP EPS | 剔除股票薪酬等 | 公司常用 |

**为什么调整后 EPS 重要**：
- 剔除股票薪酬（SBC）、重组费用、减值等
- 反映"经营基本面"
- 公司偏好强调 Non-GAAP EPS
- 投资者需对比 GAAP 和 Non-GAAP

**典型调整项**：
- 股票薪酬（Stock-Based Compensation）
- 重组费用（Restructuring Charges）
- 减值损失（Impairment）
- 一次性诉讼费用
- 收购相关费用
- 汇兑损益

#### 5.4 自由现金流（FCF）

**定义**：Free Cash Flow，自由现金流 = 经营活动现金流 - 资本支出。

**公式**：
```
FCF = OCF - CapEx
   = (净利润 + D&A + 营运资本变动) - CapEx
```

**FCF 与净利润的区别**：
- 净利润：会计准则下的利润
- FCF：实际收到的现金
- 可能差异巨大（如 SaaS 公司递延收入）

**为什么 FCF 重要**：
- 不能操纵（现金为王）
- 反映真实盈利能力
- 可用于回购、派息、并购、研发

**FCF 收益率**：
```
FCF Yield = FCF / 市值
```

- < 3%：估值偏高
- 3-5%：合理
- 5-8%：低估
- > 8%：明显低估

---

### 6. 估值方法速查

#### 6.1 估值倍数

| 倍数 | 公式 | 适用 |
|------|------|------|
| **P/E** | 股价 / EPS | 盈利公司 |
| **EV/EBITDA** | 企业价值 / EBITDA | 通用 |
| **EV/Revenue** | 企业价值 / 收入 | SaaS、亏损公司 |
| **P/B** | 股价 / 每股净资产 | 银行、保险 |
| **P/S** | 股价 / 每股收入 | 亏损公司 |
| **PEG** | P/E / 增长率 | 高成长公司 |

**EV（企业价值）计算**：
```
EV = 市值 + 净债务 + 少数股东权益 + 优先股 - 现金
```

#### 6.2 各种估值场景

| 公司类型 | 首选方法 | 次选 |
|---------|---------|------|
| **成熟公司** | DCF + P/E | EV/EBITDA |
| **高成长 SaaS** | EV/Revenue | EV/ARR |
| **亏损科技公司** | EV/Revenue | DCF（远期） |
| **银行** | P/B | P/E + 股息率 |
| **房地产** | NAV（净资产价值） | P/B |
| **周期股** | EV/EBITDA（中位周期） | 资产重置价值 |
| **公用事业** | 股息率 + DCF | P/E |

#### 6.3 目标价的设定

**目标价（Target Price）**：
- 通常 12 个月目标价
- 基于估值方法（DCF、Comps、Precedents）
- 对应预期回报率

**目标价计算示例**（DCF）：
```
预测 5 年 FCF
计算 WACC（加权平均资本成本）
计算终值（永续增长假设）
折现求和
= 内在价值
÷ 流通股数
= 每股价值（目标价）
```

**目标价计算示例**（相对估值）：
```
预测 NTM EPS
行业平均 P/E
目标价 = NTM EPS × 行业 P/E
```

#### 6.4 投资评级体系

**标准评级**（3 档）：

| 评级 | 英文 | 预期回报 |
|------|------|---------|
| **Buy / Outperform** | 买入 | > 15% |
| **Hold / Neutral** | 持有 | -10% ~ +15% |
| **Sell / Underperform** | 卖出 | < -10% |

**部分机构用 5 档**：
- Strong Buy（强烈买入）
- Buy
- Hold
- Sell
- Strong Sell

**评级分布规则**（MiFID II 后）：
- 投行需公布评级分布
- Buy 占比过高可能有问题
- 典型：40-50% Buy / 40-50% Hold / 5-15% Sell

---

### 7. HTML 报告设计详解

#### 7.1 报告设计原则

**本模板的设计目标**：
- 单页 4-5 个打印页
- 屏幕显示和打印都友好
- 内嵌 CSS，无需外部资源（除 Chart.js CDN）
- 响应式布局

**金融报告的设计黄金法则**：

| 法则 | 说明 |
|------|------|
| **简洁专业** | 配色克制（深蓝、灰、白） |
| **数据为王** | 图表大于文字 |
| **可读性** | 关键数字加粗、颜色突出 |
| **品牌一致** | 统一的字体、配色、布局 |
| **打印友好** | `@media print` 样式 |
| **响应式** | 桌面、平板、手机都可用 |

#### 7.2 金融报告常用配色

**标准投行配色**：

| 主色 | 辅色 | 强调色 | 警示色 |
|------|------|--------|--------|
| 深蓝 #003366 | 灰 #666666 | 绿 #00A651 | 红 #C8102E |
| 高盛金 #7399C6 | 白 #FFFFFF | 金 #FFB81C | 警示 #DC3545 |
| 摩根蓝 #012169 | 浅蓝 #A0B6D6 | 绿 #008C00 | 红 #B22222 |

**S&P Global 配色**（本模板）：
- 主色：#1a1a2e（深蓝）
- 辅色：#1a1a4e
- 中性：#555, #333, #222

#### 7.3 Chart.js 使用技巧

**Chart.js** 是金融报告最常用的图表库：

| 图表类型 | 适用场景 |
|---------|---------|
| **折线图（Line）** | 趋势变化（收入、股价） |
| **柱状图（Bar）** | 类别对比（部门收入） |
| **饼图（Pie）** | 占比（业务分布） |
| **散点图（Scatter）** | 相关性分析 |
| **雷达图（Radar）** | 多维度对比 |
| **混合图（Mixed）** | 柱状+折线（收入+利润率） |

**关键配置**：

```javascript
new Chart(ctx, {
  type: 'line',  // 图表类型
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [{
      label: 'Revenue',
      data: [100, 120, 140, 160],
      borderColor: '#1a1a4e',
      backgroundColor: 'rgba(26, 26, 78, 0.1)',
      tension: 0.3
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Quarterly Revenue' }
    }
  }
});
```

#### 7.4 打印优化

**`@media print` 样式**：

```css
@media print {
  /* 隐藏导航、不必要元素 */
  .no-print { display: none; }
  
  /* 调整字体 */
  body { font-size: 11pt; }
  
  /* 强制分页 */
  .page-break { page-break-before: always; }
  
  /* 避免分页切断表格 */
  table { page-break-inside: avoid; }
  
  /* 打印背景色（Chrome） */
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
```

**打印考虑**：
- 避免元素被分页切断
- 重要内容放在页内（"orphan/widow control"）
- 隐藏交互元素
- 黑白打印也能识别（颜色 + 文字）
- 节省墨水（浅色背景）

---

### 8. 数据可视化最佳实践

#### 8.1 选择正确的图表

| 数据关系 | 推荐图表 |
|---------|---------|
| **时间趋势** | 折线图 |
| **类别对比** | 柱状图 |
| **占比** | 饼图（≤5 类）/ 堆叠柱状图（>5 类） |
| **分布** | 直方图、箱线图 |
| **相关性** | 散点图 |
| **地理** | 地图 |
| **层级** | 树图、旭日图 |
| **流程** | 桑基图 |

#### 8.2 数据可视化的"坑"

| 常见错误 | 后果 |
|---------|------|
| **Y 轴不从 0 开始** | 差异被放大，误导 |
| **3D 效果** | 扭曲数据感知 |
| **颜色过多** | 难以分辨 |
| **缺失标签** | 数据点无法理解 |
| **饼图太多类** | 难以识别小块 |
| **柱状图太多类** | 视觉杂乱 |
| **双 Y 轴** | 容易误导 |
| **隐藏数据点** | 选择性展示 |

#### 8.3 金融图表常用模式

**Waterfall Chart（瀑布图）**：
- 收入 → 各成本 → 利润的拆解
- 直观展示利润来源

**Stacked Bar（堆叠柱）**：
- 各业务收入贡献
- 总收入 + 结构变化

**Combo Chart（混合图）**：
- 柱状图（收入）+ 折线（利润率）
- 绝对值 + 比率

**Heatmap（热力图）**：
- 多维度对比
- 行业 vs 公司的多指标

**Sparkline（迷你图）**：
- 趋势速览
- 嵌入表格中

---

### 9. 卖方研究分析师的一天

#### 9.1 财报季特别忙

**财报季（Earnings Season）**：
- 1月、4月、7月、10月
- 3-4 周内发布数百份财报
- 分析师工作强度翻倍

**分析师财报季时间表**：

| 时间 | 任务 |
|------|------|
| **财报前 1-2 周** | 撰写 Earnings Preview |
| **财报前 1 天** | 最后准备，整理 checklist |
| **财报日** | 听电话会议，整理要点 |
| **财报日 24h 内** | 发布 Earnings Review |
| **财报后 1 周** | 更新模型，调整预测 |
| **财报后 1 月** | 下一个迭代 |

#### 9.2 Earnings Call 准备清单

**财报前 1 天**：
- [ ] 预读脚本
- [ ] 预读 slides
- [ ] 重温上次电话会议
- [ ] 检查一致预期变化
- [ ] 准备 5-10 个关键问题
- [ ] 检查是否有时点事件（疫情、地缘政治）

**财报日**：
- [ ] 听电话会议（8:00 AM PT 常见）
- [ ] 实时记录要点
- [ ] 注意语调变化
- [ ] 整理 Q&A 重点
- [ ] 立即发布 Flash Note

**财报后**：
- [ ] 详细分析财报数据
- [ ] 对比实际 vs 预期
- [ ] 更新财务模型
- [ ] 撰写完整 Earnings Review
- [ ] 调整评级/目标价

---

### 10. 风险因素分类

#### 10.1 财报分析中的常见风险

| 风险类型 | 说明 | 影响 |
|---------|------|------|
| **指引风险** | 指引下调 | 股价通常下跌 |
| **Margin 风险** | 毛利率/营业利润率不及预期 | 利润压力 |
| **指引撤回** | 不再给具体数字 | 失去分析师信任 |
| **一次性事件** | 重组、减值、诉讼 | 需调整分析 |
| **汇率风险** | 美元强势影响海外收入 | 收入被压缩 |
| **宏观风险** | 经济衰退、消费疲软 | 行业整体下滑 |
| **监管风险** | 反垄断、数据隐私 | 合规成本上升 |
| **供应链** | 芯片短缺、原料涨价 | 成本上升 |
| **人才流失** | 关键高管离职 | 战略不确定性 |

#### 10.2 风险评估框架

**风险概率 × 影响矩阵**：

| 概率 \\ 影响 | 低 | 中 | 高 |
|-------------|----|----|-----|
| **高** | 关注 | 警告 | 灾难 |
| **中** | 监控 | 关注 | 警告 |
| **低** | 忽略 | 监控 | 关注 |

#### 10.3 财报中的"红旗"信号

**财务造假信号**（"Red Flags"）：

| 信号 | 含义 |
|------|------|
| 应收账款增长 > 收入增长 | 可能在虚增收入 |
| 库存增长 > 收入增长 | 销售可能有问题 |
| 经营现金流远低于净利润 | 利润可能不可持续 |
| 频繁更换审计师 | 可能有争议 |
| 高管集中抛售 | 内部人信心不足 |
| 关联交易复杂 | 可能有利益输送 |
| 持续"一次性"费用 | 调整利润的嫌疑 |
| 收入确认激进 | 提前确认收入 |

---

### 11. 行业研究框架

#### 11.1 行业分析维度

**波特五力（Porter's Five Forces）**：

| 力量 | 内容 |
|------|------|
| **同业竞争** | 现有公司之间的竞争 |
| **新进入者** | 新公司进入的威胁 |
| **替代品** | 替代产品/服务的威胁 |
| **供应商议价** | 上游供应商的力量 |
| **客户议价** | 下游客户的力量 |

**PESTEL 分析**：

| 维度 | 含义 |
|------|------|
| **P**olitical | 政治因素 |
| **E**conomic | 经济因素 |
| **S**ocial | 社会因素 |
| **T**echnological | 技术因素 |
| **E**nvironmental | 环境因素 |
| **L**egal | 法律因素 |

#### 11.2 TAM/SAM/SOM

| 概念 | 英文 | 含义 |
|------|------|------|
| **TAM** | Total Addressable Market | 总潜在市场 |
| **SAM** | Serviceable Addressable Market | 可服务市场 |
| **SOM** | Serviceable Obtainable Market | 实际可获得市场 |

**示例**（Salesforce）：
- TAM：$1T（全球企业软件）
- SAM：$80B（CRM 市场）
- SOM：$40B（3 年内可达）

---

### 12. 重要监管机构

| 地区 | 机构 | 英文 | 职责 |
|------|------|------|------|
| **美国** | SEC | Securities and Exchange Commission | 证券监管 |
| **美国** | FINRA | Financial Industry Regulatory Authority | 券商监管 |
| **美国** | FASB | Financial Accounting Standards Board | 会计准则 |
| **英国** | FCA | Financial Conduct Authority | 金融行为监管 |
| **欧盟** | ESMA | European Securities and Markets Authority | 证券监管 |
| **中国** | CSRC | China Securities Regulatory Commission | 证监会 |
| **中国** | PCAOB | Public Company Accounting Oversight Board | 上市公司会计监督 |
| **国际** | IOSCO | International Organization of Securities Commissions | 国际证监会 |

---

### 13. 财务报表勾稽关系

#### 13.1 三大报表的勾稽

**关键等式**：

```
资产 = 负债 + 股东权益

净利润 = 期初留存收益 + 净利 - 分红

经营现金流 + 投资现金流 + 融资现金流 = 现金净变动

期末现金 = 期初现金 + 现金净变动
```

#### 13.2 常见会计科目

**资产负债表**：

| 类别 | 科目 |
|------|------|
| **流动资产** | 现金、应收账款、存货、预付费用 |
| **非流动资产** | PP&E、商誉、无形资产、长期投资 |
| **流动负债** | 应付账款、短期借款、预收账款 |
| **非流动负债** | 长期借款、债券 |
| **股东权益** | 股本、资本公积、留存收益 |

**利润表**：

| 类别 | 科目 |
|------|------|
| **收入** | 产品收入、服务收入 |
| **成本** | COGS、毛利 |
| **营业费用** | 销售费用、管理费用、研发费用 |
| **非经营** | 利息收入、利息支出、投资收益 |
| **税收** | 所得税 |
| **净利润** | 最终利润 |

**现金流量表**：

| 类别 | 科目 |
|------|------|
| **经营** | 净利润 + D&A + 营运资本变动 |
| **投资** | CapEx、并购、证券投资 |
| **融资** | 借款、还款、回购、派息、发行股票 |

---

### 14. 关键术语速查

| 中文 | 英文 | 缩写 | 解释 |
|------|------|------|------|
| 财报 | Earnings Report | - | 公司定期披露的财务报告 |
| 季度财报 | Quarterly Report | 10-Q | 美国 SEC 季度财报 |
| 年度财报 | Annual Report | 10-K | 美国 SEC 年度财报 |
| 即时披露 | Current Report | 8-K | 重大事件即时披露 |
| 业绩预览 | Earnings Preview | EP | 财报前预告性研报 |
| 业绩回顾 | Earnings Review | ER | 财报后实际点评 |
| 业绩超预期 | Beat | - | 实际 > 预期 |
| 业绩不及预期 | Miss | - | 实际 < 预期 |
| 符合预期 | In-line | - | 实际 ≈ 预期 |
| 共识预期 | Consensus Estimates | - | 分析师预测中位数 |
| 管理层指引 | Management Guidance | - | 公司对未来业绩的预测 |
| 电话会议 | Earnings Call | - | 财报后管理层与分析师沟通 |
| 目标价 | Target Price | - | 12 个月预期价格 |
| 投资评级 | Rating | - | Buy/Hold/Sell |
| 每股收益 | Earnings Per Share | EPS | 净利润 / 流通股 |
| 自由现金流 | Free Cash Flow | FCF | 经营现金流 - CapEx |
| 资本支出 | Capital Expenditure | CapEx | 购买长期资产支出 |
| 企业价值 | Enterprise Value | EV | 买下整个公司的价格 |
| 净债务 | Net Debt | - | 总债务 - 现金 |
| 摊销折旧 | Depreciation & Amortization | D&A | 非现金费用 |
| 营业利润 | Operating Income | - | 主营业务利润 |
| 净利润 | Net Income | - | 最终利润 |
| 毛利率 | Gross Margin | - | (收入-COGS)/收入 |
| 营业利润率 | Operating Margin | - | 营业利润/收入 |
| 净利润率 | Net Margin | - | 净利润/收入 |
| 调整后 | Adjusted | - | 剔除一次性项目 |
| 非 GAAP | Non-GAAP | - | 不严格按 GAAP |
| 预读脚本 | Prepared Remarks | - | 管理层电话会议稿 |
| Q&A 环节 | Question & Answer | Q&A | 问答环节 |
| 投资者关系 | Investor Relations | IR | 公司与投资者沟通 |
| 卖方研究 | Sell-side Research | - | 投行研究 |
| 买方研究 | Buy-side Research | - | 资管内部研究 |
| 首次覆盖 | Initiation of Coverage | - | 首次发布研报 |
| 升级 | Upgrade | - | 评级上调 |
| 降级 | Downgrade | - | 评级下调 |
| 报告期 | Reporting Period | - | 财报对应期间 |
| 静默期 | Quiet Period | - | 财报前不能公开宣传 |
| 禁售期 | Blackout Period | - | 高管不能交易 |
| 留存收益 | Retained Earnings | - | 累计未分配利润 |
| 营运资本 | Working Capital | - | 流动资产 - 流动负债 |
| 递延收入 | Deferred Revenue | - | 预收但未确认收入 |
| 股票薪酬 | Stock-Based Compensation | SBC | 用股票支付员工 |
| 一次性损益 | One-time Charge | - | 非经常性项目 |
| 重组费用 | Restructuring Charge | - | 裁员、整合等费用 |
| 商誉 | Goodwill | - | 并购溢价 |
| 无形资产 | Intangible Assets | - | 专利、品牌等 |
| 库存 | Inventory | - | 原材料、在制品、成品 |
| 应收账款 | Accounts Receivable | AR | 客户欠款 |
| 应付账款 | Accounts Payable | AP | 欠供应商的款 |
| 长期债务 | Long-term Debt | - | 1 年以上债务 |
| 短期债务 | Short-term Debt | - | 1 年内债务 |
| 股息 | Dividend | - | 派发给股东的现金 |
| 股票回购 | Share Buyback | - | 公司回购自己的股票 |
| 股权稀释 | Dilution | - | 每股权益被摊薄 |
| 同行 | Peers | - | 同行业可比公司 |
| 周期性 | Cyclical | - | 随经济周期波动 |
| 防御性 | Defensive | - | 抗周期 |

---

> **提示**：本附录覆盖了财报分析、Earnings Preview 方法论、管理层指引分析、电话会议准备、HTML 报告设计等核心知识，是金融分析师、投行人员和投资者学习 earnings season 的系统化参考。

---

## Appendix: 金融背景知识

这份文件是"财报预览报告模板（Earnings Preview Report Template）"的详细说明。在股权研究中，财报预览（Earnings Preview）是在公司发布财报前撰写的预测报告——它帮助客户在"大考前"做好心理准备。

---

### 1. 什么是 Earnings Preview 报告？

**类比：**
想象你是一家车队的"赛前分析师"。本周末有一场重大赛事，你需要在赛前给车队经理一份报告：对手车手的状态、赛道条件、我们车手的胜算、值得注意的风险点。

Earnings Preview 报告就是金融世界的"赛前分析"——在财报发布前告诉客户"我们预计这家公司会交出什么样的成绩单，你应该在财报前做好什么准备"。

---

### 2. 财报预览报告的"标准结构"

| 章节 | 内容 | 读者最关心的问题 |
|------|------|----------------|
| 核心预测 | 收入/EPS/关键指标预测 vs 共识 | Beat 还是 Miss？ |
| 关键假设 | 预测的前提条件 | 你的预测靠谱吗？ |
| 需要关注的焦点 | 毛利率、指引、新业务 | 什么最关键？ |
| 情景分析 | 熊市/基准/牛市三种情景 | 最好和最坏情况？ |
| 风险提示 | 可能出问题的地方 | 有什么需要注意的？ |

---

### 3. 预测 vs 共识：市场反应矩阵

| 实际 vs 共识 | 股价短期反应 | 中长期反应 |
|-------------|------------|-----------|
| Beat 显著（>10%） | 大涨 5-10% | 看指引 |
| Beat 轻微（2-5%） | 微涨 1-3% | 看指引 |
| In Line | 波动不大 | 看指引 |
| Miss 轻微（2-5%） | 微跌 1-3% | 看原因 |
| Miss 显著（>10%） | 大跌 5-10% | 大风险 |

**关键洞察**：股价短期反应由"实际 vs 预期"决定，但中长期走势由"管理层指引"决定——如果 Beat 但指引下调，股价可能先涨后跌。

---

### 4. 三种情景分析的"标准格式"

| 情景 | 假设 | 收入 | EPS | 概率 |
|------|------|------|-----|------|
| 牛市 | 新市场突破、份额大幅增长 | $1.5B | $1.20 | 20% |
| 基准 | 正常增长、团队稳定 | $1.2B | $0.85 | 60% |
| 熊市 | 竞争加剧、成本上升 | $1.0B | $0.60 | 20% |

**加权平均**：$1.5B×20% + $1.2B×60% + $1.0B×20% = $1.22B

---

### 5. 真实案例：一篇优秀的 Earnings Preview

**公司**：某科技公司，即将发布 Q3 财报

**报告核心内容**：

> **核心预测**：收入 $2.5B（vs consensus $2.45B，Beat 2%）。EPS $0.55（vs consensus $0.52，Beat 6%）。
>
> **关键假设**：
> - 大中华区收入增长 15%（vs 上季度 10%）——基于渠道调研证实
> - 毛利率改善 50bps 至 42.5%——受益于规模效应
>
> **需要关注的焦点**：
> 1. 管理层对 Q4 的指引——市场预期 $2.7B
> 2. 印度市场进展——管理层是否提及
> 3. 新产品的客户反馈
>
> **建议**：财报前轻仓做多，如果指引超预期再加仓

---

### 给小白的一句话

> Earnings Preview 报告就是金融分析师给客户写的"考前预测卷"——在考试成绩（财报）揭晓前，你根据自己的调查和分析，预测公司能考多少分。最重要的是要说明"你为什么这样预测"（你的假设是什么），这样客户才能判断你的预测靠不靠谱。好的 Preview 报告要做到三点：第一，给出具体的数字预测而不是"估计会增长"；第二，说明你的假设（增长是基于什么）；第三，告诉客户"如果结果比预期好怎么办，如果比预期差怎么办"。
