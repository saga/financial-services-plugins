#!/usr/bin/env python3
"""
Claude in Office — Bootstrap 端点参考实现

Office 加载项调用 GET /bootstrap 并携带用户的 Entra ID 令牌。
此服务器验证令牌，决定该员工可以使用哪些技能和 MCP 服务器，并返回它们。

所有可由客户编辑的设置都保存在 config.py 中 — 编辑 config.py，而非本文件。
"""
import re
import time

import jwt  # PyJWT
from config import (
    AUDIENCE,
    DEV_JWKS_PATH,
    HOST,
    ISSUER,
    JWKS_URL,
    MCP_SERVERS,
    PORT,
    RULES,
    SKILLS,
)
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from jwt import PyJWKClient

# ─── 用户代理解析 ─────────────────────────────────────────────────────
# 匹配 Office 应用的用户代理字符串，格式如 "claude-word/1.0" 或 "claude-excel/1.0"
# 用于确定用户正在使用的是哪个 Office 应用（Word、Excel 或 PowerPoint）
_UA_RE = re.compile(r"^claude-(word|excel|powerpoint)/", re.I)


def parse_app(user_agent: str | None) -> str:
    """
    从用户代理字符串中解析出 Office 应用类型

    参数:
        user_agent: HTTP 请求头中的用户代理字符串

    返回:
        小写的应用名称 ("word", "excel", "powerpoint") 或空字符串
    """
    m = _UA_RE.match(user_agent or "")
    return m.group(1).lower() if m else ""


def resolve(oid: str, groups: set[str], app: str) -> dict:
    """
    根据用户身份、所属组和应用类型，解析出可用的技能和 MCP 服务器

    参数:
        oid: 用户的 Entra ID 对象标识符 (Object ID)
        groups: 用户所属的安全组集合
        app: Office 应用类型 ("word", "excel", "powerpoint")

    返回:
        包含 "skills" 和 "mcp_servers" 的字典
    """
    # 遍历 RBAC 规则，按顺序匹配（首条匹配规则生效）
    for r in RULES:
        w = r["when"]
        # 检查用户条件：如果指定了用户且不匹配，则跳过此规则
        if "user" in w and w["user"] != oid:
            continue
        # 检查组条件：如果指定了组但用户不在该组中，则跳过此规则
        if "group" in w and w["group"] not in groups:
            continue
        # 检查应用条件：如果指定了应用且不匹配，则跳过此规则
        if "app" in w and w["app"] != app:
            continue
        # 所有条件匹配，返回该规则对应的技能和 MCP 服务器配置
        return {
            "skills":      [{"name": n, **SKILLS[n]} for n in r.get("skills", [])],
            "mcp_servers": [MCP_SERVERS[n] for n in r.get("mcp_servers", [])],
        }
    # 无匹配规则，返回空配置
    return {"skills": [], "mcp_servers": []}


# ─── 令牌验证 ────────────────────────────────────────────────────────
# JWKS 客户端用于获取用于验证 JWT 签名的公钥
# 开发模式下使用本地 JWKS 文件，生产模式连接 Microsoft Entra ID
_jwks = PyJWKClient(JWKS_URL) if not DEV_JWKS_PATH else None


def validate(auth_header: str) -> dict:
    """
    验证 HTTP Authorization 头中的 JWT 令牌

    参数:
        auth_header: Authorization HTTP 头，格式为 "Bearer <token>"

    返回:
        解码后的 JWT 声明 (claims)

    抛出:
        HTTPException: 令牌无效或缺失时返回 401 错误
    """
    # 检查 Authorization 头是否存在且格式正确
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(401, "Missing bearer token")
    
    # 提取令牌部分（去除 "Bearer " 前缀）
    token = auth_header.removeprefix("Bearer ").strip()
    
    # 获取用于验证签名的公钥
    if DEV_JWKS_PATH:
        # 开发模式：从本地 JSON 文件加载自签名公钥
        import json
        with open(DEV_JWKS_PATH) as f:
            key = jwt.PyJWK(json.load(f)["keys"][0]).key
    else:
        # 生产模式：从 Microsoft Entra ID 获取 JWKS
        key = _jwks.get_signing_key_from_jwt(token).key
    
    # 验证令牌并解码
    try:
        # RS256 算法验证签名
        # audience: 验证令牌预期受众（应用 ID）
        # issuer: 验证令牌签发者（Entra ID）
        return jwt.decode(token, key, algorithms=["RS256"], audience=AUDIENCE, issuer=ISSUER)
    except jwt.InvalidTokenError as e:
        raise HTTPException(401, f"Invalid token: {e}")


# ─── HTTP 端点 ───────────────────────────────────────────────────────
# 创建 FastAPI 应用实例
app = FastAPI()

# 配置 CORS 中间件，允许来自 Claude AI pivot 站点的跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://pivot.claude.ai"],  # 允许的来源域
    allow_methods=["GET"],                       # 允许的 HTTP 方法
    allow_headers=["*"],                          # 允许所有请求头（FastAPI 会反映预检请求的头）
)


@app.get("/bootstrap")
def bootstrap(
    authorization: str = Header(None),           # Authorization 请求头
    x_claude_user_agent: str = Header(None),   # 自定义请求头，标识 Office 应用
):
    """
    Bootstrap 端点：Office 加载项在启动时调用此端点获取用户配置

    工作流程:
    1. 从 Authorization 头验证用户 JWT 令牌
    2. 从令牌中提取用户 ID (oid) 和所属组 (groups)
    3. 根据用户组和应用类型解析可用的技能和 MCP 服务器
    4. 返回配置信息，包含 bootstrap_expires_at 指示何时需要刷新

    返回:
        包含 skills、mcp_servers 和 bootstrap_expires_at 的 JSON 响应
    """
    # 验证并解码 JWT 令牌，获取用户声明
    claims = validate(authorization)
    oid = claims.get("oid", "")
    
    # 注意：假设组成员关系在令牌的 `groups` 声明中传递
    # 如果你的租户不发送此声明（或你更喜欢自己的 RBAC），
    # 可以将此行替换为从你的 IdP / HRIS 查询，例如：
    #   groups = fetch_groups_from_graph(oid) 或 your_iam.groups_for(email)
    groups = set(claims.get("groups", []))
    
    # 根据用户身份、组和应用解析配置
    config = resolve(oid, groups, parse_app(x_claude_user_agent))
    
    # 返回配置，包含过期时间戳（1小时后过期）
    return {**config, "bootstrap_expires_at": int(time.time()) + 3600}


if __name__ == "__main__":
    import uvicorn
    # 启动 FastAPI 服务器
    uvicorn.run(app, host=HOST, port=PORT)
