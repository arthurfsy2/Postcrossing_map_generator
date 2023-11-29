import json
import re
import requests
from bs4 import BeautifulSoup
import threading
import os
import json
import pandas as pd
import math
from datetime import datetime, timedelta
import sys
import sqlite3
import statistics
import hashlib
import argparse



with open("scripts/config.json", "r") as file:
    data = json.load(file)
# account = data["account"]
# nickName = data["nickName"]
Cookie = data["Cookie"]
picDriverPath = data["picDriverPath"]
dbpath = data["dbpath"]

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

# 获取当前日期
current_date = datetime.now().date()
 
# 将日期格式化为指定格式
date = current_date.strftime("%Y-%m-%d")

url = f"https://www.postcrossing.com/user/{account}/gallery"  # 替换为您要获取数据的链接
userUrl = f"https://www.postcrossing.com/user/{account}"  
galleryUrl = f"{userUrl}/gallery"  # 设置该账号的展示墙
dataUrl = f"{userUrl}/data/sent"  
types_map = ['sent', 'received']  



headers = {
    'authority': 'www.postcrossing.com',
    'Cookie': Cookie,
    
    }

#获取账号状态
def getAccountStat(Cookie):
    headers = {
    'authority': 'www.postcrossing.com',
    'Cookie': Cookie,
    
    }
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
        print(f"{account}的Cookies有效，可访问个人账号内容……\n")
    elif galleryStatus == 200 and cookieStat == 404:
        totalStat ="getPublic"
        types = ['sent', 'received'] 
        print(f"{account}的Cookies无效，正在尝试重新登陆……\n")
    elif galleryStatus != 200:
        totalStat ="unAccessible"
        print(f"用户:{account}已注销/设置为非公开，无法获取！\n")
        sys.exit()

    return totalStat,galleryContent,types


def getPageNum(stat,content,types):
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
    
    print("counts:",counts)
    sentNum, sentPageNum, receivedNum, receivedPageNum = counts[:4]
    if stat == "getPrivate":
        favouritesNum, favouritesPageNum, popularNum, popularPageNum = counts[4:8]
    else:
        favouritesNum = favouritesPageNum = popularNum = popularPageNum = 0
     
    data = {
    "received": ("来自", receivedPageNum, receivedNum, f"明信片展示墙（收到：{receivedNum}）"),
    "sent": ("寄往", sentPageNum, sentNum, f"明信片展示墙（寄出：{sentNum}）"),
    "favourites": ("来自", favouritesPageNum, favouritesNum, f"明信片展示墙（我的点赞：{favouritesNum}）"),
    "popular": ("寄往", popularPageNum, popularNum, f"明信片展示墙（我收到的赞：{popularNum}）")
            }
    path = "./output/title.json"


    with open(path, "w",encoding="utf-8") as file:
            json.dump(data, file, indent=2)

# 获取对应国家的Emoji旗帜简写代码 
def getCountryFlagEmoji(flag):
    with open('scripts/contryNameEmoji.json') as file:
        data = json.load(file)
    # 获取flag对应的值
    value = data.get(flag)
    return value

# 获取不同类型的展示墙的详细信息，并组装数据
def getGalleryInfo(type):
    path = "./output/title.json"
    with open(path, "r",encoding="utf-8") as file:
        data = json.load(file)
    value = data.get(type)
    from_or_to, pageNum, Num, title = value
    i = 1
    content_all=[]
    while i <= pageNum:
        all_url = f"{galleryUrl}/{type}/{i}"
        print(f"正在获取/{account}/gallery/{type}/{i}的数据")
        response = requests.get(all_url,headers=headers)
        
        content_i = response.text.replace('"//', '"https://')
        soup = BeautifulSoup(content_i, "html.parser")
        lis = soup.find_all("li")
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
                    userInfo = ""
                    contryNameEmoji = ""
                else:
                    user = figcaption.find("div").find("a").text
                    userInfo = f"[{user}]({baseUrl}user/{user})"
                    if not user:
                        userInfo = "***该用户已关闭***"
                    flag = re.search(r'href="/country/(.*?)"', str(figcaption)).group(1)
                    contryNameEmoji = getCountryFlagEmoji(flag)
                    num = ""
                item={
                    'id': postcardID,
                    'userInfo': userInfo,
                    'contryNameEmoji': contryNameEmoji,
                    'picFileName': picFileName,
                    'favoritesNum': num,
                    'type': type
                        }
                content_all.append(item)
        # 连接到数据库test.db
        tablename = "Galleryinfo"
        writeDB(dbpath, content_all,tablename)
        i += 1
        print(f"已更新Galleryinfo_{type}：数据库{dbpath}\n")
        print("————————————————————")


