---
title: 明信片展示墙（收到：259）
icon: address-card
date: 2026-03-04
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
  "https://raw.githubusercontent.com/arthurfsy2/Postcrossing_map_generator/main/output/year.json"
).then((res) => res.json());

const newData = data.map(({ year, received}) => ({ name: year, value: received}));

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

### 2026(18)

[DE-16306421](https://www.postcrossing.com/postcards/DE-16306421) 
>来自 [flowersfrommars](https://www.postcrossing.com/user/flowersfrommars) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=50.93032~12.01005&lvl=12.0&setlang=zh-Hans) 2026/01/29 06:57 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/03/04 09:57 (当地)
 📏 8,889 | ⏱ 34


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/peo7ulihnk2du7onhermeh6fk9209txi.jpg)

[DE-16304640](https://www.postcrossing.com/postcards/DE-16304640) 
>来自 [bstb](https://www.postcrossing.com/user/bstb) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=54.46854~9.83824&lvl=12.0&setlang=zh-Hans) 2026/01/28 15:23 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/03/04 09:53 (当地)
 📏 8,862 | ⏱ 34


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/7eprcoy8t2eonl8bfnxqtsrck5y3f182.jpg)

[FR-1867591](https://www.postcrossing.com/postcards/FR-1867591) 
>来自 [marie70](https://www.postcrossing.com/user/marie70) 🇫🇷
> 📤 [France](https://www.bing.com/maps/?cp=48.44984~6.73946&lvl=12.0&setlang=zh-Hans) 2026/01/29 07:01 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/03/04 09:48 (当地)
 📏 9,350 | ⏱ 34


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/sk03nkbgc2ji1abb4y9mhcgx9w6cz94v.jpg)

[BY-3438094](https://www.postcrossing.com/postcards/BY-3438094) 
>来自 [Karinaleshchevich](https://www.postcrossing.com/user/Karinaleshchevich) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.7817~27.4346&lvl=12.0&setlang=zh-Hans) 2026/01/29 08:58 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/03/04 09:45 (当地)
 📏 7,797 | ⏱ 34


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/3ocmyezr7idpgt66ra7sh90lwtyvotj3.jpg)

[IN-709997](https://www.postcrossing.com/postcards/IN-709997) 
>来自 [muthu](https://www.postcrossing.com/user/muthu) 🇮🇳
> 📤 [India](https://www.bing.com/maps/?cp=13.08784~80.27847&lvl=12.0&setlang=zh-Hans) 2026/01/29 12:06 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/03/04 09:37 (当地)
 📏 3,735 | ⏱ 34


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ccy26078d1tkmmc9am1v5kx6h7vx92zw.jpg)

[MY-714966](https://www.postcrossing.com/postcards/MY-714966) 
>来自 [Jayordean94](https://www.postcrossing.com/user/Jayordean94) 🇲🇾
> 📤 [Malaysia](https://www.bing.com/maps/?cp=3.1412~101.68653&lvl=12.0&setlang=zh-Hans) 2026/01/29 13:58 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/03/04 09:33 (当地)
 📏 2,547 | ⏱ 34


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/2jp8v3sqtb4ps8u1sz2wzcr2y4e24j3v.jpg)

[US-12113195](https://www.postcrossing.com/postcards/US-12113195) 
>来自 [kristinlee3](https://www.postcrossing.com/user/kristinlee3) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=42.58474~-87.82119&lvl=12.0&setlang=zh-Hans) 2026/01/28 08:24 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/03/04 09:28 (当地)
 📏 12,426 | ⏱ 34


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/jhkt3ulu1zr6rw2kha5x3v9h97gxrlcr.jpg)

[BY-3437884](https://www.postcrossing.com/postcards/BY-3437884) 
>来自 [NataKlv](https://www.postcrossing.com/user/NataKlv) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=52.6329~29.7389&lvl=12.0&setlang=zh-Hans) 2026/01/28 17:22 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/03/04 09:24 (当地)
 📏 7,670 | ⏱ 34


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/png6ffeczfl4evk3owzkpzg30cp6cmej.jpg)

[IE-283039](https://www.postcrossing.com/postcards/IE-283039) 
>来自 [sloth98](https://www.postcrossing.com/user/sloth98) 🇮🇪
> 📤 [Ireland](https://www.bing.com/maps/?cp=53.75977~-9.11719&lvl=12.0&setlang=zh-Hans) 2026/01/28 14:40 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/03/04 09:20 (当地)
 📏 9,948 | ⏱ 34


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/7i1c4q68q84sesovz7h9iv6gw5jri3yr.jpg)

[FR-1867589](https://www.postcrossing.com/postcards/FR-1867589) 
>来自 [claudiaNes](https://www.postcrossing.com/user/claudiaNes) 🇫🇷
> 📤 [France](https://www.bing.com/maps/?cp=48.80359~2.13424&lvl=12.0&setlang=zh-Hans) 2026/01/29 06:58 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/02/24 15:36 (当地)
 📏 9,626 | ⏱ 26


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/1c4mp5vt5bdveck7nzb72h5odcj5vemt.jpg)

[KR-386201](https://www.postcrossing.com/postcards/KR-386201) 
>来自 [nikolet](https://www.postcrossing.com/user/nikolet) 🇰🇷
> 📤 [Korea (South)](https://www.bing.com/maps/?cp=35.10168~129.03004&lvl=12.0&setlang=zh-Hans) 2026/01/29 14:59 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/02/24 15:30 (当地)
 📏 2,000 | ⏱ 26


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/onjuwfmx0q45wwm8rl5xn2sm0jefzgoe.jpg)

[DE-16304639](https://www.postcrossing.com/postcards/DE-16304639) 
>来自 [catjojo](https://www.postcrossing.com/user/catjojo) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.63388~13.70662&lvl=12.0&setlang=zh-Hans) 2026/01/28 15:23 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/02/24 15:03 (当地)
 📏 8,750 | ⏱ 27


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/8s9pl7wwyqfxvu428x3d9miwesxgqnc7.jpg)

[DE-16306788](https://www.postcrossing.com/postcards/DE-16306788) 
>来自 [pyroschreck](https://www.postcrossing.com/user/pyroschreck) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=53.51703~10.2488&lvl=12.0&setlang=zh-Hans) 2026/01/29 09:39 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/02/24 14:29 (当地)
 📏 8,881 | ⏱ 26


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/bg3sbe22gfcb7klrydbny6ru71clygki.jpg)

[JP-2376124](https://www.postcrossing.com/postcards/JP-2376124) 
>来自 [aliya98](https://www.postcrossing.com/user/aliya98) 🇯🇵
> 📤 [Japan](https://www.bing.com/maps/?cp=35.74893~139.71497&lvl=12.0&setlang=zh-Hans) 2026/01/29 14:58 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/02/12 12:22 (当地)
 📏 2,862 | ⏱ 14


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/8lyxz5ip8oy0zcn50e2vnc7mpvbf1vi2.jpg)

[CH-846101](https://www.postcrossing.com/postcards/CH-846101) 
>来自 [Guny](https://www.postcrossing.com/user/Guny) 🇨🇭
> 📤 [Switzerland](https://www.bing.com/maps/?cp=46.68473~7.69111&lvl=12.0&setlang=zh-Hans) 2026/01/29 06:59 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/02/12 12:19 (当地)
 📏 9,377 | ⏱ 14


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/oc6lok9dyzef9j765v4dufb34ops0jax.jpg)

[UA-2019769](https://www.postcrossing.com/postcards/UA-2019769) 
>来自 [V_N](https://www.postcrossing.com/user/V_N) 🇺🇦
> 📤 [Ukraine](https://www.bing.com/maps/?cp=50.45466~30.5238&lvl=12.0&setlang=zh-Hans) 2025/10/22 06:21 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/02/02 13:29 (当地)
 📏 7,659 | ⏱ 103


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/j2y3befyhvipmpoazfh12zse8plzzqka.jpg)

[IT-802392](https://www.postcrossing.com/postcards/IT-802392) 
>来自 [Pino246](https://www.postcrossing.com/user/Pino246) 🇮🇹
> 📤 [Italy](https://www.bing.com/maps/?cp=42.34827~14.16494&lvl=12.0&setlang=zh-Hans) 2025/04/24 20:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/01/17 23:07 (当地)
 📏 9,118 | ⏱ 268


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/03g5zwd0x4uhum9a9437a23jjycuz5zz.jpg)

[RS-104911](https://www.postcrossing.com/postcards/RS-104911) 
>来自 [drsko](https://www.postcrossing.com/user/drsko) 🇷🇸
> 📤 [Serbia](https://www.bing.com/maps/?cp=44.80401~20.46513&lvl=12.0&setlang=zh-Hans) 2025/10/08 22:48 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2026/01/13 15:14 (当地)
 📏 8,546 | ⏱ 96


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/4qtsptwvq3af5g545tgoawkmvkp522be.jpg)

### 2025(82)

[AT-832307](https://www.postcrossing.com/postcards/AT-832307) 
>来自 [TanteHuu](https://www.postcrossing.com/user/TanteHuu) 🇦🇹
> 📤 [Austria](https://www.bing.com/maps/?cp=47.06667~15.45&lvl=12.0&setlang=zh-Hans) 2025/10/19 21:58 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/12/05 09:29 (当地)
 📏 8,823 | ⏱ 46


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/wu7ygp0zes8jwp2g1t6xw2c8uq96ln3p.jpg)

[US-11847931](https://www.postcrossing.com/postcards/US-11847931) 
>来自 [Moongroovy](https://www.postcrossing.com/user/Moongroovy) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=42.43933~-123.33067&lvl=12.0&setlang=zh-Hans) 2025/10/21 20:17 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/12/01 19:15 (当地)
 📏 10,688 | ⏱ 40


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/1kdt986ci5giya5c84fmvxq60s92cbpe.jpg)

[US-11813528](https://www.postcrossing.com/postcards/US-11813528) 
>来自 [LDSN57](https://www.postcrossing.com/user/LDSN57) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=42.32652~-122.87559&lvl=12.0&setlang=zh-Hans) 2025/10/08 13:49 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/11/25 10:23 (当地)
 📏 10,725 | ⏱ 47


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/r765ul3wb5751ssszp3cy65tekndb0e9.jpg)

[DE-15911341](https://www.postcrossing.com/postcards/DE-15911341) 
>来自 [om2019](https://www.postcrossing.com/user/om2019) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.52437~13.41053&lvl=12.0&setlang=zh-Hans) 2025/10/08 22:50 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/11/25 10:10 (当地)
 📏 8,731 | ⏱ 47


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/pstouuxjsed3sppu1ezevt2q6803zkjs.jpg)

[US-11813517](https://www.postcrossing.com/postcards/US-11813517) 
>来自 [Tundra_dust](https://www.postcrossing.com/user/Tundra_dust) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=47.05606~-93.91607&lvl=12.0&setlang=zh-Hans) 2025/10/08 15:45 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/11/09 22:23 (当地)
 📏 11,775 | ⏱ 32


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/mem8b7bn6n202oe25y07c9anm72n2y3e.jpg)

[US-11813515](https://www.postcrossing.com/postcards/US-11813515) 
>来自 [HeyLittleRobby](https://www.postcrossing.com/user/HeyLittleRobby) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=41.37477~-83.65132&lvl=12.0&setlang=zh-Hans) 2025/10/08 16:44 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/11/09 22:22 (当地)
 📏 12,670 | ⏱ 32


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/hrr0mbdvk4xerg0m3cs025p10akgkain.jpg)

[DE-15928128](https://www.postcrossing.com/postcards/DE-15928128) 
>来自 [moniwo](https://www.postcrossing.com/user/moniwo) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=50.23085~7.58992&lvl=12.0&setlang=zh-Hans) 2025/10/13 18:56 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/11/09 22:21 (当地)
 📏 9,204 | ⏱ 27


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/zy87i8ikwngsb35ha0b41go7dino1j8t.jpg)

[TW-3924258](https://www.postcrossing.com/postcards/TW-3924258) 
>来自 [Milo](https://www.postcrossing.com/user/Milo) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=23.91566~120.66387&lvl=12.0&setlang=zh-Hans) 2025/10/22 12:07 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/11/09 22:20 (当地)
 📏 673 | ⏱ 18


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/f4supn8zz40axrkbxmv7pop2482zdhqd.jpg)

[MY-702063](https://www.postcrossing.com/postcards/MY-702063) 
>来自 [carolinechia](https://www.postcrossing.com/user/carolinechia) 🇲🇾
> 📤 [Malaysia](https://www.bing.com/maps/?cp=5.11922~115.93719&lvl=12.0&setlang=zh-Hans) 2025/10/22 16:09 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/11/09 21:33 (当地)
 📏 1,947 | ⏱ 18


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/um2yim9rmz1v72b6ky2gno85dxdbclt3.jpg)

[TW-3918550](https://www.postcrossing.com/postcards/TW-3918550) 
>来自 [MacArthur](https://www.postcrossing.com/user/MacArthur) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=24.80361~120.96861&lvl=12.0&setlang=zh-Hans) 2025/10/09 10:32 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/11/09 21:26 (当地)
 📏 729 | ⏱ 31


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/x37jfyds75999cz402cwga3aktq43tz7.jpg)

[SK-361016](https://www.postcrossing.com/postcards/SK-361016) 
>来自 [mkubiatko](https://www.postcrossing.com/user/mkubiatko) 🇸🇰
> 📤 [Slovakia](https://www.bing.com/maps/?cp=49.43503~18.78895&lvl=12.0&setlang=zh-Hans) 2025/10/08 22:47 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/11/04 21:16 (当地)
 📏 8,499 | ⏱ 27


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/x554jgqsin2nioqyi57e1u4c2c46suur.jpg)

[DE-15911318](https://www.postcrossing.com/postcards/DE-15911318) 
>来自 [anke1465](https://www.postcrossing.com/user/anke1465) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.05089~13.73832&lvl=12.0&setlang=zh-Hans) 2025/10/08 22:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/11/04 21:15 (当地)
 📏 8,772 | ⏱ 27


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/k7jgx0ifjlehxap2lruvqgsvtfa0g5p9.jpg)

[US-11813524](https://www.postcrossing.com/postcards/US-11813524) 
>来自 [saracoulter](https://www.postcrossing.com/user/saracoulter) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=39.82894~-84.89024&lvl=12.0&setlang=zh-Hans) 2025/10/08 16:48 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/11/04 21:13 (当地)
 📏 12,799 | ⏱ 27


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/9vs65yd1carn0szlj1h3cpcws7fvrvvg.jpg)

[US-11813520](https://www.postcrossing.com/postcards/US-11813520) 
>来自 [DixieLou](https://www.postcrossing.com/user/DixieLou) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=33.44838~-112.07404&lvl=12.0&setlang=zh-Hans) 2025/10/08 13:47 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/10/30 01:17 (当地)
 📏 12,088 | ⏱ 21


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/nkl7ya7wa6n823zea488amckm4820fjk.jpg)

[DE-15911337](https://www.postcrossing.com/postcards/DE-15911337) 
>来自 [natalja](https://www.postcrossing.com/user/natalja) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.32611~9.17015&lvl=12.0&setlang=zh-Hans) 2025/10/08 22:49 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/10/30 01:15 (当地)
 📏 9,051 | ⏱ 21


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/s3vq8o9tdz2d8rd9i3q3fnssryesngqs.jpg)

[AU-1036963](https://www.postcrossing.com/postcards/AU-1036963) 
>来自 [WattlePark](https://www.postcrossing.com/user/WattlePark) 🇦🇺
> 📤 [Australia](https://www.bing.com/maps/?cp=-37.814~144.96332&lvl=12.0&setlang=zh-Hans) 2025/10/09 07:47 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/10/30 01:13 (当地)
 📏 7,441 | ⏱ 21


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/jna2gbxkm24g49zyysi8qmjybmyjyv73.jpg)

[DE-15911339](https://www.postcrossing.com/postcards/DE-15911339) 
>来自 [CaptUebermorgen](https://www.postcrossing.com/user/CaptUebermorgen) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.52437~13.41053&lvl=12.0&setlang=zh-Hans) 2025/10/08 22:49 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/10/24 22:02 (当地)
 📏 8,731 | ⏱ 16


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ketpctb8ui8g01zzz3shbuw46s7adkor.jpg)

[TH-369455](https://www.postcrossing.com/postcards/TH-369455) 
>来自 [timetoday](https://www.postcrossing.com/user/timetoday) 🇹🇭
> 📤 [Thailand](https://www.bing.com/maps/?cp=13.75398~100.50144&lvl=12.0&setlang=zh-Hans) 2025/10/09 09:09 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/10/21 21:53 (当地)
 📏 1,748 | ⏱ 12


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/y8f2hlndxiiqdthti95skr9tfafzcc7m.jpg)

[JP-2320540](https://www.postcrossing.com/postcards/JP-2320540) 
>来自 [yukah](https://www.postcrossing.com/user/yukah) 🇯🇵
> 📤 [Japan](https://www.bing.com/maps/?cp=35.43333~139.65&lvl=12.0&setlang=zh-Hans) 2025/10/09 05:48 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/10/21 21:46 (当地)
 📏 2,843 | ⏱ 13


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/z1lussnpth7tqh8x6ukzhcneus4ftmq0.jpg)

[JP-2320820](https://www.postcrossing.com/postcards/JP-2320820) 
>来自 [hakop](https://www.postcrossing.com/user/hakop) 🇯🇵
> 📤 [Japan](https://www.bing.com/maps/?cp=35.43333~139.65&lvl=12.0&setlang=zh-Hans) 2025/10/09 18:57 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/10/21 21:45 (当地)
 📏 2,843 | ⏱ 12


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/jypj17whnopvuvholjd5wjbna9dehna7.jpg)

[NL-6019290](https://www.postcrossing.com/postcards/NL-6019290) 
>来自 [LiesenWim](https://www.postcrossing.com/user/LiesenWim) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=53.25~6.86806&lvl=12.0&setlang=zh-Hans) 2025/07/08 07:11 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/24 22:32 (当地)
 📏 9,096 | ⏱ 47


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/bmr8y9odekz7b5aqjh87tq70djbcr93f.jpg)

[PH-201724](https://www.postcrossing.com/postcards/PH-201724) 
>来自 [Janver](https://www.postcrossing.com/user/Janver) 🇵🇭
> 📤 [Philippines](https://www.bing.com/maps/?cp=14.45056~120.98278&lvl=12.0&setlang=zh-Hans) 2025/07/22 00:30 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/18 15:13 (当地)
 📏 1,148 | ⏱ 28


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/22tw4n9hdp59hqv6562k2zm9vamq1mna.jpg)

[US-11542775](https://www.postcrossing.com/postcards/US-11542775) 
>来自 [angierobinson1375](https://www.postcrossing.com/user/angierobinson1375) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=39.44534~-83.82854&lvl=12.0&setlang=zh-Hans) 2025/07/07 23:24 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/15 08:25 (当地)
 📏 12,869 | ⏱ 38


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/j5af0r0ave4wrbfkb54bdqcvg03chpaa.jpg)

[CA-1593707](https://www.postcrossing.com/postcards/CA-1593707) 
>来自 [taylorrdenison](https://www.postcrossing.com/user/taylorrdenison) 🇨🇦
> 📤 [Canada](https://www.bing.com/maps/?cp=43.25011~-79.84963&lvl=12.0&setlang=zh-Hans) 2025/07/07 23:26 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/12 10:27 (当地)
 📏 12,556 | ⏱ 35


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/2vlx8l7muwgqr8rxemqup5mr4ti5t8yo.jpg)

[DE-15657739](https://www.postcrossing.com/postcards/DE-15657739) 
>来自 [Chrisse8772](https://www.postcrossing.com/user/Chrisse8772) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=48.13743~11.57549&lvl=12.0&setlang=zh-Hans) 2025/07/22 08:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/12 10:24 (当地)
 📏 9,043 | ⏱ 21


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/p4l3mrllzmf31pu3nodnycfwdjvsy7oq.jpg)

[DE-15613085](https://www.postcrossing.com/postcards/DE-15613085) 
>来自 [kultakatriina](https://www.postcrossing.com/user/kultakatriina) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=54.0887~12.14049&lvl=12.0&setlang=zh-Hans) 2025/07/08 09:13 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/12 10:22 (当地)
 📏 8,742 | ⏱ 35


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/6x303yor5s8wqvo1s1kprhku1r9rippw.jpg)

[DE-15657706](https://www.postcrossing.com/postcards/DE-15657706) 
>来自 [Pawhuska](https://www.postcrossing.com/user/Pawhuska) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.38217~8.5823&lvl=12.0&setlang=zh-Hans) 2025/07/22 07:46 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/12 10:12 (当地)
 📏 9,183 | ⏱ 21


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/c3x6fwwxf3sdhtr1t11fjp5xrw70weq3.jpg)

[RU-10565483](https://www.postcrossing.com/postcards/RU-10565483) 
>来自 [Starshiy](https://www.postcrossing.com/user/Starshiy) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=44.89497~37.31623&lvl=12.0&setlang=zh-Hans) 2025/07/08 06:31 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/12 10:05 (当地)
 📏 7,254 | ⏱ 35


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/5u8gg24f8349gc0o2ewfco8zto1vfxzu.jpg)

[US-11542787](https://www.postcrossing.com/postcards/US-11542787) 
>来自 [bw94612](https://www.postcrossing.com/user/bw94612) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=32.22174~-110.92648&lvl=12.0&setlang=zh-Hans) 2025/07/07 20:28 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/12 09:58 (当地)
 📏 12,260 | ⏱ 35


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/pwiu1gokqjst4begqrw6002u71a76gwm.jpg)

[BY-3352451](https://www.postcrossing.com/postcards/BY-3352451) 
>来自 [Toni_Arashony](https://www.postcrossing.com/user/Toni_Arashony) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=55.1904~30.2049&lvl=12.0&setlang=zh-Hans) 2025/07/13 17:56 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/12 09:55 (当地)
 📏 7,594 | ⏱ 29


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ht2nld6nzkkq3nqhwneyaftycxgqda1m.jpg)

[LK-25643](https://www.postcrossing.com/postcards/LK-25643) 
>来自 [Portakal_kizi](https://www.postcrossing.com/user/Portakal_kizi) 🇱🇰
> 📤 [Sri Lanka](https://www.bing.com/maps/?cp=6.4394~79.9895&lvl=12.0&setlang=zh-Hans) 2025/04/25 00:08 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/04 16:08 (当地)
 📏 4,082 | ⏱ 102


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/5sqql6tyvd1yxdsa1xdokrexut8ai7x6.jpg)

[DE-15612819](https://www.postcrossing.com/postcards/DE-15612819) 
>来自 [Beckmeier](https://www.postcrossing.com/user/Beckmeier) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.37052~9.73322&lvl=12.0&setlang=zh-Hans) 2025/07/08 07:19 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/04 16:05 (当地)
 📏 8,966 | ⏱ 27


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/wxljacfgmzvyuhmqzozz33kqci5ngmrh.jpg)

[RU-10565516](https://www.postcrossing.com/postcards/RU-10565516) 
>来自 [MARINA-ALEX](https://www.postcrossing.com/user/MARINA-ALEX) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.53332~55.96253&lvl=12.0&setlang=zh-Hans) 2025/07/08 10:11 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/04 16:04 (当地)
 📏 5,978 | ⏱ 27


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/pn1zrjfpvec98q12n4ow5809ba2ywrbq.jpg)

[TW-3881180](https://www.postcrossing.com/postcards/TW-3881180) 
>来自 [pohantseng](https://www.postcrossing.com/user/pohantseng) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=24.1469~120.6839&lvl=12.0&setlang=zh-Hans) 2025/07/22 13:46 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/04 16:01 (当地)
 📏 681 | ⏱ 13


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ce2ei9hxoo15cy0i7xi9q36gdocsufkq.jpg)

[US-11542779](https://www.postcrossing.com/postcards/US-11542779) 
>来自 [kburrell](https://www.postcrossing.com/user/kburrell) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=47.57093~-122.38652&lvl=12.0&setlang=zh-Hans) 2025/07/07 20:26 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/02 09:17 (当地)
 📏 10,387 | ⏱ 25


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/zvtkjwzz8lkd9h3vi4vgas8kdwke4yji.jpg)

[US-11542796](https://www.postcrossing.com/postcards/US-11542796) 
>来自 [snow_storm_x](https://www.postcrossing.com/user/snow_storm_x) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=34.8348~-97.60253&lvl=12.0&setlang=zh-Hans) 2025/07/07 22:31 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/02 09:12 (当地)
 📏 12,802 | ⏱ 25


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/u36eusvumb7vgald9hut2ut565egitdf.jpg)

[US-11542794](https://www.postcrossing.com/postcards/US-11542794) 
>来自 [kruben](https://www.postcrossing.com/user/kruben) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=37.77493~-122.41942&lvl=12.0&setlang=zh-Hans) 2025/07/07 20:30 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/08/02 09:11 (当地)
 📏 11,071 | ⏱ 25


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/c6gubaphehmyxz5c4k9o6032dfjitiwz.jpg)

[AU-1018358](https://www.postcrossing.com/postcards/AU-1018358) 
>来自 [Telopea](https://www.postcrossing.com/user/Telopea) 🇦🇺
> 📤 [Australia](https://www.bing.com/maps/?cp=-33.65982~151.29878&lvl=12.0&setlang=zh-Hans) 2025/07/08 13:26 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/07/28 21:44 (当地)
 📏 7,380 | ⏱ 20


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/eam6s8kcjp93y1ybxh71v3b4zb1sgv5n.jpg)

[SG-456709](https://www.postcrossing.com/postcards/SG-456709) 
>来自 [Suki25](https://www.postcrossing.com/user/Suki25) 🇸🇬
> 📤 [Singapore](https://www.bing.com/maps/?cp=1.28967~103.85007&lvl=12.0&setlang=zh-Hans) 2025/07/08 11:30 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/07/24 22:02 (当地)
 📏 2,617 | ⏱ 16


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/vd4tze3im6eyssmm3gdlqzcftc99basg.jpg)

[US-11542780](https://www.postcrossing.com/postcards/US-11542780) 
>来自 [elizabethkurtz](https://www.postcrossing.com/user/elizabethkurtz) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=36.30477~-86.62&lvl=12.0&setlang=zh-Hans) 2025/07/07 22:26 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/07/24 22:00 (当地)
 📏 13,112 | ⏱ 16


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/bytkm06j3opg2mc2n27w33ls666lyayp.jpg)

[JP-2275476](https://www.postcrossing.com/postcards/JP-2275476) 
>来自 [yoich](https://www.postcrossing.com/user/yoich) 🇯🇵
> 📤 [Japan](https://www.bing.com/maps/?cp=33.6~130.41667&lvl=12.0&setlang=zh-Hans) 2025/07/08 14:11 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/07/22 20:08 (当地)
 📏 2,002 | ⏱ 14


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/1j24ta0mp6on222gtgh3mno1frfqnh0r.jpg)

[JP-2275475](https://www.postcrossing.com/postcards/JP-2275475) 
>来自 [joelc](https://www.postcrossing.com/user/joelc) 🇯🇵
> 📤 [Japan](https://www.bing.com/maps/?cp=34.69379~135.50107&lvl=12.0&setlang=zh-Hans) 2025/07/08 14:11 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/07/22 20:07 (当地)
 📏 2,467 | ⏱ 14


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/7fp1jdp09jmgrmpgzdccta7nfa0j37ms.jpg)

[IN-656658](https://www.postcrossing.com/postcards/IN-656658) 
>来自 [visweswaran](https://www.postcrossing.com/user/visweswaran) 🇮🇳
> 📤 [India](https://www.bing.com/maps/?cp=9.5096~78.09588&lvl=12.0&setlang=zh-Hans) 2025/05/04 14:43 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/07/04 21:20 (当地)
 📏 4,111 | ⏱ 61


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/udyspvaj2ovoxo0kqwbf71msgd7h1w3g.jpg)

[US-11408235](https://www.postcrossing.com/postcards/US-11408235) 
>来自 [Green_Heron](https://www.postcrossing.com/user/Green_Heron) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=44.29496~-93.26883&lvl=12.0&setlang=zh-Hans) 2025/05/18 21:13 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/07/03 08:44 (当地)
 📏 12,071 | ⏱ 45


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/fn917zf3j6kcvwq7xuo2lux35gkhuypa.jpg)

[US-11408234](https://www.postcrossing.com/postcards/US-11408234) 
>来自 [Lisaorpheus](https://www.postcrossing.com/user/Lisaorpheus) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=36.64097~-80.26561&lvl=12.0&setlang=zh-Hans) 2025/05/18 22:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/06/13 20:06 (当地)
 📏 13,258 | ⏱ 25


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/gehuulkby8q2pgkteo6d8p1o1j33ze2x.jpg)

[JP-2252270](https://www.postcrossing.com/postcards/JP-2252270) 
>来自 [azusa](https://www.postcrossing.com/user/azusa) 🇯🇵
> 📤 [Japan](https://www.bing.com/maps/?cp=35.43333~139.65&lvl=12.0&setlang=zh-Hans) 2025/05/19 11:13 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/06/13 20:03 (当地)
 📏 2,843 | ⏱ 25


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/cg95nyfc9a25bgxy541n8f71xhbu50ta.jpg)

[AU-1009099](https://www.postcrossing.com/postcards/AU-1009099) 
>来自 [leschkerj](https://www.postcrossing.com/user/leschkerj) 🇦🇺
> 📤 [Australia](https://www.bing.com/maps/?cp=-38.27448~144.48853&lvl=12.0&setlang=zh-Hans) 2025/05/19 12:13 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/06/08 13:10 (当地)
 📏 7,464 | ⏱ 20


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/115g6cybeqc2v2m6lp1l5lv4hm9p6tbf.jpg)

[UA-1997314](https://www.postcrossing.com/postcards/UA-1997314) 
>来自 [prudens_cat](https://www.postcrossing.com/user/prudens_cat) 🇺🇦
> 📤 [Ukraine](https://www.bing.com/maps/?cp=50.45466~30.5238&lvl=12.0&setlang=zh-Hans) 2025/04/24 21:37 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/06/06 09:16 (当地)
 📏 7,659 | ⏱ 42


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/7cgh6b014920dra2oazu1cz2tzvxlfsh.jpg)

[TW-3851534](https://www.postcrossing.com/postcards/TW-3851534) 
>来自 [WingFei](https://www.postcrossing.com/user/WingFei) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=25.04776~121.53185&lvl=12.0&setlang=zh-Hans) 2025/05/19 11:59 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/06/06 09:13 (当地)
 📏 792 | ⏱ 18


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/xcail4om8jpvbzs5srr66fbm03l8ubri.jpg)

[MY-682667](https://www.postcrossing.com/postcards/MY-682667) 
>来自 [iamshufen](https://www.postcrossing.com/user/iamshufen) 🇲🇾
> 📤 [Malaysia](https://www.bing.com/maps/?cp=3.1412~101.68653&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:51 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/06/06 09:12 (当地)
 📏 2,547 | ⏱ 18


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/vzbe0k43vft3w7a1jjwxuui76fopu3up.jpg)

[US-11345356](https://www.postcrossing.com/postcards/US-11345356) 
>来自 [DiannaGrindstaff](https://www.postcrossing.com/user/DiannaGrindstaff) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=44.18582~-88.46261&lvl=12.0&setlang=zh-Hans) 2025/04/25 14:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/30 16:59 (当地)
 📏 12,241 | ⏱ 35


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/bd9b1ia9uqog051itmvct54ho10u9lzn.jpg)

[DE-15398863](https://www.postcrossing.com/postcards/DE-15398863) 
>来自 [Sommerwiese](https://www.postcrossing.com/user/Sommerwiese) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.52437~13.41053&lvl=12.0&setlang=zh-Hans) 2025/04/24 20:36 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/30 16:50 (当地)
 📏 8,731 | ⏱ 36


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/te4bcqyxld9cauy9fjwcenwdeckjo8ho.jpg)

[JP-2252269](https://www.postcrossing.com/postcards/JP-2252269) 
>来自 [E-MASAKI](https://www.postcrossing.com/user/E-MASAKI) 🇯🇵
> 📤 [Japan](https://www.bing.com/maps/?cp=35.6895~139.69171&lvl=12.0&setlang=zh-Hans) 2025/05/19 11:13 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/30 16:48 (当地)
 📏 2,858 | ⏱ 11


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ahicku56gsv3c1mqbn9w74ea3bx12g2x.jpg)

[CN-4032714](https://www.postcrossing.com/postcards/CN-4032714) 
>来自 [JinjinTian](https://www.postcrossing.com/user/JinjinTian) 🇨🇳
> 📤 [China](https://www.bing.com/maps/?cp=36.06488~120.38042&lvl=12.0&setlang=zh-Hans) 2025/05/19 10:43 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/25 20:22 (当地)
 📏 1,614 | ⏱ 6


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/xyi1hps5dtj2gu05mmulyfhdvjvvw10n.jpg)

[US-11342114](https://www.postcrossing.com/postcards/US-11342114) 
>来自 [bugmanPNW](https://www.postcrossing.com/user/bugmanPNW) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=48.56177~-122.39822&lvl=12.0&setlang=zh-Hans) 2025/04/24 11:36 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/22 22:06 (当地)
 📏 10,316 | ⏱ 28


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/fmkd90bqkcou94790cv639ofakjwhfac.jpg)

[DE-15398867](https://www.postcrossing.com/postcards/DE-15398867) 
>来自 [CraftyHill](https://www.postcrossing.com/user/CraftyHill) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.32083~8.43111&lvl=12.0&setlang=zh-Hans) 2025/04/24 20:38 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/20 19:06 (当地)
 📏 9,196 | ⏱ 26


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/9fnvzfwwo4vdvpj0z556w0mgada3bnyl.jpg)

[MO-69924](https://www.postcrossing.com/postcards/MO-69924) 
>来自 [khaki_catia](https://www.postcrossing.com/user/khaki_catia) 🇲🇴
> 📤 [Macao](https://www.bing.com/maps/?cp=22.20056~113.54611&lvl=12.0&setlang=zh-Hans) 2025/04/26 15:52 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/20 19:02 (当地)
 📏 81 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/dohcjhkyayh1nmm6x5ele4k8c015iwgf.jpg)

[US-11342115](https://www.postcrossing.com/postcards/US-11342115) 
>来自 [Jim0819](https://www.postcrossing.com/user/Jim0819) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=35.31762~-82.59429&lvl=12.0&setlang=zh-Hans) 2025/04/24 14:36 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 09:20 (当地)
 📏 13,339 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/9vbucxnkwsewvmzjp8cqjnuxkv9kfk5u.jpg)

[LU-121426](https://www.postcrossing.com/postcards/LU-121426) 
>来自 [nikolenkooo](https://www.postcrossing.com/user/nikolenkooo) 🇱🇺
> 📤 [Luxembourg](https://www.bing.com/maps/?cp=49.61167~6.13&lvl=12.0&setlang=zh-Hans) 2025/04/24 20:38 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 09:19 (当地)
 📏 9,329 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/bjv4af02zdh7knaw228glm3062y1c8yw.jpg)

[US-11342120](https://www.postcrossing.com/postcards/US-11342120) 
>来自 [tacogal729](https://www.postcrossing.com/user/tacogal729) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=40.68729~-80.27145&lvl=12.0&setlang=zh-Hans) 2025/04/24 14:38 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 09:19 (当地)
 📏 12,824 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/zes6752yz1z6i13mi2q5s7vwxt4wvogl.jpg)

[DE-15398868](https://www.postcrossing.com/postcards/DE-15398868) 
>来自 [ghostspider](https://www.postcrossing.com/user/ghostspider) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.22172~6.77616&lvl=12.0&setlang=zh-Hans) 2025/04/24 20:38 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/19 09:18 (当地)
 📏 9,205 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/uzjznheze45absnihosv6c62qep1ql0b.jpg)

[FR-1798160](https://www.postcrossing.com/postcards/FR-1798160) 
>来自 ***该用户已关闭*** 🇫🇷
> 📤 [France](https://www.bing.com/maps/?cp=45.4177~-0.59466&lvl=12.0&setlang=zh-Hans) 2025/04/24 20:38 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/12 10:44 (当地)
 📏 10,000 | ⏱ 17


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/knrxt3dxf9ure8u5gqllaya3qihbsz8c.jpg)

[DE-15398865](https://www.postcrossing.com/postcards/DE-15398865) 
>来自 [phasin](https://www.postcrossing.com/user/phasin) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.56014~13.0927&lvl=12.0&setlang=zh-Hans) 2025/04/24 20:37 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/12 10:38 (当地)
 📏 8,749 | ⏱ 17


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/g3n63snpw8vegk5oyo7llnejv346naxz.jpg)

[NL-5733716](https://www.postcrossing.com/postcards/NL-5733716) 
>来自 [Arbor](https://www.postcrossing.com/user/Arbor) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=53.20213~6.11183&lvl=12.0&setlang=zh-Hans) 2024/05/07 10:18 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/05/05 14:21 (当地)
 📏 9,143 | ⏱ 363


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/z6nq8z240j5v5eb0aq4sy6rw7vop6e73.jpg)

[BE-940863](https://www.postcrossing.com/postcards/BE-940863) 
>来自 [loops](https://www.postcrossing.com/user/loops) 🇧🇪
> 📤 [Belgium](https://www.bing.com/maps/?cp=50.80154~4.41436&lvl=12.0&setlang=zh-Hans) 2025/01/18 09:19 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/24 10:34 (当地)
 📏 9,373 | ⏱ 65


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/b0699nw0symvjc9v3df9ytyxs7cwrunv.jpg)

[TW-3675643](https://www.postcrossing.com/postcards/TW-3675643) 
>来自 [tn058359](https://www.postcrossing.com/user/tn058359) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=22.99083~120.21333&lvl=12.0&setlang=zh-Hans) 2024/05/07 16:18 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/24 09:21 (当地)
 📏 614 | ⏱ 321


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/272bfb6b2lzb5m9n5gxptbvzrl72r0y9.jpg)

[CA-1548364](https://www.postcrossing.com/postcards/CA-1548364) 
>来自 [Sc123456](https://www.postcrossing.com/user/Sc123456) 🇨🇦
> 📤 [Canada](https://www.bing.com/maps/?cp=49.8844~-97.14704&lvl=12.0&setlang=zh-Hans) 2025/02/02 11:14 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/10 23:48 (当地)
 📏 11,385 | ⏱ 36


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/bxaje6mohsqchjtsyod5l370fidkkk4g.jpg)

[US-11115566](https://www.postcrossing.com/postcards/US-11115566) 
>来自 [DosRobles](https://www.postcrossing.com/user/DosRobles) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=32.71571~-117.16472&lvl=12.0&setlang=zh-Hans) 2025/02/02 09:35 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/03 21:32 (当地)
 📏 11,798 | ⏱ 29


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/1f4tycx1tz4goc6foztx7n2j2ntqhs70.jpg)

[UA-1985093](https://www.postcrossing.com/postcards/UA-1985093) 
>来自 [morpheu_12](https://www.postcrossing.com/user/morpheu_12) 🇺🇦
> 📤 [Ukraine](https://www.bing.com/maps/?cp=50.45466~30.5238&lvl=12.0&setlang=zh-Hans) 2025/01/18 10:19 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/03/03 21:30 (当地)
 📏 7,659 | ⏱ 44


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/mgkzhrp8nm3mc8gwpn5lru6kevggu1pj.jpg)

[LV-433935](https://www.postcrossing.com/postcards/LV-433935) 
>来自 [Semlina](https://www.postcrossing.com/user/Semlina) 🇱🇻
> 📤 [Latvia](https://www.bing.com/maps/?cp=57.39485~21.56121&lvl=12.0&setlang=zh-Hans) 2025/01/18 10:21 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/23 16:25 (当地)
 📏 8,066 | ⏱ 36


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/pfr65bl6yr8dicezg5a13dc3t3zx12cu.jpg)

[DE-15094232](https://www.postcrossing.com/postcards/DE-15094232) 
>来自 [blnbear](https://www.postcrossing.com/user/blnbear) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.97397~8.82816&lvl=12.0&setlang=zh-Hans) 2025/01/18 09:21 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/23 16:20 (当地)
 📏 9,138 | ⏱ 36


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/6b641d5h6nztzw27w1jgt6zsxstjar5s.jpg)

[RU-10398212](https://www.postcrossing.com/postcards/RU-10398212) 
>来自 [Sunnydream](https://www.postcrossing.com/user/Sunnydream) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.42419~37.55472&lvl=12.0&setlang=zh-Hans) 2025/01/18 11:19 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/23 16:17 (当地)
 📏 7,128 | ⏱ 36


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/de66jh5td5si4g68ymrgagf680ppvwhz.jpg)

[DE-15094228](https://www.postcrossing.com/postcards/DE-15094228) 
>来自 [SimiWeidi](https://www.postcrossing.com/user/SimiWeidi) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.34669~7.24343&lvl=12.0&setlang=zh-Hans) 2025/01/18 09:21 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/23 16:13 (当地)
 📏 9,170 | ⏱ 36


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/5jxd0lw2yfx5z8lt2arkkhyxareodt0k.jpg)

[BY-3270850](https://www.postcrossing.com/postcards/BY-3270850) 
>来自 [Chasodeyka](https://www.postcrossing.com/user/Chasodeyka) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.9~27.56667&lvl=12.0&setlang=zh-Hans) 2025/01/18 12:05 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/21 00:18 (当地)
 📏 7,786 | ⏱ 33


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/7bsepfdi28q4an1dax7c4ifia3e03u2c.jpg)

[CZ-2181877](https://www.postcrossing.com/postcards/CZ-2181877) 
>来自 [Ladikka](https://www.postcrossing.com/user/Ladikka) 🇨🇿
> 📤 [Czechia](https://www.bing.com/maps/?cp=50.08804~14.42076&lvl=12.0&setlang=zh-Hans) 2025/01/19 16:22 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/21 00:05 (当地)
 📏 8,768 | ⏱ 32


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/4e6wr1cxzebqxaph51twp7ny8orfp915.jpg)

[DE-15094225](https://www.postcrossing.com/postcards/DE-15094225) 
>来自 [Lutzkrannich](https://www.postcrossing.com/user/Lutzkrannich) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=50.9787~11.03283&lvl=12.0&setlang=zh-Hans) 2025/01/18 09:19 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/21 00:00 (当地)
 📏 8,949 | ⏱ 33


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/dtvytmp5saychi0c8vj9bbldaf5ro2md.jpg)

[DE-15094224](https://www.postcrossing.com/postcards/DE-15094224) 
>来自 [luciusmetellus](https://www.postcrossing.com/user/luciusmetellus) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=53.56414~13.27532&lvl=12.0&setlang=zh-Hans) 2025/01/18 09:18 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/20 23:53 (当地)
 📏 8,696 | ⏱ 33


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/q9unx5fl0dkq22rm0z6xvgfip2ue33r8.jpg)

[DE-15094223](https://www.postcrossing.com/postcards/DE-15094223) 
>来自 [siegfried48](https://www.postcrossing.com/user/siegfried48) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=50.8357~12.92922&lvl=12.0&setlang=zh-Hans) 2025/01/18 09:17 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/10 20:17 (当地)
 📏 8,834 | ⏱ 23


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/3qsmcg90rqpc2305271i7rs4fwash8bi.jpg)

[DE-15094234](https://www.postcrossing.com/postcards/DE-15094234) 
>来自 [eule75](https://www.postcrossing.com/user/eule75) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=53.4~9.96667&lvl=12.0&setlang=zh-Hans) 2025/01/18 09:21 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/10 19:51 (当地)
 📏 8,904 | ⏱ 23


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/d60evvcn3juucjpcw5jwe739px3eps96.jpg)

[US-11073689](https://www.postcrossing.com/postcards/US-11073689) 
>来自 [marora](https://www.postcrossing.com/user/marora) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=32.71571~-117.16472&lvl=12.0&setlang=zh-Hans) 2025/01/18 00:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/10 19:49 (当地)
 📏 11,798 | ⏱ 23


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/gpykzgidkgxwde3lezduqrbkxov2i3ay.jpg)

[BE-940862](https://www.postcrossing.com/postcards/BE-940862) 
>来自 [LowerDecksPOBox](https://www.postcrossing.com/user/LowerDecksPOBox) 🇧🇪
> 📤 [Belgium](https://www.bing.com/maps/?cp=50.85045~4.34878&lvl=12.0&setlang=zh-Hans) 2025/01/18 09:19 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/09 14:19 (当地)
 📏 9,374 | ⏱ 22


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/b7mh0t7dp7807vyobmrnykltmmbbynuw.jpg)

[BY-3194098](https://www.postcrossing.com/postcards/BY-3194098) 
>来自 [Famickiy](https://www.postcrossing.com/user/Famickiy) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.1561~24.4513&lvl=12.0&setlang=zh-Hans) 2024/08/19 09:35 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2025/02/09 14:15 (当地)
 📏 8,005 | ⏱ 174


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/bl98vyt4uczsrvq56k7smw99bh0o5rko.jpg)

### 2024(90)

[DE-14827045](https://www.postcrossing.com/postcards/DE-14827045) 
>来自 [Emily_Gertrud](https://www.postcrossing.com/user/Emily_Gertrud) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=48.00674~10.59666&lvl=12.0&setlang=zh-Hans) 2024/11/12 12:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/12/22 22:23 (当地)
 📏 9,116 | ⏱ 40


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/hqpxdouxtcaix3da1o45bxa1m25ewaev.jpg)

[US-10929032](https://www.postcrossing.com/postcards/US-10929032) 
>来自 [Soyprincesa2](https://www.postcrossing.com/user/Soyprincesa2) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=36.19886~-115.1175&lvl=12.0&setlang=zh-Hans) 2024/11/21 21:19 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/12/22 22:13 (当地)
 📏 11,675 | ⏱ 30


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/xt3k1cmmkrh74qppqliftvuekxceinvk.jpg)

[FI-4708463](https://www.postcrossing.com/postcards/FI-4708463) 
>来自 [minglesluvr](https://www.postcrossing.com/user/minglesluvr) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=60.45148~22.26869&lvl=12.0&setlang=zh-Hans) 2024/11/02 12:29 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/12/22 21:54 (当地)
 📏 7,944 | ⏱ 50


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/tc714ihpfkl6vysqbww1b5ckdv9g326g.jpg)

[FI-4719313](https://www.postcrossing.com/postcards/FI-4719313) 
>来自 [paulancrossing1suomi](https://www.postcrossing.com/user/paulancrossing1suomi) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=62.3~27.13333&lvl=12.0&setlang=zh-Hans) 2024/11/22 09:45 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/12/14 13:48 (当地)
 📏 7,651 | ⏱ 22


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/tgmli14et9ysxov401l9tbpbpu73vct1.jpg)

[DE-14747625](https://www.postcrossing.com/postcards/DE-14747625) 
>来自 [Mysticfleur](https://www.postcrossing.com/user/Mysticfleur) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=50.87197~9.70891&lvl=12.0&setlang=zh-Hans) 2024/10/21 09:10 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/12/11 21:16 (当地)
 📏 9,038 | ⏱ 51


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/6qlppbt3na7z0ye7rhkma6od3yuzo23t.jpg)

[RU-10292585](https://www.postcrossing.com/postcards/RU-10292585) 
>来自 [Natalka72](https://www.postcrossing.com/user/Natalka72) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=58.19148~60.65492&lvl=12.0&setlang=zh-Hans) 2024/10/21 12:08 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/12/11 21:14 (当地)
 📏 5,787 | ⏱ 51


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/t5qgc8csd026uly2sestqlg53ygf8kbj.jpg)

[DE-14747622](https://www.postcrossing.com/postcards/DE-14747622) 
>来自 [Arhel](https://www.postcrossing.com/user/Arhel) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=53.55073~9.99302&lvl=12.0&setlang=zh-Hans) 2024/10/21 09:10 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/12/05 20:28 (当地)
 📏 8,895 | ⏱ 45


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/d7tod5dfkbhb1z6ckz3m88pm93rsnk1q.jpg)

[RU-10295172](https://www.postcrossing.com/postcards/RU-10295172) 
>来自 [gav23](https://www.postcrossing.com/user/gav23) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.91979~36.86876&lvl=12.0&setlang=zh-Hans) 2024/10/23 10:13 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/12/02 09:28 (当地)
 📏 7,169 | ⏱ 40


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/9avan79d8gkdztep9tv18pzixrj6tedi.jpg)

[LU-115905](https://www.postcrossing.com/postcards/LU-115905) 
>来自 [Delol](https://www.postcrossing.com/user/Delol) 🇱🇺
> 📤 [Luxembourg](https://www.bing.com/maps/?cp=49.78733~6.0654&lvl=12.0&setlang=zh-Hans) 2024/10/21 09:09 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/29 09:34 (当地)
 📏 9,324 | ⏱ 39


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/5j1ameev3u71sr0otvv4pg0gf5rrkip5.jpg)

[AT-759553](https://www.postcrossing.com/postcards/AT-759553) 
>来自 [JuKarin888](https://www.postcrossing.com/user/JuKarin888) 🇦🇹
> 📤 [Austria](https://www.bing.com/maps/?cp=48.20849~16.37208&lvl=12.0&setlang=zh-Hans) 2024/10/21 09:08 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/29 09:16 (当地)
 📏 8,712 | ⏱ 39


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/o1gh6kicp67jybaadf8xu4vp9cfw8hqe.jpg)

[US-10877429](https://www.postcrossing.com/postcards/US-10877429) 
>来自 [notmychelle](https://www.postcrossing.com/user/notmychelle) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=47.30732~-122.22845&lvl=12.0&setlang=zh-Hans) 2024/11/02 22:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/25 18:53 (当地)
 📏 10,415 | ⏱ 22


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/gh5d3zducgythkpqs5b3u6nrmsvzc1hr.jpg)

[CN-3893939](https://www.postcrossing.com/postcards/CN-3893939) 
>来自 [Luna_Trusova](https://www.postcrossing.com/user/Luna_Trusova) 🇨🇳
> 📤 [China](https://www.bing.com/maps/?cp=24.47979~118.08187&lvl=12.0&setlang=zh-Hans) 2024/11/22 13:24 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/25 18:50 (当地)
 📏 446 | ⏱ 3


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/nlmqr9hclpnqh0r5jjlor56j0fk1p1x4.jpg)

[US-10847283](https://www.postcrossing.com/postcards/US-10847283) 
>来自 [Cardiffgal](https://www.postcrossing.com/user/Cardiffgal) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=34.05223~-118.24368&lvl=12.0&setlang=zh-Hans) 2024/10/22 20:37 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/22 21:26 (当地)
 📏 11,625 | ⏱ 30


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/v5zbhzeu1ww8qsar96o1ury0w33kp7kt.jpg)

[US-10847318](https://www.postcrossing.com/postcards/US-10847318) 
>来自 [TrvlnMatt](https://www.postcrossing.com/user/TrvlnMatt) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=33.30616~-111.84125&lvl=12.0&setlang=zh-Hans) 2024/10/22 20:53 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/22 21:21 (当地)
 📏 12,114 | ⏱ 30


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/k7425q6uvokixuajbekut62fztreqdxb.jpg)

[RU-10292586](https://www.postcrossing.com/postcards/RU-10292586) 
>来自 [Trushina_N](https://www.postcrossing.com/user/Trushina_N) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=51.67204~39.1843&lvl=12.0&setlang=zh-Hans) 2024/10/21 10:09 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/20 21:27 (当地)
 📏 7,043 | ⏱ 30


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/hqlmkxd9x1tx9jxwtbrrzismst3vra9n.jpg)

[US-10842005](https://www.postcrossing.com/postcards/US-10842005) 
>来自 ***该用户已关闭*** 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=43.57664~-91.2243&lvl=12.0&setlang=zh-Hans) 2024/10/21 02:11 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/14 19:53 (当地)
 📏 12,214 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ohahknsgfsthmrhygnd6weedi5hly9q0.jpg)

[DE-14747621](https://www.postcrossing.com/postcards/DE-14747621) 
>来自 [LittleWordThrower82](https://www.postcrossing.com/user/LittleWordThrower82) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=48.78232~9.17702&lvl=12.0&setlang=zh-Hans) 2024/10/21 09:09 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/12 11:17 (当地)
 📏 9,173 | ⏱ 22


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/7m3bei9pty0st5psmveifawd1kn6ltdk.jpg)

[DE-14754578](https://www.postcrossing.com/postcards/DE-14754578) 
>来自 [Giegsegaggse](https://www.postcrossing.com/user/Giegsegaggse) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.33962~12.37129&lvl=12.0&setlang=zh-Hans) 2024/10/23 05:34 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/12 11:15 (当地)
 📏 8,848 | ⏱ 20


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ksps44zkil5uqt3l23cwlvz6abb1ochj.jpg)

[JP-2152688](https://www.postcrossing.com/postcards/JP-2152688) 
>来自 [gurima](https://www.postcrossing.com/user/gurima) 🇯🇵
> 📤 [Japan](https://www.bing.com/maps/?cp=34.68505~135.80485&lvl=12.0&setlang=zh-Hans) 2024/10/23 12:32 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/05 20:13 (当地)
 📏 2,491 | ⏱ 13


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/nz30ufrvx9hwj1cecsmtpzgio4xtzbmw.jpg)

[HK-881204](https://www.postcrossing.com/postcards/HK-881204) 
>来自 [popopyaya](https://www.postcrossing.com/user/popopyaya) 🇭🇰
> 📤 [Hong Kong](https://www.bing.com/maps/?cp=22.27832~114.17469&lvl=12.0&setlang=zh-Hans) 2024/10/21 15:08 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/11/05 20:09 (当地)
 📏 31 | ⏱ 15


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/7qyapacl7egikxkwpfsmcavhrg8kbiv8.jpg)

[BA-14379](https://www.postcrossing.com/postcards/BA-14379) 
>来自 [Oara](https://www.postcrossing.com/user/Oara) 🇧🇦
> 📤 [Bosnia-Herzegovina](https://www.bing.com/maps/?cp=43.84864~18.35644&lvl=12.0&setlang=zh-Hans) 2024/06/20 10:10 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/10/11 18:44 (当地)
 📏 8,740 | ⏱ 113


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/vf7n495616r3oie9uad7lx4lurt4pkut.jpg)

[US-10593683](https://www.postcrossing.com/postcards/US-10593683) 
>来自 [tklbridget](https://www.postcrossing.com/user/tklbridget) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=32.55376~-83.88741&lvl=12.0&setlang=zh-Hans) 2024/07/25 01:43 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/10/04 02:15 (当地)
 📏 13,591 | ⏱ 71


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/vurz7x69m5bq6x9xienho65cu247baul.jpg)

[US-10662757](https://www.postcrossing.com/postcards/US-10662757) 
>来自 [ewerannette](https://www.postcrossing.com/user/ewerannette) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=29.42412~-98.49363&lvl=12.0&setlang=zh-Hans) 2024/08/18 21:07 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/09/20 00:27 (当地)
 📏 13,256 | ⏱ 32


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/r6o57kxi2rixawis8i3bh0ni34hmh7yt.jpg)

[RU-10208779](https://www.postcrossing.com/postcards/RU-10208779) 
>来自 [red_crocodile](https://www.postcrossing.com/user/red_crocodile) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2024/08/11 23:46 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/09/17 12:36 (当地)
 📏 7,123 | ⏱ 36


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/f5tbp1yjsd1sct3b9bhy1rvdbwi2ia84.jpg)

[ID-431633](https://www.postcrossing.com/postcards/ID-431633) 
>来自 [Ireneind](https://www.postcrossing.com/user/Ireneind) 🇮🇩
> 📤 [Indonesia](https://www.bing.com/maps/?cp=-7.9797~112.6304&lvl=12.0&setlang=zh-Hans) 2024/08/11 20:34 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/09/10 20:09 (当地)
 📏 3,400 | ⏱ 30


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/u5qy7segc8dkcwxpzwuei3d7nmf1yb38.jpg)

[ES-808083](https://www.postcrossing.com/postcards/ES-808083) 
>来自 [JaimeBilbao](https://www.postcrossing.com/user/JaimeBilbao) 🇪🇸
> 📤 [Spain](https://www.bing.com/maps/?cp=43.32842~-3.03248&lvl=12.0&setlang=zh-Hans) 2024/08/16 09:04 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/09/09 08:36 (当地)
 📏 10,291 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/vbvw7ps7vuvk5v2aml5kida50780se7x.jpg)

[SE-237946](https://www.postcrossing.com/postcards/SE-237946) 
>来自 [trobbe](https://www.postcrossing.com/user/trobbe) 🇸🇪
> 📤 [Sweden](https://www.bing.com/maps/?cp=59.32938~18.06871&lvl=12.0&setlang=zh-Hans) 2024/06/12 20:54 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/30 19:44 (当地)
 📏 8,203 | ⏱ 79


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/2v3uny82sejlnmuc28w7o0e9mbmxoj9a.jpg)

[DE-14501760](https://www.postcrossing.com/postcards/DE-14501760) 
>来自 [DocSchuette](https://www.postcrossing.com/user/DocSchuette) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.05~9.9&lvl=12.0&setlang=zh-Hans) 2024/08/12 07:39 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/30 19:41 (当地)
 📏 8,971 | ⏱ 18


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/10sjvwrhqmf3gd3clq6j86l8ouyb42hy.jpg)

[DE-14440000](https://www.postcrossing.com/postcards/DE-14440000) 
>来自 [CharlottePia](https://www.postcrossing.com/user/CharlottePia) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=48.17904~11.2547&lvl=12.0&setlang=zh-Hans) 2024/07/25 08:30 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/30 19:38 (当地)
 📏 9,063 | ⏱ 36


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/s5iybwjeqidtneve60sl2nin6uudi6jh.jpg)

[DE-14475272](https://www.postcrossing.com/postcards/DE-14475272) 
>来自 [hepman](https://www.postcrossing.com/user/hepman) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.25627~7.14816&lvl=12.0&setlang=zh-Hans) 2024/08/04 15:54 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/26 21:12 (当地)
 📏 9,180 | ⏱ 22


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/1n71xzvde89i9kkft2oviwndykp5199a.jpg)

[US-10623806](https://www.postcrossing.com/postcards/US-10623806) 
>来自 [tomphila](https://www.postcrossing.com/user/tomphila) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=47.65966~-117.42908&lvl=12.0&setlang=zh-Hans) 2024/08/05 03:32 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/22 08:50 (当地)
 📏 10,659 | ⏱ 17


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ffvljrr9ogvz7biorhrhp2we5cz8yr1i.jpg)

[DE-14443316](https://www.postcrossing.com/postcards/DE-14443316) 
>来自 [Patrick_H_F](https://www.postcrossing.com/user/Patrick_H_F) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.00937~8.40444&lvl=12.0&setlang=zh-Hans) 2024/07/26 08:34 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/19 22:38 (当地)
 📏 9,213 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/n5rowcbn8a0ts1wqv4trghcnpymuc1vn.jpg)

[RU-10168180](https://www.postcrossing.com/postcards/RU-10168180) 
>来自 [Alluring](https://www.postcrossing.com/user/Alluring) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2024/07/07 14:07 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/19 22:35 (当地)
 📏 7,123 | ⏱ 43


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/33qrc5019x5k3z24eq50w529uefc1nxf.jpg)

[US-10584951](https://www.postcrossing.com/postcards/US-10584951) 
>来自 [schamplin](https://www.postcrossing.com/user/schamplin) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=42.35843~-71.05977&lvl=12.0&setlang=zh-Hans) 2024/07/21 22:37 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/16 23:28 (当地)
 📏 12,776 | ⏱ 26


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/y54d4but101zwg3lnr8u119oic14y1rp.jpg)

[FI-4654970](https://www.postcrossing.com/postcards/FI-4654970) 
>来自 [Jussi](https://www.postcrossing.com/user/Jussi) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=60.16952~24.93545&lvl=12.0&setlang=zh-Hans) 2024/07/29 11:50 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/16 23:27 (当地)
 📏 7,807 | ⏱ 18


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/8tty35ec75j6y12o4iyfsvbw3zvh2uma.jpg)

[US-10529701](https://www.postcrossing.com/postcards/US-10529701) 
>来自 [chandlerguera](https://www.postcrossing.com/user/chandlerguera) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=35.23338~-106.66447&lvl=12.0&setlang=zh-Hans) 2024/07/01 23:06 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/13 12:27 (当地)
 📏 12,277 | ⏱ 42


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/itcuy4hgnc2n2fi6xanuozfrymmafik7.jpg)

[LT-945721](https://www.postcrossing.com/postcards/LT-945721) 
>来自 [Deite](https://www.postcrossing.com/user/Deite) 🇱🇹
> 📤 [Lithuania](https://www.bing.com/maps/?cp=54.68916~25.2798&lvl=12.0&setlang=zh-Hans) 2024/06/24 20:37 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/13 12:09 (当地)
 📏 7,913 | ⏱ 49


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/3ixzyfy1g318fi98e8g4rol3tn602rxq.jpg)

[US-10584950](https://www.postcrossing.com/postcards/US-10584950) 
>来自 [vnusbaum](https://www.postcrossing.com/user/vnusbaum) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=41.67533~-85.7061&lvl=12.0&setlang=zh-Hans) 2024/07/21 22:37 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/13 12:04 (当地)
 📏 12,582 | ⏱ 22


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/6ys988cg2gt476f9vemiev7dt0udamye.jpg)

[DE-14374200](https://www.postcrossing.com/postcards/DE-14374200) 
>来自 [Boryslawa](https://www.postcrossing.com/user/Boryslawa) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.25627~7.14816&lvl=12.0&setlang=zh-Hans) 2024/07/06 10:19 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/12 10:08 (当地)
 📏 9,180 | ⏱ 37


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/x0jw17jquhxrzxrwfibfor76nwceo766.jpg)

[FI-4642929](https://www.postcrossing.com/postcards/FI-4642929) 
>来自 [ajoutsenlampi](https://www.postcrossing.com/user/ajoutsenlampi) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=60.98267~25.66151&lvl=12.0&setlang=zh-Hans) 2024/07/06 11:19 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/05 00:08 (当地)
 📏 7,752 | ⏱ 29


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/n6xqvqvrnwshxc1kadkl3ias2sfbeku4.jpg)

[FI-4642961](https://www.postcrossing.com/postcards/FI-4642961) 
>来自 [Minna71](https://www.postcrossing.com/user/Minna71) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=62.43333~22.18333&lvl=12.0&setlang=zh-Hans) 2024/07/06 11:45 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/08/05 00:06 (当地)
 📏 7,900 | ⏱ 29


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/v4p2idipjs7u2tuiamlxpl31wsskudpn.jpg)

[FI-4640895](https://www.postcrossing.com/postcards/FI-4640895) 
>来自 [AnnekaA](https://www.postcrossing.com/user/AnnekaA) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=64.08333~24.55&lvl=12.0&setlang=zh-Hans) 2024/07/02 08:06 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/27 22:03 (当地)
 📏 7,747 | ⏱ 25


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/w4vjnki6x182vvjrgksit9hk5v4168pq.jpg)

[DE-14306905](https://www.postcrossing.com/postcards/DE-14306905) 
>来自 [RunnIng_cat_mum](https://www.postcrossing.com/user/RunnIng_cat_mum) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.96667~8.66667&lvl=12.0&setlang=zh-Hans) 2024/06/15 09:57 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/18 20:20 (当地)
 📏 9,003 | ⏱ 33


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/szl9ero35ku96vxsm53k01vworzh583l.jpg)

[AT-729735](https://www.postcrossing.com/postcards/AT-729735) 
>来自 [fliederling](https://www.postcrossing.com/user/fliederling) 🇦🇹
> 📤 [Austria](https://www.bing.com/maps/?cp=47.52183~16.19419&lvl=12.0&setlang=zh-Hans) 2024/05/07 10:18 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/12 19:06 (当地)
 📏 8,752 | ⏱ 66


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/7rcqfsrglq1ffhfyv0lzi3y08j9cpq2l.jpg)

[IE-259244](https://www.postcrossing.com/postcards/IE-259244) 
>来自 [nopecat](https://www.postcrossing.com/user/nopecat) 🇮🇪
> 📤 [Ireland](https://www.bing.com/maps/?cp=53.45972~-6.21806&lvl=12.0&setlang=zh-Hans) 2024/06/16 16:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/12 19:04 (当地)
 📏 9,819 | ⏱ 26


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/xi5hlo2lz3k166xgj1uom0i29tr3nw95.jpg)

[US-10478110](https://www.postcrossing.com/postcards/US-10478110) 
>来自 [mfeda](https://www.postcrossing.com/user/mfeda) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=32.54487~-94.36742&lvl=12.0&setlang=zh-Hans) 2024/06/12 13:59 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/02 20:25 (当地)
 📏 13,175 | ⏱ 20


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/9mbz0n00w2t3x8s9vszvdyqxxnr90x8q.jpg)

[FI-4633650](https://www.postcrossing.com/postcards/FI-4633650) 
>来自 [veverka](https://www.postcrossing.com/user/veverka) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=60.86667~26.7&lvl=12.0&setlang=zh-Hans) 2024/06/17 08:45 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/07/02 20:22 (当地)
 📏 7,699 | ⏱ 15


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/4ttbpxkkr9v2qr10jxkkaj3wqof97sdz.jpg)

[US-10415575](https://www.postcrossing.com/postcards/US-10415575) 
>来自 [vidhyasanjeev](https://www.postcrossing.com/user/vidhyasanjeev) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=33.38067~-84.79966&lvl=12.0&setlang=zh-Hans) 2024/05/20 06:02 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/22 23:40 (当地)
 📏 13,475 | ⏱ 33


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/r8xuixklzgp307whw1xmdw6br0q58d57.jpg)

[US-10443866](https://www.postcrossing.com/postcards/US-10443866) 
>来自 [clbrown](https://www.postcrossing.com/user/clbrown) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=40.8~-96.66696&lvl=12.0&setlang=zh-Hans) 2024/05/30 15:40 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/20 21:25 (当地)
 📏 12,279 | ⏱ 21


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/plwc1h1m210eygspwym2pulw98cjtnly.jpg)

[US-10397099](https://www.postcrossing.com/postcards/US-10397099) 
>来自 [Parker51](https://www.postcrossing.com/user/Parker51) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=40.71427~-74.00597&lvl=12.0&setlang=zh-Hans) 2024/05/13 00:23 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/20 21:25 (当地)
 📏 12,927 | ⏱ 38


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/gpik6mxu6eb18rl45q62itb78j0g0m91.jpg)

[RU-10097926](https://www.postcrossing.com/postcards/RU-10097926) 
>来自 [mint-pluto](https://www.postcrossing.com/user/mint-pluto) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=52.29778~104.29639&lvl=12.0&setlang=zh-Hans) 2024/05/07 16:19 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/16 22:57 (当地)
 📏 3,413 | ⏱ 40


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/gapjrcmytxzo33lke19vb5fqm85f7s6t.jpg)

[DE-14183085](https://www.postcrossing.com/postcards/DE-14183085) 
>来自 [marie5](https://www.postcrossing.com/user/marie5) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=54.30911~13.0818&lvl=12.0&setlang=zh-Hans) 2024/05/07 10:25 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/13 20:35 (当地)
 📏 8,676 | ⏱ 37


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/squbx8q082796z9wmv1m62hswwex6qj0.jpg)

[DE-14228192](https://www.postcrossing.com/postcards/DE-14228192) 
>来自 [Rainbow211](https://www.postcrossing.com/user/Rainbow211) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.9624~9.24719&lvl=12.0&setlang=zh-Hans) 2024/05/20 18:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/13 20:34 (当地)
 📏 9,112 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/hq5v2fihlqr6b65f23y0pavuv5utr6co.jpg)

[DE-14197980](https://www.postcrossing.com/postcards/DE-14197980) 
>来自 [Martin-Gittig](https://www.postcrossing.com/user/Martin-Gittig) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.23367~12.71959&lvl=12.0&setlang=zh-Hans) 2024/05/11 06:35 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/11 20:32 (当地)
 📏 8,830 | ⏱ 31


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/nm9ik99hsn29l2s47v1brnsvzvks30um.jpg)

[DE-14183067](https://www.postcrossing.com/postcards/DE-14183067) 
>来自 [sollex](https://www.postcrossing.com/user/sollex) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.41997~10.3633&lvl=12.0&setlang=zh-Hans) 2024/05/07 10:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/05 23:32 (当地)
 📏 8,971 | ⏱ 29


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/yyy7seek9v9xrtlbrmz3ohaivb3kr9ek.jpg)

[US-10392528](https://www.postcrossing.com/postcards/US-10392528) 
>来自 [DemianLV](https://www.postcrossing.com/user/DemianLV) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=36.0397~-114.98194&lvl=12.0&setlang=zh-Hans) 2024/05/10 22:49 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/03 23:27 (当地)
 📏 11,696 | ⏱ 23


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/jftiw2d8ar5tfj2azgsxumfck1s9f4yg.jpg)

[NL-5735018](https://www.postcrossing.com/postcards/NL-5735018) 
>来自 [Willempie2](https://www.postcrossing.com/user/Willempie2) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=52.46167~5.99861&lvl=12.0&setlang=zh-Hans) 2024/05/09 10:50 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/01 23:02 (当地)
 📏 9,188 | ⏱ 23


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/txy0slkdu6tm7vsuoomc071uy5fbzqnb.jpg)

[GB-1757199](https://www.postcrossing.com/postcards/GB-1757199) 
>来自 [LauraLou](https://www.postcrossing.com/user/LauraLou) 🇬🇧
> 📤 [U.K.](https://www.bing.com/maps/?cp=53.64904~-1.78416&lvl=12.0&setlang=zh-Hans) 2024/05/07 09:18 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/06/01 23:00 (当地)
 📏 9,568 | ⏱ 25


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/i3afjwafueaqs8n3n7x3hcinm1x910er.jpg)

[HR-108981](https://www.postcrossing.com/postcards/HR-108981) 
>来自 [jilli1002](https://www.postcrossing.com/user/jilli1002) 🇭🇷
> 📤 [Croatia](https://www.bing.com/maps/?cp=44.11578~15.22514&lvl=12.0&setlang=zh-Hans) 2024/05/07 10:17 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/05/27 22:39 (当地)
 📏 8,962 | ⏱ 20


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/3muyxpwujwl5gulj3uua81zu92gp1gki.jpg)

[AT-729734](https://www.postcrossing.com/postcards/AT-729734) 
>来自 [Zwiebel123](https://www.postcrossing.com/user/Zwiebel123) 🇦🇹
> 📤 [Austria](https://www.bing.com/maps/?cp=47.26266~11.39454&lvl=12.0&setlang=zh-Hans) 2024/05/07 10:18 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/05/24 23:12 (当地)
 📏 9,096 | ⏱ 17


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/qtgrtx9dizw0ykp1fo2tscsbq6q8dwu8.jpg)

[JP-2075151](https://www.postcrossing.com/postcards/JP-2075151) 
>来自 [dream3225](https://www.postcrossing.com/user/dream3225) 🇯🇵
> 📤 [Japan](https://www.bing.com/maps/?cp=35.08333~137.15&lvl=12.0&setlang=zh-Hans) 2024/05/07 17:16 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/05/21 20:41 (当地)
 📏 2,620 | ⏱ 14


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/xdyyhnwy7o5hdlqsyhwy34v4miryawnt.jpg)

[RU-9991674](https://www.postcrossing.com/postcards/RU-9991674) 
>来自 [Ledon2015](https://www.postcrossing.com/user/Ledon2015) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2024/02/09 22:21 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/23 19:35 (当地)
 📏 7,123 | ⏱ 74


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/78k8s94ftzz9wttc6fq78790o5g6uk3y.jpg)

[RU-9991671](https://www.postcrossing.com/postcards/RU-9991671) 
>来自 [jul_nov](https://www.postcrossing.com/user/jul_nov) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2024/02/09 22:18 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/18 18:54 (当地)
 📏 7,123 | ⏱ 69


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/8kmo9qjxz6kvunt5vit5kbnvmnoaf7ue.jpg)

[US-10240079](https://www.postcrossing.com/postcards/US-10240079) 
>来自 [waydowneast](https://www.postcrossing.com/user/waydowneast) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=44.02163~-92.4699&lvl=12.0&setlang=zh-Hans) 2024/03/16 15:16 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/06 12:27 (当地)
 📏 12,127 | ⏱ 20


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/c6j8qns0fwqmo1bi5zinj0rjk87oyxsa.jpg)

[DE-14019750](https://www.postcrossing.com/postcards/DE-14019750) 
>来自 [Havanna](https://www.postcrossing.com/user/Havanna) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.47593~10.98856&lvl=12.0&setlang=zh-Hans) 2024/03/16 07:37 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/06 12:12 (当地)
 📏 9,021 | ⏱ 21


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/sm03ogvybqys253tqskqm7aov92o34t8.jpg)

[MY-634790](https://www.postcrossing.com/postcards/MY-634790) 
>来自 [SerHuy](https://www.postcrossing.com/user/SerHuy) 🇲🇾
> 📤 [Malaysia](https://www.bing.com/maps/?cp=3.21~101.561&lvl=12.0&setlang=zh-Hans) 2024/03/16 14:38 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/04/06 12:01 (当地)
 📏 2,548 | ⏱ 21


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/cb7ft4eyjurh3ncp22d5ktsw3oox5el6.jpg)

[US-10173050](https://www.postcrossing.com/postcards/US-10173050) 
>来自 [blairwortham20](https://www.postcrossing.com/user/blairwortham20) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=42.91259~-71.1245&lvl=12.0&setlang=zh-Hans) 2024/02/21 22:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/22 19:04 (当地)
 📏 12,714 | ⏱ 29


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/m4x243q6e3xzwsprdsl8vs3scp8ai50t.jpg)

[TW-3636606](https://www.postcrossing.com/postcards/TW-3636606) 
>来自 [SophieAD](https://www.postcrossing.com/user/SophieAD) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=25.04776~121.53185&lvl=12.0&setlang=zh-Hans) 2024/02/22 12:04 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/18 20:26 (当地)
 📏 792 | ⏱ 25


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/z0fgmt19upgwg6p7vg576mbuvfeg8xf5.jpg)

[DE-13722055](https://www.postcrossing.com/postcards/DE-13722055) 
>来自 [Lara1992](https://www.postcrossing.com/user/Lara1992) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=48.78232~9.17702&lvl=12.0&setlang=zh-Hans) 2023/12/19 13:30 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/18 10:50 (当地)
 📏 9,173 | ⏱ 90


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/g9vtk8lteshvn5sgzzqb8n5hccaalw7v.jpg)

[DE-13953758](https://www.postcrossing.com/postcards/DE-13953758) 
>来自 [kjk87](https://www.postcrossing.com/user/kjk87) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.80557~8.60307&lvl=12.0&setlang=zh-Hans) 2024/02/25 13:25 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/18 10:40 (当地)
 📏 9,161 | ⏱ 22


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/8cbmr2589ihn93jhz7t99vlds9xjp5fz.jpg)

[US-10173049](https://www.postcrossing.com/postcards/US-10173049) 
>来自 [Morningofthesun](https://www.postcrossing.com/user/Morningofthesun) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=26.96201~-82.3526&lvl=12.0&setlang=zh-Hans) 2024/02/21 22:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/18 10:37 (当地)
 📏 14,226 | ⏱ 25


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/70d4m0tgu32c1f1c7gku2siy1tckduqt.jpg)

[CA-1436021](https://www.postcrossing.com/postcards/CA-1436021) 
>来自 [kittenwsharpclaws](https://www.postcrossing.com/user/kittenwsharpclaws) 🇨🇦
> 📤 [Canada](https://www.bing.com/maps/?cp=43.70011~-79.4163&lvl=12.0&setlang=zh-Hans) 2024/02/09 14:21 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/18 10:30 (当地)
 📏 12,516 | ⏱ 37


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/3fv8lw8qch3npecpsa4h7w65da93kv2n.jpg)

[FI-4563418](https://www.postcrossing.com/postcards/FI-4563418) 
>来自 [Emmietta](https://www.postcrossing.com/user/Emmietta) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=61.49911~23.78712&lvl=12.0&setlang=zh-Hans) 2024/02/09 21:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/18 10:20 (当地)
 📏 7,839 | ⏱ 37


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/o6mpesh50v8xttziy01yeirahmhv1krj.jpg)

[FI-4563419](https://www.postcrossing.com/postcards/FI-4563419) 
>来自 [mieite](https://www.postcrossing.com/user/mieite) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=60.98267~25.66151&lvl=12.0&setlang=zh-Hans) 2024/02/09 21:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/10 13:56 (当地)
 📏 7,752 | ⏱ 29


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/07hkdu7lxdtil6jtc54jsyn5q0e1yl80.jpg)

[DE-13904674](https://www.postcrossing.com/postcards/DE-13904674) 
>来自 [Thumla](https://www.postcrossing.com/user/Thumla) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.67502~7.94983&lvl=12.0&setlang=zh-Hans) 2024/02/10 17:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/10 13:53 (当地)
 📏 9,060 | ⏱ 29


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/7cp1tsfnfvwk7ry1x3kkoubtno86y8b0.jpg)

[US-10143953](https://www.postcrossing.com/postcards/US-10143953) 
>来自 [mbgris](https://www.postcrossing.com/user/mbgris) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=42.45843~-71.06616&lvl=12.0&setlang=zh-Hans) 2024/02/11 16:59 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/04 23:13 (当地)
 📏 12,764 | ⏱ 22


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/w82ajeefdvnxtn4huxus9igicuccxkwd.jpg)

[DE-13942438](https://www.postcrossing.com/postcards/DE-13942438) 
>来自 [Stiflers-Mom](https://www.postcrossing.com/user/Stiflers-Mom) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.06556~8.80306&lvl=12.0&setlang=zh-Hans) 2024/02/22 08:11 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/04 22:54 (当地)
 📏 9,184 | ⏱ 11


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ngxabnqi7ztlwpdqhywyq65oonsad12s.jpg)

[US-10137660](https://www.postcrossing.com/postcards/US-10137660) 
>来自 [trish13](https://www.postcrossing.com/user/trish13) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=38.58157~-121.4944&lvl=12.0&setlang=zh-Hans) 2024/02/09 11:22 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/04 22:52 (当地)
 📏 11,078 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/kmkr5nwo95vce912l7qls8wspoz4rj3k.jpg)

[NL-5673465](https://www.postcrossing.com/postcards/NL-5673465) 
>来自 [Femkuhhhh](https://www.postcrossing.com/user/Femkuhhhh) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=53.20139~5.80859&lvl=12.0&setlang=zh-Hans) 2024/02/09 20:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/03/04 22:51 (当地)
 📏 9,161 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/i59brbowdhb1zgjzlhuqcvl1bpsu9ugr.jpg)

[GB-1729911](https://www.postcrossing.com/postcards/GB-1729911) 
>来自 [PattyG](https://www.postcrossing.com/user/PattyG) 🇬🇧
> 📤 [U.K.](https://www.bing.com/maps/?cp=53.48771~-2.29042&lvl=12.0&setlang=zh-Hans) 2024/02/09 19:18 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/02/29 13:45 (当地)
 📏 9,606 | ⏱ 19


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/utmcwgbonrd64cpzezf72j8sahy7egqh.jpg)

[NL-5673466](https://www.postcrossing.com/postcards/NL-5673466) 
>来自 [Anski1979](https://www.postcrossing.com/user/Anski1979) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=52.1275~4.44861&lvl=12.0&setlang=zh-Hans) 2024/02/09 20:20 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/02/27 19:55 (当地)
 📏 9,299 | ⏱ 18


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ix9sfvo9d2yc0erfxg7wtd0d4u8iionc.jpg)

[DE-13743074](https://www.postcrossing.com/postcards/DE-13743074) 
>来自 [siobhan](https://www.postcrossing.com/user/siobhan) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.0303~6.98432&lvl=12.0&setlang=zh-Hans) 2023/12/25 20:56 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/31 20:16 (当地)
 📏 9,202 | ⏱ 37


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/v3wxlv2ez5u3hwa67ba06osu5x6kq3ym.jpg)

[US-9960301](https://www.postcrossing.com/postcards/US-9960301) 
>来自 [Nicole1313](https://www.postcrossing.com/user/Nicole1313) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=35.43532~-101.17294&lvl=12.0&setlang=zh-Hans) 2023/12/05 10:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/26 23:12 (当地)
 📏 12,565 | ⏱ 52


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/8v3ov8tmzqztv8mcrrrxy0x0sxlwlwq3.jpg)

[IN-569670](https://www.postcrossing.com/postcards/IN-569670) 
>来自 [ashokarox](https://www.postcrossing.com/user/ashokarox) 🇮🇳
> 📤 [India](https://www.bing.com/maps/?cp=14.22262~76.40038&lvl=12.0&setlang=zh-Hans) 2024/01/01 19:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/26 23:08 (当地)
 📏 4,086 | ⏱ 25


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/io1w6erf6ty0da60efye6k0xppjo22rt.jpg)

[DE-13755664](https://www.postcrossing.com/postcards/DE-13755664) 
>来自 [Akasha78](https://www.postcrossing.com/user/Akasha78) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=48.80537~9.52721&lvl=12.0&setlang=zh-Hans) 2023/12/29 09:58 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/26 23:07 (当地)
 📏 9,149 | ⏱ 28


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/uu8q81luyj40ilslp5kli03m890t618b.jpg)

[PL-1969946](https://www.postcrossing.com/postcards/PL-1969946) 
>来自 [RobertoK](https://www.postcrossing.com/user/RobertoK) 🇵🇱
> 📤 [Poland](https://www.bing.com/maps/?cp=49.98738~20.06473&lvl=12.0&setlang=zh-Hans) 2023/12/05 17:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/14 16:12 (当地)
 📏 8,393 | ⏱ 40


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/wd450wovwocll0euien8tfkm2y713he1.jpg)

[RU-9911412](https://www.postcrossing.com/postcards/RU-9911412) 
>来自 [MariBrown](https://www.postcrossing.com/user/MariBrown) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=56.8519~60.6122&lvl=12.0&setlang=zh-Hans) 2023/12/05 21:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/04 18:46 (当地)
 📏 5,741 | ⏱ 30


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/oy3wlx1zzhd0dzl0ahcfteg4zxhem003.jpg)

[DE-13722056](https://www.postcrossing.com/postcards/DE-13722056) 
>来自 [Nordbaer](https://www.postcrossing.com/user/Nordbaer) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.22172~6.77616&lvl=12.0&setlang=zh-Hans) 2023/12/19 13:30 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/02 13:08 (当地)
 📏 9,205 | ⏱ 14


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/exft376nr2jfvn5k98lgex28ym6di6yq.jpg)

[GB-1710416](https://www.postcrossing.com/postcards/GB-1710416) 
>来自 [gordonf](https://www.postcrossing.com/user/gordonf) 🇬🇧
> 📤 [U.K.](https://www.bing.com/maps/?cp=54.42302~-6.44434&lvl=12.0&setlang=zh-Hans) 2023/12/05 16:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/02 13:07 (当地)
 📏 9,766 | ⏱ 28


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/odxhm6bwc8gpouuj6t5nt3hrsdy3npwm.jpg)

[NL-5633161](https://www.postcrossing.com/postcards/NL-5633161) 
>来自 [read-addict](https://www.postcrossing.com/user/read-addict) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=52.26167~4.49306&lvl=12.0&setlang=zh-Hans) 2023/12/12 10:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2024/01/02 13:05 (当地)
 📏 9,289 | ⏱ 21


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/py0eb56dlh1fs9yj4dsi6h5gty9upog4.jpg)

### 2023(22)

[FI-4527706](https://www.postcrossing.com/postcards/FI-4527706) 
>来自 [Salladeemus](https://www.postcrossing.com/user/Salladeemus) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=64.22728~27.72846&lvl=12.0&setlang=zh-Hans) 2023/12/05 18:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/31 18:17 (当地)
 📏 7,593 | ⏱ 26


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/3e4hr6a3so631dpg9nb8n568vz0vgdul.jpg)

[CA-1412998](https://www.postcrossing.com/postcards/CA-1412998) 
>来自 [yuliavolosevych](https://www.postcrossing.com/user/yuliavolosevych) 🇨🇦
> 📤 [Canada](https://www.bing.com/maps/?cp=45.50884~-73.58781&lvl=12.0&setlang=zh-Hans) 2023/12/05 11:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/29 21:09 (当地)
 📏 12,404 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/87xk4heemaugky0k4ekus8hs5m6g8k5r.jpg)

[RU-9911406](https://www.postcrossing.com/postcards/RU-9911406) 
>来自 [Reymas](https://www.postcrossing.com/user/Reymas) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2023/12/05 19:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/29 21:06 (当地)
 📏 7,123 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/eqylfu3vj74g38w0a6258ya0spo2ohh9.jpg)

[BY-3083966](https://www.postcrossing.com/postcards/BY-3083966) 
>来自 [gallinka](https://www.postcrossing.com/user/gallinka) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=52.4345~30.9754&lvl=12.0&setlang=zh-Hans) 2023/12/05 19:41 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/29 21:05 (当地)
 📏 7,591 | ⏱ 24


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ue5f37htbbdaeriqqkse6fvn8imnfyt1.jpg)

[RU-9847210](https://www.postcrossing.com/postcards/RU-9847210) 
>来自 [Di_Purple](https://www.postcrossing.com/user/Di_Purple) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=44.89497~37.31623&lvl=12.0&setlang=zh-Hans) 2023/10/17 09:56 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/29 21:00 (当地)
 📏 7,254 | ⏱ 73


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ecsxuv0c10jn33u29cdrn7dk90cwtmh4.jpg)

[NL-5628599](https://www.postcrossing.com/postcards/NL-5628599) 
>来自 [hippoos](https://www.postcrossing.com/user/hippoos) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=51.87167~4.07083&lvl=12.0&setlang=zh-Hans) 2023/12/06 08:17 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/26 19:18 (当地)
 📏 9,335 | ⏱ 20


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/h8mhntqyo4432gvgbyz5ia883s1sr9sz.jpg)

[HK-846298](https://www.postcrossing.com/postcards/HK-846298) 
>来自 [jojo2023](https://www.postcrossing.com/user/jojo2023) 🇭🇰
> 📤 [Hong Kong](https://www.bing.com/maps/?cp=22.39175~113.97157&lvl=12.0&setlang=zh-Hans) 2023/12/06 00:42 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/12/21 14:15 (当地)
 📏 32 | ⏱ 16


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/fjddvjjax3f1mgnr4slc328duxqr96wl.jpg)

[LT-913966](https://www.postcrossing.com/postcards/LT-913966) 
>来自 [valras](https://www.postcrossing.com/user/valras) 🇱🇹
> 📤 [Lithuania](https://www.bing.com/maps/?cp=54.64364~25.05162&lvl=12.0&setlang=zh-Hans) 2023/10/17 09:57 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/11/30 13:00 (当地)
 📏 7,928 | ⏱ 44


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/dfsgfv5r49yok2quiwxlxh25edsrjl37.jpg)

[RU-9830214](https://www.postcrossing.com/postcards/RU-9830214) 
>来自 [EvaS18](https://www.postcrossing.com/user/EvaS18) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.38752~36.73307&lvl=12.0&setlang=zh-Hans) 2023/10/01 21:36 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/11/19 18:39 (当地)
 📏 7,180 | ⏱ 49


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/0mntqe2lc0sfygrisja5uria62de2y7a.jpg)

[NL-5593570](https://www.postcrossing.com/postcards/NL-5593570) 
>来自 [essie1109](https://www.postcrossing.com/user/essie1109) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=51.84917~5.43333&lvl=12.0&setlang=zh-Hans) 2023/10/17 08:56 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/11/19 18:37 (当地)
 📏 9,255 | ⏱ 33


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/1fgbz23qvpbsc89bxala10k47jc6a05u.jpg)

[DE-13430232](https://www.postcrossing.com/postcards/DE-13430232) 
>来自 [vic_and_co](https://www.postcrossing.com/user/vic_and_co) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=48.76508~11.42372&lvl=12.0&setlang=zh-Hans) 2023/09/28 15:57 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/28 18:27 (当地)
 📏 9,025 | ⏱ 30


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/r83g6pj7f3c3qv6s0cjsswrgru1u9w7x.jpg)

[UA-1928471](https://www.postcrossing.com/postcards/UA-1928471) 
>来自 [Iwanka](https://www.postcrossing.com/user/Iwanka) 🇺🇦
> 📤 [Ukraine](https://www.bing.com/maps/?cp=50.45466~30.5238&lvl=12.0&setlang=zh-Hans) 2023/09/28 16:59 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/28 18:27 (当地)
 📏 7,659 | ⏱ 30


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/4i8m3wd4pcpmirk80czwz1elh8rfouoi.jpg)

[CA-1386650](https://www.postcrossing.com/postcards/CA-1386650) 
>来自 [canadaposter](https://www.postcrossing.com/user/canadaposter) 🇨🇦
> 📤 [Canada](https://www.bing.com/maps/?cp=49.10635~-122.82509&lvl=12.0&setlang=zh-Hans) 2023/09/28 06:59 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/28 18:26 (当地)
 📏 10,254 | ⏱ 30


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/l9a18bl5utrfblm89rdy57pnhioeiegp.jpg)

[FR-1651137](https://www.postcrossing.com/postcards/FR-1651137) 
>来自 [yabiz](https://www.postcrossing.com/user/yabiz) 🇫🇷
> 📤 [France](https://www.bing.com/maps/?cp=47.71675~-1.37643&lvl=12.0&setlang=zh-Hans) 2023/09/28 16:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/26 13:57 (当地)
 📏 9,910 | ⏱ 28


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/iyf9a5cc4yv2dr4acdjyyv4p42olxa37.jpg)

[US-9761474](https://www.postcrossing.com/postcards/US-9761474) 
>来自 [KarlaKM](https://www.postcrossing.com/user/KarlaKM) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=34.0584~-106.89142&lvl=12.0&setlang=zh-Hans) 2023/09/28 08:01 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/26 13:56 (当地)
 📏 12,363 | ⏱ 28


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/t9l7z7dtp197o01wzb9r640n7nohvwn3.jpg)

[US-9761471](https://www.postcrossing.com/postcards/US-9761471) 
>来自 [ilysejohnson](https://www.postcrossing.com/user/ilysejohnson) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=37.55376~-77.46026&lvl=12.0&setlang=zh-Hans) 2023/09/28 10:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/26 13:53 (当地)
 📏 13,219 | ⏱ 28


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/fe4nng7tl273fn4tq36wtar0ykk1n89r.jpg)

[AT-696805](https://www.postcrossing.com/postcards/AT-696805) 
>来自 [Bruno1405](https://www.postcrossing.com/user/Bruno1405) 🇦🇹
> 📤 [Austria](https://www.bing.com/maps/?cp=48.20849~16.37208&lvl=12.0&setlang=zh-Hans) 2023/10/01 08:23 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/24 14:00 (当地)
 📏 8,712 | ⏱ 23


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/kx9gctk1k68qndt7q2dwyieasadwmjen.jpg)

[US-9781326](https://www.postcrossing.com/postcards/US-9781326) 
>来自 [mangoqueen24](https://www.postcrossing.com/user/mangoqueen24) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=42.93173~-76.56605&lvl=12.0&setlang=zh-Hans) 2023/10/01 16:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/24 13:58 (当地)
 📏 12,649 | ⏱ 22


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/4a7h4utxbydc5j8mlfkcqlvb7hci4qyp.jpg)

[AT-696806](https://www.postcrossing.com/postcards/AT-696806) 
>来自 [MysticVampire](https://www.postcrossing.com/user/MysticVampire) 🇦🇹
> 📤 [Austria](https://www.bing.com/maps/?cp=48.30639~14.28611&lvl=12.0&setlang=zh-Hans) 2023/10/01 08:23 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/24 13:55 (当地)
 📏 8,852 | ⏱ 23


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/7tonrpjcvm0ftsh5v1edteyk3u5nai22.jpg)

[FI-4485079](https://www.postcrossing.com/postcards/FI-4485079) 
>来自 [pikkumyy15](https://www.postcrossing.com/user/pikkumyy15) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=63.83847~23.13066&lvl=12.0&setlang=zh-Hans) 2023/09/28 16:58 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/24 13:53 (当地)
 📏 7,821 | ⏱ 26


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ra3h05wn9h19d36d51m8q4inz9la4wqi.jpg)

[CZ-2061495](https://www.postcrossing.com/postcards/CZ-2061495) 
>来自 [Jitka-cz](https://www.postcrossing.com/user/Jitka-cz) 🇨🇿
> 📤 [Czechia](https://www.bing.com/maps/?cp=49.83465~18.28204&lvl=12.0&setlang=zh-Hans) 2023/09/28 16:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/24 13:52 (当地)
 📏 8,519 | ⏱ 26


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/z6gmmq6k6pbyc1ki9yxl0nn4y4hcbdso.jpg)

[DE-13430236](https://www.postcrossing.com/postcards/DE-13430236) 
>来自 [annegret](https://www.postcrossing.com/user/annegret) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.45657~7.01228&lvl=12.0&setlang=zh-Hans) 2023/09/28 16:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=22.56004~114.23477&lvl=12.0&setlang=zh-Hans) 2023/10/11 13:57 (当地)
 📏 9,178 | ⏱ 13


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/pac25ahehnw47mqqtyrml2khs4q02pyg.jpg)

### 2015(8)

[RU-3481494](https://www.postcrossing.com/postcards/RU-3481494) 
>来自 ***该用户已关闭*** 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=58.07894~54.6557&lvl=12.0&setlang=zh-Hans) 2015/02/21 02:09 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/04/30 09:01 (当地)
 📏 5,014 | ⏱ 68


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/eb76fb68310040c1b77038ea719cdd14.jpg)

[RU-3317948](https://www.postcrossing.com/postcards/RU-3317948) 
>来自 [Gromakina](https://www.postcrossing.com/user/Gromakina) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=56.49771~84.97437&lvl=12.0&setlang=zh-Hans) 2014/12/24 15:57 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/03/23 13:24 (当地)
 📏 3,406 | ⏱ 89


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/039111ac3670a940e7028bc76f9caa22.jpg)

[NL-2813272](https://www.postcrossing.com/postcards/NL-2813272) 
>来自 [Lexa157](https://www.postcrossing.com/user/Lexa157) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=51.91917~4.38889&lvl=12.0&setlang=zh-Hans) 2014/12/24 10:43 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/03/12 19:24 (当地)
 📏 8,200 | ⏱ 78


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/83a035bc5fe08c8d0909db1aff55b3d9.jpg)

[DE-3809033](https://www.postcrossing.com/postcards/DE-3809033) 
>来自 [BilleLovesBerlin](https://www.postcrossing.com/user/BilleLovesBerlin) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=51.43247~6.76516&lvl=12.0&setlang=zh-Hans) 2014/12/24 10:44 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/03/09 20:25 (当地)
 📏 8,079 | ⏱ 75


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/47a9a53e5fa97480e5e6314eefed0d89.jpg)

[RU-3283393](https://www.postcrossing.com/postcards/RU-3283393) 
>来自 ***该用户已关闭*** 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=59.57639~30.12833&lvl=12.0&setlang=zh-Hans) 2014/12/11 21:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/03/09 20:24 (当地)
 📏 6,427 | ⏱ 88


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/055a622a026e8eadede572375354f6b7.jpg)

[NL-2813278](https://www.postcrossing.com/postcards/NL-2813278) 
>来自 [Pippi2014](https://www.postcrossing.com/user/Pippi2014) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=52.255~6.16389&lvl=12.0&setlang=zh-Hans) 2014/12/24 10:51 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/03/08 23:15 (当地)
 📏 8,075 | ⏱ 74


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/190f02e512026930626537c18cbf9e03.jpg)

[RU-3209780](https://www.postcrossing.com/postcards/RU-3209780) 
>来自 [Red_Queen](https://www.postcrossing.com/user/Red_Queen) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2014/11/19 09:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/03/08 23:10 (当地)
 📏 6,006 | ⏱ 109


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/d94058520953e038f4e8ea8ef0d0db75.jpg)

[BY-1456970](https://www.postcrossing.com/postcards/BY-1456970) 
>来自 [olive_chemistry](https://www.postcrossing.com/user/olive_chemistry) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.9~27.56667&lvl=12.0&setlang=zh-Hans) 2014/11/19 09:11 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2015/01/04 13:04 (当地)
 📏 6,668 | ⏱ 46


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/2b1ce703735b60462dbd22a0c62b7020.jpg)

### 2014(34)

[UA-1140480](https://www.postcrossing.com/postcards/UA-1140480) 
>来自 [Shvets-Jane](https://www.postcrossing.com/user/Shvets-Jane) 🇺🇦
> 📤 [Ukraine](https://www.bing.com/maps/?cp=50.45466~30.5238&lvl=12.0&setlang=zh-Hans) 2014/09/01 11:08 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/30 11:24 (当地)
 📏 6,539 | ⏱ 120


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/66f10b2a5d8fd27da71c75a2307c731e.jpg)

[NL-2773491](https://www.postcrossing.com/postcards/NL-2773491) 
>来自 [Pjotter](https://www.postcrossing.com/user/Pjotter) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=51.53083~4.46528&lvl=12.0&setlang=zh-Hans) 2014/11/23 19:39 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/24 17:34 (当地)
 📏 8,216 | ⏱ 31


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/bc3219e3af342412898d563c5f90bb13.jpg)

[KR-112465](https://www.postcrossing.com/postcards/KR-112465) 
>来自 [minjeomi89](https://www.postcrossing.com/user/minjeomi89) 🇰🇷
> 📤 [Korea (South)](https://www.bing.com/maps/?cp=35.10168~129.03004&lvl=12.0&setlang=zh-Hans) 2014/11/19 15:07 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/24 17:32 (当地)
 📏 2,193 | ⏱ 35


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/0774ccd1d3ea65b27193547f7df31ec3.jpg)

[UA-1195370](https://www.postcrossing.com/postcards/UA-1195370) 
>来自 [oksanagamai](https://www.postcrossing.com/user/oksanagamai) 🇺🇦
> 📤 [Ukraine](https://www.bing.com/maps/?cp=50.47438~24.28288&lvl=12.0&setlang=zh-Hans) 2014/11/19 08:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/22 12:19 (当地)
 📏 6,969 | ⏱ 33


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/d45fbde0fa00ade1cda4f6bc1b3288e5.jpg)

[TW-1431636](https://www.postcrossing.com/postcards/TW-1431636) 
>来自 [Mickeyliu](https://www.postcrossing.com/user/Mickeyliu) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=22.795~120.27639&lvl=12.0&setlang=zh-Hans) 2014/11/19 14:08 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/12/05 16:48 (当地)
 📏 1,582 | ⏱ 16


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/aab5646a22fce46cc103ef7d2f15e8bd.jpg)

[FI-2219730](https://www.postcrossing.com/postcards/FI-2219730) 
>来自 [Holappa](https://www.postcrossing.com/user/Holappa) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=60.29414~25.04099&lvl=12.0&setlang=zh-Hans) 2014/10/02 12:15 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/10/21 16:12 (当地)
 📏 6,698 | ⏱ 19


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/5b170a8cf8ecc675cf73e408e1242d3b.jpg)

[DE-3561745](https://www.postcrossing.com/postcards/DE-3561745) 
>来自 ***该用户已关闭*** 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.52437~13.41053&lvl=12.0&setlang=zh-Hans) 2014/10/02 20:24 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/10/20 18:46 (当地)
 📏 7,616 | ⏱ 18


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/115fb3fbf178d1960069b27c6c3737d9.jpg)

[CZ-524596](https://www.postcrossing.com/postcards/CZ-524596) 
>来自 [Shalila](https://www.postcrossing.com/user/Shalila) 🇨🇿
> 📤 [Czechia](https://www.bing.com/maps/?cp=50.23271~12.87117&lvl=12.0&setlang=zh-Hans) 2014/10/02 11:48 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/10/20 18:45 (当地)
 📏 7,744 | ⏱ 18


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/9c9cf76ca55f0503b9de29da15eec701.jpg)

[BY-1380918](https://www.postcrossing.com/postcards/BY-1380918) 
>来自 [Alenka1](https://www.postcrossing.com/user/Alenka1) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.9~27.56667&lvl=12.0&setlang=zh-Hans) 2014/09/01 08:35 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/26 17:22 (当地)
 📏 6,668 | ⏱ 25


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/c7d9cbca570f09443b2bce06e8c822ad.jpg)

[NL-2652178](https://www.postcrossing.com/postcards/NL-2652178) 
>来自 [andrealandman](https://www.postcrossing.com/user/andrealandman) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=52.7875~4.79861&lvl=12.0&setlang=zh-Hans) 2014/09/02 15:22 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/22 12:57 (当地)
 📏 8,131 | ⏱ 20


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/09e42b276f4db73e1d6212b0d9912520.jpg)

[CA-463793](https://www.postcrossing.com/postcards/CA-463793) 
>来自 [Stinkypaw](https://www.postcrossing.com/user/Stinkypaw) 🇨🇦
> 📤 [Canada](https://www.bing.com/maps/?cp=45.50884~-73.58781&lvl=12.0&setlang=zh-Hans) 2014/09/01 01:35 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/22 12:46 (当地)
 📏 11,636 | ⏱ 21


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/e505c7ac92af313eca757815b6e4d876.jpg)

[RU-2831920](https://www.postcrossing.com/postcards/RU-2831920) 
>来自 [anni-danni](https://www.postcrossing.com/user/anni-danni) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=55.75222~37.61556&lvl=12.0&setlang=zh-Hans) 2014/07/02 13:06 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/22 12:43 (当地)
 📏 6,006 | ⏱ 82


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/47ab21c1ca324c08a5498c81b211f380.jpg)

[FR-427139](https://www.postcrossing.com/postcards/FR-427139) 
>来自 [Cyliane](https://www.postcrossing.com/user/Cyliane) 🇫🇷
> 📤 [France](https://www.bing.com/maps/?cp=46.0802~6.40726&lvl=12.0&setlang=zh-Hans) 2014/09/01 10:07 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/15 15:07 (当地)
 📏 8,374 | ⏱ 14


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/b4f5c081a0694d655c023f12e7e0648c.jpg)

[KR-104416](https://www.postcrossing.com/postcards/KR-104416) 
>来自 [yaho-anna](https://www.postcrossing.com/user/yaho-anna) 🇰🇷
> 📤 [Korea (South)](https://www.bing.com/maps/?cp=37.566~126.9784&lvl=12.0&setlang=zh-Hans) 2014/08/13 09:19 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/02 17:00 (当地)
 📏 2,080 | ⏱ 20


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/045349fb114b9fc3739d25a94faafb59.jpg)

[MK-4914](https://www.postcrossing.com/postcards/MK-4914) 
>来自 [anea09](https://www.postcrossing.com/user/anea09) 🇲🇰
> 📤 [North Macedonia](https://www.bing.com/maps/?cp=41.03143~21.33474&lvl=12.0&setlang=zh-Hans) 2014/07/06 15:51 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/01 13:32 (当地)
 📏 7,506 | ⏱ 57


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/027977b2fc60946bdef3e870409e288c.jpg)

[BY-1344892](https://www.postcrossing.com/postcards/BY-1344892) 
>来自 [MiLENA-](https://www.postcrossing.com/user/MiLENA-) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.9~27.56667&lvl=12.0&setlang=zh-Hans) 2014/07/21 00:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/09/01 13:30 (当地)
 📏 6,668 | ⏱ 42


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/e55ff63ed70b0588f6ca26a3110dd8fa.jpg)

[JP-546807](https://www.postcrossing.com/postcards/JP-546807) 
>来自 [khitomi](https://www.postcrossing.com/user/khitomi) 🇯🇵
> 📤 [Japan](https://www.bing.com/maps/?cp=34.4~132.45&lvl=12.0&setlang=zh-Hans) 2014/06/04 17:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/06/16 16:08 (当地)
 📏 2,493 | ⏱ 12


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ccc32e154e8dd8abbcfc3ca6891de7ff.jpg)

[MY-205746](https://www.postcrossing.com/postcards/MY-205746) 
>来自 [vin_ann](https://www.postcrossing.com/user/vin_ann) 🇲🇾
> 📤 [Malaysia](https://www.bing.com/maps/?cp=3.1412~101.68653&lvl=12.0&setlang=zh-Hans) 2014/05/14 20:23 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/30 21:33 (当地)
 📏 3,007 | ⏱ 16


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/e853702f3763f1a51c65437542e2c580.jpg)

[BY-1268116](https://www.postcrossing.com/postcards/BY-1268116) 
>来自 [Avruha](https://www.postcrossing.com/user/Avruha) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.6884~23.8258&lvl=12.0&setlang=zh-Hans) 2014/04/28 14:43 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/20 11:59 (当地)
 📏 6,913 | ⏱ 22


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/4eec17ae7a8f6caf0a7d2ceb5843e958.jpg)

[DE-3097383](https://www.postcrossing.com/postcards/DE-3097383) 
>来自 [Gaby1967](https://www.postcrossing.com/user/Gaby1967) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=52.43081~7.06833&lvl=12.0&setlang=zh-Hans) 2014/04/16 19:40 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/12 12:17 (当地)
 📏 8,011 | ⏱ 25


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/e8df72704276939fc7633e07e85e08ce.jpg)

[RU-1876931](https://www.postcrossing.com/postcards/RU-1876931) 
>来自 [Krasovskii](https://www.postcrossing.com/user/Krasovskii) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=60.70763~28.75283&lvl=12.0&setlang=zh-Hans) 2013/07/22 20:14 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/12 12:14 (当地)
 📏 6,503 | ⏱ 294


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/aa4cde8359c36bf565da6659226cefb0.jpg)

[NL-2441827](https://www.postcrossing.com/postcards/NL-2441827) 
>来自 [Nighthawk1964](https://www.postcrossing.com/user/Nighthawk1964) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=53.10325~6.01853&lvl=12.0&setlang=zh-Hans) 2014/04/10 20:25 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/09 12:40 (当地)
 📏 8,037 | ⏱ 28


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/af953a2a9c7b70b4bb38553b878ed213.jpg)

[FI-2084613](https://www.postcrossing.com/postcards/FI-2084613) 
>来自 [orienteerer](https://www.postcrossing.com/user/orienteerer) 🇫🇮
> 📤 [Finland](https://www.bing.com/maps/?cp=61.03333~22.33333&lvl=12.0&setlang=zh-Hans) 2014/04/23 14:35 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/05/09 12:38 (当地)
 📏 6,827 | ⏱ 16


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/56a617562753c57021112273b8354ad5.jpg)

[DE-2941052](https://www.postcrossing.com/postcards/DE-2941052) 
>来自 [bluebutterfly222](https://www.postcrossing.com/user/bluebutterfly222) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=49.71754~11.05877&lvl=12.0&setlang=zh-Hans) 2014/02/24 01:03 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/04/16 12:36 (当地)
 📏 7,885 | ⏱ 51


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/0mc10wez9rlow90hnqkmstdgb4y304iw.jpg)

[UA-982846](https://www.postcrossing.com/postcards/UA-982846) 
>来自 [lerolero](https://www.postcrossing.com/user/lerolero) 🇺🇦
> 📤 [Ukraine](https://www.bing.com/maps/?cp=50.45466~30.5238&lvl=12.0&setlang=zh-Hans) 2014/03/04 23:36 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/04/16 12:34 (当地)
 📏 6,539 | ⏱ 42


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/5f24a48ce251612c0861489bce22269c.jpg)

[TW-1215866](https://www.postcrossing.com/postcards/TW-1215866) 
>来自 [Penny7](https://www.postcrossing.com/user/Penny7) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=24.99298~121.49385&lvl=12.0&setlang=zh-Hans) 2014/03/28 23:21 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/04/16 12:32 (当地)
 📏 1,579 | ⏱ 19


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/a418497762809c32d8b20c85a8d10b4f.jpg)

[MY-198583](https://www.postcrossing.com/postcards/MY-198583) 
>来自 [KaiQin](https://www.postcrossing.com/user/KaiQin) 🇲🇾
> 📤 [Malaysia](https://www.bing.com/maps/?cp=1.4655~103.7578&lvl=12.0&setlang=zh-Hans) 2014/03/28 13:12 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/04/11 19:12 (当地)
 📏 3,165 | ⏱ 14


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/4wxbm70ou30tc5ylp4ylkvqyhr9hskmg.jpg)

[TW-1213069](https://www.postcrossing.com/postcards/TW-1213069) 
>来自 [Viola-Pan](https://www.postcrossing.com/user/Viola-Pan) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=25.04776~121.53185&lvl=12.0&setlang=zh-Hans) 2014/03/26 01:35 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/04/04 20:20 (当地)
 📏 1,573 | ⏱ 10


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/4ju868hwkvsljxqh8jz4051n7rmmoc5t.jpg)

[NL-2374423](https://www.postcrossing.com/postcards/NL-2374423) 
>来自 [Anoushka](https://www.postcrossing.com/user/Anoushka) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=52.2375~4.82639&lvl=12.0&setlang=zh-Hans) 2014/03/02 13:22 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/03/24 12:14 (当地)
 📏 8,157 | ⏱ 22


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/dcb79e94963d086e9b2fd7d60588ae24.jpg)

[DE-2812796](https://www.postcrossing.com/postcards/DE-2812796) 
>来自 [ostsee23730](https://www.postcrossing.com/user/ostsee23730) 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=54.10707~10.8145&lvl=12.0&setlang=zh-Hans) 2014/01/13 06:55 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/02/19 20:34 (当地)
 📏 7,722 | ⏱ 37


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/y0y2qqj7716dookhnv8dbtdgax2h59mh.jpg)

[BY-1117952](https://www.postcrossing.com/postcards/BY-1117952) 
>来自 [Breeze87](https://www.postcrossing.com/user/Breeze87) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=53.9~27.56667&lvl=12.0&setlang=zh-Hans) 2013/12/09 14:28 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/02/19 20:34 (当地)
 📏 6,679 | ⏱ 72


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/j9r0fza27qilbesdeg04htxpugzg33js.jpg)

[RU-2254488](https://www.postcrossing.com/postcards/RU-2254488) 
>来自 [SouthWest](https://www.postcrossing.com/user/SouthWest) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=59.93863~30.31413&lvl=12.0&setlang=zh-Hans) 2013/12/09 15:39 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/02/19 20:33 (当地)
 📏 6,424 | ⏱ 72


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/bbfs4b2o9brbjavgkqkbf1l9aiwg1o3a.jpg)

[US-2568426](https://www.postcrossing.com/postcards/US-2568426) 
>来自 [century26](https://www.postcrossing.com/user/century26) 🇺🇸
> 📤 [U.S.A.](https://www.bing.com/maps/?cp=33.44838~-112.07404&lvl=12.0&setlang=zh-Hans) 2013/12/28 13:50 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/02/19 20:32 (当地)
 📏 11,911 | ⏱ 53


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/k9m503n0xlxcrqlj6pw14nsgts3825yt.jpg)

[TW-1121808](https://www.postcrossing.com/postcards/TW-1121808) 
>来自 [YunHung](https://www.postcrossing.com/user/YunHung) 🇹🇼
> 📤 [Taiwan](https://www.bing.com/maps/?cp=23.73944~120.56444&lvl=12.0&setlang=zh-Hans) 2013/12/28 22:00 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2014/01/13 12:25 (当地)
 📏 1,554 | ⏱ 16


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/sg7kqtzxlhr5m9vrglqx2nm0i9vgtzs5.jpg)

### 2013(5)

[RU-2144539](https://www.postcrossing.com/postcards/RU-2144539) 
>来自 [fulun](https://www.postcrossing.com/user/fulun) 🇷🇺
> 📤 [Russia](https://www.bing.com/maps/?cp=53.20007~50.15&lvl=12.0&setlang=zh-Hans) 2013/11/03 18:40 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/12/09 19:27 (当地)
 📏 5,192 | ⏱ 36


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/x5us9epjm1k0rzun7wy5mqo4duh0q8mc.jpg)

[BY-1066085](https://www.postcrossing.com/postcards/BY-1066085) 
>来自 [poliakos](https://www.postcrossing.com/user/poliakos) 🇧🇾
> 📤 [Belarus](https://www.bing.com/maps/?cp=52.4345~30.9754&lvl=12.0&setlang=zh-Hans) 2013/10/26 17:38 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/12/09 19:21 (当地)
 📏 6,480 | ⏱ 44


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/47jtvrurpcy8h4ppd4fuj25btx4d64s3.jpg)

[CZ-322514](https://www.postcrossing.com/postcards/CZ-322514) 
>来自 [TerezkaS](https://www.postcrossing.com/user/TerezkaS) 🇨🇿
> 📤 [Czechia](https://www.bing.com/maps/?cp=49.36064~18.28355&lvl=12.0&setlang=zh-Hans) 2013/08/09 02:10 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/10/02 07:25 (当地)
 📏 7,427 | ⏱ 54


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/ybl39ka8m4j3eyrbyhxga685zhad5v3c.jpg)

[DE-2337903](https://www.postcrossing.com/postcards/DE-2337903) 
>来自 ***该用户已关闭*** 🇩🇪
> 📤 [Germany](https://www.bing.com/maps/?cp=54.9079~8.30326&lvl=12.0&setlang=zh-Hans) 2013/07/22 18:05 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/08/30 15:14 (当地)
 📏 7,835 | ⏱ 39


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/f51f92694ae3571dee5e80be73a063dc.jpg)

[NL-1979851](https://www.postcrossing.com/postcards/NL-1979851) 
>来自 [airsnowmiss](https://www.postcrossing.com/user/airsnowmiss) 🇳🇱
> 📤 [Netherlands](https://www.bing.com/maps/?cp=51.44083~5.47778&lvl=12.0&setlang=zh-Hans) 2013/07/25 17:57 (当地)
> 📥 [China](https://www.bing.com/maps/?cp=29.82739~106.43645&lvl=12.0&setlang=zh-Hans) 2013/08/30 15:12 (当地)
 📏 8,174 | ⏱ 36


![](https://cdn.jsdelivr.net/gh/arthurfsy2/Postcrossing_map_generator@main/gallery/picture/f034894d687e190e2552bb2b6946be17.jpg)