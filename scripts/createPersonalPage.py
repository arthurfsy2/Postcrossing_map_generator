import multiDownload as dl
import pandas as pd
import sqlite3
import json
import os


with open("scripts/config.json", "r") as file:
    data = json.load(file)
account = data["account"]
nickName = data["nickName"]
Cookie = data["Cookie"]
picDriverPath = data["picDriverPath"]
dbpath = data["dbpath"]


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
    calendar = getCalendarList()
    with open(f"./template/信息汇总_template.md", "r",encoding="utf-8") as f:
        data = f.read()  
        dataNew = data.replace('//请替换明信片墙title',title_final)
        print("已替换明信片墙title")
        dataNew = dataNew.replace('//请替换明信片表格',sheet)
        print("已替换明信片表格")
        dataNew = dataNew.replace('//请替换明信片故事list',list)
        print("已替换明信片故事list")

        dataNew = dataNew.replace('//请替换明信片日历list',calendar)
        print("已替换明信片日历list")

    with open(f"./output/信息汇总.md", "w",encoding="utf-8") as f:
        f.write(dataNew)  

    blog_path = r"D:\web\Blog2\src\Arthur\Postcrossing\信息汇总.md"
    
    # 换为你的blog的本地链接，可自动同步过去
    if os.path.exists(blog_path):
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
          f':::tabs\n' \
          f'@tab 图片\n' \
          f'<div class="image-preview">  <img src="{onlinelink}/{picFileName}" />' \
          f'  <img src="{storypicLink}/{postcardID}.webp" /></div>' \
          f'\n\n' \
          f'@tab 内容\n' \
          f'::: info 内容\n{content_en}\n\n\n' \
          f'@tab 翻译\n' \
          f'::: tip 翻译\n{content_cn}\n:::\n\n' \
          f'---\n'   
        list_all +=list
    return list_all

def getCalendarList():
    # 指定文件夹路径
    folder_path = "./output/calendar"

    # 获取文件夹下所有文件和文件夹的名称列表
    file_names = os.listdir(folder_path)

    # 筛选出以.html结尾的文件名，并去除后缀，导出到year_list中
    year_list = [os.path.splitext(file_name)[0] for file_name in file_names if file_name.endswith(".html")]

    # 打印year_list
    print(year_list)
    list_all = ""
    for year in year_list:
        list = f'@tab {year}\n' \
          f'<iframe\n' \
          f'src="https://postcrossing.4a1801.life/output/calendar/{year}.html" \n' \
          f'frameborder=0\nheight=200\nwidth=100%\nseamless=seamless\nscrolling=auto\n></iframe>\n' \
           
        list_all +=list
    list_all =f":::tabs\n{list_all}\n:::"
    return list_all


dl.replaceTemplateCheck()
excel_file="./template/postcardStory.xlsx"
getStoryContent(excel_file)
replaceTemplate()

getCardStoryList()