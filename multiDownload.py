import json
import re
import requests
from bs4 import BeautifulSoup
import threading
import os
import time
import json
import pandas as pd
import math
from datetime import datetime, timedelta
import sys



with open("config.json", "r") as file:
    data = json.load(file)
account = data["account"]
account = data["account"]
nickName = data["nickName"]
Cookie = data["Cookie"]
picDriverPath = data["picDriverPath"]

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
        print(f"{account}的Cookies有效，可访问个人账号内容……\n")
    elif galleryStatus == 200 and cookieStat == 404:
        totalStat ="getPublic"
        types = ['sent', 'received'] 
        print(f"{account}的Cookies无效，只能访问gallery内容")
    elif galleryStatus != 200:
        totalStat ="unAccessible"
        print(f"用户:{account}已注销/设置为非公开，无法获取！\n")
        sys.exit()

    return totalStat,galleryContent,types





def getCountryFlagEmoji(flag):
    # 读取contryName.json文件
    with open('contryNameEmoji.json') as file:
        data = json.load(file)
    # 获取flag对应的值
    value = data.get(flag)
    return value

def getGalleryInfo(pageNum,type):
    i = 1
    content_all=[]
    while i <= pageNum:
        all_url = f"{galleryUrl}/{type}/{i}"
        print(f"正在获取/{account}/gallery/{type}/{i}的数据")
        response = requests.get(all_url,headers=headers)
        
        content_i = response.text.replace('"//', '"https://')
        soup = BeautifulSoup(content_i, "html.parser")
        lis = soup.find_all("li")
        content_page=[]
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
                    userInfo = ""
                    contryName = ""
                elif type == "favourites":                 
                    picDownloadPath = f"gallery/picture/{picFileName}"  # 替换为你要保存的文件路径和文件名
                    if os.path.exists(picDownloadPath):
                        #print(f"已存在{picDownloadPath}")
                        pass
                    else:
                        # picDownloadUrl = f"https://s3.amazonaws.com/static2.postcrossing.com/postcard/medium/{picFileName}"
                        # #print(f"picDownloadurl:{picDownloadurl}")
                        # response = requests.get(picDownloadUrl)
                        print(f"正在下载{picFileName}")
                        # with open(picDownloadPath, "wb") as file:
                        #     file.write(response.content)
                    user = figcaption.find("div").find("a").text
                    userInfo = f"[{user}]({baseUrl}user/{user})"
                    if not user:
                        userInfo = "***该用户已关闭***"
                    flag = re.search(r'href="/country/(.*?)"', str(figcaption)).group(1)
                    contryName = getCountryFlagEmoji(flag)
                else:
                    user = figcaption.find("div").find("a").text
                    userInfo = f"[{user}]({baseUrl}user/{user})"
                    if not user:
                        userInfo = "***该用户已关闭***"
                    flag = re.search(r'href="/country/(.*?)"', str(figcaption)).group(1)
                    contryName = getCountryFlagEmoji(flag)
                content_page.append({
                    'id': postcardID,
                    'userInfo': userInfo,
                    'contryNameEmoji': contryName,
                    'picFileName': picFileName,
                })
        content_all.extend(content_page)                        
        i += 1
        with open(f'./gallery/{type}.json', 'w') as file:
            json.dump(content_all, file, indent=2)
        print(f"已导出:./gallery/{type}.json\n")

def getCount(type,content):
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

def createGalleryJS(type,content):
    counts=getCount(type,content)
    #print(f"\n{account}展示墙链接：{galleryUrl}/{type}")      
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
    getGalleryInfo(pageNum,type)
    with open(f"./gallery/title.json", "w",encoding="utf-8") as file:
            json.dump(data, file, indent=2)
    return data



def getLocalID(type):
    ID_Local = []    
    file_path = f"./output/{type}_List.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            Data = json.load(file)
        for item in Data:
            ID_Local.append(item["id"])
        oldID = ID_Local
        
    else:
        oldID = None
    return oldID

