---
name: tear-sheet
description: "使用 Kensho LLM-ready API MCP 服务器通过 S&P Capital IQ 数据生成专业的公司简介文件。当用户请求简介文件、公司单页、公司概况、情况说明书、公司快照或公司概述文档时使用此技能 — 特别是当他们提到特定公司名称或股票代码时。当用户请求股票研究摘要、并购公司概况、企业发展目标公司概况、销售/商务发展会议准备文档或任何简洁的单公司财务摘要时也会触发。此技能支持四种受众类型：股票研究、投资银行/并购、企业发展和销售/商务发展。如果用户未指定受众，请询问。适用于上市公司和私营公司。"
---

# 财务简介文件生成器

通过 S&P Capital IQ（通过 S&P Global MCP 工具）提取实时数据，并将结果格式化为专业的 Word 文档，生成针对特定受众的公司简介文件。

## 样式配置

这些是合理的默认值。要根据贵公司的品牌进行自定义，请修改此部分 — 常见更改包括交换调色板、更改字体（Calibri 在许多银行是标准字体）和更新免责声明文本。

**颜色：**
- 主色调（页眉横幅背景、章节标题文本）：#1F3864
- 强调色（签名部分高亮）：#2E75B6
- 表格表头行填充：#D6E4F0
- 表格交替行填充：#F2F2F2
- 表格边框：#CCCCCC
- 页眉横幅文本：#FFFFFF

**排版（docx-js 的半点数）：**
- 字体族：Arial
- 公司名称：18pt 粗体（大小：36）
- 章节标题：11pt 粗体（大小：22），主色调
- 正文：9pt（大小：18）
- 表格文本：8.5pt（大小：17）
- 页脚/免责声明：7pt 斜体（大小：14）
- 每个模板的覆盖在各参考文件的格式说明中指定。

**公司页眉横幅：**
- 页眉是一个深蓝色（#1F3864）横幅，横跨整个页面宽度，公司名称为白色。
- **横幅下方，键值对必须在横跨整个页面宽度的双列无边框表格中呈现。** 左列：公司标识符（股票代码、总部、成立时间、员工数、行业）。右列：财务标识符（市值、企业价值、股票价格、流通股数）。每个单元格包含一个粗体标签和同一行上的常规权重值（例如，"**市值** $124.7B"）。不要将所有字段左对齐在单个列中 — 这会浪费水平空间且看起来不专业。双列布局是区分专业简介文件与默认文档的最重要视觉信号。
  - **实现：** 创建一个 2 列表格，所有单元格的 `borders: none` 和 `shading: none`。将列宽设置为各 50%。将左列字段（股票代码、总部、成立时间、员工数）作为左单元格中的单独段落放置。将右列字段（市值、企业价值、股票价格、流通股数）放在右单元格中。每个字段是一个单独的段落：标签为粗体运行，值为常规运行。
  - 每列中的具体字段因受众而异 — 请参见参考文件的页眉规范。原则始终是：跨页面分布，不要聚集在左侧。
- **不要对页眉键值块使用边框表格。** 边框表格仅保留用于财务数据。
- 页眉中的关键指标（市值、企业价值、股票价格）应显示为内联键值对，而不是在单独的边框表格中。

**章节标题：**
- 每个章节标题正下方有一条水平线（细线，#CCCCCC，0.5pt），在各章节之间创建清晰的视觉分隔。
- **将规则渲染为标题段落本身的底部边框** — 不要为规则插入单独的段落元素。单独的段落会添加自己的前后间距，并在章节标题下方造成过多空白。
- **实现：** 在 docx-js 中，通过 `paragraph.borders.bottom = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" }` 将底部边框应用于章节标题段落。不要使用 `doc.addParagraph()` 和单独的水平规则元素。不要使用 `thematicBreak`。边框必须在标题段落本身上，后面有 0pt 间距，以便规则紧贴标题文本。
- 间距：标题段之前 12pt，标题段之后 0pt，下一个内容元素之前 4pt。

**项目符号格式：**
- 所有简介文件类型的所有项目符号内容使用单个项目符号字符（•）。不要在简介文件内或跨简介文件混合使用 •、-、▸ 或编号列表。
- **综合/分析项目符号**（收益亮点、战略契合度、整合考虑因素、对话切入点）：缩进块样式格式，左缩进 360 DXA（0.25"），项目符号字符悬挂缩进。这些应该与正文视觉上偏移 — 它们是解释性内容，应该与数据表格和散文段落区分开来。
- **关系部分内的信息性项目符号**：标准正文缩进（180 DXA），无悬挂缩进。
- **不要对任何项目符号部分应用左边框强调。** 左边框样式在 docx-js 中渲染不一致，并会产生视觉伪影。改用缩进和文本大小差异来区分签名部分。

**表格（仅限财务数据）：**
- 表头行：表格表头填充（#D6E4F0），粗体深色文本
- 正文行：交替白色 / 表格交替填充（#F2F2F2）
- 边框：表格边框颜色（#CCCCCC），细（BorderStyle.SINGLE，大小 1）
- 单元格填充：上下 40 DXA，左右 80 DXA
- 所有数字列右对齐
- 始终使用 ShadingType.CLEAR（永远不要使用 SOLID — SOLID 会导致黑色背景）

