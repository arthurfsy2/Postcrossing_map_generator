import multiDownload as dl
import pandas as pd
import sqlite3
import json

with open("config.json", "r") as file:
    data = json.load(file)
account = data["account"]
nickName = data["nickName"]
Cookie = data["Cookie"]
picDriverPath = data["picDriverPath"]

def replateTitle(type):    
    
    with open(f"./output/title.json", "r",encoding="utf-8") as f:
        title = json.load(f)
    value = title.get(type)
    from_or_to, pageNum, Num, title = value
    return title

def getUserSheet():
    # 读取 stats.json 文件并将内容存储在 stats_data 变量中
    with open('./output/stats.json', 'r') as file:
        stats_data = json.load(file)

    # 按照 name 的 A-Z 字母顺序对 stats_data 进行排序
    sorted_stats_data = sorted(stats_data, key=lambda x: x['name'])
    #print("sorted_stats_data",sorted_stats_data)
    # 创建表头
    #table_header = "| No. | Country | Sent | Received | Avg travel(Sent) | Avg travel(Received) |\n"
    table_header1 = "| 序号 | 国家 | 已寄出 | 已收到 | 寄出-平均所需天数 | 收到-平均所需天数 |\n"
    table_header2 = "| --- | --- | --- | --- | --- | --- |\n"

    # 创建表格内容
    table_content = ""
    for i, stats in enumerate(sorted_stats_data, start=1):
        country = stats['name']
        flag = stats['flagEmoji']
        sent = stats['sentNum']
        received = stats['receivedNum']
        sent_avg = stats['sentAvg']
        received_avg = stats['receivedAvg']
        if sent_avg =="-":
            sent_avg_days = "-"
        else:
            sent_avg_days = f"{sent_avg}天"
        
        if received_avg =="-":
            received_avg_days = "-"
        else:
            received_avg_days = f"{received_avg}天"

        
        table_content += f"| {i} | {country} {flag} | {sent} | {received} | {sent_avg_days} | {received_avg_days} |\n"

    # 将表头和表格内容合并
    table = table_header1 + table_header2 + table_content

    # 将表格内容写入 mdsheet.md 文件
    with open('./output/mdsheet.md', 'w' ,encoding="utf-8") as file:
        file.write(table)
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
        dataNew = dataNew.replace('//请替换明信片表格',sheet)
        dataNew = dataNew.replace('//请替换明信片故事list',list)

    with open(f"./output/信息汇总.md", "w",encoding="utf-8") as f:
        f.write(dataNew)  

def getContent(excel_file, json_file):
    # 读取Excel文件
    df = pd.read_excel(excel_file)

    # 将数据转换为字典格式
    data = df.to_dict(orient='records')

    # 将字典转换为JSON格式
    json_data = json.dumps(data, indent=2)

    # 将JSON数据写入文件
    with open(json_file, 'w') as file:
        file.write(json_data)
    
    # 连接到数据库
    conn = sqlite3.connect('./template/test.db')

    # 将数据写入数据库
    df.to_sql('postcardStory', conn, if_exists='replace', index=False)

excel_file="./template/postcardStory.xlsx"
json_file="./template/postcardStory.json"
getContent(excel_file, json_file)


def getCardStoryList():
    # 连接到test.db数据库
    conn = sqlite3.connect('./template/test.db')
    cursor = conn.cursor()

    # 查询postcardStory表和Galleryinfo表，并通过id字段进行连接查询
    cursor.execute('''SELECT postcardStory.id, 
                   postcardStory.content_cn, 
                   postcardStory.content_en,
                   Galleryinfo.userInfo,
                   Galleryinfo.picFileName,
                   Galleryinfo.contryNameEmoji,
                   Galleryinfo.type
                   FROM postcardStory
                   INNER JOIN Galleryinfo ON postcardStory.id = Galleryinfo.id''')

    # 将查询结果存储到content列表中
    content = cursor.fetchall()
    #print(f"content:\n",content)
    # 关闭数据库连接
    conn.close()
    list_all = ""
    for row in content:
        onlinelink ="https://s3.amazonaws.com/static2.postcrossing.com/postcard/medium"
        storypicLink = "https://pan.4a1801.life/d/Onedrive-4A1801/%E4%B8%AA%E4%BA%BA%E5%BB%BA%E7%AB%99/public/Postcrossing/content"

        list = f'### [{row[0]}](https://www.postcrossing.com/postcards/{row[0]})\n\n' \
          f'> 来自 {row[3]} {row[5]}\n\n' \
          f'<div class="image-preview">  <img src="{onlinelink}/{row[4]}" />' \
          f'  <img src="{storypicLink}/{row[0]}.webp" /></div>' \
          f'\n\n' \
          f'::: info 内容\n{row[2]}\n:::\n\n' \
          f'::: tip 翻译\n{row[1]}\n:::\n\n' \

        
        list_all +=list
    print("已导出明信片故事list")
    return list_all
    # 输出查询结果
    # for row in content:
        # print(f"ID: {row[0]}, Content: {row[1]}, PicFileName: {row[2]}")

dl.replaceTemplateCheck()
replaceTemplate()

# getCardStoryList()