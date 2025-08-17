from datetime import datetime
import json
import time
from multi_download import PicDataCheck
from common_tools import db_path, read_db_table, insert_or_update_db, compareMD5
import os
import shutil
import argparse
import re
from jinja2 import Template

BIN = os.path.dirname(os.path.realpath(__file__))

with open("scripts/config.json", "r") as file:
    data = json.load(file)
# account = data["account"]
# nick_name = data["nick_name"]
Cookie = data["Cookie"]
pic_driver_path = data["pic_driver_path"]


def read_template_file():
    # 读取模板
    with open(
        os.path.join(BIN, f"../template/type_template.txt"),
        "r",
        encoding="utf-8",
    ) as f:
        gallery_template = Template(f.read())

    with open(
        os.path.join(BIN, f"../template/type_frontmatter_template.txt"),
        "r",
        encoding="utf-8",
    ) as f:
        frontmatter_template = Template(f.read())
    return gallery_template, frontmatter_template


def create_summary_text(data_list, frontmatter, card_type):

    def create_gallery_summary_md(data):

        gallery_info_data = read_db_table(
            db_path,
            "gallery_info",
            {"card_id": data.get("card_id"), "card_type": card_type},
        )
        if gallery_info_data:
            data.update(gallery_info_data[0])
        # start_date = data.get("received_date").split(" ")[0]
        # print("正在合并md数据：", start_date)
        if data.get("distance"):
            data["distance"] = format(data.get("distance"), ",")
            # if data.get("from_coor"):

            from_coor = json.loads(data.get("from_coor"))
            to_coor = json.loads(data.get("to_coor"))

            from_coor0 = from_coor[0] if from_coor else ""
            from_coor1 = from_coor[1] if from_coor else ""

            to_coor0 = to_coor[0] if to_coor[0] else ""
            to_coor1 = to_coor[1] if to_coor[1] else ""
            summary_output = gallery_template.render(
                card_type=card_type,
                data=data,
                # from_or_to=from_or_to,
                from_coor0=from_coor0,
                from_coor1=from_coor1,
                to_coor0=to_coor0,
                to_coor1=to_coor1,
            )
        else:
            summary_output = gallery_template.render(
                card_type=card_type,
                data=data,
                # from_or_to=from_or_to,
            )
        return summary_output

    year_data = {}  # 改为字典
    for i, data in enumerate(data_list, start=1):
        summary_single_text = create_gallery_summary_md(data)
        year = data.get("received_date", "其他").split("/")[0]
        if year not in year_data:
            year_data[year] = []  # 初始化为列表
        year_data[year].append(summary_single_text)
    summary_text = ""
    for year in year_data:
        summary_output = "\n\n".join(year_data[year])
        summary_text += f"\n\n### {year}({len(year_data[year])})\n\n" + summary_output
    summary_text = frontmatter + summary_text
    return summary_text


def create_gallery_md(sorted_data_list, card_type):
    title_name = read_db_table(db_path, "title_info", {"card_type": card_type})[0]
    last_record = sorted_data_list[0]
    last_date = ""
    if last_record.get("received_date"):
        last_date = last_record.get("received_date").split(" ")[0].replace("/", "-")

    frontmatter = frontmatter_template.render(
        last_date=last_date,
        card_type=card_type,
        num=str(num),
        repo=repo,
        title_name=title_name.get("title_name"),
    )
    summary_text = create_summary_text(sorted_data_list, frontmatter, card_type)
    output_path = os.path.join(BIN, "../gallery", f"{card_type}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary_text)
    print("已导出：", os.path.abspath(output_path))
    blog_path = r"D:\web\Blog\src\Arthur\Postcrossing"
    if os.path.exists(blog_path):
        summary_output_path = os.path.join(blog_path, f"{card_type}.md")
        with open(summary_output_path, "w", encoding="utf-8") as f:
            f.write(summary_text)
        print("已导出：", summary_output_path)


if __name__ == "__main__":
    start_time = time.time()
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser()
    parser.add_argument("account", help="输入account")
    # parser.add_argument("password", help="输入password")
    parser.add_argument("nick_name", help="输入nickName")
    # parser.add_argument("Cookie", help="输入Cookie")
    parser.add_argument("repo", help="输入repo")
    options = parser.parse_args()

    account = options.account
    # password = options.password
    nick_name = options.nick_name
    # Cookie = options.Cookie
    repo = options.repo

    gallery_types = ["sent", "received", "favourites", "popular"]
    gallery_template, frontmatter_template = read_template_file()
    sort_key = {
        "sent": "received_date",
        "received": "received_date_local",
        "favourites": "received_date_local",
        "popular": "received_date",
    }
    for card_type in gallery_types:
        title_data = read_db_table(db_path, "title_info", {"card_type": card_type})

        # from_or_to, page_num, Num, title = title_data.get(card_type)
        num = gallery_types.index(card_type) + 2
        data_list = read_db_table(db_path, "map_info", {"card_type": card_type})

        if card_type in ["favourites", "popular"]:

            data_list = read_db_table(db_path, "gallery_info", {"card_type": card_type})

            # 关联其他表信息
            for data in data_list:
                data.update(title_data[0])
                map_info_data = read_db_table(
                    db_path, "map_info", {"card_id": data.get("card_id")}
                )

                if map_info_data:
                    data.update(map_info_data[0])

                else:
                    data.update({"received_date_local": ""})
                country_stats_data = read_db_table(
                    db_path, "country_stats", {"name": data.get("received_country")}
                )

                if country_stats_data:
                    data.update(country_stats_data[0])

        else:
            for data in data_list:
                data.update(title_data[0])
            data_list = [
                item for item in data_list if "noPic.png" not in item["link"]
            ]  # 或根据具体条件过滤
        sorted_data_list = sorted(
            data_list,
            key=lambda item: item[sort_key.get(card_type)],
            reverse=True,
        )
        create_gallery_md(sorted_data_list, card_type)
    end_time = time.time()
    execution_time = round((end_time - start_time), 3)
    print(f"create_gallery.py脚本执行时间：{execution_time}秒\n")