def getLocalPic():
    localPicList = []
    picPath = "./gallery/picture"
    for root, dirs,files in os.walk(picPath):
        for file in files:
            localPicList.append(file)
    #print(f"localPicList({len(localPicList)}):\n{localPicList}")
    return localPicList



#读取所有sent、received的列表，获取每个postcardID的详细数据
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
    if getLocalID(type) is not None:
        oldID = getLocalID(type)       
        newID = []
        # 遍历onlineID中的元素
        for id in onlineID:
            # 如果id不在oldID中，则将其添加到newID中
            if id not in oldID:
                newID.append(id)
        if len(newID) == 0:
            print(f"{type}_List.json无需更新\n")
            updateID = None
        else:
            print(f"{type}_等待更新list({len(newID)}个):{newID}\n")
            updateID = newID
    else:
        # 当本地文件不存在时，则取online的postcardId作为待下载列表
        updateID = onlineID    
    return updateID,hasPicID

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

def get_data(postcardID,type, data_json):
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
        # print(f"{id}_sentAddr:", sentAddr)
        # print(f"{id}_sentCountry:", sentCountry)
        # print(f"{id}_receivedAddr:", receivedAddr)
        # print(f"{id}_receivedCountry:", receivedCountry)

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
            # 将字典对象添加到列表中
            data_json.append({
                "id": id,
                "From":from_coord,
                "To":to_coord,
                "distance": distance,
                "travel_time": travel_time,
                "link": link,
                "user": user,
                "sentAddr":f"{sentAddr}({sentCountry})",
                "receivedAddr":f"{receivedAddr}({receivedCountry})",
            })

        # 将列表中的JSON对象写入文件
        with open(f"./output/{type}_List_update.json", "w") as file:
            json.dump(data_json, file, indent=2)
        print(f"{type}_List:已提取{round((i+1)/(len(postcardID))*100,2)}%")

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
    with open(f'./gallery/{type}.json', 'r') as file:
        data = json.load(file)

    # 提取picFileName字段内容
    picFileNameList = [item['picFileName'] for item in data]
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
    #print(f"{type}_updatePic:{updatePic}\n")
    return updatePic



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
    print(f"已生成output/month.json")
    # 统计每个国家代码的出现次数
    country_count = {}
    for item in a_data:
        country_code = item[-1]
        if country_code in country_count:
            country_count[country_code] += 1
        else:
            country_count[country_code] = 1

    # 读取contryName.json文件
    with open('contryName.json', 'r') as f:
        country_data = json.load(f)

    # 读取contryName.json文件
    with open('contryNameEmoji.json', 'r') as f:
        country_data_emoji = json.load(f)


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
    result = [{'date': date, 'num': summary[date]} for date in summary]

    # 将结果输出到month.json文件中
    with open(f"./output/month.json", 'w') as f:
        json.dump(result, f, indent=2)

    print(f"已生成output/month.json")
    # 创建一个空列表用于存储每个国家的统计结果
    country_stats = []

    # 遍历 a_data 中的每个元素
    for item in a_data:
        country_code = item[3]  # 获取国家代码
        country_type = item[2]  # 获取类型（sent 或 received）

        # 根据国家代码在 countryName.json 中查找对应的英文名
        if country_code in country_data:
            country_name = country_data[country_code]
            country_flag = country_data_emoji[country_code]
        else:
            country_name = "Unknown"

        # 判断是否已存在相同国家名称的统计项
        found = False
        for stats in country_stats:
            if stats['name'] == country_name:
                found = True
                stats['value'] += 1
                if country_type == 's':
                    stats['sentNum'] += 1
                    stats['sentAvg'] += item[1]
                elif country_type == 'r':
                    stats['receivedNum'] += 1
                    stats['receivedAvg'] += item[1]
                break

        # 如果不存在相同国家名称的统计项，则添加新的统计项
        if not found:
            if country_type == 's':
                country_stats.append({
                    'name': country_name,
                    'flagEmoji': country_flag,
                    'value': 1,
                    'sentNum': 1,
                    'receivedNum': 0,
                    'sentAvg': item[1],
                    'receivedAvg': 0
                })
            elif country_type == 'r':
                country_stats.append({
                    'name': country_name,
                    'flagEmoji': country_flag,
                    'value': 1,
                    'sentNum': 0,
                    'receivedNum': 1,
                    'sentAvg': 0,
                    'receivedAvg': item[1]
                })

    # 计算平均值并保留小数点后一位
    for stats in country_stats:
        if stats['sentNum'] > 0:
            stats['sentAvg'] = round(stats['sentAvg'] / stats['sentNum'], 1)
        else:
            stats['sentAvg'] = '-'
        if stats['receivedNum'] > 0:
            stats['receivedAvg'] = round(stats['receivedAvg'] / stats['receivedNum'], 1)
        else:
            stats['receivedAvg'] = '-'

    # 将结果按照 value 值从大到小进行排序
    country_stats.sort(key=lambda x: x['value'], reverse=True)

    # 将统计结果写入 b.json 文件
    with open('./output/stats.json', 'w') as file:
        json.dump(country_stats, file, indent=2)
    print(f"./output/stats.json")
    
