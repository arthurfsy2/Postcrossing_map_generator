import requests
from bs4 import BeautifulSoup
import math
import re
from datetime import datetime
import json
import time
import os
import sys


start_time = time.time()

with open("config.json", "r") as file:
    data = json.load(file)
account = data["account"]
nickName = data["nickName"]
Cookie = data["Cookie"]
isPrivate = data["isPrivate"]
picDriverPath = data["picDriverPath"]

# 获取当前日期
current_date = datetime.now().date()

# 将日期格式化为指定格式
date = current_date.strftime("%Y-%m-%d")

url = f"https://www.postcrossing.com/user/{account}/gallery"  # 设置该账号的展示墙

if isPrivate =="Y":
    types = ['sent', 'received', 'favourites', 'popular']  # 设置个人账号的取值类别
else:
    types = ['sent', 'received']

headers = {
    'authority': 'www.postcrossing.com',
    'Cookie': Cookie,
    }


#获取账号状态
def getAccountStat():
    response = requests.get(url,headers=headers)
    response_status = response.status_code
    content = response.text.replace('"//', '"https://')
    return response_status,content


stat,content_raw = getAccountStat()

#获取account的sent, received, favourites, popular对应的数量
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


def getPostCardPic(type,response_status, counts):
    print(f"\n{account}展示墙链接：{url}")      
    sentNum = counts[0]
    sentPageNum = counts[1]
    receivedNum = counts[2]
    receivedPageNum = counts[3]
    if isPrivate =="Y":
        response = requests.get(url,headers=headers)
        favouritesNum = counts[4]
        favouritesPageNum = counts[5]
        popularNum = counts[6]
        popularPageNum = counts[7]
    else:
        response = requests.get(url)
        favouritesNum = 0
        favouritesPageNum = 0
        popularNum = 0
        popularPageNum = 0

    response_status = response.status_code
    
    
    
    content = response.text.replace('"//', '"https://"')
    #filename = f"./output/{account}_{type}({i}).html"
    """ with open(filename, "w", encoding="utf-8") as file:
                content_i = response.text.replace('"//', '"https://')
                file.write(content_i)
                print(f"\n{type}({i})数据保存成功：{filename}") """
    
    data = {
    "received": ("来自", receivedPageNum, receivedNum, f"明信片展示墙（收到：{receivedNum}）"),
    "sent": ("寄往", sentPageNum, sentNum, f"明信片展示墙（寄出：{sentNum}）"),
    "favourites": ("来自", favouritesPageNum, favouritesNum, f"明信片展示墙（我的点赞：{favouritesNum}）"),
    "popular": ("", popularPageNum, popularNum, f"明信片展示墙（我收到的赞：{popularNum}）")
            }
    value = data.get(type)
    if value:
        # 获取元组中的变量
        from_or_to, pageNum, Num, title = value
    print(f"{account}'{type}展示墙数量:{Num}\n{account}'{type}展示墙页数:{pageNum}\n")
    galleryInfo(response_status, pageNum ,from_or_to, title)

def galleryInfo(response_status, pageNum ,from_or_to, title):
    i = 1
    picurl_all = ""
    while i <= pageNum:
        if response_status == 200:
            all_url = f"{url}/{type}/{i}"
            print(f"正在获取/{account}/gallery/{type}/{i}的数据")
            response = requests.get(all_url,headers=headers)
            filename_md = f"gallery/{type}.md"
            # filename = f"./output/{type}({i}).html"
            # with open(filename, "w", encoding="utf-8") as file:
            #     content_i = response.text.replace('"//', '"https://')
            #     file.write(content_i)
                #print(f"\n{type}({i})数据保存成功：{filename}") 
            content_i = response.text.replace('"//', '"https://')
            soup = BeautifulSoup(content_i, "html.parser")
            lis = soup.find_all("li")
            picurl_page = ""
            
            for li in lis:
                figure = li.find("figure")
                figcaption = li.find("figcaption")
                if figure:
                    href = figure.find("a")["href"]
                    #print(f"href:{href}")
                    postcardID = figcaption.find("a").text
                    picFileName = re.search(r"/([^/]+)$", href).group(1)
                    #print(f"picFileName:{picFileName}")                   
                    picDownloadPath = f"gallery/picture/{picFileName}"  # 替换为你要保存的文件路径和文件名
                    if os.path.exists(picDownloadPath):
                        #print(f"已存在{picDownloadPath}")
                        pass
                    else:
                        picDownloadurl = f"https://s3.amazonaws.com/static2.postcrossing.com/postcard/medium/{picFileName}"
                        print(f"picDownloadurl:{picDownloadurl}")
                        response = requests.get(picDownloadurl)
                        print(f"正在下载{picDownloadPath}的图片")
                        with open(picDownloadPath, "wb") as file:
                            file.write(response.content)
                    baseUrl = "https://www.postcrossing.com/"
                    if type == "popular":
                        favoritesNum = figcaption.find("div").text
                        num = re.search(r'\d+', favoritesNum).group()
                        picurl = f"## [{postcardID}]({baseUrl}postcards/{postcardID})\n>点赞人数：{num}\n\n![]({href}) \n "
                    else:
                        user = figcaption.find("div").find("a").text
                        userInfo = f"[{user}]({baseUrl}user/{user})"
                        if not user:
                            userInfo = "***该用户已关闭***"
                        picurl = f"## [{postcardID}]({baseUrl}postcards/{postcardID}) \n >{from_or_to} {userInfo}\n\n![]({picDriverPath}/{picFileName})\n\n"
                    picurl_page += picurl                
            picurl_all += picurl_page
            
            
            with open(filename_md, "w", encoding="utf-8") as file:
                
                content = f'---\ntitle: {title}\nicon: address-card\ndate: {date}\ncategory:\n  - {nickName}\ntag:\n  - postcrossing\n---\n\n{picurl_all}'
                file.write(content)
                print(f"{type}_展示墙数据转换为md格式成功：{filename_md}\n")
            i += 1

        else:
            print(f"用户:{account}已注销/设置为非公开，无法获取！\n")
            return None


if stat == 200:
    print(f"用户:{account}的数据为公开，可获取！\n")
    for type in types:
        getPostCardPic(type, stat, counts) 
        
else:
    print(f"用户:{account}已注销/设置为非公开，无法获取！\n")
    sys.exit()

end_time = time.time()
execution_time = round((end_time - start_time),3)
print(f"脚本执行时间：{execution_time}秒")