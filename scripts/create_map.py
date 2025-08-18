import folium
from folium.plugins import MarkerCluster
import json
import time
import sqlite3
import random
import os
from common_tools import db_path, read_db_table
from multi_download import get_update_id
import sys
import shutil
import argparse


with open("scripts/config.json", "r") as file:
    data = json.load(file)
# account = data["account"]
Cookie = data["Cookie"]
db_update = data["db_update"]


def get_map_home_info(received_data):
    # print("received_data:",received_data)
    addr_count = {}
    home_coords = []
    home_addrs = []
    for item in received_data:
        addr = f'{item["received_addr"]} [{item["received_country"]}]'
        if addr in addr_count:
            addr_count[addr] += 1
        else:
            addr_count[addr] = 1
        coord = tuple(json.loads(item["to_coor"]))
        if coord not in home_coords:
            home_coords.append(coord)
            home_addrs.append(addr)
    most_common_addr = max(addr_count, key=addr_count.get)
    most_common_coord = home_coords[home_addrs.index(most_common_addr)]

    return most_common_coord, most_common_addr, home_coords, home_addrs


def geojson(m):
    footprint = []
    stats_data = read_db_table(db_path, "country_stats")
    for data in stats_data:
        sent_num = float(data["sent_num"])
        received_num = float(data["received_num"])
        country_code = data["country_code"]

        if sent_num > 0 and received_num > 0:
            footprint.append({"country_code": country_code, "type": 2})
        elif sent_num > 0 or received_num > 0:
            footprint.append({"country_code": country_code, "type": 1})
        else:
            footprint.append({"country_code": country_code, "type": 0})
    with open("./src/geojson/world.zh.json", "r", encoding="utf-8") as f:
        geojson_data = json.load(f)
    geojson = folium.GeoJson(
        geojson_data,
        name="geojson",
        style_function=lambda feature: {
            "fillColor": (
                "blue"
                if feature["properties"]["iso_a2"]
                in [d["country_code"] for d in footprint if d["type"] == 2]
                else (
                    "green"
                    if feature["properties"]["iso_a2"]
                    in [d["country_code"] for d in footprint if d["type"] == 1]
                    else "gray"
                )
            ),
            "weight": 0.8,  # 设置边界的粗细度
        },
    )
    return geojson.add_to(m)


def create_map():
    """
    读取已获取数据生成地图
    """
    sent_data = read_db_table(db_path, "map_info", {"card_type": "sent"})
    received_data = read_db_table(db_path, "map_info", {"card_type": "received"})
    allData = [sent_data, received_data]
    most_common_home_coord, most_common_home_addr, home_coords, home_addrs = (
        get_map_home_info(received_data)
    )
    m = folium.Map(
        location=most_common_home_coord,
        zoom_start=2,
        tiles="https://webrd02.is.autonavi.com/appmaptile?lang=zh_en&size=1&scale=1&style=8&x={x}&y={y}&z={z}",
        # tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr="map",
    )
    geojson(m)

    def generate_random_offset():
        return random.uniform(-0.0001, 0.0001)

    for i, coord in enumerate(home_coords):
        # 生成home标记(ClusterMap)
        marker = folium.Marker(
            location=coord,
            icon=folium.Icon(color="blue", icon="home"),
            popup=f"{home_addrs[i]}",
        )
        marker.add_to(m)  # 设置home的marker固定显示，不被聚合统计

    for i, datas in enumerate(allData):
        for coords in datas:
            # 解析postcardID、from坐标、to坐标、distance、days、link、user
            postcardID = coords["card_id"]
            from_coord = json.loads(coords["from_coor"])
            to_coord = json.loads(coords["to_coor"])
            distance = coords["distance"]
            days = coords["travel_days"]
            link = coords["link"]
            user = coords["user"]
            sent_addr = f'{coords["sent_addr"]} [{coords["sent_country"]}]'
            received_addr = f'{coords["received_addr"]} [{coords["received_country"]}]'
            if user == "account closed":
                userInfo = "<b><i>account closed</b></i>"
            else:
                userInfo = (
                    f'<a href="https://www.postcrossing.com/user/{user}">{user}</a>'
                )

            if link == "":
                linkInfo = f'<a href="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" target="_blank"><img src="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" alt="Image"></a>'  # 替换图片为空时的logo
            else:
                linkInfo = f'<a href="{link}" target="_blank"><img src="{link}" alt="Image"></a>'

            # 生成已寄送明信片的接收地标记(ClusterMap)

            if i == 0:
                color = "red"
                icon = "stop"
                from_or_to = "To"
                location = to_coord
            elif i == 1:
                color = "green"
                icon = "play"
                from_or_to = "From"
                location = from_coord
            marker = folium.Marker(
                location=[
                    location[0] + generate_random_offset(),
                    location[1] + generate_random_offset(),
                ],
                icon=folium.Icon(color=color, icon=icon),
                popup=f'{from_or_to} {userInfo}</a> <br><a href="https://www.postcrossing.com/postcards/{postcardID}">{postcardID}</a><br>From: {sent_addr}<br>To: {received_addr} <br>📏 {distance} | ⏱ {days} {linkInfo}',
            ).add_to(m)

            # 添加航线
            folium.PolyLine(
                locations=[from_coord, to_coord],
                color=color,
                weight=1,
                opacity=0.7,
                smooth_factor=10,
            ).add_to(m)
    m.save("map.html")
    replace_js_ref("./map.html")