# 读取本地数据库的明信片ID
def getLocalID(type,dbpath):
    oldID = None
    if os.path.exists(dbpath):
        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Mapinfo'")
        table_exists = cursor.fetchone()
        if table_exists:
            # 从Mapinfo表中获取id
            cursor.execute("SELECT id FROM Mapinfo WHERE type=?", (type,))
            rows = cursor.fetchall()
            oldID = [row[0] for row in rows]
        conn.close()
    return oldID

# 读取本地已下载图片的文件名列表
def getLocalPic():
    localPicList = []
    picPath = "./gallery/picture"
    for root, dirs,files in os.walk(picPath):
        for file in files:
            localPicList.append(file)
    return localPicList



# 实时获取该账号所有sent、received的明信片列表，获取每个postcardID的详细数据
def getUpdateID(account,type,Cookie):
    headers = {
    'Host': 'www.postcrossing.com',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Sec-Fetch-Mode': 'cors',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0.1 Mobile/15E148 Safari/604.1',
    'Connection': 'keep-alive',
    'Referer': f'https://www.postcrossing.com/user/{account}/{type}',
    'Cookie': Cookie,
    'Sec-Fetch-Dest': 'empty'
        }
    url=f'https://www.postcrossing.com/user/{account}/data/{type}'    
    response = requests.get(url,headers=headers).json()

    onlineID = [item[0] for item in response]
    hasPicID = [item[0] for item in response if item[-1] == 1]
    #print(f"hasPicID({len(hasPicID)}):{hasPicID}")
    if getLocalID(type,dbpath) is not None:
        oldID = getLocalID(type,dbpath)    
        newID = []
        # 遍历onlineID中的元素
        for id in onlineID:
            # 如果id不在oldID中，则将其添加到newID中
            if id not in oldID:
                newID.append(id)
        if len(newID) == 0:
            print(f"数据库{dbpath}：Mapinfo_{type}暂无更新内容\n")
            updateID = None
        else:
            print(f"{type}_等待更新Mapinfo({len(newID)}个):{newID}\n")
            updateID = newID
    else:
        # 当本地文件不存在时，则取online的postcardId作为待下载列表
        updateID = onlineID

    return updateID,hasPicID

# 获取日期
def convert_to_utc(zoneNum,type,time_str):
    # 使用正则表达式提取时间部分
    pattern = rf"{type} on (\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}})"
    #print("pattern:",pattern)
    match = re.search(pattern, time_str)
    if match:
        time_str = match.group(1)
    else:
        return "No match found"
    # 转换为datetime对象
    time_utc = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    # 转换为UTC-8时间
    time_utc = time_utc + timedelta(hours=zoneNum)
    # 格式化为字符串
    time_utc_str = time_utc.strftime(f"%Y/%m/%d")
    return time_utc_str




