---
description: 生成包含自有云配置的加载项 manifest XML
---

# 生成加载项 manifest

该脚本会获取标准 manifest 模板，并把你的配置作为 URL 查询参数追加进去。
加载项启动时会读取这些参数。Outlook 使用单独模板，因为微软的 `MailApp`
schema 与 Excel / Word / PowerPoint 使用的 `TaskPaneApp` schema 不同。

因此，开始之前要先确认：用户要部署的是 `office`、`outlook`，还是两者都要。

| Host 参数 | 对应应用 | 模板 |
|---|---|---|
| `office` | Excel、Word、PowerPoint | `pivot.claude.ai/manifest.xml` |
| `outlook` | Outlook（邮件与日历） | `pivot.claude.ai/manifest-outlook-3p.xml` |

## 按云类型需要的键

只询问该部署路径需要的参数，不要把所有字段都问一遍。

| 云类型 | 所需键 |
|---|---|
| Vertex | `gcp_project_id` `gcp_region` `google_client_id` `google_client_secret` |
| Bedrock | `aws_role_arn` `aws_region` |
| Foundry | `azure_resource_name` `azure_api_key` |
| Gateway | `gateway_url` `gateway_token` `gateway_auth_header` `gateway_api_format` |
| Gateway（`gateway_api_format=vertex`） | 还需要 `gcp_project_id` `gcp_region` |

当前 **Outlook host 不支持 Bedrock**。如果给 `outlook` 传入 `aws_*` 键，
脚本会直接报错退出。

## Outlook：Microsoft Graph

Outlook 通过 Microsoft Graph 读取邮箱和日历，因此无论模型实际运行在哪个云，
都需要先做一次租户级管理员同意。部署前请先运行：

