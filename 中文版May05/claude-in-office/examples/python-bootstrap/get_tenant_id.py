#!/usr/bin/env python3
"""
打印你的 Entra (Azure AD) 租户 ID

使用方法:
    python get_tenant_id.py alice@yourcompany.com    # 从邮箱域名获取
    python get_tenant_id.py yourcompany.com         # 从域名获取
    python get_tenant_id.py                        # 尝试使用 Azure CLI（如果已登录）

将结果设置为运行 app.py 前的 TENANT_ID 环境变量
"""
import json
import subprocess
import sys
import urllib.request


def from_domain(domain: str) -> str:
    """
    从域名获取 Entra 租户 ID

    Entra 在此众所周知的 URL 发布每个租户的 OIDC 元数据。
    `issuer` 字段格式为 https://login.microsoftonline.com/<tenant_id>/v2.0

    参数:
        domain: 域名（如 yourcompany.com）

    返回:
        租户 ID（GUID 格式）
    """
    # Entra 的 OpenID 配置端点
    url = f"https://login.microsoftonline.com/{domain}/v2.0/.well-known/openid-configuration"
    
    # 请求配置并解析 issuer 字段
    with urllib.request.urlopen(url, timeout=5) as r:
        issuer = json.load(r)["issuer"]
    
    # 从 issuer URL 中提取租户 ID（倒数第二段）
    return issuer.rstrip("/").split("/")[-2]


def from_az_cli() -> str:
    """
    从 Azure CLI 获取当前登录的租户 ID

    返回:
        租户 ID（GUID 格式）

    抛出:
        subprocess.CalledProcessError: 如果 Azure CLI 未登录
    """
    # 使用 Azure CLI 获取当前账户的租户 ID
    out = subprocess.run(
        ["az", "account", "show", "--query", "tenantId", "-o", "tsv"],
        capture_output=True, text=True, check=True,
    )
    return out.stdout.strip()


if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        # 如果参数包含 @，提取域名部分；否则直接作为域名
        domain = arg.split("@", 1)[1] if "@" in arg else arg
        print(from_domain(domain))
    else:
        # 无参数时尝试从 Azure CLI 获取
        try:
            print(from_az_cli())
        except Exception as e:
            # 如果 Azure CLI 未登录，提示用户
            sys.exit(f"Pass an email/domain, or run `az login` first ({e})")