def get_data(postcardID,type):
    
    content_all=[]
    for i, id in enumerate(postcardID): 
             
        url=f"https://www.postcrossing.com/postcards/{id}"        
        response = requests.get(url)       
        pattern = r"var senderLocation\s+=\s+new L.LatLng\(([-\d.]+), ([-\d.]+)\);\s+var receiverLocation\s+=\s+new L.LatLng\(([-\d.]+), ([-\d.]+)\);"
        matches = re.findall(pattern, response.text)  #提取发送、接收的经纬度坐标

        # 提取距离、发送/到达时间、历经天数
        distance = int(re.search(r'traveled (.*?) km', response.text).group(1).replace(',', ''))
        travel_days = int(re.search(r'in (.*?) days', response.text).group(1))
        sentDate = convert_to_utc(8,"Sent",response.text)
        receivedDate = convert_to_utc(8,"Received",response.text)
        travel_time = f"{travel_days} days [{sentDate}--{receivedDate}]"
        #print(f"{id}_travel_time:{travel_time}")
        # 提取发送者/接受者user
        userPattern = r'<a itemprop="url" href="/user/(.*?)"'
        userResults = re.findall(userPattern, response.text)
        #print(f"{id}_userResults:{userResults}]")

        # 提取链接link
        link = re.search(r'<meta property="og:image" content="(.*?)" />', response.text).group(1)  
        if "logo" in link:
            link = "gallery/picture/noPic.png"  #替换图片为空时的logo
        else:
            picFileName = re.search(r"/([^/]+)$", link).group(1)
            #print(f"{id}_picFileName:{picFileName}")
            link = f"gallery/picture/{picFileName}"


        # 提取地址信息
        addrPattern = r'<a itemprop="addressCountry" title="(.*?)" href="/country/(.*?)">(.*?)</a>'
        addrResults = re.findall(addrPattern, response.text)
        #print(f"{id}_addrResults:", addrResults)

        sentAddrInfo = addrResults[0]
        receivedInfo = addrResults[1]

        sentAddr = sentAddrInfo[0]
        sentCountry = sentAddrInfo[2]
        receivedAddr = receivedInfo[0]
        receivedCountry = receivedInfo[2]

        # 提取发送/接收user
        userPattern = r'<a itemprop="url" href="/user/(.*?)"'
        userResults = re.findall(userPattern, response.text)
        #print(f"{id}_userResults:{userResults}")
        if len(userResults) == 1:
            user = "account closed"
        elif len(userResults) >= 2 and type == "sent":
            user = userResults[1]
            
        elif len(userResults) >= 2 and type == "received":
            user = userResults[0]
        #print(f"User:{user}")        
        
    
        for match in matches:
            
            # 将拼接后的坐标字符串转换为浮点数
            from_coord = (float(match[0]), float(match[1]))
            to_coord = (float(match[2]), float(match[3]))

        tablename = "Mapinfo"
        
        item = {
                "id": id,
                "FromCoor":from_coord,
                "ToCoor":to_coord,
                "distance": distance,
                "travel_time": travel_time,
                "link": link,
                "user": user,
                "sentAddr":f"{sentAddr}({sentCountry})",
                "receivedAddr":f"{receivedAddr}({receivedCountry})",
                "type":type
            }
        content_all.append(item)
        print(f"{type}_List:已提取{round((i+1)/(len(postcardID))*100,2)}%")
    writeDB(dbpath, content_all,tablename)

# 下载展示墙的图片  
def downloadPic(updatePic,pic_json):
    picFileNameList=[]
    for i, picFileName in enumerate(updatePic):         
        picDownloadPath = f"gallery/picture/{picFileName}"  # 替换为你要保存的文件路径和文件名
        if os.path.exists(picDownloadPath):
            #print(f"已存在：{picFileName}") 
            pass
        else:
            picDownloadUrl = f"https://s3.amazonaws.com/static2.postcrossing.com/postcard/medium/{picFileName}"
            #print(f"picDownloadUrl:{picDownloadUrl}")
            response = requests.get(picDownloadUrl)
            print(f"正在下载{picFileName}")
            with open(picDownloadPath, "wb") as file:
                file.write(response.content)
    pic_json.append(picFileName)

def getUpdatePic(type):
    picFileNameList=[]
    content =readDB(dbpath, type,"Galleryinfo")

    # 提取picFileName字段内容
    picFileNameList = [item['picFileName'] for item in content]
    #print("picFileNameList:",picFileNameList)
    if getLocalPic() is not None:
        oldPic = getLocalPic()       
        newPic = []
        # 遍历onlineID中的元素
        for pic in picFileNameList:
            # 如果id不在oldID中，则将其添加到newID中
            if pic not in oldPic:
                newPic.append(pic)
        if len(newPic) == 0:
            updatePic = None
        else:
            
            updatePic = newPic
    else:
        # 当本地文件不存在时，则取online的postcardId作为待下载列表
        updatePic = picFileNameList 

    return updatePic


