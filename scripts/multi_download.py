import json
import re
import requests
from bs4 import BeautifulSoup
import threading
import os
import json
import pandas as pd
import math
from datetime import datetime, timedelta, timezone
import sys
import sqlite3
import statistics
import pycountry
from emojiflags.lookup import lookup as flag
import hashlib
import argparse
from common_tools import (
    db_path,
    read_db_table,
    insert_or_update_db,
    initialize_database,
    get_local_date,
)


with open("scripts/config.json", "r") as file:
    data = json.load(file)
# account = data["account"]
# nick_name = data["nick_name"]
Cookie = data["Cookie"]
pic_driver_path = data["pic_driver_path"]
BIN = os.path.dirname(os.path.realpath(__file__))


def getAccountStat(account, Cookie):
    """
    获取账号状态
    """
    headers = {
        "authority": "www.postcrossing.com",
        "Cookie": Cookie,
    }
    userUrl = f"https://www.postcrossing.com/user/{account}"
    galleryUrl = f"{userUrl}/gallery"  # 设置该账号的展示墙
    dataUrl = f"{userUrl}/data/sent"
    galleryResponse = requests.get(galleryUrl, headers=headers)
    galleryStatus = galleryResponse.status_code
    galleryContent = galleryResponse.text.replace('"//', '"https://')

    dataResponse = requests.get(dataUrl, headers=headers)
    dataContent = dataResponse.text
    if "Log in to see this content" in dataContent:
        cookieStat = 404
    else:
        cookieStat = 200
    if galleryStatus == 200 and cookieStat == 200:
        totalStat = "getPrivate"
        types = ["sent", "received", "favourites", "popular"]
        print(f"{account}的Cookies有效，可访问个人账号内容……\n")
    elif galleryStatus == 200 and cookieStat == 404:
        totalStat = "getPublic"
        types = ["sent", "received"]
        print(f"{account}的Cookies无效，正在尝试重新登陆……\n")
    elif galleryStatus != 200:
        totalStat = "unAccessible"
        print(f"用户:{account}已注销/设置为非公开，无法获取！\n")
        sys.exit()

    return totalStat, galleryContent, types


def get_page_num(stat, content, types):
    if stat == "getPrivate":
        return
    for card_type in types:
        from_or_to = "来自" if card_type in ["received", "favourites"] else "寄往"
        title_key = {
            "received": "收到",
            "sent": "寄出",
            "favourites": "我的点赞",
            "popular": "我收到的赞",
        }
        if card_type == "favourites":
            pattern = r"Favorites \((\d+)\)"
        else:
            pattern = r"{} \((\d+)\)"
        # 获取数量
        content_pattern = pattern.format(card_type.capitalize())
        content_match = re.search(content_pattern, content)
        count = int(content_match.group(1)) if content_match else 0
        # 获取页数
        page_num = math.ceil(count / 60)
        item = {
            "card_type": card_type,
            "from_or_to": from_or_to,
            "page_num": page_num,
            "card_num": count,
            "title_name": f"明信片展示墙（{title_key.get(card_type)}：{count}）",
        }

        insert_or_update_db(db_path, "title_info", item)


# 获取不同类型的展示墙的详细信息，并组装数据


def get_gallery_info(type, account, Cookie):
    headers = {
        "authority": "www.postcrossing.com",
        "Cookie": Cookie,
    }
    userUrl = f"https://www.postcrossing.com/user/{account}"
    galleryUrl = f"{userUrl}/gallery"  # 设置该账号的展示墙
    title_info_data = read_db_table(db_path, "title_info", {"card_type": type})
    page_num = int(title_info_data[0].get("page_num"))
    i = 1

    while i <= page_num:
        all_url = f"{galleryUrl}/{type}/{i}"
        print(f"正在获取/gallery/{type}({i}/{page_num})")
        response = requests.get(all_url, headers=headers)

        content_i = response.text.replace('"//', '"https://')
        soup = BeautifulSoup(content_i, "html.parser")
        lis = soup.find_all("li")
        # 获取每个postcard信息
        for li in lis:
            figure = li.find("figure")
            figcaption = li.find("figcaption")
            if figure:
                href = figure.find("a")["href"]
                # print(f"href:{href}")
                postcardID = figcaption.find("a").text
                baseUrl = "https://www.postcrossing.com/"
                pic_file_name = re.search(r"/([^/]+)$", href).group(1)
                favorites_num = "0"
                if type == "popular":
                    favorites_num = figcaption.find("div").text
                    favorites_num = re.search(r"\d+", favorites_num).group()
                    user_info = ""
                    country_name_emoji = ""
                else:
                    user = figcaption.find("div").find("a").text
                    user_info = f"[{user}]({baseUrl}user/{user})"
                    if not user:
                        user_info = "***该用户已关闭***"
                    code = re.search(r'href="/country/(.*?)"', str(figcaption)).group(1)
                    country_name_emoji = flag(code)

                item = {
                    "card_id": postcardID,
                    "user_info": user_info,
                    "country_name_emoji": country_name_emoji,
                    "pic_file_name": pic_file_name,
                    "favorites_num": favorites_num,
                    "card_type": type,
                }

                insert_or_update_db(db_path, "gallery_info", item)

        i += 1
    print("————————————————————")


