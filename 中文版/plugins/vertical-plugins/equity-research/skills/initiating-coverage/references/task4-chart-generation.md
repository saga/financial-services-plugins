# 任务 4：图表生成 - 详细工作流

本文档提供了执行首次覆盖（initiating-coverage）技能中任务 4（图表生成）的逐步操作指南。

## 任务概览

**目的**：为报告生成 25-35 张专业的财务与商业图表。

**前提条件**：⚠️ 开始前请务必验证
- **必需**：来自任务 1 的公司研究
  - 公司历史与里程碑（用于时间轴图表）
  - 管理团队与组织架构（用于架构图表）
  - 产品矩阵（用于产品图表）
  - 客户分层特征（用于客户细分图表）
  - 竞争格局（用于竞争定位图表）
  - TAM（总可供需市场）分析（用于市场规模图表）
- **必需**：来自任务 2 的财务模型
  - 按产品/地区划分的营收数据
  - 利润率趋势
  - 预测情景对比数据
- **必需**：来自任务 3 的估值分析
  - DCF（现金流折现）敏感性分析表
  - 可比公司数据
  - 估值区间
- **必需**：外部市场数据
  - 历史股价数据（雅虎财经、彭博）
  - 历史估值倍数（图表 34 的可选项）

**⚠️ 核心严禁事项：在任务 1、2、3 全部完成之前，切勿开始此任务**

此任务依赖前三个任务的所有输出成果。在缺乏数据支撑的情况下启动，将导致图表内容缺失。

**如果任务 1、2、3 中有任何一项未完成**：请立即停止，并告知用户需要先完成哪些任务。具体要求如下：
- 任务 1：公司研究说明文档（用于 9 张图表）
- 任务 2：包含完整的 6 个工作表的财务模型（用于 8 张图表）
- 任务 3：已将估值分析工作表添加至模型中（用于 6 张图表）
- 外部数据访问权限（用于 2 张图表）

切勿尝试创建占位符图表或因数据缺失而跳过图表生成。

**输出交付物**：25-35 张专业图表文件（PNG/JPG 格式，300 DPI 分辨率）

---

## 输入数据验证

**开始前 - 请检查所有前提条件：**

### 任务 1 验证（公司研究）
- [ ] 任务 1 是否完成？（存在公司研究文档）
- [ ] 是否已记录公司历史和里程碑？（用于图表 05、06）
- [ ] 是否已描述管理团队和组织架构？（用于图表 07）
- [ ] 是否已详述产品矩阵？（用于图表 08）
- [ ] 是否已分析客户分层特征？（用于图表 09）
- [ ] 是否已梳理竞争格局？（用于图表 16、17、18）
- [ ] 是否已完成 TAM 市场测算？（用于图表 15）

### 任务 2 验证（财务模型）
- [ ] 任务 2 是否完成？（存在财务模型 Excel 文件）
- [ ] 是否具备按产品划分的营收分类数据？（用于图表 03 ⭐）
- [ ] 是否具备按地区划分的营收分类数据？（用于图表 04 ⭐）
- [ ] 历史 + 预测财务数据是否完整？（用于图表 02、10、11、12）
- [ ] 情景分析（乐观/基准/悲观）是否完成？（用于图表 14）
- [ ] 经营/运营指标是否齐备？（用于图表 13）

### 任务 3 验证（估值分析）
- [ ] 任务 3 是否完成？（估值工作表已加入模型）
- [ ] DCF 敏感性分析矩阵是否存在？（用于图表 28 ⭐）
- [ ] DCF 计算的详细分解过程是否存在？（用于图表 29）
- [ ] 可比公司数据是否已收集？（用于图表 30、31）
- [ ] 估值区间是否已计算得出？（用于图表 32 ⭐）

### 外部数据验证
- [ ] 是否能获取历史股价数据？（雅虎财经、彭博，用于图表 01）
- [ ] 是否能获取历史估值数据？（可选，用于图表 34）

**如果任何验证未通过**：
- 缺少任务 1？→ 先完成任务 1（公司研究）
- 缺少任务 2？→ 先完成任务 2（财务建模）
- 缺少任务 3？→ 先完成任务 3（估值分析）
- 缺少外部数据？→ 从雅虎财经、彭博或类似平台收集

---

## 图表清单要求：25 张必需图表 + 10 张可选图表

**重要提示**：任务 5（报告组装）会将**创建的所有图表**嵌入到整份报告中。这份报告需要高密度的视觉内容支撑（每 200-300 字配一张图表），因此请确保图表覆盖面的完整性。

### 4 张强制必需图表（不可省略） ⭐

这 4 张图表是至关重要的可视化内容，绝对不可或缺：

1. **chart_03**：按产品/业务线划分的营收 - 堆积面积图 ⭐
2. **chart_04**：按地理区域划分的营收 - 堆积柱状图 ⭐
3. **chart_28**：DCF 敏感性分析 - 双向热力图 ⭐
4. **chart_32**：综合估值图（Football Field） - 水平条形图 ⭐

### 25 张必需图表（完整基础集合）

请生成这 25 张核心图表。每一张图表在任务 5 中都有其特定的排布用途：

**投资概要部分（1 张图表）：**
- chart_01：股价历史表现（过去 12-24 个月）

**财务业绩部分（6 张图表）：**
- chart_02：营收增长轨迹
- chart_03：按产品划分的营收 - 堆积面积图 ⭐ 强制必需
- chart_04：按地区划分的营收 - 堆积柱状图 ⭐ 强制必需
- chart_10：毛利率历史演变
- chart_11：EBITDA 利润率趋势
- chart_12：自由现金流（FCF）趋势

**公司概况 (101) 部分（7 张图表）：**
- chart_05：公司概况/发展历程
- chart_06：关键里程碑时间轴
- chart_07：组织架构
- chart_08：产品矩阵概览
- chart_09：客户分层特征
- chart_15：市场规模演进（TAM）
- chart_16：竞争定位矩阵

**竞争与市场部分（2 张图表）：**
- chart_17：市场份额分布
- chart_18：竞争基准对标分析

