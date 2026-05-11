# 任务 2：财务建模 - 详细工作流程

此文件为执行“首次覆盖研究（initiating-coverage）”技能中的任务 2（财务建模）提供分步指导。

## 任务概述

**目的**：提取历史财务数据，并构建包含预测和情景分析的全面 Excel 财务模型。

**前提条件**：⚠️ 开始前请核实
- **必要条件**：获取公司财务数据的权限
  - 上市公司：通过 SEC EDGAR 获取最新的 10-K 和近期的 10-Q 报告
  - 私营公司：从可用渠道获取财务报表或估算值
  - 或者：用户提供的已提取的历史财务数据
- **可选条件**：任务 1（公司研究）提供的业务背景信息

**输出**：包含 6 个核心工作表的 Excel 财务模型 (.xlsx)：
1. 营收模型 (Revenue Model)
2. 利润表 (Income Statement)
3. 现金流量表 (Cash Flow Statement)
4. 资产负债表 (Balance Sheet)
5. 情景分析 (Scenarios)
6. DCF 输入 (DCF Inputs)

---

## 输入核实

**在开始之前，请检查：**

**选项 A：直接提取财务数据（最常见）**
- [ ] 是否有权访问 10-K 申报文件（上市公司）？
- [ ] 或者是否有权访问财务报表（私营公司）？
- [ ] 是否已准备好用于历史数据提取的 Excel 文件？

**选项 B：用户已有预先提取的财务数据**
- [ ] 是否已提供历史财务文件？（.xlsx 或其他格式）
- [ ] 是否包含 3-5 年的利润表、现金流量表和资产负债表？
- [ ] 数据是否干净且可直接使用？

**可选背景：**
- [ ] 是否已完成任务 1（公司研究）以理解业务？

**如果核实失败**：请在继续操作前停止，并获取财务报表（10-K 或同等文件）的访问权限。

---

## 模型结构与格式规范

### 颜色编码（行业标准）
- **蓝色文本**：硬编码输入（用户可更改的数值）
- **黑色文本**：公式与计算结果
- **绿色文本**：跨表链接（链接至其他工作表）
- **红色文本**：错误或警告标记（需解决）

### 格式标准
- 专业的边框与阴影美化
- 清晰的各部分标题
- 设置行组（Grouped rows）以便折叠查看
- 为关键输入/输出定义命名区域（Named ranges）
- 公式中不得含有硬编码数字（常数如“12个月”除外）
- 明确的单位标注（千美元、百万美元等）

### 公式最佳实践
- 所有数字应从假设中流转得出
- 更改一个假设 → 整个模型随之更新
- 严禁循环引用
- 为关键单元格使用命名区域
- 保持公式简洁且易于审计
- 为复杂的计算添加注释

---

## 财务建模分步流程

### 第 1 步：提取历史财务数据

**如果历史财务数据已提取，请跳至第 2 步。**

**针对上市公司：**

