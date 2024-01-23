import pandas as pd
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
# import emoji
import pycountry
from emojiflags.lookup import lookup as flag
from multiDownload import getAccountStat
from common_tools import readDB, writeDB, compareMD5, translate
import pytz
import shutil
from PIL import Image
import re

with open("scripts/config.json", "r") as file:
    data = json.load(file)
personalPageLink = data["personalPageLink"]
# nickName = data["nickName"]
Cookie = data["Cookie"]
picDriverPath = data["picDriverPath"]
dbpath = data["dbpath"]
storyPicLink = data["storyPicLink"]
storyPicType = data["storyPicType"]

# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser()
parser.add_argument("account", help="输入account")
parser.add_argument("nickName", help="输入nickName")
parser.add_argument("repo", help="输入repo1")
parser.add_argument("apikey", help="输入小牛翻译apikey")
options = parser.parse_args()

account = options.account
nickName = options.nickName
repo = options.repo
apikey = options.apikey

font_path = "./scripts/font.otf"
cn_path_svg = "./output/postcrossing_cn.svg"
en_path_svg = "./output/postcrossing_en.svg"
excel_file = "./template/postcardStory.xlsx"

if os.path.exists(dbpath):
    shutil.copyfile(dbpath, f"{dbpath}BAK")


def replateTitle(type):

    with open(f"./output/title.json", "r", encoding="utf-8") as f:
        title = json.load(f)
    value = title.get(type)
    from_or_to, pageNum, Num, title = value
    return title

# 获取收发总距离


def getUserHomeInfo(type):
    content = readDB(dbpath, "", "userSummary")
    for id in content:
        about = id["about"]
        coors = id["coors"]
        sentDistance = int(id["sentDistance"])
        sentLaps = id["sentLaps"]
        sentPostcardNum = id["sentPostcardNum"]
        receivedDistance = int(id["receivedDistance"])
        receivedLaps = id["receivedLaps"]
        receivedPostcardNum = id["receivedPostcardNum"]
        registerd_years = id["registerd_years"]
        registerd_days = id["registerd_days"]
        register_date = id["register_date"]
        logo = id["logo"]
        if type == "sent":
            return sentDistance, sentPostcardNum, sentLaps, registerd_years, registerd_days, register_date, about, coors, logo
        if type == "received":
            return receivedDistance, receivedPostcardNum, receivedLaps, registerd_years, registerd_days, register_date, about, coors, logo


def getUserSheet(tableName):
    data = readDB(dbpath, "", tableName)
    countryCount = len(data)
    new_data = []
    for i, item in enumerate(data):
        if item['sentMedian']:
            sentMedian = f"{item['sentMedian']}天"
            sentAvg = f"{item['sentAvg']}天"
        else:
            sentMedian = "-"
            sentAvg = "-"
        if item['receivedMedian']:
            receivedMedian = f"{item['receivedMedian']}天"
            receivedAvg = f"{item['receivedAvg']}天"
        else:
            receivedMedian = "-"
            receivedAvg = "-"
        formatted_item = {
            '国家': f"{item['name']} {flag(item['countryCode'])}",
            '已寄出': item['sentNum'],
            '已收到': item['receivedNum'],
            '寄出-平均': sentAvg,
            '收到-平均': receivedAvg,
            '寄出-中间值': sentMedian,
            '收到-中间值': receivedMedian,
        }
        new_data.append(formatted_item)
    html_content = htmlFormat(tableName, new_data)
    # 保存HTML表格为网页文件
    with open(f'./output/{tableName}.html', 'w', encoding="utf-8") as file:
        file.write(html_content)

    return countryCount


