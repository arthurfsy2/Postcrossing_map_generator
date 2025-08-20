---
title: 明信片展示墙（寄出：192）
icon: address-card
date: 2025-08-19
category:
  - Arthur
tag:
  - postcrossing
order: 2
---

## [arthurfsy's sent](https://www.postcrossing.com/user/arthurfsy/gallery/sent)

### 收发记录（年度）

::: echarts

```js
const data = await fetch(
  "https://raw.githubusercontent.com/arthurfsy2/Postcrossing_map_generator/main/output/year.json"
).then((res) => res.json());

const newData = data.map(({ year, sent}) => ({ name: year, value: sent}));

const option = {
  title: {
    text: "",
    subtext: "",
    left: "center",
  },
  tooltip: {
    trigger: "item",
    formatter: "{a} <br/>{b} : {c} ({d}%)",
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
          shadowColor: "rgba(0, 0, 0, 0.5)",
        },
      },
      label: {
        alignTo: "none",
        formatter: "{name|{b}}\n{value|{d}%}",
        minMargin: 1,
        fontStyle: "italic",
        fontWeight: "bold",

        rich: {
          num: {
            fontSize: 10,
            color: "#999",
          },
        },
      },
      labelLine: {
        length: 50,
      },
    },
  ],
};
```

:::

### 收发记录（月度）

:::echarts

```js
const data = await fetch(
  "https://raw.githubusercontent.com/arthurfsy2/Postcrossing_map_generator/main/output/month.json"
).then((res) => res.json());

var date = data.map(function (item) {
  return item.date;
});

var sent = data.map(function (item) {
  return item.sent;
});

var sentSum = sent.reduce(function (acc, curr) {
  return acc + curr;
}, 0);

var received = data.map(function (item) {
  return item.received;
});

var receivedSum = received.reduce(function (acc, curr) {
  return acc + curr;
}, 0);

sentName = sentSum + "张已寄出";
receivedName = receivedSum + "张已收到";

const option = {
  title: {
    text: "",
    left: "center",
  },
  legend: {
    data: [sentName, receivedName],
  },
  tooltip: {
    trigger: "axis",
  },
  xAxis: {
    type: "category",
    data: date,
  },
  yAxis: {
    type: "value",
  },
  dataZoom: [
    {
      start: 0,
    },
    {
      type: "inside",
    },
  ],
  series: [
    {
      name: sentName,
      data: sent,
      type: "line",
      smooth: true,
    },
    {
      name: receivedName,
      data: received,
      type: "line",
      smooth: true,
    },
  ],
};
```

:::

### 2025(53)

