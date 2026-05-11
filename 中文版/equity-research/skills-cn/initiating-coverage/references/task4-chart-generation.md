# 任务 4：图表生成 - 详细工作流

本文件为执行“首次覆盖（Initiating-Coverage）”技能的任务 4（图表生成）提供分步骤指导。

## 任务概述

**目的**：为研究报告生成 25-35 张专业的金融图表。

**前提条件**：⚠️ 开始前请务必确认
- **必选**：任务 1 的公司研究数据
  - 公司历史、里程碑（用于时间轴图表）
  - 管理团队、组织架构（用于架构图）
  - 产品组合（用于产品图表）
  - 客户细分（用于客户图表）
  - 竞争格局（用于竞争地位图表）
  - TAM 分析（用于市场规模图表）
- **必选**：任务 2 的财务模型
  - 按产品/地区划分的营收数据
  - 利润率趋势
  - 情景比较数据
- **必选**：任务 3 的估值分析
  - DCF 敏感性分析表
  - 可比公司数据
  - 估值区间
- **必选**：外部市场数据
  - 历史股价数据（Yahoo Finance, Bloomberg）
  - 历史估值倍数（图表 34 可选）

**⚠️ 至关重要：除非任务 1、2、3 已全部完成，否则请勿开始本任务**

本任务需要前三个任务的产出。若在未完成的情况下开始，将导致图表内容不完整。

**如果任务 1、2 或 3 中有任何一项未完成**：请立即停止，并告知用户哪些任务需要优先完成。具体要求如下：
- 任务 1：公司研究文档（对应 9 张图表）
- 任务 2：包含所有 6 个标签页的财务模型（对应 8 张图表）
- 任务 3：模型中已添加估值标签页（对应 6 张图表）
- 外部数据访问（对应 2 张图表）

严禁创建占位图表或因数据缺失而跳过图表。

**产出**：25-35 个专业图表文件（PNG/JPG 格式，300 DPI）

---

## 输入验证

**开始之前 - 检查所有前提条件：**

### 任务 1 验证（公司研究）
- [ ] 任务 1 已完成？（公司研究文档已存在）
- [ ] 公司历史与里程碑已记录？（用于图表 05、06）
- [ ] 管理团队与组织架构已描述？（用于图表 07）
- [ ] 产品组合已详细列出？（用于图表 08）
- [ ] 客户细分已分析？（用于图表 09）
- [ ] 竞争格局已勾勒？（用于图表 16、17、18）
- [ ] TAM 规模测算已完成？（用于图表 15）

### 任务 2 验证（财务模型）
- [ ] 任务 2 已完成？（财务模型 Excel 文件已存在）
- [ ] 按产品划分的营收细分可用？（用于图表 03 ⭐）
- [ ] 按地区划分的营收细分可用？（用于图表 04 ⭐）
- [ ] 历史 + 预测财务数据已完成？（用于图表 02、10、11、12）
- [ ] 情景分析（牛市/基准/熊市）已完成？（用于图表 14）
- [ ] 运营指标可用？（用于图表 13）

### 任务 3 验证（估值分析）
- [ ] 任务 3 已完成？（估值标签页已添加到模型中）
- [ ] DCF 敏感性矩阵已存在？（用于图表 28 ⭐）
- [ ] DCF 计算细节可用？（用于图表 29）
- [ ] 已收集可比公司数据？（用于图表 30、31）
- [ ] 估值区间已计算？（用于图表 32 ⭐）

### 外部数据验证
- [ ] 是否可以获取历史股价数据？（Yahoo Finance, Bloomberg，用于图表 01）
- [ ] 是否可以获取历史估值数据？（可选，用于图表 34）

**若任何验证失败**：
- 缺少任务 1？ → 先完成任务 1（公司研究）
- 缺少任务 2？ → 先完成任务 2（财务建模）
- 缺少任务 3？ → 先完成任务 3（估值分析）
- 缺少外部数据？ → 从 Yahoo Finance、Bloomberg 或类似渠道获取

---

## 图表要求：25 项必选 + 10 项可选

**重要提示**：任务 5（报告汇编）会将**创建的所有图表**嵌入到报告中。报告需要高密度的视觉内容（每 200-300 字配一张图），因此请确保图表覆盖全面。

### 4 项核心必选图表（不可或缺） ⭐

这 4 张图表是报告中必须存在的关键可视化内容：