**布局：**
- US Letter 纵向，0.75" 边距（四面 1080 DXA）

**数字格式：**
- 货币：美元。除非公司收入 > 500 亿美元（然后使用十亿美元，保留一位小数），否则使用百万。在列标题中标注单位（例如，"收入（百万美元）"），不要在单个单元格中标注。
- **表格单元格：带逗号的纯数字，无美元符号。** 示例：收入单元格显示 "4,916" 而不是 "$4,916"。列标题包含单位。
- 财年：实际年份（FY2022、FY2023、FY2024），永远不要使用相对标签（FY-2、FY-1）。
- 负数：括号，例如 (2.3%)
- 百分比：一位小数
- 大数字：逗号作为千位分隔符

**页脚（文档页脚，非内联）：**
将来源归属和免责声明放在实际文档页脚中（每页重复），而不是作为底部的内联正文文本。页脚正好两行，居中，每页都有：
- 第 1 行："数据：S&P Capital IQ via Kensho | 分析：AI 生成 | [Month Day, Year]"
- 第 2 行："仅供参考。非投资建议。"
- 样式：7pt 斜体，居中，#666666 文本颜色
- 此页脚文本在同一家公司的所有简介文件类型中必须相同。不要因受众而异。
- **此页脚是每个简介文件、每种受众类型、每页都必需的。不要省略。**

## 组件函数

**您必须使用这些确切的函数来创建文档元素。不要编写自定义 docx-js 样式代码。** 将这些函数复制到您生成的 Node 脚本中并调用它们。上面的样式配置散文仍然作为文档；这些函数是执行机制。

