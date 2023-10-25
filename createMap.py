import folium
from folium.plugins import MarkerCluster
import json
import re
import requests
import threading
import random
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("account", help="输入account")
parser.add_argument("Cookie", help="输入Cookie")      
options = parser.parse_args()

account = options.account
Cookie = options.Cookie


# with open("config.json", "r") as file:
#     data = json.load(file)
# account = data["account"]
# Cookie = data["Cookie"]
# threadsNum = data["threadsNum"]


url = f"https://www.postcrossing.com/user/{account}/gallery"  # 替换为您要获取数据的链接
types_map = ['sent', 'received']  


headers = {
    'authority': 'www.postcrossing.com',
    'Cookie': Cookie,
    
    }

# sentID_Local=[]
# with open(f"output/sent_List.json", "r") as file:
#         sentData = json.load(file)
# for item in sentData:
#     sentID_Local.append(item["id"])
# print(f"\nsentID_Local({len(sentID_Local)}):",sentID_Local)       

# receiveID_Local=[]
# with open(f"output/received_List.json", "r") as file:
#         receivedData = json.load(file)
# for item in receivedData:
#     receiveID_Local.append(item["id"])
# print(f"\nreceiveID_Local({len(receiveID_Local)}):",receiveID_Local)  

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
   


#获取账号状态
def getAccountStat(url,headers):
    i = 1
    url = url 
    #print(f"{url}")
    
    response = requests.get(url,headers=headers)
    #response = requests.get(url)
    response_status = response.status_code
    content_i = response.text.replace('"//', '"https://')
    #filename = f"./output/{account}_{type}({i}).html"
    """ with open(filename, "w", encoding="utf-8") as file:
        content_i = response.text.replace('"//', '"https://')
        file.write(content_i)
        print(f"\n{type}({i})数据保存成功：{filename}")   """ 
    return response_status,content_i

#读取所有sent、received的列表，获取每个postcardID的详细数据
def getUpdateID(account,type,Cookie):
    headers = {
    'Host': 'www.postcrossing.com',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0.1 Mobile/15E148 Safari/604.1',
    'Connection': 'keep-alive',
    'Referer': f'https://www.postcrossing.com/user/{account}/{type}',
    'Cookie': Cookie,
    'Sec-Fetch-Dest': 'empty'
        }
    url=f'https://www.postcrossing.com/user/{account}/data/{type}'    
    response = requests.get(url,headers=headers).text
    with open(f"./output/{type}_OnlineList.json", "w",encoding="utf-8") as file:
        file.write(response)
    with open(f"./output/{type}_OnlineList.json", "r",encoding="utf-8") as file:
        response = json.load(file)
    print("response:",response)
    onlineID = []
    for item in response:
         onlineID.append(item[0])
    if getLocalID(type) is not None:
        oldID = getLocalID(type)       
        newID = []
        # 遍历onlineID中的元素
        for id in onlineID:
            # 如果id不在oldID中，则将其添加到newID中
            if id not in oldID:
                newID.append(id)
        if len(newID) == 0:
            print(f"{type}_无需更新更新")
        else:
            print(f"{type}_等待更新list({len(newID)}个):{newID}\n")
        return newID
    else:
        # 当本地文件不存在时，则取online的postcardId作为待下载列表
        return onlineID
    

data_json = []  # 存储最终的data_json
def get_data(postcardID, data_json):
    for i, id in enumerate(postcardID):        
        url=f"https://www.postcrossing.com/postcards/{id}"        
        response = requests.get(url)       
        pattern = r"var senderLocation\s+=\s+new L.LatLng\(([-\d.]+), ([-\d.]+)\);\s+var receiverLocation\s+=\s+new L.LatLng\(([-\d.]+), ([-\d.]+)\);"
        matches = re.findall(pattern, response.text)  #提取发送、接收的经纬度坐标
        distance = int(re.search(r'traveled (.*?) km', response.text).group(1).replace(',', ''))
        travel_time = int(re.search(r'in (.*?) days', response.text).group(1))
        
        # 使用正则表达式提取发送者/接受者user
        userPattern = r'<a itemprop="url" href="/user/(.*?)"'
        userResults = re.findall(userPattern, response.text)
        print(f"{id}_userResults:{userResults}]")
        
        # 使用正则表达式提取链接link
        link = re.search(r'<meta property="og:image" content="(.*?)" />', response.text).group(1)  
        if "logo" in link:
            link = "gallery/picture/noPic.png"  #替换图片为空时的logo
        else:
            picFileName = re.search(r"/([^/]+)$", link).group(1)
            #print(f"{id}_picFileName:{picFileName}")
            link = f"gallery/picture/{picFileName}"
        
        # 使用正则表达式提取匹配结果
        addrPattern = r'<a itemprop="addressCountry" title="(.*?)" href="/country/(.*?)">(.*?)</a>'
        addrResults = re.findall(addrPattern, response.text)
        #print("{id}_addrResults:", addrResults)
        # 检查是否有匹配结果
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
        print(f"{type}_List:已提取{round((i+1)/(len(postcardID))*100,2)}%\n")
        

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

        pass
    
    #return data_all

