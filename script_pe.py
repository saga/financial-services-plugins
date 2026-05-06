import os

files = {
    "中文版May06/plugins/vertical-plugins/private-equity/commands/portfolio.md": """---
description: 回顾并审查已投标的公司的近期财务健康度表现 (Portfolio Monitoring)
argument-hint: "[输入公司名称或公司月度/季度发来的经营报表路径]"
---

加载 `portfolio-monitoring` (投后监测) 技能模块，分析基金持股公司的业绩是否跟上了当年拿钱时的业务规划（Business Plan）。重点分析核心痛点 KPI，计算业绩的偏离差值 (Variances) 并亮出潜在的亏损风险预警弹。

如果用户没有提供公司名称或报表数据，请主动索取。

---
> **💡 Appendix: 领域知识小贴士**
> 1. **Portfolio Monitoring (投后管理/投后监测)**: 买完公司不代表结束。每个月基金公司的财务团队都会死盯着这些被投企业的报表，看他们有没有按时完成对赌、钱有没有乱花。
> 2. **Variances (偏差/差异值)**: 实际赚的钱和原本在 Excel 模型里答应应该赚到的预算之间的差额。Variance Analysis 是每个月最令所投公司 CFO 头秃的对账分析。
""",

    "中文版May06/plugins/vertical-plugins/private-equity/commands/returns.md": """---
description: 构建内部收益率 (IRR) 及资本回报倍数 (MOIC) 敏感性分析测算表
argument-hint: "[输入公司参数名或具体交易金额参数]"
---

加载 `returns-analysis` (回报分析) 技能模块。针对不同极端的剧本建立私募股权回报矩阵，变量维度需包含：入场时的初始估值溢价倍数 (Entry multiple)、借债杠杆使用量 (Leverage)、几年后离场的套现卖出估值倍数 (Exit multiple) 以及内生的业务增长假设。

如果用户没有提供这些核心交易假定，请主动询问其设定的买入价、杠杆比例和预期退出年份。

---
> **💡 Appendix: 领域知识小贴士**
> 1. **Sensitivity Tables (敏感性分析表)**: 是一个类似于九九乘法表的二维矩阵展示图。横轴假设如果用 15倍 或 10倍 的价格去买，竖轴假设借银行 10个亿 还是只借 2个亿杠杆，交叉格子里的百分比就会自动算出这种组合情况下对应的每年能赚多少利息 (IRR)。能帮助大佬们在几秒内一目了然看清利润天花板和回本生死线。
""",

    "中文版May06/plugins/vertical-plugins/private-equity/commands/screen-deal.md": """---
description: 快速初筛外发或送上门的项目推介材料 (Inbound Deal Screening)
argument-hint: "[输入对方发来的 CIM 或 Teaser 文件的路径]"
---

加载 `deal-screening` (项目初筛) 技能模块，极速阅读外部上门寻求融资的项目文件。并在第一眼阶段无情地套用本基金的偏好筛选底线 (Investment criteria) 标出其是否值得进入下一步论证。

如果用户没有提供文件路径，请让其上传待筛选的推介材料。

---
> **💡 Appendix: 领域知识小贴士**
> 1. **Inbound Deal (案源送上门/被动接收交易)**: 知名基金每天邮箱能收到无数投行塞过来的希望被并购的“卖身契”邮件。分析师最初的一项脏活累活就是在一分钟内判断这些邮件是不是垃圾邮件。如果这标的跟自家基金看管的战略行业毫无干系，就会直接 Pass 跳过，这道第一道门槛动作被称为 Screen。
""",

    "中文版May06/plugins/vertical-plugins/private-equity/commands/source.md": """---
description: 搜寻标的项目池资源并草拟外拓搭讪信 (Deal Sourcing & Outreach)
argument-hint: "[填入标的画像，例如 '德州地区收入规模在 10M-50M 的工业服务平台企业']"
---

加载 `deal-sourcing` (项目挖掘) 获取源头的项目捕捉模块流程：扫描市场并找到水下的潜在标的企业；翻阅 CRM 以确认是否有过往的历史拜访脉络关联；自动草拟个性化且高度针对性的冷启动套磁私信给对方公司合伙人或创始人开展邀约 (Founder outreach emails)。

---
> **💡 Appendix: 领域知识小贴士**
> 1. **Deal Sourcing (项目发掘/找案源)**: 不只是被动等着投行的推介资料，那些最赚钱和最低廉的绝佳收购，往往都是靠私募内部的分析专员每天自己按标签查公司电话，然后用 LinkedIn 冷启动私信主动寻访得来的。
""",

    "中文版May06/plugins/vertical-plugins/private-equity/commands/unit-economics.md": """---
description: 分析深层次单位经济效益与客户留存 (Unit Economics)
argument-hint: "[输入公司名称或大数据的提取路径]"
---

加载 `unit-economics` (单位经济效益) 模块。深度还原透视公司底层客户漏斗的盈利面相：包含年度经常性收入的不同批次同期群分层追踪 (ARR cohorts)、客户全生命周期价值对赌初始获客成本的倍数极值 (LTV/CAC ratio)、绝对流失重筛与净营收留存率 (Net retention) 以及最终的收入质量 (Revenue quality)。

---
> **💡 Appendix: 领域知识小贴士**
> 1. **Unit Economics / UE (单位经济效益 / 单客模型)**: 从大势上看一家互联网公司总体可能在亏钱，但单算获取并服务好“每一个单独的散户”，在这个独立的闭环内赚的钱能否覆盖他背后的拉新营销花销 (即 LTV > CAC)。只要这个单人模型永远能跑通，那就意味只要不停往里面无脑灌钱砸广告拉人，未来规模化后就能产生巨额净利润。
> 2. **Cohorts (同期群分析/留存分析)**: 指那些“在去年同一月份段内”被吸引进来的客户，随着时间推移，这波人两年后还有多少人留下来保持续订。这是扒下 SaaS 型公司华丽外衣的最凶狠利器。
""",

    "中文版May06/plugins/vertical-plugins/private-equity/commands/value-creation.md": """---
description: 构建投后整合与价值提升规划路线图 (Value Creation Plan)
argument-hint: "[输入被投公司之名称]"
---

加载 `value-creation-plan` (价值创造规划) 模块，在收购打款落定的同时，即刻建立起一套提升重组的干预路线图：梳理利润率强提增项清单搭成拆桥矩阵 (EBITDA bridge)，罗列入驻接管后的新官上任头一百天急救执行清单 (100-day plan)，并设计配套的高频执行看板监控 (KPI dashboard)。

---
> **💡 Appendix: 领域知识小贴士**
> 1. **Value Creation Plan / VCP (投后价值提升/价值创造路线)**: 对于私募老鸟而言，已经是好公司的标的是不配产生多少超额倍数收益的。PE 的核心做法是买一家的有着重组拯救空间的脏公司或笨公司，进去后派上自己一帮前咨询背景的干预专员，砍掉冗余成本，重写制度，这就叫“投后赋能及价值重塑”。
> 2. **100-day Plan (投后百日行动计划)**: 被视为接管期最重要的摩擦攻坚期窗口。百日内的强行结构合并与人员洗牌是最黄金的操作期。
"""
}

for p, c in files.items():
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(c.strip() + "\n")
print("Done fixing PE remaining files.")
