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

def getGalleryListBYyear(type):
    
    list_all = ""
    content = readDB(dbpath, type, "Galleryinfo")
    total_num = str(len(content))

    content_years = {}
    content_years["其他"] = []
    for item in content:
        received_date = item['receivedDate']
        if received_date is None:
            content_years["其他"].append(item)
        else:
            received_year = received_date.split('/')[0]
            if received_year not in content_years:
                content_years[received_year] = []
            content_years[received_year].append(item)
    for year in content_years:
        content_years[year] = sorted(content_years[year], key=lambda x: x['receivedDate'], reverse=True)

    total_num = str(len(content_years))
    return content_years,total_num
    # 其他代码


def createMD(type):
    content_all = ""
    year_all = ""
    
    content_years,total_num = getGalleryListBYyear(type)
    with open(f"./output/title.json", "r",encoding="utf-8") as file:
        data = json.load(file)
    value = data.get(type)
    from_or_to, pageNum, Num, title = value
    # content = readDB(dbpath, type,"Galleryinfo")
    # print(content)
    MDcontent_all =""
    for year in content_years:
        content = content_years.get(year)
        list_all = ""
        year_num = str(len(content))
        for id in content:
            baseUrl = "https://www.postcrossing.com/"
            postcardID = id["id"]  
            travel_days = id["travel_days"] 
            sentAddr = id["sentAddr"] 
            sentCountry = id["sentCountry"]
            receivedAddr = id["receivedAddr"] 
            receivedCountry = id["receivedCountry"] 
            picFileName = id["picFileName"]
            distanceNum = id["distance"]
            sentDate_local = id["sentDate_local"]
            receivedDate_local= id["receivedDate_local"]
            
            FromCoor= json.loads(id["FromCoor"]) if id["FromCoor"] else ""
            ToCoor= json.loads(id["ToCoor"]) if id["ToCoor"] else ""

            travel_time_local = f'> 📤 [{sentCountry}](https://www.bing.com/maps/?cp={FromCoor[0]}~{FromCoor[1]}&lvl=12.0&setlang=zh-Hans) {sentDate_local} (当地)\n' \
                                f'> 📥 [{receivedCountry}](https://www.bing.com/maps/?cp={ToCoor[0]}~{ToCoor[1]}&lvl=12.0&setlang=zh-Hans) {receivedDate_local} (当地)\n' if id["FromCoor"] else ""
            userInfo = f'{from_or_to} {id["userInfo"]}' if id["userInfo"] is not None else ""
            #userInfo}]({baseUrl}/user/{userInfo}
            countryNameEmoji = id["countryNameEmoji"] if id["countryNameEmoji"] else ""
            
            if distanceNum is None:
                travel_info = ">"
            else:
                distance = format(distanceNum, ",")
                travel_info = f"{travel_time_local} 📏 {distance} | ⏱ {travel_days}"
            
            pattern=f"[{postcardID}]({baseUrl}postcards/{postcardID}) \n >{userInfo} {countryNameEmoji}\n{travel_info}\n"
            if type == "popular":
                num = id["favoritesNum"]
                picurl = f"{pattern}>点赞人数：**{num}**\n\n![]({picDriverPath}/{picFileName}) \n\n "
            else:
                countryNameEmoji = id["countryNameEmoji"]
                userInfo = id["userInfo"]
                picurl = f"{pattern}\n\n![]({picDriverPath}/{picFileName})\n\n"
            list_all += picurl
            year_all = f"### {year}({year_num})\n\n{list_all}"
        MDcontent_all += year_all
        #print(f"{account}'{type}展示墙数量:{Num}\n{account}'{type}展示墙页数:{pageNum}\n")
    

    filename_md = f"gallery/{type}.md"
    
    if type in types:
        num = types.index(type) + 2
    link = f"## [{account}'s {type}]({baseUrl}user/{account}/gallery/{type})"
    if os.path.exists(f"{dbpath}BAK"):
        dbStat = compareMD5(dbpath, f"{dbpath}BAK")
        if dbStat == "1":
            print(f"{dbpath} 有更新") 
            replaceTemplate(type,date,num,title,MDcontent_all,repo)
            print(f"\n{type}.md已成功更新")
        else:
            print(f"{dbpath} 暂无更新") 
            print(f"\n{type}.md无更新")
            print("————————————————————")
    
    # replaceTemplate(type,date,num,title,MDcontent_all,repo)

def replaceTemplate(type,date,num,title,MDcontent_all,repo): 
    baseUrl = "https://www.postcrossing.com/"
    link = f"## [{account}'s {type}]({baseUrl}user/{account}/gallery/{type})"
    filename_md = f"gallery/{type}.md"
    if type == "sent" or type == "received":
        with open(f"./template/type_template.md", "r",encoding="utf-8") as f:
            data = f.read()  
            dataNew = data.replace('$type',type)
            print(f"已替换type:{type}")  
            dataNew = dataNew.replace('$date',date)
            print("已替换明信片墙date")      
            dataNew = dataNew.replace('$num',str(num))
            print("已替换明信片墙order")
            dataNew = dataNew.replace('$title',title)
            print("已替换明信片墙title")
            dataNew = dataNew.replace('$content',MDcontent_all)
            print("已替换明信片内容")
            dataNew = dataNew.replace('$repo',repo)
            print("已替换明信片内容")
    else:
        
        dataNew = f'---\ntitle: {title}\nicon: address-card\ndate: {date}\ncategory:\n  - {nickName}\ntag:\n  - postcrossing\norder: {num}\n---\n\n{link}\n\n{MDcontent_all}'
        dataNew = dataNew.replace('$repo',repo)
    # 换为你的blog的本地链接，可自动同步过去
    blog_path = rf"D:\web\Blog\src\Arthur\Postcrossing\{type}.md"
    if os.path.exists(blog_path):  
        with open(blog_path, "w",encoding="utf-8") as f:
            f.write(dataNew) 
    with open(filename_md, "w", encoding="utf-8") as f:    
                f.write(dataNew)

for type in types:
    createMD(type) 

os.remove(f"{dbpath}BAK")
end_time = time.time()
execution_time = round((end_time - start_time),3)
print(f"createGallery.py脚本执行时间：{execution_time}秒\n")
