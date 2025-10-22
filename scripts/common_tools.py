import requests
import json
import sqlite3
import os
import hashlib
import sys
import argparse
from urllib import parse, request
import pytz
from datetime import datetime, timedelta
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import (
    create_engine,
    Column,
    String,
    Float,
    DateTime,
    Integer,
    JSON,
    and_,
    Date,
    PrimaryKeyConstraint,
)
import toml

config = toml.load("scripts/config.toml")
Cookie = config.get("settings").get("Cookie")
pic_driver_path = config.get("url").get("pic_driver_path")


def initialize_database(Base, db_path):
    engine = create_engine(f"sqlite:///{db_path}")
    Base.metadata.create_all(engine)  # 创建所有定义的表


Base = declarative_base()
BIN = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.abspath(os.path.join(BIN, "../template/postcrossing.db"))

initialize_database(Base, db_path)


class countryList(Base):
    __tablename__ = "country_list"
    country_code = Column(String, primary_key=True)
    country_name = Column(String)
    country_name_emoji = Column(String)


class titleInfo(Base):
    __tablename__ = "title_info"
    card_type = Column(String, primary_key=True)
    from_or_to = Column(String)
    page_num = Column(String)
    card_num = Column(String)
    title_name = Column(String)


class mapInfo(Base):
    __tablename__ = "map_info"

    card_id = Column(String, primary_key=True)
    from_coor = Column(String)
    to_coor = Column(String)
    distance = Column(String)
    travel_days = Column(Integer)
    sent_date = Column(String)
    received_date = Column(String)
    link = Column(String)
    user = Column(String)
    sent_addr = Column(String)
    sent_country = Column(String)
    received_addr = Column(String)
    received_country = Column(String)
    sent_date_local = Column(String)
    received_date_local = Column(String)
    card_type = Column(String)


class countryStat(Base):
    __tablename__ = "country_stats"

    name = Column(String, primary_key=True)
    country_code = Column(String)
    flag_emoji = Column(String)
    value = Column(Integer)
    sent_num = Column(Integer)
    received_num = Column(Integer)
    sent_avg = Column(Float)
    received_avg = Column(Float)
    sent_median = Column(Float)
    received_median = Column(Float)
    sent_history = Column(String)
    received_history = Column(String)
    sent_date_history = Column(String)
    received_date_history = Column(String)
    sent_date_first = Column(String)
    received_date_first = Column(String)


class userSummary(Base):
    __tablename__ = "user_summary"

    account = Column(String, primary_key=True)
    about = Column(String)
    coors = Column(String)
    sent_distance = Column(String)
    sent_laps = Column(String)
    sent_postcard_num = Column(String)
    received_distance = Column(String)
    received_laps = Column(String)
    received_postcard_num = Column(String)
    registered_years = Column(String)
    registered_days = Column(String)
    register_date = Column(String)
    logo = Column(String)
    is_supporter = Column(String)


class galleryInfo(Base):
    __tablename__ = "gallery_info"

    card_id = Column(String)
    user_info = Column(String)
    country_name_emoji = Column(String)
    pic_file_name = Column(String)
    favorites_num = Column(String)
    card_type = Column(String)

    __table_args__ = (PrimaryKeyConstraint("card_id", "card_type"),)


class postcardStory(Base):
    __tablename__ = "postcard_story"
    card_id = Column(String, primary_key=True)
    content_original = Column(String)
    content_cn = Column(String)
    comment_original = Column(String)
    comment_cn = Column(String)


def insert_or_update_db(db_path, table_name, data):
    """
    设置写入数据库的统一入口函数
    """
    initialize_database(Base, db_path)

    def get_table_data(table_name, data):
        if table_name == "user_summary":
            # 过滤掉不需要的字段，比如 primary_key
            table_data = userSummary(
                **{
                    key: value
                    for key, value in data.items()
                    if key in userSummary.__dict__
                }
            )
        elif table_name == "gallery_info":
            table_data = galleryInfo(
                **{
                    key: value
                    for key, value in data.items()
                    if key in galleryInfo.__dict__
                }
            )
        elif table_name == "country_stats":
            table_data = countryStat(
                **{
                    key: value
                    for key, value in data.items()
                    if key in countryStat.__dict__
                }
            )
        elif table_name == "map_info":
            table_data = mapInfo(
                **{key: value for key, value in data.items() if key in mapInfo.__dict__}
            )
        elif table_name == "postcard_story":
            table_data = postcardStory(
                **{
                    key: value
                    for key, value in data.items()
                    if key in postcardStory.__dict__
                }
            )
        elif table_name == "title_info":
            table_data = titleInfo(
                **{
                    key: value
                    for key, value in data.items()
                    if key in titleInfo.__dict__
                }
            )
        elif table_name == "country_list":
            table_data = countryList(
                **{
                    key: value
                    for key, value in data.items()
                    if key in countryList.__dict__
                }
            )
        return table_data

    engine = create_engine(f"sqlite:///{db_path}")
    Session = sessionmaker(bind=engine)
    session = Session()

    table_data = get_table_data(table_name, data)

    session.merge(table_data)
    session.commit()
    session.close()


