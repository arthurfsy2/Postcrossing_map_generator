import pycountry
import json
from emojiflags.lookup import lookup as flag
from datetime import datetime, timedelta
import time
import os
from collections import Counter
from jinja2 import Template
from common_tools import db_path, read_db_table
import argparse
import toml

BIN = os.path.dirname(os.path.realpath(__file__))
config = toml.load("scripts/config.toml")
pic_driver_path = config.get("url").get("pic_driver_path")
personal_page_link = config.get("url").get("personal_page_link")


def read_template_file(lang="cn"):
    # 读取模板
    with open(
        os.path.join(BIN, f"../template/年度报告_template.txt"), "r", encoding="utf-8"
    ) as f:
        summary_template = Template(f.read())
    # 读取模板
    with open(
        os.path.join(BIN, f"../recap/template_{lang}.html"), "r", encoding="utf-8"
    ) as f:
        recap_template = Template(f.read())
    return summary_template, recap_template


def as_string(i: int) -> str:
    return "{:,}".format(i).replace(",", " ")


def country_alpha_to_str(alpha_2):
    return pycountry.countries.get(alpha_2=alpha_2).name.title() + " " + flag(alpha_2)


def get_year_record(year, card_type):
    def get_records(data, key, min_or_max):
        record = sorted(set([int(item.get(key)) for item in data]))
        if min_or_max == "min":
            return min(record)
        if min_or_max == "max":
            return max(record)
        if min_or_max == "sum":
            record = sorted([int(item.get(key)) for item in data])

            sum_data = sum(record)
            sum_data = format(sum_data, ",")
            return sum_data

    year_data = read_db_table(
        db_path, "map_info", {"card_type": card_type, "received_date": year}
    )

    # print(f"{year}_data_new0", year_data_new[0])
    # print(f"{year}_data_new-1", year_data_new[-1])

    # print("max_distance:", max_distance)
    # print("min_distance:", min_distance)
    countries_key = "sent_country" if card_type == "received" else "received_country"
    countries = [
        item.get(countries_key)
        for item in year_data
        if item.get(countries_key) is not None
    ]
    counts = Counter(countries)
    max_count = max(counts.values()) if counts else 0
    max_card_countries = [
        country for country, count in counts.items() if count == max_count
    ]
    max_card_country = " | ".join(max_card_countries)
    sum_distance = get_records(year_data, "distance", "sum")
    time_records = sorted(year_data, key=lambda x: int(x["travel_days"]))

    if not time_records:

        item = {
            "num": 0,
            "nearest_distance": 0,
            "longest_distance": 0,
            "nearest_country": 0,
            "nearest_country_flag_emoji": 0,
            "longest_country": 0,
            "longest_country_flag_emoji": 0,
            "max_card_country": 0,
            # "max_card_flag_emoji": max_card_flag_emoji,
            "sum_distance": 0,
        }
        return item
    elif card_type == "received":

        fast_record = time_records[0]
        slowest_record = time_records[-1]

        fastest_country_flag_emoji = read_db_table(
            db_path,
            "country_stats",
            {
                "name": fast_record.get("sent_country"),
            },
        )[0].get("flag_emoji")
        slowest_country_flag_emoji = read_db_table(
            db_path,
            "country_stats",
            {
                "name": slowest_record.get("sent_country"),
            },
        )[0].get("flag_emoji")
        item = {
            "num": len(year_data),
            "min_travel_days": fast_record.get("travel_days"),
            "max_travel_days": slowest_record.get("travel_days"),
            "fastest_country": fast_record.get("sent_country"),
            "fastest_country_flag_emoji": fastest_country_flag_emoji,
            "slowest_country": slowest_record.get("sent_country"),
            "slowest_country_flag_emoji": slowest_country_flag_emoji,
            "max_card_country": max_card_country,
            # "max_card_flag_emoji": max_card_flag_emoji,
            "sum_distance": sum_distance,
        }
    elif card_type == "sent":
        distance_records = sorted(year_data, key=lambda x: int(x["distance"]))
        nearest_record = distance_records[0]

        longest_record = distance_records[-1]
        # print("nearest_country:", nearest_record)
        # print("longest_record:", longest_record)
        nearest_country_flag_emoji = read_db_table(
            db_path,
            "country_stats",
            {
                "name": nearest_record.get("received_country"),
            },
        )[0].get("flag_emoji")
        longest_country_flag_emoji = read_db_table(
            db_path,
            "country_stats",
            {
                "name": longest_record.get("received_country"),
            },
        )[0].get("flag_emoji")
        item = {
            "num": len(year_data),
            "nearest_distance": format(nearest_record.get("distance"), ","),
            "longest_distance": format(longest_record.get("distance"), ","),
            "nearest_country": nearest_record.get("received_country"),
            "nearest_country_flag_emoji": nearest_country_flag_emoji,
            "longest_country": longest_record.get("received_country"),
            "longest_country_flag_emoji": longest_country_flag_emoji,
            "max_card_country": max_card_country,
            # "max_card_flag_emoji": max_card_flag_emoji,
            "sum_distance": sum_distance,
        }
    return item


def create_year_recap(lang):
    summary_template, recap_template = read_template_file(lang)
    db_data = read_db_table(db_path, "map_info")
    year_lists = [item.get("received_date").split("/")[0] for item in db_data]

    year_lists = sorted(set(year_lists), reverse=True)
    for year in year_lists:
        sent_record = get_year_record(year, "sent")
        received_record = get_year_record(year, "received")
        content = recap_template.render(
            year=year, sent_record=sent_record, received_record=received_record
        )

        with open(f"./recap/{year}_recap_{lang}.html", "w", encoding="utf-8") as recap:
            recap.write(content)
        print(f"已生成 ./recap/{year}_recap_{lang}.html")
    summary_content = summary_template.render(
        personal_page_link=personal_page_link, year_lists=year_lists, lang=lang
    )
    with open(f"./gallery/年度报告.md", "w", encoding="utf-8") as f:
        f.write(summary_content)
    print(f"已生成./gallery/年度报告.md")
    blog_path = r"D:\web\Blog\src\Arthur\Postcrossing\年度报告.md"

    # 换为你的blog的本地链接，可自动同步过去，方便测试
    if os.path.exists(blog_path):
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(summary_content)
        print(f"已生成 {os.path.abspath(blog_path)}")


if __name__ == "__main__":
    card_types = ["received", "sent"]

    # 示例调用
    directory_to_clean = "./data"
    files_to_keep = [".gitkeep"]
    create_year_recap("cn")
