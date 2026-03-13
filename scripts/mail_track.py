from imap_tools import MailBox, AND
from imap_tools.errors import *
import re
import json
from urllib import parse, request
import sqlite3
import os
from common_tools import (
    translate,
    db_path,
    insert_or_update_db,
    read_db_table,
    remove_blank_lines,
)
from ai_tool import translate_by_gemini
import argparse
import time
from concurrent.futures import ThreadPoolExecutor
import toml

import os

BIN = os.path.dirname(os.path.realpath(__file__))
COOKIE_CONFIG_FILE = os.path.join(BIN, ".cookie_config.toml")

config = toml.load("scripts/config.toml")
# 优先从环境变量读取 Cookie，其次从 Cookie 配置文件
Cookie = os.environ.get("POSTCROSSING_COOKIE", "")
if not Cookie and os.path.exists(COOKIE_CONFIG_FILE):
    cookie_config = toml.load(COOKIE_CONFIG_FILE)
    Cookie = cookie_config.get("auth", {}).get("cookie", "")
pic_driver_path = config.get("url").get("pic_driver_path")

parser = argparse.ArgumentParser()


parser.add_argument(
    "input_string", help="输入host//user//passwd//filename,以英文逗号‘,’隔开"
)
parser.add_argument("apikey", help="输入小牛翻译apikey")
options = parser.parse_args()


input_string = options.input_string
apikey = options.apikey


def process_message(msg):

    online_card_id = re.search(r"Hurray! Your postcard (.*?) to", msg.subject).group(1)

    story_data = read_db_table(db_path, "postcard_story", {"card_id": online_card_id})

    if not story_data:  # 只翻译新的内容
        match = re.search(r"“([\s\S]*?)”", msg.text)
        match = match.group(1)
        print("new card id:", online_card_id)
        comment_original = remove_blank_lines(match)
        # 以下是使用小牛翻译api
        # comment_cn = translate(apikey, comment_original)
        # 以下是使用Gemini api
        comment_cn = translate_by_gemini(apikey, comment_original)
        item = {
            "card_id": online_card_id,
            "content_original": "",
            "content_cn": "",
            "comment_original": f"`[由imap_tools提取]`\n“{comment_original}”",
            # "comment_cn": f"`[由小牛API进行翻译]`\n“{comment_cn}”",
            "comment_cn": f"`[由Gemini {MODEL_NAME} 翻译]`\n“{comment_cn}”",
        }
        print("已保存更新内容:", item)
        insert_or_update_db(db_path, "postcard_story", item)
    return None


def get_mail_reply(host, user, passwd, filename):

    try:
        with MailBox(host).login(user, passwd) as mailbox:
            mailbox.folder.set(filename)
            with ThreadPoolExecutor() as executor:
                futures = {
                    executor.submit(process_message, msg): msg
                    for msg in mailbox.fetch(AND(subject="Hurray! Your postcard"))
                }

    except MailboxLoginError:
        print("登录失败！请检查邮箱账号/邮箱授权密码是否正确")
    except MailboxFolderSelectError:
        print("请检查邮件对应的目录是否正确")
    except Exception as e:
        print(e)
        print("请检查邮箱host是否正确")


def parse_string(input_string):
    arr = []
    groups = input_string.split(",")
    for group in groups:
        host, user, passwd, filename = group.split("//")

        host = host.strip()
        user = user.strip()
        passwd = passwd.strip()
        filename = filename.strip()
        arr.append({"host": host, "user": user, "passwd": passwd, "filename": filename})
    return arr


if __name__ == "__main__":
    start_time = time.time()
    ai_settings = toml.load("scripts/config.toml")
    # 优先从环境变量读取 Gemini API Key
    MODEL_NAME = ai_settings["gemini"]["model"]
    GEMINI_APIKEY = os.environ.get("GEMINI_APIKEY", "") or ai_settings["gemini"].get(
        "api_key", ""
    )
    parms = parse_string(input_string)
    # print(parms)
    for parm in parms:
        get_mail_reply(parm["host"], parm["user"], parm["passwd"], parm["filename"])
    end_time = time.time()
    execution_time = round((end_time - start_time), 3)
    print("————————————————————")
    print(f"scripts/mail_track.py脚本执行时间：{execution_time}秒")
