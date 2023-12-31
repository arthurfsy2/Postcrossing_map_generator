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
parser.add_argument("nickName", help="输入nickName")    
# parser.add_argument("Cookie", help="输入Cookie") 
parser.add_argument("repo", help="输入repo")  
parser.add_argument("apikey", help="输入小牛翻译apikey")     
options = parser.parse_args()

account = options.account
password = options.password
nickName = options.nickName
# Cookie = options.Cookie
repo = options.repo
apikey = options.apikey


command = f'python scripts/login.py "{account}" "{password}"'
subprocess.run(command, shell=True)

command = f'python scripts/multiDownload.py "{account}" "{password}" "{nickName}" "{repo}"'
subprocess.run(command, shell=True)

command = f'python scripts/createGallery.py "{account}" "{nickName}" "{repo}"'
subprocess.run(command, shell=True)

command = f'python scripts/createMap.py "{account}"'
subprocess.run(command, shell=True)    

command = f'python scripts/createPersonalPage.py "{account}" "{nickName}" "{repo}" "{apikey}"'
subprocess.run(command, shell=True)    