def multiTask(account,type,Cookie):
    postcardID = getUpdateID(account,type,Cookie)  
#     if len(postcardID) > 0:
#         group_size = len(postcardID) // N
#         print(f"将{type}的postcardID分为{N}个线程并行处理，每个线程处理个数：{group_size}\n") 

    if len(postcardID) > 0:
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
            thread = threading.Thread(target=get_data, args=(group, data_json))
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
        if os.path.exists(removePath):  # 检查文件是否存在
            os.remove(removePath)  
    else:
        pass


    

def getHomeInfo(received):
    addr_count = {}
    home_coords = []
    home_addrs = []
    for item in received:
        addr = item["receivedAddr"]
        if addr in addr_count:
            addr_count[addr] += 1
        else:
            addr_count[addr] = 1       
        coord = tuple(item["To"])
        if coord not in home_coords:
            home_coords.append(coord)
            home_addrs.append(addr)
    most_common_addr = max(addr_count, key=addr_count.get)
    most_common_coord = home_coords[home_addrs.index(most_common_addr)]

    return most_common_coord, most_common_addr, home_coords, home_addrs


#读取已获取数据生成地图
def createMap(sent, received):
    most_common_homeCoord, most_common_homeAddr, homeCoords, homeAddrs = getHomeInfo(received)

    # print(f"most_common_homeCoord:\n", most_common_homeCoord)
    # print(f"most_common_homeAddr:\n", most_common_homeAddr)
    # print(f"homeCoords:\n", homeCoords)
    # print(f"homeAddrs:\n", homeAddrs)
    
    m = folium.Map(
        location=most_common_homeCoord,
        zoom_start=2,
        tiles='https://webrd02.is.autonavi.com/appmaptile?lang=zh_en&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
        
        #tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr='map',
    )

    def generate_random_offset():
            return random.uniform(-0.0001, 0.0001)
    for i,coord in enumerate(homeCoords):
        #生成home标记(Map)
        folium.Marker(
                location=coord,
                icon=folium.Icon(color='blue', icon='home'),
                popup=f'{homeAddrs[i]}'
            ).add_to(m)


    for coords in sent:
        # 解析postcardID、from坐标、to坐标、distance、days、link、user
        postcardID = coords["id"]
        from_coord = coords["From"]
        to_coord = coords["To"]
        distance = coords["distance"]
        days = coords["travel_time"]
        link = coords["link"]
        user = coords["user"]
        sentAddr = coords["sentAddr"]
        receivedAddr = coords["receivedAddr"]
        if user =='account closed':
            userInfo ='<b><i>account closed</b></i>'
        else:
            userInfo = f'<a href="https://www.postcrossing.com/user/{user}">{user}</a>' 

        if link == "":
            linkInfo = f'<a href="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" target="_blank"><img src="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" alt="Image"></a>'  #替换图片为空时的logo
        else:
            linkInfo =f'<a href="{link}" target="_blank"><img src="{link}" alt="Image"></a>'
        
        #生成已寄送明信片的接收地标记(Map)
        folium.Marker(
            location=[to_coord[0] + generate_random_offset(), to_coord[1] + generate_random_offset()],
            icon=folium.Icon(color='red', icon='stop'),
            popup=f'To {userInfo}</a> <br><a href="https://www.postcrossing.com/postcards/{postcardID}">{postcardID}</a><br>From: {sentAddr}<br>To: {receivedAddr} <br>📏 {distance} | ⏱ {days} days{linkInfo}'
        ).add_to(m)

        # 添加航线
        folium.PolyLine(
            locations=[from_coord,to_coord],
            color='red',
            weight=1,
            opacity=0.7,
            smooth_factor=10  
        ).add_to(m)    
        
    for coords in received:
        # 解析postcardID、from坐标、to坐标、distance、days、link、user
        postcardID = coords["id"]
        from_coord = coords["From"]
        to_coord = coords["To"]
        distance = coords["distance"]
        days = coords["travel_time"]
        link = coords["link"]
        user = coords["user"]
        sentAddr = coords["sentAddr"]
        receivedAddr = coords["receivedAddr"]
        if user =='account closed':
            userInfo ='<b><i>account closed</b></i>'
        else:
            userInfo = f'<a href="https://www.postcrossing.com/user/{user}">{user}</a>'
        if link == "":
            linkInfo = f'<a href="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" target="_blank"><img src="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" alt="Image"></a>'  #替换图片为空时的logo
        else:
            linkInfo =f'<a href="{link}" target="_blank"><img src="{link}" alt="Image"></a>'

        #生成已收到明信片的发送点标记(Map)
        folium.Marker(
            location=[from_coord[0] + generate_random_offset(), from_coord[1] + generate_random_offset()],
            icon=folium.Icon(color='green', icon='play'),
            popup=f'From {userInfo} <br><a href="https://www.postcrossing.com/postcards/{postcardID}">{postcardID}</a><br>From: {sentAddr}<br>To: {receivedAddr} <br>📏 {distance} | ⏱ {days} days{linkInfo}'
        ).add_to(m)

        # 添加航线
        folium.PolyLine(
            locations=[from_coord,to_coord],
            color='green',
            weight=1,
            opacity=0.7,
            smooth_factor=10  
        ).add_to(m)
        
    m.save("Map.html")
    replaceJsRef("./Map.html")

    print((f"\nMap.html已生成!"))
    # 保存地图为HTML文件

