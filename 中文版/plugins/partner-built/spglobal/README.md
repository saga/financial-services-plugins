# S&P Global 插件

本插件通过一系列预制技能，将 S&P Global 的金融数据和分析直接引入您的 AI 工作流。专为需要 AI 辅助研究、分析和文档生成的金融专业人士设计，所有数据均来源于权威的 S&P Global。

这些技能基于开放标准（MCP）构建，可在各种 AI 平台和代理框架中使用。虽然本插件遵循 Claude Cowork 标准，但所有技能及其底层数据层均与平台无关。如果您想在其它环境中使用这些技能，欢迎使用。

我们理解每个组织都有独特需求。这些技能是起点，帮助您快速构建最终产品。欢迎您根据公司的具体流程、模板和数据需求调整提示词、输出格式和工作流。

本插件中的技能按"原样"提供。生成的输出和数据不保证正确性。**务必验证 LLM 生成的输出是否准确。**

## 所含技能

### 公司概览页面（Tearsheets）
**前提条件**：[S&P Global LLM-ready API](https://www.marketplace.spglobal.com/en/solutions/kensho-llm-ready-api-%28a156fe9f-5564-4f60-a624-95d8645dc98f%29) 订阅

生成格式化的 1-2 页公司概览页面（Word 文档），使用来自 S&P Capital IQ 的实时数据。支持四种受众类型，每种针对不同场景优化：
* 股权研究：面向买方/卖方分析师的投资论点快照
* 投资银行 / 并购：交易情境下的公司简介
* 企业发展：供内部战略团队使用的收购目标简介
* 销售 / 业务拓展：面向商业团队的客户会议准备材料

**示例提示词**："为 Palantir 生成一份业务拓展概览页面。"

### 行业交易摘要
**前提条件**：[S&P Global LLM-ready API](https://www.marketplace.spglobal.com/en/solutions/kensho-llm-ready-api-%28a156fe9f-5564-4f60-a624-95d8645dc98f%29) 订阅

汇总某行业或特定公司近期的并购和交易活动，数据来自 S&P Capital IQ 交易数据库。适用于市场地图绘制、推介准备和竞争情报。

**示例提示词**："汇总数据基础设施领域近期交易。"

### 财报预览
**前提条件**：[S&P Global LLM-ready API](https://www.marketplace.spglobal.com/en/solutions/kensho-llm-ready-api-%28a156fe9f-5564-4f60-a624-95d8645dc98f%29) 订阅

为即将发布的财报生成结构化预览，包含一致预期、近期指引、分析师情绪和关注要点——所有数据均来自 S&P Capital IQ。

**示例提示词**："给我一份 Salesforce 的财报预览。"

## 使用方法
本插件和技能需要 S&P Global 数据权限，可以是 [Capital IQ Pro](https://www.spglobal.com/market-intelligence/en/solutions/products/sp-capital-iq-pro) 或 [S&P Global LLM-ready API](https://www.marketplace.spglobal.com/en/solutions/kensho-llm-ready-api-%28a156fe9f-5564-4f60-a624-95d8645dc98f%29) 订阅。

LLM-ready API 可通过其 MCP 服务器在 Claude 或其他应用中轻松集成。请按照[这些步骤](docs.kensho.com/llmreadyapi/mcp/third-party/claude)进行设置。

### 在 Cowork 中使用
您需要付费的 Claude 套餐（Pro、Max、Team 或 Enterprise）以及 macOS 或 Windows 的 Claude 桌面版。

1. 打开 Claude 桌面版，进入 **Cowork** 标签
2. 点击 **使用插件自定义**
3. 在浏览插件中，选择 **个人**
4. 点击 **加号"+"** 添加插件
5. 按提示使用您的 S&P Global 凭证进行身份验证

安装后，技能会在相关时自动激活——只需用自然语言描述您的需求。您也可以通过在聊天中输入 / 来查看可用命令并显式调用特定技能。

要为您的公司自定义插件的工作流、模板或术语，请在查看已安装插件时点击 **自定义**。我们鼓励这样做；默认设置是起点，不是规定。

### 在 Claude Desktop 中使用（单个技能）
要在 Claude Desktop 中安装单个技能而不使用完整插件：

1. 打开 **设置**
2. 进入 **功能 → 技能**
3. 点击 **添加**
4. 上传此仓库中的技能文件

技能上传后即可在 Claude Desktop 中使用。您可以根据需要安装一个或多个。

### 在 Claude Code 中使用（单个技能）

请按照 [Claude Code 文档](https://code.claude.com/docs/en/discover-plugins#add-from-github)中的说明操作。

### 其他平台
此仓库中的技能文件为 Markdown 格式。任何支持自定义指令、系统提示或知识文件上传的 AI 平台都可以使用它们——不同平台的机制不同，但原理相同：加载技能内容，使其成为模型的持久上下文。

**ChatGPT**：将技能内容粘贴到自定义指令（设置 → 自定义 ChatGPT）、在项目内上传为知识文件，或添加到自定义 GPT 的配置中。自定义指令在会话间全局生效；项目级文件将上下文限定在特定工作流。

**Microsoft Copilot**：根据您的 Copilot 配置（M365 Copilot、Copilot Studio 等）将技能内容粘贴到自定义提示或系统指令中。通过 Copilot Studio 的企业级部署可以直接上传知识源。

**其他平台**：如果您的平台支持系统提示或持久指令层，将技能 Markdown 粘贴到那里。如果支持基于文件的知识检索，上传技能文件。技能是纯 Markdown，无需特殊格式或工具。

## 后续计划
我们正在积极构建更多技能和插件，覆盖一系列金融工作流。欢迎告诉我们什么对您最有用！如有一般性问题、反馈或合作咨询，请联系 [commercial@kensho.com](mailto:commercial@kensho.com) 或在此仓库中提交 Issue。

# 许可

基于 Apache 2.0 许可。除非适用法律要求或书面同意，按"原样"分发的软件不附带任何明示或暗示的保证。详见许可文件中的具体条款。

Copyright 2026-present Kensho Technologies, LLC。当前日期由仓库中最近提交的时间戳确定。

---

## 📖 本篇金融知识小贴士

**S&P Global**：全球最大的金融数据和评级机构之一，旗下包括 S&P 评级、S&P Capital IQ（公司财务数据库）、S&P 指数（标普500）等。

**Capital IQ**：S&P Global 旗下的金融数据和软件平台。提供全球公司的财务数据、一致预期、并购交易等深度信息。金融从业者的标配工具。

**公司概览页面（Tearsheet）**：一份简明扼要的公司简介，通常 1-2 页，包含关键财务数据、业务描述和估值指标。投行和投资研究中极常用。

**报表预览（Earnings Preview）**：公司发布正式财报前，分析师做的"预告"。包含市场预期数据、关键关注点和管理层近期评论。

**并购交易摘要**：汇总近期并购活动，包括交易金额、买卖方、行业等。用于了解市场动态和竞争对手。

**受众定向的财务报告**：同样的数据，不同读者需要不同的呈现方式。股权研究读者关心估值，投行关心交易背景，销售关心如何切入谈话。

**AI 生成的财务内容**：这些技能生成的报告带有免责声明"AI生成，请确认所有输出"——因为 AI 可能产生幻觉，所有数字都需要人工核实。