**情景分析部分（2 张图表）：**
- chart_13：核心运营指标仪表盘
- chart_14：情景对比预测（乐观/基准/悲观）

**估值分析部分（7 张图表）：**
- chart_28：DCF 敏感性分析热力图 ⭐ 强制必需
- chart_29：DCF 估值瀑布图
- chart_30：交易可比公司散点图
- chart_31：同业估值倍数对比
- chart_32：综合估值图（Football Field） ⭐ 强制必需
- chart_33：目标价情景推演
- chart_34：历史估值倍数趋势

**总计：25 张必需图表**

### 10 张可选图表（用于扩展至 30-35 张范围）

添加以下图表以提供更高的视觉密度和叙事逻辑（总图表数达到 26-35 张）：

- chart_19：获客趋势分析
- chart_20：单位经济效益（Unit Economics）演变
- chart_21：产品研发路线图
- chart_22：地域扩张版图
- chart_23：研发（R&D）投入趋势
- chart_24：销售与营销（S&M）效率分析
- chart_25：营运资金运营趋势
- chart_26：债务到期时间表
- chart_27：股权结构
- chart_35：分析师目标价分布情况

**总数范围：25-35 张图表（25 张必需 + 0-10 张可选）**

---

## 必需图表的数据源映射关系

确保准确理解每张图表的数据源落脚点：

### 来自任务 1（公司研究） - 9 张图表
- chart_05：公司概况 → 任务 1：公司概况部分
- chart_06：关键里程碑 → 任务 1：公司历史部分
- chart_07：架构图 → 任务 1：管理团队部分
- chart_08：产品矩阵 → 任务 1：产品与服务部分
- chart_09：客户分层特征 → 任务 1：客户与市场进入（GTM）部分
- chart_15：市场规模演进 → 任务 1：市场机遇（TAM）部分
- chart_16：竞争定位 → 任务 1：竞争格局部分
- chart_17：市场份额 → 任务 1：竞争格局部分
- chart_18：竞争基准对标 → 任务 1：竞争格局部分

### 来自任务 2（财务模型） - 8 张图表
- chart_02：营收增长 → 利润表工作表（营收行）
- chart_03：按产品划分的营收 ⭐ → 营收模型工作表（产品拆分）
- chart_04：按地区划分的营收 ⭐ → 营收模型工作表（地区拆分）
- chart_10：毛利率 → 利润表工作表（毛利润 / 营收）
- chart_11：EBITDA利润率 → 利润表工作表（EBITDA / 营收）
- chart_12：自由现金流 → 现金流量表（经营现金流 CFO - 资本支出 CapEx）
- chart_13：运营指标 → 多个工作表（利润表、现金流量表）
- chart_14：情景对比 → 情景分析工作表（乐观/基准/悲观）

### 来自任务 3（估值分析） - 6 张图表
- chart_28：DCF敏感性分析 ⭐ → 敏感性分析工作表
- chart_29：DCF瀑布图 → DCF估值工作表（企业价值构成部分）
- chart_30：交易可比对标散点图 → 可比公司工作表
- chart_31：同业估值倍数 → 可比公司工作表
- chart_32：综合估值图 ⭐ → 估值总结工作表
- chart_33：目标价情景推演 → 估值总结工作表（或从情景分析测算）

### 来自外部数据源 - 2 张图表
- chart_01：股价历史表现 → 雅虎财经、彭博、Alpha Vantage
- chart_34：历史估值倍数 → 雅虎财经、彭博（历史 P/E、EV/EBITDA）

**重要提示**：需要所有三个核心任务（1、2、3）全部完成，外加外部数据访问权限，才能生成完整的 25 张必需图表。

---

## 图表生成的逐步工作流

### 第 1 步：环境配置

**安装必需的环境库：**
```bash
pip install matplotlib seaborn pandas numpy plotly
```

**创建 Python 脚本头部文件：**
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

# 全局配置参数
DPI = 300
FIGURE_WIDTH = 10
FIGURE_HEIGHT = 6
TITLE_FONT_SIZE = 14
AXIS_FONT_SIZE = 12
LABEL_FONT_SIZE = 10
```

### 第 2 步：从模型与估值中提取数据

#### A. 提取营收数据
```python
# 按产品分类的营收（来自任务 2 模型）
years = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029]

# 从 Excel 提取或从模型手动设定映射
product_a = [100, 120, 145, 175, 210, 252, 302, 363, 435, 522]
product_b = [80, 95, 115, 138, 165, 198, 238, 285, 342, 411]
product_c = [50, 62, 78, 98, 122, 153, 191, 239, 299, 374]
product_d = [30, 38, 48, 61, 77, 97, 122, 153, 191, 239]

