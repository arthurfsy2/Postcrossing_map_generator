import multiDownload as dl
import pandas as pd
import sqlite3
import json
import os
from datetime import datetime, timedelta
import shutil
import argparse
import jieba
from jieba import analyse
from wordcloud import WordCloud
from opencc import OpenCC
import requests
import emoji

with open("scripts/config.json", "r") as file:
    data = json.load(file)
# account = data["account"]
# nickName = data["nickName"]
Cookie = data["Cookie"]
picDriverPath = data["picDriverPath"]
dbpath = data["dbpath"]
storyPicLink = data["storyPicLink"]
storyPicType = data["storyPicType"]

# 创建 ArgumentParser 对象
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

font_path = "./scripts/font.otf"
cn_path_svg = "./output/postcrossing_cn.svg"
en_path_svg = "./output/postcrossing_en.svg"
excel_file = "./template/postcardStory.xlsx"

if os.path.exists(dbpath):
    shutil.copyfile(dbpath, f"{dbpath}BAK")

def replateTitle(type):    
    
    with open(f"./output/title.json", "r",encoding="utf-8") as f:
        title = json.load(f)
    value = title.get(type)
    from_or_to, pageNum, Num, title = value
    return title

# 获取收发总距离
def getUserHomeInfo(type):
    distance_all = []
    content = dl.readDB(dbpath,type,"Mapinfo")
    #print("content:",content)
    for item in content:
        distance_all.append(int(item["distance"]))
    total = sum(distance_all)
    rounds = round((total/40076),2)
    return total,len(content),rounds

def getUserSheet():
    stats_data=dl.readDB(dbpath, "", "CountryStats")
    countryCount = len(stats_data)
    # 按照 name 的 A-Z 字母顺序对 stats_data 进行排序
    sorted_stats_data = sorted(stats_data, key=lambda x: x['name'])
    #print("sorted_stats_data",sorted_stats_data)
    # 创建表头
    #table_header = "| No. | Country | Sent | Received | Avg travel(Sent) | Avg travel(Received) |\n"
    table_header1 = "| 序号 | 国家 | 已寄出 | 已收到 | 寄出-平均 | 收到-平均 | 寄出-中间值 | 收到-中间值 \n"
    table_header2 = "| --- | --- | --- | --- | --- | --- | --- | --- \n"
    print("sorted_stats_data:\n",sorted_stats_data)
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
    return table,countryCount

def getUserSheet2():
    data=dl.readDB(dbpath, "", "CountryStats")
    countryCount = len(data)
    new_data = []
    for i, item in enumerate(data):
        item['序号'] = i + 1
        emojiName = item['flagEmoji']

        item['国家'] = f"{item.pop('name')} {emoji.emojize(emojiName,language='alias')}"
        item['已寄出'] = item.pop('sentNum')
        item['已收到'] = item.pop('receivedNum')
        item['寄出-平均'] = f"{item.pop('sentAvg')}天"
        item['收到-平均'] = f"{item.pop('receivedAvg')}天"
        item['寄出-中间值'] = f"{item.pop('sentMedian')}天"
        item['收到-中间值'] = f"{item.pop('receivedMedian')}天"
        del item['countryCode']
        del item['flagEmoji']
        del item['value']
        new_data.append(item)

    # 将数据数组转换为DataFrame
    df = pd.DataFrame(new_data)

    # 修改索引从1开始
    df.index = df.index + 1

    # 删除序号列
    df = df.drop(columns=['序号'])

    # 将DataFrame转换为HTML表格
    html_table = df.to_html(escape=False)

    # 添加CSS样式
    html_table = '<style>th, td {text-align: center;}</style>' + html_table
    # 保存HTML表格为网页文件
    with open('./output/sheet.html', 'w',encoding="utf-8") as file:
        file.write(html_table)

    return countryCount