def calculateAVGandMedian(a_data):
    with open('scripts/contryName.json', 'r') as f:
        countryName = json.load(f)

    # 读取scripts/contryName.json文件
    with open('scripts/contryNameEmoji.json', 'r') as f:
        countryNameEmoji = json.load(f)
    
    name_dict = {}
    
    for item in a_data:
        code = item[3]
        country = countryName[code]
        flagEmoji = countryNameEmoji[code]
        r_or_s = item[2]
        travel_days = item[1]
        
        if code not in name_dict:
            name_dict[code] = {'name': country, 'countryCode': code, 'flagEmoji': flagEmoji, 'sent': [], 'received': []}
        
        if r_or_s == 's':
            name_dict[code]['sent'].append(travel_days)
        elif r_or_s == 'r':
            name_dict[code]['received'].append(travel_days)
    
    country_stats = []
    
    for code, data in name_dict.items():
        sent_median = None
        received_median = None
        
        if data['sent']:
            sent_avg = round(statistics.mean(data['sent']),1)
            sent_median = round(statistics.median(data['sent']),1)
        
        if data['received']:
            received_avg = round(statistics.mean(data['received']),1)
            received_median = round(statistics.median(data['received']),1)
        
        country_stats.append({
            'name': data['name'],
            'countryCode': data['countryCode'],
            'flagEmoji': data['flagEmoji'],
            'value':len(data['sent']) + len(data['received']),
            'sentNum':len(data['sent']),
            'receivedNum':len(data['received']),
            'sentAvg': sent_avg,
            'receivedAvg': received_avg,
            'sentMedian': sent_median,
            'receivedMedian': received_median,
        })
    country_stats.sort(key=lambda x: x['value'], reverse=True)
    return country_stats

# def createCalendar(year, data):
#     # Create Calendar chart object
#     calendar = (
#         Calendar()
#         .set_global_opts(
#             tooltip_opts=opts.TooltipOpts(),
#             visualmap_opts=opts.VisualMapOpts(
#                 is_show=False,
#                 min_=1,
#                 max_=10,
#                 range_color=["#7bc96f", "#239a3b", "#196127", "#196127"],
#             )            
#         )
#         .add(
#             series_name="",
#             yaxis_data=data,
#             calendar_opts=opts.CalendarOpts(
#                 width="600px",
#                 pos_top="10%",
#                 cell_size=["auto", 12],
#                 range_= year,
#                 itemstyle_opts=opts.ItemStyleOpts(
#                     color="#ccc",
#                     border_width=3,
#                     border_color="#fff",
#                 ),
#                 splitline_opts=opts.SplitLineOpts(is_show=False),
#                 yearlabel_opts=opts.CalendarYearLabelOpts(is_show=True),
#                 daylabel_opts=opts.CalendarDayLabelOpts(
#                     first_day=1,
#                     name_map=["","Mon", "", "Wed", "", "Fri", "" ]
#                     ),
#             ),
#         )
#     )



#     # Render the Calendar chart and save it as an SVG file
#     calendar.render(f"./output/calendar/{year}.html")
#     # make_snapshot(snapshot, calendar.render(f"./output/calendar/{year}.html"), f"./output/calendar/{year}.png")






def getUserStat():
    headers = {
    'Host': 'www.postcrossing.com',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Sec-Fetch-Mode': 'cors',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0.1 Mobile/15E148 Safari/604.1',
    'Connection': 'keep-alive',
    'Referer': f'https://www.postcrossing.com/user/{account}/stats',
    'Cookie': Cookie,
    'Sec-Fetch-Dest': 'empty'
        }
    url=f'https://www.postcrossing.com/user/{account}/feed'    
    a_data = requests.get(url,headers=headers).json()
    with open(f"./output/UserStats.json", "w") as file:
        json.dump(a_data, file, indent=2)

    # 统计每个国家代码的出现次数
    country_count = {}
    for item in a_data:
        country_code = item[-1]
        if country_code in country_count:
            country_count[country_code] += 1
        else:
            country_count[country_code] = 1

    # 创建一个字典用于存储汇总结果
    summary = {}

    # 遍历数据
    for item in a_data:
        # 将时间戳转换为YYYY-MM的格式
        timestamp = item[0]
        date = datetime.fromtimestamp(timestamp).strftime('%Y-%m')
        
        # 判断sent还是received
        if item[2] == 's':
            key = 'sent'
        elif item[2] == 'r':
            key = 'received'
        else:
            continue
        
        # 更新汇总结果
        if date in summary:
            summary[date][key] += 1
        else:
            summary[date] = {'sent': 0, 'received': 0}
            summary[date][key] = 1

    # 将汇总结果转换为新的数组
    #result = [{'date': date, 'num': summary[date]} for date in summary]
    result = [{'date': date, 'sent': summary[date]['sent'], 'received': summary[date]['received']} for date in summary]
    
    # 将结果输出到month.json文件中，以供“信息汇总.md"的收发记录（月度）模块使用
    with open(f"./output/month.json", 'w') as f:
        json.dump(result, f, indent=2)

    print(f"已生成output/month.json\n")
    
    calendar = {}
    # 遍历数据列表
    for data in a_data:
        # 将时间戳转换为YYYY-MM-DD格式
        timestamp = data[0]
        date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

        # 统计每天的总数
        if date in calendar:
            calendar[date] += 1
        else:
            calendar[date] = 1

    # 将结果转换为列表格式
    calendar_result = [[date, total] for date, total in calendar.items()]

    # 将结果输出到calendar.json文件
    with open('./output/calendar.json', 'w') as file:
        json.dump(calendar_result, file,indent=2)

    country_stats = calculateAVGandMedian(a_data)
    #print("country_stats:\n",country_stats)
    # # 将统计结果写入 b.json 文件
    with open('./output/stats.json', 'w') as file:
        json.dump(country_stats, file, indent=2)
    print(f"已生成./output/stats.json\n")
    tablename = "CountryStats"
    writeDB(dbpath, country_stats,tablename)
    