def create_cluster_map():
    sent_data = read_db_table(db_path, "map_info", {"card_type": "sent"})
    received_data = read_db_table(db_path, "map_info", {"card_type": "received"})
    allData = [sent_data, received_data]
    most_common_home_coord, most_common_home_addr, home_coords, home_addrs = (
        get_map_home_info(received_data)
    )
    cluster = folium.Map(
        location=most_common_home_coord,
        zoom_start=2,
        tiles="https://webrd02.is.autonavi.com/appmaptile?lang=zh_en&size=1&scale=1&style=8&x={x}&y={y}&z={z}",
        # tiles='https://mt.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr="map",
    )
    geojson(cluster)
    marker_cluster = MarkerCluster().add_to(cluster)

    def generate_random_offset():
        return random.uniform(-0.0005, 0.0005)

    for i, coord in enumerate(home_coords):
        # 生成home标记(ClusterMap)
        marker = folium.Marker(
            location=coord,
            icon=folium.Icon(color="blue", icon="home"),
            popup=f"{home_addrs[i]}",
        )
        marker.add_to(cluster)  # 设置home的marker固定显示，不被聚合统计

    for i, datas in enumerate(allData):
        for coords in datas:
            # 解析postcardID、from坐标、to坐标、distance、days、link、user
            postcardID = coords["card_id"]
            from_coord = json.loads(coords["from_coor"])
            to_coord = json.loads(coords["to_coor"])
            distance = coords["distance"]
            days = coords["travel_days"]
            link = coords["link"]
            user = coords["user"]
            sent_addr = f'{coords["sent_addr"]} [{coords["sent_country"]}]'
            received_addr = f'{coords["received_addr"]} [{coords["received_country"]}]'
            if user == "account closed":
                userInfo = "<b><i>account closed</b></i>"
            else:
                userInfo = (
                    f'<a href="https://www.postcrossing.com/user/{user}">{user}</a>'
                )

            if link == "":
                linkInfo = f'<a href="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" target="_blank"><img src="https://www.postcrossing.com/images/pwa/manifest-icon-192.maskable.png" alt="Image"></a>'  # 替换图片为空时的logo
            else:
                linkInfo = f'<a href="{link}" target="_blank"><img src="{link}" alt="Image"></a>'

            # 生成已寄送明信片的接收地标记(ClusterMap)

            if i == 0:
                color = "red"
                icon = "stop"
                from_or_to = "To"
                location = to_coord
            elif i == 1:
                color = "green"
                icon = "play"
                from_or_to = "From"
                location = from_coord
            marker = folium.Marker(
                location=location,
                icon=folium.Icon(color=color, icon=icon),
                popup=f'{from_or_to} {userInfo}</a> <br><a href="https://www.postcrossing.com/postcards/{postcardID}">{postcardID}</a><br>From: {sent_addr}<br>To: {received_addr} <br>📏 {distance} | ⏱ {days} {linkInfo}',
            ).add_to(marker_cluster)

    # 保存地图为HTML文件
    cluster.save("cluster_map.html")
    replace_js_ref("./cluster_map.html")