def getUserSheet():
    # 读取 stats.json 文件并将内容存储在 stats_data 变量中
    with open('./output/stats.json', 'r') as file:
        stats_data = json.load(file)

    # 按照 name 的 A-Z 字母顺序对 stats_data 进行排序
    sorted_stats_data = sorted(stats_data, key=lambda x: x['name'])
    #print("sorted_stats_data",sorted_stats_data)
    # 创建表头
    #table_header = "| No. | Country | Sent | Received | Avg travel(Sent) | Avg travel(Received) |\n"
    table_header1 = "| 序号 | 国家 | 已寄出 | 已收到 | 寄出-平均所需天数 | 收到-平均所需天数 |\n"
    table_header2 = "| --- | --- | --- | --- | --- | --- |\n"

    # 创建表格内容
    table_content = ""
    for i, stats in enumerate(sorted_stats_data, start=1):
        country = stats['name']
        flag = stats['flagEmoji']
        sent = stats['sentNum']
        received = stats['receivedNum']
        sent_avg = stats['sentAvg']
        received_avg = stats['receivedAvg']
        if sent_avg =="-":
            sent_avg_days = "-"
        else:
            sent_avg_days = f"{sent_avg}天"
        
        if received_avg =="-":
            received_avg_days = "-"
        else:
            received_avg_days = f"{received_avg}天"

        
        table_content += f"| {i} | {country} {flag} | {sent} | {received} | {sent_avg_days} | {received_avg_days} |\n"

    # 将表头和表格内容合并
    table = table_header1 + table_header2 + table_content

    # 将表格内容写入 mdsheet.md 文件
    with open('./output/mdsheet.md', 'w' ,encoding="utf-8") as file:
        file.write(table)
    return table


def multiTask(account,type,Cookie):
    postcardID,hasPicID = getUpdateID(account,type,Cookie)  
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
        data_json = []  # 存储最终的data_json

        # 创建并启动线程
        for i,group in enumerate(postcard_groups):
            thread = threading.Thread(target=get_data, args=(group, type, data_json))
            thread.start()
            threads.append(thread)
            
        # 等待所有线程完成
        for thread in threads:
            thread.join()
            
        # 将列表中的JSON对象写入文件
        with open(f"./output/{type}_List_update.json", "w") as file:
            json.dump(data_json, file, indent=2)
        print(f"{type}的update List已提取完成！\n")

        # 读取update文件的数组内容
        with open(f"./output/{type}_List_update.json", "r") as update_file:
            update_data = json.load(update_file)

        # 读取原有的JSON文件内容
        file_path = f"./output/{type}_List.json"
        if os.path.exists(file_path):
            with open(file_path, "r") as existing_file:
                existing_data = json.load(existing_file)
                # 将update数据追加到existing数据后面
                existing_data.extend(update_data)           
        else:
            existing_data = update_data
        # 写入合并后的内容到JSON文件
        with open(f"./output/{type}_List.json", "w") as file:
            json.dump(existing_data, file, indent=2)

        removePath = f"./output/{type}_List_update.json"
        if os.path.exists(removePath):  # 更新完后删除List_update.json
            os.remove(removePath)  
    else:
        pass
    