```javascript
const docx = require("docx");
const {
  Document, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, AlignmentType, BorderStyle, ShadingType,
  Header, Footer, PageNumber, HeadingLevel, TableLayoutType,
  convertInchesToTwip
} = docx;

// ── 颜色常量 ──
const COLORS = {
  PRIMARY: "1F3864",
  ACCENT: "2E75B6",
  TABLE_HEADER_FILL: "D6E4F0",
  TABLE_ALT_ROW: "F2F2F2",
  TABLE_BORDER: "CCCCCC",
  HEADER_TEXT: "FFFFFF",
  FOOTER_TEXT: "666666",
};

const FONT = "Arial";

// ── 1. createHeaderBanner ──
// 返回 docx 元素数组：[横幅段落, 键值表格]
function createHeaderBanner(companyName, leftFields, rightFields) {
  // leftFields / rightFields: { label: string, value: string } 的数组
  const banner = new Paragraph({
    children: [
      new TextRun({
        text: companyName,
        bold: true,
        size: 36, // 18pt
        color: COLORS.HEADER_TEXT,
        font: FONT,
      }),
    ],
    shading: { type: ShadingType.CLEAR, color: "auto", fill: COLORS.PRIMARY },
    spacing: { after: 0 },
    alignment: AlignmentType.LEFT,
  });

  function buildCellParagraphs(fields) {
    return fields.map(
      (f) =>
        new Paragraph({
          children: [
            new TextRun({ text: f.label + "  ", bold: true, size: 18, font: FONT }),
            new TextRun({ text: f.value, size: 18, font: FONT }),
          ],
          spacing: { after: 40 },
        })
    );
  }

  const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
  const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };
  const noShading = { type: ShadingType.CLEAR, color: "auto", fill: "FFFFFF" };

  const kvTable = new Table({
    rows: [
      new TableRow({
        children: [
          new TableCell({
            children: buildCellParagraphs(leftFields),
            width: { size: 50, type: WidthType.PERCENTAGE },
            borders: noBorders,
            shading: noShading,
          }),
          new TableCell({
            children: buildCellParagraphs(rightFields),
            width: { size: 50, type: WidthType.PERCENTAGE },
            borders: noBorders,
            shading: noShading,
          }),
        ],
      }),
    ],
    width: { size: 100, type: WidthType.PERCENTAGE },
  });

  return [banner, kvTable];
}

// ── 2. createSectionHeader ──
// 返回带底部边框规则的单个段落
function createSectionHeader(text) {
  return new Paragraph({
    children: [
      new TextRun({
        text: text,
        bold: true,
        size: 22, // 11pt
        color: COLORS.PRIMARY,
        font: FONT,
      }),
    ],
    spacing: { before: 240, after: 0 }, // 之前 12pt，之后 0pt
    border: {
      bottom: { style: BorderStyle.SINGLE, size: 1, color: COLORS.TABLE_BORDER },
    },
  });
}

// ── 3. createTable ──
// headers: string[], rows: string[][], options: { accentHeader?, fontSize? }
function createTable(headers, rows, options = {}) {
  const fontSize = options.fontSize || 17; // 默认 8.5pt
  const headerFill = options.accentHeader ? COLORS.ACCENT : COLORS.TABLE_HEADER_FILL;
  const headerTextColor = options.accentHeader ? COLORS.HEADER_TEXT : "000000";

  const cellBorders = {
    top: { style: BorderStyle.SINGLE, size: 1, color: COLORS.TABLE_BORDER },
    bottom: { style: BorderStyle.SINGLE, size: 1, color: COLORS.TABLE_BORDER },
    left: { style: BorderStyle.SINGLE, size: 1, color: COLORS.TABLE_BORDER },
    right: { style: BorderStyle.SINGLE, size: 1, color: COLORS.TABLE_BORDER },
  };

  const cellMargins = { top: 40, bottom: 40, left: 80, right: 80 };

  function isNumeric(val) {
    if (typeof val !== "string") return false;
    const cleaned = val.replace(/[,$%()]/g, "").trim();
    return cleaned !== "" && !isNaN(cleaned);
  }

  // 表头行
  const headerRow = new TableRow({
    children: headers.map(
      (h) =>
        new TableCell({
          children: [
            new Paragraph({
              children: [
                new TextRun({
                  text: h,
                  bold: true,
                  size: fontSize,
                  color: headerTextColor,
                  font: FONT,
                }),
              ],
            }),
          ],
          shading: { type: ShadingType.CLEAR, color: "auto", fill: headerFill },
          borders: cellBorders,
          margins: cellMargins,
        })
    ),
  });

  // 带交替阴影的数据行
  const dataRows = rows.map((row, rowIdx) => {
    const fill = rowIdx % 2 === 1 ? COLORS.TABLE_ALT_ROW : "FFFFFF";
    return new TableRow({
      children: row.map((cell, colIdx) => {
        const align = colIdx > 0 && isNumeric(cell)
          ? AlignmentType.RIGHT
          : AlignmentType.LEFT;
        return new TableCell({
          children: [
            new Paragraph({
              children: [
                new TextRun({ text: cell, size: fontSize, font: FONT }),
              ],
              alignment: align,
            }),
          ],
          shading: { type: ShadingType.CLEAR, color: "auto", fill: fill },
          borders: cellBorders,
          margins: cellMargins,
        });
      }),
    });
  });

  return new Table({
    rows: [headerRow, ...dataRows],
    width: { size: 100, type: WidthType.PERCENTAGE },
  });
}

// ── 4. createBulletList ──
// items: string[], style: "synthesis" | "informational"
function createBulletList(items, style = "synthesis") {
  const indent =
    style === "synthesis"
      ? { left: 360, hanging: 180 }   // 左缩进 360 DXA，项目符号悬挂缩进
      : { left: 180 };                 // 180 DXA，无悬挂缩进

  return items.map(
    (item) =>
      new Paragraph({
        children: [
          new TextRun({ text: "•  ", font: FONT, size: 18 }),
          new TextRun({ text: item, font: FONT, size: 18 }),
        ],
        indent: indent,
        spacing: { after: 60 },
      })
  );
}

// ── 5. createFooter ──
// date: string (例如，"February 23, 2026")
function createFooter(date) {
  return new Footer({
    children: [
      new Paragraph({
        children: [
          new TextRun({
            text: `Data: S&P Capital IQ via Kensho | Analysis: AI-generated | ${date}`,
            italics: true,
            size: 14, // 7pt
            color: COLORS.FOOTER_TEXT,
            font: FONT,
          }),
        ],
        alignment: AlignmentType.CENTER,
      }),
      new Paragraph({
        children: [
          new TextRun({
            text: "For informational purposes only. Not investment advice.",
            italics: true,
            size: 14,
            color: COLORS.FOOTER_TEXT,
            font: FONT,
          }),
        ],
        alignment: AlignmentType.CENTER,
      }),
    ],
  });
}
```

**在生成脚本中的用法：**
1. 将上面的所有函数和常量复制到生成的 Node.js 脚本中
2. 调用 `createHeaderBanner(...)` 而不是手动构建横幅段落和表格
3. 为每个章节标题调用 `createSectionHeader(...)` — 永远不要手动设置段落边框
4. 为**所有**表格数据调用 `createTable(...)` — 财务摘要、交易对比、并购活动、关系表、融资历史等。对于并购活动表（IB/M&A 模板），传递 `{ accentHeader: true }`。对于非数字表格（例如，关系、所有权），该函数仍然正确工作 — 它只对包含数值的单元格右对齐。
5. 为收益亮点、战略契合度、整合考虑因素和对话切入点调用 `createBulletList(items, "synthesis")`
6. 为关系条目调用 `createBulletList(items, "informational")`
7. 将 `createFooter(date)` 传递给 Document 构造函数的 `footers.default` 属性

**这些函数消除了：**
- 黑色背景表格（在各处强制执行 `ShadingType.CLEAR`）
- 章节标题下的单独水平规则段落（在段落本身上强制执行 `border.bottom`）
- 页眉中的边框键值表格（强制执行 `borders: none`）
- 不一致的项目符号样式（仅强制执行 `•` 字符）
- 缺失的页脚（提供确切的页脚结构）

## 工作流程