# 读取本地已下载图片的文件名列表
def getLocalPic():
    localPicList = []
    picPath = "./gallery/picture"
    for root, dirs, files in os.walk(picPath):
        for file in files:
            localPicList.append(file)
    return localPicList


# 实时获取该账号所有sent、received的明信片列表，获取每个postcardID的详细数据
def getUpdateID(account, type, Cookie):
    headers = {
        "Host": "www.postcrossing.com",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Fetch-Site": "same-origin",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Sec-Fetch-Mode": "cors",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0.1 Mobile/15E148 Safari/604.1",
        "Connection": "keep-alive",
        "Referer": f"https://www.postcrossing.com/user/{account}/{type}",
        "Cookie": Cookie,
        "Sec-Fetch-Dest": "empty",
    }
    url = f"https://www.postcrossing.com/user/{account}/data/{type}"
    response = requests.get(url, headers=headers).json()
    with open(f"./data/{type}.json", "w") as f:
        json.dump(response, f, indent=2)
    onlineID = [item[0] for item in response]
    hasPicID = [item[0] for item in response if item[-1] == 1]
    # print(f"onlineID({len(onlineID)}):{onlineID}")
    # print(f"hasPicID({len(hasPicID)}):{hasPicID}")

    local_data = read_db_table(db_path, "map_info")
    old_id = [item.get("card_id") for item in local_data]

    if old_id:

        newID = []
        # 遍历onlineID中的元素
        for id in onlineID:
            # 如果id不在oldID中，则将其添加到newID中
            if id not in old_id:
                newID.append(id)
        if len(newID) == 0:
            print(f"数据库{db_path}：Mapinfo_{type}暂无更新内容\n")
            updateID = None
        else:
            print(f"{type}_等待更新Mapinfo({len(newID)}个):{newID}\n")
            updateID = newID
    else:
        # 当本地文件不存在时，则取online的postcardId作为待下载列表
        updateID = onlineID

    return updateID


# 获取日期


def convert_to_utc(zoneNum, type, time_str):
    # 使用正则表达式提取时间部分
    pattern = rf"{type} on (\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}})"
    # print("pattern:",pattern)
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
    time_utc_str = time_utc.strftime(f"%Y/%m/%d %H:%M")
    return time_utc_str


