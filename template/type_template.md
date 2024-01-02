---
title: $title
icon: address-card
date: $date
category:
  - Arthur
tag:
  - postcrossing
order: $num
---

## [arthurfsy's $type](https://www.postcrossing.com/user/arthurfsy/gallery/$type)

### 收发记录（年度）
::: echarts 

```js
const data = await fetch(
  "https://raw.gitmirror.com/$repo/main/output/year.json"
).then((res) => res.json());

const newData = data.map(({ year, $type }) => ({ name: year, value: $type }));

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

$content
