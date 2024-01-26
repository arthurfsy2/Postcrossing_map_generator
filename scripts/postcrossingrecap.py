import pycountry
import json
from emojiflags.lookup import lookup as flag
from datetime import datetime, timedelta
import time
import os
from collections import Counter

with open("scripts/config.json", "r") as file:
    data = json.load(file)
personalPageLink = data["personalPageLink"]


def getYearList(type):
    # 读取received.json文件
    with open(f'data/{type}.json', 'r') as file:
        data_raw = json.load(file)
    year_list = []

    for data in data_raw:
        timestamp = data[5]  # 获取时间戳
        date = datetime.fromtimestamp(timestamp)  # 将时间戳转换为日期格式
        year = date.strftime("%Y")  # 提取年份（YYYY）
        if year not in year_list:
            year_list.append(year)
    return year_list


def getYearData(type, year):
    # 读取received.json文件
    with open(f'data/{type}.json', 'r') as file:
        data_raw = json.load(file)
    # 创建一个空列表来存储符合条件的子数组
    yearData = []

    # 遍历receivedData中的每个子数组
    for item in data_raw:
        # 将时间戳转换为年份
        timestamp = item[5]
        date = datetime.fromtimestamp(timestamp)  # 将时间戳转换为日期格式
        timestamp_year = date.strftime("%Y")  # 提取年份（YYYY）

        # 如果时间戳的年份与输入的年份相同，则保留该子数组
        if timestamp_year == year:
            yearData.append(item)

    # # 确保输出目录存在
    # output_dir = f"./data"
    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)

    # 将筛选后的数据输出到指定的JSON文件中
    with open(f"./data/{type}_{year}.json", 'w') as outfile:
        json.dump(yearData, outfile, indent=2)

# 调用函数示例


def createCalendar():
    with open("data/.json", "r") as file:
        a_data = json.load(file)
    year_list = []

    for data in a_data:
        timestamp = data[5]  # 获取时间戳
        date = datetime.fromtimestamp(timestamp)  # 将时间戳转换为日期格式
        year = date.strftime("%Y")  # 提取年份（YYYY）
        if year not in year_list:
            year_list.append(year)


def as_string(i: int) -> str:
    return "{:,}".format(i).replace(",", " ")


def country_alpha_to_str(alpha_2):
    return pycountry.countries.get(alpha_2=alpha_2).name.title() + " " + flag(alpha_2)


class CardInfo:
    def __init__(self, data_card) -> None:
        self.id = data_card[0]
        self.other = data_card[1]
        self.country_code = data_card[3]
        self.posted = data_card[4]
        self.arrived = data_card[5]
        self.kilometers = data_card[6]
        self.days = data_card[7]


