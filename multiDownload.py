import json
import re
import requests
import threading
import os
import json
from pyecharts import options as opts
from pyecharts.charts import Pie

from datetime import datetime, timedelta


with open("config.json", "r") as file:
    data = json.load(file)
account = data["account"]
Cookie = data["Cookie"]

url = f"https://www.postcrossing.com/user/{account}/gallery"  # 替换为您要获取数据的链接
types_map = ['sent', 'received']  

def getLocalID(type):
    ID_Local = []    
    file_path = f"output/{type}_List.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            Data = json.load(file)
        for item in Data:
            ID_Local.append(item["id"])
        oldID = ID_Local
        return oldID
    else:
        return None

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
        with open(f"output/{type}_List_update.json", "w") as file:
            json.dump(data_json, file, indent=2)
        print(f"{type}_List:已提取{round((i+1)/(len(postcardID))*100,2)}%")
def downloadPic(postcardID):
    for i, id in enumerate(postcardID): 
        url=f"https://www.postcrossing.com/postcards/{id}"        
        response = requests.get(url) 
        # 提取链接link
        link = re.search(r'<meta property="og:image" content="(.*?)" />', response.text).group(1)  
        if "logo" in link:
            pass
        else:
            picFileName = re.search(r"/([^/]+)$", link).group(1)
            picDownloadPath = f"gallery/picture/{picFileName}"  # 替换为你要保存的文件路径和文件名
            if os.path.exists(picDownloadPath):
                #print(f"已存在{picDownloadPath}")
                pass
            else:
                picDownloadUrl = f"https://s3.amazonaws.com/static2.postcrossing.com/postcard/medium/{picFileName}"
                #print(f"picDownloadUrl:{picDownloadUrl}")
                response = requests.get(picDownloadUrl)
                #print(f"正在下载{picFileName}")
                with open(picDownloadPath, "wb") as file:
                    file.write(response.content)
        print(f"图片下载进度：{round((i+1)/(len(postcardID))*100,2)}%")

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
    with open(f"output/UserStats.json", "w") as file:
        json.dump(a_data, file, indent=2)
   
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

    # 构建输出结果
    output = []
    for country_code, count in country_count.items():
        country_name = country_data.get(country_code, "")
        result = {
            "name": country_name,
            "value": int(count)
        }
        output.append(result)


    # 将结果输出到stats.json文件
    with open('./output/stats.json', 'w') as f:
        json.dump(output, f, indent=2)


    


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
        with open(f"output/{type}_List_update.json", "w") as file:
            json.dump(data_json, file, indent=2)
        print(f"{type}的update List已提取完成！\n")

        # 读取update文件的数组内容
        with open(f"output/{type}_List_update.json", "r") as update_file:
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
        with open(f"output/{type}_List.json", "w") as file:
            json.dump(existing_data, file, indent=2)

        removePath = f"./output/{type}_List_update.json"
        if os.path.exists(removePath):  # 更新完后删除List_update.json
            os.remove(removePath)  
    else:
        pass
    
    if hasPicID is not None:
        Num = round(len(hasPicID)/20) 
        if Num < 1:
            realNum = 1
        elif Num >= 1 and Num <= 10:
            realNum = Num
        elif Num >10: # 最大并发数为10
            realNum = 10
        group_size = len(hasPicID) // realNum
        print(f"将{type}的postcardID分为{realNum}个线程并行下载，每个线程下载图片个数：{group_size}\n")
        picDownload_groups = [hasPicID[i:i+group_size] for i in range(0, len(hasPicID), group_size)]
        # 创建线程列表

        # 创建并启动线程
        for i,group in enumerate(picDownload_groups):
            thread = threading.Thread(target=downloadPic, args=(group,))
            thread.start()
            

getUserStat()