1. **chart_03**：按产品/业务板块划分的营收 - 堆积面积图 ⭐
2. **chart_04**：按地区划分的营收 - 堆积柱状图 ⭐
3. **chart_28**：DCF 敏感性分析 - 双因素热力图 ⭐
4. **chart_32**：估值足球场图 - 水平条形图 ⭐

### 25 项必选图表（完整套件）

请创建以下全部 25 张图表。每张图表在任务 5 中都有特定用途：

**投资摘要部分 (1 张):**
- chart_01: 股价表现 (12-24 个月)

**财务表现部分 (6 张):**
- chart_02: 营收增长轨迹
- chart_03: 按产品划分的营收 - 堆积面积图 ⭐ 核心必选
- chart_04: 按地区划分的营收 - 堆积柱状图 ⭐ 核心必选
- chart_10: 毛利率演变
- chart_11: EBITDA 利润率趋势
- chart_12: 自由现金流趋势

**公司概况部分 (7 张):**
- chart_05: 公司概览/时间轴
- chart_06: 关键里程碑时间轴
- chart_07: 组织架构图
- chart_08: 产品组合概览
- chart_09: 客户细分
- chart_15: 市场规模演变 (TAM)
- chart_16: 竞争定位矩阵

**竞争与市场部分 (2 张):**
- chart_17: 市场份额细分
- chart_18: 竞争对标

**情景分析部分 (2 张):**
- chart_13: 运营指标仪表盘
- chart_14: 情景对比 (牛市/基准/熊市)

**估值部分 (7 张):**
- chart_28: DCF 敏感性热力图 ⭐ 核心必选
- chart_29: DCF 估值瀑布图
- chart_30: 交易对标散点图
- chart_31: 同业倍数对比
- chart_32: 估值足球场图 ⭐ 核心必选
- chart_33: 目标价情景分析
- chart_34: 历史估值倍数

**总计：25 项必选图表**

### 10 项可选图表（用于达到 30-35 张规模）

添加这些图表以增加视觉密度和叙事深度（总数达到 26-35 张）：

- chart_19: 客户获取趋势
- chart_20: 单位经济效益演变
- chart_21: 产品路线图时间轴
- chart_22: 地域扩张版图
- chart_23: 研发投入趋势
- chart_24: 营销效率分析
- chart_25: 营运资本趋势
- chart_26: 债务到期计划表
- chart_27: 股权结构
- chart_35: 分析师目标价分布

**总数区间：25-35 张 (25 项必选 + 0-10 项可选)**

---

## 必选图表的数据源映射

清晰了解每张图表的数据来源：

### 来自任务 1 (公司研究) - 9 张
- chart_05: 公司概览 → 任务 1：公司概览部分
- chart_06: 关键里程碑 → 任务 1：公司历史部分
- chart_07: 组织架构 → 任务 1：管理团队部分
- chart_08: 产品组合 → 任务 1：产品与服务部分
- chart_09: 客户细分 → 任务 1：客户与进入市场策略部分
- chart_15: 市场规模演变 → 任务 1：市场机遇 (TAM) 部分
- chart_16: 竞争定位 → 任务 1：竞争格局部分
- chart_17: 市场份额 → 任务 1：竞争格局部分
- chart_18: 竞争对标 → 任务 1：竞争格局部分

### 来自任务 2 (财务模型) - 8 张
- chart_02: 营收增长 → 利润表标签页 (营收行)
- chart_03: 按产品划分营收 ⭐ → 营收模型标签页 (产品细分)
- chart_04: 按地区划分营收 ⭐ → 营收模型标签页 (地区细分)
- chart_10: 毛利率 → 利润表标签页 (毛利 / 营收)
- chart_11: EBITDA 利润率 → 利润表标签页 (EBITDA / 营收)
- chart_12: 自由现金流 → 现金流量表标签页 (经营活动现金流 - 资本开支)
- chart_13: 运营指标 → 多个标签页 (利润表、现金流量表)
- chart_14: 情景对比 → 情景标签页 (牛市/基准/熊市)

### 来自任务 3 (估值分析) - 6 张
- chart_28: DCF 敏感性 ⭐ → 敏感性分析标签页
- chart_29: DCF 瀑布图 → DCF 标签页 (企业价值构成)
- chart_30: 交易对标散点图 → 可比公司标签页
- chart_31: 同业倍数 → 可比公司标签页
- chart_32: 估值足球场图 ⭐ → 估值汇总标签页
- chart_33: 目标价情景分析 → 估值汇总标签页 (或基于情景计算)

### 来自外部渠道 - 2 张
- chart_01: 股价表现 → Yahoo Finance, Bloomberg, Alpha Vantage
- chart_34: 历史估值倍数 → Yahoo Finance, Bloomberg (历史 P/E, EV/EBITDA)

