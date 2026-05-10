# PowerPoint XML参考

本文档包含用于程序化PowerPoint编辑的XML模式。在直接使用OOXML格式时使用这些模式。

**注意：** 示例中的颜色值（例如 `E67E22`, `D35400`）是占位符。请替换为您模板的品牌颜色。

---

## ⚠️ 何时使用此参考

**使用python-pptx进行：**
- 创建新表格（自动处理单元格结构和关系）
- 添加文本框
- 插入图片
- 大多数形状创建
- python-pptx提供API的任何操作

**仅在以下情况使用直接XML编辑：**
- 修改python-pptx未公开的现有元素属性
- 在通过python-pptx创建表格后微调单元格格式
- 调整python-pptx API不可用的特定形状属性

**切勿使用直接XML进行：**
- 从头创建表格（关系管理容易出错，可能损坏文件）
- 初始形状创建（形状ID冲突风险）
- 任何可以通过python-pptx完成的事情

本文档中的XML模式仅供**参考和针对性修改**，而非大规模元素构建。

---

## XML编辑风险

如果不小心，直接XML编辑可能会损坏PowerPoint文件：
- PowerPoint XML具有相互依赖性（关系文件、内容类型）
- 无效XML或缺失关系可能损坏整个文件
- 形状ID在每张幻灯片中必须唯一

**始终在备份副本上工作** — 切勿直接编辑原始文件。

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

### 关键：验证表格是实际的表格对象

创建任何表格后，**必须**验证它是实际的表格对象，而不是带分隔符的文本。

**程序化验证（python-pptx）：**
```python
for shape in slide.shapes:
    if shape.has_table:
        print(f"✓ 找到表格：{len(shape.table.rows)}行，{len(shape.table.columns)}列")
```

**视觉验证（在导出的图像中）：**
- 列对齐完美，与内容长度无关
- 单元格边框一致
- 选择表格时将所有单元格作为一个单元选择

**失败指标 — 你创建的是文本，不是表格：**
- 可见`|`字符在值之间
- 当内容长度变化时列不对齐
- 使用制表符（`\t`）进行间距
- 多个文本框排列成表格外观

基于文本的"表格"无法被接收者编辑，字体改变时会错位，标志着业余工作。在推介材料中，没有使用竖线/制表符分隔的表格数据的合理场景。

---

### 基本表格结构

```xml
<a:tbl>
  <a:tblPr firstRow="1" bandRow="1">
    <a:tableStyleId>{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}</a:tableStyleId>
  </a:tblPr>
  <a:tblGrid>
    <a:gridCol w="2000000"/>  <!-- 来源列 - 宽度以EMU为单位 -->
    <a:gridCol w="1200000"/>  <!-- 2024年规模列 -->
    <a:gridCol w="1200000"/>  <!-- CAGR列 -->
    <a:gridCol w="1200000"/>  <!-- 2030年预测列 -->
  </a:tblGrid>
  <!-- 行定义如下 -->
</a:tbl>
```

### 带单元格的表格行

