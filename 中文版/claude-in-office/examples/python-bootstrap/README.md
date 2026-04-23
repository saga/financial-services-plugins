# Claude in Office 中文注释说明

本目录包含 `claude-in-office` 项目的 Python 代码文件，已添加详细的中文注释说明。

## 文件说明

### app.py
**主应用程序文件** - Bootstrap 端点的 FastAPI 实现

**主要功能：**
- 提供 `/bootstrap` HTTP 端点供 Office 加载项调用
- 验证用户 JWT 令牌（来自 Microsoft Entra ID）
- 根据用户身份、所属组和应用类型解析可用的技能和 MCP 服务器
- 返回用户配置信息

**关键函数：**
- `parse_app()`: 从用户代理字符串解析 Office 应用类型
- `resolve()`: 根据 RBAC 规则解析用户可用的技能和 MCP 服务器
- `validate()`: 验证 JWT 令牌的有效性

**配置依赖：**
- 所有可配置参数在 `config.py` 中定义
- 无需修改此文件即可自定义行为

### config.py
**配置文件** - 所有可由客户编辑的设置

**主要配置项：**
- **基础配置**: 租户 ID、应用 ID、服务器地址和端口
- **技能目录 (SKILLS)**: 定义所有可用的技能及其配置
  - 支持两种格式：URL 下载或内联内容（Base64 编码）
- **MCP 服务器目录 (MCP_SERVERS)**: 定义所有可用的 MCP 服务器
  - 支持 SSE 或 HTTP 端点
  - 可配置自定义 HTTP 头（如认证令牌）
- **RBAC 规则 (RULES)**: 基于角色和组的访问控制规则
  - 支持按用户、组、应用类型进行权限控制
  - 首条匹配规则生效

**使用说明：**
- 编辑此文件以配置你的技能和 MCP 服务器
- 修改 RBAC 规则以控制不同用户的访问权限
- 无需修改 `app.py`

### get_tenant_id.py
**工具脚本** - 获取 Entra 租户 ID

**使用方法：**
```bash
# 从邮箱域名获取
python get_tenant_id.py alice@yourcompany.com

# 从域名获取
python get_tenant_id.py yourcompany.com

# 从 Azure CLI 获取（需要先登录）
python get_tenant_id.py
```

**返回值：**
- Entra 租户 ID（GUID 格式）

**用途：**
- 在运行 `app.py` 前，将获取的租户 ID 设置为 `TENANT_ID` 环境变量

### mint_dev_token.py
**开发工具** - 生成自签名的开发令牌

**使用方法：**
```bash
# 首次运行：生成密钥对和 JWKS
python mint_dev_token.py --oid alice --group investment-banking

# 后续运行：重用现有密钥
python mint_dev_token.py --oid alice --group risk
```

**参数说明：**
- `--oid`: 用户的对象 ID（Object ID），默认为 "alice"
- `--group`: 用户所属的安全组 ID（可多次使用）

**生成的文件：**
- `dev_private.pem`: RSA 私钥（PEM 格式）
- `dev_jwks.json`: JSON Web Key Set（用于验证签名）

**用途：**
- 在本地开发环境中测试 `app.py` 的令牌验证功能
- 无需连接 Microsoft Entra ID 即可模拟用户身份

## 开发流程

### 1. 设置环境变量
```bash
export TENANT_ID=<你的租户ID>
```

### 2. 配置技能和 MCP 服务器
编辑 `config.py`，添加你的技能和 MCP 服务器配置

### 3. 配置 RBAC 规则
编辑 `config.py` 中的 `RULES`，定义不同用户的访问权限

### 4. 启动服务器
```bash
python app.py
```

### 5. 测试（可选）
```bash
# 生成开发令牌
python mint_dev_token.py --oid alice --group investment-banking

# 使用令牌测试 /bootstrap 端点
curl -H "Authorization: Bearer <生成的令牌>" \
     -H "X-Claude-User-Agent: claude-word/1.0" \
     http://127.0.0.1:8080/bootstrap
```

## 生产部署注意事项

1. **移除开发模式配置**
   - 不要设置 `DEV_JWKS_PATH` 环境变量
   - 确保使用 Microsoft Entra ID 的 JWKS URL

2. **使用真实的租户 ID**
   - 使用 `get_tenant_id.py` 获取真实的租户 ID
   - 不要使用默认的 "dev-tenant"

3. **配置 RBAC 规则**
   - 将示例中的组名和用户 ID 替换为真实的 Entra ID 对象 ID
   - 在 Entra 管理中心获取真实的对象 ID

4. **部署到生产环境**
   - 使用 HTTPS 端点
   - 配置适当的 CORS 策略
   - 确保服务器安全性和可扩展性

## 技术栈

- **FastAPI**: Web 框架
- **PyJWT**: JWT 令牌处理
- **cryptography**: RSA 密钥生成和处理
- **Microsoft Entra ID**: 身份验证和授权

## 相关资源

- [Microsoft Entra ID 文档](https://learn.microsoft.com/en-us/entra/identity/)
- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [JWT 规范](https://jwt.io/)