**重要提示**：必须完成全部前三项任务（1, 2, 3）并拥有外部数据访问权限，才能完整创建 25 项必选图表。

---

## 分步图表生成工作流

### 第一步：环境配置

**安装必要的库：**
```bash
pip install matplotlib seaborn pandas numpy plotly
```

**创建 Python 脚本头部：**
```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.patches import Rectangle
import warnings
warnings.filterwarnings('ignore')

# 设置全局样式
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# 全局设置
DPI = 300
FIGURE_WIDTH = 10
FIGURE_HEIGHT = 6
TITLE_FONT_SIZE = 14
AXIS_FONT_SIZE = 12
LABEL_FONT_SIZE = 10
```

### 第二步：从模型与估值中提取数据

#### A. 提取营收数据
```python
# 按产品划分的营收 (来自任务 2 模型)
years = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029]

# 从 Excel 提取或基于模型手动定义
product_a = [100, 120, 145, 175, 210, 252, 302, 363, 435, 522]
product_b = [80, 95, 115, 138, 165, 198, 238, 285, 342, 411]
product_c = [50, 62, 78, 98, 122, 153, 191, 239, 299, 374]
product_d = [30, 38, 48, 61, 77, 97, 122, 153, 191, 239]

# 按地区划分的营收
north_america = [150, 180, 220, 265, 320, 384, 461, 553, 664, 797]
europe = [80, 95, 115, 140, 170, 204, 245, 294, 353, 423]
asia_pacific = [40, 50, 63, 80, 101, 127, 159, 199, 249, 311]
rest_of_world = [20, 25, 32, 40, 51, 64, 80, 100, 125, 156]
```

#### B. 提取利润率数据
```python
# 利润率演变
gross_margin = [58.0, 59.2, 60.5, 61.8, 63.0, 64.5, 66.0, 67.0, 67.5, 68.0]
ebitda_margin = [12.0, 15.5, 18.8, 22.0, 25.0, 28.0, 30.5, 32.0, 33.0, 34.0]
fcf_margin = [8.0, 11.0, 14.5, 18.0, 21.0, 24.0, 26.5, 28.0, 29.0, 30.0]
```

#### C. 提取 DCF 敏感性数据
```python
# DCF 敏感性 (来自任务 3 估值)
wacc_values = [7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
terminal_growth = [1.5, 2.0, 2.5, 3.0, 3.5]

# 每股价格矩阵 (行 = WACC, 列 = 永续增长率)
dcf_sensitivity = np.array([
    [66, 71, 76, 82, 89],
    [58, 62, 67, 72, 78],
    [52, 55, 59, 63, 68],
    [47, 50, 53, 56, 60],
    [42, 45, 48, 51, 54],
    [39, 41, 44, 46, 49]
])
```

#### D. 提取估值区间
```python
# 估值足球场图 (来自任务 3)
valuation_methods = ['DCF Analysis', 'Trading Comps\n(NTM)', 'Precedent\nTransactions']
valuation_low = [48, 45, 52]
valuation_high = [62, 57, 66]
current_price = 50
target_price = 55
```

### 第三步：创建核心必选图表

#### 图表 1: 按产品划分营收 - 堆积面积图 ⭐ 核心必选

```python
def create_revenue_by_product_chart():
    """创建按产品划分的营收堆积面积图"""

    fig, ax = plt.subplots(figsize=(10, 6))

    # 创建堆积面积图
    ax.stackplot(years, product_a, product_b, product_c, product_d,
                 labels=['Product A', 'Product B', 'Product C', 'Product D'],
                 colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
                 alpha=0.8)

    # 格式化
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Revenue ($M)', fontsize=12, fontweight='bold')
    ax.set_title('Figure 3 - Revenue by Product/Segment (2020-2029E)',
                 fontsize=14, fontweight='bold', pad=20)

    # 图例
    ax.legend(loc='upper left', frameon=False, fontsize=10)

    # 网格线
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    # 去除顶部和右侧边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 添加垂直线区分历史与预测
    ax.axvline(x=2024, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax.text(2024.2, ax.get_ylim()[1]*0.95, 'Projected →',
            fontsize=9, color='gray', ha='left')

    # 数据来源
    fig.text(0.12, 0.02, 'Source: Company data, [Firm] estimates',
             fontsize=9, style='italic', color='gray')

    # 保存
    plt.tight_layout()
    plt.savefig('chart_03_revenue_by_product_stacked_area.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 已创建: chart_03_revenue_by_product_stacked_area.png")

create_revenue_by_product_chart()
```