### 步骤 1：识别输入

在继续之前收集最多四件事：

1. **公司** — 名称或股票代码。如果只有股票代码，通过初始查询解析完整公司名称（例如，使用公司信息工具）。
2. **受众** — 四种类型之一：
   - **股票研究** — 面向买方/卖方分析师评估投资
   - **IB / M&A** — 面向银行家在交易背景下对公司进行分析
   - **企业发展** — 面向内部战略团队评估收购目标
   - **销售 / BD** — 面向商业团队准备客户会议
3. **可比公司**（可选）— 如果用户有特定的可比公司，请注明。否则，技能将从 S&P Global 数据中识别同行。这对股票研究、IB/M&A 和企业发展简介文件很重要。
4. **页数偏好**（可选）— 默认值因受众而异（见下文），但用户可以覆盖。

如果用户未指定受众，请询问。

### 步骤 2：读取受众特定参考

从此技能的目录中读取相应的参考文件：

- 股票研究 → `references/equity-research.md`
- IB / M&A → `references/ib-ma.md`
- 企业发展 → `references/corp-dev.md`
- 销售 / BD → `references/sales-bd.md`

每个参考定义了章节、查询计划、格式指导和页数默认值。

### 步骤 3：通过 S&P Global MCP 获取数据

**首先：** 创建中间文件目录：
```bash
mkdir -p /tmp/tear-sheet/
```

使用 **S&P Global** MCP 工具（也称为 Kensho LLM-ready API）。Claude 将有权访问用于财务数据、公司信息、市场数据、共识估计、收益记录、并购交易和业务关系的结构化工具。每个参考文件中的查询计划描述了每个部分需要什么数据 — 将这些映射到对话中可用的适当 S&P Global 工具。

**每次查询步骤后，立即将检索到的数据写入参考文件的查询计划中指定的中间文件。** 不要延迟写入 — 写入磁盘的数据受到保护，不会在长对话中发生上下文退化。

**查询策略：**
每个参考文件包含一个 4-6 个数据检索步骤的查询计划。这些是起点，不是严格的约束。优先考虑数据完整性而非最小化调用：

- **始终提取 4 个财年的财务数据**，即使只显示 3 年。第四年（最早）需要计算第一个显示年份的同比收入增长。没有它，最早年份的增长率将显示 "N/A" — 这看起来像缺失数据，而不是设计选择。
- 按编写的方式执行查询计划，使用与所需数据匹配的任何 S&P Global 工具。
- 如果工具调用返回不完整的结果，请尝试替代工具或更窄的查询。例如，如果公司摘要不包含部门详情，请直接尝试部门工具。
- 如果经过有针对性的重试后仍未返回数据点，请继续 — 将其标记为 "N/A" 或 "未披露"。
- 切勿编造数据。如果工具未返回数字，请不要根据训练知识进行估算。

**用户指定的可比公司：** 如果用户提供了可比公司，明确查询每个可比公司的财务数据和倍数。如果未提供可比公司，使用工具返回的任何同行数据，或使用竞争对手工具从公司的行业中识别同行。

**用户的可选背景：** 自然倾听用户提供的额外背景。如果他们提到收购方是谁（"我们正在为我们的平台考虑这个"）、他们卖什么（"我们向银行销售数据分析"）或可能的买家是谁（"这对 Salesforce 或 Microsoft 来说会很有趣"），将该背景纳入相关的综合部分（战略契合度、对话切入点、交易角度）。不要提示此信息 — 如果提供了就使用它。

**私营公司处理：**
CIQ 包含私营公司数据，因此以相同方式查询。但是，预期结果更稀疏。为私营公司生成时：
- 跳过：股票价格、52 周范围、贝塔系数、股票表现、共识估计、交易对比
- 强调：业务概述、关系、所有权结构、任何可用的财务数据
- 在页眉中突出显示"私营公司"

### 步骤 3b：计算派生指标

完成所有数据收集并写入中间文件后，在单个专用过程中计算所有派生指标。这是仅计算步骤 — 不进行新的 MCP 查询。

**将所有中间文件读回上下文**，然后计算：

- **利润率：** 毛利率 %、EBITDA 利润率 %、FCF 利润率 %、营业利润率 %
- **增长率：** 同比收入增长、同比部门收入增长、同比每股收益增长
- **效率比率：** FCF 转化率（FCF/EBITDA）、研发占收入百分比、资本支出占收入百分比
- **资本结构：** 净债务（总债务 − 现金及等价物）、净债务 / EBITDA
- **部门组合：** 每个部门的收入占合并总收入的百分比（根据数据完整性规则 8，使用合并收入作为分母）

**验证（从算术验证移动）：** 在此计算过程中，强制执行所有算术检查：