```xml
<a:tr h="370840">  <!-- 行高（EMU） -->
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
      <a:off x="3000000" y="2500000"/>  <!-- 位置（EMU） -->
      <a:ext cx="500000" cy="300000"/>   <!-- 大小（EMU） -->
    </a:xfrm>
    <a:prstGeom prst="rightArrow">
      <a:avLst/>
    </a:prstGeom>
    <a:solidFill>
      <a:srgbClr val="E67E22"/>  <!-- 箭头填充颜色 -->
    </a:solidFill>
    <a:ln>
      <a:noFill/>  <!-- 无边框 -->
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

### V形箭头形状

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
      <a:buChar char="&#252;"/>  <!-- 勾选字符 -->
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
    </a:cNvPicPr>
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

### 直线连接

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

| 单位 | 每单位EMU数 |
|------|---------------|
| 1英寸 | 914400 |
| 1厘米 | 360000 |
| 1点 | 12700 |
| 1像素（96 DPI） | 9525 |

### 常见幻灯片尺寸（16:9）

- 宽度：12192000 EMU（13.333英寸）
- 高度：6858000 EMU（7.5英寸）

### 典型元素位置

| 元素 | X位置 | Y位置 |
|---------|------------|------------|
| Logo（右上角） | 10800000 | 200000 |
| 标题 | 342583 | 286603 |
| 副标题 | 402591 | 1767390 |
| 页脚 | 342583 | 6435334 |

---

## 📚 金融术语和知识解释

### 1. OOXML（Office Open XML）

**定义**：Office Open XML是Microsoft Office文档的标准化文件格式，基于XML和ZIP压缩技术。

**组成结构**：
- **文档内容**：存储实际文本、表格、图表等
- **关系文件**：记录文档内部各部分之间的关联
- **元数据**：文档属性和设置

**优势**：
- 跨平台兼容性
- 易于编程处理
- 较小的文件体积
- 支持高级功能

### 2. python-pptx

**定义**：一个用于创建和更新PowerPoint `.pptx` 文件的Python库。

**主要功能**：
- 创建和修改幻灯片
- 添加文本框、表格、图表
- 设置字体、颜色、布局
- 插入图片和形状

**使用场景**：
- 自动化报告生成
- 批量处理演示文稿
- 数据可视化自动化

### 3. EMU（English Metric Unit）

**定义**：Office Open XML中使用的标准度量单位。

**换算关系**：
- 1 EMU = 1/914400 英寸
- 1英寸 = 914400 EMU
- 1厘米 = 360000 EMU

**用途**：确保在不同设备和分辨率下的精确布局。

### 4. API（应用程序接口）

**定义**：Application Programming Interface，是软件组件之间交互的约定。

**类型**：
- **REST API**：基于HTTP协议的Web服务接口
- **库API**：编程语言库提供的函数和方法
- **操作系统API**：操作系统提供的系统调用

**重要性**：
- 简化开发流程
- 促进代码复用
- 实现系统集成

### 5. 自动化演示文稿生成

**定义**：使用编程方式自动创建和格式化演示文稿的过程。

**优势**：
- 提高效率
- 保证一致性
- 减少人为错误
- 支持大规模处理

**典型流程**：
1. 定义模板和样式
2. 收集和处理数据
3. 程序化生成内容
4. 应用格式和布局
5. 导出和分发

### 6. 数据可视化

**定义**：将数据转换为图形或图表的过程，使复杂信息更容易理解。

**类型**：
- **图表**：折线图、柱状图、饼图等
- **表格**：结构化数据展示
- **信息图**：视觉化信息设计
- **仪表盘**：实时数据监控

**原则**：
- 清晰简洁
- 突出重点
- 保持一致性
- 避免信息过载

### 7. 推介材料自动化

**投资银行应用场景**：
- **批量生成**：为多个客户生成标准化材料
- **数据更新**：自动更新财务数据和市场信息
- **格式统一**：确保所有材料符合公司标准
- **快速响应**：缩短准备时间，提高竞争力

**关键技术**：
- 模板引擎
- 数据集成
- 自动化脚本
- 版本控制

### 8. 财务演示最佳实践

**设计原则**：
- **清晰性**：信息易于理解
- **简洁性**：避免过多文字
- **专业性**：使用专业模板和字体
- **一致性**：保持格式统一

**内容原则**：
- 重点突出关键数据
- 提供数据来源
- 保持逻辑连贯
- 讲述有说服力的故事

### 9. 投资银行技术栈

**常用工具**：
- **Excel**：财务建模和数据分析
- **PowerPoint**：演示文稿制作
- **Python/R**：数据分析和自动化
- **专业数据库**：Capital IQ、PitchBook、Bloomberg

**新兴技术**：
- AI辅助内容生成
- 自动化文档处理
- 数据可视化工具
- 云协作平台

### 10. 金融科技（FinTech）

**定义**：Financial Technology，指利用技术创新提供金融服务的行业。

**领域**：
- **支付**：移动支付、数字钱包
- **借贷**：P2P借贷、在线贷款
- **投资**：智能投顾、在线交易
- **保险**：数字保险、理赔自动化

**趋势**：
- AI和机器学习应用
- 区块链和分布式账本
- 开放银行API
- 监管科技（RegTech）