#### 图表 2: 按地区划分营收 - 堆积柱状图 ⭐ 核心必选

```python
def create_revenue_by_geography_chart():
    """创建按地区划分的营收堆积柱状图"""

    years_labels = ['2020', '2021', '2022', '2023', '2024',
                    '2025E', '2026E', '2027E', '2028E', '2029E']

    fig, ax = plt.subplots(figsize=(10, 6))

    # 创建堆积柱状图
    width = 0.6
    x = np.arange(len(years_labels))

    p1 = ax.bar(x, north_america, width, label='North America', color='#1f77b4')
    p2 = ax.bar(x, europe, width, bottom=north_america,
                label='Europe', color='#ff7f0e')
    p3 = ax.bar(x, asia_pacific, width,
                bottom=np.array(north_america) + np.array(europe),
                label='Asia-Pacific', color='#2ca02c')
    p4 = ax.bar(x, rest_of_world, width,
                bottom=np.array(north_america) + np.array(europe) + np.array(asia_pacific),
                label='Rest of World', color='#d62728')

    # 格式化
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Revenue ($M)', fontsize=12, fontweight='bold')
    ax.set_title('Figure 4 - Revenue by Geography (2020-2029E)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(years_labels, rotation=45, ha='right')

    # 图例
    ax.legend(loc='upper left', frameon=False, fontsize=10)

    # 网格线
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    # 去除顶部和右侧边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 数据来源
    fig.text(0.12, 0.02, 'Source: Company data, [Firm] estimates',
             fontsize=9, style='italic', color='gray')

    # 保存
    plt.tight_layout()
    plt.savefig('chart_04_revenue_by_geography_stacked_bar.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 已创建: chart_04_revenue_by_geography_stacked_bar.png")

create_revenue_by_geography_chart()
```

#### 图表 3: DCF 敏感性 - 热力图 ⭐ 核心必选

```python
def create_dcf_sensitivity_heatmap():
    """创建 DCF 敏感性分析热力图"""

    # 创建 DataFrame
    df = pd.DataFrame(dcf_sensitivity,
                      index=[f'{w}%' for w in wacc_values],
                      columns=[f'{g}%' for g in terminal_growth])

    fig, ax = plt.subplots(figsize=(8, 6))

    # 创建热力图
    sns.heatmap(df, annot=True, fmt='d', cmap='RdYlGn',
                cbar_kws={'label': 'Price per Share ($)'},
                linewidths=0.5, linecolor='white',
                ax=ax, vmin=35, vmax=95)

    # 格式化
    ax.set_xlabel('Terminal Growth Rate', fontsize=12, fontweight='bold')
    ax.set_ylabel('WACC', fontsize=12, fontweight='bold')
    ax.set_title('Figure 28 - DCF Sensitivity Analysis ($/share)',
                 fontsize=14, fontweight='bold', pad=20)

    # 旋转 y 轴标签
    plt.yticks(rotation=0)

    # 数据来源
    fig.text(0.12, 0.02, 'Source: [Firm] estimates',
             fontsize=9, style='italic', color='gray')

    # 保存
    plt.tight_layout()
    plt.savefig('chart_28_dcf_sensitivity_heatmap.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 已创建: chart_28_dcf_sensitivity_heatmap.png")

create_dcf_sensitivity_heatmap()
```

#### 图表 4: 估值足球场图 ⭐ 核心必选

```python
def create_valuation_football_field():
    """创建估值足球场图"""

    fig, ax = plt.subplots(figsize=(10, 5))

    # 创建水平条形
    y_positions = np.arange(len(valuation_methods))
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

    for i, (method, low, high, color) in enumerate(
            zip(valuation_methods, valuation_low, valuation_high, colors)):
        ax.barh(i, high - low, left=low, height=0.6,
                color=color, alpha=0.7, label=method)

        # 在两端添加数值标签
        ax.text(low - 1, i, f'${low}', va='center', ha='right', fontsize=10)
        ax.text(high + 1, i, f'${high}', va='center', ha='left', fontsize=10)

    # 添加现价线
    ax.axvline(x=current_price, color='red', linestyle='--', linewidth=2,
               label=f'Current: ${current_price}', alpha=0.7)

    # 添加目标价线
    ax.axvline(x=target_price, color='black', linestyle='-', linewidth=2,
               label=f'Target: ${target_price}')

    # 格式化
    ax.set_yticks(y_positions)
    ax.set_yticklabels(valuation_methods, fontsize=11)
    ax.set_xlabel('Price Per Share ($)', fontsize=12, fontweight='bold')
    ax.set_title('Figure 32 - Valuation Football Field',
                 fontsize=14, fontweight='bold', pad=20)

    # 设置 x 轴范围
    ax.set_xlim(40, 70)

    # 去除边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # 网格线
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    # 图例
    ax.legend(loc='upper right', frameon=False, fontsize=9)

    # 数据来源
    fig.text(0.12, 0.02, 'Source: [Firm] estimates',
             fontsize=9, style='italic', color='gray')

    # 保存
    plt.tight_layout()
    plt.savefig('chart_32_valuation_football_field.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 已创建: chart_32_valuation_football_field.png")

create_valuation_football_field()
```