- **利润率计算：** 验证 EBITDA 利润率 = EBITDA / 收入，毛利率 = 毛利润 / 收入等。如果计算的利润率与原始数字不匹配，使用原始组件的计算结果。
- **增长率：** 验证同比增长 = (当期 − 上期) / 上期。如果您有基础值，请不要依赖预先计算的增长率。
- **部门总计：** 如果按部门显示收入，验证部门总和等于总收入（在舍入容差内）。如果不相等，省略总行而不是发布不一致的数学计算。
- **百分比列：** 验证"占总计百分比"列总和约为 100%。
- **估值交叉检查：** 如果同时显示 EV 和 EV/收入，验证 EV / 收入 ≈ 声明的倍数。

如果验证失败：尝试从原始数据重新计算。如果仍然不一致，将指标标记为 "N/A" 而不是发布不正确的数字。简介文件中的静默数学错误会破坏可信度。

**将结果写入** `/tmp/tear-sheet/calculations.csv`，列：`metric,value,formula,components`

示例行：
```
metric,value,formula,components
gross_margin_fy2024,72.4%,gross_profit/revenue,"9524/13159"
revenue_growth_fy2024,12.3%,(current-prior)/prior,"13159/11716"
net_debt_fy2024,2150,total_debt-cash,"4200-2050"
```

### 步骤 3c：验证数据文件

在生成文档之前，验证所有中间文件是否存在并已填充。

**通过单独的读取操作读取每个中间文件**并打印验证摘要：

```
=== Tear Sheet Data Verification ===
company-profile.txt: ✓ (12 fields)
financials.csv:      ✓ (36 rows)
segments.csv:        ✓ (8 rows)
valuation.csv:       ✓ (5 rows)
calculations.csv:    ✓ (18 rows)
earnings.txt:        ✓ (populated)
relationships.txt:   ⚠ MISSING
peer-comps.csv:      ✓ (12 rows)
================================
```

**软门限：** 如果当前受众类型预期的任何文件缺失或为空，打印警告但继续。简介文件优雅地处理缺失数据，使用 "N/A" 和跳过部分。但是，警告确保可见性了解丢失的数据。

**关键规则：文件 — 而不是您对早期对话的记忆 — 是文档中每个数字的唯一真实来源。** 在步骤 4 中生成 DOCX 时，从中间文件读取值。不要依赖对话上下文获取财务数据。

### 步骤 4：格式化为 DOCX

读取 `/mnt/skills/public/docx/SKILL.md` 了解 docx 创建机制（通过 Node 的 docx-js）。应用上面的样式配置加上参考文件中的特定于部分的格式。

**页数默认值（用户可以覆盖）：**
- 股票研究：1 页（密度是惯例）
- IB / M&A：1-2 页
- 企业发展：1-2 页
- 销售 / BD：1-2 页

如果内容超过目标，每个参考文件指定首先要删减哪些部分。

**输出文件名：** `[CompanyName]_TearSheet_[Audience]_[YYYYMMDD].docx`
示例：`Nvidia_TearSheet_CorpDev_20260220.docx`

保存到 `/mnt/user-data/outputs/` 并呈现给用户。

## 数据完整性规则

这些覆盖其他所有内容：
1. **S&P Global 工具是财务数据的唯一来源。** 不要用训练知识填补空白 — 它可能过时或错误。
2. **标注找不到的内容。** 使用 "N/A" 或 "未披露" 而不是静默省略一行。
3. **日期很重要。** 注明财年末或报告期。不要假设日历年 = 财年。市场数据（股票价格、市值）应包含"截至"日期。
4. **不要混合报告期。** 如果您有 FY2023 收入和 LTM EBITDA，请明确标注它们。
5. **优先使用 MCP 返回的字段而不是手动计算。** 如果 S&P Global 工具返回预先计算的字段（例如，净债务、EBITDA、FCF），直接使用该值而不是从组件计算。仅在工具不返回字段时手动计算派生指标。这减少差异。
6. **确保跨简介文件类型的一致性。** 如果为同一家公司生成多个简介文件（例如，同一会话中的股票研究和 IB/M&A），相同的基础数据点必须在所有输出中产生相同的值。净债务、收入、EBITDA、利润率和增长率必须完全匹配。不要为每个报告独立重新查询或重新计算 — 重用相同的检索值。
7. **永远不要降低已知交易价值。** 如果并购工具返回交易的交易价值，该价值必须出现在输出中。不要用"未披露"替换已知的交易价值。仅在工具确实未返回交易价值时使用"未披露"。
8. **使用合并收入作为部门百分比的分母。** 在计算部门表的"占总计百分比"时，将每个部门的收入除以合并总收入（如损益表中报告的），而不是部门收入之和。部门总和通常因部门间消除而超过合并收入。使用合并收入确保百分比与文档中显示的总收入数字一致。
9. **可用时始终包含远期（NTM）倍数。** 如果工具同时返回滞后和远期估值倍数，两者都必须出现在输出中。远期倍数是股票研究、IB/M&A 和企业发展受众的主要估值参考。永远不要在可用远期数据时只显示滞后倍数。
10. **没有 S&P Global 工具返回高管或管理数据。** 不要从训练数据填充管理层姓名、职位或传记细节 — 这违反规则 1 并产生过时信息。如果模板中出现管理层部分，请完全省略。所有权结构（机构持有人、内部人士百分比、私募股权赞助商）只有在工具返回时才可以包含 — 用"数据允许"限制。

