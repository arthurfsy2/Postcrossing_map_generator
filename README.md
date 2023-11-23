**一个可以输入account、Cookies即可获取Postcrossing gallery数据、生成个性化地图的脚本。**

个人地图展示：
[收发标记图](https://postcrossing.4a1801.life/ClusterMap.html)
[聚类图](https://postcrossing.4a1801.life/Map.html)

个人博客效果展示：
[Postcrossing](https://blog.4a1801.life/Arthur/postcrossing)

# 前言

本项目特点：

1. 可以下载gallery对应的图片，并生成包含fronttage的.md文件，以便你放入到vuepress当中使用
2. 可抓取对应账户的收、发明信片的信息，形成2个地图文件，内容是仿官方的map部分的谷歌地图，但是加入了自定义的内容
3. 抓取后的信息会保存到./output/sent_List.json和received_List.json当中，如果以后有更新，只会抓取更新部分，减少对Postcrossing的压力。

# 一.步骤

1. clone本项目到本地
2. 将scripts/config.jsonBAK这个文件修改为scripts/config.json

```
{
    "account": "",//输入你的个人账户,如链接：“https://www.postcrossing.com/user/arthurfsy/gallery”当中的“arthurfsy”
    "nickName": "",//输入你定义的昵称，用于生成.md文件的fronttage内容，生成后的.md文件可作为vuepress项目使用
    "Cookie": "",//通过浏览器获取的Cookies，具体获取方式见最后的备注，且cookie的有效期可能只有几个小时。如果cookie错误/过期，则只能获取gallery/sent或received的内容
    "picDriverPath":"https://s3.amazonaws.com/static2.postcrossing.com/postcard/medium"//默认为Postcrossing图片的官方链接前缀。也可以在运行`python postcrossing.py`后改为"./gallery/picture"，进行本地读取
}
```

执行 `pip install -r requirements.txt安装依赖`

3. 在当前路径下运行终端，运行以下代码获取gallery数据：

`python postcrossing.py`

注：如果account、Cookie无误的话，即可在./gallery路径下生成4个.md格式的文件，分别对应gallery当中的sent、received、favourites、popular的内容,并自动在./gallery/picture路径下保存对应的图片。

4. 运行以下代码生成地图：
   `python scripts/contryNameEmoji.json`
   注：如果account、Cookie无误的话，即可在./路径下生成2个.html格式的文件，分别是ClusterMap.html和Map.html。

# 二. Github Page在线展示

**如果你想通过Github Page来在线展示地图数据，可进行以下步骤**

1. fork本项目到你自己的仓库，clone到本地后修改fork仓库内的scripts/config.jsonBAK文件名称、内容
2. 参考上述的步骤1-4，在本地生成2个地图html文件
3. 将HTML文件push到你fork的仓库当中
4. 参考以下截图开通Github Page,即可访问(需要手动在链接后面增加ClusterMap.html或Map.html)
   ![](img/20231026155131.png)

# 三.备注

## 获取Cookie的方法：

1. 登陆你的postcrossing账号，并打开你个人的gallery/sent链接。
2. 按下F12打开调试模式，再F5刷新网页，在“网络/network”下找到“sent”名称的项，点击“标头”，在“请求标头”中找到Cookie开头的内容（红框当中显示的内容）。鼠标选中，复制粘贴到scripts/config.json的Cookie对应位置。
   找到__Host-postcrossing=XXX，复制XXX这一串内容粘贴到你的scripts/config.json的"Cookie"当中
3. 如果cookie错误/过期，则只能获取gallery/sent或received的内容

## vercel

你也可以通过vercel来接入fork的项目，这样可以在本地生成，然后每次push到GitHub后，通过vercel生成新的地图html

## changelog:

2023/10/26新功能：在.md的文件中，新增了国家2位英文代码对应的emoji表情（在不同平台看到的效果可能不一样）
注：大部分是通过简写代码标注，少部分国家和地区是通过十六进制HTML字符实体标注。如果发现某个国家的国旗emoji表情无法正常显示（如显示:xxx:，则说明这个国家没有简码/设置不正确）

修改步骤：

1. 通过这个网址查询到对应的国家或地区：https://emojidaquan.com/category2-country-flags
2. 找到对应的国家或地区，如香港：https://emojidaquan.com/emoji-flag-for-hong-kong
3. 查询简写代码、或十六进制HTML字符实体，填写到 `scripts/contryName.json`文件中。（如果是十六进制HTML字符实体，则复制粘贴后需要去除中间的空格。如香港的是"&#x1f1ed\;&#x1f1f0\;"
4. 修改保存后，获取新的Cookie填入scripts/config.json，然后重新执行py postcrossing.py