### 第四步：创建剩余必选图表 (图表 1-34)

**完成全部 25 项必选图表**。每张图表在任务 5 中都有其特定的叙事角色。

#### 投资摘要 (1 张)
```python
# chart_01: 股价表现 (12-24 个月)
# - 显示股价随时间演变并与市场指数对比的折线图
# - 用于最终报告的第 1 页
```

#### 财务表现 (除图表 03 和 04 外的 5 张)
```python
# chart_02: 营收增长轨迹
# chart_10: 毛利率演变
# chart_11: EBITDA 利润率趋势
# chart_12: 自由现金流趋势
# chart_14: 情景对比 (牛市/基准/熊市)
```

#### 公司概况部分 (7 张)
```python
# chart_05: 公司概览/时间轴
# chart_06: 关键里程碑时间轴
# chart_07: 组织架构图
# chart_08: 产品组合概览
# chart_09: 客户细分
# chart_15: 市场规模演变 (TAM)
# chart_16: 竞争定位矩阵
```

#### 竞争与市场部分 (2 张)
```python
# chart_17: 市场份额细分
# chart_18: 竞争对标
```

#### 情景分析部分 (1 张)
```python
# chart_13: 运营指标仪表盘
```

#### 估值部分 (除图表 28 和 32 外的 6 张)
```python
# chart_29: DCF 估值瀑布图
# chart_30: 交易对标散点图
# chart_31: 同业倍数对比
# chart_33: 目标价情景分析
# chart_34: 历史估值倍数
```

**所有图表请保持一致的工作标准：**
- 300 DPI 分辨率
- 专业配色方案
- 清晰的标签、图例和标题
- 图表编号（如“Figure 5 - Company Timeline”）
- 底部标注数据来源

### 第四步 B：创建可选图表 (总数达到 26-35)

**可选**：从下表中额外选取 1-10 张图表，以增强视觉叙事：

```python
# chart_19: 客户获取趋势
# chart_20: 单位经济效益演变
# chart_21: 产品路线图时间轴
# chart_22: 地域扩张版图
# chart_23: 研发投入趋势
# chart_24: 营销效率分析
# chart_25: 营运资本趋势
# chart_26: 债务到期计划表
# chart_27: 股权结构
# chart_35: 分析师目标价分布
```

这些可选图表提供了额外的视觉支持，有助于在任务 5 中达成“每 200-300 字一张图”的目标。

### 第五步：创建图表索引

创建一个文档记录所有图表：