def replace_js_ref(fileFullName):
    replaceContents = [
        [
            """<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>""",
            """<script src="./src/jquery-1.12.4/package/dist/jquery.min.js"></script>""",
        ],
        [
            """<script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>""",
            """<script src="./src/leaflet-1.9.3/package/dist/leaflet.js"></script>""",
        ],
        [
            """<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>""",
            """<script src="./src/bootstrap-5.2.2/package/dist/js/bootstrap.bundle.min.js"></script>""",
        ],
        [
            """<script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>""",
            """<script src="./src/Leaflet.awesome-markers-2.0.2/dist/leaflet.awesome-markers.js"></script>""",
        ],
        [
            """<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>""",
            """<link rel="stylesheet" type="text/css" href="./src/leaflet-1.9.3/package/dist/leaflet.css"/>""",
        ],
        [
            """<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>""",
            """<link rel="stylesheet" type="text/css" href="./src/bootstrap-5.2.2/package/dist/css/bootstrap.min.css"/>""",
        ],
        [
            """<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>""",
            """<link rel="stylesheet" type="text/css" href="./src/bootstrap-3.0.0/dist/css/bootstrap.min.css"/>""",
        ],
        [
            """<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>""",
            """<link rel="stylesheet" type="text/css" href="./src/fontawesome-free-6.2.0/package/css/all.min.css"/>""",
        ],
        [
            """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>""",
            """<link rel="stylesheet" type="text/css" href="./src/Leaflet.awesome-markers-2.0.2/dist/leaflet.awesome-markers.css"/>""",
        ],
        [
            """<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>""",
            """<link rel="stylesheet" type="text/css" href="./src/templates/leaflet.awesome.rotate.min.css"/>""",
        ],
        [
            """<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/leaflet.markercluster.js"></script>""",
            """<script src="./src/leaflet.markercluster-1.1.0/package/dist/leaflet.markercluster.js"></script>""",
        ],
        [
            """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/MarkerCluster.css"/>""",
            """<link rel="stylesheet" type="text/css" href="./src/leaflet.markercluster-1.1.0/package/dist/MarkerCluster.css"/>""",
        ],
        [
            """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/MarkerCluster.Default.css"/>""",
            """<link rel="stylesheet" type="text/css" href="./src/leaflet.markercluster-1.1.0/package/dist/MarkerCluster.Default.css"/>""",
        ],
        [
            """<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet-dvf/0.3.0/leaflet-dvf.markers.min.js"></script>""",
            """<script src="./src/leaflet-dvf/leaflet-dvf.markers.min.js"></script>""",
        ],
    ]

    with (
        open(fileFullName, "r", encoding="utf-8") as f1,
        open(f"{fileFullName}.bak", "w", encoding="utf-8") as f2,
    ):
        for line in f1:
            for itm in replaceContents:
                if itm[0] in line:
                    line = line.replace(itm[0], itm[1])
                    replaceContents.remove(itm)
            f2.write(line)
    os.remove(fileFullName)
    os.rename(f"{fileFullName}.bak", fileFullName)


def createUserLocationMap():
    content = read_db_table(db_path, "user_summary")
    for id in content:
        coors = json.loads(id["coors"])
    # 创建地图对象
    map = folium.Map(
        location=coors,
        zoom_start=7,
        tiles="https://webrd02.is.autonavi.com/appmaptile?lang=zh_en&size=1&scale=1&style=8&x={x}&y={y}&z={z}",
        # tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr="map",
    )
    # 创建标记对象
    marker = folium.Marker(location=coors, icon=folium.Icon(icon="home"))
    # 将标记添加到地图上
    marker.add_to(map)
    # 保存地图为HTML文件
    map.save("location_map.html")
    replace_js_ref("./location_map.html")


if __name__ == "__main__":
    start_time = time.time()
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser()
    parser.add_argument("account", help="输入account")
    # parser.add_argument("password", help="输入password")
    # parser.add_argument("nick_name", help="输入nickName")
    # parser.add_argument("Cookie", help="输入Cookie")
    # parser.add_argument("repo", help="输入repo")
    options = parser.parse_args()

    account = options.account
    # password = options.password
    # nick_name = options.nick_name
    # Cookie = options.Cookie
    # repo = options.repo

    userUrl = f"https://www.postcrossing.com/user/{account}"
    galleryUrl = f"{userUrl}/gallery"  # 设置该账号的展示墙
    dataUrl = f"{userUrl}/data/sent"
    types_map = ["sent", "received"]

    headers = {
        "authority": "www.postcrossing.com",
        "Cookie": Cookie,
    }

    if not os.path.exists("./location_map.html"):
        createUserLocationMap()
    new_sent_id = get_update_id(account, "sent")
    new_received_id = get_update_id(account, "received")

    if db_update:
        print(f"{db_path} 有更新")
        create_map()
        print("map.html已生成!")
        create_cluster_map()
        print("cluster_map.html已生成!")
    else:
        print(f"{db_path} 暂无更新")
        print("map.html 暂无更新")
        print("cluster_map.html 暂无更新")

    # 重置db_update初始状态
    with open("scripts/config.json", "r") as f:
        config_data = json.load(f)
        config_data["db_update"] = False
        with open("scripts/config.json", "w") as f:
            json.dump(config_data, f, indent=2)
    end_time = time.time()
    execution_time = round((end_time - start_time), 3)
    print("————————————————————")
    print(f"scripts/create_map.py脚本执行时间：{execution_time}秒")