## 中间文件规则

从 MCP 工具检索的所有数据必须在文档生成之前持久化到结构化中间文件。这些文件 — 而不是对话上下文 — 是文档中每个数字的唯一真实来源。

**设置：** 在步骤 3 开始时，创建工作目录：
```
mkdir -p /tmp/tear-sheet/
```

**查询后写入任务：** 每次 MCP 查询步骤完成后，立即将检索到的数据写入相应的中间文件。不要等到所有查询完成后再写入。每个参考文件的查询计划指定每个步骤后要写入哪些文件。

**文件模式：**

| 文件 | 格式 | 列 / 结构 | 使用者 |
|---|---|---|---|
| `/tmp/tear-sheet/company-profile.txt` | 键值文本 | name, ticker, exchange, HQ, sector, industry, founded, employees, market_cap, enterprise_value, stock_price, 52wk_high, 52wk_low, shares_outstanding, beta, ownership | 全部 |
| `/tmp/tear-sheet/financials.csv` | CSV | `period,line_item,value,source` | 全部 |
| `/tmp/tear-sheet/segments.csv` | CSV | `period,segment_name,revenue,source` | ER, IB, CD |
| `/tmp/tear-sheet/valuation.csv` | CSV | `metric,trailing,forward,source` | ER, IB, CD |
| `/tmp/tear-sheet/consensus.csv` | CSV | `metric,fy_year,value,source` | ER |
| `/tmp/tear-sheet/earnings.txt` | 结构化文本 | Quarter, date, key quotes, guidance, key drivers | ER, IB, Sales |
| `/tmp/tear-sheet/relationships.txt` | 结构化文本 | Customers, suppliers, partners, competitors — 每个都有描述符 | IB, CD, Sales |
| `/tmp/tear-sheet/peer-comps.csv` | CSV | `ticker,metric,value,source` | ER, IB, CD |
| `/tmp/tear-sheet/ma-activity.csv` | CSV | `date,target,deal_value,type,rationale,source` | IB, CD |
| `/tmp/tear-sheet/calculations.csv` | CSV | `metric,value,formula,components` | 全部（在步骤 3b 中写入） |

**缩写：** ER = 股票研究，IB = IB/M&A，CD = 企业发展，Sales = 销售/BD。

并非每种受众类型都使用每个文件 — 参考文件定义适用哪些查询步骤。与当前受众类型无关的文件不需要创建。

**仅原始值。** 中间文件存储工具返回的原始值。不要在这些文件中预先计算利润率、增长率或其他派生指标 — 这发生在步骤 3b 中。

**页数预算执行：** 每个参考文件指定默认页数和编号删减顺序。如果渲染的文档超过目标，按指定顺序应用删减 — 不要尝试将字体大小或边距缩小到模板最小值以下。删减顺序是严格的优先级堆栈：在接触第 2 节之前完全删减第 1 节。

## 内容质量规则

11. **为受众重写每个叙述部分。** CIQ 公司摘要是输入，不是输出。每种受众类型需要不同的描述：股票研究简洁且面向主题，IB 是推介文稿风格，企业发展是产品聚焦，销售/BD 是简单明了的语言。永远不要将 CIQ 摘要逐字粘贴到任何简介文件中。
12. **按受众区分收益亮点。** 同一次财报电话会议为不同读者产生不同的要点。股票研究想要部门级表现和共识超出/不及预期。IB 想要利润率轨迹和战略评论。销售/BD 想要创造对话角度的战略主题。不要在简介文件类型之间重用相同的项目符号。
13. **综合部分是差异化因素。** 战略契合度分析、整合考虑因素、对话切入点和业务概述段落是简介文件获得其价值的地方。这些部分需要分析推理，将数据点连接成叙述 — 列出公司名称而没有背景不是综合。
14. **在部门表中标记待剥离业务。** 如果公司已宣布剥离某个部门或业务单元的计划，在部门表中添加脚注或括号注明待处理交易（例如，"Mobility* — *待剥离，预计 2026 年年中"）。对于企业发展和 IB/M&A 简介文件，在部门表下方添加一行注释，显示剥离部门后的预计收入和收入组合。这帮助读者自己评估"前进"业务而无需计算。

### 算术验证

**→ 算术验证现在在步骤 3b（计算派生指标）中强制执行。** 所有利润率计算、增长率、部门总计、百分比列和估值交叉检查在文档生成之前的专用计算过程中进行验证。有关完整验证清单，请参见步骤 3b。

---

## 金融术语解释

### 1. 公司简介文件 (Tear Sheet)

**定义**：公司简介文件是一份简洁的单页或多页文档，包含公司的关键信息和财务摘要。它是金融专业人士用于快速评估公司的常用工具。

**用途**：
- **投资分析**：帮助投资者快速了解公司的基本面
- **会议准备**：为客户会议或内部讨论准备背景资料
- **交易评估**：在并购交易中评估目标公司
- **销售支持**：为销售团队提供客户或潜在客户的概况

