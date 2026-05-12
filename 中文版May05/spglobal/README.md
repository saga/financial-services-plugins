# 标普全球 (S&P Global) 插件

该插件将标普全球的金融数据与分析能力通过一系列预构建技能 (Skills) 直接引入您的 AI 工作流中。它专为寻求基于权威标普全球数据进行 AI 辅助研究、分析及文档生成的金融专业人士量身定制。

这些技能基于开放标准 (MCP) 构建，旨在跨 AI 平台和智能体框架运行。虽然该插件遵循 Claude Cowork 标准，但所有技能及其底层数据层均与平台无关。如果您希望在其他环境中使用这些技能，请随意使用。

我们深知每家机构都有其独特需求。这些技能是帮助您打造最终产品的起点。我们鼓励您根据公司的特定流程、模板和数据需求，对提示词 (Prompts)、输出内容和工作流程进行调整。

本插件中的技能按“原样”提供。生成的输出内容和数据不保证准确无误。**请务必核实大语言模型 (LLM) 生成内容的准确性。**

## 包含的技能

### 公司简报 (Tearsheets)
**要求**：订阅 [S&P Global LLM-ready API](https://www.marketplace.spglobal.com/en/solutions/kensho-llm-ready-api-%28a156fe9f-5564-4f60-a624-95d8645dc98f%29)

生成格式规范、长度为一至两页的 Word 文档版公司简报，数据由 S&P Capital IQ 实时填充。支持四种受众类型，每种类型均针对不同的使用场景进行了优化：
* 股票研究 (Equity Research)：为买方/卖方分析师提供投资逻辑速览。
* 投资银行 / 并购 (Investment Banking / M&A)：在交易背景下的公司概况分析。
* 企业发展 (Corporate Development)：为内部战略团队提供收购目标画像。
* 销售 / 业务开发 (Sales / Business Development)：为业务团队提供客户会议准备资料。

**示例提示词**："为 Palantir 生成一份业务开发用的公司简报。"

### 行业交易摘要 (Industry Transaction Summaries)
**要求**：订阅 [S&P Global LLM-ready API](https://www.marketplace.spglobal.com/en/solutions/kensho-llm-ready-api-%28a156fe9f-5564-4f60-a624-95d8645dc98f%29)

基于 S&P Capital IQ 的交易数据，总结特定行业或特定公司近期的并购及交易活动。适用于市场图谱绘制、投行提案 (Pitch) 准备以及竞争情报分析。

**示例提示词**："总结数据基础设施领域近期的交易活动。"

### 业绩前瞻 (Earnings Previews)
**要求**：订阅 [S&P Global LLM-ready API](https://www.marketplace.spglobal.com/en/solutions/kensho-llm-ready-api-%28a156fe9f-5564-4f60-a624-95d8645dc98f%29)

针对即将发布的财报生成结构化前瞻报告，内容涵盖市场一致预期、近期业绩指引、分析师情绪以及关键观察点——所有数据均源自 S&P Capital IQ。

**示例提示词**："给我一份 Salesforce 的业绩前瞻。"

## 如何使用
该插件及其技能需要访问标普全球数据方可运行，您需订阅 [Capital IQ Pro](https://www.spglobal.com/market-intelligence/en/solutions/products/sp-capital-iq-pro) 或 [S&P Global LLM-ready API](https://www.marketplace.spglobal.com/en/solutions/kensho-llm-ready-api-%28a156fe9f-5564-4f60-a624-95d8645dc98f%29)。

LLM-ready API 可以通过其 MCP 服务端轻松集成到 Claude 或其他应用程序中。请参考[这些步骤](docs.kensho.com/llmreadyapi/mcp/third-party/claude)进行设置。

### 在 Cowork 中使用
您需要拥有付费的 Claude 方案（Pro、Max、Team 或 Enterprise）以及适用于 macOS 或 Windows 的 Claude 桌面端应用。

1. 打开 Claude Desktop 并导航至 **Cowork** 选项卡
1. 点击 **Customize with Plugins** (通过插件自定义)
1. 在浏览插件中，选择 **Personal** (个人)
1. 点击 **加号 “+”** 添加插件
1. 弹出提示时，使用您的标普全球凭据进行身份验证

安装完成后，相关技能会在需要时自动激活——您只需用自然语言描述您的需求即可。您也可以通过在聊天框中输入 `/` 来查看可用命令，从而显式调用特定技能。

如需针对您公司的流程、模板或术语定制插件，请在查看已安装插件时点击 **Customize** (定制)。我们鼓励这样做；默认设置仅是起点，而非固定标准。

### 在 Claude Desktop 中使用（单项技能）
若要在 Claude Desktop 中安装单项技能而非整个插件：

1. 打开 **Settings** (设置)
1. 导航至 **Capabilities → Skills** (功能 → 技能)
1. 点击 **Add** (添加)
1. 从此代码库上传对应的技能文件

上传后，技能将立即在您的 Claude Desktop 会话中可用。您可以根据需要安装一个或多个技能。

### 在 Claude Code 中使用（单项技能）

请遵循 [Claude Code 文档](https://code.claude.com/docs/en/discover-plugins#add-from-github)中的说明。

### 其他平台
此库中的技能均为 Markdown 文件。任何支持自定义指令 (Custom Instructions)、系统提示词 (System Prompts) 或知识库文件上传的 AI 平台均可使用——具体机制因平台而异，但原理相同：加载技能内容，使其成为模型的持久上下文。

**ChatGPT**：将技能内容粘贴到“自定义指令”（设置 → 自定义 ChatGPT）中，或在“项目 (Project)”中作为知识库文件上传，亦或添加到自定义 GPT 的配置中。自定义指令适用于所有会话；项目级文件则将上下文限制在特定工作流中。

**Microsoft Copilot**：根据您的 Copilot 配置（M365 Copilot、Copilot Studio 等），将技能内容粘贴到自定义提示词或系统指令中。通过 Copilot Studio 进行的企业级部署可以直接上传知识源。

**其他平台**：如果您的平台支持系统提示词或持久指令层，请将技能的 Markdown 内容粘贴至该处。如果支持基于文件的知识检索，请上传技能文件。这些技能是纯 Markdown 格式，无需特殊的格式处理或工具。

## 后续计划
我们正积极构建涵盖一系列金融工作流的更多技能和插件。我们非常期待听到对您最有帮助的需求！如有一般性问题、反馈或合作意向，请联系 [commercial@kensho.com](mailto:commercial@kensho.com) 或在此代码库中提交 Issue。

# 许可证

根据 Apache 2.0 许可证授权。除非适用法律要求或书面同意，否则根据本许可证分发的软件均按“原样”基础分发，不附带任何明示或暗示的保证或条件。请参阅许可证以了解管理权限和限制的具体语言。

版权所有 2026-至今 Kensho Technologies, LLC。当前日期由代码库中最近一次提交的时间戳确定。

> **💡 Appendix: 领域知识小贴士**
>
> 1.  **简报 (Tearsheet)**：在金融圈，这被称为“一页纸调研”。想象一下，要把一家公司的底细（财务、业务、高管）全部浓缩在 1-2 页纸里，让你在进电梯前看完就能跟老板汇报，这就是简报。
> 2.  **S&P Capital IQ**：这是金融界的“超级图书馆”。它存满了全球公司的账本、交易记录和研报。投行、基金经理每天都要靠它来查数据。
> 3.  **一致预期 (Consensus Estimates)**：市场上有很多分析师在预测一家公司的利润。把他们的预测加起来取个平均值，就是“一致预期”。如果公司财报出来的数比这个平均值高，通常股价就会飞。
> 4.  **业绩指引 (Guidance)**：这是公司的“自我预测”。公司老板会告诉大家：“我预计明年我们能赚多少钱。”这对投资者判断公司底气非常重要。
> 5.  **并购 (M&A)**：即兼并与收购。简单说就是“大鱼吃小鱼”或者“两鱼变一鱼”。行业交易摘要就是告诉你有谁在买谁，卖了多少钱。
> 6.  **股票研究 (Equity Research)**：就是专门研究股票值不值钱的工作。你是该买入、持有还是赶紧卖出？研究员会写厚厚的报告来告诉你。
