from imap_tools import MailBox, AND
from imap_tools.errors import *
import re
import json
from urllib import parse, request
import sqlite3
import os
from common_tools import translate
import argparse

with open("scripts/config.json", "r") as file:
    data = json.load(file)
# account = data["account"]
# nickName = data["nickName"]
Cookie = data["Cookie"]
picDriverPath = data["picDriverPath"]
dbpath = data["dbpath"]
# repo = data["repo"]

parser = argparse.ArgumentParser()


parser.add_argument(
    "input_string", help="输入host//user//passwd//filename,以英文逗号‘,’隔开")
parser.add_argument("apikey", help="输入小牛翻译apikey")
options = parser.parse_args()


input_string = options.input_string
apikey = options.apikey


def remove_blank_lines(text):
    if text:
        return "\n".join(line for line in text.splitlines() if line.strip())
    return text


def getMailReply(host, user, passwd, filename):
    tablename = "postcardStory"
    oldReplyID = getLocalReplyID(dbpath, tablename)  # 获取本地数据库已保存的ID
    content = []
    
    try:
        with MailBox(host).login(user, passwd) as mailbox:
            mailbox.folder.set(filename)
            for msg in mailbox.fetch(AND(subject="Hurray! Your postcard")):
                id = re.search(r'Hurray! Your postcard (.*?) to', msg.subject).group(1)
                match = re.search(r'“([\s\S]*?)”', msg.text)
                if match:
                    match = match.group(1)
                    if id not in oldReplyID:  # 只翻译新的内容
                        print("idNEW:", id)
                        comment_original = remove_blank_lines(match)
                        comment_cn = translate(apikey, comment_original, 'auto', 'zh')
                        data = {
                            "id": id,
                            "content_original": "",
                            "content_cn": "",
                            "comment_original": f"“{comment_original}”",
                            "comment_cn": f"“{comment_cn}”",
                        }
                        content.append(data)
            if len(content) > 0:
                writeDB(dbpath, content, tablename)
                print("已发现更新内容:", content)
            else:
                print("无更新内容")
    except MailboxLoginError:
        print("登录失败！请检查邮箱账号/邮箱授权密码是否正确")
    except MailboxFolderSelectError:
        print("请检查邮件对应的目录是否正确")
    except Exception as e:
        print("请检查邮箱host是否正确")



def getLocalReplyID(dbpath, tablename):
    oldID = None
    if os.path.exists(dbpath):
        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tablename,))
        table_exists = cursor.fetchone()
        if table_exists:
            # 从Mapinfo表中获取id
            cursor.execute(f"SELECT id FROM {tablename} WHERE id LIKE 'CN-%'")
            rows = cursor.fetchall()
            oldID = [row[0] for row in rows]
        conn.close()
    return oldID


def writeDB(dbpath, content, tablename):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    if tablename == 'postcardStory':
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
                    (id TEXT, content_original TEXT, content_cn TEXT, comment_original TEXT, comment_cn TEXT)''')
        for item in content:
            id = item['id']
            content_original = item['content_original']
            content_cn = item['content_cn']
            comment_original = item['comment_original']
            comment_cn = item['comment_cn']
            cursor.execute(f"SELECT * FROM {tablename} WHERE id=? ", (id, ))
            existing_data = cursor.fetchone()
            if existing_data:
                # 更新已存在的行的其他列数据
                cursor.execute(f"UPDATE {tablename} SET content_original=?, content_cn=?,comment_original=?, comment_cn=?  WHERE id=?",
                               (content_original, content_cn, comment_original, comment_cn, id))
            else:
                # 插入新的行
                cursor.execute(f"INSERT OR REPLACE INTO {tablename} VALUES (?, ?, ?, ?, ?)",
                               (id, content_cn, content_original, comment_original, comment_cn))

    print(f'已更新数据库{dbpath}的{tablename}\n')
    conn.commit()
    conn.close()


def parse_string(input_string):
    arr = []
    groups = input_string.split(',')
    for group in groups:
        host, user, passwd, filename = group.split('//')

        host = host.strip()
        user = user.strip()
        passwd = passwd.strip()
        filename = filename.strip()
        arr.append({'host': host, 'user': user,
                   'passwd': passwd, 'filename': filename})
    return arr


if __name__ == "__main__":
    parms = parse_string(input_string)
    # print(parms)
    for parm in parms:
        getMailReply(parm['host'], parm['user'],
                     parm['passwd'], parm['filename'])
