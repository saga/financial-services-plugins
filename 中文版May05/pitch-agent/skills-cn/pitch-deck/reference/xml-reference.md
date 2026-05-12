# PowerPoint XML 参考指南

本文件包含用于程序化编辑 PowerPoint 的 XML 模式。在直接处理 OOXML 格式时，请参考这些模式。

**注意：** 示例中的颜色值（如 `E67E22`、`D35400`）均为占位符。请替换为您模板的品牌色。

---

## ⚠️ 本参考指南的使用场景

**使用 python-pptx 进行以下操作：**
- 创建新表格（可自动处理单元格结构和关系）
- 添加文本框
- 插入图片
- 创建大多数形状
- 任何 python-pptx 提供了 API 的操作

**仅在以下情况下建议进行 XML 直接编辑：**
- 修改 python-pptx 未公开的现有元素属性
- 在通过 python-pptx 创建表格后，对单元格格式进行精细调整
- 调整 python-pptx API 无法实现的特定形状属性

**切勿使用 XML 直接编辑进行以下操作：**
- 从零开始创建表格（关系管理极易出错，可能导致文件损坏）
- 初始形状创建（存在形状 ID 冲突风险）
- 任何可以通过 python-pptx 实现的操作

本文件中的 XML 模式仅供 **参考和针对性修改**，而非用于大规模构建元素。

---

## XML 编辑风险

如果不谨慎操作，直接编辑 XML 可能会损坏 PowerPoint 文件：
- PowerPoint XML 具有相互依赖性（关系文件、内容类型）
- 无效的 XML 或缺失的关系会导致整个文件损坏
- 每一页幻灯片内的形状 ID (Shape ID) 必须保持唯一

**务必在备份副本上进行操作** —— 切勿直接编辑原始文件。

---

