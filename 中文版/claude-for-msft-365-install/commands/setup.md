---
description: 设置向导：配置 Vertex / Bedrock / Foundry / gateway、管理员同意，并生成 manifest
---

# Claude in Office：直连云端设置

你正在引导企业管理员配置 Claude Office 加载项，使其调用自有云资源，而不是
Anthropic API。最终交付物是一个可通过 M365 Admin Center 部署的定制化
`manifest.xml`。

**开始前先做一件事：** 设置日志文件位于：

```text
~/Desktop/claude-for-msft-365-install-setup.md
```

如果该文件已存在，先读取它，你可能是在续接之前的一次配置过程。每次新的操作都应
新增一个 `## Run — <timestamp>` 段落，并把执行过的命令及关键输出
（ID、URL、生成结果）附加进去。

**检查 Node.js：** 第 4 步和第 6 步会调用 `node` 和 `npx`。先运行：

```bash
node --version
```

如果没有安装，先征求管理员同意，再按其平台安装。

## 第 1 步：加载项如何访问 Claude？

先问管理员一个最容易答错、但最关键的问题：
**你们是否已经有自己的 LLM gateway（如 LiteLLM、Portkey、Kong 等）？**

- **有 → 选 `gateway`。** 即使 gateway 背后接的是 Vertex 或 Bedrock，
  对加载项来说，它只是在调用你们自己的网关。
- **没有 → 选 `vertex` 或 `bedrock` 或 `foundry`。**

| 路径 | 含义 | 需要准备什么 | manifest 键 |
|---|---|---|---|
| `gateway` | 加载项 → 你的 gateway | 通常无需额外云侧配置 | `gateway_url` 及可选 `gateway_api_format` |
| `vertex` | 加载项直接访问 Vertex AI | Google OAuth client | `gcp_project_id` `gcp_region` `google_client_id` `google_client_secret` |
| `bedrock` | 加载项直接访问 AWS Bedrock | IAM OIDC provider + role | `aws_role_arn` `aws_region` |
| `foundry` | 加载项直接访问 Azure AI Foundry | Foundry 资源 + API key | `azure_resource_name` `azure_api_key` |

Bedrock 以及所有按用户配置（bootstrap / extension attrs）场景都需要
`entra_sso=1`。

## 第 1b 步：要支持哪些 Office 应用？

询问管理员：**只部署 Excel / Word / PowerPoint，还是 Outlook，或两者都要？**

如果包含 Outlook：

- **Bedrock 当前不支持 Outlook**
- **必须先完成 Microsoft Graph 管理员同意**

## Vertex AI 路径

### 前置条件

确认管理员能提供：

- GCP project ID
- 具备 Claude 模型配额的 region（通常 `us-east5`）

### 创建 OAuth client

这个步骤没有纯命令行接口，通常需要管理员打开控制台手工创建：

```text
https://console.cloud.google.com/apis/credentials?project=<PROJECT_ID>
```

创建 Web application 类型的 OAuth client，并加入回调地址：

```text
https://pivot.claude.ai/auth/callback
```

同时启用 Vertex API：

```bash
gcloud services enable aiplatform.googleapis.com --project=<PROJECT_ID>
```

记录以下参数：

- `gcp_project_id`
- `gcp_region`
- `google_client_id`
- `google_client_secret`

## Bedrock 路径

### 前置条件

确认管理员能提供：

- AWS account ID
- 启用了 Claude 模型的区域（通常 `us-east-1`）
- Azure tenant ID
- 已配置好的 `aws` CLI

### 创建 OIDC provider 和 role

典型命令如下：

```bash
TENANT_ID="<their-azure-tenant-guid>"
CLAUDE_APP_ID="c2995f31-11e7-4882-b7a7-ef9def0a0266"
AWS_REGION="us-east-1"
ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
ISSUER="login.microsoftonline.com/${TENANT_ID}/v2.0"
```

后续按源码命令创建：

- OIDC provider
- `ClaudeBedrockAccess` role
- `BedrockInvoke` policy

最终记录：

- `aws_role_arn`
- `aws_region`

并在 manifest 中启用：

```text
entra_sso=1
```

## Gateway 路径

无需云侧新建资源，直接问管理员：

- gateway 基础 URL
- gateway token

如果 token 是按用户不同的，不应写入 manifest，而应放入第 5 步的用户级配置。

### API 格式

确认 gateway 暴露的是哪一种接口：

- 默认：Anthropic `/v1/messages`
- Bedrock pass-through
- Vertex pass-through

如果是 `vertex` pass-through，还需要额外记录：

- `gcp_project_id`
- `gcp_region`

### 认证头

默认加载项使用：

```text
x-api-key: <token>
```

如果网关要求：

```text
Authorization: Bearer <token>
```

则需要设置：

```text
gateway_auth_header=authorization
```

## Azure AI Foundry 路径

确认管理员已有：

- Azure AI Foundry 资源
- 至少一个已部署的 Claude 模型
- 资源名（如 `contoso-foundry`）

然后在 Azure Portal 的 **Keys and Endpoint** 页面读取 `KEY 1`。