def replaceTemplate():   
    stat,content_raw,types = dl.getAccountStat(Cookie)  
    title_all=""
    desc_all=""      
    sheet,countryNum = getUserSheet()
    getUserSheet2()
    traveling,travelingNum = getTravelingID(account,"traveling",Cookie)

    countryCount = f"> 涉及国家[🗺️**{countryNum}**]\n\n"
    travelingCount = f"> 待签收[📨**{travelingNum}**]\n\n"
    for type in types: 
        distance,num,rounds = getUserHomeInfo(type)
        distance_all = format(distance, ",")
        summary = f"**{num}** 📏**{distance_all}** km 🌏**{rounds}** 圈]\n\n"
        if type == "sent":
            desc = f"> 寄出[📤{summary}"
        elif type == "received":
            desc = f"> 收到[📥{summary}"
        else:
            desc =""
        desc_all += desc
    for type in types:        
        title = replateTitle(type)
        title_all += f"#### [{title}](/{nickName}/postcrossing/{type})\n\n"
        title_final = f"{desc_all}\n{countryCount}\n{travelingCount}\n{title_all}"
    #print("title_all:\n",title_all)
    
    
    storylist,storyNum = getCardStoryList("received")
    commentlist,commentNum = getCardStoryList("sent")
    calendar,series,height = createCalendar()
    with open(f"./template/信息汇总_template.md", "r",encoding="utf-8") as f:
        data = f.read()  
        dataNew = data.replace('$account',account)
        print(f"已替换account:{account}")        
        dataNew = dataNew.replace('$title',title_final)
        print("已替换明信片墙title")
        # dataNew = dataNew.replace('$sheet',sheet)
        # print("已替换明信片统计")
        dataNew = dataNew.replace('$traveling',traveling)
        print("已替换待登记list")
        dataNew = dataNew.replace('$storylist',storylist).replace('$storyNum',storyNum)
        print("已替换明信片故事list")
        dataNew = dataNew.replace('$commentlist',commentlist).replace('$commentNum',commentNum)
        print("已替换明信片评论list")
        dataNew = dataNew.replace('$calendar',calendar)
        dataNew = dataNew.replace('$series',series)
        dataNew = dataNew.replace('$height',str(height))
        print("已替换明信片日历list")
        dataNew = dataNew.replace('$repo',repo)
        print(f"已替换仓库名:{repo}")

    with open(f"./output/信息汇总.md", "w",encoding="utf-8") as f:
        f.write(dataNew)  

    blog_path = r"D:\web\Blog2\src\Arthur\Postcrossing\信息汇总.md"
    
    # 换为你的blog的本地链接，可自动同步过去
    if os.path.exists(blog_path):
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(dataNew)

def StoryXLS2DB(excel_file):
    df = pd.read_excel(excel_file)
    content_all = []

    for index, row in df.iterrows():
        data = {
            "id": row[0],
            "content_en": row[1],
            "content_cn": row[2],
            "comment_en": row[3],
            "comment_cn": row[4],
        }
        content_all.append(data)
    tablename = "postcardStory"
    dl.writeDB(dbpath, content_all,tablename)



def getCardStoryList(type):
    list_all = ""
    content =dl.readDB(dbpath, type,"postcardStory")
    num = str(len(content))
    for id in content:
        postcardID = id["id"]  
        content_en = id["content_en"]
        content_cn = id["content_cn"]
        comment_en = id["comment_en"] 
        comment_cn = id["comment_cn"] 
        def remove_blank_lines(text):
            if text:
                return "\n".join(line for line in text.splitlines() if line.strip())
            return text

        # 去掉空白行
        content_en = remove_blank_lines(content_en)
        content_cn = remove_blank_lines(content_cn)
        comment_en = remove_blank_lines(comment_en)
        comment_cn = remove_blank_lines(comment_cn)

        if comment_en:
            comment = f'@tab 回复\n' \
                    f'* 回复原文\n\n> {comment_en}\n\n* 翻译：\n\n> {comment_cn}\n\n:::' 
            
        else:
            comment = ":::"      
        #print("comment:",comment)
        userInfo = id["userInfo"]
        picFileName = id["picFileName"]
        contryNameEmoji = id["contryNameEmoji"] if id["contryNameEmoji"] is not None else ""
        travel_time = id["travel_time"]
        distanceNum = id["distance"]
        distance = format(distanceNum, ",")
        
        if type == "received":
            list = f'### [{postcardID}](https://www.postcrossing.com/postcards/{postcardID})\n\n' \
            f'> 来自 {userInfo} {contryNameEmoji}\n' \
            f'> 📏 {distance} km\n⏱ {travel_time}\n\n' \
            f':::tabs\n' \
            f'@tab 图片\n' \
            f'<div class="image-preview">  <img src="{picDriverPath}/{picFileName}" />' \
            f'  <img src="{storyPicLink}/{postcardID}.{storyPicType}" /></div>' \
            f'\n\n' \
            f'@tab 内容\n' \
            f'* 卡片文字\n\n> {content_en}\n\n* 翻译：\n\n> {content_cn}\n\n' \
            f'{comment}\n\n' \
            f'---\n'   
        else:
            list = f'### [{postcardID}](https://www.postcrossing.com/postcards/{postcardID})\n\n' \
            f'> 寄往 {userInfo} {contryNameEmoji}\n' \
            f'> 📏 {distance} km\n⏱ {travel_time}\n\n' \
            f':::tabs\n' \
            f'@tab 图片\n' \
            f'![]({picDriverPath}/{picFileName})\n\n' \
            f'' \
            f'{comment}\n\n' \
            f'---\n'
        list_all += list
    return list_all,num
    

