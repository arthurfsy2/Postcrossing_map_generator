import requests
from bs4 import BeautifulSoup
import math
import re
from datetime import datetime
import json
import time
import os
import sys
import subprocess



start_time = time.time()

with open("config.json", "r") as file:
    data = json.load(file)
account = data["account"]
nickName = data["nickName"]
Cookie = data["Cookie"]
picDriverPath = data["picDriverPath"]

# 获取当前日期
current_date = datetime.now().date()

# 将日期格式化为指定格式
date = current_date.strftime("%Y-%m-%d")

userUrl = f"https://www.postcrossing.com/user/{account}"  
galleryUrl = f"{userUrl}/gallery"  # 设置该账号的展示墙
dataUrl = f"{userUrl}/data/sent"  

headers = {
    'authority': 'www.postcrossing.com',
    'Cookie': Cookie,
    }


#获取账号状态
def getAccountStat():
    galleryResponse = requests.get(galleryUrl,headers=headers)
    galleryStatus = galleryResponse.status_code
    galleryContent = galleryResponse.text.replace('"//', '"https://')

    dataResponse = requests.get(dataUrl,headers=headers)
    dataContent = dataResponse.text
    if "Log in to see this content" in dataContent:
        cookieStat = 404
    else:
        cookieStat = 200
    if galleryStatus == 200 and cookieStat == 200:
        totalStat ="getPrivate"
        types = ['sent', 'received', 'favourites', 'popular']
        print(f"{account}的Cookies有效，可访问个人账号内容\n")
    elif galleryStatus == 200 and cookieStat == 404:
        totalStat ="getPublic"
        types = ['sent', 'received'] 
        print(f"{account}的Cookies无效，只能访问gallery内容")
    elif galleryStatus != 200:
        totalStat ="unAccessible"
        print(f"用户:{account}已注销/设置为非公开，无法获取！\n")
        sys.exit()

    return totalStat,galleryContent,types


stat,content_raw,types = getAccountStat()

#获取account的types对应的数量
def get_message_counts(content):
    # 定义正则表达式模式
    counts = ()
    for type in types:
        if type =="favourites":
            pattern = r"Favorites \((\d+)\)"
        else:
            pattern = r"{} \((\d+)\)"
        # 获取数量
        content_pattern = pattern.format(type.capitalize())
        content_match = re.search(content_pattern, content)
        count = int(content_match.group(1)) if content_match else 0
        # 获取页数
        page_num = math.ceil(count / 60)
        counts += (count, page_num)

    return counts
counts = get_message_counts(content_raw)
print(f"计数：{counts}")


def createMD(type, counts):
    print(f"\n{account}展示墙链接：{galleryUrl}/{type}")      
    sentNum, sentPageNum, receivedNum, receivedPageNum = counts[:4]
    if stat == "getPrivate":
        favouritesNum, favouritesPageNum, popularNum, popularPageNum = counts[4:8]
    else:
        favouritesNum = favouritesPageNum = popularNum = popularPageNum = 0
     
    data = {
    "received": ("来自", receivedPageNum, receivedNum, f"明信片展示墙（收到：{receivedNum}）"),
    "sent": ("寄往", sentPageNum, sentNum, f"明信片展示墙（寄出：{sentNum}）"),
    "favourites": ("来自", favouritesPageNum, favouritesNum, f"明信片展示墙（我的点赞：{favouritesNum}）"),
    "popular": ("", popularPageNum, popularNum, f"明信片展示墙（我收到的赞：{popularNum}）")
            }
    value = data.get(type)
    from_or_to, pageNum, Num, title = value
    #print(f"{account}'{type}展示墙数量:{Num}\n{account}'{type}展示墙页数:{pageNum}\n")
    MDcontent_all = getMDcontent(pageNum ,from_or_to)
    filename_md = f"gallery/{type}.md"
    with open(filename_md, "w", encoding="utf-8") as file:
            content = f'---\ntitle: {title}\nicon: address-card\ndate: {date}\ncategory:\n  - {nickName}\ntag:\n  - postcrossing\n---\n\n{MDcontent_all}'
            file.write(content)
            print(f"{type}_展示墙数据转换为md格式成功：{filename_md}\n")

def getCountryName(flag):
    # 读取contryName.json文件
    with open('contryName.json') as file:
        data = json.load(file)
    # 获取flag对应的值
    value = data.get(flag)
    return value

def getMDcontent(pageNum ,from_or_to):
    i = 1
    MDcontent_all = ""
    while i <= pageNum:
        all_url = f"{galleryUrl}/{type}/{i}"
        print(f"正在获取/{account}/gallery/{type}/{i}的数据")
        response = requests.get(all_url,headers=headers)
        
        content_i = response.text.replace('"//', '"https://')
        soup = BeautifulSoup(content_i, "html.parser")
        lis = soup.find_all("li")
        picurl_page = ""
        
        # 获取每个postcard信息
        for li in lis:
            figure = li.find("figure")
            figcaption = li.find("figcaption")
            if figure:
                href = figure.find("a")["href"]
                #print(f"href:{href}")
                postcardID = figcaption.find("a").text                   
                baseUrl = "https://www.postcrossing.com/"
                picFileName = re.search(r"/([^/]+)$", href).group(1)
                if type == "popular":
                    favoritesNum = figcaption.find("div").text
                    num = re.search(r'\d+', favoritesNum).group()
                    picurl = f"## [{postcardID}]({baseUrl}postcards/{postcardID})\n>点赞人数：{num}\n\n![]({href}) \n "
                elif type == "favourites":                 
                    picDownloadPath = f"gallery/picture/{picFileName}"  # 替换为你要保存的文件路径和文件名
                    if os.path.exists(picDownloadPath):
                        #print(f"已存在{picDownloadPath}")
                        pass
                    else:
                        picDownloadUrl = f"https://s3.amazonaws.com/static2.postcrossing.com/postcard/medium/{picFileName}"
                        #print(f"picDownloadurl:{picDownloadurl}")
                        response = requests.get(picDownloadUrl)
                        print(f"正在下载{picFileName}")
                        with open(picDownloadPath, "wb") as file:
                            file.write(response.content)
                    user = figcaption.find("div").find("a").text
                    userInfo = f"[{user}]({baseUrl}user/{user})"
                    if not user:
                        userInfo = "***该用户已关闭***"
                    flag = re.search(r'href="/country/(.*?)"', str(figcaption)).group(1)
                    contryName = getCountryName(flag)
                    picurl = f"## [{postcardID}]({baseUrl}postcards/{postcardID}) \n >{from_or_to} {userInfo} {contryName}\n\n![]({picDriverPath}/{picFileName})\n\n"
                else:
                    user = figcaption.find("div").find("a").text
                    userInfo = f"[{user}]({baseUrl}user/{user})"
                    if not user:
                        userInfo = "***该用户已关闭***"
                    flag = re.search(r'href="/country/(.*?)"', str(figcaption)).group(1)
                    contryName = getCountryName(flag)
                    picurl = f"## [{postcardID}]({baseUrl}postcards/{postcardID}) \n >{from_or_to} {userInfo} {contryName}\n\n![]({picDriverPath}/{picFileName})\n\n"
                picurl_page += picurl                
        MDcontent_all += picurl_page
        i += 1
        return MDcontent_all

for type in types:
    createMD(type, counts) 

end_time = time.time()
execution_time = round((end_time - start_time),3)
print(f"postcrossing.py脚本执行时间：{execution_time}秒\n")

command = "py createMap.py"
subprocess.run(command, shell=True)

# print("请按下任意键退出")
# input()