[CN-4069193](https://www.postcrossing.com/postcards/CN-4069193) 
>寄往 [reinholdo](https://www.postcrossing.com/user/reinholdo) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/07/08 13:10 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=50.10068~11.45032&lvl=12.0&setlang=zh-Hans) 2025/08/19 16:54 (当地)
 📏 8,962 | ⏱ 42


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/24o8k77m4j4b3uy9ffd0lieq88nsl1t3.jpg)

[CN-4069192](https://www.postcrossing.com/postcards/CN-4069192) 
>寄往 [zaza19](https://www.postcrossing.com/user/zaza19) 🇫🇷
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/07/08 13:10 (当地)
> 📥 [France](https://www.bing.com/maps/?cp=45.60366~-0.84802&lvl=12.0&setlang=zh-Hans) 2025/08/13 10:03 (当地)
 📏 10,006 | ⏱ 36


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/2ysctkozw6a5cnh8lzgg7rziu38fy2ip.jpg)

[CN-4069195](https://www.postcrossing.com/postcards/CN-4069195) 
>寄往 [Tomo3](https://www.postcrossing.com/user/Tomo3) 🇯🇵
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/07/08 13:10 (当地)
> 📥 [Japan](https://www.bing.com/maps/?cp=40.68682~141.38969&lvl=12.0&setlang=zh-Hans) 2025/08/07 09:30 (当地)
 📏 3,243 | ⏱ 30


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/goc8i0ep9spq0mzla3u3aqj6na3b4vn3.jpg)

[CN-4060193](https://www.postcrossing.com/postcards/CN-4060193) 
>寄往 [cerres](https://www.postcrossing.com/user/cerres) 🇪🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/06/25 13:27 (当地)
> 📥 [Estonia](https://www.bing.com/maps/?cp=59.43696~24.75353&lvl=12.0&setlang=zh-Hans) 2025/07/29 22:32 (当地)
 📏 7,833 | ⏱ 35


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/13xye3fikfq7lf8me2uklj2ur4yq1fex.jpg)

[CN-4060194](https://www.postcrossing.com/postcards/CN-4060194) 
>寄往 [mijasn](https://www.postcrossing.com/user/mijasn) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/06/25 13:30 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=48.88791~9.39267&lvl=12.0&setlang=zh-Hans) 2025/07/26 11:45 (当地)
 📏 9,154 | ⏱ 31


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/g6eyy6qdsloskg857w2r5e4kuk0a7sdv.jpg)

[CN-4060782](https://www.postcrossing.com/postcards/CN-4060782) 
>寄往 [saher](https://www.postcrossing.com/user/saher) 🇮🇳
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/06/26 14:25 (当地)
> 📥 [India](https://www.bing.com/maps/?cp=18.51957~73.85535&lvl=12.0&setlang=zh-Hans) 2025/07/21 21:54 (当地)
 📏 4,216 | ⏱ 25


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/898fn6rp3b56dokhobv3ix1xz5h3jpvt.jpg)

[CN-4032664](https://www.postcrossing.com/postcards/CN-4032664) 
>寄往 [Tuulukka](https://www.postcrossing.com/user/Tuulukka) 🇫🇮
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:12 (当地)
> 📥 [Finland](https://www.bing.com/maps/?cp=60.16952~24.93545&lvl=12.0&setlang=zh-Hans) 2025/07/21 13:33 (当地)
 📏 7,807 | ⏱ 63


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/pez7popbcjpxwdssoq11pvot0zxisq3f.jpg)

[CN-4032659](https://www.postcrossing.com/postcards/CN-4032659) 
>寄往 [Shadowflame](https://www.postcrossing.com/user/Shadowflame) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:11 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=48.40351~11.74876&lvl=12.0&setlang=zh-Hans) 2025/07/13 10:25 (当地)
 📏 9,020 | ⏱ 55


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/9vfojcwphezhvttokwptncztvwnkv7mu.jpg)

[CN-4032669](https://www.postcrossing.com/postcards/CN-4032669) 
>寄往 [AlexVL](https://www.postcrossing.com/user/AlexVL) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:12 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=43.10562~131.87353&lvl=12.0&setlang=zh-Hans) 2025/07/08 13:24 (当地)
 📏 2,804 | ⏱ 50


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/nsu6fl4j493uewn462gj12oekzw0zu12.jpg)

[CN-4032670](https://www.postcrossing.com/postcards/CN-4032670) 
>寄往 [mlodor](https://www.postcrossing.com/user/mlodor) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:12 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=40.34785~-79.86422&lvl=12.0&setlang=zh-Hans) 2025/07/03 10:42 (当地)
 📏 12,869 | ⏱ 46


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/rg6npvad9msk2704i1sx5q7l78l8ltei.jpg)

[CN-4032665](https://www.postcrossing.com/postcards/CN-4032665) 
>寄往 [legacy_hardware](https://www.postcrossing.com/user/legacy_hardware) 🇦🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:12 (当地)
> 📥 [Australia](https://www.bing.com/maps/?cp=-37.96667~145.16667&lvl=12.0&setlang=zh-Hans) 2025/07/03 16:35 (当地)
 📏 7,465 | ⏱ 45


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/kqjzenervwpjxboc1i3l5snbswdqjj0r.jpg)

[CN-4032662](https://www.postcrossing.com/postcards/CN-4032662) 
>寄往 [MissErica](https://www.postcrossing.com/user/MissErica) 🇨🇦
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:12 (当地)
> 📥 [Canada](https://www.bing.com/maps/?cp=45.68342~-74.4159&lvl=12.0&setlang=zh-Hans) 2025/06/26 18:06 (当地)
 📏 12,376 | ⏱ 39


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/ewg1tz5sqrew7mqeqwhv0lfp5cxolt5q.jpg)

[CN-4032666](https://www.postcrossing.com/postcards/CN-4032666) 
>寄往 [Vejoseselis](https://www.postcrossing.com/user/Vejoseselis) 🇱🇹
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:12 (当地)
> 📥 [Lithuania](https://www.bing.com/maps/?cp=54.68916~25.2798&lvl=12.0&setlang=zh-Hans) 2025/06/26 08:46 (当地)
 📏 7,913 | ⏱ 38


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/83fgzsdzcuwhsyg8z9pg2w89l5i8yio1.jpg)

[CN-4032661](https://www.postcrossing.com/postcards/CN-4032661) 
>寄往 [amartinez](https://www.postcrossing.com/user/amartinez) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:11 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=40.69161~-112.00105&lvl=12.0&setlang=zh-Hans) 2025/06/24 22:32 (当地)
 📏 11,513 | ⏱ 37


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/25mfdljifnv9wy5yw2qufql4ujfrlpmy.jpg)

[CN-3980200](https://www.postcrossing.com/postcards/CN-3980200) 
>寄往 [Eiju](https://www.postcrossing.com/user/Eiju) 🇫🇮
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/13 13:52 (当地)
> 📥 [Finland](https://www.bing.com/maps/?cp=63.9~23.9&lvl=12.0&setlang=zh-Hans) 2025/06/23 18:48 (当地)
 📏 7,782 | ⏱ 102


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/946bujlp2fta6kfw8tzaibyizrrrpdg8.jpg)

[CN-3980204](https://www.postcrossing.com/postcards/CN-3980204) 
>寄往 [nicky1983](https://www.postcrossing.com/user/nicky1983) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/13 13:53 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=53.28308~13.66136&lvl=12.0&setlang=zh-Hans) 2025/06/23 07:58 (当地)
 📏 8,684 | ⏱ 102


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/2olzlmzpvjgvv5gghlysiixkw5lxa1w3.jpg)

[CN-4032668](https://www.postcrossing.com/postcards/CN-4032668) 
>寄往 [hjbcats](https://www.postcrossing.com/user/hjbcats) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:12 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=38.65922~-87.17279&lvl=12.0&setlang=zh-Hans) 2025/06/21 20:02 (当地)
 📏 12,851 | ⏱ 34


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/90m6css5jvh2ybtipnkmaad6htmhusje.jpg)

[CN-4032663](https://www.postcrossing.com/postcards/CN-4032663) 
>寄往 [Jakez44](https://www.postcrossing.com/user/Jakez44) 🇫🇷
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:12 (当地)
> 📥 [France](https://www.bing.com/maps/?cp=47.21725~-1.55336&lvl=12.0&setlang=zh-Hans) 2025/06/21 15:40 (当地)
 📏 9,952 | ⏱ 33


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/q8r5z3ul6wisg1dm44rz2txiz2xhb9ko.jpg)

[CN-3980206](https://www.postcrossing.com/postcards/CN-3980206) 
>寄往 [OlafArens](https://www.postcrossing.com/user/OlafArens) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/13 13:53 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=51.48165~7.21648&lvl=12.0&setlang=zh-Hans) 2025/06/14 16:38 (当地)
 📏 9,165 | ⏱ 93


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/jxx1bp337bo7ejbmfe8hgsngcqbbjw9v.jpg)

[CN-4032667](https://www.postcrossing.com/postcards/CN-4032667) 
>寄往 [Altalsbach1](https://www.postcrossing.com/user/Altalsbach1) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:12 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=53.56952~9.61218&lvl=12.0&setlang=zh-Hans) 2025/06/10 17:24 (当地)
 📏 8,917 | ⏱ 23


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/92h2bdomcyd4hrkxc7zv5271ptpl7ibm.jpg)

[CN-4032660](https://www.postcrossing.com/postcards/CN-4032660) 
>寄往 [KITTEmeguri](https://www.postcrossing.com/user/KITTEmeguri) 🇯🇵
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:11 (当地)
> 📥 [Japan](https://www.bing.com/maps/?cp=33.31667~130.51667&lvl=12.0&setlang=zh-Hans) 2025/06/10 22:22 (当地)
 📏 1,992 | ⏱ 22


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/cmy3xmky1lfo64bv9z8j0x45za738hnj.jpg)

[CN-4001501](https://www.postcrossing.com/postcards/CN-4001501) 
>寄往 [Valenti](https://www.postcrossing.com/user/Valenti) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/04/08 15:28 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=61.68523~50.80819&lvl=12.0&setlang=zh-Hans) 2025/05/30 17:41 (当地)
 📏 6,420 | ⏱ 52


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/mb57zn2hh38qfil56sp4t6uas13zsorv.jpg)

[CN-4001499](https://www.postcrossing.com/postcards/CN-4001499) 
>寄往 [Evenstar3896](https://www.postcrossing.com/user/Evenstar3896) 🇳🇱
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/04/08 15:28 (当地)
> 📥 [Netherlands](https://www.bing.com/maps/?cp=52.20333~4.63333&lvl=12.0&setlang=zh-Hans) 2025/05/15 23:00 (当地)
 📏 9,284 | ⏱ 38


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/rwddnn08cj8u77w6wkvvtpphb3hc2bfu.jpg)

[CN-3980201](https://www.postcrossing.com/postcards/CN-3980201) 
>寄往 [rosscott](https://www.postcrossing.com/user/rosscott) 🇦🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/13 13:52 (当地)
> 📥 [Australia](https://www.bing.com/maps/?cp=-41.05584~145.90375&lvl=12.0&setlang=zh-Hans) 2025/05/15 10:00 (当地)
 📏 7,792 | ⏱ 63


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/f8ntrhxb2on3at7u1nuf0yruxfthhvl4.jpg)

[CN-3930389](https://www.postcrossing.com/postcards/CN-3930389) 
>寄往 [BarbSchmidt](https://www.postcrossing.com/user/BarbSchmidt) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/01/08 13:09 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=33.24678~-84.26409&lvl=12.0&setlang=zh-Hans) 2025/05/11 23:10 (当地)
 📏 13,507 | ⏱ 124


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/xf7k56nmftkbwvsgqvtv21a71ws6goru.jpg)

[CN-4001500](https://www.postcrossing.com/postcards/CN-4001500) 
>寄往 [VJacinto](https://www.postcrossing.com/user/VJacinto) 🇵🇹
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/04/08 15:28 (当地)
> 📥 [Portugal](https://www.bing.com/maps/?cp=38.06078~-8.7822&lvl=12.0&setlang=zh-Hans) 2025/05/05 12:13 (当地)
 📏 11,029 | ⏱ 27


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/mqaymn693ueghj626ftbfonj9fqqq643.jpg)

[CN-3980203](https://www.postcrossing.com/postcards/CN-3980203) 
>寄往 [dariusz1212](https://www.postcrossing.com/user/dariusz1212) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/13 13:53 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=33.44838~-112.07404&lvl=12.0&setlang=zh-Hans) 2025/04/29 23:07 (当地)
 📏 12,088 | ⏱ 48


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/0plti68m2are73y77vm0m075kebgr7e1.jpg)

[CN-3980202](https://www.postcrossing.com/postcards/CN-3980202) 
>寄往 [pcer9527](https://www.postcrossing.com/user/pcer9527) 🇹🇼
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/13 13:53 (当地)
> 📥 [Taiwan](https://www.bing.com/maps/?cp=22.99083~120.21333&lvl=12.0&setlang=zh-Hans) 2025/04/26 10:30 (当地)
 📏 614 | ⏱ 44


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/g6mzbsujjrgmtkr9numic6hybv3hwhya.jpg)

[CN-3914593](https://www.postcrossing.com/postcards/CN-3914593) 
>寄往 [yanusha_k](https://www.postcrossing.com/user/yanusha_k) 🇧🇾
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/12/18 17:35 (当地)
> 📥 [Belarus](https://www.bing.com/maps/?cp=53.9614~27.6696&lvl=12.0&setlang=zh-Hans) 2025/04/25 22:42 (当地)
 📏 7,778 | ⏱ 128


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/69mka1r7h2qgyydamzlmdgl3r99wt65w.jpg)

[CN-3980199](https://www.postcrossing.com/postcards/CN-3980199) 
>寄往 [Olga_Zybailo17](https://www.postcrossing.com/user/Olga_Zybailo17) 🇧🇾
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/13 13:52 (当地)
> 📥 [Belarus](https://www.bing.com/maps/?cp=53.9~27.56667&lvl=12.0&setlang=zh-Hans) 2025/04/24 21:36 (当地)
 📏 7,786 | ⏱ 43


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/2rsrtiw1nkb8lcnq5ktwkk1eracyutn0.jpg)

[CN-3986781](https://www.postcrossing.com/postcards/CN-3986781) 
>寄往 [Ntkkak](https://www.postcrossing.com/user/Ntkkak) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/21 16:02 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=59.93863~30.31413&lvl=12.0&setlang=zh-Hans) 2025/04/24 14:53 (当地)
 📏 7,517 | ⏱ 34


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/gfw635yyl3ktvc3opc3v62q92slobk1m.jpg)

[CN-3962833](https://www.postcrossing.com/postcards/CN-3962833) 
>寄往 [contessedelphine](https://www.postcrossing.com/user/contessedelphine) 🇫🇷
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/21 00:20 (当地)
> 📥 [France](https://www.bing.com/maps/?cp=48.38333~2.95&lvl=12.0&setlang=zh-Hans) 2025/04/11 14:39 (当地)
 📏 9,598 | ⏱ 50


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/22pl99b5ezw36ezo481n1y8xdo7a2xo6.jpg)

[CN-3961585](https://www.postcrossing.com/postcards/CN-3961585) 
>寄往 [Lcabal](https://www.postcrossing.com/user/Lcabal) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/19 14:30 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=32.67895~-115.49888&lvl=12.0&setlang=zh-Hans) 2025/04/06 17:58 (当地)
 📏 11,917 | ⏱ 47


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/nhkzqidfuexp1uj1cgcms9xz0xihcvsy.jpg)

[CN-3961584](https://www.postcrossing.com/postcards/CN-3961584) 
>寄往 [rakete78](https://www.postcrossing.com/user/rakete78) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/19 14:30 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=51.17343~7.0845&lvl=12.0&setlang=zh-Hans) 2025/04/04 09:43 (当地)
 📏 9,188 | ⏱ 44


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/oopbyh8br0e58op1eiv9n3dlwgjxqx2r.jpg)

[CN-3930391](https://www.postcrossing.com/postcards/CN-3930391) 
>寄往 [Zandy](https://www.postcrossing.com/user/Zandy) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/01/08 13:09 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=49.23498~9.33215&lvl=12.0&setlang=zh-Hans) 2025/04/01 22:12 (当地)
 📏 9,141 | ⏱ 84


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/c87dkppy2aooigeqo9gc7jddky3gj609.jpg)

[CN-3963357](https://www.postcrossing.com/postcards/CN-3963357) 
>寄往 [Seliad](https://www.postcrossing.com/user/Seliad) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/21 15:27 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=49.59099~11.00783&lvl=12.0&setlang=zh-Hans) 2025/04/01 16:41 (当地)
 📏 9,015 | ⏱ 39


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/iihmjjid3jxo5jagst9okum1wq2d19zn.jpg)

[CN-3935240](https://www.postcrossing.com/postcards/CN-3935240) 
>寄往 ***该用户已关闭*** 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/01/14 09:44 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=60.04796~30.45204&lvl=12.0&setlang=zh-Hans) 2025/03/18 18:46 (当地)
 📏 7,507 | ⏱ 64


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/u82y210bep54zo996zz2dvc2symy6lyw.jpg)

[CN-3934897](https://www.postcrossing.com/postcards/CN-3934897) 
>寄往 [wanderingAkash](https://www.postcrossing.com/user/wanderingAkash) 🇮🇳
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/01/13 17:44 (当地)
> 📥 [India](https://www.bing.com/maps/?cp=12.97194~77.59369&lvl=12.0&setlang=zh-Hans) 2025/03/09 20:29 (当地)
 📏 4,011 | ⏱ 55


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/5dj5j08chro7djyf0ccb03pe1as2dvr8.jpg)

[CN-3944801](https://www.postcrossing.com/postcards/CN-3944801) 
>寄往 [Konobas](https://www.postcrossing.com/user/Konobas) 🇺🇦
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/01/26 09:10 (当地)
> 📥 [Ukraine](https://www.bing.com/maps/?cp=50.45466~30.5238&lvl=12.0&setlang=zh-Hans) 2025/03/08 00:18 (当地)
 📏 7,659 | ⏱ 41


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/9818nknsk932ev0gl0cku7umlwoky47e.jpg)

[CN-3931256](https://www.postcrossing.com/postcards/CN-3931256) 
>寄往 [Trans_Niqabi](https://www.postcrossing.com/user/Trans_Niqabi) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/01/09 13:27 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=41.92704~-73.99736&lvl=12.0&setlang=zh-Hans) 2025/03/04 16:16 (当地)
 📏 12,794 | ⏱ 55


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/owbjrgmuxy4hurps9chs0fqen9vl2qni.jpg)

[CN-3944802](https://www.postcrossing.com/postcards/CN-3944802) 
>寄往 [LarisaLeon](https://www.postcrossing.com/user/LarisaLeon) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/01/26 09:11 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=54.5293~36.27542&lvl=12.0&setlang=zh-Hans) 2025/03/04 11:28 (当地)
 📏 7,216 | ⏱ 37


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/emcelxgwyr4qgig54h9wq7il0r2hd2u6.jpg)

[CN-3954376](https://www.postcrossing.com/postcards/CN-3954376) 
>寄往 [Tiesk](https://www.postcrossing.com/user/Tiesk) 🇳🇱
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/10 09:52 (当地)
> 📥 [Netherlands](https://www.bing.com/maps/?cp=51.6825~5.07083&lvl=12.0&setlang=zh-Hans) 2025/02/28 14:04 (当地)
 📏 9,285 | ⏱ 18


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/lgvuteqfjtqbqgc7wbh9xc8cgxu3qhje.jpg)

[CN-3930378](https://www.postcrossing.com/postcards/CN-3930378) 
>寄往 [disisdi](https://www.postcrossing.com/user/disisdi) 🇦🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/01/08 13:06 (当地)
> 📥 [Australia](https://www.bing.com/maps/?cp=-37.814~144.96332&lvl=12.0&setlang=zh-Hans) 2025/02/21 17:16 (当地)
 📏 7,441 | ⏱ 44


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/a1nwb6qdm9rfouo2upgxa13pcl2rzgel.jpg)

[CN-3934895](https://www.postcrossing.com/postcards/CN-3934895) 
>寄往 [catherine_rol](https://www.postcrossing.com/user/catherine_rol) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/01/13 17:44 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=52.60311~39.57076&lvl=12.0&setlang=zh-Hans) 2025/02/20 14:50 (当地)
 📏 7,011 | ⏱ 38


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/o0dfwi5r0cgy3910p26rc06ardxs0z1q.jpg)

[CN-3839329](https://www.postcrossing.com/postcards/CN-3839329) 
>寄往 ***该用户已关闭*** 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/09/14 09:45 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=48.78583~44.77973&lvl=12.0&setlang=zh-Hans) 2025/02/19 03:00 (当地)
 📏 6,655 | ⏱ 158


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/qcgop1nvq3p6s3b7wh3u2cupklkh683u.jpg)

[CN-3930388](https://www.postcrossing.com/postcards/CN-3930388) 
>寄往 [gentiana](https://www.postcrossing.com/user/gentiana) 🇫🇮
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/01/08 13:09 (当地)
> 📥 [Finland](https://www.bing.com/maps/?cp=60.16952~24.93545&lvl=12.0&setlang=zh-Hans) 2025/02/17 19:49 (当地)
 📏 7,807 | ⏱ 41


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/huuc7gj6o17z25dje2awdg4s98gr56ma.jpg)

[CN-3914594](https://www.postcrossing.com/postcards/CN-3914594) 
>寄往 [manu86](https://www.postcrossing.com/user/manu86) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/12/18 17:35 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=49.56798~10.88565&lvl=12.0&setlang=zh-Hans) 2025/01/31 22:28 (当地)
 📏 9,024 | ⏱ 44


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/8jqgqwyqukx95qvq3eg30p0sjo8044yy.jpg)

[CN-3914595](https://www.postcrossing.com/postcards/CN-3914595) 
>寄往 [jukar](https://www.postcrossing.com/user/jukar) 🇫🇮
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/12/18 17:35 (当地)
> 📥 [Finland](https://www.bing.com/maps/?cp=60.16952~24.93545&lvl=12.0&setlang=zh-Hans) 2025/01/18 10:17 (当地)
 📏 7,807 | ⏱ 31


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/km15x6a8vx8zl2o07p5yxqycgkaickrc.jpg)

[CN-3893937](https://www.postcrossing.com/postcards/CN-3893937) 
>寄往 [TBattung](https://www.postcrossing.com/user/TBattung) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/22 13:19 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=37.77993~-121.97802&lvl=12.0&setlang=zh-Hans) 2025/01/13 17:41 (当地)
 📏 11,101 | ⏱ 53


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/oeh2sle1t8517lrqhcf0ic5j3g834wg7.jpg)

[CN-3914596](https://www.postcrossing.com/postcards/CN-3914596) 
>寄往 [Amillisyn](https://www.postcrossing.com/user/Amillisyn) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/12/18 17:35 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=52.37052~9.73322&lvl=12.0&setlang=zh-Hans) 2025/01/11 12:04 (当地)
 📏 8,966 | ⏱ 24


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/d4ap93yblbluwl8gedmakapb2zl3lpzn.jpg)

[CN-3893936](https://www.postcrossing.com/postcards/CN-3893936) 
>寄往 [Metelitsa](https://www.postcrossing.com/user/Metelitsa) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/22 13:18 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=56.84976~53.20448&lvl=12.0&setlang=zh-Hans) 2025/01/09 09:18 (当地)
 📏 6,176 | ⏱ 48


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/ah46sfrc4imco98jq7aal3xpvfxvriaw.jpg)

[CN-3886025](https://www.postcrossing.com/postcards/CN-3886025) 
>寄往 [Berry_Duck](https://www.postcrossing.com/user/Berry_Duck) 🇳🇱
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/12 13:02 (当地)
> 📥 [Netherlands](https://www.bing.com/maps/?cp=52.2375~4.82639&lvl=12.0&setlang=zh-Hans) 2025/01/08 00:53 (当地)
 📏 9,270 | ⏱ 57


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/uvz6i6t23tss0hijfhsmo31nygbfbmkz.jpg)

[CN-3886026](https://www.postcrossing.com/postcards/CN-3886026) 
>寄往 [tabru](https://www.postcrossing.com/user/tabru) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/12 13:02 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=49.43665~8.8088&lvl=12.0&setlang=zh-Hans) 2025/01/03 17:27 (当地)
 📏 9,165 | ⏱ 52


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/ye8o9wm4lr108xvvotkgi79nmza01b5s.jpg)

### 2024(78)

[CN-3893934](https://www.postcrossing.com/postcards/CN-3893934) 
>寄往 [gitagric](https://www.postcrossing.com/user/gitagric) 🇱🇹
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/22 13:18 (当地)
> 📥 [Lithuania](https://www.bing.com/maps/?cp=54.68916~25.2798&lvl=12.0&setlang=zh-Hans) 2024/12/31 20:01 (当地)
 📏 7,913 | ⏱ 40


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/0r30aaiso69kzh18kbaxjtl4wdw46zey.jpg)

[CN-3893935](https://www.postcrossing.com/postcards/CN-3893935) 
>寄往 [Funyee](https://www.postcrossing.com/user/Funyee) 🇹🇼
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/22 13:18 (当地)
> 📥 [Taiwan](https://www.bing.com/maps/?cp=24.80361~120.96861&lvl=12.0&setlang=zh-Hans) 2024/12/26 09:30 (当地)
 📏 729 | ⏱ 34


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/lk7mk7t9xiq234a7h8txgb4l0z71s9s2.jpg)

[CN-3820898](https://www.postcrossing.com/postcards/CN-3820898) 
>寄往 [LadyMiriam](https://www.postcrossing.com/user/LadyMiriam) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/19 14:31 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=50.77555~7.28308&lvl=12.0&setlang=zh-Hans) 2024/12/19 16:42 (当地)
 📏 9,196 | ⏱ 122


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/sjfi128au6ygdsz3ldzwwop3bxrxh1pt.jpg)

[CN-3870501](https://www.postcrossing.com/postcards/CN-3870501) 
>寄往 [karlynmeow](https://www.postcrossing.com/user/karlynmeow) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/10/23 11:31 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=36.07125~-79.56447&lvl=12.0&setlang=zh-Hans) 2024/12/15 16:50 (当地)
 📏 13,336 | ⏱ 54


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/kop2zdny1ve6zexeaehu1tq6gg7e2vsl.jpg)

[CN-3870499](https://www.postcrossing.com/postcards/CN-3870499) 
>寄往 [akiko_w](https://www.postcrossing.com/user/akiko_w) 🇯🇵
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/10/23 11:31 (当地)
> 📥 [Japan](https://www.bing.com/maps/?cp=33.85181~130.85034&lvl=12.0&setlang=zh-Hans) 2024/12/10 00:07 (当地)
 📏 2,051 | ⏱ 47


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/6kduka4ymqj9reizlcq6ep2im16tei9x.jpg)

[CN-3861177](https://www.postcrossing.com/postcards/CN-3861177) 
>寄往 [alexsnow348](https://www.postcrossing.com/user/alexsnow348) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/10/10 10:31 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=52.15077~9.95112&lvl=12.0&setlang=zh-Hans) 2024/12/03 12:36 (当地)
 📏 8,963 | ⏱ 54


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/7fv94sst8g8mhf79pr9ab0p1eaayyo1e.jpg)

[CN-3870500](https://www.postcrossing.com/postcards/CN-3870500) 
>寄往 [MAnastasia](https://www.postcrossing.com/user/MAnastasia) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/10/23 11:31 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2024/11/30 17:59 (当地)
 📏 7,123 | ⏱ 38


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/9ooi44iz1p16pvd86z0ils0poaqhgoj7.jpg)

[CN-3846151](https://www.postcrossing.com/postcards/CN-3846151) 
>寄往 [Katsiaryna1988](https://www.postcrossing.com/user/Katsiaryna1988) 🇧🇾
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/09/23 10:03 (当地)
> 📥 [Belarus](https://www.bing.com/maps/?cp=53.9~27.56667&lvl=12.0&setlang=zh-Hans) 2024/11/24 15:42 (当地)
 📏 7,786 | ⏱ 62


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/mqrvof59nmnp0kauou0dl66aay160z4c.jpg)

[CN-3842766](https://www.postcrossing.com/postcards/CN-3842766) 
>寄往 [AmandaJay](https://www.postcrossing.com/user/AmandaJay) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/09/18 10:34 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=27.33643~-82.53065&lvl=12.0&setlang=zh-Hans) 2024/11/17 17:56 (当地)
 📏 14,181 | ⏱ 61


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/sxn8gab5qfs7c668idaexxb2eyevpgyp.jpg)

[CN-3844232](https://www.postcrossing.com/postcards/CN-3844232) 
>寄往 [Myrake](https://www.postcrossing.com/user/Myrake) 🇧🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/09/20 14:18 (当地)
> 📥 [Belgium](https://www.bing.com/maps/?cp=50.77343~3.88223&lvl=12.0&setlang=zh-Hans) 2024/11/15 14:41 (当地)
 📏 9,407 | ⏱ 56


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/mai3moqz6th4hplmvmjldk07r3k6bvpm.jpg)

[CN-3844231](https://www.postcrossing.com/postcards/CN-3844231) 
>寄往 [bibka](https://www.postcrossing.com/user/bibka) 🇸🇰
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/09/20 14:18 (当地)
> 📥 [Slovakia](https://www.bing.com/maps/?cp=49.22315~18.73941&lvl=12.0&setlang=zh-Hans) 2024/11/12 12:07 (当地)
 📏 8,510 | ⏱ 53


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/0xwlil4bi4yxucfvpb28c2m92g5bmivw.jpg)

[CN-3870498](https://www.postcrossing.com/postcards/CN-3870498) 
>寄往 [angusjai](https://www.postcrossing.com/user/angusjai) 🇭🇰
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/10/23 11:31 (当地)
> 📥 [Hong Kong](https://www.bing.com/maps/?cp=22.27832~114.17469&lvl=12.0&setlang=zh-Hans) 2024/11/08 23:59 (当地)
 📏 31 | ⏱ 17


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/lgluh884rel3homhshdfolzfneq6js8t.jpg)

[CN-3828120](https://www.postcrossing.com/postcards/CN-3828120) 
>寄往 [karengigliotti](https://www.postcrossing.com/user/karengigliotti) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/29 11:10 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=33.18012~-96.49804&lvl=12.0&setlang=zh-Hans) 2024/11/02 22:24 (当地)
 📏 13,012 | ⏱ 66


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/q0fkhxt40wqjqaxnss3x238mkne71kkr.jpg)

[CN-3820899](https://www.postcrossing.com/postcards/CN-3820899) 
>寄往 [Ksyunya74](https://www.postcrossing.com/user/Ksyunya74) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/19 14:31 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=55.15402~61.42915&lvl=12.0&setlang=zh-Hans) 2024/10/29 18:12 (当地)
 📏 5,633 | ⏱ 71


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/e4550m3nmxb6uanrla2nid7at8p4tqwi.jpg)

[CN-3837376](https://www.postcrossing.com/postcards/CN-3837376) 
>寄往 [Ich_bin_Berliner](https://www.postcrossing.com/user/Ich_bin_Berliner) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/09/11 13:01 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=52.52437~13.41053&lvl=12.0&setlang=zh-Hans) 2024/10/21 09:08 (当地)
 📏 8,731 | ⏱ 40


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/mk7i71svkrd9pfi7omfez1515h928gsu.jpg)

[CN-3836542](https://www.postcrossing.com/postcards/CN-3836542) 
>寄往 [Alexandra_moon](https://www.postcrossing.com/user/Alexandra_moon) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/09/10 08:30 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2024/10/16 21:05 (当地)
 📏 7,123 | ⏱ 37


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/4c32c7v232ovs8xewidmp36kv1b2ki02.jpg)

[CN-3837234](https://www.postcrossing.com/postcards/CN-3837234) 
>寄往 [Child_of_post-rock](https://www.postcrossing.com/user/Child_of_post-rock) 🇧🇾
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/09/11 09:10 (当地)
> 📥 [Belarus](https://www.bing.com/maps/?cp=54.3167~26.854&lvl=12.0&setlang=zh-Hans) 2024/10/06 23:38 (当地)
 📏 7,822 | ⏱ 26


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/tdhx9b2lpmy05elnqlcwvc0ovaim0f7d.jpg)

[CN-3800374](https://www.postcrossing.com/postcards/CN-3800374) 
>寄往 [Limoncello4Me](https://www.postcrossing.com/user/Limoncello4Me) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/22 10:37 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=44.00766~-116.91655&lvl=12.0&setlang=zh-Hans) 2024/09/22 13:55 (当地)
 📏 10,967 | ⏱ 63


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/8pzdi92tw3f4e6f1ms7n86eg9mzg7xj3.jpg)

[CN-3800372](https://www.postcrossing.com/postcards/CN-3800372) 
>寄往 [licinnamon](https://www.postcrossing.com/user/licinnamon) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/22 10:37 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=37.77493~-122.41942&lvl=12.0&setlang=zh-Hans) 2024/09/21 16:09 (当地)
 📏 11,071 | ⏱ 62


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/6rq6s2h5x32wjwxu34tx0yu4exxjendl.jpg)

[CN-3815238](https://www.postcrossing.com/postcards/CN-3815238) 
>寄往 ***该用户已关闭*** 🇳🇱
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/12 13:02 (当地)
> 📥 [Netherlands](https://www.bing.com/maps/?cp=53.07417~6.57778&lvl=12.0&setlang=zh-Hans) 2024/09/21 14:32 (当地)
 📏 9,122 | ⏱ 40


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/al5mrguzz8ro48j6x0y5qd5s94hrold7.jpg)

[CN-3803179](https://www.postcrossing.com/postcards/CN-3803179) 
>寄往 [DetroitTigersFan](https://www.postcrossing.com/user/DetroitTigersFan) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/26 09:09 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=42.58031~-83.0302&lvl=12.0&setlang=zh-Hans) 2024/09/16 20:59 (当地)
 📏 12,558 | ⏱ 53


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/q8t8vwq4q8s60qy2qkrk0cjsu0y9iy29.jpg)

[CN-3816759](https://www.postcrossing.com/postcards/CN-3816759) 
>寄往 [trkm_el](https://www.postcrossing.com/user/trkm_el) 🇹🇼
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/14 11:05 (当地)
> 📥 [Taiwan](https://www.bing.com/maps/?cp=23.47917~120.44889&lvl=12.0&setlang=zh-Hans) 2024/09/13 18:34 (当地)
 📏 644 | ⏱ 30


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/hy9ckfb6gcenoeoo79sj4j0f07od1bix.jpg)

[CN-3802608](https://www.postcrossing.com/postcards/CN-3802608) 
>寄往 [Flicki](https://www.postcrossing.com/user/Flicki) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/25 12:21 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=51.31667~6.28333&lvl=12.0&setlang=zh-Hans) 2024/09/11 06:22 (当地)
 📏 9,230 | ⏱ 48


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/29ui1peo33e0xl8xj13php2i62m4g5fp.jpg)

[CN-3811647](https://www.postcrossing.com/postcards/CN-3811647) 
>寄往 [u-j-a](https://www.postcrossing.com/user/u-j-a) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/07 15:23 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=52.52437~13.41053&lvl=12.0&setlang=zh-Hans) 2024/09/10 20:33 (当地)
 📏 8,731 | ⏱ 34


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/eo7n5q166tkwjnal49le3b6emdv326ff.jpg)

[CN-3810147](https://www.postcrossing.com/postcards/CN-3810147) 
>寄往 [MayaCat](https://www.postcrossing.com/user/MayaCat) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/05 14:54 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=47.23627~38.9053&lvl=12.0&setlang=zh-Hans) 2024/09/09 23:10 (当地)
 📏 7,101 | ⏱ 36


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/aea95rgiwypvzntdkys7ijoo1b8qn08g.jpg)

[CN-3806043](https://www.postcrossing.com/postcards/CN-3806043) 
>寄往 [Yuting1012](https://www.postcrossing.com/user/Yuting1012) 🇹🇼
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/30 11:37 (当地)
> 📥 [Taiwan](https://www.bing.com/maps/?cp=22.67135~120.48814&lvl=12.0&setlang=zh-Hans) 2024/09/09 20:21 (当地)
 📏 641 | ⏱ 41


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/99s1ecw05jt40kfe0ww9160e6di288x9.jpg)

[CN-3800371](https://www.postcrossing.com/postcards/CN-3800371) 
>寄往 [JennySu](https://www.postcrossing.com/user/JennySu) 🇹🇼
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/22 10:37 (当地)
> 📥 [Taiwan](https://www.bing.com/maps/?cp=25.04776~121.53185&lvl=12.0&setlang=zh-Hans) 2024/08/28 20:52 (当地)
 📏 792 | ⏱ 37


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/rn8cr2mbw52mw19oclci6xuspsc51fai.jpg)

[CN-3776706](https://www.postcrossing.com/postcards/CN-3776706) 
>寄往 [brittany7227](https://www.postcrossing.com/user/brittany7227) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/20 09:59 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=41.44448~-87.63143&lvl=12.0&setlang=zh-Hans) 2024/08/18 16:52 (当地)
 📏 12,549 | ⏱ 60


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/mk80b33kaeugheur67aaxec8bh4g1147.jpg)

[CN-3786550](https://www.postcrossing.com/postcards/CN-3786550) 
>寄往 [thisisshree](https://www.postcrossing.com/user/thisisshree) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/04 10:50 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=38.80484~-77.04692&lvl=12.0&setlang=zh-Hans) 2024/08/15 15:46 (当地)
 📏 13,091 | ⏱ 43


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/n00ja0c3oks0n6lffy9m06dzhyidkf4m.jpg)

[CN-3776926](https://www.postcrossing.com/postcards/CN-3776926) 
>寄往 [katerenok](https://www.postcrossing.com/user/katerenok) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/20 16:05 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=55.78874~49.12214&lvl=12.0&setlang=zh-Hans) 2024/08/12 15:49 (当地)
 📏 6,405 | ⏱ 53


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/igu02t8hqwhmhfy6siirihm5argy3u8d.jpg)

[CN-3785191](https://www.postcrossing.com/postcards/CN-3785191) 
>寄往 [annaviola](https://www.postcrossing.com/user/annaviola) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/02 13:04 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=53.07582~8.80717&lvl=12.0&setlang=zh-Hans) 2024/08/10 13:15 (当地)
 📏 8,989 | ⏱ 39


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/fnpk84olal0jn3q69it7xfjysutmo7d1.jpg)

[CN-3780693](https://www.postcrossing.com/postcards/CN-3780693) 
>寄往 [OrianaGirl](https://www.postcrossing.com/user/OrianaGirl) 🇦🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/26 09:21 (当地)
> 📥 [Australia](https://www.bing.com/maps/?cp=-28.81354~153.2773&lvl=12.0&setlang=zh-Hans) 2024/08/07 16:55 (当地)
 📏 7,079 | ⏱ 42


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/nqlubteg3x26wnygm0jlqoa3ki63lx7i.jpg)

[CN-3800373](https://www.postcrossing.com/postcards/CN-3800373) 
>寄往 [dcktam](https://www.postcrossing.com/user/dcktam) 🇲🇴
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/22 10:37 (当地)
> 📥 [Macao](https://www.bing.com/maps/?cp=22.20056~113.54611&lvl=12.0&setlang=zh-Hans) 2024/08/05 14:52 (当地)
 📏 81 | ⏱ 14


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/h56li9r7tvdsmxu1rbjpwv7z8ztkq19d.jpg)

[CN-3772688](https://www.postcrossing.com/postcards/CN-3772688) 
>寄往 [JacobTheShuhite](https://www.postcrossing.com/user/JacobTheShuhite) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/14 17:27 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=51.0303~6.98432&lvl=12.0&setlang=zh-Hans) 2024/07/29 19:19 (当地)
 📏 9,202 | ⏱ 45


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/3144cte43ov5fne5rb4ma12cl2c8vgwf.jpg)

[CN-3774506](https://www.postcrossing.com/postcards/CN-3774506) 
>寄往 [Kosmopilot](https://www.postcrossing.com/user/Kosmopilot) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/17 07:45 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2024/07/26 00:35 (当地)
 📏 7,123 | ⏱ 39


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/5c7ikibml8fax0ovf2yse34xfc0fuk3w.jpg)

[CN-3771386](https://www.postcrossing.com/postcards/CN-3771386) 
>寄往 [ccremisii](https://www.postcrossing.com/user/ccremisii) 🇮🇹
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/12 21:50 (当地)
> 📥 [Italy](https://www.bing.com/maps/?cp=40.96801~14.25563&lvl=12.0&setlang=zh-Hans) 2024/07/23 12:03 (当地)
 📏 9,172 | ⏱ 41


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/olpt54cowozq3ixme47skuddjrxal6bt.jpg)

[CN-3770706](https://www.postcrossing.com/postcards/CN-3770706) 
>寄往 ***该用户已关闭*** 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/11 22:53 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=48.62638~9.26315&lvl=12.0&setlang=zh-Hans) 2024/07/20 15:25 (当地)
 📏 9,175 | ⏱ 39


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/9musin8jwzsydr1oj0gx3cjb7defezsh.jpg)

[CN-3771897](https://www.postcrossing.com/postcards/CN-3771897) 
>寄往 [Doreen74](https://www.postcrossing.com/user/Doreen74) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/13 16:12 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=48.08095~12.59652&lvl=12.0&setlang=zh-Hans) 2024/07/19 14:49 (当地)
 📏 8,977 | ⏱ 36


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/p14vl3slu6rqh7i44iou2pstftom1qcq.jpg)

[CN-3772289](https://www.postcrossing.com/postcards/CN-3772289) 
>寄往 [LMJillian](https://www.postcrossing.com/user/LMJillian) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/14 07:53 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=34.05223~-118.24368&lvl=12.0&setlang=zh-Hans) 2024/07/18 07:39 (当地)
 📏 11,625 | ⏱ 35


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/iv02faz6htlc1u2ve86e2i7utblfn6su.jpg)

[CN-3760818](https://www.postcrossing.com/postcards/CN-3760818) 
>寄往 [JoshC](https://www.postcrossing.com/user/JoshC) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/05/29 23:32 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=43.48035~-72.38481&lvl=12.0&setlang=zh-Hans) 2024/07/03 17:17 (当地)
 📏 12,640 | ⏱ 35


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/n2kfcxwxlcabqiey2c6i2j6v9ris66cu.jpg)

[CN-3755145](https://www.postcrossing.com/postcards/CN-3755145) 
>寄往 [vlabor](https://www.postcrossing.com/user/vlabor) 🇸🇮
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/05/21 17:42 (当地)
> 📥 [Slovenia](https://www.bing.com/maps/?cp=45.84667~13.96306&lvl=12.0&setlang=zh-Hans) 2024/07/01 14:19 (当地)
 📏 8,980 | ⏱ 41


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/jdtyvyyd55g785p0z9z2fckoali0vek3.jpg)

[CN-3747913](https://www.postcrossing.com/postcards/CN-3747913) 
>寄往 [PonchikMakoviy](https://www.postcrossing.com/user/PonchikMakoviy) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/05/11 12:31 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2024/06/24 20:36 (当地)
 📏 7,123 | ⏱ 45


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/s58b65phveo5chwo50hld2i3mwapdntn.jpg)

[CN-3747914](https://www.postcrossing.com/postcards/CN-3747914) 
>寄往 [onecleverkid](https://www.postcrossing.com/user/onecleverkid) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/05/11 12:32 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=35.19807~-111.65127&lvl=12.0&setlang=zh-Hans) 2024/06/20 01:04 (当地)
 📏 11,976 | ⏱ 40


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/0myoplr0omd58m1j6wganoesmz0q3z2q.jpg)

[CN-3730279](https://www.postcrossing.com/postcards/CN-3730279) 
>寄往 [MSFOTINAS](https://www.postcrossing.com/user/MSFOTINAS) 🇧🇾
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/15 15:55 (当地)
> 📥 [Belarus](https://www.bing.com/maps/?cp=53.9~27.56667&lvl=12.0&setlang=zh-Hans) 2024/06/16 18:42 (当地)
 📏 7,786 | ⏱ 62


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/psgzqf5s9nemqhgy1xkmjlfdx4aoqlh4.jpg)

[CN-3737191](https://www.postcrossing.com/postcards/CN-3737191) 
>寄往 [Malder](https://www.postcrossing.com/user/Malder) 🇺🇿
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/26 10:54 (当地)
> 📥 [Uzbekistan](https://www.bing.com/maps/?cp=41.26465~69.21627&lvl=12.0&setlang=zh-Hans) 2024/06/15 11:43 (当地)
 📏 4,664 | ⏱ 50


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/3qccu6zoylz41yk0c9qjq9q105j0oiqi.jpg)

[CN-3737189](https://www.postcrossing.com/postcards/CN-3737189) 
>寄往 [CasSaintDenys](https://www.postcrossing.com/user/CasSaintDenys) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/26 10:54 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=30.52297~-87.90333&lvl=12.0&setlang=zh-Hans) 2024/06/13 13:11 (当地)
 📏 13,657 | ⏱ 49


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/ylmfz1e9bfz3yjz17c8q4pcmre2xik9s.jpg)

[CN-3739257](https://www.postcrossing.com/postcards/CN-3739257) 
>寄往 [Selena](https://www.postcrossing.com/user/Selena) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/29 12:02 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=45.52345~-122.67621&lvl=12.0&setlang=zh-Hans) 2024/06/12 11:54 (当地)
 📏 10,514 | ⏱ 45


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/xsmgkq2jqnb7t01bjyzubncgnpam3bhw.jpg)

[CN-3749434](https://www.postcrossing.com/postcards/CN-3749434) 
>寄往 [Tati888](https://www.postcrossing.com/user/Tati888) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/05/13 12:17 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=53.62937~11.41316&lvl=12.0&setlang=zh-Hans) 2024/06/12 12:33 (当地)
 📏 8,806 | ⏱ 30


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/l0wuvic9onniv10v6kfygof4sx4o0o8k.jpg)

[CN-3754575](https://www.postcrossing.com/postcards/CN-3754575) 
>寄往 [DrobinGud](https://www.postcrossing.com/user/DrobinGud) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/05/20 17:55 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=55.07108~38.78399&lvl=12.0&setlang=zh-Hans) 2024/06/11 16:15 (当地)
 📏 7,052 | ⏱ 22


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/bmb82oigx6lsgpyk8zfu160t7p4snsf3.jpg)

[CN-3692797](https://www.postcrossing.com/postcards/CN-3692797) 
>寄往 [Cynt](https://www.postcrossing.com/user/Cynt) 🇨🇦
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/02/22 11:20 (当地)
> 📥 [Canada](https://www.bing.com/maps/?cp=43.25011~-79.84963&lvl=12.0&setlang=zh-Hans) 2024/06/10 13:21 (当地)
 📏 12,556 | ⏱ 110


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/5dm6vhkifj9a8nu7rpqsor27s3f0vda8.jpg)

[CN-3730278](https://www.postcrossing.com/postcards/CN-3730278) 
>寄往 [Filip](https://www.postcrossing.com/user/Filip) 🇵🇱
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/15 15:55 (当地)
> 📥 [Poland](https://www.bing.com/maps/?cp=52.2545~18.22958&lvl=12.0&setlang=zh-Hans) 2024/05/21 10:21 (当地)
 📏 8,435 | ⏱ 36


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/mp5x823kmc733mnzzfjs1gmmhmj3fb7e.jpg)

[CN-3730280](https://www.postcrossing.com/postcards/CN-3730280) 
>寄往 [Reksa](https://www.postcrossing.com/user/Reksa) 🇫🇮
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/15 15:55 (当地)
> 📥 [Finland](https://www.bing.com/maps/?cp=61.67538~21.62092&lvl=12.0&setlang=zh-Hans) 2024/05/19 22:44 (当地)
 📏 7,947 | ⏱ 34


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/7799a46pjhfbgsl5vb2nupoal58zmspb.jpg)

[CN-3723133](https://www.postcrossing.com/postcards/CN-3723133) 
>寄往 [CHIHUANCHANG](https://www.postcrossing.com/user/CHIHUANCHANG) 🇹🇼
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/04 18:22 (当地)
> 📥 [Taiwan](https://www.bing.com/maps/?cp=24.95608~121.3507&lvl=12.0&setlang=zh-Hans) 2024/05/11 16:38 (当地)
 📏 771 | ⏱ 37


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/yux7rk1t73qrpf2buyetg5sl8i4a3ik0.jpg)

[CN-3713709](https://www.postcrossing.com/postcards/CN-3713709) 
>寄往 [EGer71](https://www.postcrossing.com/user/EGer71) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/22 11:02 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2024/05/07 11:15 (当地)
 📏 7,123 | ⏱ 46


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/k8dsycjx94ucbnjkri50u4s4mpwecb39.jpg)

[CN-3713710](https://www.postcrossing.com/postcards/CN-3713710) 
>寄往 [heyheyray](https://www.postcrossing.com/user/heyheyray) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/22 11:03 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=37.77493~-122.41942&lvl=12.0&setlang=zh-Hans) 2024/04/22 21:46 (当地)
 📏 11,071 | ⏱ 32


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/76arxu1v5nb0nlkkesi1e2y07r70vcks.jpg)

[CN-3706232](https://www.postcrossing.com/postcards/CN-3706232) 
>寄往 [TimSarah](https://www.postcrossing.com/user/TimSarah) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/10 15:42 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=49.23262~7.00982&lvl=12.0&setlang=zh-Hans) 2024/04/13 14:51 (当地)
 📏 9,292 | ⏱ 34


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/2q8b91wy4k87ltnq9hzx57rckx2wa5ar.jpg)

[CN-3692799](https://www.postcrossing.com/postcards/CN-3692799) 
>寄往 [bishop95](https://www.postcrossing.com/user/bishop95) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/02/22 11:20 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=46.78327~-92.10658&lvl=12.0&setlang=zh-Hans) 2024/04/08 19:03 (当地)
 📏 11,862 | ⏱ 47


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/wiy4tsuyaxtpv2lt8q9p2abdx4x0rxkh.jpg)

[CN-3692796](https://www.postcrossing.com/postcards/CN-3692796) 
>寄往 [ana_solovyova](https://www.postcrossing.com/user/ana_solovyova) 🇯🇵
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/02/22 11:20 (当地)
> 📥 [Japan](https://www.bing.com/maps/?cp=35.43333~139.65&lvl=12.0&setlang=zh-Hans) 2024/04/03 08:32 (当地)
 📏 2,843 | ⏱ 41


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/y0pp57u0yyu4n8smvuz15xru8jcf7q8j.jpg)

[CN-3692800](https://www.postcrossing.com/postcards/CN-3692800) 
>寄往 [GermanInArabia](https://www.postcrossing.com/user/GermanInArabia) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/02/22 11:20 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=50.51545~8.38918&lvl=12.0&setlang=zh-Hans) 2024/04/01 14:46 (当地)
 📏 9,139 | ⏱ 39


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/x469la2o3it4bk0lep5okgozr2w5g82x.jpg)

[CN-3683275](https://www.postcrossing.com/postcards/CN-3683275) 
>寄往 [Cok](https://www.postcrossing.com/user/Cok) 🇳🇱
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/02/06 15:52 (当地)
> 📥 [Netherlands](https://www.bing.com/maps/?cp=51.7325~5.05278&lvl=12.0&setlang=zh-Hans) 2024/03/29 08:27 (当地)
 📏 9,284 | ⏱ 52


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/smufdl6whop9sbyyhf878giho6kx0xii.jpg)

[CN-3683277](https://www.postcrossing.com/postcards/CN-3683277) 
>寄往 [Irulka](https://www.postcrossing.com/user/Irulka) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/02/06 15:52 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=57.62987~39.87368&lvl=12.0&setlang=zh-Hans) 2024/03/18 20:28 (当地)
 📏 6,981 | ⏱ 41


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/qsooydm1ak1vt7me77amuxtzrfl445f7.jpg)

[CN-3673808](https://www.postcrossing.com/postcards/CN-3673808) 
>寄往 [Madhavan_1982](https://www.postcrossing.com/user/Madhavan_1982) 🇮🇳
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/23 16:24 (当地)
> 📥 [India](https://www.bing.com/maps/?cp=9.919~78.11953&lvl=12.0&setlang=zh-Hans) 2024/03/16 12:07 (当地)
 📏 4,089 | ⏱ 53


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/rc4pcxug0pos71skt55ofogyoqqqh7na.jpg)

[CN-3673809](https://www.postcrossing.com/postcards/CN-3673809) 
>寄往 [Pyrah](https://www.postcrossing.com/user/Pyrah) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/23 16:25 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=34.02029~-117.86534&lvl=12.0&setlang=zh-Hans) 2024/03/10 20:04 (当地)
 📏 11,653 | ⏱ 48


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/h452vt02fal6gkiknj27ubqh82i8rtm6.jpg)

[CN-3655671](https://www.postcrossing.com/postcards/CN-3655671) 
>寄往 [Daniel_and_Tanya](https://www.postcrossing.com/user/Daniel_and_Tanya) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/29 22:23 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=66.53~66.60194&lvl=12.0&setlang=zh-Hans) 2024/03/07 21:03 (当地)
 📏 5,909 | ⏱ 69


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/b7vw4a69coy80djw7elnf300djzor9es.jpg)

[CN-3692798](https://www.postcrossing.com/postcards/CN-3692798) 
>寄往 ***该用户已关闭*** 🇭🇰
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/02/22 11:20 (当地)
> 📥 [Hong Kong](https://www.bing.com/maps/?cp=22.27832~114.17469&lvl=12.0&setlang=zh-Hans) 2024/03/07 09:46 (当地)
 📏 31 | ⏱ 14


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/ep122ew11tql5sbe2qptuny0xc6je6n5.jpg)

[CN-3683276](https://www.postcrossing.com/postcards/CN-3683276) 
>寄往 [reepeecheep](https://www.postcrossing.com/user/reepeecheep) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/02/06 15:52 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=51.93855~8.87318&lvl=12.0&setlang=zh-Hans) 2024/03/06 10:59 (当地)
 📏 9,040 | ⏱ 29


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/x8mbc4zuinu9sw43ajcr441nsto0ji94.jpg)

[CN-3651287](https://www.postcrossing.com/postcards/CN-3651287) 
>寄往 [Marisolt](https://www.postcrossing.com/user/Marisolt) 🇺🇦
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/23 09:22 (当地)
> 📥 [Ukraine](https://www.bing.com/maps/?cp=50.45466~30.5238&lvl=12.0&setlang=zh-Hans) 2024/03/04 20:55 (当地)
 📏 7,659 | ⏱ 73


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/wk4vtr31f4t0cb8ahj2wesqtwahtpm0b.jpg)

[CN-3677114](https://www.postcrossing.com/postcards/CN-3677114) 
>寄往 [sktour](https://www.postcrossing.com/user/sktour) 🇯🇵
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/28 10:45 (当地)
> 📥 [Japan](https://www.bing.com/maps/?cp=35.08333~137.15&lvl=12.0&setlang=zh-Hans) 2024/02/21 21:20 (当地)
 📏 2,620 | ⏱ 24


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/ccguoytiuj04yc90o08w4jh1mmrkbbkj.jpg)

[CN-3659000](https://www.postcrossing.com/postcards/CN-3659000) 
>寄往 [BeckyS](https://www.postcrossing.com/user/BeckyS) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/03 10:20 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=47.56732~-122.63264&lvl=12.0&setlang=zh-Hans) 2024/02/10 13:16 (当地)
 📏 10,373 | ⏱ 39


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/n88czl5pibik5e7neu59988cxmb4x7kj.jpg)

[CN-3658999](https://www.postcrossing.com/postcards/CN-3658999) 
>寄往 [chacoco2](https://www.postcrossing.com/user/chacoco2) 🇫🇷
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/03 10:20 (当地)
> 📥 [France](https://www.bing.com/maps/?cp=46.58261~0.34348&lvl=12.0&setlang=zh-Hans) 2024/02/09 20:18 (当地)
 📏 9,869 | ⏱ 38


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/alc8fplc9d9x3x09szx1ximdl37wy9tq.jpg)

[CN-3660599](https://www.postcrossing.com/postcards/CN-3660599) 
>寄往 [sarmas](https://www.postcrossing.com/user/sarmas) 🇫🇮
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/05 15:19 (当地)
> 📥 [Finland](https://www.bing.com/maps/?cp=61.49911~23.78712&lvl=12.0&setlang=zh-Hans) 2024/02/07 14:16 (当地)
 📏 7,839 | ⏱ 33


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/tk5fio0qx4p35riku7ohuo92b5zoh3q5.jpg)

[CN-3660600](https://www.postcrossing.com/postcards/CN-3660600) 
>寄往 [Micha37](https://www.postcrossing.com/user/Micha37) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/05 15:19 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=53.4~9.96667&lvl=12.0&setlang=zh-Hans) 2024/02/05 18:04 (当地)
 📏 8,904 | ⏱ 31


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/aryr9eiz0yc0s3h5k5czzf3o0zjjn6sk.jpg)

[CN-3659001](https://www.postcrossing.com/postcards/CN-3659001) 
>寄往 [Topas](https://www.postcrossing.com/user/Topas) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/03 10:20 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=50.11552~8.68417&lvl=12.0&setlang=zh-Hans) 2024/02/05 11:54 (当地)
 📏 9,140 | ⏱ 33


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/oqbxrzqviv11fkgdpw3o0kuzrkw8h4vm.jpg)

[CN-3655425](https://www.postcrossing.com/postcards/CN-3655425) 
>寄往 [volker-55](https://www.postcrossing.com/user/volker-55) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/29 16:58 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=50.65278~11.98377&lvl=12.0&setlang=zh-Hans) 2024/02/02 13:48 (当地)
 📏 8,903 | ⏱ 35


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/a78wugdrvuw8d3sw0inber0258gvrb3c.jpg)

[CN-3651286](https://www.postcrossing.com/postcards/CN-3651286) 
>寄往 [NonnieL](https://www.postcrossing.com/user/NonnieL) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/23 09:22 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=37.94449~-87.40529&lvl=12.0&setlang=zh-Hans) 2024/01/25 19:09 (当地)
 📏 12,917 | ⏱ 34


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/sci47iqoeuw16b4840eqw9gkyhcu48sj.jpg)

[CN-3645301](https://www.postcrossing.com/postcards/CN-3645301) 
>寄往 [Eckhardt](https://www.postcrossing.com/user/Eckhardt) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/12 17:31 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=53.59337~9.47629&lvl=12.0&setlang=zh-Hans) 2024/01/04 15:46 (当地)
 📏 8,924 | ⏱ 23


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/4qeczvrsqivz8dpgace4co1qbrra3kg4.jpg)

[CN-3637956](https://www.postcrossing.com/postcards/CN-3637956) 
>寄往 [Zodiak](https://www.postcrossing.com/user/Zodiak) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/11/30 17:22 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=55.15402~61.42915&lvl=12.0&setlang=zh-Hans) 2024/01/03 18:29 (当地)
 📏 5,633 | ⏱ 34


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/pwmfkwvn9j09onpxhlgxz9zrscqwss18.jpg)

[CN-3624713](https://www.postcrossing.com/postcards/CN-3624713) 
>寄往 [Tonka2505](https://www.postcrossing.com/user/Tonka2505) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/11/09 22:01 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=52.49271~9.85757&lvl=12.0&setlang=zh-Hans) 2024/01/01 15:10 (当地)
 📏 8,953 | ⏱ 53


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/p08hbdt2tr9vujkev9hue5vcdv2d1yde.jpg)

### 2023(19)

[CN-3640692](https://www.postcrossing.com/postcards/CN-3640692) 
>寄往 [Matin](https://www.postcrossing.com/user/Matin) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/04 18:30 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=51.88333~8.51667&lvl=12.0&setlang=zh-Hans) 2023/12/30 15:51 (当地)
 📏 9,064 | ⏱ 26


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/46hy3aa8nvjf50qinzh36mpbb132twu5.jpg)

[CN-3641753](https://www.postcrossing.com/postcards/CN-3641753) 
>寄往 [blauweregen](https://www.postcrossing.com/user/blauweregen) 🇧🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/06 14:56 (当地)
> 📥 [Belgium](https://www.bing.com/maps/?cp=51.32254~4.94471&lvl=12.0&setlang=zh-Hans) 2023/12/29 11:35 (当地)
 📏 9,312 | ⏱ 23


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/acy5i7qaiin0x199jacwdn8spxzg6pz8.jpg)

[CN-3637489](https://www.postcrossing.com/postcards/CN-3637489) 
>寄往 [Engel76](https://www.postcrossing.com/user/Engel76) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/11/29 17:41 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=51.75912~11.35306&lvl=12.0&setlang=zh-Hans) 2023/12/28 17:39 (当地)
 📏 8,894 | ⏱ 29


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/82moz0oyr8vks6tnx6v63j34i0p8wj68.jpg)

[CN-3624711](https://www.postcrossing.com/postcards/CN-3624711) 
>寄往 [Pando4ka](https://www.postcrossing.com/user/Pando4ka) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/11/09 22:01 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2023/12/20 23:31 (当地)
 📏 7,123 | ⏱ 41


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/qq00j12z4eihspkdmyr9jjr6b0qbgdk0.jpg)

[CN-3610297](https://www.postcrossing.com/postcards/CN-3610297) 
>寄往 [adillon](https://www.postcrossing.com/user/adillon) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/17 14:55 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=42.26259~-71.80229&lvl=12.0&setlang=zh-Hans) 2023/12/19 07:29 (当地)
 📏 12,780 | ⏱ 63


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/dw9o001glnllx5dtpcxc6s2pv18r7dip.jpg)

[CN-3610302](https://www.postcrossing.com/postcards/CN-3610302) 
>寄往 [Katerina199](https://www.postcrossing.com/user/Katerina199) 🇧🇾
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/17 14:56 (当地)
> 📥 [Belarus](https://www.bing.com/maps/?cp=54.0072~27.6963&lvl=12.0&setlang=zh-Hans) 2023/12/12 12:04 (当地)
 📏 7,775 | ⏱ 56


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/nbmikzs0ubddlkp1zoqeidvqcx9c1r87.jpg)

[CN-3610299](https://www.postcrossing.com/postcards/CN-3610299) 
>寄往 [RailiH](https://www.postcrossing.com/user/RailiH) 🇫🇮
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/17 14:56 (当地)
> 📥 [Finland](https://www.bing.com/maps/?cp=60.2052~24.6522&lvl=12.0&setlang=zh-Hans) 2023/12/05 18:41 (当地)
 📏 7,822 | ⏱ 49


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/c44bk4spzg9di3z05l2tpn0bstqwphbm.jpg)

[CN-3610300](https://www.postcrossing.com/postcards/CN-3610300) 
>寄往 [josera](https://www.postcrossing.com/user/josera) 🇪🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/17 14:56 (当地)
> 📥 [Spain](https://www.bing.com/maps/?cp=37.72107~-3.97264&lvl=12.0&setlang=zh-Hans) 2023/12/02 14:36 (当地)
 📏 10,713 | ⏱ 46


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/x61xyan4pmiu4xg6apttle8izokgt15o.jpg)

[CN-3610305](https://www.postcrossing.com/postcards/CN-3610305) 
>寄往 [memom](https://www.postcrossing.com/user/memom) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/17 14:57 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=33.42227~-111.82264&lvl=12.0&setlang=zh-Hans) 2023/11/29 19:05 (当地)
 📏 12,106 | ⏱ 44


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/jbz5bqc6s4hzqsd9yohpsdnblgmdc4xz.jpg)

[CN-3610298](https://www.postcrossing.com/postcards/CN-3610298) 
>寄往 [Akaka](https://www.postcrossing.com/user/Akaka) 🇹🇼
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/17 14:56 (当地)
> 📥 [Taiwan](https://www.bing.com/maps/?cp=25.04776~121.53185&lvl=12.0&setlang=zh-Hans) 2023/11/27 13:46 (当地)
 📏 792 | ⏱ 41


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/agm365cpsijgun9rrcn7twaw2e3c48hk.jpg)

[CN-3610301](https://www.postcrossing.com/postcards/CN-3610301) 
>寄往 [mcbuchanan](https://www.postcrossing.com/user/mcbuchanan) 🇨🇦
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/17 14:56 (当地)
> 📥 [Canada](https://www.bing.com/maps/?cp=42.98339~-81.23304&lvl=12.0&setlang=zh-Hans) 2023/11/15 15:56 (当地)
 📏 12,556 | ⏱ 30


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/oohrfavt1t9r94p0rbd0i4tmdr2wj073.jpg)

[CN-3578746](https://www.postcrossing.com/postcards/CN-3578746) 
>寄往 [Silpion29](https://www.postcrossing.com/user/Silpion29) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/08/29 10:36 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=52.29778~104.29639&lvl=12.0&setlang=zh-Hans) 2023/11/15 22:14 (当地)
 📏 3,413 | ⏱ 78


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/7cgyw5d7vk088mt7ohrq9f6nyvf4177e.jpg)

[CN-3621313](https://www.postcrossing.com/postcards/CN-3621313) 
>寄往 [ChrisRe](https://www.postcrossing.com/user/ChrisRe) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/11/04 16:04 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=50.06906~8.48632&lvl=12.0&setlang=zh-Hans) 2023/11/13 23:54 (当地)
 📏 9,155 | ⏱ 10


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/i09vi7tqj1k2rvmxe9sjpyvd07xzdhjg.jpg)

[CN-3610296](https://www.postcrossing.com/postcards/CN-3610296) 
>寄往 [juergenvomdeich](https://www.postcrossing.com/user/juergenvomdeich) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/17 14:55 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=54.01667~9.0&lvl=12.0&setlang=zh-Hans) 2023/11/09 14:57 (当地)
 📏 8,932 | ⏱ 23


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/c49bj2bvagsfwve94liksgrrfwikz1hb.jpg)

[CN-3610303](https://www.postcrossing.com/postcards/CN-3610303) 
>寄往 [niku-niku](https://www.postcrossing.com/user/niku-niku) 🇯🇵
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/17 14:56 (当地)
> 📥 [Japan](https://www.bing.com/maps/?cp=34.8~134.98333&lvl=12.0&setlang=zh-Hans) 2023/11/08 15:14 (当地)
 📏 2,430 | ⏱ 22


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/1owavt13j40taanl62523g6qef9d8iwc.jpg)

[CN-3578753](https://www.postcrossing.com/postcards/CN-3578753) 
>寄往 [Masha_krb](https://www.postcrossing.com/user/Masha_krb) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/08/29 10:37 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=55.80945~37.95806&lvl=12.0&setlang=zh-Hans) 2023/10/10 19:04 (当地)
 📏 7,101 | ⏱ 43


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/yoj61d8x1s9puup4jkncrgvtsttbq6k4.jpg)

[CN-3578749](https://www.postcrossing.com/postcards/CN-3578749) 
>寄往 [shrikantkp](https://www.postcrossing.com/user/shrikantkp) 🇮🇳
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/08/29 10:36 (当地)
> 📥 [India](https://www.bing.com/maps/?cp=23.02579~72.58727&lvl=12.0&setlang=zh-Hans) 2023/10/03 20:15 (当地)
 📏 4,254 | ⏱ 36


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/bqzh2e9b8atqorxqj8k9n5trg0r9yvv2.jpg)

[CN-3578752](https://www.postcrossing.com/postcards/CN-3578752) 
>寄往 [Prairiegal](https://www.postcrossing.com/user/Prairiegal) 🇨🇦
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/08/29 10:37 (当地)
> 📥 [Canada](https://www.bing.com/maps/?cp=50.40005~-105.53445&lvl=12.0&setlang=zh-Hans) 2023/09/28 07:57 (当地)
 📏 11,010 | ⏱ 30


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/qj9bpbnv88jzskujd240srf7ojtt6atm.jpg)

[CN-3578747](https://www.postcrossing.com/postcards/CN-3578747) 
>寄往 [lyo](https://www.postcrossing.com/user/lyo) 🇯🇵
> 📤 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/08/29 10:36 (当地)
> 📥 [Japan](https://www.bing.com/maps/?cp=35.6895~139.69171&lvl=12.0&setlang=zh-Hans) 2023/09/23 09:57 (当地)
 📏 2,858 | ⏱ 25


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/do9uyzjm74nbtieowaxbposwus90lbz0.jpg)

### 2015(6)

[CN-1439411](https://www.postcrossing.com/postcards/CN-1439411) 
>寄往 [Rita8871](https://www.postcrossing.com/user/Rita8871) 🇹🇼
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/10/02 16:00 (当地)
> 📥 [Taiwan](https://www.bing.com/maps/?cp=24.87714~121.2851&lvl=12.0&setlang=zh-Hans) 2015/07/15 00:08 (当地)
 📏 1,563 | ⏱ 285


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/9c42dfa1cdfe8f091cac8826b0993467.jpg)

[CN-1509462](https://www.postcrossing.com/postcards/CN-1509462) 
>寄往 [Hannavanoost](https://www.postcrossing.com/user/Hannavanoost) 🇳🇱
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/24 17:41 (当地)
> 📥 [Netherlands](https://www.bing.com/maps/?cp=51.81~4.89444&lvl=12.0&setlang=zh-Hans) 2015/01/31 19:56 (当地)
 📏 8,175 | ⏱ 38


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/98d7720e8d9abb17388aa2ac4faa1176.jpg)

[CN-1509460](https://www.postcrossing.com/postcards/CN-1509460) 
>寄往 [lady_of_sorrows](https://www.postcrossing.com/user/lady_of_sorrows) 🇺🇦
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/24 17:40 (当地)
> 📥 [Ukraine](https://www.bing.com/maps/?cp=48.89917~33.44954&lvl=12.0&setlang=zh-Hans) 2015/01/30 16:03 (当地)
 📏 6,360 | ⏱ 37


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/943ce20ae7bd8ac518c64f0a8f964b41.jpg)

[CN-1509464](https://www.postcrossing.com/postcards/CN-1509464) 
>寄往 [Ting-Ti](https://www.postcrossing.com/user/Ting-Ti) 🇹🇼
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/24 17:41 (当地)
> 📥 [Taiwan](https://www.bing.com/maps/?cp=24.1469~120.6839&lvl=12.0&setlang=zh-Hans) 2015/01/27 21:31 (当地)
 📏 1,544 | ⏱ 34


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/2b99f06a551404ccc649291f5ebbbd27.jpg)

[CN-1480161](https://www.postcrossing.com/postcards/CN-1480161) 
>寄往 [Ziecha71](https://www.postcrossing.com/user/Ziecha71) 🇱🇻
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/11/19 14:07 (当地)
> 📥 [Latvia](https://www.bing.com/maps/?cp=56.40794~24.19443&lvl=12.0&setlang=zh-Hans) 2015/01/17 07:52 (当地)
 📏 6,825 | ⏱ 59


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/2e6fd0ad2d4fe9b12fba48320589c819.jpg)

[CN-1480155](https://www.postcrossing.com/postcards/CN-1480155) 
>寄往 [lothardornau](https://www.postcrossing.com/user/lothardornau) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/11/19 14:06 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=51.83879~6.61531&lvl=12.0&setlang=zh-Hans) 2015/01/11 02:18 (当地)
 📏 8,068 | ⏱ 53


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/65e6d916f8c2702d65e2de3874e1d4b4.jpg)

### 2014(29)

[CN-1480156](https://www.postcrossing.com/postcards/CN-1480156) 
>寄往 [banabree](https://www.postcrossing.com/user/banabree) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/11/19 14:06 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=45.21012~-123.19872&lvl=12.0&setlang=zh-Hans) 2014/12/28 01:43 (当地)
 📏 10,280 | ⏱ 39


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/00290c7eec324c425ed445f6266f8ba4.jpg)

[CN-1480158](https://www.postcrossing.com/postcards/CN-1480158) 
>寄往 [Kotarouchan](https://www.postcrossing.com/user/Kotarouchan) 🇯🇵
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/11/19 14:07 (当地)
> 📥 [Japan](https://www.bing.com/maps/?cp=35.32785~139.33735&lvl=12.0&setlang=zh-Hans) 2014/12/19 15:56 (当地)
 📏 3,128 | ⏱ 30


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/dc03f1af18ef4d10d59648891b82a8d3.jpg)

[CN-1480157](https://www.postcrossing.com/postcards/CN-1480157) 
>寄往 [Alize](https://www.postcrossing.com/user/Alize) 🇳🇱
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/11/19 14:07 (当地)
> 📥 [Netherlands](https://www.bing.com/maps/?cp=51.9325~4.83194&lvl=12.0&setlang=zh-Hans) 2014/12/17 15:33 (当地)
 📏 8,172 | ⏱ 28


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/672f2c134502ea042e3e46da73ef08bf.jpg)

[CN-1480160](https://www.postcrossing.com/postcards/CN-1480160) 
>寄往 ***该用户已关闭*** 🇸🇪
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/11/19 14:07 (当地)
> 📥 [Sweden](https://www.bing.com/maps/?cp=60.60357~15.62597&lvl=12.0&setlang=zh-Hans) 2014/12/08 21:46 (当地)
 📏 7,194 | ⏱ 20


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/62408acec9a9fcc9ce5fcd7601155658.jpg)

[CN-1410995](https://www.postcrossing.com/postcards/CN-1410995) 
>寄往 [Darinchik](https://www.postcrossing.com/user/Darinchik) 🇧🇾
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/01 16:04 (当地)
> 📥 [Belarus](https://www.bing.com/maps/?cp=54.2279~28.505&lvl=12.0&setlang=zh-Hans) 2014/10/28 17:19 (当地)
 📏 6,600 | ⏱ 57


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/488d90a923a0608f085143ad2da1c712.jpg)

[CN-1410993](https://www.postcrossing.com/postcards/CN-1410993) 
>寄往 [Monka_G](https://www.postcrossing.com/user/Monka_G) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/01 16:03 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=48.76508~11.42372&lvl=12.0&setlang=zh-Hans) 2014/10/04 11:44 (当地)
 📏 7,904 | ⏱ 33


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/84a82eca7cc181df54e65265ccb47771.jpg)

[CN-1411001](https://www.postcrossing.com/postcards/CN-1411001) 
>寄往 [pioenrosa](https://www.postcrossing.com/user/pioenrosa) 🇳🇱
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/01 16:05 (当地)
> 📥 [Netherlands](https://www.bing.com/maps/?cp=52.255~6.16389&lvl=12.0&setlang=zh-Hans) 2014/10/02 09:48 (当地)
 📏 8,075 | ⏱ 31


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/869460af40add2292917a00565e9d693.jpg)

[CN-1410996](https://www.postcrossing.com/postcards/CN-1410996) 
>寄往 [Antlynny](https://www.postcrossing.com/user/Antlynny) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/01 16:04 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=43.54997~-96.70033&lvl=12.0&setlang=zh-Hans) 2014/09/20 05:08 (当地)
 📏 11,521 | ⏱ 19


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/6d622a4a49783ff352aea9bdb49992b5.jpg)

[CN-1333455](https://www.postcrossing.com/postcards/CN-1333455) 
>寄往 [Nastya1211](https://www.postcrossing.com/user/Nastya1211) 🇧🇾
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/06/12 09:39 (当地)
> 📥 [Belarus](https://www.bing.com/maps/?cp=52.42671~31.31219&lvl=12.0&setlang=zh-Hans) 2014/08/11 13:42 (当地)
 📏 6,448 | ⏱ 60


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/59b74dddc3804178f4dfb3d6d3af1cf7.jpg)

[CN-1345019](https://www.postcrossing.com/postcards/CN-1345019) 
>寄往 [Veritas_Stern](https://www.postcrossing.com/user/Veritas_Stern) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/06/24 10:09 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=51.16158~13.4737&lvl=12.0&setlang=zh-Hans) 2014/07/31 07:57 (当地)
 📏 7,665 | ⏱ 37


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/12eb4e76d57d8e3cf67c97b6c0007aa1.jpg)

[CN-1345015](https://www.postcrossing.com/postcards/CN-1345015) 
>寄往 [lorrier](https://www.postcrossing.com/user/lorrier) 🇳🇱
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/06/24 10:08 (当地)
> 📥 [Netherlands](https://www.bing.com/maps/?cp=53.17333~6.97222&lvl=12.0&setlang=zh-Hans) 2014/07/24 10:16 (当地)
 📏 7,979 | ⏱ 30


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/5644e8d57ff6b82084231b898847ca8c.jpg)

[CN-1345017](https://www.postcrossing.com/postcards/CN-1345017) 
>寄往 [strawberry_sandra](https://www.postcrossing.com/user/strawberry_sandra) 🇸🇪
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/06/24 10:09 (当地)
> 📥 [Sweden](https://www.bing.com/maps/?cp=55.60587~13.00073&lvl=12.0&setlang=zh-Hans) 2014/07/22 20:31 (当地)
 📏 7,515 | ⏱ 29


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/fe5404fa762c45bf45a40f371e3e65aa.jpg)

[CN-1360087](https://www.postcrossing.com/postcards/CN-1360087) 
>寄往 [Kao02](https://www.postcrossing.com/user/Kao02) 🇯🇵
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/07/09 15:46 (当地)
> 📥 [Japan](https://www.bing.com/maps/?cp=37.45~138.85&lvl=12.0&setlang=zh-Hans) 2014/07/22 14:58 (当地)
 📏 3,100 | ⏱ 13


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/571d90dafdd3975ab4a4a15f56474e58.jpg)

[CN-1333612](https://www.postcrossing.com/postcards/CN-1333612) 
>寄往 [__Prenses](https://www.postcrossing.com/user/__Prenses) 🇫🇮
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/06/12 12:31 (当地)
> 📥 [Finland](https://www.bing.com/maps/?cp=63.67486~22.70256&lvl=12.0&setlang=zh-Hans) 2014/07/14 15:09 (当地)
 📏 6,761 | ⏱ 32


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/3487aa703d54998d757e77d64c01be2d.jpg)

[CN-1333452](https://www.postcrossing.com/postcards/CN-1333452) 
>寄往 [Marlene0911](https://www.postcrossing.com/user/Marlene0911) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/06/12 09:38 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=38.64123~-75.61104&lvl=12.0&setlang=zh-Hans) 2014/07/02 15:59 (当地)
 📏 12,397 | ⏱ 21


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/2ab07266398d1b503cb21df76556e0f8.jpg)

[CN-1302234](https://www.postcrossing.com/postcards/CN-1302234) 
>寄往 [Suah](https://www.postcrossing.com/user/Suah) 🇰🇷
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/09 12:44 (当地)
> 📥 [Korea (South)](https://www.bing.com/maps/?cp=37.566~126.9784&lvl=12.0&setlang=zh-Hans) 2014/06/26 15:58 (当地)
 📏 2,080 | ⏱ 48


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/f3829ccd5b5dbe98f4b143b3bfa20642.jpg)

[CN-1318206](https://www.postcrossing.com/postcards/CN-1318206) 
>寄往 [MaikeT](https://www.postcrossing.com/user/MaikeT) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/26 10:37 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=49.01513~12.10161&lvl=12.0&setlang=zh-Hans) 2014/06/14 17:34 (当地)
 📏 7,847 | ⏱ 20


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/c43e998b6020e43e7257f0ec03919370.jpg)

[CN-1318207](https://www.postcrossing.com/postcards/CN-1318207) 
>寄往 [wjfrijling](https://www.postcrossing.com/user/wjfrijling) 🇳🇱
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/26 10:38 (当地)
> 📥 [Netherlands](https://www.bing.com/maps/?cp=51.83167~4.6875&lvl=12.0&setlang=zh-Hans) 2014/06/13 18:24 (当地)
 📏 8,187 | ⏱ 19


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/f6a5fca4cedc75d9a9fa3224311b3fce.jpg)

[CN-1302233](https://www.postcrossing.com/postcards/CN-1302233) 
>寄往 [kingpeiling](https://www.postcrossing.com/user/kingpeiling) 🇹🇼
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/09 12:44 (当地)
> 📥 [Taiwan](https://www.bing.com/maps/?cp=25.13089~121.74094&lvl=12.0&setlang=zh-Hans) 2014/06/02 23:20 (当地)
 📏 1,594 | ⏱ 24


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/7ba2448ba687920f15db8667c088dc2f.jpg)

[CN-1282652](https://www.postcrossing.com/postcards/CN-1282652) 
>寄往 [Tikhelangelo](https://www.postcrossing.com/user/Tikhelangelo) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/04/18 21:25 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2014/05/22 18:43 (当地)
 📏 6,006 | ⏱ 34


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/c8aeeadb907773e90ad2b17b509604db.jpg)

[CN-1282656](https://www.postcrossing.com/postcards/CN-1282656) 
>寄往 [artlover](https://www.postcrossing.com/user/artlover) 🇫🇮
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/04/18 21:25 (当地)
> 📥 [Finland](https://www.bing.com/maps/?cp=60.46407~24.8073&lvl=12.0&setlang=zh-Hans) 2014/05/02 17:55 (当地)
 📏 6,709 | ⏱ 14


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/7c25c5df87d9ceae35563a8aa99bd6ba.jpg)

[CN-1241230](https://www.postcrossing.com/postcards/CN-1241230) 
>寄往 [iris723](https://www.postcrossing.com/user/iris723) 🇹🇼
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/03/09 22:56 (当地)
> 📥 [Taiwan](https://www.bing.com/maps/?cp=25.04776~121.53185&lvl=12.0&setlang=zh-Hans) 2014/04/23 19:34 (当地)
 📏 1,573 | ⏱ 45


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/b0988c040f09b7893f92634498c00323.jpg)

[CN-1241227](https://www.postcrossing.com/postcards/CN-1241227) 
>寄往 [Paulinka_96](https://www.postcrossing.com/user/Paulinka_96) 🇧🇾
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/03/09 22:56 (当地)
> 📥 [Belarus](https://www.bing.com/maps/?cp=53.1327~26.0139&lvl=12.0&setlang=zh-Hans) 2014/04/16 20:40 (当地)
 📏 6,784 | ⏱ 38


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/7d655e7b59272187e90070fc9e2df772.jpg)

[CN-1241224](https://www.postcrossing.com/postcards/CN-1241224) 
>寄往 [Helga_Hjodd](https://www.postcrossing.com/user/Helga_Hjodd) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/03/09 22:55 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=59.93863~30.31413&lvl=12.0&setlang=zh-Hans) 2014/04/10 21:48 (当地)
 📏 6,412 | ⏱ 32


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/f23b9b1969c6720288e24e626eaba082.jpg)

[CN-1241226](https://www.postcrossing.com/postcards/CN-1241226) 
>寄往 [reismeisje](https://www.postcrossing.com/user/reismeisje) 🇳🇱
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/03/09 22:55 (当地)
> 📥 [Netherlands](https://www.bing.com/maps/?cp=51.38667~5.44444&lvl=12.0&setlang=zh-Hans) 2014/04/04 16:33 (当地)
 📏 8,163 | ⏱ 26


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/b23f5bb79a266ae4b0a9b7fe47983a1b.jpg)

[CN-1170638](https://www.postcrossing.com/postcards/CN-1170638) 
>寄往 [saarlaender](https://www.postcrossing.com/user/saarlaender) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/12/30 16:31 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=49.46633~7.16814&lvl=12.0&setlang=zh-Hans) 2014/03/04 22:36 (当地)
 📏 8,165 | ⏱ 65


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/98d8474caf46ccd66f2752a1cc51685d.jpg)

[CN-1170641](https://www.postcrossing.com/postcards/CN-1170641) 
>寄往 [katena1000000](https://www.postcrossing.com/user/katena1000000) 🇺🇦
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/12/30 16:31 (当地)
> 📥 [Ukraine](https://www.bing.com/maps/?cp=45.83861~29.61123&lvl=12.0&setlang=zh-Hans) 2014/03/02 14:20 (当地)
 📏 6,721 | ⏱ 62


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/0da3add01dfb4e47f788478419aee3af.jpg)

[CN-1152857](https://www.postcrossing.com/postcards/CN-1152857) 
>寄往 [SpartakGirl](https://www.postcrossing.com/user/SpartakGirl) 🇷🇺
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/12/09 19:44 (当地)
> 📥 [Russia](https://www.bing.com/maps/?cp=56.49771~84.97437&lvl=12.0&setlang=zh-Hans) 2014/01/23 16:41 (当地)
 📏 3,409 | ⏱ 45


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/6e4756e769b039889c5a89cef233a167.jpg)

[CN-1152859](https://www.postcrossing.com/postcards/CN-1152859) 
>寄往 [juliaclaire](https://www.postcrossing.com/user/juliaclaire) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/12/09 19:45 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=38.58157~-121.4944&lvl=12.0&setlang=zh-Hans) 2014/01/09 14:03 (当地)
 📏 10,952 | ⏱ 31


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/199982bb7e20c17298d3c15a1dcc8051.jpg)

### 2013(7)

[CN-1152862](https://www.postcrossing.com/postcards/CN-1152862) 
>寄往 [nevena1502](https://www.postcrossing.com/user/nevena1502) 🇦🇹
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/12/09 19:45 (当地)
> 📥 [Austria](https://www.bing.com/maps/?cp=47.26266~11.39454&lvl=12.0&setlang=zh-Hans) 2013/12/28 12:13 (当地)
 📏 7,987 | ⏱ 19


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/9b5a2768220eb28163645fbe35e6b079.jpg)

[CN-1152864](https://www.postcrossing.com/postcards/CN-1152864) 
>寄往 [ANP](https://www.postcrossing.com/user/ANP) 🇫🇮
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/12/09 19:45 (当地)
> 📥 [Finland](https://www.bing.com/maps/?cp=60.99596~24.46434&lvl=12.0&setlang=zh-Hans) 2013/12/27 12:35 (当地)
 📏 6,730 | ⏱ 18


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/c709974037cd3ec3380edd88bb2e99f4.jpg)

[CN-1085556](https://www.postcrossing.com/postcards/CN-1085556) 
>寄往 [Podarenok](https://www.postcrossing.com/user/Podarenok) 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/10/01 21:44 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=52.52437~13.41053&lvl=12.0&setlang=zh-Hans) 2013/11/19 12:11 (当地)
 📏 7,630 | ⏱ 49


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/8e1d48876fd00e2ba35b5b5799899519.jpg)

[CN-1085558](https://www.postcrossing.com/postcards/CN-1085558) 
>寄往 ***该用户已关闭*** 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/10/01 21:44 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=35.68698~-105.9378&lvl=12.0&setlang=zh-Hans) 2013/10/26 08:25 (当地)
 📏 12,004 | ⏱ 25


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/a8fbd2d62f9be48980412dae572add53.jpg)

[CN-949499](https://www.postcrossing.com/postcards/CN-949499) 
>寄往 [Happybutterfly](https://www.postcrossing.com/user/Happybutterfly) 🇳🇱
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/05/18 09:40 (当地)
> 📥 [Netherlands](https://www.bing.com/maps/?cp=52.02917~5.08056&lvl=12.0&setlang=zh-Hans) 2013/07/25 17:56 (当地)
 📏 8,167 | ⏱ 69


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/7daaecb07d05b6a87efb3b4abc8139d7.jpg)

[CN-949486](https://www.postcrossing.com/postcards/CN-949486) 
>寄往 ***该用户已关闭*** 🇩🇪
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/05/18 09:23 (当地)
> 📥 [Germany](https://www.bing.com/maps/?cp=52.52437~13.41053&lvl=12.0&setlang=zh-Hans) 2013/07/24 17:26 (当地)
 📏 7,630 | ⏱ 68


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/a61f5d5fbb292f0ae2f34e8dad5af576.jpg)

[CN-949489](https://www.postcrossing.com/postcards/CN-949489) 
>寄往 [laurelr](https://www.postcrossing.com/user/laurelr) 🇺🇸
> 📤 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/05/18 09:28 (当地)
> 📥 [U.S.A.](https://www.bing.com/maps/?cp=37.38605~-122.08385&lvl=12.0&setlang=zh-Hans) 2013/07/20 14:29 (当地)
 📏 11,016 | ⏱ 64


![](https://pan.4a1801.life:11443/d/public/article/Arthur/Postcrossing_map_generator/gallery/picture/023065f841be8fc2ef00308ae793a107.jpg)