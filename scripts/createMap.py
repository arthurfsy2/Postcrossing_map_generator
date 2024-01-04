import folium
from folium.plugins import MarkerCluster
import json
import time
import sqlite3
import random
import os
from multiDownload import MapDataCheck
from common_tools import readDB,writeDB,compareMD5
import sys
import shutil
import argparse

start_time = time.time()

with open("scripts/config.json", "r") as file:
    data = json.load(file)
# account = data["account"]
Cookie = data["Cookie"]
dbpath = data["dbpath"]

# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser()
parser.add_argument("account", help="输入account")
#parser.add_argument("password", help="输入password")      
#parser.add_argument("nickName", help="输入nickName")    
# parser.add_argument("Cookie", help="输入Cookie") 
#parser.add_argument("repo", help="输入repo")    
options = parser.parse_args()

account = options.account
#password = options.password
#nickName = options.nickName
# Cookie = options.Cookie
#repo = options.repo


userUrl = f"https://www.postcrossing.com/user/{account}"  
galleryUrl = f"{userUrl}/gallery"  # 设置该账号的展示墙
dataUrl = f"{userUrl}/data/sent"  
types_map = ['sent', 'received']  

headers = {
    'authority': 'www.postcrossing.com',
    'Cookie': Cookie,
    
    }

if os.path.exists(dbpath):
    shutil.copyfile(dbpath, f"{dbpath}BAK")

def getMapHomeInfo(receivedData):
    addr_count = {}
    home_coords = []
    home_addrs = []
    for item in receivedData:
        addr = f'{item["receivedAddr"]} [{item["receivedCountry"]}]'
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

def geojson(m):
    footprint = []
    stats_data=readDB(dbpath, "", "CountryStats")
    for data in stats_data:
        sentNum = float(data['sentNum'])
        receivedNum = float(data['receivedNum'])
        countryCode = data['countryCode']
        
        if sentNum > 0 and receivedNum > 0:
            footprint.append({'countryCode': countryCode, 'type': 2})
        elif sentNum > 0 or receivedNum > 0:
            footprint.append({'countryCode': countryCode, 'type': 1})
        else:
            footprint.append({'countryCode': countryCode, 'type': 0})
    with open('./src/geojson/world.zh.json', 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)
    geojson = folium.GeoJson(
        geojson_data,
        name='geojson',
        style_function=lambda feature: {
            'fillColor': 'blue' if feature['properties']['iso_a2'] in [d['countryCode'] for d in footprint if d['type'] == 2] else ('green' if feature['properties']['iso_a2'] in [d['countryCode'] for d in footprint if d['type'] == 1] else 'gray'),
            'weight': 0.8,  # 设置边界的粗细度
        }
    )
    return geojson.add_to(m)

#读取已获取数据生成地图
def createMap():
    sentData =readDB(dbpath, "sent", "Mapinfo")
    receivedData =readDB(dbpath, "received", "Mapinfo")
    allData = [sentData,receivedData]
    most_common_homeCoord, most_common_homeAddr, homeCoords, homeAddrs = getMapHomeInfo(receivedData)
    m = folium.Map(
        location=most_common_homeCoord,
        zoom_start=2,
        tiles='https://webrd02.is.autonavi.com/appmaptile?lang=zh_en&size=1&scale=1&style=8&x={x}&y={y}&z={z}',       
        #tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr='map',
    )
    geojson(m)    
    def generate_random_offset(): 
            return random.uniform(-0.0001, 0.0001)
    for i,coord in enumerate(homeCoords):
        #生成home标记(ClusterMap)
        marker = folium.Marker(
                location=coord,
                icon=folium.Icon(color='blue', icon='home'),
                popup=f'{homeAddrs[i]}'
            )
        marker.add_to(m) #设置home的marker固定显示，不被聚合统计

    for i,datas in enumerate(allData):
        for coords in datas:
            # 解析postcardID、from坐标、to坐标、distance、days、link、user
            postcardID = coords["id"]
            from_coord = coords["FromCoor"]
            to_coord = coords["ToCoor"]
            distance = coords["distance"]
            days = coords["travel_days"]
            link = coords["link"]
            user = coords["user"]
            sentAddr = f'{coords["sentAddr"]} [{coords["sentCountry"]}]'
            receivedAddr = f'{coords["receivedAddr"]} [{coords["receivedCountry"]}]'
            if user =='account closed':
                userInfo ='<b><i>account closed</b></i>'
            else:
                userInfo = f'<a href="https://www.postcrossing.com/user/{user}">{user}</a>' 

            if link == "":
                linkInfo = f'<a href="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" target="_blank"><img src="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" alt="Image"></a>'  #替换图片为空时的logo
            else:
                linkInfo =f'<a href="{link}" target="_blank"><img src="{link}" alt="Image"></a>'
            
            #生成已寄送明信片的接收地标记(ClusterMap)
            
            if i== 0:
                color='red'
                icon='stop'
                from_or_to = "To"
                location = to_coord
            elif i== 1:
                color='green'
                icon='play'
                from_or_to = "From"
                location = from_coord
            marker = folium.Marker(
                location=[location[0] + generate_random_offset(), location[1] + generate_random_offset()],
                icon=folium.Icon(color=color, icon=icon),
                popup=f'{from_or_to} {userInfo}</a> <br><a href="https://www.postcrossing.com/postcards/{postcardID}">{postcardID}</a><br>From: {sentAddr}<br>To: {receivedAddr} <br>📏 {distance} | ⏱ {days} {linkInfo}'
            ).add_to(m)  

           # 添加航线
            folium.PolyLine(
                locations=[from_coord,to_coord],
                color=color,
                weight=1,
                opacity=0.7,
                smooth_factor=10  
            ).add_to(m)
    m.save("Map.html")
    replaceJsRef("./Map.html")

    

