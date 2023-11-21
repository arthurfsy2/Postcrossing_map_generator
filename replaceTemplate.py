import multiDownload as dl
import pandas as pd
import sqlite3
import json
import os
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
    table_header1 = "| 序号 | 国家 | 已寄出 | 已收到 | 寄出-平均 | 收到-平均 | 寄出-中间值 | 收到-中间值 \n"
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
    title_all=""
    desc_all=""      
    
    for type in types: 
        distance_all,num = dl.getUserHomeInfo(type)
        if type == "sent":
            desc = f"寄出总数：**{num}**  寄出总距离：**{distance_all}** km\n"
        elif type == "received":
            desc = f"收到总数：**{num}**  收到总距离：**{distance_all}** km\n"
        else:
            desc =""
        desc_all += desc
    print("desc_all：",desc_all)
    for type in types:        
        title = replateTitle(type)
        title_all += f"#### [{title}](/{nickName}/postcrossing/{type})\n\n"
        title_final = f"{desc_all}\n{title_all}"
    #print("title_all:\n",title_all)
    sheet = getUserSheet()
    list = getCardStoryList()
    with open(f"./template/信息汇总_template.md", "r",encoding="utf-8") as f:
        data = f.read()  
        dataNew = data.replace('//请替换明信片墙title',title_final)
        print("已替换明信片墙title")
        dataNew = dataNew.replace('//请替换明信片表格',sheet)
        print("已替换明信片表格")
        dataNew = dataNew.replace('//请替换明信片故事list',list)
        print("已替换明信片故事list")

    with open(f"./output/信息汇总.md", "w",encoding="utf-8") as f:
        f.write(dataNew)  

    blog_path = r"D:\web\Blog2\src\Arthur\Postcrossing\信息汇总.md"
    
    # 换为你的blog的本地链接，可自动同步过去
    if os.path.exists(blog_path):
        print("路径状态：",os.path.exists(blog_path))
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(dataNew)

def getStoryContent(excel_file):
    # 读取Excel文件
    df = pd.read_excel(excel_file)
    # 连接到数据库
    conn = sqlite3.connect(dbpath)
    # 将数据写入数据库
    df.to_sql('postcardStory', conn, if_exists='replace', index=False)




def getCardStoryList():
    content =dl.readDB(dbpath, "","postcardStory")
    list_all = ""
    for id in content:
        postcardID = id["id"]  
        content_cn = id["content_cn"]
        content_en = id["content_en"]
        userInfo = id["userInfo"]
        picFileName = id["picFileName"]
        contryNameEmoji = id["contryNameEmoji"] if id["contryNameEmoji"] is not None else ""
        travel_time = id["travel_time"]
        distance = id["distance"]
        onlinelink ="https://s3.amazonaws.com/static2.postcrossing.com/postcard/medium"
        storypicLink = "https://pan.4a1801.life/d/Onedrive-4A1801/%E4%B8%AA%E4%BA%BA%E5%BB%BA%E7%AB%99/public/Postcrossing/content"

        list = f'### [{postcardID}](https://www.postcrossing.com/postcards/{postcardID})\n\n' \
          f'> 来自 {userInfo} {contryNameEmoji}\n' \
          f'> 📏{distance} km\n⏱{travel_time}\n\n' \
          f'<div class="image-preview">  <img src="{onlinelink}/{picFileName}" />' \
          f'  <img src="{storypicLink}/{postcardID}.webp" /></div>' \
          f'\n\n' \
          f'::: info 内容\n{content_en}\n:::\n\n' \
          f'::: tip 翻译\n{content_cn}\n:::\n\n'       
        list_all +=list
    return list_all



dl.replaceTemplateCheck()
excel_file="./template/postcardStory.xlsx"
getStoryContent(excel_file)
replaceTemplate()

# getCardStoryList()