```python
def create_chart_index():
    """创建图表索引文档"""

    # 25 项必选图表
    required_charts = [
        "chart_01_stock_price_performance.png - 股价表现 (12-24个月)",
        "chart_02_revenue_growth_trajectory.png - 营收增长轨迹",
        "chart_03_revenue_by_product_stacked_area.png - 按产品划分营收 [核心必选]",
        "chart_04_revenue_by_geography_stacked_bar.png - 按地区划分营收 [核心必选]",
        "chart_05_company_overview.png - 公司概览/时间轴",
        "chart_06_key_milestones_timeline.png - 关键里程碑时间轴",
        "chart_07_organizational_structure.png - 组织架构图",
        "chart_08_product_portfolio.png - 产品组合概览",
        "chart_09_customer_segmentation.png - 客户细分",
        "chart_10_gross_margin_evolution.png - 毛利率演变趋势",
        "chart_11_ebitda_margin_progression.png - EBITDA 利润率趋势",
        "chart_12_free_cash_flow_trend.png - 自由现金流趋势",
        "chart_13_operating_metrics_dashboard.png - 运营指标仪表盘",
        "chart_14_scenario_comparison.png - 情景对比 (牛市/基准/熊市)",
        "chart_15_market_size_evolution.png - 市场规模演变 (TAM)",
        "chart_16_competitive_positioning.png - 竞争定位矩阵",
        "chart_17_market_share.png - 市场份额细分",
        "chart_18_competitive_benchmarking.png - 竞争对标分析",
        "chart_28_dcf_sensitivity_heatmap.png - DCF 敏感性热力图 [核心必选]",
        "chart_29_dcf_waterfall.png - DCF 估值瀑布图",
        "chart_30_trading_comps_scatter.png - 交易对标散点图",
        "chart_31_peer_multiples_comparison.png - 同业倍数对比",
        "chart_32_valuation_football_field.png - 估值足球场图 [核心必选]",
        "chart_33_price_target_scenarios.png - 目标价情景分析",
        "chart_34_historical_valuation_multiples.png - 历史估值倍数",
    ]

    # 10 项可选图表 (用于总数 26-35)
    optional_charts = [
        "chart_19_customer_acquisition_trends.png - 客户获取趋势 [可选]",
        "chart_20_unit_economics_evolution.png - 单位经济效益演变 [可选]",
        "chart_21_product_roadmap_timeline.png - 产品路线图时间轴 [可选]",
        "chart_22_geographic_expansion_map.png - 地域扩张版图 [可选]",
        "chart_23_rd_investment_trends.png - 研发投入趋势 [可选]",
        "chart_24_sales_marketing_efficiency.png - 营销效率分析 [可选]",
        "chart_25_working_capital_trends.png - 营运资本趋势 [可选]",
        "chart_26_debt_maturity_schedule.png - 债务到期计划表 [可选]",
        "chart_27_ownership_structure.png - 股权结构 [可选]",
        "chart_35_analyst_price_targets.png - 分析师目标价分布 [可选]",
    ]

    with open('chart_index.txt', 'w') as f:
        f.write("[公司名称] 权益研究报告图表索引\n")
        f.write("=" * 60 + "\n\n")

        f.write("4 项核心必选图表 (务必包含):\n")
        f.write("- chart_03: 按产品划分营收 (堆积面积图) ⭐\n")
        f.write("- chart_04: 按地区划分营收 (堆积柱状图) ⭐\n")
        f.write("- chart_28: DCF 敏感性 (热力图) ⭐\n")
        f.write("- chart_32: 估值足球场图 ⭐\n\n")

        f.write("25 项必选图表:\n")
        for chart in required_charts:
            f.write(f"  {chart}\n")

        f.write("\n10 项可选图表 (总数区间 26-35):\n")
        for chart in optional_charts:
            f.write(f"  {chart}\n")

        f.write("\n" + "=" * 60 + "\n")
        f.write("注：任务 5 将把所创建的所有图表 (25-35) 嵌入报告中，\n")
        f.write("以确保视觉密度 (约每 200-300 字一张配图)。\n")

    print("✓ 已创建: chart_index.txt")

create_chart_index()
```

### 第六步：质量检查

**执行验证脚本：**

```python
import os

def verify_charts():
    """验证所有图表是否成功创建"""

    mandatory_charts = [
        'chart_03_revenue_by_product_stacked_area.png',
        'chart_04_revenue_by_geography_stacked_bar.png',
        'chart_28_dcf_sensitivity_heatmap.png',
        'chart_32_valuation_football_field.png'
    ]

    print("\n" + "="*60)
    print("图表生成状态验证")
    print("="*60)

    # 检查必选图表
    print("\n1. 核心必选图表:")
    all_mandatory_present = True
    for chart in mandatory_charts:
        if os.path.exists(chart):
            size = os.path.getsize(chart) / 1024  # KB
            print(f"   ✓ {chart} ({size:.1f} KB)")
        else:
            print(f"   ✗ 缺失: {chart}")
            all_mandatory_present = False

    # 统计总数
    chart_files = [f for f in os.listdir('.') if f.startswith('chart_') and f.endswith('.png')]
    print(f"\n2. 图表总数: {len(chart_files)}")
    print(f"   目标: 25-35 项")
    print(f"   状态: {'✓ 通过' if 25 <= len(chart_files) <= 35 else '⚠ 警告'}")

    # 检查文件大小 (300 DPI 应大于 50KB)
    print("\n3. 文件大小检查:")
    small_files = []
    for chart in chart_files[:5]:  # 示例检查前 5 个
        size = os.path.getsize(chart) / 1024
        if size < 50:
            small_files.append(chart)
        print(f"   {chart}: {size:.1f} KB")

    if small_files:
        print(f"   ⚠ 警告: {len(small_files)} 个文件可能分辨率较低")
    else:
        print(f"   ✓ 所有抽检文件大小合格")

    # 最终结果
    print("\n" + "="*60)
    if all_mandatory_present and 25 <= len(chart_files) <= 35:
        print("✓ 验证通过 - 已准备好进入任务 5")
    else:
        print("✗ 验证失败 - 请核对缺失图表")
    print("="*60 + "\n")

verify_charts()
```