**内容组成**：
- 公司基本信息（股票代码、总部、成立时间等）
- 财务摘要（收入、利润、现金流）
- 估值指标（市盈率、企业价值倍数）
- 关键业务指标和亮点
- 行业对比和竞争对手分析

### 2. 股票研究 (Equity Research)

**定义**：股票研究是对上市公司的深入分析，旨在为投资者提供投资建议和估值判断。

**分析师类型**：
- **卖方分析师**：为投资银行工作，向客户提供研究报告
- **买方分析师**：为基金或投资公司工作，支持内部投资决策

**报告类型**：
- **首次覆盖报告**：对公司进行全面分析
- **财报预览/点评**：在财报发布前后的分析
- **行业报告**：对特定行业的整体评估

**核心内容**：
- 公司业务模式和竞争优势
- 财务预测和估值分析
- 投资建议（买入/持有/卖出）
- 目标价格

### 3. 投资银行/并购 (IB/M&A)

**定义**：投资银行在并购交易中扮演顾问角色，帮助客户进行收购、出售或合并。

**服务内容**：
- **并购顾问**：协助买方或卖方完成交易
- **估值服务**：为交易提供定价建议
- **融资安排**：为收购提供资金支持
- **尽职调查**：对目标公司进行全面审查

**并购类型**：
- **横向并购**：同行业公司合并
- **纵向并购**：产业链上下游整合
- **混合并购**：不同行业公司合并

### 4. 企业发展 (Corporate Development)

**定义**：企业发展部门负责公司的战略规划和执行，包括并购、战略合作和投资。

**职责范围**：
- **战略规划**：制定公司长期发展战略
- **并购执行**：寻找和执行收购机会
- **战略合作**：建立合作伙伴关系
- **投资管理**：管理公司的投资组合

**关键活动**：
- 识别潜在的收购目标
- 进行尽职调查
- 谈判交易条款
- 整合收购后的业务

### 5. 销售/商务发展 (Sales/Business Development)

**定义**：销售和商务发展团队负责开拓市场、建立客户关系和推动收入增长。

**销售团队职责**：
- 开发新客户
- 维护现有客户关系
- 达成销售目标
- 提供客户支持

**商务发展职责**：
- 识别新的市场机会
- 建立战略合作伙伴关系
- 开拓新业务领域
- 评估市场趋势

### 6. EBITDA

**定义**：EBITDA 代表息税折旧摊销前利润，是衡量公司盈利能力的常用指标。

**计算公式**：
- EBITDA = 营业收入 + 折旧 + 摊销

**用途**：
- **估值**：作为企业价值倍数的基础
- **业绩比较**：消除不同资本结构的影响
- **现金流评估**：作为经营现金流的近似值

**优缺点**：
- **优点**：简单易懂，便于跨公司比较
- **缺点**：忽略资本支出需求，可能高估现金流

### 7. 自由现金流 (FCF)

**定义**：自由现金流是公司在支付所有运营费用和资本支出后剩余的现金。

**计算公式**：
- FCF = 经营现金流 - 资本支出

**用途**：
- **估值**：DCF 模型的核心输入
- **财务健康**：衡量公司生成现金的能力
- **股东回报**：可用于股息、回购或再投资

**类型**：
- **经营自由现金流**：核心业务产生的现金流
- **杠杆自由现金流**：考虑债务后的现金流

### 8. 净债务 (Net Debt)

**定义**：净债务是公司总债务减去现金及现金等价物后的余额。

**计算公式**：
- 净债务 = 总债务 - 现金及等价物

**用途**：
- **资本结构分析**：评估公司的实际债务负担
- **估值**：计算企业价值的关键组成部分
- **财务健康**：衡量公司的净负债水平

**解读**：
- **正净债务**：公司有净负债
- **负净债务**：公司现金多于债务，财务状况强劲

### 9. 估值倍数 (Valuation Multiples)

**定义**：估值倍数是用于评估公司价值的比率，通常基于财务指标。

**常用倍数**：
- **P/E 比率**：市盈率
- **EV/Revenue**：企业价值与收入比
- **EV/EBITDA**：企业价值与 EBITDA 比
- **Price/Book**：市净率

**应用场景**：
- **相对估值**：与同行业公司比较
- **投资决策**：评估投资机会的吸引力
- **交易定价**：并购交易中的定价参考

### 10. 交易对比 (Trading Comps)

**定义**：交易对比是一种估值方法，通过比较目标公司与类似上市公司的估值倍数来确定价值。

**步骤**：
1. **选择可比公司**：选择业务模式、规模、行业相似的公司
2. **收集财务数据**：获取可比公司的财务指标
3. **计算估值倍数**：计算各种估值倍数
4. **应用倍数**：将平均倍数应用于目标公司

**优点**：
- 基于市场数据，客观透明
- 易于理解和解释
- 适用于公开交易的公司

**局限性**：
- 难以找到完全可比的公司
- 市场情绪可能影响倍数
- 未考虑公司特有因素

### 11. 合并财务报表 (Consolidated Financials)