def createClusterMap():
    sentData =readDB(dbpath, "sent", "Mapinfo")
    receivedData =readDB(dbpath, "received", "Mapinfo")
    allData = [sentData,receivedData]
    most_common_homeCoord, most_common_homeAddr, homeCoords, homeAddrs = getMapHomeInfo(receivedData)
    cluster = folium.Map(
        location=most_common_homeCoord,
        zoom_start=2,
        tiles='https://webrd02.is.autonavi.com/appmaptile?lang=zh_en&size=1&scale=1&style=8&x={x}&y={y}&z={z}',       
        #tiles='https://mt.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr='map',
    )
    geojson(cluster)
    marker_cluster = MarkerCluster().add_to(cluster)
    
    def generate_random_offset():
            return random.uniform(-0.0005, 0.0005)
    for i,coord in enumerate(homeCoords):
        #生成home标记(ClusterMap)
        marker = folium.Marker(
                location=coord,
                icon=folium.Icon(color='blue', icon='home'),
                popup=f'{homeAddrs[i]}'
            )
        marker.add_to(cluster) #设置home的marker固定显示，不被聚合统计

    for i,datas in enumerate(allData):
        for coords in datas:
            # 解析postcardID、from坐标、to坐标、distance、days、link、user
            postcardID = coords["id"]
            from_coord = coords["FromCoor"]
            to_coord = coords["ToCoor"]
            distance = coords["distance"]
            days = coords["travel_days"]
            link = coords["link"]
            user = coords["user"]
            sentAddr = f'{coords["sentAddr"]} [{coords["sentCountry"]}]'
            receivedAddr = f'{coords["receivedAddr"]} [{coords["receivedCountry"]}]'
            if user =='account closed':
                userInfo ='<b><i>account closed</b></i>'
            else:
                userInfo = f'<a href="https://www.postcrossing.com/user/{user}">{user}</a>' 

            if link == "":
                linkInfo = f'<a href="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" target="_blank"><img src="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" alt="Image"></a>'  #替换图片为空时的logo
            else:
                linkInfo =f'<a href="{link}" target="_blank"><img src="{link}" alt="Image"></a>'
            
            #生成已寄送明信片的接收地标记(ClusterMap)
            
            if i== 0:
                color='red'
                icon='stop'
                from_or_to = "To"
                location = to_coord
            elif i== 1:
                color='green'
                icon='play'
                from_or_to = "From"
                location = from_coord
            marker = folium.Marker(
                location=location,
                icon=folium.Icon(color=color, icon=icon),
                popup=f'{from_or_to} {userInfo}</a> <br><a href="https://www.postcrossing.com/postcards/{postcardID}">{postcardID}</a><br>From: {sentAddr}<br>To: {receivedAddr} <br>📏 {distance} | ⏱ {days} {linkInfo}'
            ).add_to(marker_cluster)  

        
    # 保存地图为HTML文件
    cluster.save("ClusterMap.html")
    replaceJsRef("./ClusterMap.html")




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

def createUserLocationMap():
    content =readDB(dbpath, "","userSummary")
    for id in content:
        coors = json.loads(id["coors"]  )
    # 创建地图对象
    map = folium.Map(
        location=coors,
        zoom_start=7,
        tiles='https://webrd02.is.autonavi.com/appmaptile?lang=zh_en&size=1&scale=1&style=8&x={x}&y={y}&z={z}',       
        #tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr='map',
    )
    # 创建标记对象
    marker = folium.Marker(location=coors, icon=folium.Icon(icon='home'))
    # 将标记添加到地图上
    marker.add_to(map)
    # 保存地图为HTML文件
    map.save("LocationMap.html")
    replaceJsRef("./LocationMap.html")

if not os.path.exists("./LocationMap.html"):
    createUserLocationMap()
if os.path.exists(f"{dbpath}BAK"):
    dbStat = compareMD5(dbpath, f"{dbpath}BAK")
    if dbStat == "1":
        print(f"{dbpath} 有更新") 
        createMap()
        print("Map.html已生成!")
        createClusterMap() 
        print("ClusterMap.html已生成!")
        os.remove(f"{dbpath}BAK")
    else:
        print(f"{dbpath} 暂无更新") 
        print("Map.html 暂无更新")
        print("ClusterMap.html 暂无更新")
        os.remove(f"{dbpath}BAK")
end_time = time.time()
execution_time = round((end_time - start_time),3)
print("————————————————————") 
print(f"scripts/createMap.py脚本执行时间：{execution_time}秒")