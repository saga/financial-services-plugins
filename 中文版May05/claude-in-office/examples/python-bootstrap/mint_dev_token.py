"""
生成用于本地测试 app.py 的自签名开发令牌

首次运行会在当前目录生成 dev_private.pem + dev_jwks.json。
后续运行会重用这些文件。

使用方法:
    python mint_dev_token.py --oid alice --group <gid> --group <gid2>

参数说明:
    --oid: 用户的对象 ID（Object ID），默认为 "alice"
    --group: 用户所属的安全组 ID（可多次使用）
"""
import argparse
import json
import os
import time
import base64
import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# 文件名常量
PRIV = "dev_private.pem"     # 私钥文件
JWKS = "dev_jwks.json"     # JWKS（JSON Web Key Set）文件

# Claude in Office 加载项的应用 ID（固定值）
AUDIENCE = "c2995f31-11e7-4882-b7a7-ef9def0a0266"

# 租户 ID（从环境变量读取，默认为 "dev-tenant"）
TENANT_ID = os.getenv("TENANT_ID", "dev-tenant")

# 令牌签发者 URL（基于租户 ID 构建）
ISSUER = f"https://login.microsoftonline.com/{TENANT_ID}/v2.0"


def b64u(n: int) -> str:
    """
    将整数转换为 Base64 URL 安全编码（用于 JWK）

    参数:
        n: 大整数（RSA 模数或指数）

    返回:
        Base64 URL 安全编码的字符串
    """
    # 将整数转换为字节
    raw = n.to_bytes((n.bit_length() + 7) // 8, "big")
    # Base64 URL 安全编码并去除填充符
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


# ─── 首次运行：生成自签名密钥对和 JWKS ───────────────────────────
if not os.path.exists(PRIV):
    # 生成 2048 位 RSA 私钥
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    
    # 将私钥保存为 PEM 格式
    with open(PRIV, "wb") as f:
        f.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        ))
    
    # 从公钥提取 RSA 参数以创建 JWK
    nums = key.public_key().public_numbers()
    jwk = {
        "kty": "RSA",      # 密钥类型
        "kid": "dev",      # 密钥 ID（开发密钥）
        "alg": "RS256",    # 签名算法
        "use": "sig",      # 密钥用途（签名）
        "n": b64u(nums.n),  # 模数（Base64 URL 编码）
        "e": b64u(nums.e),  # 指数（Base64 URL 编码）
    }
    
    # 将 JWKS 保存为 JSON 文件
    with open(JWKS, "w") as f:
        json.dump({"keys": [jwk]}, f, indent=2)

# ─── 解析命令行参数 ─────────────────────────────────────────────────────
ap = argparse.ArgumentParser(description="生成开发用的自签名 JWT 令牌")
ap.add_argument("--oid", default="alice", help="用户对象 ID")
ap.add_argument("--group", action="append", default=[], help="用户所属的安全组（可多次使用）")
args = ap.parse_args()

# ─── 加载私钥并生成 JWT ─────────────────────────────────────────────
with open(PRIV, "rb") as f:
    # 从 PEM 文件加载私钥
    priv = serialization.load_pem_private_key(f.read(), password=None)

# 构建令牌声明（claims）
claims = {
    "aud": AUDIENCE,           # 受众（应用 ID）
    "iss": ISSUER,            # 签发者（Entra ID URL）
    "oid": args.oid,          # 用户对象 ID
    "groups": args.group,      # 用户所属的安全组列表
    "exp": int(time.time()) + 3600  # 过期时间：1小时后
}

# 使用 RS256 算法签名并编码 JWT
print(jwt.encode(claims, priv, algorithm="RS256", headers={"kid": "dev"}))
