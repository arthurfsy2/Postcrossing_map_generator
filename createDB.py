import json
import sqlite3

dbpath = './template/test.db'

def getMapinfo(type, tablename):
    # 读取sent_Mapinfo.json文件
    with open(f'./output/{type}_Mapinfo.json', 'r') as f:
        data = json.load(f)

    # 连接到数据库test.db
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    # 创建新的Mapinfo表（如果不存在）
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
                    (id TEXT PRIMARY KEY, FromCoor TEXT, ToCoor TEXT, distance INTEGER, travel_time TEXT, link TEXT, user TEXT, sentAddr TEXT, receivedAddr TEXT, type TEXT)''')

    # 将sent_Mapinfo.json中的内容写入Mapinfo表
    for item in data:
        id = item['id']
        FromCoor = json.dumps(item['From'])
        ToCoor = json.dumps(item['To'])
        distance = item['distance']
        travel_time = item['travel_time']
        link = item['link']
        user = item['user']
        sentAddr = item['sentAddr']
        receivedAddr = item['receivedAddr']
        type = type
        
        cursor.execute(f"INSERT OR REPLACE INTO {tablename} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (id, FromCoor, ToCoor, distance, travel_time, link, user, sentAddr, receivedAddr, type))
    print(f'已将./output/{type}_Mapinfo.json写入数据库')
    conn.commit()
    conn.close()


import datetime

def getGalleryinfo(type, tablename):
    # 读取sent_Mapinfo.json文件
    with open(f'./output/{type}.json', 'r') as f:
        data = json.load(f)

    # 连接到数据库test.db
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
                    (id TEXT, userInfo TEXT, contryNameEmoji TEXT, picFileName TEXT, favoritesNum TEXT, type TEXT, createTime TEXT)''')

    # 获取当前时间
    current_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    # 将sent_Mapinfo.json中的内容写入Mapinfo表
    for item in data:
        
        id = item['id']
        userInfo = item.get('userInfo', '')
        contryNameEmoji = item.get('contryNameEmoji', '')
        picFileName = item['picFileName']
        favoritesNum = item.get('favoritesNum', '')
        type = type

        # 检查是否已存在相同的id和type
        cursor.execute(f"SELECT * FROM {tablename} WHERE id=? AND type=?", (id, type))
        existing_data = cursor.fetchone()

        if existing_data:
            # 更新已存在的行的其他列数据
            cursor.execute(f"UPDATE {tablename} SET userInfo=?, contryNameEmoji=?, picFileName=?, favoritesNum=? WHERE id=? AND type=?",
                            (userInfo, contryNameEmoji, picFileName, favoritesNum, id, type))
        else:
            # 插入新的行
            cursor.execute(f"INSERT INTO {tablename} VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (id, userInfo, contryNameEmoji, picFileName, favoritesNum, type, current_time))

    print(f'已将./output/{type}.json写入数据库')
    conn.commit()
    conn.close()

def getCountryStats(tablename):
    # 读取sent_Mapinfo.json文件
    with open(f'./output/stats.json', 'r') as f:
        data = json.load(f)

    # 连接到数据库test.db
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    # 创建新的Mapinfo表（如果不存在）
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
                    (name TEXT, flagEmoji TEXT, value INTEGER, sentNum INTEGER, receivedNum INTEGER, sentAvg INTEGER, receivedAvg INTEGER)''')

    # 将sent_Mapinfo.json中的内容写入Mapinfo表
    for item in data:
        name = item['name']
        flagEmoji = item['flagEmoji']
        value = item['value']
        sentNum = item['sentNum']
        receivedNum = item['receivedNum']
        sentAvg = item['sentAvg']
        receivedAvg = item['receivedAvg']
        
        cursor.execute(f"INSERT OR REPLACE INTO {tablename} VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (name, flagEmoji, value, sentNum, receivedNum, sentAvg, receivedAvg))
    print(f'已将./output/stats.json写入数据库')
    conn.commit()
    conn.close()


types_map = ['sent', 'received']

for type in types_map:
    getMapinfo(type, "Mapinfo")

types = ['sent', 'received', 'favourites', 'popular']
for type in types:
    getGalleryinfo(type, "Galleryinfo")

getCountryStats("CountryStats")