def get_map_info_data(postcardID, type):

    for i, id in enumerate(postcardID):

        url = f"https://www.postcrossing.com/postcards/{id}"
        response = requests.get(url)
        pattern = r"var senderLocation\s+=\s+new L.LatLng\(([-\d.]+), ([-\d.]+)\);\s+var receiverLocation\s+=\s+new L.LatLng\(([-\d.]+), ([-\d.]+)\);"
        matches = re.findall(pattern, response.text)  # 提取发送、接收的经纬度坐标

        # 提取距离、发送/到达时间、历经天数
        distance = int(
            re.search(r"traveled (.*?) km", response.text).group(1).replace(",", "")
        )
        travel_days = int(re.search(r"in (.*?) days", response.text).group(1))
        sentDate = convert_to_utc(0, "Sent", response.text)
        receivedDate = convert_to_utc(0, "Received", response.text)
        travel_time = f"{travel_days} days [{sentDate}--{receivedDate}]"
        # print(f"{id}_travel_time:{travel_time}")
        # 提取发送者/接受者user
        userPattern = r'<a itemprop="url" href="/user/(.*?)"'
        userResults = re.findall(userPattern, response.text)
        # print(f"{id}_userResults:{userResults}]")

        # 提取链接link
        link = re.search(
            r'<meta property="og:image" content="(.*?)" />', response.text
        ).group(1)
        if "logo" in link:
            link = "gallery/picture/noPic.png"  # 替换图片为空时的logo
        else:
            pic_file_name = re.search(r"/([^/]+)$", link).group(1)
            # print(f"{id}_picFileName:{pic_file_name}")
            link = f"gallery/picture/{pic_file_name}"

        # 提取地址信息
        addrPattern = r'<a itemprop="addressCountry" title="(.*?)" href="/country/(.*?)">(.*?)</a>'
        addrResults = re.findall(addrPattern, response.text)
        # print(f"{id}_addrResults:", addrResults)

        sentAddrInfo = addrResults[0]
        receivedInfo = addrResults[1]

        sentAddr = sentAddrInfo[0]
        sentCountry = sentAddrInfo[2]
        receivedAddr = receivedInfo[0]
        receivedCountry = receivedInfo[2]

        # 提取发送/接收user
        userPattern = r'<a itemprop="url" href="/user/(.*?)"'
        userResults = re.findall(userPattern, response.text)
        # print(f"{id}_userResults:{userResults}")
        if len(userResults) == 1:
            user = "account closed"
        elif len(userResults) >= 2 and type == "sent":
            user = userResults[1]

        elif len(userResults) >= 2 and type == "received":
            user = userResults[0]
        # print(f"User:{user}")

        for match in matches:

            # 将拼接后的坐标字符串转换为浮点数
            from_coord = json.dumps([float(match[0]), float(match[1])])
            to_coord = json.dumps([float(match[2]), float(match[3])])

        item = {
            "card_id": id,
            "from_coor": from_coord,
            "to_coor": to_coord,
            "distance": distance,
            "travel_days": travel_days,
            "sent_date": sentDate,
            "received_date": receivedDate,
            "link": link,
            "user": user,
            "sent_addr": sentAddr,
            "sent_country": sentCountry,
            "received_addr": receivedAddr,
            "received_country": receivedCountry,
            "sent_date_local": get_local_date(
                [float(match[0]), float(match[1])], sentDate
            ),
            "received_date_local": get_local_date(
                [float(match[2]), float(match[3])], receivedDate
            ),
            "card_type": type,
        }
        insert_or_update_db(db_path, "map_info", item)
        print(f"{type}_List:已提取{round((i+1)/(len(postcardID))*100,2)}%")


# 下载展示墙的图片


def downloadPic(updatePic, pic_json):
    picFileNameList = []
    for i, pic_file_name in enumerate(updatePic):
        picDownloadPath = (
            f"gallery/picture/{pic_file_name}"  # 替换为你要保存的文件路径和文件名
        )
        if os.path.exists(picDownloadPath):
            # print(f"已存在：{pic_file_name}")
            pass
        else:
            picDownloadUrl = f"https://s3.amazonaws.com/static2.postcrossing.com/postcard/medium/{pic_file_name}"
            # print(f"picDownloadUrl:{picDownloadUrl}")
            response = requests.get(picDownloadUrl)
            print(f"正在下载{pic_file_name}")
            with open(picDownloadPath, "wb") as file:
                file.write(response.content)
    pic_json.append(pic_file_name)


def getUpdatePic(type):
    picFileNameList = []
    content = read_db_table(db_path, "gallery_info")

    # 提取picFileName字段内容
    picFileNameList = [item["pic_file_name"] for item in content]
    # print("picFileNameList:",picFileNameList)
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


