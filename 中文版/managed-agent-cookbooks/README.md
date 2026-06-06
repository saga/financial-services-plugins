# 金融服务托管代理模板

本仓库中的每个代理都以**两种形式**交付：一种是供分析师立即安装的Cowork插件（参见仓库根目录下的垂直行业目录），另一种是供平台团队部署在您自己的工作流引擎背后的Claude托管代理模板。**同一个代理，同一套技能 —— 任您选择部署方式。** 以下每个目录都是一个部署清单，引用了对应插件中的规范系统提示词和技能，因此只有一个事实来源。

运行 `../scripts/deploy-managed-agent.sh <slug>` 即可上传技能、创建叶子工作节点，并通过 `POST /v1/agents` 提交解析后的配置。每个模板都附带 [`steering-examples.json`](./pitch-agent/steering-examples.json) 和每个代理专属的README，涵盖其安全层级和交接机制。

| 代理 | 垂直行业插件 | Cowork功能模块 | CMA引导事件 | 叶子工作节点 |
|---|---|---|---|---|
| [`pitch-agent`](./pitch-agent/) | investment-banking | 可比公司分析、先例交易、LBO → 品牌化Pitch材料 | `Build pitch book: <目标公司> / <收购方>, 投资论点: <文本>` | researcher · modeler · **deck-writer** |
| [`market-researcher`](./market-researcher/) | equity-research | 行业或主题 → 概览、竞争格局、同业对比、投资标的清单 | `Primer: <行业或主题>, 角度: <文本>` | sector-reader · comps-spreader · **note-writer** |
| [`earnings-reviewer`](./earnings-reviewer/) | equity-research | 财报电话会议 + 监管文件 → 模型更新 → 报告草稿 | `Process earnings: <股票代码> <报告期>` | transcript-reader · model-updater · **note-writer** |
| [`meeting-prep-agent`](./meeting-prep-agent/) | wealth-management | 每次客户会议前的简报材料 | `Briefing pack for <客户ID>, meeting <事件ID>` | profiler · news-reader · **pack-writer** |
| [`model-builder`](./model-builder/) | financial-analysis | DCF、LBO、三表模型、可比分析 —— 以文件形式输出 | `Build <dcf\|lbo\|3-stmt> for <股票代码>, 假设条件: {...}` | data-puller · **builder** · auditor |
| [`gl-reconciler`](./gl-reconciler/) | financial-analysis | 发现差异、追踪根因、路由至审批人 | `Reconcile GL vs subledger, trade date <日期>, classes: <列表>` | reader · critic · **resolver** |
| [`kyc-screener`](./kyc-screener/) | financial-analysis | 解析开户文件、运行规则、标记缺失项 | `Screen onboarding packet <ID>` | doc-reader · rules-engine · **escalator** |
| [`valuation-reviewer`](./valuation-reviewer/) | private-equity | 接收GP材料包、运行估值、准备LP报告 | `Review portco valuations for fund <X> as of <日期>` | package-reader · valuation-runner · **publisher** |
| [`month-end-closer`](./month-end-closer/) | financial-analysis | 应计项目、滚动预测、差异分析 | `Close <实体> for period <YYYY-MM>` | ledger-reader · rollforward · **poster** |
| [`statement-auditor`](./statement-auditor/) | private-equity | 分发前审计LP报表 | `Tie out statement batch <ID> against <基金> NAV材料包` | statement-reader · reconciler · **flagger** |

**粗体**叶子节点 = 唯一拥有 `Write` 权限的工作节点。

## 清单文件与API对照

`agent.yaml` 文件使用真实的 `POST /v1/agents` 字段名，同时提供几项便利功能，由部署脚本自动解析：

| 清单约定 | 解析为 |
|---|---|
| `system: {file: ../../plugins/agent-plugins/<slug>/agents/<slug>.md, append: "..."}` | `system: "<内联内容 + append>"` |
| `system: {text: "..."}` | `system: "<文本>"` |
| `skills: [{from_plugin: ../../plugins/agent-plugins/<slug>}]` | 上传该目录下所有 `skills/*` → `[{type: custom, skill_id: ...}, ...]` |
| `skills: [{path: ../../...}]` | `skills: [{type: custom, skill_id: <已上传ID>}]` |
| `callable_agents: [{manifest: ./subagents/x.yaml}]` | `callable_agents: [{type: agent, id: <已创建ID>, version: latest}]` |

> **研究预览：** `callable_agents`（多代理委托）支持**一级委托**。编排器可以调用工作节点；工作节点不能进一步调用子代理。