def multiTask(account,type,Cookie):
    result = getUpdateID(account,type,Cookie)
    postcardID = result[0]
    if postcardID is not None:
        Num = round(len(postcardID)/20) 
        if Num < 1:
            realNum = 1
        elif Num >= 1 and Num <= 10:
            realNum = Num
        elif Num >10: # 最大并发数为10
            realNum = 10
        group_size = len(postcardID) // realNum
        print(f"将{type}的postcardID分为{realNum}个线程并行处理，每个线程处理个数：{group_size}\n")
        postcard_groups = [postcardID[i:i+group_size] for i in range(0, len(postcardID), group_size)]
        # 创建线程列表
        threads = []

        # 创建并启动线程
        for i,group in enumerate(postcard_groups):
            thread = threading.Thread(target=get_data, args=(group, type))
            thread.start()
            threads.append(thread)
            
        # 等待所有线程完成
        for thread in threads:
            thread.join()
            
        print(f"{type}的update List已提取完成！\n")
    else:
        pass
    
# 设置多线程下载图片
def multiDownload(type):
    updatePic = getUpdatePic(type)
    
    if updatePic is not None:
        Num = round(len(updatePic)/20) 
        if Num < 1:
            realNum = 1
        elif Num >= 1 and Num <= 10:
            realNum = Num
        elif Num >10: # 最大并发数为10
            realNum = 10
        group_size = len(updatePic) // realNum
        print(f"将{type}的postcardID分为{realNum}个线程并行下载，每个线程下载图片个数：{group_size}\n")
        picDownload_groups = [updatePic[i:i+group_size] for i in range(0, len(updatePic), group_size)]
        # 创建线程列表
        threads = []
        pic_json = []  # 存储最终的pic_json
        # 创建并启动线程
        for i,group in enumerate(picDownload_groups):
            thread = threading.Thread(target=downloadPic, args=(group, pic_json))
            thread.start()
            threads.append(thread)
        
        # 等待所有线程完成
        for thread in threads:
            thread.join()
        
    else:
        print(f"{type}_图库无需更新")
        print("————————————————————")