## 目录
- [表格实现](#表格实现)
- [箭头形状](#箭头形状)
- [文本框](#文本框)
- [带填充的形状](#带填充的形状)
- [插入图片](#插入图片)
- [连接线](#连接线)
- [单位换算](#单位换算)

---

## 表格实现

### 关键要求：验证表格属于实体表格对象

创建任何表格后，您必须验证其为真实的表格对象，而非带分隔符的文本。

**程序化验证 (python-pptx)：**
```python
for shape in slide.shapes:
    if shape.has_table:
        print(f"✓ 找到表格：{len(shape.table.rows)} 行, {len(shape.table.columns)} 列")
```

**视觉验证（在导出的图片中）：**
- 无论内容长短，各列均能完美对齐
- 单元格边框保持一致
- 选中表格时，所有单元格作为一个整体被选中

**失效预警 —— 您创建的是文本，而非表格：**
- 数值之间可见 `|` 字符
- 当内容长度变化时，列对齐发生错位
- 使用制表符 (`\t`) 进行间距调整
- 多个文本框排列成表格样式

基于文本的“表格”无法供接收方编辑，在字体变更时会发生错位，且显得缺乏专业水准。在投资推介材料 (Pitch Deck) 中，没有任何理由使用管道符或制表符分隔的表格数据。

---

### 基础表格结构

```xml
<a:tbl>
  <a:tblPr firstRow="1" bandRow="1">
    <a:tableStyleId>{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}</a:tableStyleId>
  </a:tblPr>
  <a:tblGrid>
    <a:gridCol w="2000000"/>  <!-- 来源列 - 宽度单位为 EMUs -->
    <a:gridCol w="1200000"/>  <!-- 2024年规模列 -->
    <a:gridCol w="1200000"/>  <!-- 复合年均增长率 (CAGR) 列 -->
    <a:gridCol w="1200000"/>  <!-- 2030年预测列 -->
  </a:tblGrid>
  <!-- 以下为行定义 -->
</a:tbl>
```

### 包含单元格的表格行

```xml
<a:tr h="370840">  <!-- 行高单位为 EMUs -->
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
        <a:pPr algn="ctr"/>  <!-- 数值列居中对齐 -->
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

### 表头行样式

```xml
<a:tr h="370840">
  <a:tc>
    <a:txBody>
      <a:bodyPr/>
      <a:lstStyle/>
      <a:p>
        <a:pPr algn="l"/>
        <a:r>
          <a:rPr lang="en-US" sz="1000" b="1">  <!-- 表头加粗 -->
            <a:solidFill>
              <a:srgbClr val="FFFFFF"/>  <!-- 白色文本 -->
            </a:solidFill>
          </a:rPr>
          <a:t>来源</a:t>
        </a:r>
      </a:p>
    </a:txBody>
    <a:tcPr>
      <a:solidFill>
        <a:srgbClr val="E67E22"/>  <!-- 橙色背景 -->
      </a:solidFill>
    </a:tcPr>
  </a:tc>
  <!-- 其他表头单元格... -->
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
      <a:off x="3000000" y="2500000"/>  <!-- 位置 (EMUs) -->
      <a:ext cx="500000" cy="300000"/>   <!-- 尺寸 (EMUs) -->
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

### 燕尾形 (Chevron)

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

### 基础文本框

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
        <a:t>此处为文本内容</a:t>
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
      <a:buChar char="&#252;"/>  <!-- 对勾符号 -->
    </a:pPr>
    <a:r>
      <a:rPr lang="en-US" sz="1400" dirty="0"/>
      <a:t>第一项内容</a:t>
    </a:r>
  </a:p>
  <a:p>
    <a:pPr marL="342900" indent="-342900">
      <a:buFont typeface="Wingdings" panose="05000000000000000000" pitchFamily="2" charset="2"/>
      <a:buChar char="&#252;"/>
    </a:pPr>
    <a:r>
      <a:rPr lang="en-US" sz="1400" dirty="0"/>
      <a:t>第二项内容</a:t>
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
  <a:t>有色背景上的白色文本</a:t>
</a:r>
```

---

## 带填充的形状

### 纯色填充矩形

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
    <a:bodyPr rtlCol="0" anchor="ctr"/>  <!-- 文本垂直居中 -->
    <a:lstStyle/>
    <a:p>
      <a:pPr algn="ctr"/>  <!-- 文本水平居中 -->
      <a:r>
        <a:rPr lang="en-US" sz="1600" b="1">
          <a:solidFill>
            <a:srgbClr val="FFFFFF"/>
          </a:solidFill>
        </a:rPr>
        <a:t>标签文本</a:t>
      </a:r>
    </a:p>
  </p:txBody>
</p:sp>
```

---

## 插入图片

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
    <a:blip r:embed="rIdLogo"/>  <!-- 引用关系 ID -->
    <a:stretch>
      <a:fillRect/>
    </a:stretch>
  </p:blipFill>
  <p:spPr>
    <a:xfrm>
      <a:off x="10800000" y="200000"/>  <!-- 右上角位置 -->
      <a:ext cx="800000" cy="600000"/>   <!-- Logo 尺寸 -->
    </a:xfrm>
    <a:prstGeom prst="rect">
      <a:avLst/>
    </a:prstGeom>
  </p:spPr>
</p:pic>
```

### 添加图片关系定义

在 `ppt/slides/_rels/slideN.xml.rels` 文件中：

```xml
<Relationship Id="rIdLogo" 
  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" 
  Target="../media/logo.png"/>
```

---

## 连接线

### 直线连接符

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

## 单位换算

| 单位 | 每单位对应的 EMUs 数值 |
|------|---------------|
| 1 英寸 | 914400 |
| 1 厘米 | 360000 |
| 1 磅 (Point) | 12700 |
| 1 像素 (96 DPI) | 9525 |

### 常用幻灯片尺寸 (16:9)

- 宽度：12192000 EMUs (13.333 英寸)
- 高度：6858000 EMUs (7.5 英寸)

### 典型元素位置

| 元素 | X 轴位置 | Y 轴位置 |
|---------|------------|------------|
| Logo (右上角) | 10800000 | 200000 |
| 标题 | 342583 | 286603 |
| 副标题 | 402591 | 1767390 |
| 页脚 | 342583 | 6435334 |

> **💡 Appendix: 领域知识小贴士**
>
> 制作一份专业的**投资推介材料 (Pitch Deck)**，细节决定成败：
> 1. **CAGR (复合年均增长率)**：这是衡量公司增长潜力的“金标准”。它不是简单的平均数，而是考虑了复利效应的增长率，能平滑年度间的波动，让投资人一眼看出业务的长远势头。
> 2. **Pitch Deck (路演PPT)**：金融圈的“敲门砖”。无论是投行并购还是初创融资，一份格式严谨、数据对齐到像素级的 PPT 代表了你的专业态度。这也是为什么我们一定要用“真实表格对象”而不能用空格对齐的原因。
> 3. **EMU (英语公制单位)**：这是微软为了解决不同分辨率、不同屏幕下对齐问题而设计的极小单位。1 厘米等于 360,000 个 EMU，这么精细的刻度能确保你的财报图表在任何人的电脑上看起来都完美对齐，不会“散架”。
> 4. **2030 Projection (2030年展望)**：在金融模型中，未来预测必须基于历史数据（如 2024 Size）和合理的增长逻辑。在 PPT 中，这些数字通常需要用醒目的品牌色（如本例中的橙色）来表现，引导观众的注意力。