def calculateAvgAndMedian(a_data):
    with open("scripts/countryName.json", "r") as f:
        countryName = json.load(f)
    name_dict = {}

    for item in a_data:
        date = item[0]
        code = item[3]
        country = countryName[code]
        flagEmoji = flag(code)
        r_or_s = item[2]
        travel_days = item[1]

        if code not in name_dict:
            name_dict[code] = {
                "name": country,
                "countryCode": code,
                "flagEmoji": flagEmoji,
                "sent": [],
                "received": [],
                "sentDate": [],
                "receivedDate": [],
            }

        if r_or_s == "s":
            name_dict[code]["sent"].append(travel_days)
            name_dict[code]["sentDate"].append(date)
        elif r_or_s == "r":
            name_dict[code]["received"].append(travel_days)
            name_dict[code]["receivedDate"].append(date)
    country_stats = []
    for code, data in name_dict.items():
        if data["sent"]:
            sent_avg = int(statistics.mean(data["sent"]))
            sent_median = int(statistics.median(data["sent"]))
            sentDate_first = datetime.fromtimestamp(
                min(data["sentDate"]), timezone.utc
            ).strftime("%Y/%m/%d")

        else:
            sent_avg = None
            sent_median = None
            sentDate_first = None
        if data["received"]:
            received_avg = int(statistics.mean(data["received"]))
            received_median = int(statistics.median(data["received"]))
            receivedDate_first = datetime.fromtimestamp(
                min(data["receivedDate"]), timezone.utc
            ).strftime("%Y/%m/%d")
        else:
            received_avg = None
            received_median = None
            receivedDate_first = None
        item = {
            "name": data["name"],
            "country_code": data["countryCode"],
            "flag_emoji": flag(data["countryCode"]),
            "value": len(data["sent"]) + len(data["received"]),
            "sent_num": len(data["sent"]),
            "received_num": len(data["received"]),
            "sent_avg": sent_avg,
            "received_avg": received_avg,
            "sent_median": sent_median,
            "received_median": received_median,
            "sent_history": json.dumps(name_dict[code]["sent"]),
            "received_history": json.dumps(name_dict[code]["received"]),
            "sent_date_history": json.dumps(name_dict[code]["sentDate"]),
            "received_date_history": json.dumps(name_dict[code]["receivedDate"]),
            "sent_date_first": sentDate_first,
            "received_date_first": receivedDate_first,
        }
        country_stats.append(item)
        insert_or_update_db(db_path, "country_stats", item)
    return country_stats


def getUserStat(account):
    headers = {
        "Host": "www.postcrossing.com",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Fetch-Site": "same-origin",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Sec-Fetch-Mode": "cors",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0.1 Mobile/15E148 Safari/604.1",
        "Connection": "keep-alive",
        "Referer": f"https://www.postcrossing.com/user/{account}/stats",
        "Cookie": Cookie,
        "Sec-Fetch-Dest": "empty",
    }
    url = f"https://www.postcrossing.com/user/{account}/feed"
    a_data = requests.get(url, headers=headers).json()
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
    year_summary = {}
    # 遍历数据
    for item in a_data:
        # 将时间戳转换为YYYY-MM的格式
        timestamp = item[0]
        date = datetime.fromtimestamp(timestamp, timezone.utc).strftime("%Y-%m")
        year = datetime.fromtimestamp(timestamp, timezone.utc).strftime("%Y")
        # 判断sent还是received
        if item[2] == "s":
            key = "sent"
        elif item[2] == "r":
            key = "received"
        else:
            continue
        # 更新汇总结果
        if date in summary:
            summary[date][key] += 1
        else:
            summary[date] = {"sent": 0, "received": 0}
            summary[date][key] = 1

        if year in year_summary:
            year_summary[year][key] += 1
        else:
            year_summary[year] = {"sent": 0, "received": 0}
            year_summary[year][key] = 1

    # 将汇总结果转换为新的数组
    # result = [{'date': date, 'num': summary[date]} for date in summary]
    result = [
        {
            "date": date,
            "sent": summary[date]["sent"],
            "received": summary[date]["received"],
        }
        for date in summary
    ]
    result_year = [
        {
            "year": year,
            "sent": year_summary[year]["sent"],
            "received": year_summary[year]["received"],
        }
        for year in year_summary
    ]

    # 将结果输出到month.json文件中，以供“信息汇总.md"的收发记录（月度）模块使用
    with open(f"./output/month.json", "w") as f:
        json.dump(result, f, indent=2)

    print(f"已生成output/month.json\n")

    # 将结果输出到year.json文件中，以供“sent/received.md"的收发记录（年度）模块使用
    with open(f"./output/year.json", "w") as f:
        json.dump(result_year, f, indent=2)

    print(f"已生成output/year.json\n")
    calendar = {}
    # 遍历数据列表
    for data in a_data:
        # 将时间戳转换为YYYY-MM-DD格式
        timestamp = data[0]
        date = datetime.fromtimestamp(timestamp, timezone.utc).strftime("%Y-%m-%d")

        # 统计每天的总数
        if date in calendar:
            calendar[date] += 1
        else:
            calendar[date] = 1

    # 将结果转换为列表格式
    calendar_result = [[date, total] for date, total in calendar.items()]

    # 将结果输出到calendar.json文件
    with open("./output/calendar.json", "w") as file:
        json.dump(calendar_result, file, indent=2)

    country_stats = calculateAvgAndMedian(a_data)
    # print("country_stats:\n",country_stats)
    # # 将统计结果写入 b.json 文件
    with open("./output/stats.json", "w", encoding="utf-8") as file:
        json.dump(country_stats, file, indent=2, ensure_ascii=False)
    print(f"已生成./output/stats.json\n")