---

## 质量标准

### 视觉质量
- [ ] 高分辨率 (最低 300 DPI)
- [ ] 专业的配色方案 (所有图表保持一致)
- [ ] 文字清晰易读 (字体不小于 9pt)
- [ ] 比例正确 (无拉伸变形)
- [ ] 无锯齿或人为模糊

### 数据准确性
- [ ] 数据与原始来源一致 (财务模型与估值)
- [ ] 单位和标签正确 (百万美元、百分比等)
- [ ] 坐标轴范围及步长合理
- [ ] 所有图表的时间跨度一致
- [ ] 计算过程经过验证

### 格式质量
- [ ] 所有图表样式风格统一
- [ ] 图表编号正确 (按顺序排列)
- [ ] 标题和注释含义准确
- [ ] 每张图表均附有数据来源
- [ ] 外观呈现符合专业研报标准

### 完整性
- [ ] 4 项核心必选图表均已创建
- [ ] 总数在 25-35 项之间
- [ ] 文件命名规范 (chart_01, chart_02 等)
- [ ] 图表索引已生成
- [ ] 已准备好嵌入到 Word 文档中

---

## 图表类型参考

### 何时使用各类图表

**折线图 (Line Charts)**：时间序列趋势 (营收、利润率、股价)

**堆积面积图 (Stacked Area)**：营收产品构成 ⭐, 市场规模构成

**堆积柱状图 (Stacked Bar)**：营收地区细分 ⭐, 季度数据明细

**热力图 (Heatmap)**：DCF 敏感性分析 ⭐, 相关性矩阵

**水平条形图 (Horizontal Bar)**：估值足球场图 ⭐, 行业对标排名

**瀑布图 (Waterfall)**：营收桥接分析、利润调节项、DCF 构建过程

**散点/气泡图 (Scatter/Bubble)**：增长 vs. 估值对比、竞争对标

**2×2 矩阵**：竞争地位分析、产品矩阵分析

---

## 文件命名规范

**请务必遵循以下格式：**
```
chart_[编号]_[描述].png

示例：
chart_01_stock_price_performance.png
chart_03_revenue_by_product_stacked_area.png
chart_28_dcf_sensitivity_heatmap.png
```

**图表编号**应根据其在报告中的位置编排，而非创建顺序。

---

## 常见图表生成问题

### 问题 1：分辨率低
**表现**：图表模糊或有锯齿
**解决方法**：在 `plt.savefig()` 中设置 `dpi=300`

### 问题 2：文字遮挡/缺失
**表现**：标签或标题在边缘被切断
**解决方法**：在 `plt.savefig()` 中使用 `bbox_inches='tight'`

### 问题 3：配色不佳
**表现**：颜色显得不专业或辨识度低
**解决方法**：使用 Tableau10 等标准色板或自定义企业色系

### 问题 4：标签重叠
**表现**：坐标轴标签堆叠在一起
**解决方法**：旋转标签 (如 `rotation=45`) 或缩小字号

### 问题 5：多余空白
**表现**：图表四周有过多白边
**解决方法**：在保存前调用 `plt.tight_layout()`

---

## 成功标准

一个合格的图表包应当：
1. **包含全部 4 项核心必选图表** (经验证) ⭐
   - chart_03: 按产品划分营收
   - chart_04: 按地区划分营收
   - chart_28: DCF 敏感性
   - chart_32: 估值足球场图
2. **至少包含 25 项必选图表** (经验证)
3. **可选**：包含 1-10 张额外图表，总数达到 26-35 张
4. 所有图表视觉风格高度一致、专业
5. 高分辨率 (300 DPI)，满足打印质量要求
6. 每张图表配有清晰的标签、图例和标题
7. 包含正确的图表编号及来源标注
8. 已准备好立即嵌入 Word
9. 覆盖所有关键财务指标和分析维度
10. 通过视觉叙事有效支撑文字分析
11. 准确无误，可追溯至源数据 (模型/估值)
12. 所有图表连同索引文件打包在 zip 中

**切记**：任务 5 会将所创建的所有图表 (25-35) 散布在整篇报告中以增加密度。

