---
title: 信息汇总
icon: envelope-open-text
date: 2023-10-08
category:
  - Arthur
tag:
  - Postcrossing
order: 1
---
:::tabs 
@tab 加入时间
$registerInfo


@tab 关于我
$about
:::

[我的Postcrossing主页](https://www.postcrossing.com/user/$account)



## 一.图片墙

$title

::: tabs
@tab 发送列表

<iframe 
src="https://postcrossing.4a1801.life/output/sent.html" 
frameborder=0
height=500
width=100%
seamless=seamless
scrolling=auto
></iframe>

@tab 接收列表

<iframe 
src="https://postcrossing.4a1801.life/output/received.html" 
frameborder=0
height=500
width=100%
seamless=seamless
scrolling=auto
></iframe>

@tab 还在漂泊的明信片

<iframe 
src="https://postcrossing.4a1801.life/output/traveling.html" 
frameborder=0
height=500
width=100%
seamless=seamless
scrolling=auto
></iframe>

:::

## 二.地图展示
:::tip 地图颜色
紫色：收发均有的国家
绿色：仅有收/仅有发的国家
灰色：收发均无的国家
:::

:::tabs
@tab Map
### 个人收发Map

网址：https://postcrossing.4a1801.life/Map.html

<iframe 
src="https://postcrossing.4a1801.life/Map.html" 
frameborder=0
height=500
width=100%
seamless=seamless
scrolling=auto
></iframe>

@tab ClusterMap
### 个人收发ClusterMap

网址：https://postcrossing.4a1801.life/ClusterMap.html

<iframe 
src="https://postcrossing.4a1801.life/ClusterMap.html" 
frameborder=0
height=500
width=100%
seamless=seamless
scrolling=auto
></iframe>

@tab 网址备份
### 个人收发Map、ClusterMap (Github Page)

网址：https://arthurfsy2.github.io/Postcrossing_map_generator/Map.html
网址：https://arthurfsy2.github.io/Postcrossing_map_generator/ClusterMap.html
:::

## 三.统计

### 收发记录（年度）

:::echarts

```js
const data = await fetch(
  "https://raw.gitmirror.com/$repo/main/output/calendar.json"
).then((res) => res.json());

const date = new Date();
const year = date.getFullYear().toString().padStart(4, '0');

const option = {
  tooltip: {},
  visualMap: {
    show: false,
      min: 1,
      max: 10,
      inRange: {
        color: [ "#7bc96f", "#239a3b", "#196127", "#196127"]
      }
  },
  calendar: [
    $calendar
  ],
  series: [
    $series
  ]
};
const height = $height;

```

:::

### 收发记录（月度）

:::echarts

```js
const data = await fetch(
  "https://raw.gitmirror.com/$repo/main/output/month.json"
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

### 数据统计

:::tabs
@tab 国家分布

::: echarts

```js
const data = await fetch(
  "https://raw.gitmirror.com/$repo/main/output/stats.json"
).then((res) => res.json());

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
      data: data,
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: "rgba(0, 0, 0, 0.5)"
        }
      },
      label: {
        alignTo: 'none',
        formatter: '{name|{b}}\n{num|{d}%}',
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



@tab 各国明信片

<iframe 
src="https://postcrossing.4a1801.life/output/CountryStats.html" 
frameborder=0
height=500
width=100%
seamless=seamless
scrolling=auto
></iframe>

:::

## 四.明信片故事（$storyNum）
::: tabs
@tab 中文词云
![](https://raw.gitmirror.com/$repo/main/output/postcrossing_cn.svg)
@tab 英文词云
![](https://raw.gitmirror.com/$repo/main/output/postcrossing_en.svg)
:::

$storylist

## 五.被注册时收到的回复（$commentNum）

$commentlist

<style>
  .image-preview {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    flex-wrap: wrap;
  }

  .image-preview > img {
     box-sizing: border-box;
     width: 50% !important;
     padding: 9px;
     border-radius: 16px;
  }

  @media (max-width: 719px){
    .image-preview > img {
      width: 50% !important;
    }
  }

  @media (max-width: 419px){
    .image-preview > img {
      width: 100% !important;
    }
  }
</style>
