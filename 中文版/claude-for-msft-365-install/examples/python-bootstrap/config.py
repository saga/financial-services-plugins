"""
编辑此文件以配置你的 bootstrap 服务器。app.py 不需要修改。
"""
import base64
import os

# ─── 基础配置 ──────────────────────────────────────────────────────────
# 你的 Entra 租户 ID（必需的环境变量）
TENANT_ID = os.environ["TENANT_ID"]                         # 你的 Entra 租户

# Claude in Office 加载项的应用 ID（固定值，用于验证令牌受众）
AUDIENCE  = "c2995f31-11e7-4882-b7a7-ef9def0a0266"          # Claude in Office add-in app ID

# 令牌签发者 URL（基于租户 ID 构建）
ISSUER    = f"https://login.microsoftonline.com/{TENANT_ID}/v2.0"

# JWKS 端点 URL（用于获取验证 JWT 签名的公钥）
JWKS_URL  = f"https://login.microsoftonline.com/{TENANT_ID}/discovery/v2.0/keys"

# 服务器监听地址和端口（可配置的环境变量）
HOST      = os.getenv("HOST", "127.0.0.1")
PORT      = int(os.getenv("PORT", "8080"))

# ─── 开发模式配置 ─────────────────────────────────────────────────────
# 本地开发覆盖：指向自签名的 JWKS 而非 Entra。
# 签名验证仍然运行。拒绝在非回环地址上启动。
# 设置 DEV_JWKS_PATH 环境变量以启用开发模式
DEV_JWKS_PATH = os.getenv("DEV_JWKS_PATH")

# 安全检查：开发模式只能在本地回环地址使用
if DEV_JWKS_PATH and HOST != "127.0.0.1":
    raise SystemExit("DEV_JWKS_PATH may only be used when HOST=127.0.0.1")

# ─── 目录：你可能分发的所有技能 / MCP 服务器 ───────────────────
# 辅助函数：将字符串编码为 Base64
def b64(s: str) -> str:
    return base64.b64encode(s.encode()).decode()

# 技能目录：定义所有可用的技能及其配置
# 每个技能可以有两种格式：
#   1. url: 技能包的下载 URL（如 ZIP 文件）
#   2. content: 技能内容的 Base64 编码字符串（内联技能）
SKILLS = {
    "deal-memo": {
        "description": "Draft a deal memo from a term sheet",  # 从条款清单起草交易备忘录
        "url": "https://your-bucket.s3.amazonaws.com/skills/deal-memo.zip?X-Amz-Signature=...",
    },
    "compliance-check": {
        "description": "Review a document for compliance issues",  # 审查文档的合规性问题
        "content": b64("# Compliance check\\n\\nReview document for regulatory red flags..."),
    },
    "risk-dashboard": {
        "description": "Summarize positions from risk dashboard",  # 从风险仪表板汇总持仓
        "url": "https://your-bucket.s3.amazonaws.com/skills/risk.zip?X-Amz-Signature=...",
    },
}

# MCP 服务器目录：定义所有可用的 MCP 服务器及其配置
# 每个 MCP 服务器可以包含：
#   url: MCP 服务器的 SSE 或 HTTP 端点
#   label: 显示给用户的标签
#   headers: 可选的 HTTP 头（如认证令牌）
MCP_SERVERS = {
    "linear": {
        "url": "https://mcp.linear.app/sse",  # Linear 项目的 MCP 服务器
        "label": "Linear",
    },
    "risk-api": {
        "url": "https://internal.example.com/mcp/risk",  # 内部风险 API 的 MCP 服务器
        "label": "Risk Dashboard",
        "headers": {"Authorization": "Bearer {{gateway_token}}"},  # 使用网关令牌认证
    },
}

# ─── RBAC 规则：首条匹配规则生效 ──────────────────────────────────
# `when` 条件（必须全部匹配）:
#   group — 来自 Entra 令牌 `groups` 声明的值
#   user  — Entra 用户的 `oid`（对象 ID）
#   app   — Office 主机应用: "word" | "excel" | "powerpoint"
#
# 生产环境中，group/user 值是 GUID — 将下面的名称替换为
# Entra 管理中心中的真实对象 ID
RULES = [
    # 规则 1：投资银行组用户在 Word 中可以使用 deal-memo 和 compliance-check 技能，以及 Linear MCP 服务器
    {"when": {"app": "word", "group": "investment-banking"},
     "skills": ["deal-memo", "compliance-check"], "mcp_servers": ["linear"]},

    # 规则 2：风险组用户可以使用 risk-dashboard 和 compliance-check 技能，以及风险 API MCP 服务器
    {"when": {"group": "risk"},
     "skills": ["risk-dashboard", "compliance-check"], "mcp_servers": ["risk-api"]},

    # 规则 3：特定用户 alice 可以使用 deal-memo 技能
    {"when": {"user": "alice"},
     "skills": ["deal-memo"], "mcp_servers": []},

    # 默认规则：所有用户都可以使用 compliance-check 技能
    {"when": {}, "skills": ["compliance-check"], "mcp_servers": []},
]