def replaceTemplate():
    stat, content_raw, types = getAccountStat(account, Cookie)
    desc_all = ""
    countryNum = getUserSheet("CountryStats")
    countries = f"{countryNum}/248 [{round(countryNum/248*100,2)}%]"
    travelingNum, expiredNum = getTravelingID(account, "traveling", Cookie)
    traveling = f"{travelingNum} [过期：{expiredNum}]"
    for type in types:
        if type == "sent" or type == "received":
            distance, num, rounds, registerd_years, registerd_days, register_date, about, coors, logo = getUserHomeInfo(
                type)
            registerDate = f"{register_date} [至今{registerd_years}年（{registerd_days}天）]"
        distance_all = format(distance, ",")
        summary = f"{num} 📏{distance_all} km 🌏{rounds} 圈]\n\n"
        if type == "sent":
            sent_info = f"[📤{summary}"
        elif type == "received":
            received_info = f"[📥{summary}"
        else:
            desc = ""

    coors = json.loads(coors)
    coorLink = f"{coors[0]}~{coors[1]}"
    logoLink = f"![](https://s3.amazonaws.com/static2.postcrossing.com/avatars/140x140/{logo}.jpg)"
    about = f"{logoLink}\n\n{about}"

    title_all = ""
    for type in types:
        title = replateTitle(type)
        title_all += f"#### [{title}](/{nickName}/postcrossing/{type})\n\n"

        title_final = f"{title_all}"
    createRegisterInfo(registerDate, sent_info,
                       received_info, countries, traveling)
    storylist, storyNum = getCardStoryList("received")
    commentlist, commentNum = getCardStoryList("sent")
    calendar, series, height = createCalendar()
    with open(f"./template/信息汇总_template.md", "r", encoding="utf-8") as f:
        data = f.read()
        dataNew = data.replace('$account', account)
        print(f"已替换account:{account}")
        dataNew = dataNew.replace('$about', about).replace(
            '$coors', coorLink).replace('$personalPageLink', personalPageLink)
        print("已替换个人汇总信息")
        dataNew = dataNew.replace('$title', title_final)
        print("已替换明信片墙title")
        dataNew = dataNew.replace(
            '$storylist', storylist).replace('$storyNum', storyNum)
        print("已替换明信片故事list")
        dataNew = dataNew.replace('$commentlist', commentlist).replace(
            '$commentNum', commentNum)
        print("已替换明信片评论list")
        dataNew = dataNew.replace('$calendar', calendar)
        dataNew = dataNew.replace('$series', series)
        dataNew = dataNew.replace('$height', str(height))
        print("已替换明信片日历list")
        dataNew = dataNew.replace('$repo', repo)
        print(f"已替换仓库名:{repo}")
        print(f"————————————————————")

    with open(f"./gallery/信息汇总.md", "w", encoding="utf-8") as f:
        f.write(dataNew)

    blog_path = r"D:\web\Blog\src\Arthur\Postcrossing\信息汇总.md"

    # 换为你的blog的本地链接，可自动同步过去，方便测试
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
    writeDB(dbpath, content_all, tablename)


def getCardStoryListBYyear(type):
    list_all = ""
    content = readDB(dbpath, type, "postcardStory")
    total_num = str(len(content))
    content_years = {}
    for item in content:
        received_year = item['receivedDate'].split('/')[0]
        if received_year not in content_years:
            content_years[received_year] = []
        content_years[received_year].append(item)
    for year in content_years:
        content_years[year] = sorted(
            content_years[year], key=lambda x: x['receivedDate'], reverse=True)
    return content_years, total_num
    # 其他代码