def createYearRecap(year, lang):
    cards_sent = []
    cards_received = []
    with open(f'data/sent_{year}.json', 'r') as sent_file:
        sents = json.load(sent_file)
        for s in sents:
            cards_sent.append(CardInfo(s))
    with open(f'data/received_{year}.json', 'r') as received_file:
        receiveds = json.load(received_file)
        for s in receiveds:
            cards_received.append(CardInfo(s))

    from_number = len(cards_received)
    from_quickest_days = 1000
    from_quickest_country = ""
    from_slowest_days = 0
    from_slowest_country = ""
    from_km_traveled = 0
    c_best_countries = Counter()
    for c in cards_received:
        from_km_traveled += c.kilometers
        c_best_countries[c.country_code] += 1
        if c.days < from_quickest_days:
            from_quickest_days = c.days
            from_quickest_country = country_alpha_to_str(c.country_code)
        if c.days > from_slowest_days:
            from_slowest_days = c.days
            from_slowest_country = country_alpha_to_str(c.country_code)
    from_best_country = c_best_countries.most_common(1)[0][0]
    from_best_country = country_alpha_to_str(from_best_country)

    to_number = len(cards_sent)
    to_max_km = 0
    to_max_country = ""
    to_min_km = 10000000
    to_min_country = ""
    c_best_countries = Counter()
    to_km_traveled = 0
    for c in cards_sent:
        to_km_traveled += c.kilometers
        c_best_countries[c.country_code] += 1
        if c.kilometers > to_max_km:
            to_max_km = c.kilometers
            to_max_country = country_alpha_to_str(c.country_code)
        if c.kilometers < to_min_km:
            to_min_km = c.kilometers
            to_min_country = country_alpha_to_str(c.country_code)
    to_best_country = c_best_countries.most_common(1)[0][0]
    to_best_country = country_alpha_to_str(to_best_country)

    with open(f"./recap/template_{lang}.html", 'r', encoding="utf-8") as temp:
        html = temp.read()
    html = html.replace("$$FROM_NUMBER$$", as_string(from_number))
    html = html.replace("$$FROM_QUICKEST_DAYS$$",
                        as_string(from_quickest_days))
    html = html.replace("$$FROM_QUICKEST_COUNTRY$$", from_quickest_country)
    html = html.replace("$$FROM_SLOWEST_DAYS$$", as_string(from_slowest_days))
    html = html.replace("$$FROM_SLOWEST_COUNTRY$$", from_slowest_country)
    html = html.replace("$$FROM_BEST_COUNTRY$$", from_best_country)
    html = html.replace("$$FROM_KM_TRAVELED$$", as_string(from_km_traveled))

    html = html.replace("$$TO_NUMBER$$", as_string(to_number))
    html = html.replace("$$TO_MAX_KM$$", as_string(to_max_km))
    html = html.replace("$$TO_MAX_COUNTRY$$", to_max_country)
    html = html.replace("$$TO_MIN_KM$$", as_string(to_min_km))
    html = html.replace("$$TO_MIN_COUNTRY$$", to_min_country)
    html = html.replace("$$TO_BEST_COUNTRY$$", to_best_country)
    html = html.replace("$$TO_KM_TRAVELED$$", as_string(to_km_traveled))
    html = html.replace("$$YEAR$$", year)
    with open(f"./recap/{year}_recap_{lang}.html", 'w', encoding="utf-8") as recap:
        recap.write(html)
    print(f"已生成 ./recap/{year}_recap_{lang}.html")


def remove_other_files(directory, keep_files):
    # 列出目录下的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # 检查文件是否在保留列表中
        if filename not in keep_files and os.path.isfile(file_path):
            # 如果不在保留列表中且是文件，则删除
            os.remove(file_path)
            # print(f"Deleted: {file_path}")


def replaceTemplate(yearlist):
    yearlist = sorted(yearlist, reverse=True)
    link_all = ""
    for year in yearlist:
        link = f"""@tab {year}\n\n<iframe src="$personalPageLink/recap/{year}_recap_cn.html" frameborder=0 height=500 width=100% seamless=seamless scrolling=auto></iframe>\n\n"""
        link_all += link.replace('$personalPageLink', personalPageLink)
    with open(f"./template/年度报告_template.md", "r", encoding="utf-8") as f:
        data = f.read()
        dataNew = data.replace('$link', link_all)

    with open(f"./gallery/年度报告.md", "w", encoding="utf-8") as f:
        f.write(dataNew)
    print(f"./gallery/年度报告.md")
    blog_path = r"D:\web\Blog\src\Arthur\Postcrossing\年度报告.md"

    # 换为你的blog的本地链接，可自动同步过去，方便测试
    if os.path.exists(blog_path):
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(dataNew)


types = ['received', 'sent']
for type in types:
    yearlist = getYearList(type)
    for year in yearlist:
        getYearData(type, year)
    print(f"————————————————————")

# 示例调用
directory_to_clean = './data'
files_to_keep = ['.gitkeep']

yearlist = getYearList("sent")
for year in yearlist:
    createYearRecap(year, "cn")
remove_other_files(directory_to_clean, files_to_keep)
replaceTemplate(yearlist)
