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
from multi_download import get_account_stat, get_online_stats_data
from common_tools import (
    db_path,
    read_db_table,
    insert_or_update_db,
    translate,
)
import pytz
import shutil
from PIL import Image
import re
from jinja2 import Template
import toml
import toml

BIN = os.path.dirname(os.path.realpath(__file__))

config = toml.load("scripts/config.toml")
personal_page_link = config.get("url").get("personal_page_link")
Cookie = config.get("settings").get("Cookie")
pic_driver_path = config.get("url").get("pic_driver_path")
story_pic_link = config.get("url").get("story_pic_link")
story_pic_type = config.get("settings").get("story_pic_type")


def read_template_file():
    # 读取模板
    with open(
        os.path.join(BIN, f"../template/card_type.html"),
        "r",
        encoding="utf-8",
    ) as f:
        card_type_template = Template(f.read())

    with open(
        os.path.join(BIN, f"../template/信息汇总_template.txt"), "r", encoding="utf-8"
    ) as f:
        summary_template = Template(f.read())
    with open(
        os.path.join(BIN, f"../template/register_info_template.html"),
        "r",
        encoding="utf-8",
    ) as f:
        register_info_template = Template(f.read())
    return card_type_template, summary_template, register_info_template


def update_sheet_data(excel_file):
    import warnings

    warnings.filterwarnings("ignore", category=FutureWarning)
    df = pd.read_excel(excel_file)
    for index, row in df.iterrows():
        item = {
            "card_id": row[0],
            "content_original": row[1],
            "content_cn": row[2],
            "comment_original": row[3],
            "comment_cn": row[4],
        }
        insert_or_update_db(db_path, "postcard_story", item)


def get_calendar_list():
    online_stats_data = get_online_stats_data(account)
    calendar_list = []

    for data in online_stats_data:
        timestamp = data[0]  # 获取时间戳
        date = datetime.fromtimestamp(timestamp)  # 将时间戳转换为日期格式
        year = date.strftime("%Y")  # 提取年份（YYYY）
        if year not in calendar_list:
            calendar_list.append(year)
    calendar_list = sorted(calendar_list, reverse=True)
    return calendar_list


def create_word_cloud(type, contents):
    keywords_old = []
    old_key_word_path = os.path.join(BIN, f"../output/keyword_old_{type}.txt")
    contents = contents.replace("nan", "")
    exclude_keywords = []  # 直接在这里指定排除的关键字
    if os.path.exists(old_key_word_path):

        with open(old_key_word_path, "r", encoding="utf-8") as f:
            keywords_old = [line.strip() for line in f.readlines()]
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

    only_in_keywords = set(keywords) - set(keywords_old)
    only_in_keywords_old = set(keywords_old) - set(keywords)

    if not (only_in_keywords or only_in_keywords_old):
        print(f"keyword_{type}无更新，终止任务")
        return
    # 生成词云

    with open(old_key_word_path, "w", encoding="utf-8") as f:
        for keyword in keywords:
            f.write(f"{keyword}\n")
        print(f"已更新：{old_key_word_path}")
    svg_image = wordcloud.to_svg(embed_font=True)

    with open(path, "w+", encoding="UTF8") as f:
        f.write(svg_image)
        print(f"已保存至{path}")


def read_story_db(db_path):
    result_cn = ""
    result_en = ""
    content = read_db_table(db_path, "postcard_story")
    for item in content:

        map_info_data = read_db_table(
            db_path, "map_info", {"card_id": item.get("card_id")}
        )
        if map_info_data:
            item.update(map_info_data[0])
        content_original = item.get("content_original", "")
        content_cn = item.get("content_cn", "")
        comment_original = item.get("comment_original", "")
        comment_cn = item.get("comment_cn", "")
        data_en = f"{content_original}\n{comment_original}\n"
        data_cn = f"{content_cn}\n{comment_cn}\n"
        result_en += data_en
        result_cn += data_cn
    # print("result_en:", result_en)
    # print("result_cn:", result_cn)
    return result_cn.replace("None", ""), result_en.replace("None", "")


# 实时获取该账号所有sent、received的明信片列表，获取每个postcardID的详细数据