# 设置读取数据库的统一入口函数
def readDB(dbpath, type,tablename):
    data_all = []
    if os.path.exists(dbpath):
        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?",(tablename,))
        table_exists = cursor.fetchone()

        if table_exists:
            if tablename == 'Galleryinfo':
                cursor.execute('''SELECT
                                    g.id,
                                    (SELECT user FROM Mapinfo WHERE id = m.id AND (type = 'sent' or type = 'received')) AS userInfo2,
                                    (SELECT contryNameEmoji FROM Galleryinfo WHERE id = g.id AND (type = 'sent' or type = 'received')) AS contryNameEmoji,
                                    g.picFileName,
                                    g.favoritesNum,
                                    g.type,
                                    m.travel_time,
                                    date(REPLACE(SUBSTR(m.travel_time, 22, 10), '/', '-')) AS receivedDate,
                                    m.distance 
                                FROM
                                    Galleryinfo g
                                    LEFT JOIN Mapinfo m ON g.id = m.id 
                                WHERE
                                    g.type = ?
                                ORDER BY
                                    receivedDate DESC
                ''', (type,))
            elif tablename == 'Mapinfo':
                cursor.execute(f"SELECT * FROM {tablename} WHERE type=? ORDER BY SUBSTR(id, 1, 2), CAST(SUBSTR(id, INSTR(id, '-') + 1) AS INTEGER) DESC", (type,))
            elif tablename == 'postcardStory':
                cursor.execute('''SELECT
                    p.id,
                    p.content_cn,
                    p.content_en,
                    p.comment,
                    g.userInfo,
                    g.picFileName,
                    g.contryNameEmoji,
                    g.type,
                    m.travel_time,
                    date( REPLACE ( SUBSTR( m.travel_time, 22, 10 ), '/', '-' ) ) AS receivedDate,
                    m.distance 
                FROM
                    postcardStory p
                    INNER JOIN Galleryinfo g ON p.id = g.id
                    INNER JOIN Mapinfo m ON p.id = m.id 
                WHERE
                    g.type = ?
                ORDER BY
                    receivedDate DESC''', (type,))
            else:
                cursor.execute(f"SELECT * FROM {tablename}")
            rows = cursor.fetchall()
            #print("rows",rows)
            for row in rows:
                if tablename == 'Galleryinfo':
                    data={
                        "id": row[0],
                        "userInfo": row[1],
                        "contryNameEmoji": row[2],
                        "picFileName": row[3],
                        "favoritesNum": row[4],
                        "type": row[5],
                        "travel_time": row[6],
                        "distance": row[8]
                        }
                elif tablename == 'Mapinfo':
                    data={
                        "id": row[0],
                        "FromCoor": json.loads(row[1]),
                        "ToCoor": json.loads(row[2]),
                        "distance": row[3],
                        "travel_time": row[4],
                        "link": row[5],
                        "user":row[6],
                        "sentAddr": row[7],
                        "receivedAddr": row[8],
                    }
                elif tablename == 'CountryStats':
                    data={
                        "name": row[0],
                        "countryCode": row[1],
                        "flagEmoji": row[2],
                        "value": row[3],
                        "sentNum": row[4],
                        "receivedNum":row[5],
                        "sentAvg": row[6],
                        "receivedAvg": row[7],
                        "sentMedian": row[8],
                        "receivedMedian": row[9],
                    }
                elif tablename == 'postcardStory':
                    data={
                        "id": row[0],
                        "content_cn": row[1],
                        "content_en": row[2],
                        "comment": row[3],
                        "userInfo": row[4],
                        "picFileName": row[5],
                        "contryNameEmoji":row[6],
                        "travel_time": row[8],
                        "distance": row[10],
                    }
                data_all.append(data)       
        conn.close()
        return data_all
    return data_all

