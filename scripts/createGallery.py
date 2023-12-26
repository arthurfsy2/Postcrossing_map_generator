from datetime import datetime
import json
import time
from multiDownload import PicDataCheck
from common_tools import readDB,writeDB,compareMD5
import os
import shutil
import argparse

start_time = time.time()

with open("scripts/config.json", "r") as file:
    data = json.load(file)
# account = data["account"]
# nickName = data["nickName"]
Cookie = data["Cookie"]
picDriverPath = data["picDriverPath"]
dbpath = data["dbpath"]

# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser()
parser.add_argument("account", help="输入account")
#parser.add_argument("password", help="输入password")      
parser.add_argument("nickName", help="输入nickName")    
# parser.add_argument("Cookie", help="输入Cookie") 
parser.add_argument("repo", help="输入repo")    
options = parser.parse_args()

account = options.account
#password = options.password
nickName = options.nickName
# Cookie = options.Cookie
repo = options.repo

if os.path.exists(dbpath):
    shutil.copyfile(dbpath, f"{dbpath}BAK")

# 获取当前日期
current_date = datetime.now().date()

# 将日期格式化为指定格式
date = current_date.strftime("%Y-%m-%d")

types = ['sent', 'received', 'favourites', 'popular']

def createMD(type):
    with open(f"./output/title.json", "r",encoding="utf-8") as file:
        data = json.load(file)
    value = data.get(type)
    from_or_to, pageNum, Num, title = value
    content = readDB(dbpath, type,"Galleryinfo")
    MDcontent_all =""
    for id in content:
        baseUrl = "https://www.postcrossing.com/"
        postcardID = id["id"]  
        picFileName = id["picFileName"]
        distanceNum = id["distance"]
        travel_time = id["travel_time"]
        userInfo = id["userInfo"]
        countryNameEmoji = id["countryNameEmoji"] if id["countryNameEmoji"] is not None else ""
        
        if distanceNum is None and travel_time is None:
            travel_info = ""
        else:
            distance = format(distanceNum, ",")
            travel_info = f"> 📏{distance} km \n⏱{travel_time}"
        
        pattern=f"## [{postcardID}]({baseUrl}postcards/{postcardID}) \n >{from_or_to} [{userInfo}]({baseUrl}/user/{userInfo}) {countryNameEmoji}\n{travel_info}\n"
        if type == "popular":
            num = id["favoritesNum"]
            picurl = f"{pattern}>点赞人数：**{num}**\n\n![]({picDriverPath}/{picFileName}) \n "
        else:
            countryNameEmoji = id["countryNameEmoji"]
            userInfo = id["userInfo"]
            picurl = f"{pattern}\n\n![]({picDriverPath}/{picFileName})\n\n"
        MDcontent_all += picurl
    #print(f"{account}'{type}展示墙数量:{Num}\n{account}'{type}展示墙页数:{pageNum}\n")
    

    filename_md = f"gallery/{type}.md"
    
    if type in types:
        num = types.index(type) + 2
    link = f"### [{account}'s {type}]({baseUrl}user/{account}/gallery/{type})"
    content = f'---\ntitle: {title}\nicon: address-card\ndate: {date}\ncategory:\n  - {nickName}\ntag:\n  - postcrossing\norder: {num}\n---\n\n{link}\n\n{MDcontent_all}'
    content = content.replace('$repo',repo)
    if os.path.exists(f"{dbpath}BAK"):
        dbStat = compareMD5(dbpath, f"{dbpath}BAK")
        if dbStat == "1":
            print(f"{dbpath} 有更新") 
            with open(filename_md, "w", encoding="utf-8") as f:    
                f.write(content)
            print(f"\n{type}.md已成功更新")
            #os.remove(f"{dbpath}BAK")
        else:
            print(f"{dbpath} 暂无更新") 
            print(f"\n{type}.md无更新")
            #os.remove(f"{dbpath}BAK")        

    # 换为你的blog的本地链接，可自动同步过去
    blog_path = rf"D:\web\Blog\src\Arthur\Postcrossing\{type}.md"
    if os.path.exists(blog_path):  
        with open(blog_path, "w",encoding="utf-8") as f:
            f.write(content) 
    

PicDataCheck(account,Cookie)
for type in types:
    createMD(type) 

os.remove(f"{dbpath}BAK")
end_time = time.time()
execution_time = round((end_time - start_time),3)
print(f"createGallery.py脚本执行时间：{execution_time}秒\n")
