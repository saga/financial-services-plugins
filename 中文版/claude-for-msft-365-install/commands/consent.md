---
description: Azure 管理员同意链接，用于 Entra SSO 与 Outlook Graph 访问的一次性租户批准
---

# Azure 管理员同意

**只有在 manifest 中设置了 `entra_sso=1` 时才需要。** 如果你使用的是
组织级的 gateway 或 Vertex 配置且不依赖 Entra，则可跳过。如果你设置了
`graph_client_id`（即使用自有 Entra 应用），本页同样不适用，此时需要对你
自己的应用单独完成同意。

每个租户只需执行一次。全局管理员打开链接并点击 **Accept** 即可。在此之前，
租户内所有用户都会在加载项中遇到 NAA 登录失败。

## 同意链接

所有客户都使用同一个 URL，`/organizations/` 会根据当前登录管理员自动解析租户，
无需替换变量。

```text
https://login.microsoftonline.com/organizations/adminconsent?client_id=c2995f31-11e7-4882-b7a7-ef9def0a0266&redirect_uri=https://pivot.claude.ai/auth/callback
```

告诉客户：请在已登录**该租户全局管理员**的浏览器中打开此链接。管理员会看到一个
权限确认页，其中列出加载项会读取的内容（用户档案、扩展属性等）。点击
**Accept** 后，会进入一个确认页，显示类似“Admin consent granted, you can close this tab.”。

## 验证是否已生效

```bash
az ad sp show --id c2995f31-11e7-4882-b7a7-ef9def0a0266 --query appId -o tsv
```

如果返回相同的 GUID，说明该租户内已经创建了对应 service principal，
管理员同意已成功。如果报错提示 “does not exist”，则说明同意流程尚未完成。

## Outlook：Microsoft Graph 同意

**只有在部署 Outlook manifest 时才需要。** 这与上面的 `entra_sso`
是两件事；即使不开启 `entra_sso`，部署 Outlook 仍然需要这一步。

Claude for Outlook 通过 Microsoft Graph 读取邮件和日历。Graph token
始终保留在用户本机 Outlook 客户端中，不会发送到 gateway，也不会发送给
Anthropic，因此无论底层模型运行在哪个云上，这个同意 URL 都一样。

```text
https://login.microsoftonline.com/organizations/v2.0/adminconsent?client_id=c2995f31-11e7-4882-b7a7-ef9def0a0266&scope=https://graph.microsoft.com/Mail.ReadWrite%20https://graph.microsoft.com/Calendars.Read%20https://graph.microsoft.com/People.Read%20https://graph.microsoft.com/User.Read%20offline_access&redirect_uri=https://pivot.claude.ai/auth/callback
```

如果没有这一步，每位用户第一次尝试让 Claude 读取邮件时，都会遇到
“Need admin approval”。

**如果客户的安全策略禁止同意第三方应用：** 他们可以自行注册一个单租户的
Entra 应用，并赋予相同的委托式 Graph 权限（`Mail.ReadWrite`,
`Calendars.Read`, `People.Read`, `User.Read`, `offline_access`），
完成管理员同意后，在生成 Outlook manifest 时把该应用的 client ID
作为 `graph_client_id` 传入。数据流不变，只是审批主体从 Anthropic 的应用
换成了客户自己的应用。
