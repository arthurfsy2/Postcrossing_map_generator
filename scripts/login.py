import re
import argparse
import os
from common_tools import db_path
from multi_download import get_account_stat
import toml
import requests

BIN = os.path.dirname(os.path.realpath(__file__))


def load_cookie_from_cache():
    """从缓存文件读取 Cookie"""
    cookie_file = os.path.join(BIN, ".cookie_cache")
    if os.path.exists(cookie_file):
        with open(cookie_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return None


def save_cookie_to_cache(cookie):
    """保存 Cookie 到缓存文件"""
    cookie_file = os.path.join(BIN, ".cookie_cache")
    with open(cookie_file, "w", encoding="utf-8") as f:
        f.write(cookie)
    return cookie_file


config = toml.load("scripts/config.toml")
# 优先从环境变量读取 Cookie，其次从缓存文件，最后从配置文件
Cookie = (
    os.environ.get("POSTCROSSING_COOKIE", "") or
    load_cookie_from_cache() or
    config.get("settings").get("Cookie", "")
)


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

        # 保存 Cookie 到缓存文件
        cookie_file = save_cookie_to_cache(Cookie)
        print(f"📁 Cookie 已保存到：{cookie_file}")

        # 注释掉导出 Cookie 到 config.toml 的逻辑（避免敏感信息泄露）
        # config = toml.load("scripts/config.toml")
        # config["settings"]["Cookie"] = Cookie
        # with open("scripts/config.toml", "w", encoding="utf-8") as f:
        #     toml.dump(config, f)
        # print(f"📝 Cookie 已更新到 config.toml（请勿提交到 Git！）")

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

    stat, content_raw, types = get_account_stat(account, Cookie)
    if stat != "get_private":
        login(account, password)
