
#导入模块##  
import mechanize  
import http.cookiejar 
import sys
import re
import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("account", help="输入account")
parser.add_argument("password", help="输入password")      
options = parser.parse_args()

account = options.account
password = options.password


  
br = mechanize.Browser()  
cj = http.cookiejar.LWPCookieJar()  
br.set_cookiejar(cj)##关联cookies  
  
###设置一些参数，因为是模拟客户端请求，所以要支持客户端的一些常用功能，比如gzip,referer等  
br.set_handle_equiv(True)  
br.set_handle_gzip(True)  
br.set_handle_redirect(True)  
br.set_handle_referer(True)  
br.set_handle_robots(False)  
  
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)  
  
###这个是degbug##你可以看到他中间的执行过程，对你调试代码有帮助  
br.set_debug_http(True)  
#br.set_debug_redirects(True)  
#br.set_debug_responses(True)  


  
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')]##模拟浏览器头  

##设定登陆url
response = br.open('https://www.postcrossing.com/login')



print("--------------------")

# 将标准输出重定向到文件


br.select_form(nr=0)##选择表单1，  
  
br.form['signin[username]'] = account  
br.form['signin[password]'] = password  

sys.stdout = open('log.txt', 'w')    
response = br.submit()##提交表单  
# 恢复标准输出
sys.stdout = sys.__stdout__

# 读取文件内容
with open('log.txt', 'r') as file:
    content = file.read()

# 使用正则表达式提取目标字符串中的内容
pattern_host = r'Set-Cookie: __Host-postcrossing=(.*?);'
pattern_remember = r'Set-Cookie: PostcrossingRemember=(.*?);'

match_host = re.search(pattern_host, content)
match_remember = re.search(pattern_remember, content)

# 提取到的内容
if match_host:
    extracted_host = match_host.group(1)
    print("Host-postcrossing:", extracted_host)
else:
    print("No match found for Host-postcrossing.")

if match_remember:
    extracted_remember = match_remember.group(1)
    print("PostcrossingRemember:", extracted_remember)
else:
    print("No match found for PostcrossingRemember.")

Cookie=f"__Host-postcrossing={extracted_host}; PostcrossingRemember={extracted_remember}"

# 读取config.json文件内容
with open('config.json', 'r') as file:
    config_data = json.load(file)

# 更新Cookie变量的值
config_data['Cookie'] = Cookie
config_data['account'] = account
config_data['Cookie'] = Cookie
# 将更新后的内容写入config.json文件
with open('config.json', 'w') as file:
    json.dump(config_data, file, indent=4)
os.remove("log.txt")  