**定义**：合并财务报表是将母公司及其子公司的财务数据合并为一个整体的报表。

**合并范围**：
- 母公司控制的子公司（通常持股 >50%）
- 可变利益实体（VIE）
- 特殊目的实体（SPE）

**合并方法**：
- **完全合并法**：将子公司的所有资产、负债、收入和费用完全合并
- **权益法**：适用于持股 20%-50% 的投资
- **成本法**：适用于持股 <20% 的投资

**消除内部交易**：
- 消除母公司与子公司之间的销售
- 消除内部应收账款和应付账款
- 消除内部利润

### 12. 部门分析 (Segment Analysis)

**定义**：部门分析是对公司不同业务部门的财务表现进行单独评估。

**目的**：
- **识别强势部门**：找出贡献最大的业务
- **发现问题部门**：识别表现不佳的业务
- **资源配置**：优化资源分配
- **战略规划**：制定部门级战略

**披露要求**：
- 上市公司通常需要按部门披露财务信息
- 包括部门收入、利润、资产等

**关键指标**：
- 部门收入及占比
- 部门利润及利润率
- 部门增长率
- 部门资产回报率

### 13. 共识估计 (Consensus Estimates)

**定义**：共识估计是多位分析师对公司财务指标的平均预测值。

**数据来源**：
- 金融数据提供商（S&P Capital IQ、FactSet）
- 卖方分析师报告
- 专业财经媒体

**类型**：
- 当前季度估计
- 年度估计
- 长期增长估计

**影响**：
- 股价对实际业绩与共识的差异敏感
- 共识估计是投资分析的重要参考

### 14. 数据完整性 (Data Integrity)

**定义**：数据完整性指数据的准确性、一致性和可靠性。

**重要性**：
- **决策质量**：准确的数据支持更好的决策
- **合规要求**：满足监管机构的信息披露要求
- **投资者信任**：维护市场信心
- **风险管理**：识别和控制风险

**保障措施**：
- 数据验证和核对
- 审计追踪
- 访问控制
- 定期数据质量检查

### 15. 尽职调查 (Due Diligence)

**定义**：尽职调查是在投资或交易前对目标公司进行的全面调查。

**类型**：
- **财务尽职调查**：审查财务报表和会计记录
- **法律尽职调查**：审查法律文件和合规性
- **商业尽职调查**：评估市场地位和竞争优势
- **技术尽职调查**：评估技术资产和知识产权

**目的**：
- **风险识别**：发现潜在风险和问题
- **价值确认**：验证公司的价值和潜力
- **条款谈判**：为交易条款提供依据

---

## Appendix: 金融背景知识

这份文件是"公司简介（Tear Sheet）"技能的详细说明。Tear Sheet 是金融圈最基础的"公司身份证"——通常只有 1-2 页，包含一家公司的所有关键信息。

---

### 1. 什么是 Tear Sheet？

**类比：**
想象你去相亲，对方递给你一张"个人简介"：姓名、年龄、身高、学历、工作、收入、兴趣爱好。1 分钟看完，你对这个人就有了基本了解。

Tear Sheet 就是公司的"相亲简历"——1-2 页纸，让投资人在 2 分钟内了解一家公司。

---

### 2. Tear Sheet 的"标准内容"

| 模块 | 内容 |
|------|------|
| 基本信息 | 公司名、股票代码、上市地、行业 |
| 财务摘要 | 收入、利润、利润率、增长率 |
| 估值指标 | P/E、EV/EBITDA、P/B |
| 股价表现 | 52 周最高/最低、年初至今涨幅 |
| 关键数据 | 员工数、市值、企业价值 |
| 投资亮点 | 3-5 个核心投资逻辑 |
| 风险因素 | 3-5 个主要风险 |

---

### 3. Tear Sheet 的"使用场景"

1. **投资人初步筛选**——快速判断"值不值得深入看"
2. **内部沟通**——向合伙人/投决会介绍公司
3. **客户汇报**——向 LP 汇报被投公司情况
4. **新闻稿**——媒体引用公司关键数据

---

### 4. 真实案例：苹果 Tear Sheet

| 项目 | 数据 |
|------|------|
| 公司名 | Apple Inc. |
| 股票代码 | AAPL（NASDAQ） |
| 行业 | 科技/消费电子 |
| 市值 | ~3 万亿美元 |
| 年收入 | ~3800 亿美元 |
| 净利润 | ~1000 亿美元 |
| P/E | ~30x |
| 投资亮点 | 品牌护城河、现金流强劲、服务业务增长 |
| 风险因素 | iPhone 依赖、中国市场风险、监管压力 |

---

### 给小白的一句话

> Tear Sheet 就是金融圈的"身份证"——2 页纸告诉你"这家公司是干什么的、赚多少钱、值多少钱、有什么风险"。对于专业投资人来说，Tear Sheet 是"快速筛选工具"——1 分钟看完就能判断"值不值得花更多时间研究"。对于金融小白来说，Tear Sheet 是"入门地图"——帮你把复杂的公司信息简化成"能看懂的关键数字"。
