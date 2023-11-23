import json

filenames = ['config','galleryUpdateStats','mapUpdateStats']
def initialize(filename):
    path=f"scripts/{filename}.json"
    # 读取scripts/config.json文件内容
    with open(path, 'r') as file:
        data = json.load(file)
    if filename =="config":
    # 更新Cookie变量的值
        data['account'] = "your account"
        data['nickName'] = "your Markdown Name"
        data['Cookie'] = "auto create"
    # 将更新后的内容写入scripts/config.json文件
    elif filename =="galleryUpdateStats":
        data['sent'] = ""
        data['received'] = ""
        data['favourites'] = ""
        data['popular'] = ""
    elif filename =="mapUpdateStats":
        data['sent'] = ""
        data['received'] = ""

    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

for name in filenames:
    initialize(name)