def multiTask(account, type, Cookie):
    postcardID = getUpdateID(account, type, Cookie)
    if postcardID is not None:
        Num = round(len(postcardID) / 20)
        if Num < 1:
            realNum = 1
        elif Num >= 1 and Num <= 10:
            realNum = Num
        elif Num > 10:  # 最大并发数为10
            realNum = 10
        group_size = len(postcardID) // realNum
        print(
            f"将{type}的postcardID分为{realNum}个线程并行处理，每个线程处理个数：{group_size}\n"
        )
        postcard_groups = [
            postcardID[i : i + group_size]
            for i in range(0, len(postcardID), group_size)
        ]
        # print("postcard_groups:", postcard_groups)
        # 创建线程列表
        threads = []

        # 创建并启动线程
        for i, group in enumerate(postcard_groups):
            thread = threading.Thread(target=get_map_info_data, args=(group, type))
            thread.start()
            threads.append(thread)

        # 等待所有线程完成
        for thread in threads:
            thread.join()

        print(f"{type}的update List已提取完成！\n")
    else:
        pass


# 设置多线程下载图片


def multi_download(type):
    updatePic = getUpdatePic(type)

    if updatePic is not None:
        Num = round(len(updatePic) / 20)
        if Num < 1:
            realNum = 1
        elif Num >= 1 and Num <= 10:
            realNum = Num
        elif Num > 10:  # 最大并发数为10
            realNum = 10
        group_size = len(updatePic) // realNum
        print(
            f"将{type}的postcardID分为{realNum}个线程并行下载，每个线程下载图片个数：{group_size}\n"
        )
        picDownload_groups = [
            updatePic[i : i + group_size] for i in range(0, len(updatePic), group_size)
        ]
        # 创建线程列表
        threads = []
        pic_json = []  # 存储最终的pic_json
        # 创建并启动线程
        for i, group in enumerate(picDownload_groups):
            thread = threading.Thread(target=downloadPic, args=(group, pic_json))
            thread.start()
            threads.append(thread)

        # 等待所有线程完成
        for thread in threads:
            thread.join()

    else:
        print(f"{type}_图库无需更新")
        print("————————————————————")


# 定义create_map.py的前置检查条件
def MapDataCheck(account, Cookie, types_map):
    print("————————————————————")
    for type in types_map:
        multiTask(account, type, Cookie)


# 定义create_gallery.py的前置检查条件


def PicDataCheck(account, Cookie):
    print("————————————————————")
    get_page_num(stat, content_raw, types)
    getUserStat(account)
    for type in types:
        get_gallery_info(type, account, Cookie)  # 获取图库信息
    for type in types:
        multi_download(type)  # 批量下载图片