def createClusterMap(sent, received):
    most_common_homeCoord, most_common_homeAddr, homeCoords, homeAddrs = getHomeInfo(received)

    # print(f"most_common_homeCoord:\n", most_common_homeCoord)
    # print(f"most_common_homeAddr:\n", most_common_homeAddr)
    # print(f"homeCoords:\n", homeCoords)
    # print(f"homeAddrs:\n", homeAddrs)

    cluster = folium.Map(
        location=most_common_homeCoord,
        zoom_start=2,
        tiles='https://webrd02.is.autonavi.com/appmaptile?lang=zh_en&size=1&scale=1&style=8&x={x}&y={y}&z={z}',       
        #tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr='map',
    )
    marker_cluster = MarkerCluster().add_to(cluster)
    
    def generate_random_offset():
            return random.uniform(-0.0001, 0.0001)
    for i,coord in enumerate(homeCoords):
        #生成home标记(ClusterMap)
        marker = folium.Marker(
                location=coord,
                icon=folium.Icon(color='blue', icon='home'),
                popup=f'{homeAddrs[i]}'
            )
        marker.add_to(cluster) #设置home的marker固定显示，不被聚合统计


    for coords in sent:
        
        # 解析postcardID、from坐标、to坐标、distance、days、link、user
        postcardID = coords["id"]
        from_coord = coords["From"]
        to_coord = coords["To"]
        distance = coords["distance"]
        days = coords["travel_time"]
        link = coords["link"]
        user = coords["user"]
        sentAddr = coords["sentAddr"]
        receivedAddr = coords["receivedAddr"]


        if user =='account closed':
            userInfo ='<b><i>account closed</b></i>'
        else:
            userInfo = f'<a href="https://www.postcrossing.com/user/{user}">{user}</a>' 

        if link == "":
            linkInfo = f'<a href="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" target="_blank"><img src="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" alt="Image"></a>'  #替换图片为空时的logo
        else:
            linkInfo =f'<a href="{link}" target="_blank"><img src="{link}" alt="Image"></a>'
        
        
        #生成已寄送明信片的接收地标记(ClusterMap)
        folium.Marker(
            location=to_coord,
            icon=folium.Icon(color='red', icon='stop'),
            popup=f'To {userInfo}</a> <br><a href="https://www.postcrossing.com/postcards/{postcardID}">{postcardID}</a><br>From: {sentAddr}<br>To: {receivedAddr} <br>📏 {distance} | ⏱ {days} days{linkInfo}'
        ).add_to(marker_cluster)
        
        

    for coords in received:
        
        # 解析postcardID、from坐标、to坐标、distance、days、link、user
        postcardID = coords["id"]
        from_coord = coords["From"]
        to_coord = coords["To"]
        distance = coords["distance"]
        days = coords["travel_time"]
        link = coords["link"]
        user = coords["user"]
        sentAddr = coords["sentAddr"]
        receivedAddr = coords["receivedAddr"]
        if user =='account closed':
            userInfo ='<b><i>account closed</b></i>'
        else:
            userInfo = f'<a href="https://www.postcrossing.com/user/{user}">{user}</a>'
        if link == "":
            linkInfo = f'<a href="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" target="_blank"><img src="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" alt="Image"></a>'  #替换图片为空时的logo
        else:
            linkInfo =f'<a href="{link}" target="_blank"><img src="{link}" alt="Image"></a>'
        
        #生成已收到明信片的发送点标记(ClusterMap)
        folium.Marker(
            location=from_coord,
            icon=folium.Icon(color='green', icon='play'),
            popup=f'From {userInfo} <br><a href="https://www.postcrossing.com/postcards/{postcardID}">{postcardID}</a><br>From: {sentAddr}<br>To: {receivedAddr} <br>📏 {distance} | ⏱ {days} days{linkInfo}'
        ).add_to(marker_cluster)

        
    # 保存地图为HTML文件
    cluster.save("ClusterMap.html")
    replaceJsRef("./ClusterMap.html")
    print((f"\nClusterMap.html已生成!"))