## 跨代理交接

命名代理之间不会直接相互调用。当一个代理需要另一个代理时，它会在输出中发出一个 `handoff_request`；[`../scripts/orchestrate.py`](../scripts/orchestrate.py)（或您的Temporal/Airflow/Guidewire事件总线）将其作为新的引导事件路由到目标会话。参考脚本对目标进行硬编码白名单校验，并对载荷进行模式验证 —— 详见其头部注释中的威胁模型说明。

---

## 金融术语和知识解释

### 1. 托管代理（Managed Agent）

**定义**：托管代理是由平台团队集中部署和管理的AI代理，与终端用户自行安装的插件相对。它运行在企业自己的工作流引擎背后，拥有更高的安全性和可控性。

**核心特点**：
- **集中管理**：由IT或平台团队统一部署，统一配置安全策略
- **工作流集成**：与Temporal、Airflow等企业级工作流引擎集成
- **安全隔离**：通过多级权限控制，确保敏感操作需要审批
- **审计追踪**：所有操作都有完整日志，便于合规审计

**部署方式对比**：

| 特性 | Cowork插件 | 托管代理 |
|------|-----------|----------|
| 部署主体 | 终端用户 | 平台团队 |
| 安装方式 | 应用商店安装 | 脚本自动化部署 |
| 配置管理 | 用户自行配置 | 集中配置 |
| 安全控制 | 基础权限 | 多级安全隔离 |
| 适用场景 | 个人分析师 | 企业级生产环境 |

**CMA（Claude Managed Agent）**：Anthropic提供的企业级代理管理服务，支持通过API创建、配置和监控代理。

---

### 2. 叶子工作节点（Leaf Worker）

**定义**：叶子工作节点是托管代理架构中的最底层执行单元，每个节点负责特定的子任务。

**架构模式**：
- **编排器（Orchestrator）**：接收任务，分解为子任务，分配给叶子节点
- **叶子节点（Leaf Worker）**：执行具体的读写操作，拥有特定的工具权限
- **安全分层**：不同叶子节点拥有不同的权限级别，实现最小权限原则

**典型分工**：
1. **读取节点**：只拥有 `Read`、`Grep` 权限，处理不可信的外部文档
2. **处理节点**：拥有 `Read`、`Grep`、`Glob`、`Agent` 权限，进行数据分析和推理
3. **写入节点**：唯一拥有 `Write`、`Edit` 权限的节点，负责输出最终结果

**安全优势**：
- 即使读取节点被恶意文档攻击，也无法修改系统
- 写入节点从不直接接触外部不可信文档
- 每个节点的权限都经过精确控制

---

### 3. 引导事件（Steering Event）

**定义**：引导事件是触发代理开始工作的初始指令，通常包含任务类型、目标对象和相关参数。

**事件格式示例**：
```json
{
  "event_type": "process_earnings",
  "ticker": "AAPL",
  "period": "Q3-2024",
  "priority": "high"
}
```

**事件来源**：
- **日历集成**：会议前自动生成简报
- **队列系统**：研究队列中的待处理任务
- **监控告警**：财报发布、市场异动等触发
- **人工提交**：分析师手动发起请求

**工作流编排**：
1. 事件进入消息队列
2. 编排器接收事件并解析
3. 创建代理会话
4. 分配任务给叶子节点
5. 收集结果并输出

---

### 4. 系统提示词（System Prompt）

**定义**：系统提示词是定义代理行为、能力和约束的指令文本，是代理的"行为准则"。

**组成要素**：
1. **角色定义**：代理的身份和职责
2. **能力说明**：可用工具和API
3. **工作流描述**：处理任务的步骤
4. **安全约束**：禁止行为和注意事项
5. **输出格式**：期望的响应结构

**内联机制**：
- 清单文件中的 `system: {file: ...}` 会被部署脚本自动解析
- 脚本读取引用的文件内容，内联到API请求中
- 支持 `append` 字段追加额外指令

**最佳实践**：
- 保持提示词简洁明确
- 使用结构化格式（Markdown、JSON）
- 包含具体的示例
- 明确边界条件和错误处理

---

### 5. 技能（Skills）

**定义**：技能是代理可以调用的功能模块，每个技能封装了特定的金融分析能力。

**技能类型**：
- **自定义技能（Custom Skills）**：通过 `skill_id` 引用，包含特定的提示词和工具配置
- **内置技能（Built-in Skills）**：平台提供的基础能力，如文件读写、网络搜索
- **MCP技能**：通过Model Context Protocol连接的外部数据源