def createCalendar():
    with open("output/UserStats.json", "r") as file:
        a_data = json.load(file)
    year_list = []

    for data in a_data:
        timestamp = data[0]  # 获取时间戳
        date = datetime.fromtimestamp(timestamp)  # 将时间戳转换为日期格式
        year = date.strftime("%Y")  # 提取年份（YYYY）
        if year not in year_list:
            year_list.append(year)
    calendar_all=""
    series_all=""

    for i,year in enumerate(year_list):
        calendar = f"""
        {{
            top: {i*150},
            cellSize: ["auto", "15"],
            range: {year},
            itemStyle: {{
                color: '#ccc',
                borderWidth: 3,
                borderColor: '#fff'
            }},
            splitLine: true,
            yearLabel: {{
                show: true
            }},
            dayLabel: {{
                firstDay: 1,
            }}
        }},
        """
        calendar_all+=calendar

        series = f"""
        {{
        type: "heatmap",
        coordinateSystem: "calendar",
        calendarIndex: {i},
        data: data
        }},
        """
        series_all+=series
    height = len(year_list)*150
    return calendar_all, series_all, height


def createWordCloud(type, contents):
    contents = contents.replace("nan","")
    # 转换为svg格式输出
    if type == "cn":
        path = cn_path_svg
        # 使用jieba的textrank功能提取关键词
        keywords = jieba.analyse.textrank(contents, topK=100, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
        #print(f"keywords={keywords}")
        # 创建 OpenCC 对象，指定转换方式为简体字转繁体字
        converter = OpenCC('s2t.json')
        # 统计每个关键词出现的次数
        keyword_counts = {}
        for keyword in keywords:
            count = contents.count(keyword)
            keyword = converter.convert(keyword) #简体转繁体
            keyword_counts[keyword] = count
        print(keyword_counts)
        # 创建一个WordCloud对象，并设置字体文件路径和轮廓图像
        wordcloud = WordCloud(width=1600, height=800, background_color="white", font_path=font_path)
        # 生成词云
        wordcloud.generate_from_frequencies(keyword_counts)
    else:
        path = en_path_svg
        wordcloud = WordCloud(width=1600, height=800, background_color="white", font_path=font_path, max_words=100).generate(contents)
        keywords = wordcloud.words_
        
        print(keywords)
    svg_image = wordcloud.to_svg(embed_font=True)

    with open(path, "w+", encoding='UTF8') as f:
        f.write(svg_image)
        print(f"已保存至{path}")

def readStoryDB(dbpath):
    result_cn = ""
    result_en = ""
    content =dl.readDB(dbpath, "sent","postcardStory")
    for id in content:
        postcardID = id["id"]  
        content_en = id["content_en"]
        content_cn = id["content_cn"]
        comment_en = id["comment_en"] 
        comment_cn = id["comment_cn"] 
        data_en = f"{content_en}\n{comment_en}\n"
        data_cn = f"{content_cn}\n{comment_cn}\n"
        result_en += data_en
        result_cn += data_cn
    return result_cn,result_en

# 实时获取该账号所有sent、received的明信片列表，获取每个postcardID的详细数据
def getTravelingID(account,type,Cookie):
    headers = {
    'Host': 'www.postcrossing.com',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Sec-Fetch-Mode': 'cors',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0.1 Mobile/15E148 Safari/604.1',
    'Connection': 'keep-alive',
    'Referer': f'https://www.postcrossing.com/user/{account}/{type}',
    'Cookie': Cookie,
    'Sec-Fetch-Dest': 'empty'
        }
    url=f'https://www.postcrossing.com/user/{account}/data/{type}'    
    response = requests.get(url,headers=headers).json()
    travelingCount = len(response)
    stats_data = sorted(response, key=lambda x: x[7])
    
    table_header1 = "| 序号 | ID号 | 收件人 | 国家 | 寄出时间 | 距离 | 天数  \n"
    table_header2 = "| --- | --- | --- | --- | --- | --- | ---  \n"

    # 创建表格内容
    table_content = ""
    for i, stats in enumerate(stats_data, start=1):
        baseurl = "https://www.postcrossing.com"
        id = f"[{stats[0]}]({baseurl}/travelingpostcard/{stats[0]})"
        toMember = f"[{stats[1]}]({baseurl}/user/{stats[1]})"
        
        toCountry = stats[3]
        sentDate = datetime.fromtimestamp(stats[4]).strftime('%Y/%m/%d')
        distanceNum = format(stats[6], ",")
        distance = f"{distanceNum} km"
        traveledDay = stats[7]
        table_content += f"| {i} | {id} | {toMember} | {toCountry} | {sentDate} | {distance} | {traveledDay} \n"

    # 将表头和表格内容合并
    table = table_header1 + table_header2 + table_content
    return table,travelingCount

dl.replaceTemplateCheck()
excel_file="./template/postcardStory.xlsx"
StoryXLS2DB(excel_file)
replaceTemplate()
if os.path.exists(f"{dbpath}BAK"):
    dbStat = dl.compareMD5(dbpath, f"{dbpath}BAK")
    if dbStat == "1":
        print(f"{dbpath} 有更新") 
        print(f"正在生成中、英文词库") 
        result_cn,result_en = readStoryDB(dbpath)
        createWordCloud("cn",result_cn)
        createWordCloud("en",result_en)
        os.remove(f"{dbpath}BAK")
    else:
        print(f"{dbpath} 暂无更新")    
        os.remove(f"{dbpath}BAK")