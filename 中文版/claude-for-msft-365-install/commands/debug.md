---
description: 诊断部署问题（旧配置缓存、连接失败、加载项缺失）
---

# 调试 Claude Office 部署

你正在协助企业管理员排查：为什么部署后的加载项工作异常。第一步永远是先问：
**具体哪里出了问题？**

## 初步分流

根据管理员描述的症状进入相应章节：

| 症状 | 对应章节 |
|---|---|
| 更新了 manifest，但用户看到的还是旧配置 | [更新后仍是旧配置](#更新后仍是旧配置) |
| 加载项提示 “Connection failed” | [读取错误详情](#读取错误详情) |
| Excel / PowerPoint 中根本看不到加载项 | [加载项未显示](#加载项未显示) |
| 想在本地先调试 manifest，再正式部署 | [本地 sideload manifest](#本地-sideload-manifest) |
| 登录弹窗反复失败或循环 | [管理员同意](#管理员同意) |
| 想查看浏览器控制台 | [打开浏览器开发者工具](#打开浏览器开发者工具) |

如果管理员手里已经有从加载项复制出来的错误详情（`Copy error details` 按钮），
优先从那里开始分析，因为它包含完整上下文。

## 读取错误详情

典型错误粘贴内容结构如下：

```text
Claude for Office connection failed (<Provider>)
Build: <sha>

<friendly message>

Request:
  <key>: <value actually sent>

Manifest params:
  <key>: <value from deployed manifest>

Raw error:
<SDK/HTTP error>
```

重点检查：

- `Request:` 与 `Manifest params:` 的差异。如果两者不同，说明用户手工覆盖了表单值。
- `Manifest params:` 里的 `m` 字段是版本标签。如果它低于你最后一次上传的版本，
  那就是旧 manifest 缓存问题。
- `Raw error:` 才是真正的根因。常见模式：
  - `invalid_client`：Google 客户端 ID / secret 配对错误
  - `Load failed (<host>)`：WebView 层面网络被阻断
  - `STS AssumeRoleWithWebIdentity failed`：AWS IAM OIDC provider 或 role trust policy 配置错误
  - `HTTP 401/403`：gateway token 无效或网关拒绝

## 更新后仍是旧配置

通常是两层缓存：

| 层级 | 谁持有 | 典型 TTL | 清理方式 |
|---|---|---|---|
| 服务端 | M365 Admin Center / Exchange Online | 更新最长约 72 小时，新部署约 24 小时 | 等待，或更换新的 `<Id>` 重新部署 |
| 客户端 | 本机 Office 的 Wef 缓存 | 直到 Office 完整重启 | 清理本地缓存 |

### 先确认 Admin Center 上的版本

如果你重新上传时没有提升 `<Version>`，Admin Center 可能会静默忽略这次上传。
去 M365 Admin Center 的 Integrated apps 页面里检查实际版本号。

### 强制刷新客户端缓存

请先完全退出 Excel / Word / PowerPoint，然后使用脚本清理缓存：

- macOS: [clear-addin-cache.sh](file:///Users/saga/code-repos/financial-services-plugins/claude-for-msft-365-install/scripts/clear-addin-cache.sh)
- Windows: [clear-addin-cache.ps1](file:///Users/saga/code-repos/financial-services-plugins/claude-for-msft-365-install/scripts/clear-addin-cache.ps1)

常见用法：

```bash
./scripts/clear-addin-cache.sh --id <GUID>
./scripts/clear-addin-cache.sh --id <GUID> --apply
```

```powershell
.\scripts\clear-addin-cache.ps1 -Id <GUID>
.\scripts\clear-addin-cache.ps1 -Id <GUID> -Apply
```

这些脚本默认 dry-run，不加 `--apply` / `-Apply` 不会实际删除内容。

**关键点：** 清理后必须完整重启 Office。仅关闭 taskpane 或最小化不算。

### 终极手段：更换新的 `<Id>`

如果 72 小时等待不可接受，可以直接给 manifest 生成一个新的 `<Id>`。
这样 M365 Admin Center 和所有客户端都会把它视为一个全新的加载项。

## 加载项未显示

- **功能区里没有：** 检查 M365 Admin Center 中该加载项是否已分配给当前用户或用户组。
- **“我的加载项”里有，但功能区按钮没有：** 检查 manifest 的 `<Hosts>` 是否包含当前 Office 宿主。
- **刚部署不到 24 小时：** 对首次部署来说是正常现象。

## 本地 sideload manifest

如果你想在本地快速迭代 manifest，而不经过 Admin Center 的 24-72 小时传播，
可以直接在本机 sideload。

辅助脚本如下：

- macOS: [sideload-addin.sh](file:///Users/saga/code-repos/financial-services-plugins/claude-for-msft-365-install/scripts/sideload-addin.sh)
- Windows: [sideload-addin.ps1](file:///Users/saga/code-repos/financial-services-plugins/claude-for-msft-365-install/scripts/sideload-addin.ps1)

```bash
./scripts/sideload-addin.sh ~/path/to/manifest.xml
```

```powershell
.\scripts\sideload-addin.ps1 C:\path\to\manifest.xml
```

之后完整重启 Excel / Word / PowerPoint，再到 **Insert → My Add-ins**
中查看。

本地 sideload 的 manifest 会覆盖同 `<Id>` 的中央部署版本，因此也是验证修复的快捷方式。

## 管理员同意

如果用户看到登录弹窗一闪而过、或登录反复循环，通常说明租户尚未完成
Claude 应用的管理员同意。此时请运行：

[consent](file:///Users/saga/code-repos/financial-services-plugins/中文版/claude-for-msft-365-install/commands/consent.md)

加载项错误详情里常见的表现是 `user_canceled`，但这通常并不是真正用户取消，
而是认证流程因未获批准而提前结束。

## Silent SSO / Entra token 故障

- **`AADSTS50194` 或提示必须使用 tenant-specific endpoint：**
  说明你使用的是单租户应用，但当前加载项版本还在走 `/common` authority。
  解决办法通常是升级加载项版本。
- **`entra_scope requires graph_client_id`：**
  说明设置了 `entra_scope` 却没设置 `graph_client_id`。
- **Silent SSO 失败，但交互式登录可成功：**
  这在管理员同意尚未完成、或 service principal 尚未创建时比较常见。

## 打开浏览器开发者工具

### macOS（Safari Web Inspector）

需要满足 3 个条件：

1. 开启 Office developer extras
2. 在 Safari 设置中开启 Develop 菜单
3. 在 macOS 的“隐私与安全性 → 开发者工具”中允许 Terminal

常用命令：

```bash
defaults write com.microsoft.Excel OfficeWebAddinDeveloperExtras -bool true
defaults write com.microsoft.Powerpoint OfficeWebAddinDeveloperExtras -bool true
defaults write com.microsoft.Word OfficeWebAddinDeveloperExtras -bool true
```

然后在任务窗格内右键选择 **Inspect Element**，或在 Safari → Develop
菜单中附加到对应页面。

### Windows（Edge DevTools）

如果机器使用 WebView2，通常可以直接在任务窗格内右键选择 **Inspect**。
如果右键菜单没有该项，可以安装 Edge DevTools Preview 并从其目标列表中附加。

旧版 Office 如果仍使用 IE11 / Trident，可运行：

```powershell
& "C:\Windows\SysWOW64\F12\IEChooser.exe"
```

然后在列表中选择对应的加载项页面。
