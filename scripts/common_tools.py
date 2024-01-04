import requests
import json
import sqlite3
import os
import hashlib
import sys
import argparse
from urllib import parse,request
import pytz
from datetime import datetime, timedelta

with open("scripts/config.json", "r") as file:
    data = json.load(file)
# account = data["account"]
# nickName = data["nickName"]
Cookie = data["Cookie"]
picDriverPath = data["picDriverPath"]
dbpath = data["dbpath"]



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
                select_type = "received" if type == "sent" else "sent"
                cursor.execute(f'''SELECT
                                    g.id,
                                    g.userInfo,
                                    (SELECT countryNameEmoji FROM Galleryinfo WHERE id = g.id AND (type = 'sent' or type = 'received')) AS countryNameEmoji,
                                    g.picFileName,
                                    g.favoritesNum,
                                    g.type,
                                    m.travel_days,
                                    m.sentDate,
                                    m.sentAddr,
                                    m.sentCountry,
                                    m.sentDate_local,
                                    m.receivedAddr,
                                    m.receivedCountry,
                                    m.receivedDate,
                                    m.receivedDate_local,
                                    m.distance,
                                    m.FromCoor,
                                    m.ToCoor 
                                FROM
                                    Galleryinfo g
                                    LEFT JOIN Mapinfo m ON g.id = m.id
                                    
                                WHERE
                                    g.type = ?
                                ORDER BY
                                    receivedDate DESC
                ''', (type,))
            elif tablename == 'Mapinfo':
                select_type = "received" if type == "sent" else "sent"
                cursor.execute(f'''
                SELECT
                    m.*,
                    c.flagEmoji 
                FROM
                    Mapinfo m
                    INNER JOIN CountryStats c ON c.name = m.{select_type}Country 
                WHERE
                    m.type = ?
                ORDER BY
                    SUBSTR( id, 1, 2 ),
                    CAST ( SUBSTR( id, INSTR ( id, '-' ) + 1 ) AS INTEGER ) DESC
                ''', (type,))
            elif tablename == 'postcardStory':
                select_type = "received" if type == "sent" else "sent"
                cursor.execute(f'''SELECT
                    p.id,
                    p.content_original,
                    p.content_cn,
                    p.comment_original,
                    p.comment_cn,
                    m.user AS userInfo,
                    REPLACE(m.link, 'gallery/picture/', '') AS picFileName,
                    c.flagEmoji AS countryNameEmoji,
                    m.type,
                    m.travel_days,
                    m.sentDate,
                    m.sentAddr,
                    m.sentCountry,
                    m.sentDate_local,
                    m.receivedAddr,
                    m.receivedCountry,
                    m.receivedDate,
                    m.receivedDate_local,
                    m.distance,
                    m.FromCoor,
                    m.ToCoor
                    
                FROM
                    postcardStory p
                    LEFT JOIN Mapinfo m ON p.id = m.id
                    LEFT JOIN CountryStats c ON c.name = m.{select_type}Country 
                WHERE
                    m.type = ?         
                ORDER BY
                    receivedDate DESC
            ''', (type,))
            elif tablename == 'CountryStats':
                cursor.execute(f"SELECT * FROM {tablename} ORDER BY name")
            else:
                cursor.execute(f"SELECT * FROM {tablename}")
            rows = cursor.fetchall()
            #print("rows",rows)
            for row in rows:
                if tablename == 'Galleryinfo':
                    data={
                        "id": row[0],
                        "userInfo": row[1],
                        "countryNameEmoji": row[2],
                        "picFileName": row[3],
                        "favoritesNum": row[4],
                        "type": row[5],
                        "travel_days": row[6],
                        "sentDate": row[7],
                        "sentAddr": row[8],
                        "sentCountry": row[9],
                        "sentDate_local": row[10],
                        "receivedAddr": row[11],
                        "receivedCountry": row[12],
                        "receivedDate": row[13],
                        "receivedDate_local": row[14],
                        "distance": row[15],
                        "FromCoor": row[16],
                        "ToCoor": row[17],
                        }
                elif tablename == 'Mapinfo':
                    data={
                        "id": row[0],
                        "FromCoor": json.loads(row[1]),
                        "ToCoor": json.loads(row[2]),
                        "distance": row[3],
                        "travel_days": row[4],
                        "sentDate": row[5],
                        "receivedDate": row[6],
                        "link": row[7],
                        "user":row[8],
                        "sentAddr": row[9],
                        "sentCountry": row[10],
                        "receivedAddr": row[11],
                        "receivedCountry": row[12],
                        "sentDate_local": row[13],
                        "receivedDate_local": row[14],
                        "type": row[15],
                        "flagEmoji": row[16],
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
                        "content_original": row[1],
                        "content_cn": row[2],
                        "comment_original": row[3],
                        "comment_cn": row[4],
                        "userInfo": row[5],
                        "picFileName": row[6],
                        "countryNameEmoji":row[7],
                        "travel_days": row[9],
                        "sentDate": row[10],
                        "sentAddr": row[11],
                        "sentCountry": row[12],
                        "sentDate_local": row[13],
                        "receivedAddr": row[14],
                        "receivedCountry": row[15],
                        "receivedDate": row[16],
                        "receivedDate_local": row[17],
                        "distance": row[18],
                        "FromCoor": row[19],
                        "ToCoor": row[20],
                    }
                elif tablename == 'userSummary':
                    data={
                        "about": row[0],
                        "coors": row[1],
                        "sentDistance": row[2],
                        "sentLaps": row[3],
                        "sentPostcardNum": row[4],
                        "receivedDistance": row[5],
                        "receivedLaps": row[6],
                        "receivedPostcardNum":row[7],
                        "registerd_years": row[8],
                        "registerd_days": row[9],
                        "register_date": row[10],
                        "logo": row[11],
                        
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
                    (id TEXT, userInfo TEXT, countryNameEmoji TEXT, picFileName TEXT, favoritesNum TEXT, type TEXT)''')
        for item in content:
            id = item['id']
            userInfo = item['userInfo']
            countryNameEmoji = item['countryNameEmoji']
            picFileName = item['picFileName']
            favoritesNum = item['favoritesNum']
            type = item['type']
            cursor.execute(f"SELECT * FROM {tablename} WHERE id=? AND type=?", (id, type))
            existing_data = cursor.fetchone()
            if existing_data:
                # 更新已存在的行的其他列数据
                cursor.execute(f"UPDATE {tablename} SET userInfo=?, countryNameEmoji=?, picFileName=?, favoritesNum=? WHERE id=? AND type=?",
                                (userInfo, countryNameEmoji, picFileName, favoritesNum,  id, type))
            else:
                # 插入新的行
                cursor.execute(f"INSERT OR REPLACE INTO {tablename} VALUES (?, ?, ?, ?, ?, ?)",
                                (id, userInfo, countryNameEmoji, picFileName, favoritesNum, type))
    elif tablename == 'Mapinfo':
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
                    (id TEXT PRIMARY KEY, FromCoor TEXT, ToCoor TEXT, distance INTEGER, travel_days TEXT, sentDate TEXT, receivedDate TEXT, link TEXT, user TEXT, sentAddr TEXT, sentCountry TEXT, receivedAddr TEXT, receivedCountry TEXT, sentDate_local TEXT, receivedDate_local TEXT, type TEXT)''')
        for item in content:
            id = item['id']
            FromCoor = json.dumps(item['FromCoor'])
            ToCoor = json.dumps(item['ToCoor'])
            distance = item['distance']
            travel_days = item['travel_days']
            sentDate = item['sentDate']
            receivedDate = item['receivedDate']
            link = item['link']
            user = item['user']
            sentAddr = item['sentAddr']
            sentCountry = item['sentCountry'] 
            receivedAddr = item['receivedAddr']
            receivedCountry = item['receivedCountry']
            sentDate_local = item['sentDate_local']
            receivedDate_local = item['receivedDate_local']
            type = item['type']    

            cursor.execute(f"INSERT OR REPLACE INTO {tablename} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (id, FromCoor, ToCoor, distance, travel_days, sentDate, receivedDate, link, user, sentAddr, sentCountry, receivedAddr, receivedCountry, sentDate_local, receivedDate_local, type))
    # 将列表中的JSON对象写入文件      
    elif tablename == 'postcardStory':
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
                    (id TEXT, content_original TEXT, content_cn TEXT, comment_original TEXT, comment_cn TEXT)''')
        for item in content:
            id = item['id']
            content_original = item['content_original']
            content_cn = item['content_cn']
            comment_original = item['comment_original']
            comment_cn = item['comment_cn']
            cursor.execute(f"SELECT * FROM {tablename} WHERE id=? ", (id, ))
            existing_data = cursor.fetchone()
            if existing_data:
                # 更新已存在的行的其他列数据
                cursor.execute(f"UPDATE {tablename} SET content_original=?, content_cn=?,comment_original=?, comment_cn=?  WHERE id=?",
                                (content_original, content_cn,comment_original, comment_cn, id))
            else:
                # 插入新的行
                cursor.execute(f"INSERT OR REPLACE INTO {tablename} VALUES (?, ?, ?, ?, ?)",
                                (id, content_original, content_cn, comment_original, comment_cn ))
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
    elif tablename == 'userSummary':
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
    (about TEXT, coors TEXT, sentDistance TEXT, sentLaps TEXT, sentPostcardNum TEXT, receivedDistance TEXT, receivedLaps TEXT, receivedPostcardNum TEXT, registerd_years TEXT, registerd_days TEXT, register_date TEXT)''')
        for item in content:
            about = item['about']
            coors = item['coors']
            sentDistance = item['sentDistance']
            sentLaps = item['sentLaps']
            sentPostcardNum = item['sentPostcardNum']
            receivedDistance = item['receivedDistance']
            receivedLaps = item['receivedLaps']
            receivedPostcardNum = item['receivedPostcardNum']
            registerd_years = item['registerd_years']
            registerd_days = item['registerd_days']
            register_date = item['register_date']
            logo = item['logo']
            cursor.execute(f"SELECT * FROM {tablename} ")
            existing_data = cursor.fetchone()
            if existing_data:
                # 更新已存在的行的其他列数据
                cursor.execute(f"UPDATE {tablename} SET about=?, coors=?, sentDistance=?, sentLaps=?, sentPostcardNum=?, receivedDistance=?, receivedLaps=?, receivedPostcardNum=?, registerd_years=?, registerd_days=?, register_date=?, logo=? ", (about, coors, sentDistance, sentLaps, sentPostcardNum, receivedDistance, receivedLaps, receivedPostcardNum,registerd_years ,registerd_days, register_date,logo))
            else:
                # 插入新的行
                cursor.execute(f"INSERT OR REPLACE INTO {tablename} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (about, coors, sentDistance, sentLaps, sentPostcardNum, receivedDistance, receivedLaps, receivedPostcardNum,registerd_years ,registerd_days, register_date,logo))


    print(f'已更新数据库{dbpath}的{tablename}\n')
    conn.commit()
    conn.close()

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
    #print(f"\n{pathA}:{A_md5}\n{pathB}:{B_md5}")
    return stat


def translate(apikey, sentence, src_lan, tgt_lan):
    url = 'http://api.niutrans.com/NiuTransServer/translation?'
    data = {"from": src_lan, "to": tgt_lan, "apikey": apikey, "src_text": sentence.encode("utf-8")}
    data_en = parse.urlencode(data)
    req = url + "&" + data_en
    res = request.urlopen(req)
    res_dict = json.loads(res.read())
    if "tgt_text" in res_dict:
        result = res_dict['tgt_text']
    else:
        result = res
    return result

def get_country_city(latitude, longitude, timestamp):
    
    url=f"https://timezones.datasette.io/timezones/by_point.json?longitude={longitude}&latitude={latitude}"
    response = requests.get(url = url)
    if response:
        country_city = response.json()['rows'][0][0]
    return country_city
    

def get_local_date(coors, utc_date):
    latitude = coors[0]
    longitude = coors[1]
    time_utc = datetime.strptime(utc_date, "%Y/%m/%d %H:%M")
    timestamp = int(time_utc.timestamp())
    country_city = get_country_city(latitude, longitude, timestamp)
    # 根据国家城市英文名称获取对应的时区
    try:
        timezone = pytz.timezone(country_city)
    except pytz.UnknownTimeZoneError:
        return "Invalid country city"

    # 将输入的UTC日期转换为datetime对象
    input_format = "%Y/%m/%d %H:%M"
    utc_datetime = datetime.strptime(utc_date, input_format)

    # 将UTC时间转换为指定时区的本地时间
    local_datetime = pytz.utc.localize(utc_datetime).astimezone(timezone)

    # 提取本地日期
    local_date = local_datetime.date()
    # 格式化本地日期和时间
    output_format = "%Y/%m/%d %H:%M"
    local_datetime_str = local_datetime.strftime(output_format)

    return local_datetime_str


if __name__ == "__main__":
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
    url = f"https://www.postcrossing.com/user/{account}/gallery"  
    userUrl = f"https://www.postcrossing.com/user/{account}"  
    galleryUrl = f"{userUrl}/gallery"  # 设置该账号的展示墙
    dataUrl = f"{userUrl}/data/sent"  
    types_map = ['sent', 'received']  



    headers = {
        'authority': 'www.postcrossing.com',
        'Cookie': Cookie,
        
        }