def getCardStoryList(type):
    content_all = ""
    year_all = ""
    content_years, total_num = getCardStoryListBYyear(type)
    for year in content_years:
        content = content_years.get(year)
        list_all = ""
        num = str(len(content))
        for id in content:
            postcardID = id["id"]
            content_original = id["content_original"]
            content_cn = id["content_cn"]
            comment_original = id["comment_original"]
            comment_cn = id["comment_cn"]
            travel_days = id["travel_days"]
            sentAddr = id["sentAddr"]
            sentCountry = id["sentCountry"]
            receivedAddr = id["receivedAddr"]
            receivedCountry = id["receivedCountry"]
            sentDate = id["sentDate"]
            receivedDate = id["receivedDate"]
            sentDate_local = id["sentDate_local"]
            receivedDate = id["receivedDate"]
            receivedDate_local = id["receivedDate_local"]

            FromCoor = json.loads(id["FromCoor"]) if id["FromCoor"] else ""
            ToCoor = json.loads(id["ToCoor"]) if id["ToCoor"] else ""
            travel_time_local = f'> 📤 [{sentCountry}](https://www.bing.com/maps/?cp={FromCoor[0]}~{FromCoor[1]}&lvl=12.0&setlang=zh-Hans) {sentDate_local} (当地)\n' \
                                f'> 📥 [{receivedCountry}](https://www.bing.com/maps/?cp={ToCoor[0]}~{ToCoor[1]}&lvl=12.0&setlang=zh-Hans) {receivedDate_local} (当地)\n' if id["FromCoor"] else ""

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
            userInfo = f'[{id["userInfo"]}](https://www.postcrossing.com/user/{id["userInfo"]})' if id["userInfo"] != "account closed" else "*用户已注销*"

            picFileName = id["picFileName"]
            countryNameEmoji = id["countryNameEmoji"] if id["countryNameEmoji"] is not None else ""

            distanceNum = id["distance"]
            distance = format(distanceNum, ",")

            if type == "received":
                picList = f'<div class="image-preview">  <img src="{picDriverPath}/{picFileName}" />  <img src="{storyPicLink}/{postcardID}.{storyPicType}" /></div>' if picFileName != 'noPic.png' else f'<div class="image-preview"> <img src="{storyPicLink}/{postcardID}.{storyPicType}" /></div>'

                list = f'[{postcardID}](https://www.postcrossing.com/postcards/{postcardID})\n\n' \
                    f'> 来自 {userInfo} {countryNameEmoji}\n' \
                    f'{travel_time_local} 📏 {distance} | ⏱ {travel_days}\n\n' \
                    f':::tabs\n' \
                    f'@tab 图片\n' \
                    f'{picList}' \
                    f'\n\n' \
                    f'@tab 内容\n' \
                    f'* 卡片文字\n\n> {content_original}\n\n* 翻译：\n\n> {content_cn}\n\n' \
                    f'{comment}\n\n' \
                    f'---\n'
            else:
                picList = f'@tab 图片\n![]({picDriverPath}/{picFileName})\n\n' if picFileName != 'noPic.png' else ''

                list = f'[{postcardID}](https://www.postcrossing.com/postcards/{postcardID})\n\n' \
                    f'> 寄往 {userInfo} {countryNameEmoji}\n' \
                    f'{travel_time_local} 📏 {distance} | ⏱ {travel_days}\n\n' \
                    f':::tabs\n' \
                    f'{picList}' \
                    f'{comment}\n\n' \
                    f'---\n'
            list_all += list
            year_all = f"### {year}({num})\n\n{list_all}"
        # print("year_all:\n",year_all)
        # print("————————————————————")
        content_all += year_all
    return content_all, total_num


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
    calendar_all = ""
    series_all = ""

    for i, year in enumerate(year_list):
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
        calendar_all += calendar

        series = f"""
        {{
        type: "heatmap",
        coordinateSystem: "calendar",
        calendarIndex: {i},
        data: data
        }},
        """
        series_all += series
    height = len(year_list)*150
    return calendar_all, series_all, height