# 按地理区域分类的营收
north_america = [150, 180, 220, 265, 320, 384, 461, 553, 664, 797]
europe = [80, 95, 115, 140, 170, 204, 245, 294, 353, 423]
asia_pacific = [40, 50, 63, 80, 101, 127, 159, 199, 249, 311]
rest_of_world = [20, 25, 32, 40, 51, 64, 80, 100, 125, 156]
```

#### B. 提取利润率数据
```python
# 利润率历史与预测演进
gross_margin = [58.0, 59.2, 60.5, 61.8, 63.0, 64.5, 66.0, 67.0, 67.5, 68.0]
ebitda_margin = [12.0, 15.5, 18.8, 22.0, 25.0, 28.0, 30.5, 32.0, 33.0, 34.0]
fcf_margin = [8.0, 11.0, 14.5, 18.0, 21.0, 24.0, 26.5, 28.0, 29.0, 30.0]
```

#### C. 提取 DCF 敏感性数据
```python
# DCF 敏感性分析（来自任务 3 估值）
wacc_values = [7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
terminal_growth = [1.5, 2.0, 2.5, 3.0, 3.5]

# 每股隐含价格矩阵（行 = WACC，列 = 永续增长率）
dcf_sensitivity = np.array([
    [66, 71, 76, 82, 89],
    [58, 62, 67, 72, 78],
    [52, 55, 59, 63, 68],
    [47, 50, 53, 56, 60],
    [42, 45, 48, 51, 54],
    [39, 41, 44, 46, 49]
])
```

#### D. 提取估值区间范围
```python
# 综合估值图 / Football Field（来自任务 3）
valuation_methods = ['DCF 现金流折现分析', '交易可比公司\n(NTM)', '历史交易先例']
valuation_low = [48, 45, 52]
valuation_high = [62, 57, 66]
current_price = 50
target_price = 55
```

### 第 3 步：创建强制必需的图表

#### 图表 1：按产品划分的营收 - 堆积面积图 ⭐ 强制必需

```python
def create_revenue_by_product_chart():
    """创建按产品划分营收的堆积面积图"""

    fig, ax = plt.subplots(figsize=(10, 6))

    # 创建堆积面积图
    ax.stackplot(years, product_a, product_b, product_c, product_d,
                 labels=['产品 A', '产品 B', '产品 C', '产品 D'],
                 colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
                 alpha=0.8)

    # 格式化图表
    ax.set_xlabel('年份 (Year)', fontsize=12, fontweight='bold')
    ax.set_ylabel('营收（百万美元）', fontsize=12, fontweight='bold')
    ax.set_title('图表 3 - 按产品/业务线划分的营收 (2020-2029E)',
                 fontsize=14, fontweight='bold', pad=20)

    # 图例设置
    ax.legend(loc='upper left', frameon=False, fontsize=10)

    # 添加网格线
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    # 移除上方与右侧边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 添加区分实际与预测年份的垂直参考线
    ax.axvline(x=2024, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax.text(2024.2, ax.get_ylim()[1]*0.95, '预测期 →',
            fontsize=9, color='gray', ha='left')

    # 数据来源注释
    fig.text(0.12, 0.02, '来源：公司数据，[机构名称] 测算',
             fontsize=9, style='italic', color='gray')

    # 保存图片
    plt.tight_layout()
    plt.savefig('chart_03_revenue_by_product_stacked_area.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 已生成: chart_03_revenue_by_product_stacked_area.png")

create_revenue_by_product_chart()
```

#### 图表 2：按地区划分的营收 - 堆积柱状图 ⭐ 强制必需

```python
def create_revenue_by_geography_chart():
    """创建按地理区域划分营收的堆积柱状图"""

    years_labels = ['2020', '2021', '2022', '2023', '2024',
                    '2025E', '2026E', '2027E', '2028E', '2029E']

    fig, ax = plt.subplots(figsize=(10, 6))

    # 创建堆积柱状图
    width = 0.6
    x = np.arange(len(years_labels))

    p1 = ax.bar(x, north_america, width, label='北美', color='#1f77b4')
    p2 = ax.bar(x, europe, width, bottom=north_america,
                label='欧洲', color='#ff7f0e')
    p3 = ax.bar(x, asia_pacific, width,
                bottom=np.array(north_america) + np.array(europe),
                label='亚太地区', color='#2ca02c')
    p4 = ax.bar(x, rest_of_world, width,
                bottom=np.array(north_america) + np.array(europe) + np.array(asia_pacific),
                label='世界其他地区', color='#d62728')

    # 格式化图表
    ax.set_xlabel('年份 (Year)', fontsize=12, fontweight='bold')
    ax.set_ylabel('营收（百万美元）', fontsize=12, fontweight='bold')
    ax.set_title('图表 4 - 按地理区域划分的营收 (2020-2029E)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(years_labels, rotation=45, ha='right')

    # 图例设置
    ax.legend(loc='upper left', frameon=False, fontsize=10)

    # 添加网格线
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    # 移除上方与右侧边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 数据来源注释
    fig.text(0.12, 0.02, '来源：公司数据，[机构名称] 测算',
             fontsize=9, style='italic', color='gray')

    # 保存图片
    plt.tight_layout()
    plt.savefig('chart_04_revenue_by_geography_stacked_bar.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 已生成: chart_04_revenue_by_geography_stacked_bar.png")

create_revenue_by_geography_chart()
```

#### 图表 3：DCF 敏感性分析 - 热力图 ⭐ 强制必需

```python
def create_dcf_sensitivity_heatmap():
    """创建 DCF 敏感性分析热力图"""

    # 创建数据框结构
    df = pd.DataFrame(dcf_sensitivity,
                      index=[f'{w}%' for w in wacc_values],
                      columns=[f'{g}%' for g in terminal_growth])

    fig, ax = plt.subplots(figsize=(8, 6))

    # 生成热力图
    sns.heatmap(df, annot=True, fmt='d', cmap='RdYlGn',
                cbar_kws={'label': '隐含目标价 ($)'},
                linewidths=0.5, linecolor='white',
                ax=ax, vmin=35, vmax=95)

    # 格式化图表
    ax.set_xlabel('永续增长率 (Terminal Growth Rate)', fontsize=12, fontweight='bold')
    ax.set_ylabel('加权平均资本成本 (WACC)', fontsize=12, fontweight='bold')
    ax.set_title('图表 28 - DCF 敏感性分析（美元/股）',
                 fontsize=14, fontweight='bold', pad=20)

    # 旋转 Y 轴坐标标签
    plt.yticks(rotation=0)

    # 数据来源注释
    fig.text(0.12, 0.02, '来源：[机构名称] 测算',
             fontsize=9, style='italic', color='gray')

    # 保存图片
    plt.tight_layout()
    plt.savefig('chart_28_dcf_sensitivity_heatmap.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 已生成: chart_28_dcf_sensitivity_heatmap.png")

create_dcf_sensitivity_heatmap()
```

#### 图表 4：综合估值图（Football Field） ⭐ 强制必需

```python
def create_valuation_football_field():
    """创建综合估值总结图（Football Field）"""

    fig, ax = plt.subplots(figsize=(10, 5))

    # 创建水平条形图
    y_positions = np.arange(len(valuation_methods))
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

    for i, (method, low, high, color) in enumerate(
            zip(valuation_methods, valuation_low, valuation_high, colors)):
        ax.barh(i, high - low, left=low, height=0.6,
                color=color, alpha=0.7, label=method)

        # 在两端标注数值标签
        ax.text(low - 1, i, f'${low}', va='center', ha='right', fontsize=10)
        ax.text(high + 1, i, f'${high}', va='center', ha='left', fontsize=10)

    # 刻画当前价格线
    ax.axvline(x=current_price, color='red', linestyle='--', linewidth=2,
               label=f'现价: ${current_price}', alpha=0.7)

    # 刻画目标价基准线
    ax.axvline(x=target_price, color='black', linestyle='-', linewidth=2,
               label=f'目标价: ${target_price}')

    # 格式化图表
    ax.set_yticks(y_positions)
    ax.set_yticklabels(valuation_methods, fontsize=11)
    ax.set_xlabel('每股价格 ($)', fontsize=12, fontweight='bold')
    ax.set_title('图表 32 - 综合估值评估图 (Valuation Football Field)',
                 fontsize=14, fontweight='bold', pad=20)

    # 设置 X 轴边界
    ax.set_xlim(40, 70)

    # 隐藏边框线
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # 添加网格线
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    # 图例设置
    ax.legend(loc='upper right', frameon=False, fontsize=9)

    # 数据来源注释
    fig.text(0.12, 0.02, '来源：[机构名称] 测算',
             fontsize=9, style='italic', color='gray')

    # 保存图片
    plt.tight_layout()
    plt.savefig('chart_32_valuation_football_field.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 已生成: chart_32_valuation_football_field.png")

create_valuation_football_field()
```

### 第 4 步：创建剩余的必需图表（图表 1-34）

通过从必需清单中创建剩余部分的图表来**完成全部 25 张必需图表的构建**。每张图在最终的任务 5 中都肩负着特定的展示使命。

#### 投资概要（1 张图表）
```python
# chart_01：股价历史表现（过去 12-24 个月）
# - 展示股价随时间演变并与大盘指数对标的折线图
# - 应用于最终研究报告的卷首定调（Page 1）
```

#### 财务业绩（在 chart_03 和 chart_04 之外的 5 张图表）
```python
# chart_02：营收增长轨迹
# chart_10：毛利率历史演变
# chart_11：EBITDA 利润率趋势
# chart_12：自由现金流趋势
# chart_14：情景对比分析（乐观/基准/悲观）
```

#### 公司概况 (101) 部分（7 张图表）
```python
# chart_05：公司概况/发展历程
# chart_06：关键里程碑时间轴
# chart_07：组织架构
# chart_08：产品矩阵概览
# chart_09：客户分层特征
# chart_15：市场规模演进（TAM）
# chart_16：竞争定位矩阵
```

#### 竞争与市场分析（2 张图表）
```python
# chart_17：市场份额分布
# chart_18：竞争基准对标分析
```

#### 情景分析（1 张图表）
```python
# chart_13：核心运营指标仪表盘
```

#### 估值分析环节（在 chart_28 和 chart_32 之外的 6 张图表）
```python
# chart_29：DCF 估值瀑布图
# chart_30：交易可比公司散点图
# chart_31：同业估值倍数对比矩阵
# chart_33：目标价情景推演
# chart_34：历史估值倍数演变
```

**对所有图表应用一致的排版格式标准：**
- 300 DPI 高清分辨率
- 统一协调的专业色彩构成
- 清晰的标签、图例与标题体系
- 标准的图表编号（如：“图表 5 - 公司发展时间轴”）
- 底部附带标准的数据来源引述

### 第 4B 步：创建可选补充图表（迈向 26-35 张的总量）

**可选配置**：从下述列表中增加 1-10 张拓展图表，以便为研报提供更加丰满的视觉密度表现：

```python
# chart_19：获客趋势分析
# chart_20：单位经济效益（Unit Economics）演变
# chart_21：产品研发路线图
# chart_22：地域扩张版图
# chart_23：研发投入（R&D）趋势
# chart_24：销售与营销（S&M）效率分析
# chart_25：营运资金（Working Capital）运营趋势
# chart_26：债务到期时间表
# chart_27：股权架构概览
# chart_35：华尔街分析师目标价集中度分布图
```

这些可选图表提供了额外的视觉化商业叙事，充分助力在整体报告（任务 5）中顺利达成“每 200-300 个字配一张图表”的排版密度目标。

### 第 5 步：生成图表索引清单

利用代码自动生成一个专门记录所有图表的文本索引指南文件：

```python
def create_chart_index():
    """生成全套图表库索引指南"""

    # 25 张必需的标准图表
    required_charts = [
        "chart_01_stock_price_performance.png - 股价历史表现 (12-24M)",
        "chart_02_revenue_growth_trajectory.png - 营收增长演变轨迹",
        "chart_03_revenue_by_product_stacked_area.png - 按产品划分营收 [强制必需]",
        "chart_04_revenue_by_geography_stacked_bar.png - 按地区划分营收 [强制必需]",
        "chart_05_company_overview.png - 公司概况/发展历程",
        "chart_06_key_milestones_timeline.png - 核心里程碑时间轴",
        "chart_07_organizational_structure.png - 公司内部组织结构",
        "chart_08_product_portfolio.png - 主营产品矩阵结构评估",
        "chart_09_customer_segmentation.png - 核心客户客群分层洞察",
        "chart_10_gross_margin_evolution.png - 历史毛利率水平纵览",
        "chart_11_ebitda_margin_progression.png - EBITDA利润转化效率趋势",
        "chart_12_free_cash_flow_trend.png - 企业自由现金流走向追踪",
        "chart_13_operating_metrics_dashboard.png - 企业经营核心运营指标概览",
        "chart_14_scenario_comparison.png - 未来基本面情景展望与折算（乐观/基准/悲观）",
        "chart_15_market_size_evolution.png - TAM 总可供需市场池扩张规模",
        "chart_16_competitive_positioning.png - 竞争象限与定位格局",
        "chart_17_market_share.png - 现有市场集中度解析",
        "chart_18_competitive_benchmarking.png - 同业玩家营运基准对比",
        "chart_28_dcf_sensitivity_heatmap.png - DCF参数敏感测试热力分布 [强制必需]",
        "chart_29_dcf_waterfall.png - DCF 折现模型企业价值转化层级",
        "chart_30_trading_comps_scatter.png - 交易比较公司动态水平测试",
        "chart_31_peer_multiples_comparison.png - 二级市场同行多重估值倍数对比",
        "chart_32_valuation_football_field.png - 券商足球场式合理估值区间 [强制必需]",
        "chart_33_price_target_scenarios.png - 针对目标价的情景假设空间",
        "chart_34_historical_valuation_multiples.png - 自身历史估值定价水位回顾",
    ]

    # 添加达到 26-35 张指标用的 10 张增量可选库
    optional_charts = [
        "chart_19_customer_acquisition_trends.png - 客源斩获与引流走势 [可选补充]",
        "chart_20_unit_economics_evolution.png - 底层单体经济效益走向 [可选补充]",
        "chart_21_product_roadmap_timeline.png - 长期产品开发及迭代部署地图 [可选补充]",
        "chart_22_geographic_expansion_map.png - 下游触达与全球业务渗透版图 [可选补充]",
        "chart_23_rd_investment_trends.png - 技术护城河：研发资本化与资源投入比重 [可选补充]",
        "chart_24_sales_marketing_efficiency.png - 销售宣发与市场培育效能分析 [可选补充]",
        "chart_25_working_capital_trends.png - 营运资金占用流转周期与趋势 [可选补充]",
        "chart_26_debt_maturity_schedule.png - 资产负债压力：长期未偿本金分布矩阵 [可选补充]",
        "chart_27_ownership_structure.png - 外部实控与二级股东基本盘比例 [可选补充]",
        "chart_35_analyst_price_targets.png - 华尔街同行目标价一致预期落点 [可选补充]",
    ]

    with open('chart_index.txt', 'w') as f:
        f.write("[公司名称] 公司首次覆盖深度研究图表生成索引指南\n")
        f.write("=" * 60 + "\n\n")

        f.write("4 张绝对强制必需图表要素（报告中必须现身）：\n")
        f.write("- chart_03：按核心产品划分营收演进模式（堆叠面积形） ⭐\n")
        f.write("- chart_04：按国际与地区拆分营收流水规模（堆砌柱状形） ⭐\n")
        f.write("- chart_28：DCF内在价值敏感带（温度热力形） ⭐\n")
        f.write("- chart_32：综合目标区间落点汇总（水平足球场分布形） ⭐\n\n")

        f.write("基准的 25 张体系必要成图：\n")
        for chart in required_charts:
            f.write(f"  {chart}\n")

        f.write("\n10 张可选用的弹性扩容图表（针对 26 至 35 幅图的最终满编诉求）：\n")
        for chart in optional_charts:
            f.write(f"  {chart}\n")

        f.write("\n" + "=" * 60 + "\n")
        f.write("执行要求：在随后的『报告成卷拼装』（任务 5）阶段，这批规模达到 25-35 张的素材，\n")
        f.write("将被强制性下沉式嵌入文章各细分板块内，用于达成硬性学术视觉覆盖指标（即保证约每 200-300 字即可见图一张的篇幅密度）。\n")

    print("✓ 已生成: chart_index.txt")

create_chart_index()
```

### 第 6 步：质量复检

**运行全量验查校验：**

```python
import os

def verify_charts():
    """核实整体验收清单及图表生成质量与情况"""

    mandatory_charts = [
        'chart_03_revenue_by_product_stacked_area.png',
        'chart_04_revenue_by_geography_stacked_bar.png',
        'chart_28_dcf_sensitivity_heatmap.png',
        'chart_32_valuation_football_field.png'
    ]

    print("\n" + "="*60)
    print("图表成片质检验收评估进程")
    print("="*60)

    # 查验四个绝对刚需核心图表
    print("\n1. 强制性重点核对:")
    all_mandatory_present = True
    for chart in mandatory_charts:
        if os.path.exists(chart):
            size = os.path.getsize(chart) / 1024  # KB
            print(f"   ✓ {chart} ({size:.1f} KB)")
        else:
            print(f"   ✗ 严重丢失环节: {chart}")
            all_mandatory_present = False

    # 统计所获图表的绝对数量
    chart_files = [f for f in os.listdir('.') if f.startswith('chart_') and f.endswith('.png')]
    print(f"\n2. 累计交付规模: {len(chart_files)} 张图件素材")
    print(f"   对标产能规划: 25-35 张")
    print(f"   总体状态评定: {'✓ 合规达标 (PASS)' if 25 <= len(chart_files) <= 35 else '⚠ 提示警告 (WARNING)'}")

    # 对于图片质量进行容量级检测（300 DPI 正常输出不应处于 50KB 线以下）
    print("\n3. 解析度输出体积查验:")
    small_files = []
    for chart in chart_files[:5]:  # 执行前五张成品的首末位抽样
        size = os.path.getsize(chart) / 1024
        if size < 50:
            small_files.append(chart)
        print(f"   {chart}: {size:.1f} KB")

    if small_files:
        print(f"   ⚠ 提示警告: 出现 {len(small_files)} 份疑似解析压缩质量不合格/数据低频图件的隐患素材。")
    else:
        print(f"   ✓ 全部抽样源头像素质量表现合规。")

    # 给出最终执行判定
    print("\n" + "="*60)
    if all_mandatory_present and 25 <= len(chart_files) <= 35:
        print("✓ 全流程检验合规通过 - 已具备发往任务 5 环节流转资格")
    else:
        print("✗ 核验流程告负 - 烦请重新清点缺失或未执行生成的任务图表！")
    print("="*60 + "\n")

verify_charts()
```

---

## 质量审核标准

### 视觉传达水准
- [ ] 确保高超的分辨率画质输出（底线 300 DPI 分辨率）
- [ ] 专业调性和克制的商业色彩组合系统（在所有图片体系中应整齐划一）
- [ ] 标签注释具有完全的可读性（禁止采用任何低于 9pt 磅值的数据标记）
- [ ] 正确及严谨的屏幕长宽比约束控制（不容丝毫变形）
- [ ] 杜绝任何形式的锯齿、噪点及渲染马赛克

### 金融数据公允度
- [ ] 信息底表源头一致，确保其数值直接等同（与财务建模卷宗与估值精算原表同步）
- [ ] 货币计量、度量单位与数量级准确无误地附注标识（百万美元计价档次，复合年均增速比率符号等界定清晰）
- [ ] 妥当公允的尺度定义与 Y/X 轴取值比例映射
- [ ] 所有图中时序演进步伐（日历计算基准）互通、统一且不存在错位
- [ ] 所有推演路径经历过缜密验证测算体系回溯

### 版式与文本格式质量
- [ ] 统驭全篇设计语言与排布模式高度统一
- [ ] 严格遵循严密的报告图号推演法则体系编定进行标识（有序递进序列标值推进）
- [ ] 清爽醒目，具有统领意义与描述能力的副词修饰标题栏内容
- [ ] 各版位尾部附加上严格符合行业审计视角的规范化追溯出处、素材数据来源说明语句
- [ ] 满足卖方机构/投资银行出版标准的专业体面视觉美学层级

### 验收交付完整度
- [ ] 包含全体 4 项“免战牌不认”核心强制要点的模型全开制作产出达成落实情况
- [ ] 保底规模控制维持在既定要求 25 张起始线-35幅总量的约束阈内
- [ ] 恰当而具备清晰业务对应导向解释功能意义的最终图名文件命名的合规执行工作
- [ ] 配套交付对应的总索引图志列表说明导航文书结构
- [ ] 素材库整体表现达到已完全直接可在 Word 原生框架下零障碍排版挂载组装就绪的使用门槛

---

## 核心商业图表范式参考

### 如何正确应用每一类专属统计金融图形：

**折线图（Line Charts）**：着重呈现带时间流动特征的宏观基本面大周期时序历史轨迹演变进程（诸如流水进账历史周期波峰波谷，盈利抽水线毛利率边际效用的兴衰拐点变相，二级市场交投曲线沉浮等）

**堆积面积图（Stacked Area）**：透视按照具体产品结构分割重组的混合营收贡献模型 ⭐，勾勒出 TAM 大盘内部格局配比生态圈演进史变迁切片

**堆积柱状图（Stacked Bar）**：常用来直观展示细分地缘区域、跨洋地域矩阵维度的总营收拆解 ⭐，或各个单季度的绝对业绩总流水累加量组成堆砌对比反馈

**热力图（Heatmap）**：承办 DCF 前瞻性关键参量交叉博弈预警灵敏度/敏感性极差沙盘演练实验体系 ⭐，或是相关性逻辑矩阵阵列网格探测

**水平条形图（Horizontal Bar）**：统领最终估值核心结案陈词报告大局的结论图腾——Football Field（综合估值区间比武场体系） ⭐，也是同行实力排位赛名次座次的揭榜首发形式

**瀑布图（Waterfall）**：财务数字水池与进出流水账本转换路径演绎拆解剖析的最佳桥梁载体结构（毛利结构进出大账透视转换分析、DCF 企业价值（Enterprise Value）构型逻辑逐步组装大纲建构推波演进推导）

**散点分布/气泡图（Scatter/Bubble）**：业绩与估值的共振表现力十字参考系统系坐标轴博弈（用以描绘预期复合增速大饼画幅大小如何左右市场对于未来对标定价倍数溢价认可度之间的权衡），或直接运用于同业跑道厮杀实力站位生态位的点位投射标绘刻画等情境

**二维矩阵/九宫格（2×2 Matrix）**：梳理各路玩家优势防线的差异化护城河高墙防御竞争定位排兵布阵大盘局势图鉴，抑或用作主营品牌产品线战矩阵纵深战略卡位战的矩阵排列诊断阵列概览

---

## 交付文件规范与通用命名法则制度约束

**始终雷打不动地恪守并维系实行以下这种定型格式规范模式：**
```
chart_[图号序号序列]_[内容缩写释义阐释].png

示例展示：
chart_01_stock_price_performance.png
chart_03_revenue_by_product_stacked_area.png
chart_28_dcf_sensitivity_heatmap.png
```

**所有图片均按其预计在研报正文展示框架结构内的顺序排列规则排号**（注意：这与它们是在哪个程序操作批次里面被加工创作生成完毕先后时间顺序无关！）。

---

## 常见绘图与视觉产出流程阻碍及对冲方案

### 问题 1：颗粒度及像素输出贫瘠粗糙
**表象**：生成结果呈献斑驳的马赛克虚焦或者锯齿
**排除手段**：务必要保障指令代码里写入 `dpi=300` 参数给到 `plt.savefig()`

### 问题 2：图样边缘溢界丢失文本/边界裁损
**表象**：轴向数值标题或刻度尺文本边缘截断断头显示
**排除手段**：果断选用 `bbox_inches='tight'` 这个裁边护航防卫保护锁参数给到 `plt.savefig()` 调用中去

### 问题 3：审美降维与配色不雅
**表象**：默认的绘图着色杂乱无章难登大型专业路演研报正堂之雅
**排除手段**：直接调取成名立腕广受推崇的高规格调色板配色（如：Tableau10），亦或索性严格定制一套金融机构自身的专业企业门面专用品牌专属调色板去全盘驾驭和覆盖全局渲染

### 问题 4：刻度坐标体系标号文字踩踏挤压
**表象**：图表底座横轴的文字相互重叠辨识率归零
**排除手段**：将其予以倾斜轴转错位排布处理操作（例如直接设置附加：`rotation=45` 角度斜转处理解决这一顽疾冲突），再或全局缩小底线说明项标尺字号等综合调试对策

### 问题 5：巨幅浪费边距的空洞版面失调
**表象**：真正承载主体信息效能区域萎缩狭促、而周围泛散着海量巨幅刺眼而无益的留白荒漠区带
**排除手段**：下达保存出图落印确认文件终稿命令代码之前呼叫排版收敛聚合紧固指令函数——运用 `plt.tight_layout()` 介入排版清洗干预整装作业

---

## 交付物合格性核心判定标准（验收达标成功铁律准绳红线规制要求）

一套达到优秀质感的完满商业图标成图组件资产包体系需完美符合：
1. **彻底并且是毫无保留地涵括交齐全部 4 类绝对不可缺省图样**并落实通过系统校准筛查环节 ⭐
   - chart_03：按核心产品明细拆解大盘流水矩阵版图
   - chart_04：全球地域跨度业务吞吐版图拆解结构
   - chart_28：DCF（折现）参数边际波动敏感区震荡沙盘
   - chart_32：综合足尺估值评估空间交汇定准大图标杆（Football Field）
2. **总共生成并建制至少达到了不低于 25 张以上的绝对主力大基础刚需基本盘数量图示库存池**并过检（确认核算通过）
3. **可扩展弹性选项：依据需量追加的 1-10 张拓展内容图形素材**共同合力搭建达成了总数量逼近了 26-35 这条高压线区间红线阈限总量的丰满骨架阵容库仓储
4. 统驭所有生成的视觉素材具有整齐划一具备行业水准的机构专业投行级商业配色外衣呈现质感体系风貌
5. 图形像素的精密性经得起各类高清实物专业印刷级（具备绝不低于 300 DPI 分辨率素质标准起点约束下限要求的）严格拷问
6. 图面主体任何地方存在的信息与文字体系的传递：各个分级明细解说的标题名称解说、副职数据批注题注及核心数据走势的图例解说体系全都要求清清楚楚干干净净
7. 图谱底侧皆包含有具备溯源出处凭证和正确依序推算的“图片序号”字样系统编号序列管理系统制度支持架构排布矩阵系统
8. 当即可以实现向报告 Word 母本里随意投送装填和毫无阻碍挂载调用渲染零瑕疵直接可商用的就绪实景水平要求地步境界要求
9. 全面横跨并完整覆盖剖析透视该受调研剖析标的全盘财务基石脉络分析精要骨架体系和运营机体生态
10. 全篇形成与文字文案书面内容能够达成珠联璧合、琴瑟和鸣般的深层次图文多模态深度逻辑相互补充的互为因果协同讲故事效果体现的专业商业图形报告分析研习文本整体表现感染力
11. 精准度经得起财务数据与资产原模建仓底层估值核心数据的逐帧核资校对与推演审计溯源排查洗礼考验
12. Tüm图样库存及其检索指南均整齐无误归置封装入拉链闭锁 zip 包封保存留档以作呈递

**请牢记**：随后的任务 5 将毫无保留地提取应用、调用排布上述生成的全部所有的所有图样图示心血素材（规模 25-35 构筑全量），旨在密布排兵布阵交差组合嵌入穿插全本长文深度研报报告大部头整体篇幅之中的全领域内去深度充实整体密集的图表内容信息数据展示度要求标准展示目的呈现。

---

## 最终打包交付产物规范要求表单

当一切就绪并彻底闭环攻克完毕任务 4 周期的节点之后，应该对外交付提交包括如下内容物清单成果展示架构档案内容全家福产品清单：

**至少绝对涵盖最低不少于规模指标为 25 张的基本功底必备图册文件组包底线池:**
1. chart_01_stock_price_performance.png
2. chart_02_revenue_growth_trajectory.png
3. chart_03_revenue_by_product_stacked_area.png ⭐ 强制绝对必需要素组件
4. chart_04_revenue_by_geography_stacked_bar.png ⭐ 强制绝对必需要素组件
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
19-27. *此号段资源顺位空间虚席以为给可选补充资源扩军排兵预留序列占位留存用途机制*
28. chart_28_dcf_sensitivity_heatmap.png ⭐ 强制绝对必需要素组件
29. chart_29_dcf_waterfall.png
30. chart_30_trading_comps_scatter.png
31. chart_31_peer_multiples_comparison.png
32. chart_32_valuation_football_field.png ⭐ 强制绝对必需要素组件
33. chart_33_price_target_scenarios.png
34. chart_34_historical_valuation_multiples.png
35. *备用预案选项末尾兜底扩招位占坑保留座席备选项机制池空间序列*

**规模达到 10 张上限区间的额外附加火力可选图件池战备库（用以冲击冲顶 26-35 成片总规模限高天花板高位成就上限体系战果量产数指标）:**
- 序列横跨 chart_19 一路下探延拓直至涵盖 chart_27、并且末尾包揽 chart_35（如果有顺手生成制作落实下来的情况的话）的所有上述衍生附加加分项图像文件列表明细单。

**图表清单总编表大纲索引指引路线地图文本（必须仅包含制作单独留存一份单一 1 个文件的文本体格式档案）:**
- chart_index.txt 文件单行文本（分门别类明晰刻画所有各类涵盖了图形品类的全集图谱列表及其所隶属属性细分标签门类名谓名称归类体系阵列）

**在此务必郑重重申申明约束并再次强化确认强调——对每一张每一幅出厂图表图形图片的格式约束红线纪律下限门槛底线标准绝不可违拗和让步：**
- 高下潜能耐打的 300 DPI 分辨率打印输出商用级清晰级解析还原质量（用以去迎接胜任物理实体报告影印级印刷输出发版出厂出版级别专业质量检阅）
- 保持横轴幅度约维持在 6-10 英寸区间的面幅尺寸范围规格区间内（这亦即全球通用的标准正规商业机构的统一化规范主流标准化规范商用版 Word 框架文档内置组件的标准插入标准模板匹配嵌入契合框定容纳预留排版预设框宽尺寸基准线尺寸）
- 配备纯美白底背景墙色系色调底基（体现恪守严谨的专业金融工笔和企业商用纯净气质表现）
- 选用且仅选用 PNG 图片介质存图存库落盘打包压缩格式进行承载容器封装（彻底消除所有一切非 PNG 图片编码机制格式附带衍生的信息损伤失真以及噪点和马赛克残次残影毛边留存残留瑕疵杂质的折损破坏降质弊病顽疾侵扰隐患问题存在）
- 确保做到一经生成便具有做到随即完全脱手可以立即拿取就能够信手拈来开箱即用当即直接一秒被嵌装植入融合进任意正统派 Word 文书大本营里的就绪预装备齐状态阶段水平要求地步。

**终局操作决胜环节：将其大圆满地做全集统合打包归类打包闭环压袋合拢交付：**

将一切所产出的零散碎图片碎片全部统一收拢集中整编制归入囊中集中打包打卷捆扎至一个 ZIP 级高阶合集包裹里去；并且需妥帖装入这本伴随导读作用的导航清单表文件做指引：

```
[被调研公司的名谓全称]_Charts_[制作产出落地当前日表日期标签代码标识].zip
├── chart_01_stock_price_performance.png
├── chart_02_revenue_growth_trajectory.png
├── chart_03_revenue_by_product_stacked_area.png ⭐
├── chart_04_revenue_by_geography_stacked_bar.png ⭐
├── chart_05_company_overview.png
├── ... (包括所有其余那排量浩浩荡荡高达 25-35 张成图规模在内的诸多图件实体素材文件集群军团序列)
├── chart_28_dcf_sensitivity_heatmap.png ⭐
├── chart_32_valuation_football_field.png ⭐
├── chart_34_historical_valuation_multiples.png
└── chart_index.txt
```

**模拟示范样板案例展示说明**: `Tesla_Charts_2024-10-28.zip`

**为何要在此关头做到这份事无巨细苛求地步的深层苦心用意所在揭秘：** 紧随其后的接力棒——“任务 5（撰文落笔与总报告装订车间）”，将会彻底抽调征用这股规模高达（25-35 张）的宏大神图库存军备储备全本集锦，并将它们悉数拆散零星分布到这本厚重如砖的机构报告大部头卷宗全盘的所有血脉枝节角落。该分析长卷本身极度饥渴于视觉元素的高能耗补给填埋堆砌量（行文密度考核金标准红线指标：每行进 200-300 个词幅必须见配副图调剂视觉疲劳的严苛工业排队化规定指标操作要求规矩）。从而确保您精心制作提炼出来的这套心血库图片，无论它是用于特定数理框架分析证明推演的利剑工具剖析解读手段支撑工具，还是用以在宏图大局上实现舒缓视觉神经进行视觉排版讲大故事进行文字版面的丰满空间架构填充等任意意图意指目的用意，最终也终究会各得其所落户归属各司其职散列驻防去坚守住整个整篇研报文章生态版图之上的属于它自己独有的那一方防区领地排版空窗缺口用以提升填充厚重扎实质感表现发挥功效的作用！
- 详实确认比对确认和审计整全的 25-35 张战队编制数目的齐全达标符合满编度与齐装满员就绪入库就绪状况无虞。
- 提取战果图片并执行交接分批入库准备等待执行启动进入下一关底终章重头戏环节“任务 5（文字拼装排版车间）”工序链条。

---

## 下一步工作交接与排期去向说明指示引导：

当此“任务 4”宣告截点竣工画上圆满休止符号之刻，这具承载一切使命的 zip 加密战果压缩行囊将去付诸于去执行以下终极宿命与去处：
- **对接迈入启动任务 5（研报报告整纂与合拢定稿打印分发工厂车间阶段操作模块流程流水线工序进度）**：开封拆卸图片库战备装具储备包裹包袋，抽取全体精工造价打磨生成的高手级商业级别神图系列集群图片素材元件资源底库库底；随即将其逐个无缝零隙地投运植入到那最终将会以浩荡繁长万字大部头式规格磅礴厚重气度面世出街的、以正式发行版标准规范的最终版终极交稿版式 DOCX 原生原体办公文档终稿实体内里各个最适配也最精准对应的段落上下文黄金挂载坐标空位和空档空位坐标地点坐标节点落点进行精准安插着陆扎根进场和完美镶嵌契合落子固定落位安营扎寨布局！

> 请将铭心铭记这其间的 4 幅带有星星标志的强制必须必考点硬通货刚性规定骨架图表：这是关系奠基整份评估文书中枢脊梁系统估值与量价关系金融资产定价系统论述段落框架板块和逻辑主轴的心血核心立身之本，不容有丝毫的或缺或跳档遗忘以及断供缺失！

> **💡 Appendix: 领域知识小贴士**
> 
> 在您接触这份详尽的财务图表生成指南时，可能遇到了一些专业的金融词汇。以下是用最简单的话为您准备的“新手大白话”科普：
> 
> *   **DCF (Discounted Cash Flow / 现金流折现)**：想象一下，如果有人承诺10年后给你100块，这100块显然不如现在就给你100块值钱。DCF就是一种算账方法，把这家公司未来许多年能赚“进来”的所有的钱，按一定打折比例算成“今天值多少钱”，从而推算公司现在的价值。
> *   **WACC (加权平均资本成本)**：公司借钱是要付利息的，发行股票也是要给股东回报的。WACC就是把这两种找钱的方法的成本平均一下。在算上面的DCF的时候，它经常被用来当做那个“打折的比例”。
> *   **TAM (Total Addressable Market / 总可供需市场)**：就是说，如果市面上完全没有别的竞争对手来抢生意，大家全都买这家公司的这个产品，这个市场能有多大？简而言之，这就是这家公司靠卖这款产品能赚到钱的“终极天花板”。
> *   **Football Field (综合估值足球场图)**：在报告里经常能见到一张类似于跑马场或者橄榄球场的横向长条图。它其实就是把好几种不同的算账（估值）方法算出来的“最高价”和“最低价”画在同一张图上进行大乱斗比对，看看各种方法推算出的价格能不能在某个区间重合。
> *   **EBITDA 利润率**：公司赚钱后要交税、还债，还得算上以前买机器的长期折旧费。EBITDA就是把这些“杂项”和“历史包袱”全都加回利润里，纯粹看看公司最核心的门面生意本身是不是在真金白银地赚钱。
> *   **Trading Comps (交易可比公司对标)**：俗话说的“货比三家”。我们要给一家公司定价时，就去找目前在股票市场上跟它业务很像的其他公司，看看大家给它们出了什么价（比如大家给同行的市盈率是多少），从而推算出我们这家公司大概值多少。
