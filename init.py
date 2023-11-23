import json

# 读取config.json文件内容
with open('config.json', 'r') as file:
    config_data = json.load(file)

# 更新Cookie变量的值
config_data['account'] = "your account"
config_data['nickName'] = "your Markdown Name"
config_data['Cookie'] = "auto create"
# 将更新后的内容写入config.json文件
with open('config.json', 'w') as file:
    json.dump(config_data, file, indent=4)