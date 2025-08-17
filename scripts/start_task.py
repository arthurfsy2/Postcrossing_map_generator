import subprocess
import argparse
import json

with open("scripts/config.json", "r") as file:
    data = json.load(file)
# account = data["account"]
Cookie = data["Cookie"]
dbpath = data["dbpath"]

# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser()
parser.add_argument("account", help="输入account")
parser.add_argument("password", help="输入password")
parser.add_argument("nick_name", help="输入nickName")
# parser.add_argument("Cookie", help="输入Cookie")
parser.add_argument("repo", help="输入repo")
parser.add_argument("apikey", help="输入小牛翻译apikey")
options = parser.parse_args()

account = options.account
password = options.password
nick_name = options.nick_name
# Cookie = options.Cookie
repo = options.repo
apikey = options.apikey


command = f'python scripts/login.py "{account}" "{password}"'
subprocess.run(command, shell=True)

command = f'python scripts/multi_download.py "{account}" "{nick_name}"'
subprocess.run(command, shell=True)

command = f'python scripts/create_gallery.py "{account}" "{nick_name}" "{repo}"'
subprocess.run(command, shell=True)

command = f'python scripts/create_map.py "{account}"'
subprocess.run(command, shell=True)

command = f'python scripts/create_personal_page.py "{account}" "{nick_name}" "{repo}"'
subprocess.run(command, shell=True)

command = f"python scripts/postcrossing_recap.py"
subprocess.run(command, shell=True)
