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
from jinja2 import Template


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
        is_supporter = id["is_supporter"]
        if type == "sent":
            return (
                sentDistance,
                sentPostcardNum,
                sentLaps,
                registerd_years,
                registerd_days,
                register_date,
                about,
                coors,
                logo,
                is_supporter,
            )
        if type == "received":
            return (
                receivedDistance,
                receivedPostcardNum,
                receivedLaps,
                registerd_years,
                registerd_days,
                register_date,
                about,
                coors,
                logo,
                is_supporter,
            )


def getUserSheet(tableName):
    data = readDB(dbpath, "", tableName)
    countryCount = len(data)
    new_data = []
    for i, item in enumerate(data):
        if item["sentMedian"]:
            sentMedian = f"{item['sentMedian']}天"
            sentAvg = f"{item['sentAvg']}天"
            sentDateFirst = item["sentDateFirst"]
        else:
            sentMedian = "-"
            sentAvg = "-"
            sentDateFirst = "-"
        if item["receivedMedian"]:
            receivedMedian = f"{item['receivedMedian']}天"
            receivedAvg = f"{item['receivedAvg']}天"
            receivedDateFirst = item["receivedDateFirst"]
        else:
            receivedMedian = "-"
            receivedAvg = "-"
            receivedDateFirst = "-"
        formatted_item = {
            "国家": f"{item['name']} {flag(item['countryCode'])}",
            "已寄出": item["sentNum"],
            "已收到": item["receivedNum"],
            "寄出-平均": sentAvg,
            "收到-平均": receivedAvg,
            "寄出-中间值": sentMedian,
            "收到-中间值": receivedMedian,
            "首次寄出": sentDateFirst,
            "首次收到": receivedDateFirst,
        }
        new_data.append(formatted_item)
    html_content = htmlFormat(tableName, new_data)
    # 保存HTML表格为网页文件
    with open(f"./output/{tableName}.html", "w", encoding="utf-8") as file:
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
            (
                distance,
                num,
                rounds,
                registerd_years,
                registerd_days,
                register_date,
                about,
                coors,
                logo,
                is_supporter,
            ) = getUserHomeInfo(type)
            registerDate = (
                f"{register_date} [至今{registerd_years}年（{registerd_days}天）]"
            )

            if is_supporter == "YES":
                supporter_pic = f'<li class="list-group-item">会员<img src="https://static1.postcrossing.com/images/supporter.png" height="25"><b>：{is_supporter}-暂未到期</b></li>'
            elif is_supporter != "No":
                supporter_pic = f'<li class="list-group-item">会员<img src="https://static1.postcrossing.com/images/supporter.png" height="25"><b>：{is_supporter}到期</b></li>'
            else:
                supporter_pic = ""

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
    about = f"{logoLink}\n\n:::info 个人简介\n{about}\n"

    title_all = ""
    for type in types:
        title = replateTitle(type)
        title_all += f"#### [{title}](/{nickName}/postcrossing/{type})\n\n"

        title_final = f"{title_all}"
    createRegisterInfo(
        registerDate, sent_info, received_info, countries, traveling, supporter_pic
    )
    storylist, storyNum = getCardStoryList("received")
    commentlist, commentNum = getCardStoryList("sent")
    calendar, series, height = createCalendar()
    with open(f"./template/信息汇总_template.md", "r", encoding="utf-8") as f:
        template = Template(f.read())

    dataNew = template.render(
        account=account,
        about=about,
        coors=coorLink,
        personalPageLink=personalPageLink,
        title=title_final,
        storylist=storylist,
        storyNum=storyNum,
        commentlist=commentlist,
        commentNum=commentNum,
        calendar=calendar,
        series=series,
        height=str(height),
        repo=repo,
    )
    print(f"已替换account:{account}")
    print("已替换个人汇总信息")
    print("已替换明信片墙title")
    print("已替换明信片故事list")
    print("已替换明信片评论list")
    print("已替换明信片日历list")
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
    import warnings

    warnings.filterwarnings("ignore", category=FutureWarning)
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
        received_year = item["receivedDate"].split("/")[0]
        if received_year not in content_years:
            content_years[received_year] = []
        content_years[received_year].append(item)
    for year in content_years:
        content_years[year] = sorted(
            content_years[year], key=lambda x: x["receivedDate"], reverse=True
        )
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
            travel_time_local = (
                f"> 📤 [{sentCountry}](https://www.bing.com/maps/?cp={FromCoor[0]}~{FromCoor[1]}&lvl=12.0&setlang=zh-Hans) {sentDate_local} (当地)\n"
                f"> 📥 [{receivedCountry}](https://www.bing.com/maps/?cp={ToCoor[0]}~{ToCoor[1]}&lvl=12.0&setlang=zh-Hans) {receivedDate_local} (当地)\n"
                if id["FromCoor"]
                else ""
            )

            def remove_blank_lines(text):
                if text:
                    return "\n".join(line for line in text.splitlines() if line.strip())
                return text

            # 去掉空白行
            content_original = remove_blank_lines(content_original)
            content_cn = remove_blank_lines(content_cn)
            comment_original = remove_blank_lines(comment_original)
            comment_cn = remove_blank_lines(comment_cn)

            userInfo = (
                f'[{id["userInfo"]}](https://www.postcrossing.com/user/{id["userInfo"]})'
                if id["userInfo"] != "account closed"
                else "*用户已注销*"
            )

            picFileName = id["picFileName"]
            countryNameEmoji = (
                id["countryNameEmoji"] if id["countryNameEmoji"] is not None else ""
            )

            distanceNum = id["distance"]
            distance = format(distanceNum, ",")

            if type == "received":
                if content_original:
                    storyPic_src = f"{storyPicLink}/{postcardID}.{storyPicType}"
                    story_text = f"* 卡片文字\n\n> {content_original}\n\n* 翻译：\n\n> {content_cn}\n\n"
                else:
                    storyPic_src = None
                    story_text = "暂无内容\n\n"
                if comment_original:
                    comment_original = comment_original.replace("`", "\`")
                    comment = (
                        f"@tab 额外消息\n"
                        f"* 消息原文\n\n> {comment_original}\n\n* 翻译：\n\n> {comment_cn}\n\n"
                    )

                else:
                    comment = ""

                if picFileName != "noPic.png" and storyPic_src:
                    picList = f'<div class="image-preview">  <img src="{picDriverPath}/{picFileName}" />  <img src="{storyPic_src}" /></div>'
                elif picFileName == "noPic.png" and storyPic_src:
                    picList = f'<div class="image-preview"> <img src="{storyPic_src}" /></div>'
                else:
                    picList = "暂无图片"

                list = (
                    f"[{postcardID}](https://www.postcrossing.com/postcards/{postcardID})\n\n"
                    f"> 来自 {userInfo} {countryNameEmoji}\n"
                    f"{travel_time_local} 📏 {distance} | ⏱ {travel_days}\n\n"
                    f":::tabs\n"
                    f"@tab 图片\n"
                    f"{picList}"
                    f"\n\n"
                    f"@tab 内容\n"
                    f"{story_text}"
                    f"{comment}:::\n\n"
                    f"---\n\n"
                )
            elif type == "sent":
                if comment_original:
                    comment = (
                        f"@tab 回复\n"
                        f"* 回复原文\n\n> {comment_original}\n\n* 翻译：\n\n> {comment_cn}"
                    )

                else:
                    comment = ""
                if content_original:
                    reply_message = (
                        f"@tab 额外消息\n"
                        f"* 消息原文\n\n> {content_original}\n\n* 翻译：\n\n> {content_cn}\n\n"
                    )

                else:
                    reply_message = ""
                picList = (
                    f"@tab 图片\n![]({picDriverPath}/{picFileName})\n\n"
                    if picFileName != "noPic.png"
                    else ""
                )

                list = (
                    f"[{postcardID}](https://www.postcrossing.com/postcards/{postcardID})\n\n"
                    f"> 寄往 {userInfo} {countryNameEmoji}\n"
                    f"{travel_time_local} 📏 {distance} | ⏱ {travel_days}\n\n"
                    f":::tabs\n"
                    f"{picList}"
                    f"{comment}\n\n"
                    f"{reply_message}:::\n\n"
                    f"---\n\n"
                )
            list_all += list
            year_all = f"### {year}({num})\n\n{list_all}"
        # print("year_all:\n",year_all)
        # print("————————————————————")
        content_all += year_all
        template = Template(content_all)
        content_all = template.render(repo=repo)
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
    height = len(year_list) * 150
    return calendar_all, series_all, height


