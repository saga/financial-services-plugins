---
description: 搭建兼并收购模型 (用于评估 增厚/摊薄效应 - Accretion/Dilution)
argument-hint: "[买方公司] 收购 [目标公司]"
---

加载 `merger-model` (并购模型) 技能模块，以建立合并后果分析 (Merger consequences analysis) 的测算。

如果用户在参数中提供了买方 (Acquirer) 和目标方 (Target)，请直接代入；否则请主动询问用户具体的交易细节假设。

---

> **💡 Appendix: 领域知识小贴士**
>
> 1. **Merger Model (并购模型/M&A模型)**：用于模拟两家公司“领完结婚证”后未来的财务表现。相当于把两张单独的财务报表加在一起，还要算上由于收购而产生的新借款利息和新发行的股票。
> 2. **Accretion / Dilution (增厚效应 / 摊薄效应)**：这是评价一笔上市公司的收购案“划不划算”的最关键指标。如果买完这家新公司后，买方自己明年的 EPS (每股收益) 比不买的时候还要高，就叫 Accretion (增厚，好交易)；如果跌了，就叫 Dilution (摊薄，会被持股股东骂死)。
> 3. **Acquirer vs Target**：Acquirer (买方/收购方)，是主动出击并愿意掏钱的一方；Target (卖方/标的公司)，是被挂牌出售或被“恶意收购”的一方。
