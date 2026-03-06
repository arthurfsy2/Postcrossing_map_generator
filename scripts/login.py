import re
import argparse
import os
from datetime import datetime
from common_tools import db_path
from multi_download import get_account_stat
import toml
import requests

BIN = os.path.dirname(os.path.realpath(__file__))
COOKIE_CONFIG_FILE = os.path.join(BIN, ".cookie_config.toml")


def load_cookie_from_config():
    """从 Cookie 配置文件读取 Cookie"""
    if os.path.exists(COOKIE_CONFIG_FILE):
        try:
            cookie_config = toml.load(COOKIE_CONFIG_FILE)
            return cookie_config.get("auth", {}).get("cookie", "")
        except Exception:
            return ""
    return ""


def save_cookie_to_config(cookie, account):
    """保存 Cookie 到配置文件"""
    cookie_config = {
        "auth": {
            "cookie": cookie,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "account": account
        }
    }
    with open(COOKIE_CONFIG_FILE, "w", encoding="utf-8") as f:
        toml.dump(cookie_config, f)
    return COOKIE_CONFIG_FILE


# 优先从环境变量读取 Cookie，其次从配置文件
Cookie = os.environ.get("POSTCROSSING_COOKIE", "") or load_cookie_from_config()


def login(account, password):
    session = requests.Session()

    # 请求登录页面以获取 CSRF 令牌
    login_url = "https://www.postcrossing.com/login"
    response = session.get(login_url)

    # 提取 CSRF 令牌
    csrf_token = re.search(
        r'name="signin\[_login_csrf_token\]" value="(.*?)"', response.text
    )
    csrf_token_value = csrf_token.group(1) if csrf_token else None
    if not csrf_token_value:
        print("❌ 未找到 CSRF 令牌！")
        return None

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }

    # 表单数据，包括 CSRF 令牌
    payload = {
        "signin[username]": account,
        "signin[password]": password,
        "signin[_login_csrf_token]": csrf_token_value,
        "signin[remember]": "on",
    }

    # 提交表单
    response = session.post(login_url, data=payload, headers=headers)

    # 检查登录是否成功
    if response.ok:
        cookies = session.cookies.get_dict()
        Cookie = f"__Host-postcrossing={cookies.get('__Host-postcrossing', '')}; PostcrossingRemember={cookies.get('PostcrossingRemember', '')}"

        print("✅ Cookie 获取成功")

        # 保存 Cookie 到配置文件
        cookie_file = save_cookie_to_config(Cookie, account)
        print(f"📁 Cookie 已保存到：{cookie_file}")

        return Cookie
    else:
        print("❌ 账号/密码错误，已退出")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("account", help="输入 account")
    parser.add_argument("password", help="输入 password")
    options = parser.parse_args()

    account = options.account
    password = options.password

    # 优先从环境变量读取 Cookie（GitHub Actions 场景）
    env_cookie = os.environ.get("POSTCROSSING_COOKIE", "")
    if env_cookie:
        print("📥 从环境变量读取 Cookie")
        save_cookie_to_config(env_cookie, account)
        Cookie = env_cookie
    else:
        # 从配置文件读取
        Cookie = load_cookie_from_config()
    
    stat, content_raw, types = get_account_stat(account, Cookie)
    if stat != "get_private":
        print("🔄 Cookie 无效或不存在，正在重新登录...")
        Cookie = login(account, password)
    else:
        print("✅ Cookie 有效")
