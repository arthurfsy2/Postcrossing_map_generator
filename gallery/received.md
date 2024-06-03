---
title: 明信片展示墙（收到：104）
icon: address-card
date: 2024-06-03
category:
  - Arthur
tag:
  - postcrossing
order: 3
---

## [arthurfsy's received](https://www.postcrossing.com/user/arthurfsy/gallery/received)

### 收发记录（年度）
::: echarts 

```js
const data = await fetch(
  "https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/output/year.json"
).then((res) => res.json());

const newData = data.map(({ year, received }) => ({ name: year, value: received }));

const option = {
  title: {
    text: "",
    subtext: "",
    left: "center"
  },
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b} : {c} ({d}%)'
  },
  series: [
    {
      name: "",
      clockwise: false,
      type: "pie",
      radius: "50%",
      data: newData,
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: "rgba(0, 0, 0, 0.5)"
        }
      },
      label: {
        alignTo: 'none',
        formatter: '{name|{b}}\n{value|{d}%}',
        minMargin: 1,
        fontStyle:'italic',
        fontWeight: 'bold',

        rich: {
          num: {
            fontSize: 10,
            color: '#999'
          }
        }
      },
      labelLine: {
        length: 50,

      }

    }
  ]
}
```
:::

### 收发记录（月度）

:::echarts

```js
const data = await fetch(
  "https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/output/month.json"
).then((res) => res.json());


var date = data.map(function (item) {
    return item.date
})

var sent = data.map(function (item) {
    return item.sent
})

var sentSum = sent.reduce(function(acc, curr) {
  return acc + curr;
}, 0);

var received = data.map(function (item) {
    return item.received
})

var receivedSum = received.reduce(function(acc, curr) {
  return acc + curr;
}, 0);

sentName = sentSum + "张已寄出"
receivedName = receivedSum + "张已收到"

const option = {
  title: {
    text: '',
     left: 'center',
  },
    legend: {
    data: [sentName, receivedName]
  },
  tooltip: {
    trigger: 'axis'
  },
  xAxis: {
    type: 'category',
    data: date
  },
  yAxis: {
    type: 'value'
  },
  dataZoom: [
  {
    start: 0
  },
  {
    type: "inside"
  }
],
  series: [
    {
      name:sentName,
      data: sent,
      type: 'line',
      smooth: true
    },
    {
      name:receivedName,
      data: received,
      type: 'line',
      smooth: true
    }
  ]
}
```

:::

### 2024(35)

