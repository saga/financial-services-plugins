---
description: 通过 Azure AD 扩展属性为用户设置个性化配置（token、区域覆盖等）
---

# 通过扩展属性配置按用户参数

这些属性已经预注册在 Anthropic 的应用
`c2995f31-11e7-4882-b7a7-ef9def0a0266` 上，你不需要自建 schema，
只需要写值。加载项会从用户 ID token 中读取：

```text
extension_c2995f3111e74882b7a7ef9def0a0266_<key>
```

**前提：manifest 中必须设置 `entra_sso=1`。**
否则加载项不会去获取 Entra token，也就根本读不到这些扩展属性。

## 可以写哪些键

任意配置键理论上都可以按用户写入，加载项会用 per-user attrs 覆盖 manifest。
但每个值长度上限通常为 256 字符，因此只适合扁平、小型配置。

| Key | 典型用途 |
|---|---|
| `gateway_token` | 每个用户单独 API key |
| `gateway_url` | 不同团队走不同 gateway |
| `gateway_api_format` | 用户级 gateway 接口格式差异 |
| `inference_headers` | 用户级计费标签（注意长度限制） |
| `bootstrap_url` | 用户级 bootstrap 入口 |
| `gcp_project_id` | 团队级 GCP project 差异 |
| `gcp_region` | 数据驻留区域覆盖 |
| `google_client_id` / `google_client_secret` | 少见，按团队区分 OAuth client |
| `aws_role_arn` / `aws_region` | 不同团队使用不同 Bedrock role |
| `otlp_endpoint` / `otlp_headers` / `otlp_resource_attributes` | 按团队把 trace 路由到不同 OTEL collector |

## 为单个用户写入

把 `<key>` 替换为上表中的属性名。对于非敏感字段（例如 region、project ID），
这通常就是最直接的方式。

```bash
az rest --method PATCH \
  --uri "https://graph.microsoft.com/v1.0/users/<upn>" \
  --body '{"extension_c2995f3111e74882b7a7ef9def0a0266_<key>":"<value>"}'
```

成功时通常返回 204 且没有 body。可用以下命令验证：

```bash
az rest --method GET --uri "https://graph.microsoft.com/v1.0/users/<upn>?\$select=extension_c2995f3111e74882b7a7ef9def0a0266_<key>"
```

如果你想查看该用户当前所有扩展属性，可以使用 `/beta/`：

```bash
az rest --method GET --uri "https://graph.microsoft.com/beta/users/<upn>" | jq 'to_entries | map(select(.key | startswith("extension"))) | from_entries'
```

## 批量写入（推荐用于敏感值）

如果管理员不希望敏感值出现在聊天记录或 shell history 中，可以让他准备一个
`users.csv`，格式如下：

```csv
upn,gateway_token,gcp_region
alice@acme.com,sk-live-aaa,
bob@acme.com,sk-live-bbb,europe-west4
carol@acme.com,,europe-west4
```

### macOS / Linux

把下面内容保存为 `apply.sh`，与 `users.csv` 放在同目录，然后运行：

```bash
bash apply.sh
```

```bash
#!/bin/bash
EXT=extension_c2995f3111e74882b7a7ef9def0a0266_
{
  IFS=, read -ra keys
  while IFS=, read -ra vals; do
    upn="${vals[0]}"
    for i in "${!keys[@]}"; do
      [ "$i" -eq 0 ] || [ -z "${vals[$i]}" ] && continue
      az rest --method PATCH --uri "https://graph.microsoft.com/v1.0/users/$upn" \
        --body "{\"${EXT}${keys[$i]}\":\"${vals[$i]}\"}" \
        && echo "✓ $upn ${keys[$i]}" || echo "✗ $upn ${keys[$i]}"
    done
  done
} < users.csv
```

### Windows

把下面内容保存为 `apply.ps1`，与 `users.csv` 同目录后执行：

```powershell
$EXT = 'extension_c2995f3111e74882b7a7ef9def0a0266_'
Import-Csv users.csv | ForEach-Object {
  $upn = $_.upn
  $_.PSObject.Properties | Where-Object { $_.Name -ne 'upn' -and $_.Value } | ForEach-Object {
    $body = @{ "$EXT$($_.Name)" = $_.Value } | ConvertTo-Json -Compress
    az rest --method PATCH --uri "https://graph.microsoft.com/v1.0/users/$upn" --body $body
    if ($?) { "OK $upn $($_.Name)" } else { "FAIL $upn $($_.Name)" }
  }
}
```

执行完成后，汇总成功和失败数量即可。

常见失败原因：

- `404`：UPN 写错了
- `403`：当前 `az login` 账号缺少 `User.ReadWrite.All`

## 生效延迟

Graph 写入通常立即成功，但加载项不是直接从 Graph 读，而是通过用户的 ID token
读取这些 claim，而 Azure STS 会缓存 token claim。

因此，实际在加载项中看到新值，通常可能需要**最多约一小时**。

如果管理员刚 PATCH 完就打开加载项却发现行为仍然没变，这通常不是写入失败，
而是 token 还没刷新。建议：

- 完整退出 Office 应用
- 重新打开并重新触发 NAA 登录
- 或等待一段时间后再试