def read_db_table(db_path, table_name, filters=None):
    """
    设置读取数据库的统一入口函数
    """
    engine = create_engine(f"sqlite:///{db_path}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # 根据 table_name 动态读取不同的数据表
    query_result = None
    if table_name == "map_info":
        query = session.query(mapInfo)
    elif table_name == "country_stats":
        query = session.query(countryStat)
    elif table_name == "user_summary":
        query = session.query(userSummary)
    elif table_name == "gallery_info":
        query = session.query(galleryInfo)
    elif table_name == "postcard_story":
        query = session.query(postcardStory)
    elif table_name == "title_info":
        query = session.query(titleInfo)
    elif table_name == "country_list":
        query = session.query(countryList)
    if filters:
        for key, value in filters.items():
            # 使用like来进行“包含”匹配
            query = query.filter(
                getattr(query.column_descriptions[0]["entity"], key).like(f"%{value}%")
            )

    query_result = query.all()
    # 将结果转换为字典
    data = [row.__dict__ for row in query_result]

    # 移除 SQLAlchemy 额外的信息
    for item in data:
        item.pop("_sa_instance_state", None)

    session.close()
    return data


def md5(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
        md5_hash = hashlib.md5(data).hexdigest()
    return md5_hash


def compareMD5(pathA, pathB):

    A_md5 = md5(pathA)
    B_md5 = md5(pathB)
    if B_md5 == A_md5:
        stat = "0"
    else:
        stat = "1"
    # print(f"\n{pathA}:{A_md5}\n{pathB}:{B_md5}")
    return stat


def translate(apikey, sentence, src_lan, tgt_lan):
    url = "http://api.niutrans.com/NiuTransServer/translation?"
    data = {
        "from": src_lan,
        "to": tgt_lan,
        "apikey": apikey,
        "src_text": sentence.encode("utf-8"),
    }
    data_en = parse.urlencode(data)
    req = url + "&" + data_en
    res = request.urlopen(req)
    res_dict = json.loads(res.read())
    if "tgt_text" in res_dict:
        result = res_dict["tgt_text"]
    else:
        result = res
    return result


def get_country_city(latitude, longitude, timestamp):
    country_city = None  # 初始化变量
    url = f"https://timezones.datasette.io/timezones/by_point.json?longitude={longitude}&latitude={latitude}"
    response = requests.get(url=url)
    if response:
        try:
            country_city = response.json()["rows"][0][0]
        except Exception as e:
            print("response:", response)
    return country_city


def get_local_date(coors, utc_date):
    latitude = coors[0]
    longitude = coors[1]
    time_utc = datetime.strptime(utc_date, "%Y/%m/%d %H:%M")
    timestamp = int(time_utc.timestamp())
    country_city = get_country_city(latitude, longitude, timestamp)
    # 根据国家城市英文名称获取对应的时区
    try:
        timezone = pytz.timezone(country_city)
    except pytz.UnknownTimeZoneError:
        return "Invalid country city"

    # 将输入的UTC日期转换为datetime对象
    input_format = "%Y/%m/%d %H:%M"
    utc_datetime = datetime.strptime(utc_date, input_format)

    # 将UTC时间转换为指定时区的本地时间
    local_datetime = pytz.utc.localize(utc_datetime).astimezone(timezone)

    # 提取本地日期
    local_date = local_datetime.date()
    # 格式化本地日期和时间
    output_format = "%Y/%m/%d %H:%M"
    local_datetime_str = local_datetime.strftime(output_format)
    return local_datetime_str


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("account", help="输入account")
    parser.add_argument("password", help="输入password")
    parser.add_argument("nick_name", help="输入nickName")
    # parser.add_argument("Cookie", help="输入Cookie")
    parser.add_argument("repo", help="输入repo")
    options = parser.parse_args()

    account = options.account
    password = options.password
    nick_name = options.nick_name
    # Cookie = options.Cookie
    repo = options.repo
    url = f"https://www.postcrossing.com/user/{account}/gallery"
    userUrl = f"https://www.postcrossing.com/user/{account}"
    galleryUrl = f"{userUrl}/gallery"  # 设置该账号的展示墙
    dataUrl = f"{userUrl}/data/sent"
    types_map = ["sent", "received"]

    headers = {
        "authority": "www.postcrossing.com",
        "Cookie": Cookie,
    }