[US-10392528](https://www.postcrossing.com/postcards/US-10392528) 
 >来自 [DemianLV](https://www.postcrossing.com/user/DemianLV) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=36.0397~-114.98194&lvl=12.0&setlang=zh-Hans) 2024/05/10 22:49 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/03 23:27 (当地)
 📏 11,696 | ⏱ 23


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/jftiw2d8ar5tfj2azgsxumfck1s9f4yg.jpg)

[NL-5735018](https://www.postcrossing.com/postcards/NL-5735018) 
 >来自 [willempie_](https://www.postcrossing.com/user/willempie_) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=52.46167~5.99861&lvl=12.0&setlang=zh-Hans) 2024/05/09 10:50 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/01 23:02 (当地)
 📏 9,188 | ⏱ 23


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/txy0slkdu6tm7vsuoomc071uy5fbzqnb.jpg)

[GB-1757199](https://www.postcrossing.com/postcards/GB-1757199) 
 >来自 [LauraLou](https://www.postcrossing.com/user/LauraLou) 🇬🇧
> 📤 [United Kingdom](https://www.bing.com/maps/?cp=53.64904~-1.78416&lvl=12.0&setlang=zh-Hans) 2024/05/07 09:18 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/01 23:00 (当地)
 📏 9,568 | ⏱ 25


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/i3afjwafueaqs8n3n7x3hcinm1x910er.jpg)

[HR-108981](https://www.postcrossing.com/postcards/HR-108981) 
 >来自 [jilli1002](https://www.postcrossing.com/user/jilli1002) 🇭🇷
> 📤 [Croatia](https://www.bing.com/maps/?cp=44.11578~15.22514&lvl=12.0&setlang=zh-Hans) 2024/05/07 10:17 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/05/27 22:39 (当地)
 📏 8,962 | ⏱ 20


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/3muyxpwujwl5gulj3uua81zu92gp1gki.jpg)

[AT-729734](https://www.postcrossing.com/postcards/AT-729734) 
 >来自 [Zwiebel123](https://www.postcrossing.com/user/Zwiebel123) 🇦🇹
> 📤 [Austria](https://www.bing.com/maps/?cp=47.26266~11.39454&lvl=12.0&setlang=zh-Hans) 2024/05/07 10:18 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/05/24 23:12 (当地)
 📏 9,096 | ⏱ 17


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/qtgrtx9dizw0ykp1fo2tscsbq6q8dwu8.jpg)

[JP-2075151](https://www.postcrossing.com/postcards/JP-2075151) 
 >来自 [dream3225](https://www.postcrossing.com/user/dream3225) 🇯🇵
> 📤 [Japan](https://www.bing.com/maps/?cp=35.08333~137.15&lvl=12.0&setlang=zh-Hans) 2024/05/07 17:16 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/05/21 20:41 (当地)
 📏 2,620 | ⏱ 14


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/xdyyhnwy7o5hdlqsyhwy34v4miryawnt.jpg)

[RU-9991674](https://www.postcrossing.com/postcards/RU-9991674) 
 >来自 [Ledon2015](https://www.postcrossing.com/user/Ledon2015) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2024/02/09 22:21 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/23 19:35 (当地)
 📏 7,123 | ⏱ 74


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/78k8s94ftzz9wttc6fq78790o5g6uk3y.jpg)

[RU-9991671](https://www.postcrossing.com/postcards/RU-9991671) 
 >来自 [jul_nov](https://www.postcrossing.com/user/jul_nov) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2024/02/09 22:18 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/18 18:54 (当地)
 📏 7,123 | ⏱ 69


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/8kmo9qjxz6kvunt5vit5kbnvmnoaf7ue.jpg)

[US-10240079](https://www.postcrossing.com/postcards/US-10240079) 
 >来自 [waydowneast](https://www.postcrossing.com/user/waydowneast) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=44.02163~-92.4699&lvl=12.0&setlang=zh-Hans) 2024/03/16 15:16 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/06 12:27 (当地)
 📏 12,127 | ⏱ 20


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/c6j8qns0fwqmo1bi5zinj0rjk87oyxsa.jpg)

[DE-14019750](https://www.postcrossing.com/postcards/DE-14019750) 
 >来自 [Havanna](https://www.postcrossing.com/user/Havanna) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.47593~10.98856&lvl=12.0&setlang=zh-Hans) 2024/03/16 07:37 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/06 12:12 (当地)
 📏 9,021 | ⏱ 21


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/sm03ogvybqys253tqskqm7aov92o34t8.jpg)

[MY-634790](https://www.postcrossing.com/postcards/MY-634790) 
 >来自 [SerHuy](https://www.postcrossing.com/user/SerHuy) 🇲🇾
> 📤 [Malaysia](https://www.bing.com/maps/?cp=3.21~101.561&lvl=12.0&setlang=zh-Hans) 2024/03/16 14:38 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/06 12:01 (当地)
 📏 2,548 | ⏱ 21


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/cb7ft4eyjurh3ncp22d5ktsw3oox5el6.jpg)

[US-10173050](https://www.postcrossing.com/postcards/US-10173050) 
 >来自 [blairwortham20](https://www.postcrossing.com/user/blairwortham20) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=42.91259~-71.1245&lvl=12.0&setlang=zh-Hans) 2024/02/21 22:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/22 19:04 (当地)
 📏 12,714 | ⏱ 29


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/m4x243q6e3xzwsprdsl8vs3scp8ai50t.jpg)

[TW-3636606](https://www.postcrossing.com/postcards/TW-3636606) 
 >来自 [SophieAD](https://www.postcrossing.com/user/SophieAD) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=25.04776~121.53185&lvl=12.0&setlang=zh-Hans) 2024/02/22 12:04 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/18 20:26 (当地)
 📏 792 | ⏱ 25


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/z0fgmt19upgwg6p7vg576mbuvfeg8xf5.jpg)

[DE-13722055](https://www.postcrossing.com/postcards/DE-13722055) 
 >来自 [Lara1992](https://www.postcrossing.com/user/Lara1992) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=48.78232~9.17702&lvl=12.0&setlang=zh-Hans) 2023/12/19 13:30 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/18 10:50 (当地)
 📏 9,173 | ⏱ 90


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/g9vtk8lteshvn5sgzzqb8n5hccaalw7v.jpg)

[DE-13953758](https://www.postcrossing.com/postcards/DE-13953758) 
 >来自 [kjk87](https://www.postcrossing.com/user/kjk87) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.80557~8.60307&lvl=12.0&setlang=zh-Hans) 2024/02/25 13:25 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/18 10:40 (当地)
 📏 9,161 | ⏱ 22


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/8cbmr2589ihn93jhz7t99vlds9xjp5fz.jpg)

[US-10173049](https://www.postcrossing.com/postcards/US-10173049) 
 >来自 [Morningofthesun](https://www.postcrossing.com/user/Morningofthesun) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=26.96201~-82.3526&lvl=12.0&setlang=zh-Hans) 2024/02/21 22:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/18 10:37 (当地)
 📏 14,226 | ⏱ 25


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/70d4m0tgu32c1f1c7gku2siy1tckduqt.jpg)

[CA-1436021](https://www.postcrossing.com/postcards/CA-1436021) 
 >来自 [kittenwsharpclaws](https://www.postcrossing.com/user/kittenwsharpclaws) 🇨🇦
> 📤 [Canada](https://www.bing.com/maps/?cp=43.70011~-79.4163&lvl=12.0&setlang=zh-Hans) 2024/02/09 14:21 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/18 10:30 (当地)
 📏 12,516 | ⏱ 37


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/3fv8lw8qch3npecpsa4h7w65da93kv2n.jpg)

[FI-4563418](https://www.postcrossing.com/postcards/FI-4563418) 
 >来自 [Emmietta](https://www.postcrossing.com/user/Emmietta) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=61.49911~23.78712&lvl=12.0&setlang=zh-Hans) 2024/02/09 21:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/18 10:20 (当地)
 📏 7,839 | ⏱ 37


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/o6mpesh50v8xttziy01yeirahmhv1krj.jpg)

[FI-4563419](https://www.postcrossing.com/postcards/FI-4563419) 
 >来自 [mieite](https://www.postcrossing.com/user/mieite) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=60.98267~25.66151&lvl=12.0&setlang=zh-Hans) 2024/02/09 21:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/10 13:56 (当地)
 📏 7,752 | ⏱ 29


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/07hkdu7lxdtil6jtc54jsyn5q0e1yl80.jpg)

[DE-13904674](https://www.postcrossing.com/postcards/DE-13904674) 
 >来自 [Thumla](https://www.postcrossing.com/user/Thumla) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.67502~7.94983&lvl=12.0&setlang=zh-Hans) 2024/02/10 17:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/10 13:53 (当地)
 📏 9,060 | ⏱ 29


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/7cp1tsfnfvwk7ry1x3kkoubtno86y8b0.jpg)

[US-10143953](https://www.postcrossing.com/postcards/US-10143953) 
 >来自 [mbgris](https://www.postcrossing.com/user/mbgris) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=42.45843~-71.06616&lvl=12.0&setlang=zh-Hans) 2024/02/11 16:59 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/04 23:13 (当地)
 📏 12,764 | ⏱ 22


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/w82ajeefdvnxtn4huxus9igicuccxkwd.jpg)

[DE-13942438](https://www.postcrossing.com/postcards/DE-13942438) 
 >来自 [Stiflers-Mom](https://www.postcrossing.com/user/Stiflers-Mom) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.06556~8.80306&lvl=12.0&setlang=zh-Hans) 2024/02/22 08:11 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/04 22:54 (当地)
 📏 9,184 | ⏱ 11


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/ngxabnqi7ztlwpdqhywyq65oonsad12s.jpg)

[US-10137660](https://www.postcrossing.com/postcards/US-10137660) 
 >来自 [trish13](https://www.postcrossing.com/user/trish13) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=38.58157~-121.4944&lvl=12.0&setlang=zh-Hans) 2024/02/09 11:22 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/04 22:52 (当地)
 📏 11,078 | ⏱ 24


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/kmkr5nwo95vce912l7qls8wspoz4rj3k.jpg)

[NL-5673465](https://www.postcrossing.com/postcards/NL-5673465) 
 >来自 [Femkuhhhh](https://www.postcrossing.com/user/Femkuhhhh) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=53.20139~5.80859&lvl=12.0&setlang=zh-Hans) 2024/02/09 20:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/04 22:51 (当地)
 📏 9,161 | ⏱ 24


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/i59brbowdhb1zgjzlhuqcvl1bpsu9ugr.jpg)

[GB-1729911](https://www.postcrossing.com/postcards/GB-1729911) 
 >来自 [PattyG](https://www.postcrossing.com/user/PattyG) 🇬🇧
> 📤 [United Kingdom](https://www.bing.com/maps/?cp=53.48771~-2.29042&lvl=12.0&setlang=zh-Hans) 2024/02/09 19:18 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/02/29 13:45 (当地)
 📏 9,606 | ⏱ 19


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/utmcwgbonrd64cpzezf72j8sahy7egqh.jpg)

[NL-5673466](https://www.postcrossing.com/postcards/NL-5673466) 
 >来自 [Anski1979](https://www.postcrossing.com/user/Anski1979) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=52.1275~4.44861&lvl=12.0&setlang=zh-Hans) 2024/02/09 20:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/02/27 19:55 (当地)
 📏 9,299 | ⏱ 18


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/ix9sfvo9d2yc0erfxg7wtd0d4u8iionc.jpg)

[DE-13743074](https://www.postcrossing.com/postcards/DE-13743074) 
 >来自 [siobhan](https://www.postcrossing.com/user/siobhan) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.0303~6.98432&lvl=12.0&setlang=zh-Hans) 2023/12/25 20:56 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/31 20:16 (当地)
 📏 9,202 | ⏱ 37


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/v3wxlv2ez5u3hwa67ba06osu5x6kq3ym.jpg)

[US-9960301](https://www.postcrossing.com/postcards/US-9960301) 
 >来自 [Nicole1313](https://www.postcrossing.com/user/Nicole1313) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=35.43532~-101.17294&lvl=12.0&setlang=zh-Hans) 2023/12/05 10:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/26 23:12 (当地)
 📏 12,565 | ⏱ 52


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/8v3ov8tmzqztv8mcrrrxy0x0sxlwlwq3.jpg)

[IN-569670](https://www.postcrossing.com/postcards/IN-569670) 
 >来自 [ashokarox](https://www.postcrossing.com/user/ashokarox) 🇮🇳
> 📤 [India](https://www.bing.com/maps/?cp=14.22262~76.40038&lvl=12.0&setlang=zh-Hans) 2024/01/01 19:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/26 23:08 (当地)
 📏 4,086 | ⏱ 25


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/io1w6erf6ty0da60efye6k0xppjo22rt.jpg)

[DE-13755664](https://www.postcrossing.com/postcards/DE-13755664) 
 >来自 [Akasha78](https://www.postcrossing.com/user/Akasha78) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=48.80537~9.52721&lvl=12.0&setlang=zh-Hans) 2023/12/29 09:58 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/26 23:07 (当地)
 📏 9,149 | ⏱ 28


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/uu8q81luyj40ilslp5kli03m890t618b.jpg)

[PL-1969946](https://www.postcrossing.com/postcards/PL-1969946) 
 >来自 [RobertoK](https://www.postcrossing.com/user/RobertoK) 🇵🇱
> 📤 [Poland](https://www.bing.com/maps/?cp=49.98738~20.06473&lvl=12.0&setlang=zh-Hans) 2023/12/05 17:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/14 16:12 (当地)
 📏 8,393 | ⏱ 40


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/wd450wovwocll0euien8tfkm2y713he1.jpg)

[RU-9911412](https://www.postcrossing.com/postcards/RU-9911412) 
 >来自 [MariBrown](https://www.postcrossing.com/user/MariBrown) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=56.8519~60.6122&lvl=12.0&setlang=zh-Hans) 2023/12/05 21:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/04 18:46 (当地)
 📏 5,741 | ⏱ 30


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/oy3wlx1zzhd0dzl0ahcfteg4zxhem003.jpg)

[DE-13722056](https://www.postcrossing.com/postcards/DE-13722056) 
 >来自 [Nordbaer](https://www.postcrossing.com/user/Nordbaer) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.22172~6.77616&lvl=12.0&setlang=zh-Hans) 2023/12/19 13:30 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/02 13:08 (当地)
 📏 9,205 | ⏱ 14


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/exft376nr2jfvn5k98lgex28ym6di6yq.jpg)

[GB-1710416](https://www.postcrossing.com/postcards/GB-1710416) 
 >来自 [gordonf](https://www.postcrossing.com/user/gordonf) 🇬🇧
> 📤 [United Kingdom](https://www.bing.com/maps/?cp=54.42302~-6.44434&lvl=12.0&setlang=zh-Hans) 2023/12/05 16:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/02 13:07 (当地)
 📏 9,766 | ⏱ 28


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/odxhm6bwc8gpouuj6t5nt3hrsdy3npwm.jpg)

[NL-5633161](https://www.postcrossing.com/postcards/NL-5633161) 
 >来自 [read-addict](https://www.postcrossing.com/user/read-addict) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=52.26167~4.49306&lvl=12.0&setlang=zh-Hans) 2023/12/12 10:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/02 13:05 (当地)
 📏 9,289 | ⏱ 21


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/py0eb56dlh1fs9yj4dsi6h5gty9upog4.jpg)

### 2023(22)

[FI-4527706](https://www.postcrossing.com/postcards/FI-4527706) 
 >来自 [Salladeemus](https://www.postcrossing.com/user/Salladeemus) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=64.22728~27.72846&lvl=12.0&setlang=zh-Hans) 2023/12/05 18:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/31 18:17 (当地)
 📏 7,593 | ⏱ 26


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/3e4hr6a3so631dpg9nb8n568vz0vgdul.jpg)

[CA-1412998](https://www.postcrossing.com/postcards/CA-1412998) 
 >来自 [yuliavolosevych](https://www.postcrossing.com/user/yuliavolosevych) 🇨🇦
> 📤 [Canada](https://www.bing.com/maps/?cp=45.50884~-73.58781&lvl=12.0&setlang=zh-Hans) 2023/12/05 11:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/29 21:09 (当地)
 📏 12,404 | ⏱ 24


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/87xk4heemaugky0k4ekus8hs5m6g8k5r.jpg)

[RU-9911406](https://www.postcrossing.com/postcards/RU-9911406) 
 >来自 [Reymas](https://www.postcrossing.com/user/Reymas) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2023/12/05 19:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/29 21:06 (当地)
 📏 7,123 | ⏱ 24


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/eqylfu3vj74g38w0a6258ya0spo2ohh9.jpg)

[BY-3083966](https://www.postcrossing.com/postcards/BY-3083966) 
 >来自 [gallinka](https://www.postcrossing.com/user/gallinka) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=52.4345~30.9754&lvl=12.0&setlang=zh-Hans) 2023/12/05 19:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/29 21:05 (当地)
 📏 7,591 | ⏱ 24


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/ue5f37htbbdaeriqqkse6fvn8imnfyt1.jpg)

[RU-9847210](https://www.postcrossing.com/postcards/RU-9847210) 
 >来自 [Di_Purple](https://www.postcrossing.com/user/Di_Purple) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=44.89497~37.31623&lvl=12.0&setlang=zh-Hans) 2023/10/17 09:56 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/29 21:00 (当地)
 📏 7,254 | ⏱ 73


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/ecsxuv0c10jn33u29cdrn7dk90cwtmh4.jpg)

[NL-5628599](https://www.postcrossing.com/postcards/NL-5628599) 
 >来自 [hippoos](https://www.postcrossing.com/user/hippoos) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=51.87167~4.07083&lvl=12.0&setlang=zh-Hans) 2023/12/06 08:17 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/26 19:18 (当地)
 📏 9,335 | ⏱ 20


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/h8mhntqyo4432gvgbyz5ia883s1sr9sz.jpg)

[HK-846298](https://www.postcrossing.com/postcards/HK-846298) 
 >来自 [jojo2023](https://www.postcrossing.com/user/jojo2023) 🇭🇰
> 📤 [Hong Kong](https://www.bing.com/maps/?cp=22.39175~113.97157&lvl=12.0&setlang=zh-Hans) 2023/12/06 00:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/21 14:15 (当地)
 📏 32 | ⏱ 16


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/fjddvjjax3f1mgnr4slc328duxqr96wl.jpg)

[LT-913966](https://www.postcrossing.com/postcards/LT-913966) 
 >来自 [valras](https://www.postcrossing.com/user/valras) 🇱🇹
> 📤 [Lithuania](https://www.bing.com/maps/?cp=54.64364~25.05162&lvl=12.0&setlang=zh-Hans) 2023/10/17 09:57 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/11/30 13:00 (当地)
 📏 7,928 | ⏱ 44


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/dfsgfv5r49yok2quiwxlxh25edsrjl37.jpg)

[RU-9830214](https://www.postcrossing.com/postcards/RU-9830214) 
 >来自 [EvaS18](https://www.postcrossing.com/user/EvaS18) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.38752~36.73307&lvl=12.0&setlang=zh-Hans) 2023/10/01 21:36 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/11/19 18:39 (当地)
 📏 7,180 | ⏱ 49


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/0mntqe2lc0sfygrisja5uria62de2y7a.jpg)

[NL-5593570](https://www.postcrossing.com/postcards/NL-5593570) 
 >来自 [essie1109](https://www.postcrossing.com/user/essie1109) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=51.84917~5.43333&lvl=12.0&setlang=zh-Hans) 2023/10/17 08:56 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/11/19 18:37 (当地)
 📏 9,255 | ⏱ 33


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/1fgbz23qvpbsc89bxala10k47jc6a05u.jpg)

[UA-1928471](https://www.postcrossing.com/postcards/UA-1928471) 
 >来自 [Iwanka](https://www.postcrossing.com/user/Iwanka) 🇺🇦
> 📤 [Ukraine](https://www.bing.com/maps/?cp=50.45466~30.5238&lvl=12.0&setlang=zh-Hans) 2023/09/28 16:59 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/28 18:27 (当地)
 📏 7,659 | ⏱ 30


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/4i8m3wd4pcpmirk80czwz1elh8rfouoi.jpg)

[DE-13430232](https://www.postcrossing.com/postcards/DE-13430232) 
 >来自 [vic_and_co](https://www.postcrossing.com/user/vic_and_co) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=48.76508~11.42372&lvl=12.0&setlang=zh-Hans) 2023/09/28 15:57 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/28 18:27 (当地)
 📏 9,025 | ⏱ 30


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/r83g6pj7f3c3qv6s0cjsswrgru1u9w7x.jpg)

[CA-1386650](https://www.postcrossing.com/postcards/CA-1386650) 
 >来自 [canadaposter](https://www.postcrossing.com/user/canadaposter) 🇨🇦
> 📤 [Canada](https://www.bing.com/maps/?cp=49.10635~-122.82509&lvl=12.0&setlang=zh-Hans) 2023/09/28 06:59 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/28 18:26 (当地)
 📏 10,254 | ⏱ 30


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/l9a18bl5utrfblm89rdy57pnhioeiegp.jpg)

[FR-1651137](https://www.postcrossing.com/postcards/FR-1651137) 
 >来自 [yabiz](https://www.postcrossing.com/user/yabiz) 🇫🇷
> 📤 [France](https://www.bing.com/maps/?cp=47.71675~-1.37643&lvl=12.0&setlang=zh-Hans) 2023/09/28 16:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/26 13:57 (当地)
 📏 9,910 | ⏱ 28


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/iyf9a5cc4yv2dr4acdjyyv4p42olxa37.jpg)

[US-9761474](https://www.postcrossing.com/postcards/US-9761474) 
 >来自 [KarlaKM](https://www.postcrossing.com/user/KarlaKM) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=34.0584~-106.89142&lvl=12.0&setlang=zh-Hans) 2023/09/28 08:01 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/26 13:56 (当地)
 📏 12,363 | ⏱ 28


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/t9l7z7dtp197o01wzb9r640n7nohvwn3.jpg)

[US-9761471](https://www.postcrossing.com/postcards/US-9761471) 
 >来自 [ilysejohnson](https://www.postcrossing.com/user/ilysejohnson) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=37.55376~-77.46026&lvl=12.0&setlang=zh-Hans) 2023/09/28 10:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/26 13:53 (当地)
 📏 13,219 | ⏱ 28


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/fe4nng7tl273fn4tq36wtar0ykk1n89r.jpg)

[AT-696805](https://www.postcrossing.com/postcards/AT-696805) 
 >来自 [Bruno1405](https://www.postcrossing.com/user/Bruno1405) 🇦🇹
> 📤 [Austria](https://www.bing.com/maps/?cp=48.20849~16.37208&lvl=12.0&setlang=zh-Hans) 2023/10/01 08:23 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/24 14:00 (当地)
 📏 8,712 | ⏱ 23


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/kx9gctk1k68qndt7q2dwyieasadwmjen.jpg)

[US-9781326](https://www.postcrossing.com/postcards/US-9781326) 
 >来自 [mangoqueen24](https://www.postcrossing.com/user/mangoqueen24) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=42.93173~-76.56605&lvl=12.0&setlang=zh-Hans) 2023/10/01 16:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/24 13:58 (当地)
 📏 12,649 | ⏱ 22


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/4a7h4utxbydc5j8mlfkcqlvb7hci4qyp.jpg)

[AT-696806](https://www.postcrossing.com/postcards/AT-696806) 
 >来自 [MysticVampire](https://www.postcrossing.com/user/MysticVampire) 🇦🇹
> 📤 [Austria](https://www.bing.com/maps/?cp=48.30639~14.28611&lvl=12.0&setlang=zh-Hans) 2023/10/01 08:23 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/24 13:55 (当地)
 📏 8,852 | ⏱ 23


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/7tonrpjcvm0ftsh5v1edteyk3u5nai22.jpg)

[FI-4485079](https://www.postcrossing.com/postcards/FI-4485079) 
 >来自 [pikkumyy15](https://www.postcrossing.com/user/pikkumyy15) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=63.83847~23.13066&lvl=12.0&setlang=zh-Hans) 2023/09/28 16:58 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/24 13:53 (当地)
 📏 7,821 | ⏱ 26


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/ra3h05wn9h19d36d51m8q4inz9la4wqi.jpg)

[CZ-2061495](https://www.postcrossing.com/postcards/CZ-2061495) 
 >来自 [Jitka-cz](https://www.postcrossing.com/user/Jitka-cz) 🇨🇿
> 📤 [Czechia](https://www.bing.com/maps/?cp=49.83465~18.28204&lvl=12.0&setlang=zh-Hans) 2023/09/28 16:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/24 13:52 (当地)
 📏 8,519 | ⏱ 26


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/z6gmmq6k6pbyc1ki9yxl0nn4y4hcbdso.jpg)

[DE-13430236](https://www.postcrossing.com/postcards/DE-13430236) 
 >来自 [annegret](https://www.postcrossing.com/user/annegret) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.45657~7.01228&lvl=12.0&setlang=zh-Hans) 2023/09/28 16:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/11 13:57 (当地)
 📏 9,178 | ⏱ 13


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/pac25ahehnw47mqqtyrml2khs4q02pyg.jpg)

### 2015(8)

[RU-3481494](https://www.postcrossing.com/postcards/RU-3481494) 
 >来自 ***该用户已关闭*** 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=58.07894~54.6557&lvl=12.0&setlang=zh-Hans) 2015/02/21 02:09 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/04/30 09:01 (当地)
 📏 5,014 | ⏱ 68


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/eb76fb68310040c1b77038ea719cdd14.jpg)

[RU-3317948](https://www.postcrossing.com/postcards/RU-3317948) 
 >来自 [Gromakina](https://www.postcrossing.com/user/Gromakina) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=56.49771~84.97437&lvl=12.0&setlang=zh-Hans) 2014/12/24 15:57 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/03/23 13:24 (当地)
 📏 3,406 | ⏱ 89


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/039111ac3670a940e7028bc76f9caa22.jpg)

[NL-2813272](https://www.postcrossing.com/postcards/NL-2813272) 
 >来自 [Lexa157](https://www.postcrossing.com/user/Lexa157) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=51.91917~4.38889&lvl=12.0&setlang=zh-Hans) 2014/12/24 10:43 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/03/12 19:24 (当地)
 📏 8,200 | ⏱ 78


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/83a035bc5fe08c8d0909db1aff55b3d9.jpg)

[DE-3809033](https://www.postcrossing.com/postcards/DE-3809033) 
 >来自 [BilleLovesBerlin](https://www.postcrossing.com/user/BilleLovesBerlin) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.43247~6.76516&lvl=12.0&setlang=zh-Hans) 2014/12/24 10:44 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/03/09 20:25 (当地)
 📏 8,079 | ⏱ 75


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/47a9a53e5fa97480e5e6314eefed0d89.jpg)

[RU-3283393](https://www.postcrossing.com/postcards/RU-3283393) 
 >来自 ***该用户已关闭*** 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=59.57639~30.12833&lvl=12.0&setlang=zh-Hans) 2014/12/11 21:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/03/09 20:24 (当地)
 📏 6,427 | ⏱ 88


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/055a622a026e8eadede572375354f6b7.jpg)

[NL-2813278](https://www.postcrossing.com/postcards/NL-2813278) 
 >来自 [Pippi2014](https://www.postcrossing.com/user/Pippi2014) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=52.255~6.16389&lvl=12.0&setlang=zh-Hans) 2014/12/24 10:51 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/03/08 23:15 (当地)
 📏 8,075 | ⏱ 74


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/190f02e512026930626537c18cbf9e03.jpg)

[RU-3209780](https://www.postcrossing.com/postcards/RU-3209780) 
 >来自 [Red_Queen](https://www.postcrossing.com/user/Red_Queen) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2014/11/19 09:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/03/08 23:10 (当地)
 📏 6,006 | ⏱ 109


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/d94058520953e038f4e8ea8ef0d0db75.jpg)

[BY-1456970](https://www.postcrossing.com/postcards/BY-1456970) 
 >来自 [olive_chemistry](https://www.postcrossing.com/user/olive_chemistry) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.9~27.56667&lvl=12.0&setlang=zh-Hans) 2014/11/19 09:11 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/01/04 13:04 (当地)
 📏 6,668 | ⏱ 46


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/2b1ce703735b60462dbd22a0c62b7020.jpg)

### 2014(34)

[UA-1140480](https://www.postcrossing.com/postcards/UA-1140480) 
 >来自 [Shvets-Jane](https://www.postcrossing.com/user/Shvets-Jane) 🇺🇦
> 📤 [Ukraine](https://www.bing.com/maps/?cp=50.45466~30.5238&lvl=12.0&setlang=zh-Hans) 2014/09/01 11:08 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/30 11:24 (当地)
 📏 6,539 | ⏱ 120


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/66f10b2a5d8fd27da71c75a2307c731e.jpg)

[NL-2773491](https://www.postcrossing.com/postcards/NL-2773491) 
 >来自 [Pjotter](https://www.postcrossing.com/user/Pjotter) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=51.53083~4.46528&lvl=12.0&setlang=zh-Hans) 2014/11/23 19:39 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/24 17:34 (当地)
 📏 8,216 | ⏱ 31


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/bc3219e3af342412898d563c5f90bb13.jpg)

[KR-112465](https://www.postcrossing.com/postcards/KR-112465) 
 >来自 [minjeomi89](https://www.postcrossing.com/user/minjeomi89) 🇰🇷
> 📤 [Korea (South)](https://www.bing.com/maps/?cp=35.10168~129.03004&lvl=12.0&setlang=zh-Hans) 2014/11/19 15:07 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/24 17:32 (当地)
 📏 2,193 | ⏱ 35


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/0774ccd1d3ea65b27193547f7df31ec3.jpg)

[UA-1195370](https://www.postcrossing.com/postcards/UA-1195370) 
 >来自 [oksanagamai](https://www.postcrossing.com/user/oksanagamai) 🇺🇦
> 📤 [Ukraine](https://www.bing.com/maps/?cp=50.47438~24.28288&lvl=12.0&setlang=zh-Hans) 2014/11/19 08:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/22 12:19 (当地)
 📏 6,969 | ⏱ 33


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/d45fbde0fa00ade1cda4f6bc1b3288e5.jpg)

[TW-1431636](https://www.postcrossing.com/postcards/TW-1431636) 
 >来自 [Mickeyliu](https://www.postcrossing.com/user/Mickeyliu) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=22.795~120.27639&lvl=12.0&setlang=zh-Hans) 2014/11/19 14:08 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/05 16:48 (当地)
 📏 1,582 | ⏱ 16


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/aab5646a22fce46cc103ef7d2f15e8bd.jpg)

[FI-2219730](https://www.postcrossing.com/postcards/FI-2219730) 
 >来自 [Holappa](https://www.postcrossing.com/user/Holappa) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=60.29414~25.04099&lvl=12.0&setlang=zh-Hans) 2014/10/02 12:15 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/10/21 16:12 (当地)
 📏 6,698 | ⏱ 19


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/5b170a8cf8ecc675cf73e408e1242d3b.jpg)

[DE-3561745](https://www.postcrossing.com/postcards/DE-3561745) 
 >来自 ***该用户已关闭*** 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.52437~13.41053&lvl=12.0&setlang=zh-Hans) 2014/10/02 20:24 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/10/20 18:46 (当地)
 📏 7,616 | ⏱ 18


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/115fb3fbf178d1960069b27c6c3737d9.jpg)

[CZ-524596](https://www.postcrossing.com/postcards/CZ-524596) 
 >来自 [Shalila](https://www.postcrossing.com/user/Shalila) 🇨🇿
> 📤 [Czechia](https://www.bing.com/maps/?cp=50.23271~12.87117&lvl=12.0&setlang=zh-Hans) 2014/10/02 11:48 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/10/20 18:45 (当地)
 📏 7,744 | ⏱ 18


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/9c9cf76ca55f0503b9de29da15eec701.jpg)

[BY-1380918](https://www.postcrossing.com/postcards/BY-1380918) 
 >来自 [Alenka1](https://www.postcrossing.com/user/Alenka1) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.9~27.56667&lvl=12.0&setlang=zh-Hans) 2014/09/01 08:35 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/26 17:22 (当地)
 📏 6,668 | ⏱ 25


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/c7d9cbca570f09443b2bce06e8c822ad.jpg)

[NL-2652178](https://www.postcrossing.com/postcards/NL-2652178) 
 >来自 [andrealandman](https://www.postcrossing.com/user/andrealandman) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=52.7875~4.79861&lvl=12.0&setlang=zh-Hans) 2014/09/02 15:22 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/22 12:57 (当地)
 📏 8,131 | ⏱ 20


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/09e42b276f4db73e1d6212b0d9912520.jpg)

[CA-463793](https://www.postcrossing.com/postcards/CA-463793) 
 >来自 [Stinkypaw](https://www.postcrossing.com/user/Stinkypaw) 🇨🇦
> 📤 [Canada](https://www.bing.com/maps/?cp=45.50884~-73.58781&lvl=12.0&setlang=zh-Hans) 2014/09/01 01:35 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/22 12:46 (当地)
 📏 11,636 | ⏱ 21


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/e505c7ac92af313eca757815b6e4d876.jpg)

[RU-2831920](https://www.postcrossing.com/postcards/RU-2831920) 
 >来自 [anni-danni](https://www.postcrossing.com/user/anni-danni) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2014/07/02 13:06 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/22 12:43 (当地)
 📏 6,006 | ⏱ 82


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/47ab21c1ca324c08a5498c81b211f380.jpg)

[FR-427139](https://www.postcrossing.com/postcards/FR-427139) 
 >来自 [Cyliane](https://www.postcrossing.com/user/Cyliane) 🇫🇷
> 📤 [France](https://www.bing.com/maps/?cp=46.0802~6.40726&lvl=12.0&setlang=zh-Hans) 2014/09/01 10:07 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/15 15:07 (当地)
 📏 8,374 | ⏱ 14


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/b4f5c081a0694d655c023f12e7e0648c.jpg)

[KR-104416](https://www.postcrossing.com/postcards/KR-104416) 
 >来自 [yaho-anna](https://www.postcrossing.com/user/yaho-anna) 🇰🇷
> 📤 [Korea (South)](https://www.bing.com/maps/?cp=37.566~126.9784&lvl=12.0&setlang=zh-Hans) 2014/08/13 09:19 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/02 17:00 (当地)
 📏 2,080 | ⏱ 20


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/045349fb114b9fc3739d25a94faafb59.jpg)

[MK-4914](https://www.postcrossing.com/postcards/MK-4914) 
 >来自 [anea09](https://www.postcrossing.com/user/anea09) 🇲🇰
> 📤 [North Macedonia](https://www.bing.com/maps/?cp=41.03143~21.33474&lvl=12.0&setlang=zh-Hans) 2014/07/06 15:51 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/01 13:32 (当地)
 📏 7,506 | ⏱ 57


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/027977b2fc60946bdef3e870409e288c.jpg)

[BY-1344892](https://www.postcrossing.com/postcards/BY-1344892) 
 >来自 [MiLENA-](https://www.postcrossing.com/user/MiLENA-) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.9~27.56667&lvl=12.0&setlang=zh-Hans) 2014/07/21 00:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/01 13:30 (当地)
 📏 6,668 | ⏱ 42


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/e55ff63ed70b0588f6ca26a3110dd8fa.jpg)

[JP-546807](https://www.postcrossing.com/postcards/JP-546807) 
 >来自 [khitomi](https://www.postcrossing.com/user/khitomi) 🇯🇵
> 📤 [Japan](https://www.bing.com/maps/?cp=34.4~132.45&lvl=12.0&setlang=zh-Hans) 2014/06/04 17:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/06/16 16:08 (当地)
 📏 2,493 | ⏱ 12


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/ccc32e154e8dd8abbcfc3ca6891de7ff.jpg)

[MY-205746](https://www.postcrossing.com/postcards/MY-205746) 
 >来自 [vin_ann](https://www.postcrossing.com/user/vin_ann) 🇲🇾
> 📤 [Malaysia](https://www.bing.com/maps/?cp=3.1412~101.68653&lvl=12.0&setlang=zh-Hans) 2014/05/14 20:23 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/30 21:33 (当地)
 📏 3,007 | ⏱ 16


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/e853702f3763f1a51c65437542e2c580.jpg)

[BY-1268116](https://www.postcrossing.com/postcards/BY-1268116) 
 >来自 [Avruha](https://www.postcrossing.com/user/Avruha) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.6884~23.8258&lvl=12.0&setlang=zh-Hans) 2014/04/28 14:43 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/20 11:59 (当地)
 📏 6,913 | ⏱ 22


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/4eec17ae7a8f6caf0a7d2ceb5843e958.jpg)

[DE-3097383](https://www.postcrossing.com/postcards/DE-3097383) 
 >来自 [Gaby1967](https://www.postcrossing.com/user/Gaby1967) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.43081~7.06833&lvl=12.0&setlang=zh-Hans) 2014/04/16 19:40 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/12 12:17 (当地)
 📏 8,011 | ⏱ 25


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/e8df72704276939fc7633e07e85e08ce.jpg)

[RU-1876931](https://www.postcrossing.com/postcards/RU-1876931) 
 >来自 [Krasovskii](https://www.postcrossing.com/user/Krasovskii) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=60.70763~28.75283&lvl=12.0&setlang=zh-Hans) 2013/07/22 20:14 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/12 12:14 (当地)
 📏 6,503 | ⏱ 294


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/aa4cde8359c36bf565da6659226cefb0.jpg)

[NL-2441827](https://www.postcrossing.com/postcards/NL-2441827) 
 >来自 [Nighthawk1964](https://www.postcrossing.com/user/Nighthawk1964) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=53.10325~6.01853&lvl=12.0&setlang=zh-Hans) 2014/04/10 20:25 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/09 12:40 (当地)
 📏 8,037 | ⏱ 28


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/af953a2a9c7b70b4bb38553b878ed213.jpg)

[FI-2084613](https://www.postcrossing.com/postcards/FI-2084613) 
 >来自 [orienteerer](https://www.postcrossing.com/user/orienteerer) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=61.03333~22.33333&lvl=12.0&setlang=zh-Hans) 2014/04/23 14:35 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/09 12:38 (当地)
 📏 6,827 | ⏱ 16


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/56a617562753c57021112273b8354ad5.jpg)

[DE-2941052](https://www.postcrossing.com/postcards/DE-2941052) 
 >来自 [bluebutterfly222](https://www.postcrossing.com/user/bluebutterfly222) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.71754~11.05877&lvl=12.0&setlang=zh-Hans) 2014/02/24 01:03 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/04/16 12:36 (当地)
 📏 7,885 | ⏱ 51


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/0mc10wez9rlow90hnqkmstdgb4y304iw.jpg)

[UA-982846](https://www.postcrossing.com/postcards/UA-982846) 
 >来自 [lerolero](https://www.postcrossing.com/user/lerolero) 🇺🇦
> 📤 [Ukraine](https://www.bing.com/maps/?cp=50.45466~30.5238&lvl=12.0&setlang=zh-Hans) 2014/03/04 23:36 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/04/16 12:34 (当地)
 📏 6,539 | ⏱ 42


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/5f24a48ce251612c0861489bce22269c.jpg)

[TW-1215866](https://www.postcrossing.com/postcards/TW-1215866) 
 >来自 [Penny7](https://www.postcrossing.com/user/Penny7) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=24.99298~121.49385&lvl=12.0&setlang=zh-Hans) 2014/03/28 23:21 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/04/16 12:32 (当地)
 📏 1,579 | ⏱ 19


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/a418497762809c32d8b20c85a8d10b4f.jpg)

[MY-198583](https://www.postcrossing.com/postcards/MY-198583) 
 >来自 [KaiQin](https://www.postcrossing.com/user/KaiQin) 🇲🇾
> 📤 [Malaysia](https://www.bing.com/maps/?cp=1.4655~103.7578&lvl=12.0&setlang=zh-Hans) 2014/03/28 13:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/04/11 19:12 (当地)
 📏 3,165 | ⏱ 14


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/4wxbm70ou30tc5ylp4ylkvqyhr9hskmg.jpg)

[TW-1213069](https://www.postcrossing.com/postcards/TW-1213069) 
 >来自 [Viola-Pan](https://www.postcrossing.com/user/Viola-Pan) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=25.04776~121.53185&lvl=12.0&setlang=zh-Hans) 2014/03/26 01:35 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/04/04 20:20 (当地)
 📏 1,573 | ⏱ 10


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/4ju868hwkvsljxqh8jz4051n7rmmoc5t.jpg)

[NL-2374423](https://www.postcrossing.com/postcards/NL-2374423) 
 >来自 [Anoushka](https://www.postcrossing.com/user/Anoushka) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=52.2375~4.82639&lvl=12.0&setlang=zh-Hans) 2014/03/02 13:22 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/03/24 12:14 (当地)
 📏 8,157 | ⏱ 22


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/dcb79e94963d086e9b2fd7d60588ae24.jpg)

[BY-1117952](https://www.postcrossing.com/postcards/BY-1117952) 
 >来自 [Breeze87](https://www.postcrossing.com/user/Breeze87) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.9~27.56667&lvl=12.0&setlang=zh-Hans) 2013/12/09 14:28 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/02/19 20:34 (当地)
 📏 6,679 | ⏱ 72


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/j9r0fza27qilbesdeg04htxpugzg33js.jpg)

[DE-2812796](https://www.postcrossing.com/postcards/DE-2812796) 
 >来自 [ostsee23730](https://www.postcrossing.com/user/ostsee23730) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=54.10707~10.8145&lvl=12.0&setlang=zh-Hans) 2014/01/13 06:55 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/02/19 20:34 (当地)
 📏 7,722 | ⏱ 37


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/y0y2qqj7716dookhnv8dbtdgax2h59mh.jpg)

[RU-2254488](https://www.postcrossing.com/postcards/RU-2254488) 
 >来自 [SouthWest](https://www.postcrossing.com/user/SouthWest) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=59.93863~30.31413&lvl=12.0&setlang=zh-Hans) 2013/12/09 15:39 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/02/19 20:33 (当地)
 📏 6,424 | ⏱ 72


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/bbfs4b2o9brbjavgkqkbf1l9aiwg1o3a.jpg)

[US-2568426](https://www.postcrossing.com/postcards/US-2568426) 
 >来自 [century26](https://www.postcrossing.com/user/century26) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=33.44838~-112.07404&lvl=12.0&setlang=zh-Hans) 2013/12/28 13:50 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/02/19 20:32 (当地)
 📏 11,911 | ⏱ 53


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/k9m503n0xlxcrqlj6pw14nsgts3825yt.jpg)

[TW-1121808](https://www.postcrossing.com/postcards/TW-1121808) 
 >来自 [YunHung](https://www.postcrossing.com/user/YunHung) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=23.73944~120.56444&lvl=12.0&setlang=zh-Hans) 2013/12/28 22:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/01/13 12:25 (当地)
 📏 1,554 | ⏱ 16


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/sg7kqtzxlhr5m9vrglqx2nm0i9vgtzs5.jpg)

### 2013(5)

[RU-2144539](https://www.postcrossing.com/postcards/RU-2144539) 
 >来自 [fulun](https://www.postcrossing.com/user/fulun) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=53.20007~50.15&lvl=12.0&setlang=zh-Hans) 2013/11/03 18:40 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/12/09 19:27 (当地)
 📏 5,192 | ⏱ 36


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/x5us9epjm1k0rzun7wy5mqo4duh0q8mc.jpg)

[BY-1066085](https://www.postcrossing.com/postcards/BY-1066085) 
 >来自 [poliakos](https://www.postcrossing.com/user/poliakos) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=52.4345~30.9754&lvl=12.0&setlang=zh-Hans) 2013/10/26 17:38 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/12/09 19:21 (当地)
 📏 6,480 | ⏱ 44


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/47jtvrurpcy8h4ppd4fuj25btx4d64s3.jpg)

[CZ-322514](https://www.postcrossing.com/postcards/CZ-322514) 
 >来自 [TerezkaS](https://www.postcrossing.com/user/TerezkaS) 🇨🇿
> 📤 [Czechia](https://www.bing.com/maps/?cp=49.36064~18.28355&lvl=12.0&setlang=zh-Hans) 2013/08/09 02:10 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/10/02 07:25 (当地)
 📏 7,427 | ⏱ 54


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/ybl39ka8m4j3eyrbyhxga685zhad5v3c.jpg)

[DE-2337903](https://www.postcrossing.com/postcards/DE-2337903) 
 >来自 [Amarosi](https://www.postcrossing.com/user/Amarosi) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=54.9079~8.30326&lvl=12.0&setlang=zh-Hans) 2013/07/22 18:05 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/08/30 15:14 (当地)
 📏 7,835 | ⏱ 39


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/f51f92694ae3571dee5e80be73a063dc.jpg)

[NL-1979851](https://www.postcrossing.com/postcards/NL-1979851) 
 >来自 [airsnowmiss](https://www.postcrossing.com/user/airsnowmiss) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=51.44083~5.47778&lvl=12.0&setlang=zh-Hans) 2013/07/25 17:57 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/08/30 15:12 (当地)
 📏 8,174 | ⏱ 36


![](https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/gallery/picture/f034894d687e190e2552bb2b6946be17.jpg)


