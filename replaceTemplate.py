import multiDownload as dl
import pandas as pd
import sqlite3
import json
from translate import Translator
from urllib import parse,request

with open("config.json", "r") as file:
    data = json.load(file)
account = data["account"]
nickName = data["nickName"]
Cookie = data["Cookie"]
picDriverPath = data["picDriverPath"]
dbpath = data["dbpath"]


def translate(sentence, src_lan, tgt_lan):
    apikey="da3f6df96672f9693e76ed14dd54f884"
    url = 'http://api.niutrans.com/NiuTransServer/translation?'
    data = {"from": src_lan, "to": tgt_lan, "apikey": apikey, "src_text": sentence}
    data_en = parse.urlencode(data)
    req = url + "&" + data_en
    res = request.urlopen(req)
    res_dict = json.loads(res.read())
    if "tgt_text" in res_dict:
        result = res_dict['tgt_text']
    else:
        result = res
    return result

def replateTitle(type):    
    
    with open(f"./output/title.json", "r",encoding="utf-8") as f:
        title = json.load(f)
    value = title.get(type)
    from_or_to, pageNum, Num, title = value
    return title

def getUserSheet():
    stats_data=dl.readDB(dbpath, "", "CountryStats")
    # 按照 name 的 A-Z 字母顺序对 stats_data 进行排序
    sorted_stats_data = sorted(stats_data, key=lambda x: x['name'])
    #print("sorted_stats_data",sorted_stats_data)
    # 创建表头
    #table_header = "| No. | Country | Sent | Received | Avg travel(Sent) | Avg travel(Received) |\n"
    table_header1 = "| 序号 | 国家 | 已寄出 | 已收到 | 寄出天数-平均 | 收到天数-平均 | 寄出天数-中间值 | 收到天数-中间值 \n"
    table_header2 = "| --- | --- | --- | --- | --- | --- | --- | --- \n"

    # 创建表格内容
    table_content = ""
    for i, stats in enumerate(sorted_stats_data, start=1):
        country = stats['name']
        flag = stats['flagEmoji']
        sent = stats['sentNum']
        received = stats['receivedNum']
        sentAvg = stats['sentAvg']
        receivedAvg = stats['receivedAvg']
        sentMedian = stats['sentMedian']
        receivedMedian = stats['receivedMedian']
        if sent ==0:
            sentAvgDays = "-"
            sentMedianDays = "-"
        else:
            sentAvgDays = f"{sentAvg}天"
            sentMedianDays = f"{sentMedian}天"

        if received ==0:
            receivedAvgDays = "-"
            receivedMedianDays = "-"
        else:
            receivedAvgDays = f"{receivedAvg}天"
            receivedMedianDays = f"{receivedMedian}天"

        
        table_content += f"| {i} | {country} {flag} | {sent} | {received} | {sentAvgDays} | {receivedAvgDays} | {sentMedianDays} | {receivedMedianDays} \n"

    # 将表头和表格内容合并
    table = table_header1 + table_header2 + table_content
    return table

def replaceTemplate():
    stat,content_raw,types = dl.getAccountStat()     
    #getUserSheet()       
    title_all=""
    for type in types:        
        title = replateTitle(type)
        #print("title:",title)
        title_all += f"#### [{title}]({nickName}/postcrossing/{type})\n\n"
    #print("title_all:\n",title_all)
    sheet = getUserSheet()
    list = getCardStoryList()
    with open(f"./template/信息汇总_template.md", "r",encoding="utf-8") as f:
        data = f.read()  
        dataNew = data.replace('//请替换明信片墙title',title_all)
        print("已替换明信片墙title")
        dataNew = dataNew.replace('//请替换明信片表格',sheet)
        print("已替换明信片表格")
        dataNew = dataNew.replace('//请替换明信片故事list',list)
        print("已替换明信片故事list")

    with open(f"./output/信息汇总.md", "w",encoding="utf-8") as f:
        f.write(dataNew)  

def getStoryContent(excel_file):
    # 读取Excel文件
    df = pd.read_excel(excel_file)
    # 连接到数据库
    conn = sqlite3.connect(dbpath)
    # 将数据写入数据库
    df.to_sql('postcardStory', conn, if_exists='replace', index=False)




def getCardStoryList():
    # 连接到test.db数据库
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    # 查询postcardStory表和Galleryinfo表，并通过id字段进行连接查询
    cursor.execute('''SELECT
	p.id,
	p.content_cn,
	p.content_en,
	g.userInfo,
	g.picFileName,
	g.contryNameEmoji,
	g.type,
	m.travel_time,
	date( REPLACE ( SUBSTR( m.travel_time, 22, 10 ), '/', '-' ) ) AS receivedDate
	
FROM
	postcardStory p
	INNER JOIN Galleryinfo g ON p.id = g.id
	INNER JOIN Mapinfo m ON p.id = m.id
	ORDER BY receivedDate DESC''')

    # 将查询结果存储到content列表中
    content = cursor.fetchall()
    #print(f"content:\n",content)
    # 关闭数据库连接
    conn.close()
    list_all = ""
    for row in content:
        onlinelink ="https://s3.amazonaws.com/static2.postcrossing.com/postcard/medium"
        storypicLink = "https://pan.4a1801.life/d/Onedrive-4A1801/%E4%B8%AA%E4%BA%BA%E5%BB%BA%E7%AB%99/public/Postcrossing/content"
        #translator = Translator(to_lang="zh")
        translation = translate(row[2], 'auto', 'zh')
        #translation = translator.translate(row[2])
        list = f'### [{row[0]}](https://www.postcrossing.com/postcards/{row[0]})\n\n' \
          f'> 来自 {row[3]} {row[5]}\n\n' \
          f'<div class="image-preview">  <img src="{onlinelink}/{row[4]}" />' \
          f'  <img src="{storypicLink}/{row[0]}.webp" /></div>' \
          f'\n\n' \
          f'::: info 内容\n{row[2]}\n:::\n\n' \
          f'::: tip 翻译\n{translation}\n:::\n\n'       
        list_all +=list   
    return list_all

dl.replaceTemplateCheck()
excel_file="./template/postcardStory.xlsx"
getStoryContent(excel_file)
replaceTemplate()

# getCardStoryList()