def multiDownload(type):
    updatePic = getUpdatePic(type)
    print("————————————————————")
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
            
        # # 将列表中的JSON对象写入文件
        # with open(f"./output/{type}_PicList_update.json", "w") as file:
        #     json.dump(pic_json, file, indent=2)
        # if getLocalPic() is not None:
        #     oldPic = getLocalPic()       
        #     newPic = []
        #     # 遍历onlineID中的元素
        #     for pic in pic_json:
        #         # 如果id不在oldID中，则将其添加到newID中
        #         if pic not in oldPic:
        #             newPic.append(pic)
        #     if len(newPic) == 0:
        #         print(f"{type}_PicList.json无需更新\n")
        #         updatePic = None
        #     else:
        #         print(f"{type}_等待更新list({len(newPic)}个):{newPic}\n")
        #         updatePic = newPic
        # else:
        #     # 当本地文件不存在时，则取online的postcardId作为待下载列表
        #     updatePic = pic_json 
        # print(f"updatePic：{updatePic}")
    else:
        print(f"{type}_图库无需更新")

def MapDataCheck():
    for type in types_map:
        print("————————————————————")
        if os.path.exists(f"output/{type}_List.json"):         
            print(f"已存在output/{type}_List.json") 
            #dl.multiTask(account,type,Cookie) 
            if stat != "getPrivate":          
                print(f"{account}的Cookies无效，无法更新数据。")
            else:
                print(f"{account}的Cookies有效，正在比对数据……")    
                multiTask(account,type,Cookie) 
            
        else:
            if stat != "getPrivate":          
                print(f"{account}的Cookies无效，且缺少output/{type}_List.json，无法生成地图数据，已退出")
                sys.exit()
            else:
                print(f"{account}的Cookies有效，准备生成output/{type}_List.json……") 
                multiTask(account,type,Cookie) 

stat,content_raw,types = getAccountStat()

def PicDataCheck():  
    for type in types:
        createGalleryJS(type,content_raw) 
    for type in types:
        multiDownload(type)
    replaceTemplate()
    

    
    



def replateTitle(type):    
    
    with open(f"./gallery/title.json", "r",encoding="utf-8") as f:
        title = json.load(f)
    value = title.get(type)
    from_or_to, pageNum, Num, title = value
    return title

def replaceTemplate():
          
    getUserStat()
    #getUserSheet()       
    title_all=""
    for type in types:
        
        title = replateTitle(type)
        #print("title:",title)
        title_all += f"#### [{title}]({nickName}/postcrossing/{type})\n\n"
    #print("title_all:\n",title_all)
    sheet = getUserSheet()
    with open(f"./信息汇总_template.md", "r",encoding="utf-8") as f:
        data = f.read()  
        dataNew = data.replace('//请替换明信片墙title',title_all)
        dataNew = dataNew.replace('//请替换明信片表格',sheet)

    with open(f"./信息汇总.md", "w",encoding="utf-8") as f:
        f.write(dataNew)  


#### [明信片展示墙（寄出）](/Arthur/postcrossing/sent)

#### [明信片展示墙（收到）](/Arthur/postcrossing/received)

#### [明信片展示墙（我收到的赞）](/Arthur/postcrossing/popular)

#### [明信片展示墙（我的点赞）](/Arthur/postcrossing/favourites)