1. **下载 10-K 文件**
   - 访问 SEC EDGAR (https://www.sec.gov/edgar/searchedgar/companysearch.html)
   - 搜索公司名称或股票代码
   - 下载最新的 10-K（年度报告）
   - 浏览至“Item 8：财务报表及补充数据”

2. **创建历史财务数据 Excel 文件**
   - 文件名：`[公司名]_Historical_Financials_[日期].xlsx`
   - 此文件将作为模型的基础

3. **提取利润表 (3-5 年)**
   - 创建工作表 1："Historical Income Statement"
   - 提取 3-5 年的所有明细行：
     - 营业收入（总额，以及若有披露的分板块收入）
     - 营业成本 / 销售成本 (COGS)
     - 毛利
     - 营业费用（研发、销售与市场、管理费用需拆分）
     - EBITDA（若未披露则计算：EBIT + 折旧摊销）
     - EBIT / 营业利润
     - 利息费用/收入
     - 其他收入/费用
     - 税前利润
     - 所得税及税率
     - 净利润
     - 每股收益 EPS（基本和稀释）
     - 发行在外股份数（基本和稀释）

4. **提取现金流量表 (3-5 年)**
   - 创建工作表 2："Historical Cash Flow"
   - 提取所有明细行：
     - 经营活动（从净利润开始）
     - 折旧与摊销
     - 股权激励费用 (SBC)
     - 营运资本变动（应收账款、存货、应付账款）
     - 经营活动现金流
     - 投资活动（资本支出 CapEx、收购）
     - 筹资活动（债务发行/偿还、股权、股利）
     - 现金净变动
     - 期初和期末现金

5. **提取资产负债表 (3-5 年)**
   - 创建工作表 3："Historical Balance Sheet"
   - 提取所有明细行：
     - 流动资产（现金、应收账款、存货、其他）
     - 非流动资产（固定资产 PP&E、无形资产、商誉）
     - 资产总计
     - 流动负债（应付账款、应计费用、短期债务）
     - 非流动负债（长期债务、递延所得税）
     - 负债合计
     - 股东权益（普通股、留存收益）
     - 负债及权益总计

6. **计算历史财务指标**
   - 创建工作表 4："Historical Metrics"
   - 根据报表计算：
     - 营收增长率 % (YoY)
     - 毛利率 %
     - EBITDA 利润率 %
     - 营业利润率 %
     - 净利率 %
     - 自由现金流 (CFO - CapEx)
     - FCF 利润率 %
     - 投资资本回报率 ROIC（近似值：NOPAT / 投资资本）
     - 产权比率 (Debt/Equity)
     - 流动比率 (流动资产 / 流动负债)

7. **记录数据来源与注释**
   - 创建工作表 5："Notes"
   - 记录：
     - 10-K 申报日期及财政年度截止日
     - 记录任何一次性数值或调整项
     - 非通用会计准则 (Non-GAAP) 与通用会计准则 (GAAP) 的差异
     - 分部明细（若收入按产品/地理位置拆分）
     - 数据质量说明及局限性

**针对私营公司：**

1. **收集可用数据**
   - 财务报表（若可用）
   - 包含营收数字的新闻稿
   - 融资公告
   - 行业估算值或可比公司数据

2. **创建简化的历史文件**
   - 估算的营收（若可用）
   - 估算的利润率（必要时参考可比公司）
   - 关键比率和指标
   - 记录所有假设和来源

**核实：**
- [ ] 已提取全部 3 张财务报表 (3-5 年)
- [ ] 各表数字勾稽一致（如净利润在三表间匹配）
- [ ] 关键指标计算准确
- [ ] Excel 文件已保存且可打开
- [ ] 数据来源已记录（10-K 日期、页码）

**预测模型的基础现已夯实。请继续执行第 2 步。**
   - 资本支出
   - 营运资本项
   - 债务与利息费用
   - 股份总数（基本和稀释）

3. **整理待录入的历史数据**
   - 准备 3-5 年的实际值 (Actuals)
   - 将直接录入利润表、现金流量表和资产负债表工作表
   - 历史年份置于前列，预测年份紧随其后

4. **计算历史趋势**
   - 营收复合增长率 (CAGR)
   - 利润率演变趋势
   - 营业费用杠杆效应
   - 营运资本模式
   - 资本支出占营收比例
   - 这些趋势将为预测假设提供参考

**注意**：假设将以蓝色文本直接记录在每个工作表中，而非设置单独的假设表。

### 第 2 步：营收建模

**核心要点：这是模型中最重要且最详尽的部分。**

#### A. 按产品/类别划分的营收 (20-30 行)

创建详细表格：
```
                        2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E
产品类别 A
  子产品 A1             XX      XX      XX      XX      XX      XX      XX      XX      XX
  子产品 A2             XX      XX      XX      XX      XX      XX      XX      XX      XX
  子产品 A3             XX      XX      XX      XX      XX      XX      XX      XX      XX
  类别 A 合计           XX      XX      XX      XX      XX      XX      XX      XX      XX
  占总营收比例          X%      X%      X%      X%      X%      X%      X%      X%      X%
  同比增长 %            -       X%      X%      X%      X%      X%      X%      X%      X%

产品类别 B
  [结构同上]

[继续输入所有产品类别]

服务收入                XX      XX      XX      XX      XX      XX      XX      XX      XX
其他收入                XX      XX      XX      XX      XX      XX      XX      XX      XX

总营收                  XX      XX      XX      XX      XX      XX      XX      XX      XX
总营收增长率 %          -       X%      X%      X%      X%      X%      X%      X%      X%
```

**关键要求：**
- 显示每个类别的绝对收入 (百万美元)
- 计算每个类别占总营收的百分比
- 显示每个类别的同比增长 % (YoY)
- 必须包含细化的子类别（而非仅 3-5 个顶级类别）
- 展示随时间推移的收入构成变化
- 将所有预测值链接至假设项

#### B. 按地理区域划分的营收 (15-20 行)

创建详细表格：
```
                        2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E
北美洲
  美国                  XX      XX      XX      XX      XX      XX      XX      XX      XX
  加拿大                XX      XX      XX      XX      XX      XX      XX      XX      XX
  墨西哥                XX      XX      XX      XX      XX      XX      XX      XX      XX
  北美合计              XX      XX      XX      XX      XX      XX      XX      XX      XX
  占总额比例            X%      X%      X%      X%      X%      X%      X%      X%      X%
  同比增长 %            -       X%      X%      X%      X%      X%      X%      X%      X%

欧洲
  英国                  XX      XX      XX      XX      XX      XX      XX      XX      XX
  德国                  XX      XX      XX      XX      XX      XX      XX      XX      XX
  法国                  XX      XX      XX      XX      XX      XX      XX      XX      XX
  其他欧洲地区          XX      XX      XX      XX      XX      XX      XX      XX      XX
  欧洲合计              XX      XX      XX      XX      XX      XX      XX      XX      XX
  占总额比例            X%      X%      X%      X%      X%      X%      X%      X%      X%
  同比增长 %            -       X%      X%      X%      X%      X%      X%      X%      X%

亚太地区
  [结构同上]

世界其他地区
  [结构同上]

总营收                  XX      XX      XX      XX      XX      XX      XX      XX      XX
```

**核实：**
- 按产品划分额 = 按地域划分额 = 总营收
- 所有百分比相加等于 100%
- 增长率计算正确

#### C. 按渠道划分的营收（若适用）

```
                        2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E
直销                    XX      XX      XX      XX      XX      XX      XX      XX      XX
电子商务/线上           XX      XX      XX      XX      XX      XX      XX      XX      XX
批发/合作伙伴           XX      XX      XX      XX      XX      XX      XX      XX      XX
零售店
  公司自营店            XX      XX      XX      XX      XX      XX      XX      XX      XX
  门店数量              XX      XX      XX      XX      XX      XX      XX      XX      XX
  单店销售额            XX      XX      XX      XX      XX      XX      XX      XX      XX
其他渠道                XX      XX      XX      XX      XX      XX      XX      XX      XX

总营收                  XX      XX      XX      XX      XX      XX      XX      XX      XX
```

### 第 3 步：营业费用建模

#### A. 营业成本 (Cost of Revenue)
1. **拆解销售成本 (COGS) 构成**
   - 产品成本（原材料、制造）
   - 运输与物流
   - 服务交付成本
   - 其他直接成本

2. **建立与营收的链接**
   - 计算各年度销售成本占营收比例
   - 模拟逐年毛利率
   - 链接至假设项

#### B. 研发费用 (R&D)
```
研究与开发 (R&D)        2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E
研发人员数量            XX      XX      XX      XX      XX      XX      XX      XX      XX
研发人均薪酬            XX      XX      XX      XX      XX      XX      XX      XX      XX
研发人力成本合计        XX      XX      XX      XX      XX      XX      XX      XX      XX
研发其他成本            XX      XX      XX      XX      XX      XX      XX      XX      XX
研发费用总额            XX      XX      XX      XX      XX      XX      XX      XX      XX
占营收比例              X%      X%      X%      X%      X%      X%      X%      X%      X%
```

#### C. 销售与市场费用 (S&M)
```
销售与市场 (S&M)        2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E
销售人员数量            XX      XX      XX      XX      XX      XX      XX      XX      XX
销售人均薪酬            XX      XX      XX      XX      XX      XX      XX      XX      XX
人力成本合计            XX      XX      XX      XX      XX      XX      XX      XX      XX
市场营销支出            XX      XX      XX      XX      XX      XX      XX      XX      XX
销售其他成本            XX      XX      XX      XX      XX      XX      XX      XX      XX
销售费用总额            XX      XX      XX      XX      XX      XX      XX      XX      XX
占营收比例              X%      X%      X%      X%      X%      X%      X%      X%      X%
```

#### D. 一般及行政费用 (G&A)
```
一般及行政 (G&A)        2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E
行政人员数量            XX      XX      XX      XX      XX      XX      XX      XX      XX
行政人均薪酬            XX      XX      XX      XX      XX      XX      XX      XX      XX
人力成本合计            XX      XX      XX      XX      XX      XX      XX      XX      XX
行政其他成本            XX      XX      XX      XX      XX      XX      XX      XX      XX
管理费用总额            XX      XX      XX      XX      XX      XX      XX      XX      XX
占营收比例              X%      X%      X%      X%      X%      X%      X%      X%      X%
```

#### E. 折旧与摊销 (D&A)
- 链接至资本支出附表
- 应用来自“假设项”的一定折旧率
- 计算年度折旧与摊销额

### 第 4 步：编制利润表 (P&L)

**创建一个包含 40-50 个明细行的完整损益表：**

```
利润表 (P&L)            2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E

营业收入
[链接至营收模型工作表]
总营收                  XX      XX      XX      XX      XX      XX      XX      XX      XX
  同比增长 %            -       X%      X%      X%      X%      X%      X%      X%      X%

营业成本
[链接至销售成本拆解]
销售成本合计            XX      XX      XX      XX      XX      XX      XX      XX      XX

毛利                    XX      XX      XX      XX      XX      XX      XX      XX      XX
  毛利率 %              X%      X%      X%      X%      X%      X%      X%      X%      X%

营业费用
研发费用合计            XX      XX      XX      XX      XX      XX      XX      XX      XX
  占营收比例            X%      X%      X%      X%      X%      X%      X%      X%      X%
销售费用合计            XX      XX      XX      XX      XX      XX      XX      XX      XX
  占营收比例            X%      X%      X%      X%      X%      X%      X%      X%      X%
管理费用合计            XX      XX      XX      XX      XX      XX      XX      XX      XX
  占营收比例            X%      X%      X%      X%      X%      X%      X%      X%      X%
折旧与摊销              XX      XX      XX      XX      XX      XX      XX      XX      XX

营业费用合计            XX      XX      XX      XX      XX      XX      XX      XX      XX
  占营收比例            X%      X%      X%      X%      X%      X%      X%      X%      X%

EBITDA                  XX      XX      XX      XX      XX      XX      XX      XX      XX
  EBITDA 利润率 %       X%      X%      X%      X%      X%      X%      X%      X%      X%

息税前利润 (EBIT)        XX      XX      XX      XX      XX      XX      XX      XX      XX
  EBIT 利润率 %         X%      X%      X%      X%      X%      X%      X%      X%      X%

利息费用                (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
利息收入                XX      XX      XX      XX      XX      XX      XX      XX      XX
其他收入/(支出)         XX      XX      XX      XX      XX      XX      XX      XX      XX

税前利润                XX      XX      XX      XX      XX      XX      XX      XX      XX

所得税                  (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
  实际税率 %            X%      X%      X%      X%      X%      X%      X%      X%      X%

净利润                  XX      XX      XX      XX      XX      XX      XX      XX      XX
  净利率 %              X%      X%      X%      X%      X%      X%      X%      X%      X%

发行在外股份数
基本股份总数 (百万)     XX      XX      XX      XX      XX      XX      XX      XX      XX
稀释股份总数 (百万)     XX      XX      XX      XX      XX      XX      XX      XX      XX

每股收益 (EPS)
基本 EPS                $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX
稀释 EPS                $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX
```

### 第 5 步：编制现金流量表

```
现金流量表              2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E

经营活动
净利润                  XX      XX      XX      XX      XX      XX      XX      XX      XX
调整项：
  折旧与摊销            XX      XX      XX      XX      XX      XX      XX      XX      XX
  股权激励费用          XX      XX      XX      XX      XX      XX      XX      XX      XX
  其他非现项            XX      XX      XX      XX      XX      XX      XX      XX      XX

营运资本变动：
  应收账款变动          (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
  存货变动              (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
  应付账款变动          XX      XX      XX      XX      XX      XX      XX      XX      XX
  其他营运资本          (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)

经营活动现金流合计      XX      XX      XX      XX      XX      XX      XX      XX      XX

投资活动
资本支出 (CapEx)        (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
资产收购                (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
其他投资活动            XX      XX      XX      XX      XX      XX      XX      XX      XX

投资活动现金流合计      (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)

自由现金流 (FCF)        XX      XX      XX      XX      XX      XX      XX      XX      XX
  FCF 利润率 %          X%      X%      X%      X%      X%      X%      X%      X%      X%

筹资活动
债务发行                XX      XX      XX      XX      XX      XX      XX      XX      XX
债务偿还                (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
股权增发                XX      XX      XX      XX      XX      XX      XX      XX      XX
股利支付                (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
其他筹资活动            XX      XX      XX      XX      XX      XX      XX      XX      XX

筹资活动现金流合计      XX      XX      XX      XX      XX      XX      XX      XX      XX

现金及等价物净增加额    XX      XX      XX      XX      XX      XX      XX      XX      XX

期初现金                XX      XX      XX      XX      XX      XX      XX      XX      XX
期末现金                XX      XX      XX      XX      XX      XX      XX      XX      XX
```

### 第 6 步：编制资产负债表

创建一个包含 35-45 个明细行的完整资产负债表：

```
资产负债表              2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E

资产
流动资产：
  现金及等价物          XX      XX      XX      XX      XX      XX      XX      XX      XX
  应收账款              XX      XX      XX      XX      XX      XX      XX      XX      XX
  存货                  XX      XX      XX      XX      XX      XX      XX      XX      XX
  预付费用              XX      XX      XX      XX      XX      XX      XX      XX      XX
  其他流动资产          XX      XX      XX      XX      XX      XX      XX      XX      XX
流动资产合计            XX      XX      XX      XX      XX      XX      XX      XX      XX

非流动资产：
  固定资产 (PP&E) 原值  XX      XX      XX      XX      XX      XX      XX      XX      XX
  累计折旧              (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
  固定资产净值          XX      XX      XX      XX      XX      XX      XX      XX      XX
  无形资产              XX      XX      XX      XX      XX      XX      XX      XX      XX
  商誉                  XX      XX      XX      XX      XX      XX      XX      XX      XX
  其他非流动资产        XX      XX      XX      XX      XX      XX      XX      XX      XX
非流动资产合计          XX      XX      XX      XX      XX      XX      XX      XX      XX

资产总计                XX      XX      XX      XX      XX      XX      XX      XX      XX

负债
流动负债：
  应付账款              XX      XX      XX      XX      XX      XX      XX      XX      XX
  应计费用              XX      XX      XX      XX      XX      XX      XX      XX      XX
  递延收入              XX      XX      XX      XX      XX      XX      XX      XX      XX
  短期债务              XX      XX      XX      XX      XX      XX      XX      XX      XX
  其他流动负债          XX      XX      XX      XX      XX      XX      XX      XX      XX
流动负债合计            XX      XX      XX      XX      XX      XX      XX      XX      XX

非流动负债：
  长期债务              XX      XX      XX      XX      XX      XX      XX      XX      XX
  递延所得税            XX      XX      XX      XX      XX      XX      XX      XX      XX
  其他非流动负债        XX      XX      XX      XX      XX      XX      XX      XX      XX
非流动负债合计          XX      XX      XX      XX      XX      XX      XX      XX      XX

负债合计                XX      XX      XX      XX      XX      XX      XX      XX      XX

所有者权益
  普通股                XX      XX      XX      XX      XX      XX      XX      XX      XX
  资本公积              XX      XX      XX      XX      XX      XX      XX      XX      XX
  留存收益              XX      XX      XX      XX      XX      XX      XX      XX      XX
  库存股                (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
  其他权益项            XX      XX      XX      XX      XX      XX      XX      XX      XX
股东权益合计            XX      XX      XX      XX      XX      XX      XX      XX      XX

负债及股东权益总计      XX      XX      XX      XX      XX      XX      XX      XX      XX

配平检查 (Check)        OK      OK      OK      OK      OK      OK      OK      OK      OK
```

**勾稽关系检查公式：**
- 每个年份的“资产总计”必须等于“负债及股东权益总计”
- 出现的任何不平衡应以红色标记

### 第 7 步：构建 DCF 输入工作表

为估值任务（任务 3）准备输入项：

```
DCF 输入项              2025E   2026E   2027E   2028E   2029E

息税前利润 (EBIT)        XX      XX      XX      XX      XX
实际税率                X%      X%      X%      X%      X%
税后净营业利润 (NOPAT)  XX      XX      XX      XX      XX

加：折旧与摊销          XX      XX      XX      XX      XX
减：资本支出 (CapEx)    (XX)    (XX)    (XX)    (XX)    (XX)
减：营运资本变动 (NWC)  (XX)    (XX)    (XX)    (XX)    (XX)

无杠杆自由现金流 (UFCF) XX      XX      XX      XX      XX

终值年份指标：
  2029E 营收            $X,XXX
  2029E EBITDA          $XXX
  2029E EBIT            $XXX
  2029E 无杠杆 FCF      $XXX
```

### 第 8 步：构建情景分析工作表

根据不同的假设创建三种情景：

#### 情景假设表
```
关键假设项                      牛市        基准        熊市
营收复合增长率 (2025-2029)      XX%         XX%         XX%
2029E 毛利率                    XX%         XX%         XX%
2029E EBITDA 利润率             XX%         XX%         XX%
资本支出占营收比例              X%          X%          X%
[添加其他关键假设]
```

#### 情景输出对比表
```
财务指标                        牛市        基准        熊市
2029E 营收 (百万美元)           $X,XXX      $X,XXX      $X,XXX
2029E EBITDA (百万美元)         $XXX        $XXX        $XXX
2029E EBITDA 利润率             XX%         XX%         XX%
2029E 净利润 (百万美元)         $XXX        $XXX        $XXX
2029E 每股收益 (EPS)            $X.XX       $X.XX       $X.XX
2029E FCF (百万美元)            $XXX        $XXX        $XXX
2029E FCF 利润率                XX%         XX%         XX%

2025-2029 累计 FCF (百万美元)   $XXX        $XXX        $XXX
```

**记录情景设定理由：**
- 牛市情景：[描述乐观但可实现的假设背景]
- 基准情景：[描述最有可能发生的平衡状态]
- 熊市情景：[描述下行风险及触发因素]

### 第 9 步：质量检查

**验证模型的完整性：**
1. [ ] 测试所有公式（抽查计算逻辑）
2. [ ] 更改一项假设 → 验证模型是否正确更新
3. [ ] 测试情景切换开关
4. [ ] 验证颜色编码是否规范 (蓝/黑/绿)
5. [ ] 检查所有年份的资产负债表是否配平
6. [ ] 验证是否存在循环引用（Excel 会有提示）
7. [ ] 检查预测部分是否含有硬编码数字
8. [ ] 验证所有跨表链接是否有效
9. [ ] 测试不同标签页间的营收总额是否勾稽一致
10. [ ] 检查整体美化与展示效果

---

## 质量标准

### 模型完整性 (Integrity)
- 所有公式跨表链接正确
- 预测年份除“假设”外不含硬编码数字
- 无循环引用
- 资产负债表所有年度均实现配平
- 情景切换功能运作正常

### 完备性 (Completeness)
- 包含全部 6 个核心标签页
- 利润表包含不少于 40-50 个明细行
- 营收模型包含细化的产品拆分（20-30 行）
- 营收模型包含细化的地域拆分（15-20 行）
- 完整的现金流与资产负债表明细行
- 牛市/基准/熊市情景数据齐备

### 专业格式 (Formatting)
- 遵循统一颜色编码（蓝/黑/绿）
- 标题与标签清晰明了
- 专业的边框及底纹设计
- 关键单元格使用命名区域
- 使用行组功能提高可阅读性
- 明确标注单位（如千 vs. 百万）

### 文档记录 (Documentation)
- 记录假设依据（蓝色数值单元格附带批注）
- 在单元格批注或注释区标明数据来源
- 对复杂计算提供注释说明
- 描述建模方法论

---

## 文件命名规范

按如下格式保存财务模型：
`[公司名]_Financial_Model_[日期].xlsx`

示例：`Tesla_Financial_Model_2024-10-27.xlsx`

---

## 成功标准

一份卓越的财务模型应：
1. 包含 6 个核心标签页 (营收、利润表、现金流、资产负债表、情景分析、DCF 输入)
2. 实现全动态化（修改假设后，模型自动更新）
3. 预测部分没有任何硬编码数字
4. 包含详尽的营收拆分（产品 20-30 行，地理 15-20 行）
5. 利润表明细行达 40-50 行
6. 涵盖牛市/基准/熊市多情景
7. 格式专业，配色规范
8. 资产负债表与现金流勾稽关系正确且配平
9. 逻辑清晰，易于他人审计和理解
10. 通过准确的 FCF 计算为后续估值提供支持

---

## 常见模型类型 - 特殊考量

### 高增长科技/SaaS 类
- 侧重年度经常性总收入 (ARR) 增长率与净留存率 (Net Retention)
- 按产品线和地域建模
- 重点关注研发 (R&D) 与销售市场 (S&M) 的高投入
- 盈利时间表预测
- 单位经济效益分析 (LTV/CAC)

### 电子商务/零售类
- 按产品类别和渠道拆分营收
- 关注门店数量及同店销售增长（若适用）
- 存货周转率与营运资本管理
- 履行/履约成本 (Fulfillment costs)
- 获客成本

### 制造/工业类
- 产能利用率 (Capacity utilization)
- 原材料成本与定价策略
- 毛利桥梁分析 (量/价/结构/成本)
- 重资产、高资本支出模型
- 营运资本循环周期

---

## 后续步骤

完成任务 2 后，财务模型将用于：
- **任务 3 (估值)**：提供 DCF 输入项及预测财务数据
- **任务 4 (制图)**：为营收趋势、利润率图表、情景对比提供数据支撑
- **任务 5 (报告汇编)**：为研究报告提供财务数据表及深度分析

> **💡 Appendix: 领域知识小贴士**
> 1. **什么是“三大报表”？** 想象你在经营一家柠檬茶店。**利润表**告诉你今天挣了多少钱（收入减成本）；**资产负债表**列出了你有多少设备和原料（资产），以及欠多少债（负债）；**现金流量表**则盯着收银机里进出了多少真金白银。
> 2. **为什么要有“蓝黑绿”颜色区分？** 这是建模界的“潜规则”。蓝色代表手动输入的原始数据，黑色代表公式算的。这样别人看你的文件时，才知道哪里可以改，哪里不要动，防止把复杂的公式误删了。
> 3. **自由现金流 (FCF) 是什么？** 这是公司把所有该交的税、该付的工资、该买的设备都搞定后，兜里剩下的能自由支配的钱。这才是投资者最看重的“含金量”，决定了公司能不能发奖金或再投资。
> 4. **什么是“勾稽关系”？** 财务报表之间是环环相扣的，就像拼图。比如净利润最后会变成资产负债表里的留存收益。如果这张拼图拼不上（不配平），说明账目里一定有弄错的地方。
> 5. **DCF 估值在做什么？** 把公司未来几十年能挣到的所有钱，按照一定的比例“打折”后加在一起，算出公司现在值多少钱。这就像是在算：未来的 100 块钱，相当于现在的多少钱。
