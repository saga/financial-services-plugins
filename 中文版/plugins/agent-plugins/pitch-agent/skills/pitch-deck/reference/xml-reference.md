# PowerPoint XML 参考

本文件包含用于程序化 PowerPoint 编辑的 XML 模式。在直接使用 OOXML 格式时使用这些模式。

**注意：** 示例中的颜色值（例如 `E67E22`、`D35400`）是占位符。请替换为您模板的品牌颜色。

---

## ⚠️ 使用此参考的时机

**使用 python-pptx 进行：**
- 创建新表格（自动处理单元格结构和关系）
- 添加文本框
- 插入图片
- 大多数形状创建
- python-pptx 提供 API 的任何操作

**仅使用直接 XML 编辑：**
- 修改 python-pptx 未公开的现有元素属性
- 在通过 python-pptx 创建表格后微调单元格格式
- 调整 python-pptx API 不可用的特定形状属性

**绝不使用直接 XML 进行：**
- 从头创建表格（关系管理容易出错，可能损坏文件）
- 初始形状创建（存在形状 ID 冲突风险）
- 任何可以通过 python-pptx 完成的事情

本文件中的 XML 模式仅供**参考和有针对性的修改**，不用于大规模元素构建。

---

## XML 编辑风险

如果不小心操作，直接 XML 编辑可能会损坏 PowerPoint 文件：
- PowerPoint XML 存在相互依赖关系（关系文件、内容类型）
- 无效的 XML 或缺失的关系可能会损坏整个文件
- 形状 ID 在每张幻灯片中必须唯一

**始终在备份副本上工作**——切勿直接编辑原始文件。

---