记录：

- `azure_resource_name`
- `azure_api_key`

## 第 2 步：Azure 管理员同意

**只有在启用了 `entra_sso=1` 时才需要。** 这通常包括：

- Bedrock
- 使用 bootstrap endpoint
- 使用 extension attrs

此时请阅读并执行：

[consent](file:///Users/saga/code-repos/financial-services-plugins/中文版/claude-for-msft-365-install/commands/consent.md)

## 第 3 步：区分组织级配置与用户级配置

加载项会优先读取 per-user attrs，然后才回退到 manifest 参数。
因此你要明确：**第 1 步收集到的哪些值对所有用户一致，哪些会因人而异？**

要具体问，不要让客户自行抽象：

- Gateway：URL 是否统一？token 是否每人不同？
- Vertex：project / region 是否因团队不同？
- Bedrock：role 是否按团队区分？

| 回答 | 处理 |
|---|---|
| 所有值都一致 | 全部写入 manifest，跳过第 5 步 |
| 部分值因用户而异 | 因用户而异的部分进入第 5 步，其余写入 manifest |

## 第 4 步：生成 manifest

用第 3 步中确定的**组织级参数**生成 manifest。请阅读并执行：

[manifest](file:///Users/saga/code-repos/financial-services-plugins/中文版/claude-for-msft-365-install/commands/manifest.md)

常用命令：

```bash
node "${CLAUDE_PLUGIN_ROOT}/scripts/build-manifest.mjs" office manifest.xml <key>=<value> ...
node "${CLAUDE_PLUGIN_ROOT}/scripts/build-manifest.mjs" outlook manifest-outlook.xml <key>=<value> ...
```

然后验证：

```bash
npx -y office-addin-manifest validate manifest.xml
npx -y office-addin-manifest validate manifest-outlook.xml
```

## 第 5 步：用户级配置

只有当第 3 步决定部分参数按用户变化时才执行。

| 需要承载的内容 | 方案 | 说明文档 |
|---|---|---|
| 少量字符串，例如 token、region | Extension attrs | [update-user-attrs](file:///Users/saga/code-repos/financial-services-plugins/中文版/claude-for-msft-365-install/commands/update-user-attrs.md) |
| `mcp_servers`、`skills`、结构化对象 | Bootstrap endpoint | [bootstrap](file:///Users/saga/code-repos/financial-services-plugins/中文版/claude-for-msft-365-install/commands/bootstrap.md) |

如果只是少量字符串，attrs 更简单；如果是结构化配置，则应走 bootstrap。

## 第 6 步：验证模型可达

在真正部署前，必须确认至少有一个 Claude 模型是可调用的，例如：

- Claude Sonnet 4.5
- Claude Opus 4.5

### Gateway 验证

按 `gateway_api_format` 使用不同探测方式：

默认 Anthropic：

```bash
curl -s -o /dev/null -w '%{http_code}\n' "<gateway_url>/v1/messages" \
  -H 'content-type: application/json' -H 'authorization: Bearer <token>' \
  -d '{"model":"claude-sonnet-4-5","max_tokens":1,"messages":[{"role":"user","content":"hi"}]}'
```

Bedrock pass-through：

```bash
curl -s -o /dev/null -w '%{http_code}\n' \
  "<gateway_url>/model/anthropic.claude-sonnet-4-5-v1:0/invoke" \
  -H 'content-type: application/json' -H 'authorization: Bearer <token>' \
  -d '{"anthropic_version":"bedrock-2023-05-31","max_tokens":1,"messages":[{"role":"user","content":"hi"}]}'
```

Vertex pass-through：

```bash
curl -s -o /dev/null -w '%{http_code}\n' \
  "<gateway_url>/projects/<gcp_project_id>/locations/<gcp_region>/publishers/anthropic/models/claude-sonnet-4-5:rawPredict" \
  -H 'content-type: application/json' -H 'authorization: Bearer <token>' \
  -d '{"anthropic_version":"vertex-2023-10-16","max_tokens":1,"messages":[{"role":"user","content":"hi"}]}'
```

### Vertex / Bedrock 验证

- Vertex：确认 Model Garden 页面已显示 **Enabled**
- Bedrock：确认对应模型访问页已显示 **Access granted**

不要在这一步含糊带过，必须确认模型真的可达。

## 第 7 步：部署

最后引导管理员上传到：

```text
https://admin.cloud.microsoft/?#/Settings/IntegratedApps
```

流程大致是：

1. Upload custom apps
2. 选择 Office Add-in
3. 上传 `manifest.xml`

### 用户分配策略

- 如果没有用户级配置：可以直接选 **Entire organization**
- 如果配置按用户分发：应只分配给那些已写入 attrs 或已支持 bootstrap 的用户 / 组
- 首次部署建议先选自己或小范围试点组

完成后提醒管理员：

- 首次部署传播最长可达 24 小时
- 加载项通常会出现在 **Home → Add-ins**

最后把生成的 manifest 路径和分配范围写回设置日志，作为完整交付记录。