def getUserSummary(
    account,
    Cookie,
):

    headers = {
        "authority": "www.postcrossing.com",
        "Cookie": Cookie,
    }
    userUrl = f"https://www.postcrossing.com/user/{account}"
    userAboutInfo = requests.get(userUrl, headers=headers)
    html_content = userAboutInfo.text
    is_supporter = "No"
    # 未到期只能判断是否是Supporter
    if "Postcrossing Supporter" in html_content:
        is_supporter = "YES"
    # Supporter快到期可获取到期日期
    match = re.search(r"<strong>(.*?)</strong>", html_content)

    if match:
        if match:
            date_str = match.group(1).strip()  # 提取并清洗数据
            # 移除日期中的后缀（st, nd, rd, th）
            date_str = re.sub(r"(\d+)(st|nd|rd|th)", r"\1", date_str)

            # 定义日期格式并转换
            current_year = datetime.now().year
            date_obj = datetime.strptime(f"{date_str} {current_year}", "%d of %B %Y")
            is_supporter = date_obj.strftime("%Y/%m/%d")

    soup = BeautifulSoup(html_content, "html.parser")
    title = soup.find("title")
    if title.get_text() == "Log in":
        print(f"用户:{account}已注销/设置为非公开，无法获取！\n")
        sys.exit()

    # 提取about信息
    div_about = soup.find("div", class_="about-text")
    if div_about:
        about = div_about.get_text()

    # 提取经纬度信息
    pattern = r"new L.LatLng\(([-\d.]+), ([-\d.]+)\)"
    match = re.search(pattern, html_content)
    if match:
        latitude = match.group(1)
        longitude = match.group(2)
        coors = json.dumps((float(latitude), float(longitude)))

    def getUserSummaryInfo(type):
        # 正则表达式匹配数字和小数
        number_pattern = rf'<a title="(.*?) km \(or (.*?) laps around the world!\)" href="/user/{account}/{type}">(.*?)</a>'

        # 提取数字和小数
        match = re.search(number_pattern, html_content)

        if match:
            distance = match.group(1).replace(",", "")
            laps = match.group(2)
            postcardnum = match.group(3)

        else:
            print("未找到数字和小数")
        return distance, laps, postcardnum

    sent_distance, sent_laps, sent_postcard_num = getUserSummaryInfo("sent")
    received_distance, received_laps, received_postcard_num = getUserSummaryInfo(
        "received"
    )
    logo_link_pattern = r"static2.postcrossing.com/avatars/140x140/(.*?).jpg"
    match = re.search(logo_link_pattern, html_content)
    logo = match.group(1)

    # 获取注册日期
    registerinfo_pattern = r'title="Member for over (.*?) years \((.*?) days\)"'
    matchs = re.search(registerinfo_pattern, html_content)

    registered_years = matchs.group(1)
    registered_days = matchs.group(2).replace(",", "")
    # 获取注册日期
    abbr_tag = soup.select('abbr[title^="Member for"]')

    for tag in abbr_tag:
        content = tag.get_text(strip=True)

    def parse_date_with_suffix(content):
        suffix = re.findall(r"\d+(st|nd|rd|th)", content)[0]  # 提取日期中的后缀部分
        format_string = f"%d{suffix} %b., %Y"  # 提取日期中的数字部分作为后缀
        date_object = datetime.strptime(content, format_string)
        register_date = date_object.strftime("%Y/%m/%d")
        return register_date

    register_date = parse_date_with_suffix(content)
    item = {
        "account": account,
        "about": str(about),
        "coors": coors,
        "sent_distance": sent_distance,
        "sent_laps": sent_laps,
        "sent_postcard_num": sent_postcard_num,
        "received_distance": received_distance,
        "received_laps": received_laps,
        "received_postcard_num": received_postcard_num,
        "registered_years": registered_years,  # 修改拼写错误并使用下划线
        "registered_days": registered_days,  # 修改拼写错误并使用下划线
        "register_date": register_date,
        "logo": logo,
        "is_supporter": is_supporter,
    }
    insert_or_update_db(db_path, "user_summary", item)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("account", help="输入account")
    # parser.add_argument("password", help="输入password")
    parser.add_argument("nick_name", help="输入nickName")
    # parser.add_argument("Cookie", help="输入Cookie")
    # parser.add_argument("repo", help="输入repo")
    options = parser.parse_args()

    account = options.account
    # password = options.password
    nick_name = options.nick_name
    # Cookie = options.Cookie
    # repo = options.repo

    # 获取当前日期
    current_date = datetime.now().date()
    # 将日期格式化为指定格式
    date = current_date.strftime("%Y-%m-%d")
    # 替换为您要获取数据的链接
    url = f"https://www.postcrossing.com/user/{account}/gallery"
    types_map = ["sent", "received"]
    stat, content_raw, types = getAccountStat(account, Cookie)

    getUserSummary(account, Cookie)
    PicDataCheck(account, Cookie)
    MapDataCheck(account, Cookie, types_map)