# 设置写入数据库的统一入口函数
def writeDB(dbpath, content,tablename):   
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    if tablename == 'Galleryinfo':
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
                    (id TEXT, userInfo TEXT, contryNameEmoji TEXT, picFileName TEXT, favoritesNum TEXT, type TEXT)''')
        for item in content:
            id = item['id']
            userInfo = item['userInfo']
            contryNameEmoji = item['contryNameEmoji']
            picFileName = item['picFileName']
            favoritesNum = item['favoritesNum']
            type = item['type']
            cursor.execute(f"SELECT * FROM {tablename} WHERE id=? AND type=?", (id, type))
            existing_data = cursor.fetchone()
            if existing_data:
                # 更新已存在的行的其他列数据
                cursor.execute(f"UPDATE {tablename} SET userInfo=?, contryNameEmoji=?, picFileName=?, favoritesNum=? WHERE id=? AND type=?",
                                (userInfo, contryNameEmoji, picFileName, favoritesNum,  id, type))
            else:
                # 插入新的行
                cursor.execute(f"INSERT OR REPLACE INTO {tablename} VALUES (?, ?, ?, ?, ?, ?)",
                                (id, userInfo, contryNameEmoji, picFileName, favoritesNum, type))
    elif tablename == 'Mapinfo':
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
                    (id TEXT PRIMARY KEY, FromCoor TEXT, ToCoor TEXT, distance INTEGER, travel_time TEXT, link TEXT, user TEXT, sentAddr TEXT, receivedAddr TEXT, type TEXT)''')
        for item in content:
            id = item['id']
            FromCoor = json.dumps(item['FromCoor'])
            ToCoor = json.dumps(item['ToCoor'])
            distance = item['distance']
            travel_time = item['travel_time']
            link = item['link']
            user = item['user']
            sentAddr = item['sentAddr']
            receivedAddr = item['receivedAddr']
            type = item['type']    

            cursor.execute(f"INSERT OR REPLACE INTO {tablename} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (id, FromCoor, ToCoor, distance, travel_time, link, user, sentAddr, receivedAddr, type))
    # 将列表中的JSON对象写入文件      
    elif tablename == 'postcardStory':
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
                    (id TEXT, content_cn TEXT, content_en TEXT, comment TEXT)''')
        for item in content:
            id = item['id']
            content_cn = item['content_cn']
            content_en = item['content_en']
            comment = item['comment']
            cursor.execute(f"SELECT * FROM {tablename} WHERE id=? ", (id, ))
            existing_data = cursor.fetchone()
            if existing_data:
                # 更新已存在的行的其他列数据
                cursor.execute(f"UPDATE {tablename} SET content_cn=?, content_en=?,comment=?  WHERE id=?",
                                (content_cn, content_en,comment, id))
            else:
                # 插入新的行
                cursor.execute(f"INSERT OR REPLACE INTO {tablename} VALUES (?, ?, ?, ?)",
                                (id, content_cn, content_en, comment))
    elif tablename == 'CountryStats':
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
            (name TEXT, countryCode TEXT, flagEmoji TEXT, value INTEGER, sentNum INTEGER, receivedNum INTEGER, sentAvg INTEGER, receivedAvg INTEGER, sentMedian INTEGER, receivedMedian INTEGER,
            PRIMARY KEY (name))''')
        for item in content:
    
            name = item['name']
            countryCode = item['countryCode']
            flagEmoji = item['flagEmoji']
            value = item['value']
            sentNum = item['sentNum']
            receivedNum = item['receivedNum']
            sentAvg = item['sentAvg']
            receivedAvg = item['receivedAvg']
            sentMedian = item['sentMedian']
            receivedMedian = item['receivedMedian']
            cursor.execute(f"SELECT * FROM {tablename} WHERE name=?", (name,))
            existing_data = cursor.fetchone()
            if existing_data:
                # 更新已存在的行的其他列数据
                cursor.execute(f"UPDATE {tablename} SET countryCode=?, flagEmoji=?, value=?, sentNum=?, receivedNum=?, sentMedian=?, receivedMedian=? WHERE name=?", (countryCode, flagEmoji, value, sentNum, receivedNum, sentMedian, receivedMedian, name))
            else:
                # 插入新的行
                cursor.execute(f"INSERT OR REPLACE INTO {tablename} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (name, countryCode, flagEmoji, value, sentNum, receivedNum, sentAvg, receivedAvg, sentMedian, receivedMedian))
    print(f'已更新数据库{dbpath}的{tablename}\n')
    conn.commit()
    conn.close()



# 定义createMap.py的前置检查条件
def MapDataCheck():
    print("————————————————————")
    for type in types_map:
         multiTask(account,type,Cookie)
    
# 定义createGallery.py的前置检查条件
def PicDataCheck():    
    print("————————————————————") 
    stat,content_raw,types = getAccountStat(Cookie)
    getPageNum(stat,content_raw,types)
    getUserStat()
    for type in types:
        getGalleryInfo(type) # 获取图库信息
    for type in types:
        multiDownload(type) # 批量下载图片
    
# 定义createPersonalPage.py的前置检查条件    
def replaceTemplateCheck():  
    print("————————————————————")
    stat,content_raw,types = getAccountStat(Cookie)
    getPageNum(stat,content_raw,types)
    getUserStat()
    for type in types:
        getGalleryInfo(type) 

def md5(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        md5_hash = hashlib.md5(data).hexdigest()
    return md5_hash

def compareMD5(pathA,pathB):

    A_md5 = md5(pathA)
    B_md5 = md5(pathB)
    if B_md5 == A_md5:
        stat = "0"
    else:
        stat = "1"
    print(f"\n{pathA}:{A_md5}\n{pathB}:{B_md5}")
    return stat

if __name__ == "__main__":
   
    stat,content_raw,types = getAccountStat(Cookie)