---

## 输出文件

完成任务 4 后，交付成果包括：

**至少 25 项必选图表文件：**
1. chart_01_stock_price_performance.png
2. chart_02_revenue_growth_trajectory.png
3. chart_03_revenue_by_product_stacked_area.png ⭐ 核心必选
4. chart_04_revenue_by_geography_stacked_bar.png ⭐ 核心必选
5. chart_05_company_overview.png
6. chart_06_key_milestones_timeline.png
7. chart_07_organizational_structure.png
8. chart_08_product_portfolio.png
9. chart_09_customer_segmentation.png
10. chart_10_gross_margin_evolution.png
11. chart_11_ebitda_margin_progression.png
12. chart_12_free_cash_flow_trend.png
13. chart_13_operating_metrics_dashboard.png
14. chart_14_scenario_comparison.png
15. chart_15_market_size_evolution.png
16. chart_16_competitive_positioning.png
17. chart_17_market_share.png
18. chart_18_competitive_benchmarking.png
19-27. *若有可选图表，占位 19-27 编号*
28. chart_28_dcf_sensitivity_heatmap.png ⭐ 核心必选
29. chart_29_dcf_waterfall.png
30. chart_30_trading_comps_scatter.png
31. chart_31_peer_multiples_comparison.png
32. chart_32_valuation_football_field.png ⭐ 核心必选
33. chart_33_price_target_scenarios.png
34. chart_34_historical_valuation_multiples.png
35. *若有可选图表，占位编号 35*

**10 项可选图表文件 (用于补齐总数):**
- chart_19 至 chart_27, 以及 chart_35 (若已创建)

**图表索引** (1 个文本文件):
- chart_index.txt (列出所有图表的描述和类别)

**所有图表文件必须符合：**
- 300 DPI 分辨率 (印刷标准)
- 宽 6-10 英寸 (标准 Word 嵌入尺寸)
- 白色背景 (显得专业)
- PNG 格式 (无损质量)
- 可直接用于 Word 嵌入

**最后一步：打包所有图表**

创建一个包含所有图表文件及索引的 zip 压缩包：

```
[公司名称]_Charts_[日期].zip
├── chart_01_stock_price_performance.png
├── chart_02_revenue_growth_trajectory.png
├── chart_03_revenue_by_product_stacked_area.png ⭐
├── chart_04_revenue_by_geography_stacked_bar.png ⭐
├── chart_05_company_overview.png
├── ... (全部 25-35 张图表)
├── chart_28_dcf_sensitivity_heatmap.png ⭐
├── chart_32_valuation_football_field.png ⭐
├── chart_34_historical_valuation_multiples.png
└── chart_index.txt
```

**示例**：`Tesla_Charts_2024-10-28.zip`

**为何这很重要**：任务 5 将在整篇报告中散布嵌入这 25-35 张图。研报需要极高的视觉密度 (每 200-300 字一图)，因此每张图都有其用途——或是支撑特定的分析章节，或是通过视觉叙事填充页面密度。
- 确认全部 25-35 张图表齐备
- 提取图表用于任务 5（报告汇编）

---

## 后续步骤

完成任务 4 后，该压缩包将用于：
- **任务 5 (报告汇编)**：提取图表并将其嵌入到 DOCX 报告的相应位置。

4 项核心必选图表对于报告中的估值分析和财务摘要章节至关重要。

> **💡 Appendix: 领域知识小贴士**
> 
> *   **TAM (潜在市场总量)**：想象你在卖奶茶，TAM 就是全城所有喝奶茶的人加起来一年会花多少钱。它决定了你的“天花板”有多高。
> *   **DCF (现金流折现法)**：现在的 100 块比明年的 100 块值钱。DCF 就是把公司未来很多年赚到的每一分钱，按一定的贴现率算回它现在值多少钱。
> *   **WACC (加权平均资本成本)**：你可以理解为公司“借钱”的综合成本。如果 WACC 是 10%，意味着公司赚回来的钱至少要超过 10% 才能对得起投资者。
> *   **敏感性分析热力图**：就像玩参数游戏。如果折现率变一点，或者永续增长率变一点，公司的估值（目标价）会怎么变？热力图颜色越绿（深），说明变量组合下公司越值钱。
> *   **足球场图 (Football Field)**：金融圈最经典的估值汇总图。它并不是足球比赛，而是把 DCF 估、同业对比估、历史估等各种方法得出的价格区间横着叠在一起。如果这些区间有一个重叠最多的地方，那通常就是最靠谱的取值范围。