def get_traveling_id(account, card_type, Cookie):
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
        "Referer": f"https://www.postcrossing.com/user/{account}/{card_type}",
        "Cookie": Cookie,
        "Sec-Fetch-Dest": "empty",
    }
    url = f"https://www.postcrossing.com/user/{account}/data/{card_type}"
    response = requests.get(url, headers=headers).json()
    expiredCount = sum(1 for item in response if item[7] > 60)
    travelingCount = len(response)
    content = sorted(response, key=lambda x: x[7])
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

    extra_info = []
    for i, stats in enumerate(content):
        sent_avg = 0
        baseurl = "https://www.postcrossing.com"
        country_stats_data = read_db_table(
            db_path, "country_stats", {"country_code": stats[3]}
        )
        country_list = read_db_table(
            db_path, "country_list", {"country_code": stats[3]}
        )

        if country_stats_data:
            sent_avg = country_stats_data[0].get("sent_avg")
        # print("country_stats_data:", country_stats_data)
        if int(stats[7]) >= 60:
            traveling_days = f'<span style="color: red;">{stats[7]}</span>'
        elif int(stats[7]) > int(sent_avg):
            traveling_days = f'<span style="color: orange;">{stats[7]}</span>'
        else:
            traveling_days = f'<span style="color: green;">{stats[7]}</span>'

        item = {
            "card_id": f"<a href='{baseurl}/travelingpostcard/{stats[0]}' target='_blank'>{stats[0]}</a>",
            "sender": f"<a href='{baseurl}/user/{stats[1]}' target='_blank'>{stats[1]}</a>",
            "country_name": f"{country_list[0].get("country_name")} {country_list[0].get("country_name_emoji")}",
            "sent_local_date": get_local_date(stats[0][0:2], stats[4]),
            "distance": f'{format(stats[6], ",")}',
            "traveling_days": traveling_days,
            "sent_avg": f"{sent_avg}",
        }
        extra_info.append(item)

    html_content = card_type_template.render(
        card_type=card_type, content=extra_info, baseurl=baseurl
    )

    with open(f"./output/{card_type}.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    return travelingCount, expiredCount


def get_HTML_table(card_type, table_name):
    content = read_db_table(db_path, table_name, {"card_type": card_type})

    baseurl = "https://www.postcrossing.com"
    for i, stats in enumerate(content):
        # print("stats:", stats)
        country_key = "sent" if card_type == "received" else "received"
        country_stats_data = read_db_table(
            db_path, "country_stats", {"name": stats.get(f"{country_key}_country")}
        )
        if country_stats_data:
            stats.update(country_stats_data[0])
        stats["distance"] = format(stats.get("distance"), ",")

    title_name = read_db_table(db_path, "title_info", {"card_type": card_type})[0]
    content = sorted(content, key=lambda x: x["received_date_local"], reverse=True)
    html_content = card_type_template.render(
        card_type=card_type, content=content, title_name=title_name, baseurl=baseurl
    )

    with open(f"./output/{card_type}.html", "w", encoding="utf-8") as file:
        file.write(html_content)


def pic_to_webp(input_dir, output_dir):
    """
    获取input_dir目录下的所有文件名
    """
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


def create_register_info():
    """
    生成register_info.html
    """

    def get_user_sheet(table_name):
        content = read_db_table(db_path, table_name)

        countryCount = len(content)
        content = sorted(content, key=lambda x: x["name"])
        html_content = card_type_template.render(
            card_type=table_name,
            content=content,
        )
        with open(f"./output/{table_name}.html", "w", encoding="utf-8") as file:
            file.write(html_content)

        return countryCount

    countryNum = get_user_sheet("country_stats")
    countries = f"{countryNum}/248 [{round(countryNum/248*100,2)}%]"
    travelingNum, expiredNum = get_traveling_id(account, "traveling", Cookie)
    traveling = f"{travelingNum} [过期：{expiredNum}]"
    # 创建HTML内容
    item = read_db_table(db_path, "user_summary")[0]
    item["sent_distance"] = format(int(item.get("sent_distance")), ",")
    item["received_distance"] = format(int(item.get("received_distance")), ",")
    item.update(
        {
            "countries": countries,
            "traveling": traveling,
        }
    )

    html_content = register_info_template.render(item=item)

    # 写入HTML文件
    with open("./output/register_info.html", "w", encoding="utf-8") as file:
        file.write(html_content)


def create_summary_text():
    """
    生成信息汇总.md
    """
    stat, content_raw, card_types = get_account_stat(account, Cookie)

    def get_card_type_data(card_type):

        data_list = read_db_table(db_path, "map_info", {"card_type": card_type})
        new_list = []
        for item in data_list:
            # g关联country_stats表数据
            country_stats_data = read_db_table(
                db_path,
                "country_stats",
                {
                    "name": (
                        item.get("sent_country")
                        if card_type == "received"
                        else item.get("received_country")
                    )
                },
            )
            if country_stats_data:
                item.update(country_stats_data[0])

            # 处理经纬度
            from_coor = json.loads(item.get("from_coor"))
            to_coor = json.loads(item.get("to_coor"))

            from_coor0 = from_coor[0] if from_coor else ""
            from_coor1 = from_coor[1] if from_coor else ""

            to_coor0 = to_coor[0] if to_coor[0] else ""
            to_coor1 = to_coor[1] if to_coor[1] else ""

            item.update(
                {
                    "from_coor0": from_coor0,
                    "from_coor1": from_coor1,
                    "to_coor0": to_coor0,
                    "to_coor1": to_coor1,
                }
            )
            item["distance"] = format(item.get("distance"), ",")

            # 关联postcard_story数据
            postcard_story = read_db_table(
                db_path, "postcard_story", {"card_id": item.get("card_id")}
            )
            if postcard_story:
                item.update(postcard_story[0])

            # 关联gallery_info数据
            gallery_info = read_db_table(
                db_path, "gallery_info", {"card_id": item.get("card_id")}
            )
            if gallery_info:
                item.update(gallery_info[0])

            if any(
                [
                    item.get("content_original"),
                    item.get("content_cn"),
                    item.get("comment_original"),
                    item.get("comment_cn"),
                ]
            ):

                new_list.append(item)
        # print(f"new_list({len(new_list)}):", len(new_list))

        content = {}
        for item in new_list:
            received_year = item["received_date"].split("/")[0]
            if received_year not in content:
                content[received_year] = []
            content[received_year].append(item)
        for year in content:
            content[year] = sorted(
                content[year], key=lambda x: x["received_date"], reverse=True
            )
        content = dict(sorted(content.items(), key=lambda x: x[0], reverse=True))

        # with open("./year_data.json", "w", encoding="utf-8") as f:
        #     json.dump(content, f, ensure_ascii=False, indent=2)

        return content, len(new_list)

    user_summary = read_db_table(
        db_path,
        "user_summary",
    )[0]

    title_all = ""
    for card_type in card_types:
        title_info = read_db_table(db_path, "title_info", {"card_type": card_type})[0]
        title_name = title_info.get("title_name")
        title_all += f"#### [{title_name}](/{nick_name}/postcrossing/{card_type})\n\n"

        title_final = f"{title_all}"

    calendar_list = get_calendar_list()
    comment_list, comment_num = get_card_type_data("sent")
    story_list, story_num = get_card_type_data("received")
    dataNew = summary_template.render(
        account=account,
        pic_driver_path=pic_driver_path,
        story_pic_link=story_pic_link,
        nick_name=nick_name,
        user_summary=user_summary,
        story_pic_type=story_pic_type,
        personal_page_link=personal_page_link,
        title_final=title_final,
        story_list=story_list,
        story_num=story_num,
        comment_list=comment_list,
        comment_num=comment_num,
        calendar_list=calendar_list,
        repo=repo,
    )
    print(f"已更新信息汇总.md")
    print(f"————————————————————")

    with open(f"./gallery/信息汇总.md", "w", encoding="utf-8") as f:
        f.write(dataNew)

    blog_path = r"D:\web\Blog\src\Arthur\Postcrossing\信息汇总.md"

    # 换为你的blog的本地链接，可自动同步过去，方便测试
    if os.path.exists(blog_path):
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(dataNew)


if __name__ == "__main__":
    card_type_template, summary_template, register_info_template = read_template_file()

    # nick_name = data["nick_name"]

    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser()
    parser.add_argument("account", help="输入account")
    parser.add_argument("nick_name", help="输入nickName")
    parser.add_argument("repo", help="输入repo1")
    options = parser.parse_args()

    account = options.account
    nick_name = options.nick_name
    repo = options.repo

    font_path = "./scripts/font.otf"
    cn_path_svg = "./output/postcrossing_cn.svg"
    en_path_svg = "./output/postcrossing_en.svg"
    excel_file = "./template/postcard_story.xlsx"

    pic_to_webp("./template/rawPic", "./template/content")
    excel_file = "./template/postcard_story.xlsx"
    update_sheet_data(excel_file)
    get_HTML_table("sent", "map_info")
    get_HTML_table("received", "map_info")
    create_register_info()

    create_summary_text()

    # 生成词云
    result_cn, result_en = read_story_db(db_path)
    create_word_cloud("cn", result_cn)
    create_word_cloud("en", result_en)
