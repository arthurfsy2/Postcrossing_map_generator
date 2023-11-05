import requests
import re
import time
from urllib.parse import quote
import json
loginurl="https://www.postcrossing.com/login"

headers1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Cookie': '__stripe_mid=23b83944-a8f0-42e9-9828-490431f1a0edeeac28; __Host-postcrossing=oeh6occscf4jmugad06qb8s3n1',
    'Pragma': 'no-cache',
    'Referer': 'https://www.postcrossing.com/',
    'Sec-Ch-Ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
}

headers2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Content-Length': '158',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '__stripe_mid=23b83944-a8f0-42e9-9828-490431f1a0edeeac28; __Host-postcrossing=et4jqbdp6qndta7hg7l78bmqef',
    'Origin': 'https://www.postcrossing.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.postcrossing.com/login?',
    'Sec-Ch-Ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
}



account="254904240@qq.com"
password="Fsy364115."




response = requests.get(loginurl,headers=headers1)
content = response.text
token = re.search(r'value="([^"]+)"', response.text).group(1)
print("csrf_token:\n",token)


payload=f"signin%5B_login_csrf_token%5D={token}&signin%5Busername%5D={quote(account)}&signin%5Bpassword%5D={password}&signin%5Bremember%5D=on"

time.sleep(2)

response2=requests.post(loginurl,headers=headers2,data=payload)
cookies = response2.cookies.get("__Host-postcrossing")
print("cookies:",cookies)

# 读取 config.json 文件
with open('config.json', 'r') as f:
    config = json.load(f)

# 替换 Cookie 的值
config['Cookie'] = cookies


# 写入更新后的数据到 config.json 文件
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)