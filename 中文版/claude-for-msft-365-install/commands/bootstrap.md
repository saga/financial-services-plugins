---
description: 构建 bootstrap 端点，用于按用户下发 MCP servers、skills 和动态配置
---

# Bootstrap 端点

你需要托管一个 HTTPS `GET` 处理器。加载项启动时会携带用户的 Entra token
调用它，你返回该用户专属的 JSON 配置，响应内容会覆盖 manifest 和
extension attributes 中的用户配置。对于 `mcp_servers`、`skills`
这类无法用扁平字符串表达的结构化配置，这就是标准做法。

## 先确认用户意图

在开始解释规范前，先弄清楚用户处于哪种模式：

- **只是想理解机制？** 直接根据下方章节回答。常见问题包括：响应结构长什么样、
  `{{...}}` 模板如何替换、为什么会被 CORS 卡住。
- **准备实际搭建？** 先问：是新建 handler 还是修改现有服务？部署在 Lambda、
  Cloud Function、Express、Python 还是其他环境？然后直接跳到
  [搭建 handler](#搭建-handler) 一节，其间的内容就是它需要遵守的协议。

## 它与扩展属性的区别

两者都能做按用户下发配置，区别在于承载能力：

| | [扩展属性](update-user-attrs.md) | Bootstrap 端点 |
|---|---|---|
| 你要维护什么 | 针对每个用户执行 `az rest PATCH` | 一个 HTTPS 服务 |
| 能承载的内容 | 扁平字符串，长度通常不超过 256 字符 | 任意 JSON，支持数组、嵌套和 base64 |
| 适合场景 | 按用户轮换 token、区域覆盖 | `mcp_servers`、`skills`、复杂动态配置 |
| 刷新方式 | 依赖 token 缓存，通常约 1 小时延迟 | 由 `bootstrap_expires_at` 控制 |
| 认证方式 | 被动读取 Entra token claims | 你主动校验 JWT |

如果你只想给每个用户下发不同的 `gateway_token`，扩展属性更省事；一旦你需要
按照部门动态分配 Linear / Jira / 内网 MCP server，就该用 bootstrap。

## 模板插值

任意字符串字段都可以写 `{{key}}`。加载项会基于**合并后的配置链**做替换：
manifest 参数 → extension attrs → 本次 bootstrap 响应，后者覆盖前者。

这意味着：

1. **`bootstrap_url` 本身** 只会用 manifest + attrs 做插值。
2. **bootstrap 响应里的字段** 则会基于完整合并结果插值，也就是 manifest +
   attrs + 当前响应。

例如，如果 `gateway_token` 已经存在于 manifest 或 attrs 中，那么响应里的：

```json
{
  "mcp_servers": [
    {
      "url": "https://internal.example.com/mcp",
      "headers": { "Authorization": "Bearer {{gateway_token}}" }
    }
  ]
}
```

就会自动得到替换。

如果某个 `{{key}}` 没有被解析出来（例如拼错了，或根本没有在任一层设置），
它会原样保留，不会报错也不会替换为空字符串。排查 MCP server 连接失败时，
一定要检查最终构造出来的 URL 和 header。

## CORS：每个 URL 都要配

加载项本质上运行在浏览器 WebView 里。它访问的每个 URL 都发生在浏览器侧，
因此都必须允许来自 `https://pivot.claude.ai` 的跨域访问。

最常见的失败原因就是：服务端返回 200，但浏览器因为 CORS 把响应拦截掉，
加载项看起来像“没有收到任何内容”。

| URL | CORS 应配置在哪里 |
|---|---|
| `bootstrap_url` | 你的 handler 响应头；如果挂在 API Gateway / Cloud Functions 后，还要处理 `OPTIONS` 预检 |
| `mcp_servers[].url` | MCP server 自己的响应头 |
| `skills[].url` | 对应存储桶的 CORS，而不是 presigned URL 本身 |
| `otlp_endpoint` | 你的 OTEL collector 的 HTTP receiver |

对 `bootstrap_url`，推荐的预检响应头如下：

```text
Access-Control-Allow-Origin:  https://pivot.claude.ai
Access-Control-Allow-Methods: GET
Access-Control-Allow-Headers: Authorization, X-Claude-User-Agent, *
```

技能文件托管在对象存储时，尤其容易踩坑。`curl` 可以访问成功并不代表浏览器能成功，
因为 `curl` 不会执行 CORS 校验。你必须在 S3 / GCS / Azure Blob 上单独配置 bucket CORS。

## 请求格式

```text
GET <bootstrap_url>
Authorization: Bearer <entra_token>         # 仅在 manifest 设置了 entra_sso=1 时存在
X-Claude-User-Agent: claude-<app>/<version> # 始终存在
```

`X-Claude-User-Agent` 可以帮助你识别当前运行宿主是 `word`、`excel`
还是 `powerpoint`，也可用于按 Office 产品区分下发不同配置。

如果设置了 `entra_sso=1`，你必须在服务端验证 JWT，至少核验：

| Claim | 检查点 |
|---|---|
| `aud` | 是否为默认加载项应用 ID，或你在 manifest 里设置的 `graph_client_id` / API App ID URI |
| `iss` | 是否为你自己的租户颁发者 |
| `exp` | 是否过期 |
| `oid` | 是否存在，用作用户稳定标识 |

强烈建议使用成熟 JWT 库，不要手写校验逻辑。

## 响应格式

返回：

- `200 OK`
- `Content-Type: application/json`
- 正确的 CORS 头

响应体是一个扁平对象。所有字段都是可选的，你只需要返回对该用户有差异的键。

### Provider 配置键

你可以返回与 [manifest](manifest.md#keys-by-cloud) 中相同的一组云配置键，
例如 `gateway_url`、`gateway_token`、`aws_role_arn`、`gcp_region` 等。

### Telemetry

```json
"otlp_endpoint": "https://otel-collector.your-domain.com",
"otlp_headers": "Authorization=Bearer {{gateway_token}}",
"otlp_resource_attributes": "team.name={{team}},deployment.environment=prod"
```

这些字段用于把加载项的 OpenTelemetry span 发送到你自己的 collector。

### `inference_headers`

```json
"inference_headers": { "x-application-id": "app123" }
```

会附加到发往 `gateway_url` 的每次推理请求上，适合做内部计费或应用标识。

### `mcp_servers`

```json
"mcp_servers": [
  { "url": "https://mcp.linear.app/sse", "label": "Linear" },
  {
    "url": "https://internal.yourcompany.com/mcp/risk",
    "label": "Risk Dashboard",
    "headers": { "Authorization": "Bearer {{gateway_token}}" }
  }
]
```

| 字段 | 说明 |
|---|---|
| `url` | MCP server 地址，支持模板替换 |
| `label` | 在加载项 UI 中展示的名称 |
| `headers` | 可选，请求该 server 时附带的头 |

### `skills`

```json
"skills": [
  {
    "name": "deal-memo",
    "description": "根据 term sheet 草拟 deal memo",
    "url": "https://yourbucket.s3.amazonaws.com/skills/deal-memo.zip?..."
  },
  {
    "name": "compliance-check",
    "content": "IyBDb21wbGlhbmNlIGNoZWNrCgpSZXZpZXcgdGhlIGRvY3VtZW50IGZvci4uLg=="
  }
]
```

| 字段 | 说明 |
|---|---|
| `name` | skill 标识符 |
| `description` | 可选，显示在 skill 选择器中 |
| `content` | base64 内容，可以是原始 `SKILL.md`，也可以是 zip |
| `url` | 指向技能包的 presigned URL，需自行处理 CORS |

### `disabled_features`

```json
"disabled_features": ["skills.authoring"]
```

用于按用户禁用部分功能。

### `bootstrap_expires_at`

表示该配置的过期时间（Unix 秒或毫秒时间戳，加载项会自动识别）。
如果你在响应中下发的是短期凭证，建议一定设置。

## 搭建 handler

一个可运行的 Python / FastAPI 参考实现位于：

[python-bootstrap](file:///Users/saga/code-repos/financial-services-plugins/claude-for-msft-365-install/examples/python-bootstrap/README.md)

如果用户希望你帮他直接实现一个 handler，请重点确保以下几点：

- **JWT 校验是安全边界**：校验签名、`aud`、`iss`，并使用 `oid` 做用户查找。
- **你返回的每个 URL 都要处理 CORS**：不仅是 handler 本身，还包括技能 URL、
  MCP server、OTLP collector。
- **用户配置查找逻辑是客户自己的业务逻辑**：要明确留出
  “按 `oid` 查库/查配置”的实现位置，不要擅自假设其数据源。
- **尽量返回稀疏对象**：只有与 manifest 默认值不同的内容才需要返回。

在真正写实现前，先问清楚：

- 部署环境是什么（Lambda / Express / Cloud Function / 其他）？
- 用户级配置存在哪里（数据库 / YAML / KV / 内联配置）？
