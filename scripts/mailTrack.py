from imap_tools import MailBox, AND
import re
import json
from urllib import parse,request
import sqlite3
import os 
#import multiDownload as dl 
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


parser.add_argument("input_string", help="输入host//user//passwd//filename,以英文逗号‘,’隔开")   
parser.add_argument("apikey", help="输入小牛翻译apikey")         
options = parser.parse_args()


input_string = options.input_string
apikey = options.apikey

def remove_blank_lines(text):
    if text:
        return "\n".join(line for line in text.splitlines() if line.strip())
    return text

def getMailReply(host,user,passwd,filename):
    tablename = "postcardStory"
    oldReplyID=getLocalReplyID(dbpath,tablename) #获取本地数据库已保存的ID 
    #print("oldReplyID:\n",oldReplyID)
    content = []
    with MailBox(host).login(user, passwd) as mailbox:        
        # for f in mailbox.folder.list():
        #     print(f) #查看当前账号的文件夹列表
        mailbox.folder.set(filename) 
        for msg in mailbox.fetch(AND(subject="Hurray! Your postcard")):
            #print("msg:\n",msg.date, msg.subject, len(msg.text or msg.html))
            id = re.search(r'Hurray! Your postcard (.*?) to', msg.subject).group(1)
            match = re.search(r'“([\s\S]*?)”', msg.text)
            if match:
                match = match.group(1)
                if id not in oldReplyID: #只翻译新的内容
                    print("idNEW:",id)
                    comment_en = remove_blank_lines(match)
                    comment_cn = translate(comment_en, 'auto', 'zh')
                    data = {
                        "id": id,
                        "content_en": "",
                        "content_cn": "",
                        "comment_en": f"“{comment_en}”",
                        "comment_cn": f"“{comment_cn}”",
                    }
                    content.append(data)       
        if len(content)>0:
            writeDB(dbpath, content,tablename)    
            print("已发现更新内容:",content)
        else:
            print("无更新内容")

def translate(sentence, src_lan, tgt_lan):
    url = 'http://api.niutrans.com/NiuTransServer/translation?'
    data = {"from": src_lan, "to": tgt_lan, "apikey": apikey, "src_text": sentence}
    data_en = parse.urlencode(data)
    req = url + "&" + data_en
    res = request.urlopen(req)
    res_dict = json.loads(res.read())
    if "tgt_text" in res_dict:
        result = res_dict['tgt_text']
    else:
        result = res
    return result

def getLocalReplyID(dbpath,tablename):
    oldID = None
    if os.path.exists(dbpath):
        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?",(tablename,))
        table_exists = cursor.fetchone()
        if table_exists:
            # 从Mapinfo表中获取id
            cursor.execute(f"SELECT id FROM {tablename} WHERE id LIKE 'CN-%'")
            rows = cursor.fetchall()
            oldID = [row[0] for row in rows]
        conn.close()
    return oldID


def writeDB(dbpath, content,tablename):   
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    if tablename == 'postcardStory':
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
                    (id TEXT, content_en TEXT, content_cn TEXT, comment_en TEXT, comment_cn TEXT)''')
        for item in content:
            id = item['id']
            content_en = item['content_en']
            content_cn = item['content_cn']
            comment_en = item['comment_en']
            comment_cn = item['comment_cn']
            cursor.execute(f"SELECT * FROM {tablename} WHERE id=? ", (id, ))
            existing_data = cursor.fetchone()
            if existing_data:
                # 更新已存在的行的其他列数据
                cursor.execute(f"UPDATE {tablename} SET content_en=?, content_cn=?,comment_en=?, comment_cn=?  WHERE id=?",
                                (content_en, content_cn,comment_en, comment_cn, id))
            else:
                # 插入新的行
                cursor.execute(f"INSERT OR REPLACE INTO {tablename} VALUES (?, ?, ?, ?, ?)",
                                (id, content_cn, content_en, comment_en, comment_cn ))
    
    print(f'已更新数据库{dbpath}的{tablename}\n')
    conn.commit()
    conn.close()

def parse_string(input_string):
    arr = []
    groups = input_string.split(',')
    for group in groups:
        host, user,passwd,filename = group.split('//')
        
        host = host.strip()
        user = user.strip()
        passwd = passwd.strip()
        filename = filename.strip()
        arr.append({'host': host, 'user': user, 'passwd': passwd, 'filename': filename})
    return arr

if __name__ == "__main__":
    parms = parse_string(input_string)
    #print(parms)
    for parm in parms:
        getMailReply(parm['host'],parm['user'],parm['passwd'],parm['filename'])