## 目录
- [表格实现](#表格实现)
- [箭头形状](#箭头形状)
- [文本框](#文本框)
- [带填充的形状](#带填充的形状)
- [图片插入](#图片插入)
- [连接线](#连接线)
- [单位转换](#单位转换)

---

## 表格实现

### 重要：验证表格是否为实际表格对象

创建任何表格后，您必须验证它是实际的表格对象，而不是带有分隔符的文本。

**程序化验证（python-pptx）：**
```python
for shape in slide.shapes:
    if shape.has_table:
        print(f"✓ Found table: {len(shape.table.rows)} rows, {len(shape.table.columns)} columns")
```

**视觉验证（在导出的图像中）：**
- 无论内容长度如何，列都完美对齐
- 单元格边框一致
- 选择表格时会作为一个单元选择所有单元格

**失败指标 — 您创建的是文本，而不是表格：**
- 值之间可见 `|` 字符
- 当内容长度变化时列错位
- 使用制表符 (`\t`) 进行间距
- 多个文本框排列成表格的样子

基于文本的"表格"无法被接收者编辑，字体更改时会错位，并且显示出业余水平。在演示文稿中使用竖线/制表符分隔的表格数据没有可接受的用例。

---

### 基本表格结构

```xml
<a:tbl>
  <a:tblPr firstRow="1" bandRow="1">
    <a:tableStyleId>{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}</a:tableStyleId>
  </a:tblPr>
  <a:tblGrid>
    <a:gridCol w="2000000"/>  <!-- 来源列 - 宽度（EMU单位）-->
    <a:gridCol w="1200000"/>  <!-- 2024年规模列 -->
    <a:gridCol w="1200000"/>  <!-- CAGR列 -->
    <a:gridCol w="1200000"/>  <!-- 2030年预测列 -->
  </a:tblGrid>
  <!-- 行定义如下 -->
</a:tbl>
```

### 带单元格的表格行

```xml
<a:tr h="370840">  <!-- 行高（EMU单位）-->
  <a:tc>
    <a:txBody>
      <a:bodyPr/>
      <a:lstStyle/>
      <a:p>
        <a:pPr algn="l"/>  <!-- 文本列左对齐 -->
        <a:r>
          <a:rPr lang="en-US" sz="1000" b="0"/>
          <a:t>Grand View Research</a:t>
        </a:r>
      </a:p>
    </a:txBody>
    <a:tcPr/>
  </a:tc>
  <a:tc>
    <a:txBody>
      <a:bodyPr/>
      <a:lstStyle/>
      <a:p>
        <a:pPr algn="ctr"/>  <!-- 数字列居中对齐 -->
        <a:r>
          <a:rPr lang="en-US" sz="1000"/>
          <a:t>22.1</a:t>
        </a:r>
      </a:p>
    </a:txBody>
    <a:tcPr/>
  </a:tc>
  <!-- 其他单元格... -->
</a:tr>
```

### 标题行样式

```xml
<a:tr h="370840">
  <a:tc>
    <a:txBody>
      <a:bodyPr/>
      <a:lstStyle/>
      <a:p>
        <a:pPr algn="l"/>
        <a:r>
          <a:rPr lang="en-US" sz="1000" b="1">  <!-- 标题加粗 -->
            <a:solidFill>
              <a:srgbClr val="FFFFFF"/>  <!-- 白色文本 -->
            </a:solidFill>
          </a:rPr>
          <a:t>Source</a:t>
        </a:r>
      </a:p>
    </a:txBody>
    <a:tcPr>
      <a:solidFill>
        <a:srgbClr val="E67E22"/>  <!-- 橙色背景 -->
      </a:solidFill>
    </a:tcPr>
  </a:tc>
  <!-- 其他标题单元格... -->
</a:tr>
```

---

## 箭头形状

### 右箭头形状

```xml
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="10" name="Arrow Right"/>
    <p:cNvSpPr/>
    <p:nvPr/>
  </p:nvSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="3000000" y="2500000"/>  <!-- 位置（EMU单位）-->
      <a:ext cx="500000" cy="300000"/>   <!-- 大小（EMU单位）-->
    </a:xfrm>
    <a:prstGeom prst="rightArrow">
      <a:avLst/>
    </a:prstGeom>
    <a:solidFill>
      <a:srgbClr val="E67E22"/>  <!-- 箭头填充颜色 -->
    </a:solidFill>
    <a:ln>
      <a:noFill/>  <!-- 无轮廓 -->
    </a:ln>
  </p:spPr>
</p:sp>
```

### 下箭头形状

```xml
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="11" name="Arrow Down"/>
    <p:cNvSpPr/>
    <p:nvPr/>
  </p:nvSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="2500000" y="3000000"/>
      <a:ext cx="300000" cy="500000"/>
    </a:xfrm>
    <a:prstGeom prst="downArrow">
      <a:avLst/>
    </a:prstGeom>
    <a:solidFill>
      <a:srgbClr val="E67E22"/>
    </a:solidFill>
  </p:spPr>
</p:sp>
```

### V形形状

```xml
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="12" name="Chevron"/>
    <p:cNvSpPr/>
    <p:nvPr/>
  </p:nvSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="3000000" y="2500000"/>
      <a:ext cx="400000" cy="600000"/>
    </a:xfrm>
    <a:prstGeom prst="chevron">
      <a:avLst/>
    </a:prstGeom>
    <a:solidFill>
      <a:srgbClr val="E67E22"/>
    </a:solidFill>
  </p:spPr>
</p:sp>
```

---

## 文本框

### 基本文本框

```xml
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="5" name="TextBox 4"/>
    <p:cNvSpPr txBox="1"/>
    <p:nvPr/>
  </p:nvSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="500000" y="1500000"/>
      <a:ext cx="4000000" cy="500000"/>
    </a:xfrm>
    <a:prstGeom prst="rect">
      <a:avLst/>
    </a:prstGeom>
    <a:noFill/>
  </p:spPr>
  <p:txBody>
    <a:bodyPr wrap="square" rtlCol="0">
      <a:spAutoFit/>
    </a:bodyPr>
    <a:lstStyle/>
    <a:p>
      <a:r>
        <a:rPr lang="en-US" sz="1400" dirty="0"/>
        <a:t>Text content here</a:t>
      </a:r>
    </a:p>
  </p:txBody>
</p:sp>
```

### 带项目符号的文本框

```xml
<p:txBody>
  <a:bodyPr wrap="square">
    <a:spAutoFit/>
  </a:bodyPr>
  <a:lstStyle/>
  <a:p>
    <a:pPr marL="342900" indent="-342900">
      <a:buFont typeface="Wingdings" panose="05000000000000000000" pitchFamily="2" charset="2"/>
      <a:buChar char="&#252;"/>  <!-- 勾选标记字符 -->
    </a:pPr>
    <a:r>
      <a:rPr lang="en-US" sz="1400" dirty="0"/>
      <a:t>First bullet point</a:t>
    </a:r>
  </a:p>
  <a:p>
    <a:pPr marL="342900" indent="-342900">
      <a:buFont typeface="Wingdings" panose="05000000000000000000" pitchFamily="2" charset="2"/>
      <a:buChar char="&#252;"/>
    </a:pPr>
    <a:r>
      <a:rPr lang="en-US" sz="1400" dirty="0"/>
      <a:t>Second bullet point</a:t>
    </a:r>
  </a:p>
</p:txBody>
```

### 白色文本（用于深色背景）

```xml
<a:r>
  <a:rPr lang="en-US" sz="1000" b="1" i="1" dirty="0">
    <a:solidFill>
      <a:srgbClr val="FFFFFF"/>  <!-- 白色文本 -->
    </a:solidFill>
  </a:rPr>
  <a:t>White text on colored background</a:t>
</a:r>
```

---

## 带填充的形状

### 带纯色填充的矩形

```xml
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="20" name="Rectangle 19"/>
    <p:cNvSpPr/>
    <p:nvPr/>
  </p:nvSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="500000" y="2500000"/>
      <a:ext cx="1000000" cy="2000000"/>
    </a:xfrm>
    <a:prstGeom prst="rect">
      <a:avLst/>
    </a:prstGeom>
    <a:solidFill>
      <a:srgbClr val="E67E22"/>  <!-- 橙色填充 -->
    </a:solidFill>
    <a:ln w="12700">  <!-- 边框宽度 -->
      <a:solidFill>
        <a:srgbClr val="D35400"/>  <!-- 深色边框 -->
      </a:solidFill>
    </a:ln>
  </p:spPr>
  <p:txBody>
    <a:bodyPr rtlCol="0" anchor="ctr"/>  <!-- 垂直居中文本 -->
    <a:lstStyle/>
    <a:p>
      <a:pPr algn="ctr"/>  <!-- 水平居中 -->
      <a:r>
        <a:rPr lang="en-US" sz="1600" b="1">
          <a:solidFill>
            <a:srgbClr val="FFFFFF"/>
          </a:solidFill>
        </a:rPr>
        <a:t>Label Text</a:t>
      </a:r>
    </a:p>
  </p:txBody>
</p:sp>
```

---

## 图片插入

### 向幻灯片添加图片

```xml
<p:pic>
  <p:nvPicPr>
    <p:cNvPr id="99" name="Company Logo"/>
    <p:cNvPicPr>
      <a:picLocks noChangeAspect="1"/>
    </p:cNvPicPr>
    <p:nvPr/>
  </p:nvPicPr>
  <p:blipFill>
    <a:blip r:embed="rIdLogo"/>  <!-- 引用关系ID -->
    <a:stretch>
      <a:fillRect/>
    </a:stretch>
  </p:blipFill>
  <p:spPr>
    <a:xfrm>
      <a:off x="10800000" y="200000"/>  <!-- 右上角位置 -->
      <a:ext cx="800000" cy="600000"/>   <!-- Logo尺寸 -->
    </a:xfrm>
    <a:prstGeom prst="rect">
      <a:avLst/>
    </a:prstGeom>
  </p:spPr>
</p:pic>
```

### 添加图片关系

在 `ppt/slides/_rels/slideN.xml.rels` 中：

```xml
<Relationship Id="rIdLogo" 
  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" 
  Target="../media/logo.png"/>
```

---

## 连接线

### 直线连接器

```xml
<p:cxnSp>
  <p:nvCxnSpPr>
    <p:cNvPr id="15" name="Straight Connector 14"/>
    <p:cNvCxnSpPr>
      <a:cxnSpLocks/>
    </p:cNvCxnSpPr>
    <p:nvPr/>
  </p:nvCxnSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="500000" y="2500000"/>
      <a:ext cx="5000000" cy="0"/>  <!-- 水平线 -->
    </a:xfrm>
    <a:prstGeom prst="line">
      <a:avLst/>
    </a:prstGeom>
    <a:ln w="12700">
      <a:solidFill>
        <a:srgbClr val="E67E22"/>
      </a:solidFill>
    </a:ln>
  </p:spPr>
</p:cxnSp>
```

### 虚线

```xml
<p:spPr>
  <a:xfrm>
    <a:off x="500000" y="4500000"/>
    <a:ext cx="5000000" cy="0"/>
  </a:xfrm>
  <a:prstGeom prst="line">
    <a:avLst/>
  </a:prstGeom>
  <a:ln w="12700">
    <a:solidFill>
      <a:srgbClr val="E67E22"/>
    </a:solidFill>
    <a:prstDash val="dash"/>  <!-- 虚线样式 -->
  </a:ln>
</p:spPr>
```

---

## 单位转换

| 单位 | 每单位 EMUs |
|------|-------------|
| 1 英寸 | 914400 |
| 1 厘米 | 360000 |
| 1 点 | 12700 |
| 1 像素（96 DPI） | 9525 |

### 常见幻灯片尺寸（16:9）

- 宽度：12192000 EMUs（13.333 英寸）
- 高度：6858000 EMUs（7.5 英寸）

### 典型元素位置

| 元素 | X 位置 | Y 位置 |
|------|--------|--------|
| Logo（右上角） | 10800000 | 200000 |
| 标题 | 342583 | 286603 |
| 副标题 | 402591 | 1767390 |
| 页脚 | 342583 | 6435334 |

---

## 金融术语解释

### 1. OOXML（Office Open XML）

**定义**：OOXML 是 Microsoft Office 使用的 XML 格式标准，用于文档、电子表格和演示文稿。

**组成部分**：
- **PPTX**：PowerPoint 演示文稿格式
- **XLSX**：Excel 电子表格格式
- **DOCX**：Word 文档格式

**特点**：
- 基于 XML 的压缩格式
- 可通过 ZIP 解压查看内部结构
- 支持程序化编辑

**应用场景**：
- 自动化文档生成
- 批量处理 Office 文件
- 文档模板定制

### 2. EMU（English Metric Unit）

**定义**：EMU 是 Office Open XML 中使用的标准度量单位。

**换算关系**：
- 1 EMU = 1/914400 英寸
- 1 英寸 = 914400 EMUs
- 1 厘米 = 360000 EMUs

**用途**：
- 精确控制元素位置和大小
- 确保跨设备一致性
- 程序化文档生成

### 3. python-pptx

**定义**：python-pptx 是一个用于创建和更新 PowerPoint 文件的 Python 库。

**功能**：
- 创建幻灯片
- 添加文本框、表格和图表
- 插入图片
- 设置样式和格式

**优势**：
- 简化 PowerPoint 自动化
- 提供高级 API 抽象
- 处理复杂的 XML 结构

**限制**：
- 某些高级功能需要直接 XML 操作
- 性能可能受限

### 4. 关系文件（Relationship File）

**定义**：关系文件是 OOXML 中用于管理文件内部引用的 XML 文件。

**作用**：
- 建立文件之间的关联
- 管理图片、图表等外部资源
- 维护文档结构完整性

**位置**：
- `ppt/slides/_rels/slideN.xml.rels`
- `_rels/.rels`

**重要性**：
- 损坏的关系文件会导致文档无法打开
- 正确管理关系是程序化编辑的关键

### 5. 形状 ID（Shape ID）

**定义**：形状 ID 是 PowerPoint 幻灯片中每个形状的唯一标识符。

**要求**：
- 在每张幻灯片中必须唯一
- 用于引用和操作形状
- 防止 ID 冲突

**管理方法**：
- 使用 python-pptx 自动分配
- 直接编辑 XML 时手动管理
- 避免硬编码 ID

### 6. XML 命名空间（XML Namespace）

**定义**：XML 命名空间用于区分不同 XML 词汇表中的元素。

**常见命名空间**：
- `a:` - DrawingML（形状、文本、样式）
- `p:` - PresentationML（幻灯片、形状）
- `r:` - Relationships（关系引用）

**作用**：
- 避免元素名称冲突
- 支持模块化 XML 设计
- 提高文档可扩展性

### 7. 表格对象（Table Object）

**定义**：表格对象是 PowerPoint 中用于展示结构化数据的元素。

**特点**：
- 由行和列组成
- 支持格式化和样式
- 可程序化创建和修改

**与文本表格的区别**：
- 实际表格对象支持编辑
- 文本表格只是文本排列
- 表格对象保持对齐和格式

**最佳实践**：
- 始终使用实际表格对象
- 避免使用文本模拟表格
- 确保表格结构正确

### 8. 演示文稿自动化（Presentation Automation）

**定义**：演示文稿自动化是指使用编程技术自动创建或修改演示文稿。

**应用场景**：
- 批量生成报告
- 动态数据更新
- 模板定制

**工具**：
- python-pptx（Python）
- VBA（Visual Basic for Applications）
- Office JavaScript API

**优势**：
- 提高效率
- 减少人为错误
- 支持大规模操作

### 9. 视觉样式（Visual Styling）

**定义**：视觉样式是指演示文稿中元素的外观和格式设置。

**组成部分**：
- 颜色方案
- 字体选择
- 布局设计
- 动画效果

**原则**：
- 保持一致性
- 提高可读性
- 增强视觉吸引力

**品牌一致性**：
- 使用品牌颜色
- 遵循品牌指南
- 保持专业形象

### 10. 数据可视化（Data Visualization）

**定义**：数据可视化是将数据转换为视觉表示形式的过程。

**类型**：
- 图表（条形图、折线图、饼图）
- 表格
- 信息图
- 仪表盘

**工具**：
- Excel
- PowerPoint
- Python 库（Matplotlib、Plotly）

**原则**：
- 清晰传达信息
- 避免误导
- 突出关键数据