[consent](file:///Users/saga/code-repos/financial-services-plugins/中文版/claude-for-msft-365-install/commands/consent.md#outlookmicrosoft-graph-同意)

如果客户策略不允许同意第三方应用，则需要他们自建 Entra app，并在生成
Outlook manifest 时提供 `graph_client_id`。

## 主权云 / 国家云

加载项会根据 Office 返回的 authority host 自动检测所处国家云，并匹配对应的
Graph 与 Entra endpoint，所以大多数主权云场景下不需要额外配置 URL。

真正重要的是：**这类租户通常必须自带 Entra 应用**，也就是通过
`graph_client_id` 指向客户自己在该环境中注册的应用。

### 何时需要设置 `graph_cloud`

`graph_cloud` 是一个枚举值，而不是 URL：

| 租户类型 | `graph_cloud` | 说明 |
|---|---|---|
| Commercial / GCC | `global` | 默认值，可省略 |
| GCC High | `us-gov-high` | 通常可自动识别，也可以显式固定 |
| US Gov DoD | `us-gov-dod` | 必须显式设置 |
| China (21Vianet) | `china` | 可自动识别，也可以显式固定 |

如果设置了非 `global` 的 `graph_cloud`，则必须同时设置 `graph_client_id`。

## Entra SSO

设置 `entra_sso=1` 后，加载项会在启动时主动获取用户的 Entra token。
这适用于：

- Bedrock：该 token 作为 STS web identity
- bootstrap endpoint：作为 Bearer token
- per-user attrs：从 token claims 中读取 `extn.*` 扩展属性

如果只是静态 gateway 配置，或纯 Vertex 且不依赖 Entra，可以不启用。

### 自带 Entra 应用

默认情况下，加载项会以 Anthropic 的多租户应用请求 token。如果你的 bootstrap
端点或 token exchange 服务要求 `aud` 必须是你自己租户里的应用，那么就需要设置：

```text
graph_client_id=<your-app-guid>
```

### 使用 access token 而不是 ID token

如果只设置了 `graph_client_id`，加载项通常仍发送 ID token。若你的服务需要
标准 OAuth2 access token（校验 `aud` + `scp`），则应额外设置：

```text
entra_scope=api://<your-app-guid>/<scope>
```

此时加载项会申请 access token，Bearer token 中会包含 `scp`。

`entra_scope` 必须与 `graph_client_id` 搭配使用。

## Bootstrap endpoint

`bootstrap_url` 指向你托管的 HTTPS 端点。加载项启动时会调用它获取用户级配置，
包括 provider 键、`mcp_servers`、`skills` 等。

完整协议说明见：

[bootstrap](file:///Users/saga/code-repos/financial-services-plugins/中文版/claude-for-msft-365-install/commands/bootstrap.md)

## MCP servers

`mcp_servers` 是一个 JSON 数组，表示加载项要直接连接的 MCP server 列表。
统一配置时可以直接写在 manifest 中；如果要按用户区分，应放到 bootstrap 层。

示例：

```bash
mcp_servers='[{"url":"{{gateway_url}}/deepwiki/mcp","label":"DeepWiki","headers":{"Authorization":"Bearer {{gateway_token}}"}}]'
```

## Telemetry

可通过以下键把加载项的 OpenTelemetry traces 发送到你自己的 collector：

- `otlp_endpoint`
- `otlp_headers`
- `otlp_resource_attributes`

如果要做统一的组织级采集，可以写在 manifest 中；如果需要按用户或团队路由，
建议放到 bootstrap 或 extension attrs。

## Inference headers

`inference_headers` 是一个 JSON 对象，会加到发往 `gateway_url` 的推理请求上。
适合用于计费标签、内部系统标识等。

```bash
inference_headers='{"x-application-id":"app123"}'
```

某些头部是保留的，加载项会自动忽略，例如：

- `Authorization`
- `x-api-key`
- `Content-Type`
- `Host`
- `Content-Length`
- `User-Agent`
- `Cookie`
- 任意 `anthropic-*` / `x-amz-*` / `x-goog-*`

## Auto-connect

默认情况下，只要某个 provider 所需字段齐全，用户会跳过连接表单直接进入聊天界面。
如果你希望仍然显示预填好的连接表单，让用户确认后再继续，请设置：

```text
auto_connect=0
```

## 是否允许回退到 Claude.ai 登录

只要存在任意企业配置，加载项默认会隐藏回到 Claude.ai 登录页的 **Back** 按钮，
即默认 `allow_1p=0`。如果你希望保留该按钮，请设置：

```text
allow_1p=1
```

## Disabled features

`disabled_features` 是逗号分隔的功能禁用列表。当前主要支持：

| Slug | 作用 |
|---|---|
| `skills.authoring` | 禁止创建、编辑、上传技能；不影响运行管理员预置技能 |

例如：

```bash
disabled_features='skills.authoring'
```

## Version

M365 Admin Center 会基于 `<Id>` + `<Version>` 做缓存。
如果你是更新已有部署，必须提升 `<Version>`，否则重新上传可能被静默忽略。

## 执行命令

```bash
node "${CLAUDE_PLUGIN_ROOT}/scripts/build-manifest.mjs" office manifest.xml \
  gcp_project_id=<value> \
  gcp_region=<value> \
  auto_connect=0 \
  ...

# 如果还要部署 Outlook：
node "${CLAUDE_PLUGIN_ROOT}/scripts/build-manifest.mjs" outlook manifest-outlook.xml \
  <same provider keys as above> \
  graph_client_id=<value>
```

该脚本会校验 key 名称，未知 key 会直接报错。

## 验证

```bash
npx --yes office-addin-manifest validate manifest.xml
```

如果校验通过，但 M365 Admin Center 上传时仍报错或不生效，优先对照下列常见问题：

| 现象 | 处理方式 |
|---|---|
| “An add-in with this ID already exists” | 生成新的 `<Id>` UUID |
| 重新上传成功但没变化 | 提升 `<Version>` 的第 4 段 |
| 只想支持 Excel，不要 PowerPoint | 删除两个 `<Hosts>` 列表中的 `Presentation` |
| 不需要 Outlook | 不生成 Outlook manifest 即可 |
