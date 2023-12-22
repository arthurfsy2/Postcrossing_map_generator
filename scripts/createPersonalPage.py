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
    for item in content:
        distance_all.append(int(item["distance"]))
    total = sum(distance_all)
    rounds = round((total/40076),2)
    return total,len(content),rounds

def getUserSheet(tableName):
    data = dl.readDB(dbpath, "", tableName)
    countryCount = len(data)
    new_data = []
    for i, item in enumerate(data):
        if item['sentMedian']:
            sentMedian = f"{item['sentMedian']}天"
        else:
            sentMedian = "-"
        if item['receivedMedian']:
            receivedMedian = f"{item['receivedMedian']}天"
        else:
           receivedMedian = "-"
        formatted_item = {
            '国家': f"{item['name']} {emoji.emojize(item['flagEmoji'],language='alias')}",
            '已寄出': item['sentNum'],
            '已收到': item['receivedNum'],
            '寄出-平均': f"{item['sentAvg']}天",
            '收到-平均': f"{item['receivedAvg']}天",
            '寄出-中间值': sentMedian,
            '收到-中间值': receivedMedian,
        }
        new_data.append(formatted_item)
    # 将数据数组转换为 DataFrame
    df = pd.DataFrame(new_data)
    # 修改索引从1开始
    df.index = df.index + 1
    # 将 DataFrame 转换为 HTML 表格，并添加 Bootstrap 的 CSS 类和居中对齐的属性
    html_table = df.to_html(classes="table table-striped table-bordered", escape=False, table_id="dataTable", header=True)
    html_table = html_table.replace('<th>', '<th class="text-center">')
    html_table = html_table.replace('<td>', '<td class="text-center">')
    
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{tableName}</title>
        <link rel="stylesheet" href="../src/bootstrap-5.2.2/package/dist/css/bootstrap.min.css">
        <script src="../src/bootstrap-5.2.2/package/dist/js/bootstrap.bundle.min.js"></script>
        <script src="../src/jquery-1.12.4/package/dist/jquery.min.js"></script>
        <script src="../src/tablesorter-2.31.3/js/jquery.tablesorter.js"></script>
        <script>
            $(document).ready(function() {{
                $("#dataTable").tablesorter();
            }});
            
            function searchTable() {{
                var input = document.getElementById("searchInput");
                var filter = input.value.toUpperCase();
                var table = document.getElementById("dataTable");
                var tr = table.getElementsByTagName("tr");
                for (var i = 1; i < tr.length; i++) {{  // Start from index 1 to exclude the table header row
                    var td = tr[i].getElementsByTagName("td");
                    var found = false;
                    for (var j = 0; j < td.length; j++) {{
                        var txtValue = td[j].textContent || td[j].innerText;
                        if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                            found = true;
                            break;
                        }}
                    }}
                    if (found) {{
                        tr[i].style.display = "";
                    }} else {{
                        tr[i].style.display = "none";
                    }}
                }}
            }}
        </script>
    <style>
    .search-input {{
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 14px;
        width: 200px;
    }}

    .search-input:focus {{
        outline: none;
        border-color: #007bff;
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
    }}
    </style>
    </head>
    <body>
        <div class="container-fluid">
            <div class="mb-3">
                <input type="text" id="searchInput" onkeyup="searchTable()" placeholder="搜索国家">
            </div>
            <div class="table-responsive">
                {html_table}
            </div>
        </div>
        <script>
            // 在页面加载完成后执行搜索表格的函数
            window.onload = function() {{
                searchTable();
            }};
        </script>
    </body>
    </html>
    '''
    # 保存HTML表格为网页文件
    with open(f'./output/{tableName}.html', 'w', encoding="utf-8") as file:
        file.write(html_content)

    return countryCount


def replaceTemplate():   
    stat,content_raw,types = dl.getAccountStat(Cookie)  
    title_all=""
    desc_all=""      
    countryNum = getUserSheet("CountryStats")
    travelingNum = getTravelingID(account,"traveling",Cookie)

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
    
    storylist,storyNum = getCardStoryList("received")
    commentlist,commentNum = getCardStoryList("sent")
    calendar,series,height = createCalendar()
    with open(f"./template/信息汇总_template.md", "r",encoding="utf-8") as f:
        data = f.read()  
        dataNew = data.replace('$account',account)
        print(f"已替换account:{account}")        
        dataNew = dataNew.replace('$title',title_final)
        print("已替换明信片墙title")
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
        print(f"————————————————————")


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
            "content_original": row[1],
            "content_cn": row[2],
            "comment_original": row[3],
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
        content_original = id["content_original"]
        content_cn = id["content_cn"]
        comment_original = id["comment_original"] 
        comment_cn = id["comment_cn"] 
        def remove_blank_lines(text):
            if text:
                return "\n".join(line for line in text.splitlines() if line.strip())
            return text

        # 去掉空白行
        content_original = remove_blank_lines(content_original)
        content_cn = remove_blank_lines(content_cn)
        comment_original = remove_blank_lines(comment_original)
        comment_cn = remove_blank_lines(comment_cn)

        if comment_original:
            comment = f'@tab 回复\n' \
                    f'* 回复原文\n\n> {comment_original}\n\n* 翻译：\n\n> {comment_cn}\n\n:::' 
            
        else:
            comment = ":::"      
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
            f'* 卡片文字\n\n> {content_original}\n\n* 翻译：\n\n> {content_cn}\n\n' \
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
        # 创建 OpenCC 对象，指定转换方式为简体字转繁体字
        converter = OpenCC('s2t.json')
        # 统计每个关键词出现的次数
        keyword_counts = {}
        for keyword in keywords:
            count = contents.count(keyword)
            keyword = converter.convert(keyword) #简体转繁体
            keyword_counts[keyword] = count
        # 创建一个WordCloud对象，并设置字体文件路径和轮廓图像
        wordcloud = WordCloud(width=1600, height=800, background_color="white", font_path=font_path)
        # 生成词云
        wordcloud.generate_from_frequencies(keyword_counts)
    else:
        path = en_path_svg
        wordcloud = WordCloud(width=1600, height=800, background_color="white", font_path=font_path, max_words=100).generate(contents)
        keywords = wordcloud.words_
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
        content_original = id["content_original"]
        content_cn = id["content_cn"]
        comment_original = id["comment_original"] 
        comment_cn = id["comment_cn"] 
        data_en = f"{content_original}\n{comment_original}\n"
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
    data = sorted(response, key=lambda x: x[7])
    new_data = []
    for i,stats in enumerate(data):
        baseurl = "https://www.postcrossing.com"
        formatted_item = {
            'ID号': f"<a href='{baseurl}/travelingpostcard/{stats[0]}'>{stats[0]}</a>",
            '收件人': f"<a href='{baseurl}/user/{stats[1]}'>{stats[1]}</a>",
            '国家': stats[3],
            '寄出时间': datetime.fromtimestamp(stats[4]).strftime('%Y/%m/%d'),
            '距离': f'{format(stats[6], ",")} km',
            '天数': stats[7]
        }
        new_data.append(formatted_item)
    df = pd.DataFrame(new_data)
    # 修改索引从1开始
    df.index = df.index + 1
    # 将 DataFrame 转换为 HTML 表格，并添加 Bootstrap 的 CSS 类和居中对齐的属性
    html_table = df.to_html(classes="table table-striped table-bordered", escape=False, table_id="dataTable", header=True)
    html_table = html_table.replace('<th>', '<th class="text-center">')
    html_table = html_table.replace('<td>', '<td class="text-center">')

    # 生成完整的HTML文件
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>还在漂泊的明信片</title>
        <link rel="stylesheet" href="../src/bootstrap-5.2.2/package/dist/css/bootstrap.min.css">
        <script src="../src/bootstrap-5.2.2/package/dist/js/bootstrap.bundle.min.js"></script>
        <script src="../src/jquery-1.12.4/package/dist/jquery.min.js"></script>
        <script src="../src/tablesorter-2.31.3/js/jquery.tablesorter.js"></script>
        <script>
            $(document).ready(function() {{
                $("#dataTable").tablesorter();
            }});
            
            function searchTable() {{
                var input = document.getElementById("searchInput");
                var filter = input.value.toUpperCase();
                var table = document.getElementById("dataTable");
                var tr = table.getElementsByTagName("tr");
                for (var i = 1; i < tr.length; i++) {{  // Start from index 1 to exclude the table header row
                    var td = tr[i].getElementsByTagName("td");
                    var found = false;
                    for (var j = 0; j < td.length; j++) {{
                        var txtValue = td[j].textContent || td[j].innerText;
                        if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                            found = true;
                            break;
                        }}
                    }}
                    if (found) {{
                        tr[i].style.display = "";
                    }} else {{
                        tr[i].style.display = "none";
                    }}
                }}
            }}
            </script>
    <style>
    .search-input {{
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 14px;
        width: 200px;
    }}

    .search-input:focus {{
        outline: none;
        border-color: #007bff;
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
    }}
    </style>
    </head>
    <body>
        <div class="container-fluid">
            <div class="mb-3">
                <input type="text" id="searchInput" onkeyup="searchTable()" placeholder="搜索国家">
            </div>
            <div class="table-responsive">
                {html_table}
            </div>
        </div>
        <script>
            // 在页面加载完成后执行搜索表格的函数
            window.onload = function() {{
                searchTable();
            }};
        </script>
    </body>
    </html>
    '''
    # 保存HTML表格为网页文件
    with open(f'./output/{type}.html', 'w', encoding="utf-8") as file:
        file.write(html_content)
    return travelingCount

dl.replaceTemplateCheck()
excel_file="./template/postcardStory.xlsx"
StoryXLS2DB(excel_file)
replaceTemplate()
if os.path.exists(f"{dbpath}BAK"):
    dbStat = dl.compareMD5(dbpath, f"{dbpath}BAK")
    if dbStat == "1":
        print(f"{dbpath} 有更新") 
        print(f"正在生成明信片故事中、英文词云") 
        result_cn,result_en = readStoryDB(dbpath)
        createWordCloud("cn",result_cn)
        createWordCloud("en",result_en)
        os.remove(f"{dbpath}BAK")
    else:
        print(f"{dbpath} 暂无更新")    
        os.remove(f"{dbpath}BAK")