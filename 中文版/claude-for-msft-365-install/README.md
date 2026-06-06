# Claude for Office：直连云端部署

用于帮助管理员配置 Claude Office 加载项，使其调用你自有的云端
（Vertex AI、Bedrock 或 LLM 网关），而不是 Anthropic 的 API。

## 安装

```bash
claude plugin marketplace add anthropics/financial-services
claude plugin install claude-for-msft-365-install@claude-for-financial-services
```

然后在当前会话内运行：

```text
/claude-for-msft-365-install:setup
```

## 更新

拉取插件最新版本：

```bash
claude plugin update claude-for-msft-365-install@claude-for-financial-services
```

重启当前会话以应用更新。只有在你需要用新选项重新生成清单时，才需要再次运行
`/claude-for-msft-365-install:setup`。

## Bootstrap

如果你需要按用户下发 MCP server、skills 或动态配置，可以部署一个
bootstrap 端点，并让加载项在启动时调用它：

```bash
claude plugin marketplace add anthropics/financial-services   # 如尚未添加
claude plugin install claude-for-msft-365-install@claude-for-financial-services
```

然后在会话中运行：

```text
/claude-for-msft-365-install:bootstrap
```

## 命令

| 命令 | 作用 |
|---|---|
| `/claude-for-msft-365-install:setup` | 交互式向导：配置云资源、管理员同意并生成 manifest |
| `/claude-for-msft-365-install:manifest` | 生成定制化的加载项 manifest XML |
| `/claude-for-msft-365-install:consent` | 生成该加载项应用注册所需的 Azure 管理员同意链接 |
| `/claude-for-msft-365-install:update-user-attrs` | 通过 Microsoft Graph 写入用户级扩展属性配置 |
| `/claude-for-msft-365-install:bootstrap` | 设计 bootstrap 端点，用于按用户下发 MCP server、skills 和动态配置 |
| `/claude-for-msft-365-install:debug` | 诊断部署问题，例如旧配置缓存、连接失败或加载项缺失 |
