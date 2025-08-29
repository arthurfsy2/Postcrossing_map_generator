import re
import argparse
from common_tools import db_path
from multi_download import get_account_stat
import toml
import requests

config = toml.load("scripts/config.toml")
Cookie = config.get("settings").get("Cookie")


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
    # print("csrf_token_value:", csrf_token_value)
    if not csrf_token_value:

        print("未找到 CSRF 令牌！")
        return None

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }

    # 表单数据，包括 CSRF 令牌
    payload = {
        "signin[username]": account,
        "signin[password]": password,
        "signin[_login_csrf_token]": csrf_token_value,  # 这里包含 CSRF 令牌
        "signin[remember]": "on",
    }

    # 提交表单
    response = session.post(login_url, data=payload, headers=headers)

    # 检查登录是否成功
    if response.ok:
        cookies = session.cookies.get_dict()
        Cookie = f"__Host-postcrossing={cookies.get('__Host-postcrossing', '')}; PostcrossingRemember={cookies.get('PostcrossingRemember', '')}"

        print("Cookie_new:", Cookie)

        # 读取config.toml文件内容
        config = toml.load("scripts/config.toml")

        # 更新Cookie变量的值
        config["settings"]["Cookie"] = Cookie

        # 将更新后的内容写入config.toml文件
        with open("scripts/config.toml", "w", encoding="utf-8") as f:
            toml.dump(config, f)

        return Cookie
    else:
        print("账号/密码错误，已退出")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("account", help="输入account")
    parser.add_argument("password", help="输入password")
    # parser.add_argument("nick_name", help="输入nickName")
    # parser.add_argument("Cookie", help="输入Cookie")
    # parser.add_argument("repo", help="输入repo")
    options = parser.parse_args()

    account = options.account
    password = options.password
    # nick_name = options.nick_name
    # Cookie = options.Cookie
    # repo = options.repo

    stat, content_raw, types = get_account_stat(account, Cookie)
    if stat != "get_private":
        login(account, password)
