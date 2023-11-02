import folium
from folium.plugins import MarkerCluster
import json
import time
import sqlite3
import random
import os
import multiDownload as dl
import sys

start_time = time.time()

with open("config.json", "r") as file:
    data = json.load(file)
account = data["account"]
Cookie = data["Cookie"]
dbpath = data["dbpath"]

userUrl = f"https://www.postcrossing.com/user/{account}"  
galleryUrl = f"{userUrl}/gallery"  # 设置该账号的展示墙
dataUrl = f"{userUrl}/data/sent"  
types_map = ['sent', 'received']  

headers = {
    'authority': 'www.postcrossing.com',
    'Cookie': Cookie,
    
    }
 

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
        coord = tuple(item["ToCoor"])
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
        from_coord = coords["FromCoor"] #FromCoor = json.dumps(item['FromCoor'])
        to_coord = coords["ToCoor"]
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
            popup=f'To {userInfo}</a> <br><a href="https://www.postcrossing.com/postcards/{postcardID}">{postcardID}</a><br>From: {sentAddr}<br>To: {receivedAddr} <br>📏 {distance} | ⏱ {days} {linkInfo}'
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
        from_coord = coords["FromCoor"]
        to_coord = coords["ToCoor"]
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
            popup=f'From {userInfo} <br><a href="https://www.postcrossing.com/postcards/{postcardID}">{postcardID}</a><br>From: {sentAddr}<br>To: {receivedAddr} <br>📏 {distance} | ⏱ {days} {linkInfo}'
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
        from_coord = coords["FromCoor"]
        to_coord = coords["ToCoor"]
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
            popup=f'To {userInfo}</a> <br><a href="https://www.postcrossing.com/postcards/{postcardID}">{postcardID}</a><br>From: {sentAddr}<br>To: {receivedAddr} <br>📏 {distance} | ⏱ {days} {linkInfo}'
        ).add_to(marker_cluster)
        
        
    for coords in received:
        # 解析postcardID、from坐标、to坐标、distance、days、link、user
        postcardID = coords["id"]
        from_coord = coords["FromCoor"]
        to_coord = coords["ToCoor"]
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
            popup=f'From {userInfo} <br><a href="https://www.postcrossing.com/postcards/{postcardID}">{postcardID}</a><br>From: {sentAddr}<br>To: {receivedAddr} <br>📏 {distance} | ⏱ {days} {linkInfo}'
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

dl.MapDataCheck()
print("——————————正在生成地图——————————")
sentData =dl.readDB(dbpath, "sent", "Mapinfo")
receivedData =dl.readDB(dbpath, "received", "Mapinfo")
createMap(sentData,receivedData)
createClusterMap(sentData,receivedData)  

end_time = time.time()
execution_time = round((end_time - start_time),3)
print("————————————————————") 
print(f"createMap.py脚本执行时间：{execution_time}秒")