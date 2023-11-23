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
:::info 说明
postcrossing是我在2013年就了解到的明信片交换的项目，当时玩了一段时间。现在尝试新家地址能否收到海外的明信片，目前看来家里的中英文地址都是可以收到的。
:::

## 一.图片墙

   以下展示的4个部分的内容。

//请替换明信片墙title

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
  "https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/output/calendar.json"
).then((res) => res.json());

const date = new Date();
const year = date.getFullYear().toString().padStart(4, '0');

const option = {
  tooltip: {},
  visualMap: {
    show: false,
      min: 0,
      max: 5,
      inRange: {
        color: [ '#c6e48b', '#7bc96f', '#239a3b', '#196127', '#196127']
      }
  },
  calendar: [
    {
    cellSize: ["auto", "15"],
    range: '2023',
    itemStyle: {
        color: '#ccc',
        borderWidth: 3,
        borderColor: '#fff'
      },
    splitLine: true,
    yearLabel: {
      show: true
    },
    dayLabel: {
      firstDay: 1,
    }
  },
  {
    top: 260,
    cellSize: ["auto", "15"],
    range: '2013',
    itemStyle: {
        color: '#ccc',
        borderWidth: 3,
        borderColor: '#fff'
      },
    splitLine: true,
    yearLabel: {
      show: true
    },
    dayLabel: {
      firstDay: 1,
    }
  }
  ],
  series: [
    {
    type: "heatmap",
    coordinateSystem: "calendar",
    calendarIndex: 0,
    data: data
  },
  {
    type: "heatmap",
    coordinateSystem: "calendar",
    calendarIndex: 1,
    data: data
  }
  ]
};

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

:::tabs
@tab 国家分布

::: echarts

```js
const data = await fetch(
  "https://raw.gitmirror.com/arthurfsy2/Postcrossing_map_generator/main/output/stats.json"
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

//请替换明信片表格

:::

## 四.明信片故事

//请替换明信片故事list

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