def createWordCloud(type, contents):
    contents = contents.replace("nan", "")
    # 转换为svg格式输出
    if type == "cn":
        path = cn_path_svg
        # 使用jieba的textrank功能提取关键词
        keywords = jieba.analyse.textrank(
            contents, topK=100, withWeight=False, allowPOS=("ns", "n", "vn", "v")
        )
        # 创建 OpenCC 对象，指定转换方式为简体字转繁体字
        converter = OpenCC("s2t.json")
        # 统计每个关键词出现的次数
        keyword_counts = {}
        for keyword in keywords:
            count = contents.count(keyword)
            keyword = converter.convert(keyword)  # 简体转繁体
            keyword_counts[keyword] = count
        # 创建一个WordCloud对象，并设置字体文件路径和轮廓图像
        wordcloud = WordCloud(
            width=1600, height=800, background_color="white", font_path=font_path
        )
        # 生成词云
        wordcloud.generate_from_frequencies(keyword_counts)
    else:
        path = en_path_svg
        wordcloud = WordCloud(
            width=1600,
            height=800,
            background_color="white",
            font_path=font_path,
            max_words=100,
        ).generate(contents)
        keywords = wordcloud.words_
    svg_image = wordcloud.to_svg(embed_font=True)

    with open(path, "w+", encoding="UTF8") as f:
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
        if (
            readDB(dbpath, stats[3], "CountryStats")
            and readDB(dbpath, stats[3], "CountryStats")[0]["sentAvg"]
        ):
            sentAvg = readDB(dbpath, stats[3], "CountryStats")[0]["sentAvg"]
        else:
            sentAvg = 0
        if int(stats[7]) >= 60:
            traveling_days = f'<span style="color: red;">{stats[7]}</span>'
        elif int(stats[7]) > int(sentAvg):
            traveling_days = f'<span style="color: orange;">{stats[7]}</span>'
        else:
            traveling_days = f'<span style="color: green;">{stats[7]}</span>'
        formatted_item = {
            "ID号": f"<a href='{baseurl}/travelingpostcard/{stats[0]}' target='_blank'>{stats[0]}</a>",
            "收信人": f"<a href='{baseurl}/user/{stats[1]}' target='_blank'>{stats[1]}</a>",
            "国家": f"{countryList[stats[3]]} {flag(stats[3])}",
            "寄出时间(当地)": get_local_date(stats[0][0:2], stats[4]),
            "距离(km)": f'{format(stats[6], ",")}',
            "天数": traveling_days,
            "历史平均到达(天)": f"{sentAvg}",
        }
        new_data.append(formatted_item)
    df = pd.DataFrame(new_data)
    # 修改索引从1开始
    df.index = df.index + 1
    html_content = htmlFormat("还在漂泊的明信片", new_data)
    # 保存HTML表格为网页文件
    with open(f"./output/{type}.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    return travelingCount, expiredCount


def get_HTML_table(type, tableName):
    content = readDB(dbpath, type, tableName)
    # print(content)
    new_data = []
    for i, stats in enumerate(content):
        # 提取travel_days
        travel_days = stats["travel_days"]
        # 提取sent_time和received_time
        sent_time = stats["sentDate_local"]
        received_time = stats["receivedDate_local"]
        distance = stats["distance"]
        baseurl = "https://www.postcrossing.com"
        if type == "sent":
            formatted_item = {
                "ID号": f"<a href='{baseurl}/postcards/{stats['id']}' target='_blank'>{stats['id']}</a>",
                "收信人": f"<a href='{baseurl}/user/{stats['user']}' target='_blank'>{stats['user']}</a>",
                "寄往地区": f"{stats['receivedCountry']} {stats['flagEmoji']}",
                "寄出时间(当地)": sent_time,
                "收到时间(当地)": received_time,
                "距离(km)": f'{format(distance, ",")}',
                "天数": travel_days,
            }
        elif type == "received":
            formatted_item = {
                "ID号": f"<a href='{baseurl}/postcards/{stats['id']}' target='_blank'>{stats['id']}</a>",
                "发信人": f"<a href='{baseurl}/user/{stats['user']}' target='_blank'>{stats['user']}</a>",
                "来自地区": f"{stats['sentCountry']} {stats['flagEmoji']}",
                "寄出时间(当地)": sent_time,
                "收到时间(当地)": received_time,
                "距离(km)": f'{format(distance, ",")} km',
                "天数": travel_days,
            }
        new_data.append(formatted_item)
        new_data = sorted(new_data, key=lambda x: x["收到时间(当地)"], reverse=True)
    html_content = htmlFormat(type, new_data)
    with open(f"./output/{type}.html", "w", encoding="utf-8") as file:
        file.write(html_content)


def htmlFormat(title, data):
    df = pd.DataFrame(data)
    # 修改索引从1开始
    df.index = df.index + 1
    # 将 DataFrame 转换为 HTML 表格，并添加 Bootstrap 的 CSS 类和居中对齐的属性
    html_table = df.to_html(
        classes="table table-striped table-bordered",
        escape=False,
        table_id="dataTable",
        header=True,
    )
    html_table = html_table.replace("<th>", '<th class="text-center">')
    html_table = html_table.replace("<td>", '<td class="text-center">')
    with open("./template/htmlFormat.html", "r", encoding="utf-8") as f:
        template = Template(f.read())
    html_content = template.render(title=title, html_table=html_table)
    return html_content


def picTowebp(input_dir, output_dir):
    # 获取input_dir目录下的所有文件名
    file_names = os.listdir(input_dir)
    for file_name in file_names:
        # 获取文件的完整路径
        file_path = os.path.join(input_dir, file_name)
        # 检查文件后缀名是否为.jpg、.jpeg或.png
        if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
            try:
                # 打开图片文件
                image = Image.open(file_path)
                # 构建输出文件的路径和文件名
                output_file_path = os.path.join(
                    output_dir, os.path.splitext(file_name)[0] + ".webp"
                )
                # 转换为webp格式并保存
                image.save(output_file_path, "webp")
                # 删除原有文件
                os.remove(file_path)
                print(f"文件 {file_name} 转换成功并已删除原有文件")
            except Exception as e:
                print(f"文件 {file_name} 转换失败: {str(e)}")


def createRegisterInfo(
    register_date, sent_info, received_info, countries, traveling, supporter_pic
):
    # 创建HTML内容
    with open("./template/registerInfo_template.html", "r", encoding="utf-8") as f:
        template = Template(f.read())

    html_content = template.render(
        register_date=register_date,
        sent_info=sent_info,
        received_info=received_info,
        countries=countries,
        traveling=traveling,
        supporter_pic=supporter_pic,
    )

    # 写入HTML文件
    with open("./output/registerInfo.html", "w", encoding="utf-8") as file:
        file.write(html_content)


if __name__ == "__main__":
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
    options = parser.parse_args()

    account = options.account
    nickName = options.nickName
    repo = options.repo

    font_path = "./scripts/font.otf"
    cn_path_svg = "./output/postcrossing_cn.svg"
    en_path_svg = "./output/postcrossing_en.svg"
    excel_file = "./template/postcardStory.xlsx"

    if os.path.exists(dbpath):
        shutil.copyfile(dbpath, f"{dbpath}BAK")
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
