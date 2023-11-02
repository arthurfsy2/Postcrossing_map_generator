from datetime import datetime
import json
import time
import multiDownload as dl
import os



start_time = time.time()

with open("config.json", "r") as file:
    data = json.load(file)
account = data["account"]
nickName = data["nickName"]
Cookie = data["Cookie"]
picDriverPath = data["picDriverPath"]
dbpath = data["dbpath"]

# 获取当前日期
current_date = datetime.now().date()

# 将日期格式化为指定格式
date = current_date.strftime("%Y-%m-%d")

types = ['sent', 'received', 'favourites', 'popular']

def createMD(type):
    with open(f"./output/title.json", "r") as file:
        data = json.load(file)
    value = data.get(type)
    from_or_to, pageNum, Num, title = value
    content =dl.readDB(dbpath, type,"Galleryinfo")
    MDcontent_all =""
    for id in content:
        baseUrl = "https://www.postcrossing.com/"
        postcardID = id["id"]  
        picFileName = id["picFileName"]
        if type == "popular":
            num = id["favoritesNum"]
            picurl = f"## [{postcardID}]({baseUrl}postcards/{postcardID})\n>点赞人数：{num}\n\n![]({picDriverPath}/{picFileName}) \n "
        else:
            contryNameEmoji = id["contryNameEmoji"]
            userInfo = id["userInfo"]
            picurl = f"## [{postcardID}]({baseUrl}postcards/{postcardID}) \n >{from_or_to} {userInfo} {contryNameEmoji}\n\n![]({picDriverPath}/{picFileName})\n\n"
        MDcontent_all += picurl
    #print(f"{account}'{type}展示墙数量:{Num}\n{account}'{type}展示墙页数:{pageNum}\n")
    

    filename_md = f"gallery/{type}.md"
    with open(filename_md, "w", encoding="utf-8") as file:
            content = f'---\ntitle: {title}\nicon: address-card\ndate: {date}\ncategory:\n  - {nickName}\ntag:\n  - postcrossing\n---\n\n{MDcontent_all}'
            file.write(content)
            print(f"\n{type}_展示墙数据转换为md格式成功：{filename_md}")


dl.PicDataCheck()
for type in types:
    createMD(type) 
    # removePath = f"./output/{type}.json"
    # if os.path.exists(removePath):  # 更新完后删除List_update.json
    #     os.remove(removePath)  

end_time = time.time()
execution_time = round((end_time - start_time),3)
print(f"postcrossing.py脚本执行时间：{execution_time}秒\n")

# command = "py createMap.py"
# subprocess.run(command, shell=True)

# print("请按下任意键退出")
# input()