def createWordCloud(type, contents):
    contents = contents.replace("nan", "")
    # 转换为svg格式输出
    if type == "cn":
        path = cn_path_svg
        # 使用jieba的textrank功能提取关键词
        keywords = jieba.analyse.textrank(
            contents, topK=100, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
        # 创建 OpenCC 对象，指定转换方式为简体字转繁体字
        converter = OpenCC('s2t.json')
        # 统计每个关键词出现的次数
        keyword_counts = {}
        for keyword in keywords:
            count = contents.count(keyword)
            keyword = converter.convert(keyword)  # 简体转繁体
            keyword_counts[keyword] = count
        # 创建一个WordCloud对象，并设置字体文件路径和轮廓图像
        wordcloud = WordCloud(width=1600, height=800,
                              background_color="white", font_path=font_path)
        # 生成词云
        wordcloud.generate_from_frequencies(keyword_counts)
    else:
        path = en_path_svg
        wordcloud = WordCloud(width=1600, height=800, background_color="white",
                              font_path=font_path, max_words=100).generate(contents)
        keywords = wordcloud.words_
    svg_image = wordcloud.to_svg(embed_font=True)

    with open(path, "w+", encoding='UTF8') as f:
        f.write(svg_image)
        print(f"已保存至{path}")


def readStoryDB(dbpath):
    result_cn = ""
    result_en = ""
    content = readDB(dbpath, "sent", "postcardStory")
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
    return result_cn.replace("None", ""), result_en.replace("None", "")

# 实时获取该账号所有sent、received的明信片列表，获取每个postcardID的详细数据


def getTravelingID(account, type, Cookie):
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
    url = f'https://www.postcrossing.com/user/{account}/data/{type}'
    response = requests.get(url, headers=headers).json()
    expiredCount = sum(1 for item in response if item[7] > 60)
    travelingCount = len(response)
    data = sorted(response, key=lambda x: x[7])
    new_data = []

    def get_local_date(country_code, timestamp):
        # 根据国家二简码获取时区
        timezone = pytz.country_timezones.get(country_code)
        if timezone:
            timezone = pytz.timezone(timezone[0])
        else:
            return "Invalid country code"
        # 将时间戳转换为datetime对象
        dt = datetime.fromtimestamp(timestamp)
        # 将datetime对象转换为当地时区的时间
        local_dt = dt.astimezone(timezone)
        # 格式化日期为"%Y/%m/%d %H:%M"的字符串
        formatted_date = local_dt.strftime("%Y/%m/%d %H:%M")
        return formatted_date
    with open("scripts/countryName.json", "r") as file:
        countryList = json.load(file)
    for i, stats in enumerate(data):

        baseurl = "https://www.postcrossing.com"
        sentAvg = readDB(dbpath, stats[3], "CountryStats")[0]['sentAvg']
        if int(stats[7]) >= 60:
            traveling_days = f'<span style="color: red;">{stats[7]}</span>'
        elif int(stats[7]) > int(sentAvg):
            traveling_days = f'<span style="color: orange;">{stats[7]}</span>'
        else:
            traveling_days = f'<span style="color: green;">{stats[7]}</span>'
        formatted_item = {
            'ID号': f"<a href='{baseurl}/travelingpostcard/{stats[0]}' target='_blank'>{stats[0]}</a>",
            '收信人': f"<a href='{baseurl}/user/{stats[1]}' target='_blank'>{stats[1]}</a>",
            '国家': f"{countryList[stats[3]]} {flag(stats[3])}",
            '寄出时间(当地)': get_local_date(stats[0][0:2], stats[4]),
            '距离(km)': f'{format(stats[6], ",")}',
            '天数': traveling_days,
            '历史平均到达(天)': f"{sentAvg}",
        }
        new_data.append(formatted_item)
    df = pd.DataFrame(new_data)
    # 修改索引从1开始
    df.index = df.index + 1
    html_content = htmlFormat("还在漂泊的明信片", new_data)
    # 保存HTML表格为网页文件
    with open(f'./output/{type}.html', 'w', encoding="utf-8") as file:
        file.write(html_content)
    return travelingCount, expiredCount


def get_HTML_table(type, tableName):
    content = readDB(dbpath, type, tableName)
    # print(content)
    new_data = []
    for i, stats in enumerate(content):
        # 提取travel_days
        travel_days = stats['travel_days']
        # 提取sent_time和received_time
        sent_time = stats['sentDate_local']
        received_time = stats['receivedDate_local']
        distance = stats['distance']
        baseurl = "https://www.postcrossing.com"
        if type == "sent":
            formatted_item = {
                'ID号': f"<a href='{baseurl}/postcards/{stats['id']}' target='_blank'>{stats['id']}</a>",
                '收信人': f"<a href='{baseurl}/user/{stats['user']}' target='_blank'>{stats['user']}</a>",
                '寄往地区': f"{stats['receivedCountry']} {stats['flagEmoji']}",
                '寄出时间(当地)': sent_time,
                '收到时间(当地)': received_time,
                '距离(km)': f'{format(distance, ",")}',
                '天数': travel_days
            }
        elif type == "received":
            formatted_item = {
                'ID号': f"<a href='{baseurl}/postcards/{stats['id']}' target='_blank'>{stats['id']}</a>",
                '发信人': f"<a href='{baseurl}/user/{stats['user']}' target='_blank'>{stats['user']}</a>",
                '来自地区': f"{stats['sentCountry']} {stats['flagEmoji']}",
                '寄出时间(当地)': sent_time,
                '收到时间(当地)': received_time,
                '距离(km)': f'{format(distance, ",")} km',
                '天数': travel_days
            }
        new_data.append(formatted_item)
        new_data = sorted(new_data, key=lambda x: x['收到时间(当地)'], reverse=True)
    html_content = htmlFormat(type, new_data)
    with open(f'./output/{type}.html', 'w', encoding="utf-8") as file:
        file.write(html_content)


def htmlFormat(title, data):
    df = pd.DataFrame(data)
    # 修改索引从1开始
    df.index = df.index + 1
    # 将 DataFrame 转换为 HTML 表格，并添加 Bootstrap 的 CSS 类和居中对齐的属性
    html_table = df.to_html(classes="table table-striped table-bordered",
                            escape=False, table_id="dataTable", header=True)
    html_table = html_table.replace('<th>', '<th class="text-center">')
    html_table = html_table.replace('<td>', '<td class="text-center">')
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
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
                <input type="text" id="searchInput" onkeyup="searchTable()" placeholder="搜索……">
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
    return html_content


def picTowebp(input_dir, output_dir):
    # 获取input_dir目录下的所有文件名
    file_names = os.listdir(input_dir)
    for file_name in file_names:
        # 获取文件的完整路径
        file_path = os.path.join(input_dir, file_name)
        # 检查文件后缀名是否为.jpg、.jpeg或.png
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                # 打开图片文件
                image = Image.open(file_path)
                # 构建输出文件的路径和文件名
                output_file_path = os.path.join(
                    output_dir, os.path.splitext(file_name)[0] + '.webp')
                # 转换为webp格式并保存
                image.save(output_file_path, 'webp')
                # 删除原有文件
                os.remove(file_path)
                print(f"文件 {file_name} 转换成功并已删除原有文件")
            except Exception as e:
                print(f"文件 {file_name} 转换失败: {str(e)}")


def createRegisterInfo(register_date, sent_info, received_info, countries, traveling):
    # 创建HTML内容
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Postcrossing Stats</title>
        <!-- 引入Bootstrap CSS -->
        <link rel="stylesheet" href="../src/bootstrap-5.2.2/package/dist/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container-fluid">
            <h1 class="text-center mb-4"></h1>
            <ul class="list-group">
                <li class="list-group-item">注册时间：<b>{register_date}</b></li>
                <li class="list-group-item">寄出：<b>{sent_info}</b></li>
                <li class="list-group-item">收到：<b>{received_info}</b></li>
                <li class="list-group-item">涉及国家：<b>{countries}</b></li>
                <li class="list-group-item">待签收：<b>{traveling}</b></li>
            </ul>
        </div>
        <!-- 引入Bootstrap JS 和依赖 -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.9.1/dist/umd/popper.min.js"></script>
        <script src="../src/bootstrap-5.2.2/package/dist/js/bootstrap.min.js"></script>
    </body>
    </html>
    """

    # 写入HTML文件
    with open('./output/registerInfo.html', 'w', encoding='utf-8') as file:
        file.write(html_content)


picTowebp("./template/rawPic", "./template/content")
excel_file = "./template/postcardStory.xlsx"
StoryXLS2DB(excel_file)
get_HTML_table("sent", "Mapinfo")
get_HTML_table("received", "Mapinfo")
replaceTemplate()
if os.path.exists(f"{dbpath}BAK"):
    dbStat = compareMD5(dbpath, f"{dbpath}BAK")
    if dbStat == "1":
        print(f"{dbpath} 有更新")
        print(f"正在生成明信片故事中、英文词云")
        result_cn, result_en = readStoryDB(dbpath)
        createWordCloud("cn", result_cn)
        createWordCloud("en", result_en)
        os.remove(f"{dbpath}BAK")
    else:
        print(f"{dbpath} 暂无更新")
        os.remove(f"{dbpath}BAK")
