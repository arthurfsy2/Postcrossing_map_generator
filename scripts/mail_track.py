from imap_tools import MailBox, AND
from imap_tools.errors import *
import re
import json
from urllib import parse, request
import sqlite3
import os
from common_tools import translate, db_path, insert_or_update_db, read_db_table
import argparse
import time
from concurrent.futures import ThreadPoolExecutor

with open("scripts/config.json", "r") as file:
    data = json.load(file)
# account = data["account"]
# nick_name = data["nick_name"]
Cookie = data["Cookie"]
pic_driver_path = data["pic_driver_path"]

# repo = data["repo"]

parser = argparse.ArgumentParser()


parser.add_argument(
    "input_string", help="输入host//user//passwd//filename,以英文逗号‘,’隔开"
)
parser.add_argument("apikey", help="输入小牛翻译apikey")
options = parser.parse_args()


input_string = options.input_string
apikey = options.apikey


def remove_blank_lines(text):
    if text:
        return "\n".join(line for line in text.splitlines() if line.strip())
    return text


def process_message(msg):

    online_card_id = re.search(r"Hurray! Your postcard (.*?) to", msg.subject).group(1)

    story_data = read_db_table(db_path, "postcard_story", {"card_id": online_card_id})

    if not story_data:  # 只翻译新的内容
        match = re.search(r"“([\s\S]*?)”", msg.text)
        match = match.group(1)
        print("new card id:", online_card_id)
        comment_original = remove_blank_lines(match)
        comment_cn = translate(apikey, comment_original, "auto", "zh")
        item = {
            "card_id": online_card_id,
            "content_original": "",
            "content_cn": "",
            "comment_original": f"“{comment_original}”",
            "comment_cn": f"“{comment_cn}”",
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
    parms = parse_string(input_string)
    # print(parms)
    for parm in parms:
        get_mail_reply(parm["host"], parm["user"], parm["passwd"], parm["filename"])
    end_time = time.time()
    execution_time = round((end_time - start_time), 3)
    print("————————————————————")
    print(f"scripts/mailTrack.py脚本执行时间：{execution_time}秒")