def replaceJsRef(fileFullName):
    replaceContents = [['''<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>''',
                        '''<script src="./src/jquery-1.12.4/package/dist/jquery.min.js"></script>'''],
                       ['''<script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>''',
                        '''<script src="./src/leaflet-1.9.3/package/dist/leaflet.js"></script>'''],
                       ['''<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>''',
                        '''<script src="./src/bootstrap-5.2.2/package/dist/js/bootstrap.bundle.min.js"></script>'''],
                       ['''<script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>''',
                        '''<script src="./src/Leaflet.awesome-markers-2.0.2/dist/leaflet.awesome-markers.js"></script>'''],
                       ['''<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>''',
                        '''<link rel="stylesheet" type="text/css" href="./src/leaflet-1.9.3/package/dist/leaflet.css"/>'''],
                       ['''<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>''',
                        '''<link rel="stylesheet" type="text/css" href="./src/bootstrap-5.2.2/package/dist/css/bootstrap.min.css"/>'''],
                       ['''<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>''',
                        '''<link rel="stylesheet" type="text/css" href="./src/bootstrap-3.0.0/dist/css/bootstrap.min.css"/>'''],
                       ['''<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>''',
                        '''<link rel="stylesheet" type="text/css" href="./src/fontawesome-free-6.2.0/package/css/all.min.css"/>'''],
                       ['''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>''',
                        '''<link rel="stylesheet" type="text/css" href="./src/Leaflet.awesome-markers-2.0.2/dist/leaflet.awesome-markers.css"/>'''],
                       ['''<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>''',
                        '''<link rel="stylesheet" type="text/css" href="./src/templates/leaflet.awesome.rotate.min.css"/>'''],
                       ['''<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/leaflet.markercluster.js"></script>''',
                        '''<script src="./src/leaflet.markercluster-1.1.0/package/dist/leaflet.markercluster.js"></script>'''],
                       ['''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/MarkerCluster.css"/>''',
                        '''<link rel="stylesheet" type="text/css" href="./src/leaflet.markercluster-1.1.0/package/dist/MarkerCluster.css"/>'''],
                       ['''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/MarkerCluster.Default.css"/>''',
                        '''<link rel="stylesheet" type="text/css" href="./src/leaflet.markercluster-1.1.0/package/dist/MarkerCluster.Default.css"/>'''],
                       ['''<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet-dvf/0.3.0/leaflet-dvf.markers.min.js"></script>''',
                        '''<script src="./src/leaflet-dvf/leaflet-dvf.markers.min.js"></script>''']
                       ]

    with open(fileFullName, "r", encoding="utf-8") as f1, open(f"{fileFullName}.bak", "w", encoding="utf-8") as f2:
        for line in f1:
            for itm in replaceContents:
                if itm[0] in line:
                    line = line.replace(itm[0], itm[1])
                    replaceContents.remove(itm)
            f2.write(line)
    os.remove(fileFullName)
    os.rename(f"{fileFullName}.bak", fileFullName)



stat,content_raw = getAccountStat(url,headers)
    #print(stat
if stat == 200:
    print(f"用户:{account}的数据可获取！\n")
    for type in types_map:
        multiTask(account,type,Cookie) 
    with open(f"output/sent_List.json", "r") as file:
        sentData = json.load(file)
    with open(f"output/received_List.json", "r") as file:
        receivedData = json.load(file)
    createMap(sentData,receivedData)
    createClusterMap(sentData,receivedData)      

else:
    print(f"用户:{account}已注销/设置为非公开，无法获取！\n")
