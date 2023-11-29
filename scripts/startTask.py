import subprocess
import argparse
import login
import multiDownload as dl
import json

with open("scripts/config.json", "r") as file:
    data = json.load(file)
# account = data["account"]
Cookie = data["Cookie"]
dbpath = data["dbpath"]

#tasks = ['login']
tasks = ['login','createMap', 'createGallery', 'createPersonalPage','getTravelingStats']

# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser()
parser.add_argument("account", help="输入account")
parser.add_argument("password", help="输入password")      
parser.add_argument("nickName", help="输入nickName")    
# parser.add_argument("Cookie", help="输入Cookie") 
parser.add_argument("repo", help="输入repo")    
options = parser.parse_args()

account = options.account
password = options.password
nickName = options.nickName
# Cookie = options.Cookie
repo = options.repo

stat,content_raw,types = dl.getAccountStat(Cookie) 
if stat != "getPrivate": 
    Cookie = login.login(account,password)


for task in tasks:
    command = f'python scripts/{task}.py "{account}" "{password}" "{nickName}" "{repo}"'
    subprocess.run(command, shell=True)


    