**技能上传**：
```bash
# 部署脚本自动处理
../scripts/deploy-managed-agent.sh <slug>
```

**技能引用**：
```yaml
skills:
  - from_plugin: ../../plugins/agent-plugins/<slug>  # 引用整个插件的所有技能
  - path: ../../plugins/agent-plugins/<slug>/skills/<skill-name>  # 引用特定技能
```

---

### 6. 多代理委托（Multi-Agent Delegation）

**定义**：多代理委托是一种架构模式，允许一个代理将任务分配给另一个代理执行。

**一级委托限制**：
- 编排器可以调用工作节点
- 工作节点不能进一步调用子代理
- 防止无限递归和循环依赖

**交接机制（Handoff）**：
1. 代理A完成任务分析，发现需要代理B的能力
2. 代理A输出 `handoff_request` 事件
3. 编排脚本接收事件，验证目标代理白名单
4. 创建代理B的新会话，传递上下文
5. 代理B执行任务，返回结果

**安全控制**：
- 目标代理白名单：只允许预定义的代理间调用
- 载荷验证：对传递的数据进行模式校验
- 上下文隔离：每个代理会话独立，防止信息泄露

---

### 7. 安全隔离层级

**三级隔离模型**：

| 层级 | 接触不可信文档 | 工具权限 | 连接器 |
|------|--------------|----------|--------|
| **读取层** | **是** | `Read`, `Grep` | 无 |
| **处理层** | 否 | `Read`, `Grep`, `Glob`, `Agent` | 只读MCP |
| **写入层** | 否 | `Read`, `Write`, `Edit` | 无 |

**不可信文档来源**：
- 财报电话会议记录
- 新闻稿和媒体报道
- 第三方研究报告
- 客户提供的文件
- 供应商发票

**防护措施**：
- **长度限制**：读取节点返回的数据有长度上限
- **模式验证**：输出必须符合预定义的JSON模式
- **只读连接**：处理层只能读取外部数据，不能写入
- **沙箱执行**：模型构建等操作在隔离环境中运行

---

### 8. MCP（Model Context Protocol）

**定义**：MCP是Anthropic提出的开放协议，用于标准化AI模型与外部数据源的连接。

**MCP类型**：
- **数据源MCP**：FactSet、CapIQ、Daloopa等金融数据提供商
- **系统MCP**：总账（GL）、子账（Subledger）、CRM等内部系统
- **工具MCP**：文档解析、估值计算等专用工具

**配置示例**：
```bash
export FACTSET_MCP_URL=https://api.factset.com/mcp
export CAPIQ_MCP_URL=https://api.capitaliq.com/mcp
export GL_MCP_URL=https://internal-erp.company.com/mcp
```

**安全特性**：
- 只读访问：代理只能查询数据，不能修改源系统
- 审计日志：所有数据访问都有记录
- 权限控制：基于角色的数据访问权限

---

### 9. 工作流引擎集成

**Temporal**：
- **定位**：开源的工作流编排平台
- **特点**：持久化工作流状态，支持长时间运行的流程
- **适用场景**：复杂的审批流程、多步骤分析任务

**Airflow**：
- **定位**：Apache开源的数据管道编排工具
- **特点**：基于DAG（有向无环图）定义依赖关系
- **适用场景**：定时任务、数据ETL流程

**Guidewire**：
- **定位**：保险行业专用的事件总线
- **特点**：支持复杂的事件路由和规则引擎
- **适用场景**：保险理赔、保单管理

**自定义编排**：
- `scripts/orchestrate.py` 提供参考实现
- 支持事件路由、白名单校验、载荷验证
- 可根据企业需求定制

---

### 10. 部署清单（Manifest）

**定义**：部署清单是描述代理配置的YAML文件，包含系统提示词、技能、子代理等配置。

**典型结构**：
```yaml
name: my-agent
system:
  file: ../../plugins/agent-plugins/my-agent/agents/my-agent.md
  append: "Additional instructions..."
skills:
  - from_plugin: ../../plugins/agent-plugins/my-agent
callable_agents:
  - manifest: ./subagents/worker.yaml
```

**部署脚本**：
```bash
# 设置环境变量
export ANTHROPIC_API_KEY=sk-ant-...
export MCP_URL=...

# 执行部署
../scripts/deploy-managed-agent.sh my-agent
```

**脚本功能**：
1. 解析清单文件
2. 上传技能到CMA平台
3. 创建叶子工作节点
4. 注册代理配置
5. 验证部署结果
