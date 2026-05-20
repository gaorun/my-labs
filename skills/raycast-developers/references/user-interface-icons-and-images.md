# Icons & Images

## API Reference

### Icon

List of built-in icons that can be used for actions or list items.

#### Example

```typescript
import { Icon, List } from "@raycast/api";

export default function Command() {
  return (
    <List>
      <List.Item title="Icon" icon={Icon.Circle} />
    </List>
  );
}
```

#### Enumeration members

|        <p><picture><source srcset="/files/GQEpI16rIsfoXBBLG6xH" media="(prefers-color-scheme: dark)"><img src="/files/DUtZw1vTDz59OwR3So2c" alt=""></picture><br>AddPerson</p>       |        <p><picture><source srcset="/files/uojOytemrhZYfCkZPN2u" media="(prefers-color-scheme: dark)"><img src="/files/MadQAHTksaltpPKYzn3j" alt=""></picture><br>Airplane</p>       |      <p><picture><source srcset="/files/x2sGdDhuRxWnIyna21Tc" media="(prefers-color-scheme: dark)"><img src="/files/lDlebxWvvHhD68ACTU6G" alt=""></picture><br>AirplaneFilled</p>     |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|     <p><picture><source srcset="/files/zCtrS1j4z1sucAB2iSve" media="(prefers-color-scheme: dark)"><img src="/files/01bC6CCwgMT3LQOOTXgA" alt=""></picture><br>AirplaneLanding</p>    |    <p><picture><source srcset="/files/jbpBLs74xH7THC8R0rOr" media="(prefers-color-scheme: dark)"><img src="/files/VMiBp9oLq453f9vqaIoD" alt=""></picture><br>AirplaneTakeoff</p>    |         <p><picture><source srcset="/files/UfL1X6XCWNp6S7DxG1Np" media="(prefers-color-scheme: dark)"><img src="/files/EPvdlpzeZA7FR4tQ0D3J" alt=""></picture><br>Airpods</p>         |
|          <p><picture><source srcset="/files/lHbHizjC9RRk41EUj0R4" media="(prefers-color-scheme: dark)"><img src="/files/g9YITS4r8RkYJfFYX8bC" alt=""></picture><br>Alarm</p>         |      <p><picture><source srcset="/files/RcROIdYI0Ay6UpsIjTeM" media="(prefers-color-scheme: dark)"><img src="/files/7o9y9Wr0iN5YLWOmkZO2" alt=""></picture><br>AlarmRinging</p>     |       <p><picture><source srcset="/files/GnrWI3HGKjCBbpAGnO2f" media="(prefers-color-scheme: dark)"><img src="/files/SV5HcC1tIKTM0Iut0Ot6" alt=""></picture><br>AlignCentre</p>       |
|        <p><picture><source srcset="/files/bBZeL6z2VjWlYs99oaOF" media="(prefers-color-scheme: dark)"><img src="/files/g6S37slmO3G40n0RFty5" alt=""></picture><br>AlignLeft</p>       |       <p><picture><source srcset="/files/EVekpk7IAB7wuzvDyLbu" media="(prefers-color-scheme: dark)"><img src="/files/UhW7luzhKAnmpHXvGUuj" alt=""></picture><br>AlignRight</p>      |     <p><picture><source srcset="/files/YBAJXdxzFyprfuUKqXUx" media="(prefers-color-scheme: dark)"><img src="/files/i9dFRCPI1yV8jUTDerKy" alt=""></picture><br>AmericanFootball</p>    |
|         <p><picture><source srcset="/files/WSptKLIoLIX3DwZhwW0y" media="(prefers-color-scheme: dark)"><img src="/files/XRgcE7xGXlnPRf4VFvwG" alt=""></picture><br>Anchor</p>         |       <p><picture><source srcset="/files/w9eWMznmiEGspkhZqupT" media="(prefers-color-scheme: dark)"><img src="/files/M8fdMlinbShN1XykH8RK" alt=""></picture><br>AppWindow</p>       |     <p><picture><source srcset="/files/Qm7a6ZcXEvcTiWWDDq5E" media="(prefers-color-scheme: dark)"><img src="/files/KcKP7IHqz0HwykKXQerL" alt=""></picture><br>AppWindowGrid2x2</p>    |
|    <p><picture><source srcset="/files/2PsSW1DlJhqOftT4s9nR" media="(prefers-color-scheme: dark)"><img src="/files/aX1iv2PYZepxv9YuMXxZ" alt=""></picture><br>AppWindowGrid3x3</p>    |     <p><picture><source srcset="/files/J1TC22tqzwIZrhOiDFDn" media="(prefers-color-scheme: dark)"><img src="/files/liZVEQw8vjkuZSG7Ar4p" alt=""></picture><br>AppWindowList</p>     |   <p><picture><source srcset="/files/3XkAm8OOlB34KHTNHcr7" media="(prefers-color-scheme: dark)"><img src="/files/QSq8TsyujhPKBdsgZtP4" alt=""></picture><br>AppWindowSidebarLeft</p>  |
|  <p><picture><source srcset="/files/SUPMVUJbARjNcNFom508" media="(prefers-color-scheme: dark)"><img src="/files/b1tjxiIuOxCKuSBDxzlI" alt=""></picture><br>AppWindowSidebarRight</p> |     <p><picture><source srcset="/files/b68tH7lZbNBdpiXAHJdU" media="(prefers-color-scheme: dark)"><img src="/files/kIP1TQS4NbaVN6uSKYWF" alt=""></picture><br>ArrowClockwise</p>    |  <p><picture><source srcset="/files/PxR6Ys7a88e5RE4HRWam" media="(prefers-color-scheme: dark)"><img src="/files/xAY08CSROzmuL5GqNQT2" alt=""></picture><br>ArrowCounterClockwise</p>  |
|        <p><picture><source srcset="/files/GcYgBR9C0O2OPn5qmKIu" media="(prefers-color-scheme: dark)"><img src="/files/t7VDIpQytQEhkaPe3Yj2" alt=""></picture><br>ArrowDown</p>       |    <p><picture><source srcset="/files/t17FutlaqE4Bd4BpY8oT" media="(prefers-color-scheme: dark)"><img src="/files/4DJJARUorUL3yXmQ4Ds4" alt=""></picture><br>ArrowDownCircle</p>    |  <p><picture><source srcset="/files/o84wiRZJTjLfcDGV5FS6" media="(prefers-color-scheme: dark)"><img src="/files/lff5GsLUJhvxjqwwrCSG" alt=""></picture><br>ArrowDownCircleFilled</p>  |
|        <p><picture><source srcset="/files/rmmpSUvPEKQoW3PyRD1h" media="(prefers-color-scheme: dark)"><img src="/files/OjB7MFLRUJzXNFDAMcgE" alt=""></picture><br>ArrowLeft</p>       |    <p><picture><source srcset="/files/SiqGtxzzVO3ngLeHBiDo" media="(prefers-color-scheme: dark)"><img src="/files/TF8ZFgy2MeBufQ23iANc" alt=""></picture><br>ArrowLeftCircle</p>    |  <p><picture><source srcset="/files/6UfXrJexg6yJjXWTjRaZ" media="(prefers-color-scheme: dark)"><img src="/files/5Y4yp4aAnWx7aPKUasC5" alt=""></picture><br>ArrowLeftCircleFilled</p>  |
|         <p><picture><source srcset="/files/BdOFlLVnAKaAn4Cr4l4U" media="(prefers-color-scheme: dark)"><img src="/files/Jh31z3DwvBj7ML1OtSfd" alt=""></picture><br>ArrowNe</p>        |       <p><picture><source srcset="/files/xSJHHAQkKpwNoXSQVEai" media="(prefers-color-scheme: dark)"><img src="/files/ixzViWIRalD4JUKwvSKK" alt=""></picture><br>ArrowRight</p>      |     <p><picture><source srcset="/files/Etanp2qRzG9DPN6TuKsg" media="(prefers-color-scheme: dark)"><img src="/files/BsdKGz8zwqwNEAZqQi1n" alt=""></picture><br>ArrowRightCircle</p>    |
| <p><picture><source srcset="/files/uRZRXZr35yoh7JliWXpM" media="(prefers-color-scheme: dark)"><img src="/files/QMHk0SgDdTNzNk8LKhh3" alt=""></picture><br>ArrowRightCircleFilled</p> |        <p><picture><source srcset="/files/bQnh7nTQB3IJbByPhiH3" media="(prefers-color-scheme: dark)"><img src="/files/ra2KKqUisyK9R9NJluDc" alt=""></picture><br>ArrowUp</p>        |      <p><picture><source srcset="/files/4JDHTrAZzbSBa2vYLmOo" media="(prefers-color-scheme: dark)"><img src="/files/SxaskkgTQjJc4p28gRCA" alt=""></picture><br>ArrowUpCircle</p>      |
|   <p><picture><source srcset="/files/Qx5kzz7ghfVuTTgVSqPz" media="(prefers-color-scheme: dark)"><img src="/files/HyNK4hb1E745WD98nTa1" alt=""></picture><br>ArrowUpCircleFilled</p>  |     <p><picture><source srcset="/files/wKqGHzFIQrqaJH9Zrxj6" media="(prefers-color-scheme: dark)"><img src="/files/xBdhdQs6UJHTX8PiT5pP" alt=""></picture><br>ArrowsContract</p>    |       <p><picture><source srcset="/files/b6Yzc7xaXNO8WPgdKWtk" media="(prefers-color-scheme: dark)"><img src="/files/0HgeWFxiKPqcOVTtraDX" alt=""></picture><br>ArrowsExpand</p>      |
|        <p><picture><source srcset="/files/M0SmwHmMB2z4yAtP95Bh" media="(prefers-color-scheme: dark)"><img src="/files/Dp78RsnPZLkPB8oDqz4q" alt=""></picture><br>AtSymbol</p>        |        <p><picture><source srcset="/files/BaBHrAGLu7e4FrE5JPd7" media="(prefers-color-scheme: dark)"><img src="/files/X9DwwoBzeYsXerDhY6Ya" alt=""></picture><br>BandAid</p>        |         <p><picture><source srcset="/files/Xq3BdDYKH6Q43dj8Xcdr" media="(prefers-color-scheme: dark)"><img src="/files/F4W0qInLvv4aqipCezG9" alt=""></picture><br>BankNote</p>        |
|        <p><picture><source srcset="/files/3ik70zN84abzsh4Zh0BS" media="(prefers-color-scheme: dark)"><img src="/files/e48r5GzymF8mQiOTBFqQ" alt=""></picture><br>BarChart</p>        |        <p><picture><source srcset="/files/KFDJem61vTAhUTlHnsuD" media="(prefers-color-scheme: dark)"><img src="/files/rfVr9jT2EK58kd5y4sEA" alt=""></picture><br>BarCode</p>        |         <p><picture><source srcset="/files/mYBZxD3vQJQS12BnJdYs" media="(prefers-color-scheme: dark)"><img src="/files/xVURlyUemq6eYe8DdAS4" alt=""></picture><br>BathTub</p>         |
|         <p><picture><source srcset="/files/MHxCunfqmR5osdONPd5j" media="(prefers-color-scheme: dark)"><img src="/files/kNSjPF2ceoAW6wwn08FQ" alt=""></picture><br>Battery</p>        |    <p><picture><source srcset="/files/JYtDl7LFvFQOzy4EnpPn" media="(prefers-color-scheme: dark)"><img src="/files/vjMXHDAlR7aOtkbFG6tn" alt=""></picture><br>BatteryCharging</p>    |     <p><picture><source srcset="/files/tx0oeQtm7TUSPMHqcRuR" media="(prefers-color-scheme: dark)"><img src="/files/fRphiXLVZrrZ7TwMI985" alt=""></picture><br>BatteryDisabled</p>     |
|          <p><picture><source srcset="/files/xI1maJcYMljhoCRtCKQG" media="(prefers-color-scheme: dark)"><img src="/files/WMRVNxsElqYGudG98MM6" alt=""></picture><br>Bell</p>          |      <p><picture><source srcset="/files/A34PpXE0uM5vi0QahZ2V" media="(prefers-color-scheme: dark)"><img src="/files/f4R12TKebi4kLwPzJqNE" alt=""></picture><br>BellDisabled</p>     |           <p><picture><source srcset="/files/zz5S9nq9uA7kTkObz7oh" media="(prefers-color-scheme: dark)"><img src="/files/sFhPmEz51Pz6C3WAEacB" alt=""></picture><br>Bike</p>          |
|       <p><picture><source srcset="/files/2KzIQA9QR6TdUf8KhKw4" media="(prefers-color-scheme: dark)"><img src="/files/QRZ2v9C7f7VYf8tJjjYI" alt=""></picture><br>Binoculars</p>       |          <p><picture><source srcset="/files/DFnO7jIOiYlkcTe1RHaQ" media="(prefers-color-scheme: dark)"><img src="/files/LFTaBDpMqa25hYVf1RjD" alt=""></picture><br>Bird</p>         |      <p><picture><source srcset="/files/xTGSZAdkEqrzzcNHbBoH" media="(prefers-color-scheme: dark)"><img src="/files/cId2wjR9ludQEwfTtIcX" alt=""></picture><br>BlankDocument</p>      |
|        <p><picture><source srcset="/files/WL4h3wAX4qRLN0qmd4yg" media="(prefers-color-scheme: dark)"><img src="/files/9FORhvw7mNa7OK1695dh" alt=""></picture><br>Bluetooth</p>       |          <p><picture><source srcset="/files/WBrjWzQAx2Cd0OnSFX9O" media="(prefers-color-scheme: dark)"><img src="/files/15xfrNM6015ajag9PA9B" alt=""></picture><br>Boat</p>         |           <p><picture><source srcset="/files/cge64uILZf3M6e7WaxpT" media="(prefers-color-scheme: dark)"><img src="/files/C0Cfy88jGnv9HqoDSL4b" alt=""></picture><br>Bold</p>          |
|          <p><picture><source srcset="/files/tif0130yxgJW9XnLA04X" media="(prefers-color-scheme: dark)"><img src="/files/wxa2mFPVUNyzqfxKdjCV" alt=""></picture><br>Bolt</p>          |      <p><picture><source srcset="/files/DLF5U9yCL3HK37g8OZxP" media="(prefers-color-scheme: dark)"><img src="/files/XXcaQbvKYnSQzwQ7bdB5" alt=""></picture><br>BoltDisabled</p>     |           <p><picture><source srcset="/files/iZk9gUgWKEvG23KxmQUl" media="(prefers-color-scheme: dark)"><img src="/files/WpTBNUKOiHYeM0W4J2kw" alt=""></picture><br>Book</p>          |
|        <p><picture><source srcset="/files/LKhnCncUyrUYTdruKeq3" media="(prefers-color-scheme: dark)"><img src="/files/nzIKre4EhssD2GaXtv5q" alt=""></picture><br>Bookmark</p>        |          <p><picture><source srcset="/files/C5m0DzHSkFKuyVoUnsv2" media="(prefers-color-scheme: dark)"><img src="/files/OgdngBj7lZdp0q9B9IKP" alt=""></picture><br>Box</p>          |          <p><picture><source srcset="/files/hKixoRF5g9l5xGVqlYtK" media="(prefers-color-scheme: dark)"><img src="/files/4NIwaHFyIM3YJFmD2bIM" alt=""></picture><br>Brush</p>          |
|         <p><picture><source srcset="/files/FUTJXuFXm11qhnzweIq1" media="(prefers-color-scheme: dark)"><img src="/files/0J4ILqAGplKVRipm5QLj" alt=""></picture><br>Bubble</p>         |          <p><picture><source srcset="/files/2QFX4l4Svv4p17pRhnHm" media="(prefers-color-scheme: dark)"><img src="/files/Af1Hxu0YeQAAuo4DzQJG" alt=""></picture><br>Bug</p>          |         <p><picture><source srcset="/files/7uGiYLRZalXZIHLljtZ9" media="(prefers-color-scheme: dark)"><img src="/files/oZs2KQYnZGrc5sgIHTlB" alt=""></picture><br>Building</p>        |
|      <p><picture><source srcset="/files/Z6jy9GHIO0N44SC4Sc4U" media="(prefers-color-scheme: dark)"><img src="/files/4Oy05j3BSBqERiiD2LBg" alt=""></picture><br>BulletPoints</p>      |        <p><picture><source srcset="/files/pFjYtUZImrTcOyaVvUpo" media="(prefers-color-scheme: dark)"><img src="/files/9xNw2wXZ8W00yXV63lzU" alt=""></picture><br>BullsEye</p>       |      <p><picture><source srcset="/files/ZkSd7NKD2IqVxV4NQYaj" media="(prefers-color-scheme: dark)"><img src="/files/NOOZ22kQeMXUUqts2b8u" alt=""></picture><br>BullsEyeMissed</p>     |
|          <p><picture><source srcset="/files/Vn6yT4UtAEBZ4IWIGtfd" media="(prefers-color-scheme: dark)"><img src="/files/X2Jysosie83siV1I6s4v" alt=""></picture><br>Buoy</p>          |       <p><picture><source srcset="/files/ykkI4127zKCBcmLPqGgV" media="(prefers-color-scheme: dark)"><img src="/files/dKF0xGRpziP7O8A03gLl" alt=""></picture><br>Calculator</p>      |         <p><picture><source srcset="/files/PJ9VHNyw9aB74y9IEQGB" media="(prefers-color-scheme: dark)"><img src="/files/QSj416UT7ur6vsYydPbg" alt=""></picture><br>Calendar</p>        |
|         <p><picture><source srcset="/files/0OIpIA3iSjOeJnR3aHhT" media="(prefers-color-scheme: dark)"><img src="/files/BSiYK9OaGeu8KFp2RhTT" alt=""></picture><br>Camera</p>         |          <p><picture><source srcset="/files/hznEwXNEpDJYl41DP4gG" media="(prefers-color-scheme: dark)"><img src="/files/kH8pspX3Y9xlGwVmOkVP" alt=""></picture><br>Car</p>          |           <p><picture><source srcset="/files/pJKb8eG3h8In9MmNoPQh" media="(prefers-color-scheme: dark)"><img src="/files/0sErBsEWmxSKGR7PB77X" alt=""></picture><br>Cart</p>          |
|           <p><picture><source srcset="/files/i6JiUdXcAvAbIcA7rIoY" media="(prefers-color-scheme: dark)"><img src="/files/p4sS7uV5m0AY7gITNsXs" alt=""></picture><br>Cd</p>           |         <p><picture><source srcset="/files/xeEJOZCvxXkul1FoEYiJ" media="(prefers-color-scheme: dark)"><img src="/files/dD001KIalMCOxbGoy4VG" alt=""></picture><br>Center</p>        |          <p><picture><source srcset="/files/q0dLwlkytBnHpABChOTD" media="(prefers-color-scheme: dark)"><img src="/files/7TJZBumYet5W3bBOcK0t" alt=""></picture><br>Check</p>          |
|       <p><picture><source srcset="/files/KuXd9rQfkFeG6oSINJn0" media="(prefers-color-scheme: dark)"><img src="/files/b8rQvvjqBYVgCB16Rbl7" alt=""></picture><br>CheckCircle</p>      |       <p><picture><source srcset="/files/Hz2qNPPznPJK3R0aH6vq" media="(prefers-color-scheme: dark)"><img src="/files/eTwgcLNdg07j9UtYEstH" alt=""></picture><br>CheckList</p>       |       <p><picture><source srcset="/files/Pby5ctfExTFoWAc89jcJ" media="(prefers-color-scheme: dark)"><img src="/files/aCtFpIK49w9EAxB3NdfK" alt=""></picture><br>CheckRosette</p>      |
|        <p><picture><source srcset="/files/CLpGWxUcVUosoEeJHU8y" media="(prefers-color-scheme: dark)"><img src="/files/0Bt5hcMAUU96vsy5cC7d" alt=""></picture><br>Checkmark</p>       |       <p><picture><source srcset="/files/kYqh6FRTq9tf7vXDjBaD" media="(prefers-color-scheme: dark)"><img src="/files/LPDKMj6oBAiu5H8kMYqu" alt=""></picture><br>ChessPiece</p>      |       <p><picture><source srcset="/files/zXhFWRp5f0EL1F46TT26" media="(prefers-color-scheme: dark)"><img src="/files/yAaeDn19a4IayYCFWHFz" alt=""></picture><br>ChevronDown</p>       |
|    <p><picture><source srcset="/files/rJyJ1gu766DHmDoyXzVe" media="(prefers-color-scheme: dark)"><img src="/files/i4bMc7fTgEzPCaff9t5F" alt=""></picture><br>ChevronDownSmall</p>    |      <p><picture><source srcset="/files/jRUgkVmFAO8XHS6Fvvne" media="(prefers-color-scheme: dark)"><img src="/files/nZsgTmQakKkIARMej3z0" alt=""></picture><br>ChevronLeft</p>      |     <p><picture><source srcset="/files/s7f2k3RhEnxMVsmGlS80" media="(prefers-color-scheme: dark)"><img src="/files/iw5WxN1cqSxlImUchp2j" alt=""></picture><br>ChevronLeftSmall</p>    |
|      <p><picture><source srcset="/files/nttmnmEQ0CzVeKXKzNTC" media="(prefers-color-scheme: dark)"><img src="/files/dY8VgrR0fLaXUC578cmX" alt=""></picture><br>ChevronRight</p>      |   <p><picture><source srcset="/files/3by7BWCItuUAdInaBgtr" media="(prefers-color-scheme: dark)"><img src="/files/WgEcwpWiSXSRBEheUb46" alt=""></picture><br>ChevronRightSmall</p>   |        <p><picture><source srcset="/files/odJGybE2VIWivsxfVKtJ" media="(prefers-color-scheme: dark)"><img src="/files/YamqwMY3RXu6ydXVGURe" alt=""></picture><br>ChevronUp</p>        |
|      <p><picture><source srcset="/files/nT7wrJHiLfOLQy7eioz2" media="(prefers-color-scheme: dark)"><img src="/files/fchFVgiLmq168KzDS1KC" alt=""></picture><br>ChevronUpDown</p>     |     <p><picture><source srcset="/files/WDV8mODZAc9szx5DSqeQ" media="(prefers-color-scheme: dark)"><img src="/files/rwopvR3PNkcWvj0LSxqM" alt=""></picture><br>ChevronUpSmall</p>    |          <p><picture><source srcset="/files/j5vxZm8FAxseozEGhpMr" media="(prefers-color-scheme: dark)"><img src="/files/OlTzDAZz12W4OkU7arQJ" alt=""></picture><br>Circle</p>         |
|     <p><picture><source srcset="/files/TiUMjNe9sMpJkCbYaBcb" media="(prefers-color-scheme: dark)"><img src="/files/TIWpZjje0ftnM3mLErB4" alt=""></picture><br>CircleDisabled</p>     |     <p><picture><source srcset="/files/IPVbh0QjlUeIKs5vwYaw" media="(prefers-color-scheme: dark)"><img src="/files/76Vmk1M1uKd9mK9erlmo" alt=""></picture><br>CircleEllipsis</p>    |       <p><picture><source srcset="/files/ofwCj0l6hQGu8CLFF8tM" media="(prefers-color-scheme: dark)"><img src="/files/SyVMnHpq7TpJzENtlA9x" alt=""></picture><br>CircleFilled</p>      |
|     <p><picture><source srcset="/files/cLYkgfQJO8shtIiTLgZb" media="(prefers-color-scheme: dark)"><img src="/files/4CHFYbMMbm9xlv69enEk" alt=""></picture><br>CircleProgress</p>     |   <p><picture><source srcset="/files/TajsabO1utrHH7PGp3ZK" media="(prefers-color-scheme: dark)"><img src="/files/RehPcoDT7bOxgIJ664vD" alt=""></picture><br>CircleProgress100</p>   |     <p><picture><source srcset="/files/gglusAXeOwB2wNoIgvtK" media="(prefers-color-scheme: dark)"><img src="/files/0r6kDLg7KoCEqOJopNnL" alt=""></picture><br>CircleProgress25</p>    |
|    <p><picture><source srcset="/files/KXoPqpXhYtKR1NKJGrlk" media="(prefers-color-scheme: dark)"><img src="/files/8AcJtIKhwDvJO5kvTLe8" alt=""></picture><br>CircleProgress50</p>    |    <p><picture><source srcset="/files/ckma3fB5mD3y8igcqlMi" media="(prefers-color-scheme: dark)"><img src="/files/SpdOzxGJK5KCXvdqF3mH" alt=""></picture><br>CircleProgress75</p>   |     <p><picture><source srcset="/files/KGlEATqQ7PVQKXfa7YFM" media="(prefers-color-scheme: dark)"><img src="/files/5WQfQN65ADy5UIqRA26G" alt=""></picture><br>ClearFormatting</p>     |
|        <p><picture><source srcset="/files/Cwsb7YIo6GTat6u510pR" media="(prefers-color-scheme: dark)"><img src="/files/KwK6Bpx9YCPlBEPwXOD1" alt=""></picture><br>Clipboard</p>       |         <p><picture><source srcset="/files/pTTb8vVat46qmaDrsgJX" media="(prefers-color-scheme: dark)"><img src="/files/hJSiJl52XeIXLr7ooecw" alt=""></picture><br>Clock</p>         |          <p><picture><source srcset="/files/DUgBIKNoG2CHvNhnjnEZ" media="(prefers-color-scheme: dark)"><img src="/files/El5iZ0o6N7WJS3eDEoau" alt=""></picture><br>Cloud</p>          |
|     <p><picture><source srcset="/files/1UI5y95B7FH5jNmQxqK9" media="(prefers-color-scheme: dark)"><img src="/files/ABtssiuq2Vm8Ix1N5FDl" alt=""></picture><br>CloudLightning</p>     |       <p><picture><source srcset="/files/XsODv8G9X1idHzaX2gCn" media="(prefers-color-scheme: dark)"><img src="/files/5ZB7HxN0t2SFcZ0Wz9Iv" alt=""></picture><br>CloudRain</p>       |        <p><picture><source srcset="/files/ZCRD8ltDnKe4ahjlSOeu" media="(prefers-color-scheme: dark)"><img src="/files/MrEEMmQUOfx74GaZPWuT" alt=""></picture><br>CloudSnow</p>        |
|        <p><picture><source srcset="/files/rxjcXzjWMI4Lv5j2YTcW" media="(prefers-color-scheme: dark)"><img src="/files/dYKh2ZdCemGZ63nC5SLz" alt=""></picture><br>CloudSun</p>        |          <p><picture><source srcset="/files/9E2fdGlUwzS5lT17SnTF" media="(prefers-color-scheme: dark)"><img src="/files/ARK5YEAQDYWw3lJtE25X" alt=""></picture><br>Code</p>         |        <p><picture><source srcset="/files/akGyr2sgbkqhXYE6k3xO" media="(prefers-color-scheme: dark)"><img src="/files/uYQkLcPWhIflmJmB3gcr" alt=""></picture><br>CodeBlock</p>        |
|           <p><picture><source srcset="/files/xcoPYEq3UQGmkDLQBwy5" media="(prefers-color-scheme: dark)"><img src="/files/bzdLaeOfeuZRB5dHjQvb" alt=""></picture><br>Cog</p>          |          <p><picture><source srcset="/files/HjLKbP0EF0lpTJdxyIoT" media="(prefers-color-scheme: dark)"><img src="/files/DHKe7GNp6HWjJ8lu9Af9" alt=""></picture><br>Coin</p>         |          <p><picture><source srcset="/files/a6JJ6NNPqGhHAYb2leCi" media="(prefers-color-scheme: dark)"><img src="/files/3OPXf4sPRVcNb1gJD2mM" alt=""></picture><br>Coins</p>          |
|      <p><picture><source srcset="/files/EoenELm59GHORKah9UMG" media="(prefers-color-scheme: dark)"><img src="/files/LQMdClGJ6vL92L4bINI3" alt=""></picture><br>CommandSymbol</p>     |        <p><picture><source srcset="/files/BnVwvUZNmBSJ3bxVxyei" media="(prefers-color-scheme: dark)"><img src="/files/9mMqYKu51Iw6n4quXL56" alt=""></picture><br>Compass</p>        |       <p><picture><source srcset="/files/IhRsKt7HsSI2jr6vZOG6" media="(prefers-color-scheme: dark)"><img src="/files/qM7FYbtWxbjiR9PdTags" alt=""></picture><br>ComputerChip</p>      |
|        <p><picture><source srcset="/files/SPGpxaWSph56fO4JIHJD" media="(prefers-color-scheme: dark)"><img src="/files/dbZAiLIYMGT2zmBwQmnd" alt=""></picture><br>Contrast</p>        |     <p><picture><source srcset="/files/Cwsb7YIo6GTat6u510pR" media="(prefers-color-scheme: dark)"><img src="/files/KwK6Bpx9YCPlBEPwXOD1" alt=""></picture><br>CopyClipboard</p>     |        <p><picture><source srcset="/files/JszDKc5A1TH7qnkDE9Ti" media="(prefers-color-scheme: dark)"><img src="/files/dEyVsA6Fw5bDEykiNPwK" alt=""></picture><br>CreditCard</p>       |
|       <p><picture><source srcset="/files/nvVPUMCYuhkG1orh2QeC" media="(prefers-color-scheme: dark)"><img src="/files/xHFpLBXfL9EQ8JWcYLMG" alt=""></picture><br>CricketBall</p>      |          <p><picture><source srcset="/files/Y4wTVzAPDYsOLXBKwlkp" media="(prefers-color-scheme: dark)"><img src="/files/XhsMKxp7Ngx2lpQJv5c3" alt=""></picture><br>Crop</p>         |          <p><picture><source srcset="/files/OePDm6nxEfEOkHCVhl6M" media="(prefers-color-scheme: dark)"><img src="/files/hAtAz33l2caa2P2pJ8eD" alt=""></picture><br>Crown</p>          |
|         <p><picture><source srcset="/files/8V145jBGNuDXSkm9R8kM" media="(prefers-color-scheme: dark)"><img src="/files/x8Wxa7krpoONxGQOUVoa" alt=""></picture><br>Crypto</p>         |     <p><picture><source srcset="/files/u7buM0F20wA167UkXKaf" media="(prefers-color-scheme: dark)"><img src="/files/YeeSZPVFZ5dNbqFWSLZ5" alt=""></picture><br>DeleteDocument</p>    |         <p><picture><source srcset="/files/QjlsbgpX7DfAPfPUOSCD" media="(prefers-color-scheme: dark)"><img src="/files/VSPseuOQHHlVbVHWLsmj" alt=""></picture><br>Desktop</p>         |
|         <p><picture><source srcset="/files/xYoChGShFP1yW1CL3bVx" media="(prefers-color-scheme: dark)"><img src="/files/yj8fFTAn2dUFCuJnW2De" alt=""></picture><br>Devices</p>        |          <p><picture><source srcset="/files/jrc7lv6KK1bQcC4B9c4t" media="(prefers-color-scheme: dark)"><img src="/files/nqzIO3vaRjR2lI55MFUe" alt=""></picture><br>Dna</p>          |         <p><picture><source srcset="/files/xTGSZAdkEqrzzcNHbBoH" media="(prefers-color-scheme: dark)"><img src="/files/cId2wjR9ludQEwfTtIcX" alt=""></picture><br>Document</p>        |
|           <p><picture><source srcset="/files/R8kGlEmIpvpNJdZUicAc" media="(prefers-color-scheme: dark)"><img src="/files/kfsm0A5fxtPIi99BFY1g" alt=""></picture><br>Dot</p>          |        <p><picture><source srcset="/files/p83pDOaLbc7HsRDmK7uF" media="(prefers-color-scheme: dark)"><img src="/files/lAh3fIMxfKvo21LCJMHY" alt=""></picture><br>Download</p>       |         <p><picture><source srcset="/files/2OFuUpg4RMSHdp7KUkfZ" media="(prefers-color-scheme: dark)"><img src="/files/A73JkhU3QlrIW2hhlAs2" alt=""></picture><br>Droplets</p>        |
|        <p><picture><source srcset="/files/mVkAhfzzUXMEXTmdCtrk" media="(prefers-color-scheme: dark)"><img src="/files/DkWB2fE1WezXYvYXGlq6" alt=""></picture><br>Duplicate</p>       |       <p><picture><source srcset="/files/6h6jYkdHL60IoChyl6D2" media="(prefers-color-scheme: dark)"><img src="/files/tcmPKyD7W6IlyqyN8uQ7" alt=""></picture><br>EditShape</p>       |          <p><picture><source srcset="/files/mbWxFbaHg1jKAHU7sjK4" media="(prefers-color-scheme: dark)"><img src="/files/xvOh629xoceycFVBxnF6" alt=""></picture><br>Eject</p>          |
|        <p><picture><source srcset="/files/PnOeySF1CEb2t4UZwrdo" media="(prefers-color-scheme: dark)"><img src="/files/ACxH0y2I42pztwYmR4rI" alt=""></picture><br>Ellipsis</p>        |    <p><picture><source srcset="/files/98hqBysSOYoIc6hsKy3B" media="(prefers-color-scheme: dark)"><img src="/files/wbwgWrExAXtWAGTDBjlu" alt=""></picture><br>EllipsisVertical</p>   |          <p><picture><source srcset="/files/AxIT1c7QrqrfNded65EF" media="(prefers-color-scheme: dark)"><img src="/files/Q0p7G6UMjTwZl55xaREG" alt=""></picture><br>Emoji</p>          |
|        <p><picture><source srcset="/files/QraSU6w25AkVZN3YLWHr" media="(prefers-color-scheme: dark)"><img src="/files/2CctgPlk0VSLGCLL3EEN" alt=""></picture><br>EmojiSad</p>        |        <p><picture><source srcset="/files/Vn8UJuV3ZP2RH496FQcv" media="(prefers-color-scheme: dark)"><img src="/files/hx57JzB022hIsHCf4LjF" alt=""></picture><br>Envelope</p>       |          <p><picture><source srcset="/files/I3mjXdhwvRZkubDORVIL" media="(prefers-color-scheme: dark)"><img src="/files/sdMC9DnYPXJg1eRle2Nn" alt=""></picture><br>Eraser</p>         |
|     <p><picture><source srcset="/files/qwWYhdPcw3sYNCBq3nuS" media="(prefers-color-scheme: dark)"><img src="/files/WmK9t3vUtUDa6ZQQpqD7" alt=""></picture><br>ExclamationMark</p>    |    <p><picture><source srcset="/files/ULhRhcSg96PIhhzM8jvo" media="(prefers-color-scheme: dark)"><img src="/files/V2zmgc26hAwJiNgeAfmu" alt=""></picture><br>Exclamationmark</p>    |     <p><picture><source srcset="/files/k7GzNrFIM4JPPFmUeb08" media="(prefers-color-scheme: dark)"><img src="/files/qMHXm9CarsAQFRr33CFy" alt=""></picture><br>Exclamationmark2</p>    |
|    <p><picture><source srcset="/files/MCdVIonHOWTX8wbhDBL4" media="(prefers-color-scheme: dark)"><img src="/files/rKdkbgcdjBrkanOoec3B" alt=""></picture><br>Exclamationmark3</p>    |          <p><picture><source srcset="/files/4rT1bga4lB85a7ynbM64" media="(prefers-color-scheme: dark)"><img src="/files/QvYYx13HpEqMhm8U9HNJ" alt=""></picture><br>Eye</p>          |       <p><picture><source srcset="/files/fY8Jj0M2zvlTGpJgBO63" media="(prefers-color-scheme: dark)"><img src="/files/nzjetlbAV2bIZylLdxWp" alt=""></picture><br>EyeDisabled</p>       |
|       <p><picture><source srcset="/files/yZise5fkkAMs1dvo98sz" media="(prefers-color-scheme: dark)"><img src="/files/tWwSbAw9hCOhDcOLwfk2" alt=""></picture><br>EyeDropper</p>       |         <p><picture><source srcset="/files/iJNpFFTERwMkX4qA6VfW" media="(prefers-color-scheme: dark)"><img src="/files/65ByoK3BPZKeo1FH9XF6" alt=""></picture><br>Female</p>        |        <p><picture><source srcset="/files/QR0njVJO3NrntZZvJbWd" media="(prefers-color-scheme: dark)"><img src="/files/m1c0PnT6IWK6dXOA1xRJ" alt=""></picture><br>FilmStrip</p>        |
|         <p><picture><source srcset="/files/zxRXflv4IaJNgfGFS02c" media="(prefers-color-scheme: dark)"><img src="/files/DJJvMqh5UFqBaC7UwC71" alt=""></picture><br>Filter</p>         |         <p><picture><source srcset="/files/IsvLFiBsf671rjBAtazB" media="(prefers-color-scheme: dark)"><img src="/files/WMazBfd9NwkkgEcujyYo" alt=""></picture><br>Finder</p>        |       <p><picture><source srcset="/files/jOXFDcQi3J8MqzxqJJXx" media="(prefers-color-scheme: dark)"><img src="/files/kalPg0jpwCEEIvoSJICA" alt=""></picture><br>Fingerprint</p>       |
|          <p><picture><source srcset="/files/TwuxeADCaznfN5PoAZzA" media="(prefers-color-scheme: dark)"><img src="/files/7krR932VnPt97YcpQaqX" alt=""></picture><br>Flag</p>          |         <p><picture><source srcset="/files/MWBCgvebgCOeP43APt2T" media="(prefers-color-scheme: dark)"><img src="/files/rhdWgMfNbpKmU1HXlTiM" alt=""></picture><br>Folder</p>        |        <p><picture><source srcset="/files/TaDvPi8S2160EustVu9f" media="(prefers-color-scheme: dark)"><img src="/files/4qj8aEFlH5FWg89zdkKg" alt=""></picture><br>Footprints</p>       |
|         <p><picture><source srcset="/files/7kMThtarR5jYH4x0JeDl" media="(prefers-color-scheme: dark)"><img src="/files/4HOKjefYbw6jvhKRTYHM" alt=""></picture><br>Forward</p>        |     <p><picture><source srcset="/files/zbvrd9Qx1b9FRvGS2s5F" media="(prefers-color-scheme: dark)"><img src="/files/gHW0lccpATa4UYnqrKkQ" alt=""></picture><br>ForwardFilled</p>     |       <p><picture><source srcset="/files/gdvcBNX9ZWmP139OnpTu" media="(prefers-color-scheme: dark)"><img src="/files/zmVqZ8L5QV8d6BzicAG6" alt=""></picture><br>FountainTip</p>       |
|       <p><picture><source srcset="/files/fdhPTQtrepy0EOUTN6zi" media="(prefers-color-scheme: dark)"><img src="/files/hFt89v99WE6RQBK846Cn" alt=""></picture><br>FullSignal</p>       |     <p><picture><source srcset="/files/UDbtQrkoH2Cipj0NTx3S" media="(prefers-color-scheme: dark)"><img src="/files/sV4Cdz0JWlktYeNNxwJW" alt=""></picture><br>GameController</p>    |          <p><picture><source srcset="/files/AmZD7wXGZQRAjp5X0s7e" media="(prefers-color-scheme: dark)"><img src="/files/IXB1G7t3Wy8tMvaNPGZX" alt=""></picture><br>Gauge</p>          |
|          <p><picture><source srcset="/files/xcoPYEq3UQGmkDLQBwy5" media="(prefers-color-scheme: dark)"><img src="/files/bzdLaeOfeuZRB5dHjQvb" alt=""></picture><br>Gear</p>          |         <p><picture><source srcset="/files/eFWIGSi3pQHWNqaVkaZr" media="(prefers-color-scheme: dark)"><img src="/files/GKy4hoVYcx70KK0f4gfg" alt=""></picture><br>Geopin</p>        |           <p><picture><source srcset="/files/awAbdO2gLZhyVe23Xpks" media="(prefers-color-scheme: dark)"><img src="/files/FKb3CfPvt6fsKvOMzlag" alt=""></picture><br>Germ</p>          |
|          <p><picture><source srcset="/files/KIs7llJMyhVFQrbAKYrm" media="(prefers-color-scheme: dark)"><img src="/files/52pBDVb9I5nJST1NowbS" alt=""></picture><br>Gift</p>          |        <p><picture><source srcset="/files/swA7R7T2dSP7aOQRLbiF" media="(prefers-color-scheme: dark)"><img src="/files/lLaxBgNctR83G7vDvlAw" alt=""></picture><br>Glasses</p>        |          <p><picture><source srcset="/files/tzEtzXgCycHXAjBkM8Ds" media="(prefers-color-scheme: dark)"><img src="/files/SxqbqVmr5ZYk5uJMwEEZ" alt=""></picture><br>Globe</p>          |
|          <p><picture><source srcset="/files/rsN5nzpEBsCklzvKR3xJ" media="(prefers-color-scheme: dark)"><img src="/files/1n4Xg76jQ3DgET0VAeNu" alt=""></picture><br>Goal</p>          |         <p><picture><source srcset="/files/FuqgHX00BUw7WRDAysxC" media="(prefers-color-scheme: dark)"><img src="/files/zzsrtr0pCt1kfwvOIDpD" alt=""></picture><br>Hammer</p>        |        <p><picture><source srcset="/files/ito0zDCSsNci7KqZAU4A" media="(prefers-color-scheme: dark)"><img src="/files/nY3j1iO8UnSx7Tc0juSf" alt=""></picture><br>HardDrive</p>        |
|         <p><picture><source srcset="/files/NHsEnyS2dReJcx0bUy07" media="(prefers-color-scheme: dark)"><img src="/files/lI0unbqPeIleqOseUlqO" alt=""></picture><br>Hashtag</p>        |        <p><picture><source srcset="/files/z29fmNOmxxXoL0mNjw6J" media="(prefers-color-scheme: dark)"><img src="/files/VxbPNWdyt9INGwLSVoHe" alt=""></picture><br>Heading</p>        |        <p><picture><source srcset="/files/W7O704SVLxKdEdzQFozR" media="(prefers-color-scheme: dark)"><img src="/files/TuXGGdqvJM7ysqYPMpbB" alt=""></picture><br>Headphones</p>       |
|          <p><picture><source srcset="/files/Qjhu0KqfiwihSMw2QJER" media="(prefers-color-scheme: dark)"><img src="/files/bAZTOWZa6806Yb0se3Q8" alt=""></picture><br>Heart</p>         |     <p><picture><source srcset="/files/1QNvIVT4Usmbz5dEUgon" media="(prefers-color-scheme: dark)"><img src="/files/iX70Cu8IIwabCGNufVCr" alt=""></picture><br>HeartDisabled</p>     |        <p><picture><source srcset="/files/V46z90cORYYbxTV1at6a" media="(prefers-color-scheme: dark)"><img src="/files/T7lssaIsBr75Asyv2qwN" alt=""></picture><br>Heartbeat</p>        |
|        <p><picture><source srcset="/files/1i2x49BpWSikBv9I4Dln" media="(prefers-color-scheme: dark)"><img src="/files/SHX1M9zf0eZc7wfHDWmz" alt=""></picture><br>Highlight</p>       |       <p><picture><source srcset="/files/liwFP5CDh8LMZpIEYvYQ" media="(prefers-color-scheme: dark)"><img src="/files/Hq5r1yN1ZwE5zT01yBNe" alt=""></picture><br>Hourglass</p>       |          <p><picture><source srcset="/files/Qb4JF8xhEdjHMGvMkWnh" media="(prefers-color-scheme: dark)"><img src="/files/iLkH6DjlACUKC37Or2hd" alt=""></picture><br>House</p>          |
|        <p><picture><source srcset="/files/4pVCfzilaSvprsPVWEEU" media="(prefers-color-scheme: dark)"><img src="/files/ix1etFL5MAaWKCweAfs1" alt=""></picture><br>Humidity</p>        |         <p><picture><source srcset="/files/JQdYHcF0GbU38LmtI5VH" media="(prefers-color-scheme: dark)"><img src="/files/bxRElzQmMuwZeEPfGZCE" alt=""></picture><br>Image</p>         |        <p><picture><source srcset="/files/qwWYhdPcw3sYNCBq3nuS" media="(prefers-color-scheme: dark)"><img src="/files/WmK9t3vUtUDa6ZQQpqD7" alt=""></picture><br>Important</p>        |
|          <p><picture><source srcset="/files/U8UVyatWdoXsqfTxGots" media="(prefers-color-scheme: dark)"><img src="/files/GpORBjUyJrhBTxJLzMUK" alt=""></picture><br>Info</p>          |        <p><picture><source srcset="/files/Xyd8hcoiSyIyCttPoGUN" media="(prefers-color-scheme: dark)"><img src="/files/eBsomxuv9TZZMEqP5nXn" alt=""></picture><br>Italics</p>        |           <p><picture><source srcset="/files/M7YTm5sdHI70KJUK40gq" media="(prefers-color-scheme: dark)"><img src="/files/wH5q0fvEEdOdvuza8DS6" alt=""></picture><br>Key</p>           |
|        <p><picture><source srcset="/files/lAc2eIi3UhfYLPFwnwGV" media="(prefers-color-scheme: dark)"><img src="/files/pWOmJiojZBDp3ZDpL0Nj" alt=""></picture><br>Keyboard</p>        |         <p><picture><source srcset="/files/bv1eiDaAnFyohAfuRESv" media="(prefers-color-scheme: dark)"><img src="/files/wr16EM2w4e70QuKPSXC4" alt=""></picture><br>Layers</p>        |       <p><picture><source srcset="/files/cCC1YiTakgroK0ofuYSm" media="(prefers-color-scheme: dark)"><img src="/files/NkN6W6AfWj7aKegP7CWP" alt=""></picture><br>Leaderboard</p>       |
|          <p><picture><source srcset="/files/lElf1GylTWMjZs9xEanW" media="(prefers-color-scheme: dark)"><img src="/files/zOWTXbDGCEzFaVB2rZ4g" alt=""></picture><br>Leaf</p>          |       <p><picture><source srcset="/files/biryJ1lpmodFItjSAoQK" media="(prefers-color-scheme: dark)"><img src="/files/hQkHwKP6myZIlqGXNKwE" alt=""></picture><br>LevelMeter</p>      |        <p><picture><source srcset="/files/Wc3YpeQN9kZ73jAaTzcM" media="(prefers-color-scheme: dark)"><img src="/files/u46ZfLfO2vFcuh4tWiSD" alt=""></picture><br>LightBulb</p>        |
|      <p><picture><source srcset="/files/i6qQuVnN20hTH8yrsd6X" media="(prefers-color-scheme: dark)"><img src="/files/TGDoMAMqPvvhl9E3CaSD" alt=""></picture><br>LightBulbOff</p>      |       <p><picture><source srcset="/files/FOcQx4jCtfdqkhXvHaQY" media="(prefers-color-scheme: dark)"><img src="/files/IbM9sSay0itK3i5qxfnb" alt=""></picture><br>LineChart</p>       |           <p><picture><source srcset="/files/ItHoXNf8qecMaOD216gO" media="(prefers-color-scheme: dark)"><img src="/files/DPHqjSvGsxpTE4Y3YMFH" alt=""></picture><br>Link</p>          |
|          <p><picture><source srcset="/files/J1TC22tqzwIZrhOiDFDn" media="(prefers-color-scheme: dark)"><img src="/files/liZVEQw8vjkuZSG7Ar4p" alt=""></picture><br>List</p>          |       <p><picture><source srcset="/files/pr1MhwceOxJmUSuhMFZC" media="(prefers-color-scheme: dark)"><img src="/files/mhDRrycIzVcsotFuTZt9" alt=""></picture><br>Livestream</p>      |    <p><picture><source srcset="/files/UlvgwNPTACr3bCDLdIgE" media="(prefers-color-scheme: dark)"><img src="/files/H5gb4tixRnPwuBfyvUkn" alt=""></picture><br>LivestreamDisabled</p>   |
|          <p><picture><source srcset="/files/tv4oqUyfwemh97AHCcHx" media="(prefers-color-scheme: dark)"><img src="/files/27yH7NgEOwRnOBmnJw3z" alt=""></picture><br>Lock</p>          |      <p><picture><source srcset="/files/tRZCmlCgDfZ0jFiaQfja" media="(prefers-color-scheme: dark)"><img src="/files/4boIbkAp3n8yoU3w74wj" alt=""></picture><br>LockDisabled</p>     |       <p><picture><source srcset="/files/Lh8ClOO8h9QVRKmIIsBH" media="(prefers-color-scheme: dark)"><img src="/files/KcEJ8Q7XCtVFUOKrxyAp" alt=""></picture><br>LockUnlocked</p>      |
|         <p><picture><source srcset="/files/lAcdLN85f6FE2eg6tlhV" media="(prefers-color-scheme: dark)"><img src="/files/outD725U8SZLNBnAJIvP" alt=""></picture><br>Logout</p>         |         <p><picture><source srcset="/files/qpntlGYCgcfbpk1hHYkr" media="(prefers-color-scheme: dark)"><img src="/files/ZyDwQElzcyXszJF7q60f" alt=""></picture><br>Lorry</p>         |        <p><picture><source srcset="/files/IjowJRDwQwPP2lHcT0ED" media="(prefers-color-scheme: dark)"><img src="/files/Pl22ShqzWHDht99YI6j4" alt=""></picture><br>Lowercase</p>        |
|     <p><picture><source srcset="/files/Dc38W4OhReOoNhZBS2r3" media="(prefers-color-scheme: dark)"><img src="/files/ALTQBxKziWV7xGmyWjVc" alt=""></picture><br>MagnifyingGlass</p>    |          <p><picture><source srcset="/files/R2sL6HfGJWUqhlm4p6dm" media="(prefers-color-scheme: dark)"><img src="/files/hhlPvKxWEiNxtLu1Tm8a" alt=""></picture><br>Male</p>         |           <p><picture><source srcset="/files/RBdFqtLNtB0oCPehlUOA" media="(prefers-color-scheme: dark)"><img src="/files/XNq5r8jiwfefyjL6yUYJ" alt=""></picture><br>Map</p>           |
|          <p><picture><source srcset="/files/iFIBCklGF0y0rmIh2dnT" media="(prefers-color-scheme: dark)"><img src="/files/0UpGephXUrfknMtOGykk" alt=""></picture><br>Mask</p>          |        <p><picture><source srcset="/files/jazt3uVrVZWJDMxgUiqd" media="(prefers-color-scheme: dark)"><img src="/files/1wE2O4qPNohqx6pHKq0r" alt=""></picture><br>Maximize</p>       |      <p><picture><source srcset="/files/RVyGeSXJO7gbsiapIchb" media="(prefers-color-scheme: dark)"><img src="/files/hKjuiW8ycsQqDc2SagTu" alt=""></picture><br>MedicalSupport</p>     |
|        <p><picture><source srcset="/files/gh45c8raR1LrvyGhm1EK" media="(prefers-color-scheme: dark)"><img src="/files/AgG2W1tB2zvLjlufzR8s" alt=""></picture><br>Megaphone</p>       |       <p><picture><source srcset="/files/IhRsKt7HsSI2jr6vZOG6" media="(prefers-color-scheme: dark)"><img src="/files/qM7FYbtWxbjiR9PdTags" alt=""></picture><br>MemoryChip</p>      |       <p><picture><source srcset="/files/CM3Wrw8JrLStQr4K7YSq" media="(prefers-color-scheme: dark)"><img src="/files/6vtktIINAuA4jFMBPDuE" alt=""></picture><br>MemoryStick</p>       |
|         <p><picture><source srcset="/files/FUTJXuFXm11qhnzweIq1" media="(prefers-color-scheme: dark)"><img src="/files/0J4ILqAGplKVRipm5QLj" alt=""></picture><br>Message</p>        |       <p><picture><source srcset="/files/U7tnnniUhoz8E52DxYVy" media="(prefers-color-scheme: dark)"><img src="/files/w7vBqSQM1tzQZk5mChNr" alt=""></picture><br>Microphone</p>      |    <p><picture><source srcset="/files/9YNyf3vCatBEiPHeDX6r" media="(prefers-color-scheme: dark)"><img src="/files/KPHwOOgv65xephkDg9fu" alt=""></picture><br>MicrophoneDisabled</p>   |
|        <p><picture><source srcset="/files/3jHQAC8dIy4kLMTuMo33" media="(prefers-color-scheme: dark)"><img src="/files/f2KeCbccTJg0Xc08X892" alt=""></picture><br>Minimize</p>        |         <p><picture><source srcset="/files/6ERvVWMhOZ6W8xH88XWJ" media="(prefers-color-scheme: dark)"><img src="/files/5V3WiAferxpcBqBG0Lhk" alt=""></picture><br>Minus</p>         |       <p><picture><source srcset="/files/rZMnZbVZg39eXm1DAVPA" media="(prefers-color-scheme: dark)"><img src="/files/oFhZzxPHpKJ1yJXPjraJ" alt=""></picture><br>MinusCircle</p>       |
|    <p><picture><source srcset="/files/rDSXhLKlDr7FpdaTdn8A" media="(prefers-color-scheme: dark)"><img src="/files/SEfaBQ8lA1SnyIZ4yJcx" alt=""></picture><br>MinusCircleFilled</p>   |         <p><picture><source srcset="/files/nnRpNgD5H7WGpsdbEeRg" media="(prefers-color-scheme: dark)"><img src="/files/9DgjD5VUREVER876hZba" alt=""></picture><br>Mobile</p>        |         <p><picture><source srcset="/files/wMMzE1pMQw0zSyDhcZ5n" media="(prefers-color-scheme: dark)"><img src="/files/McaQKYUqRqmridE3arFr" alt=""></picture><br>Monitor</p>         |
|          <p><picture><source srcset="/files/LyNgLGtsFasHvpfPlzgx" media="(prefers-color-scheme: dark)"><img src="/files/ebfYP1yVbuWEaKBpNdE8" alt=""></picture><br>Moon</p>          |        <p><picture><source srcset="/files/aGmBNTC6mXsizxvaXQGn" media="(prefers-color-scheme: dark)"><img src="/files/PSP7oPqhKZw9hT8xWQ70" alt=""></picture><br>MoonDown</p>       |          <p><picture><source srcset="/files/YPSQj5XgzLb2XH4dCOvA" media="(prefers-color-scheme: dark)"><img src="/files/AkgWgiZAAIrL7GIXl0xS" alt=""></picture><br>MoonUp</p>         |
|        <p><picture><source srcset="/files/FsRy5gBJaEV30jjyMTZV" media="(prefers-color-scheme: dark)"><img src="/files/5NxD1V46BnjyU5Mit1vF" alt=""></picture><br>Moonrise</p>        |        <p><picture><source srcset="/files/riw7ftKwDSgrMVoxJqZ1" media="(prefers-color-scheme: dark)"><img src="/files/EsWAHfZQuSxbmqEWR8fS" alt=""></picture><br>Mountain</p>       |          <p><picture><source srcset="/files/JBMBW0s8UXEDwAiVP80y" media="(prefers-color-scheme: dark)"><img src="/files/sPnyEXm5eiDNzHMtMvaV" alt=""></picture><br>Mouse</p>          |
|          <p><picture><source srcset="/files/aU20bC1UXK3V82SQjhYp" media="(prefers-color-scheme: dark)"><img src="/files/8EV5TsknXFHn7rLMoJat" alt=""></picture><br>Move</p>          |          <p><picture><source srcset="/files/5RjSVe3ds8ePtAdGzPLC" media="(prefers-color-scheme: dark)"><img src="/files/DfSgauFrebnP3kJEtbjH" alt=""></picture><br>Mug</p>          |         <p><picture><source srcset="/files/7lelPZI5riiO0hi1RcxJ" media="(prefers-color-scheme: dark)"><img src="/files/rutDe8BSVPA2PIK2YKy9" alt=""></picture><br>MugSteam</p>        |
|        <p><picture><source srcset="/files/31LhnMDlNccTAEGMxQqt" media="(prefers-color-scheme: dark)"><img src="/files/VOK6xp17iQfQuyzpBCyE" alt=""></picture><br>Multiply</p>        |         <p><picture><source srcset="/files/uWSA9muXQtiR7TJDhNCX" media="(prefers-color-scheme: dark)"><img src="/files/iLa7dWjcK5hVDqUpMPgO" alt=""></picture><br>Music</p>         |         <p><picture><source srcset="/files/dQLiK7ssTQJHmPJpov3w" media="(prefers-color-scheme: dark)"><img src="/files/f100ofJ4Usx7g1Z4fUQP" alt=""></picture><br>Network</p>         |
|       <p><picture><source srcset="/files/jKLT9v2DjZrKYt4umlTx" media="(prefers-color-scheme: dark)"><img src="/files/iJbW9EloBFwHk1xfh0cu" alt=""></picture><br>NewDocument</p>      |       <p><picture><source srcset="/files/fPB66JBR5And3OHMfkRX" media="(prefers-color-scheme: dark)"><img src="/files/qwzQLNF3pOFpms0m2ggw" alt=""></picture><br>NewFolder</p>       |        <p><picture><source srcset="/files/mKXV1mQIROFi5kYmylLL" media="(prefers-color-scheme: dark)"><img src="/files/c1qrdn8oRz9Lo10pw22H" alt=""></picture><br>Paperclip</p>        |
|        <p><picture><source srcset="/files/xTcqq4MvUn1fMGkwx19O" media="(prefers-color-scheme: dark)"><img src="/files/Rp7BIITHIzUQds1nolBJ" alt=""></picture><br>Paragraph</p>       |         <p><picture><source srcset="/files/qqJX12LFMELbsc8D5TSW" media="(prefers-color-scheme: dark)"><img src="/files/nov9g4dKLK2hT2fJEIOf" alt=""></picture><br>Patch</p>         |          <p><picture><source srcset="/files/xtToXd7KWB6kK25MMAzX" media="(prefers-color-scheme: dark)"><img src="/files/ZmnIa2lWtlFoSeQ0xhYr" alt=""></picture><br>Pause</p>          |
|       <p><picture><source srcset="/files/HawYP9SAiypI8uZkVdqs" media="(prefers-color-scheme: dark)"><img src="/files/hV07JYfuCwT4i0PkxPxq" alt=""></picture><br>PauseFilled</p>      |         <p><picture><source srcset="/files/CVVyitCwTM58v7roZro4" media="(prefers-color-scheme: dark)"><img src="/files/S5UyOUl4iQRT7BarQuqD" alt=""></picture><br>Pencil</p>        |          <p><picture><source srcset="/files/ffzbvd1ZU614KugBDjBP" media="(prefers-color-scheme: dark)"><img src="/files/zIGpiPaKb8UBPXKFBAug" alt=""></picture><br>Person</p>         |
|      <p><picture><source srcset="/files/cD5lBO9mKgf1asqXEqut" media="(prefers-color-scheme: dark)"><img src="/files/c1ZTmyHgsgrVefrIBlV7" alt=""></picture><br>PersonCircle</p>      |      <p><picture><source srcset="/files/gCnScqE8YsjsXrEb852j" media="(prefers-color-scheme: dark)"><img src="/files/5mGfFe6OAd8hKhINHclU" alt=""></picture><br>PersonLines</p>      |          <p><picture><source srcset="/files/grjqcuQsg8VQf15AtH9S" media="(prefers-color-scheme: dark)"><img src="/files/5xdrViDzmbsNpbjwGwxl" alt=""></picture><br>Phone</p>          |
|      <p><picture><source srcset="/files/NzRSQ3spG6K4K4JjFFsz" media="(prefers-color-scheme: dark)"><img src="/files/exgk53Zfu0pG2XPXx5tv" alt=""></picture><br>PhoneRinging</p>      |        <p><picture><source srcset="/files/Sv2WB8iXjT2VFEh6jHwz" media="(prefers-color-scheme: dark)"><img src="/files/lNW50HkhGrFATCuZLTT7" alt=""></picture><br>PieChart</p>       |           <p><picture><source srcset="/files/XAJfSWsL25aSSMi6AE6h" media="(prefers-color-scheme: dark)"><img src="/files/gu990OxbyIywbMNbZ6Vf" alt=""></picture><br>Pill</p>          |
|           <p><picture><source srcset="/files/oCYSntE6wdiTx5d4XHdX" media="(prefers-color-scheme: dark)"><img src="/files/4OfKVsos9nEio31XlJ0t" alt=""></picture><br>Pin</p>          |      <p><picture><source srcset="/files/H9lEsm049e8sg0w1JszB" media="(prefers-color-scheme: dark)"><img src="/files/vx3fxQRxck6OWXOVC8JG" alt=""></picture><br>PinDisabled</p>      |           <p><picture><source srcset="/files/WJd8Jug9nYEA1lcMXYoX" media="(prefers-color-scheme: dark)"><img src="/files/fAHURvUJmGKzKJan5uks" alt=""></picture><br>Play</p>          |
|       <p><picture><source srcset="/files/zqbLD59TfC8fIpz7xOyi" media="(prefers-color-scheme: dark)"><img src="/files/mrXRhdUCdaOjLFAJPS5q" alt=""></picture><br>PlayFilled</p>       |          <p><picture><source srcset="/files/gsoxq9VmoGxbDrj3JQ9M" media="(prefers-color-scheme: dark)"><img src="/files/5uXgRoGQDr5jHP3oL58j" alt=""></picture><br>Plug</p>         |           <p><picture><source srcset="/files/rHwFymqb1GnfwhlR72PZ" media="(prefers-color-scheme: dark)"><img src="/files/iRbtpIk5B09bFXKd0Q40" alt=""></picture><br>Plus</p>          |
|       <p><picture><source srcset="/files/FOsrA5Tv8Il1cJQvSg90" media="(prefers-color-scheme: dark)"><img src="/files/9fElNIXOsRewrbC9GBdk" alt=""></picture><br>PlusCircle</p>       |    <p><picture><source srcset="/files/199dl8B58lhihUYGabmh" media="(prefers-color-scheme: dark)"><img src="/files/0ij9PEbJfgyLrUSC33VS" alt=""></picture><br>PlusCircleFilled</p>   | <p><picture><source srcset="/files/W64Ul9Zus3LxyTjOxhtW" media="(prefers-color-scheme: dark)"><img src="/files/yWdB8DYxYqUE3f8iVUfq" alt=""></picture><br>PlusMinusDivideMultiply</p> |
|       <p><picture><source srcset="/files/lxbxsJ0gxJfmHR7gAKD8" media="(prefers-color-scheme: dark)"><img src="/files/PdxeK1ATSttCwuMch5WI" alt=""></picture><br>PlusSquare</p>       |   <p><picture><source srcset="/files/2w39HqXWcikQirN69646" media="(prefers-color-scheme: dark)"><img src="/files/PPiAd8KMs303D4ZWnNPB" alt=""></picture><br>PlusTopRightSquare</p>  |          <p><picture><source srcset="/files/qzXbzLYw0rAUzGxfmNwV" media="(prefers-color-scheme: dark)"><img src="/files/1HAoY95imrfuJDWW1BWs" alt=""></picture><br>Power</p>          |
|          <p><picture><source srcset="/files/SUvPdtzIWl1jNxeN0GHC" media="(prefers-color-scheme: dark)"><img src="/files/he58XRPwHhOVNeF48ZDo" alt=""></picture><br>Print</p>         |      <p><picture><source srcset="/files/DsNpAqQvNFn4ZteHcOk6" media="(prefers-color-scheme: dark)"><img src="/files/B2nCedH4bKl2BeRafMz9" alt=""></picture><br>QuestionMark</p>     |    <p><picture><source srcset="/files/DsNpAqQvNFn4ZteHcOk6" media="(prefers-color-scheme: dark)"><img src="/files/B2nCedH4bKl2BeRafMz9" alt=""></picture><br>QuestionMarkCircle</p>   |
|        <p><picture><source srcset="/files/g7i343a3vJBcVfAj7OCn" media="(prefers-color-scheme: dark)"><img src="/files/7ViYeMKBzQ7lZa3mgnRM" alt=""></picture><br>Quicklink</p>       |     <p><picture><source srcset="/files/Z0H89Yw0mkKZe16OXnTV" media="(prefers-color-scheme: dark)"><img src="/files/EEy510wxqcxAO7Vjtq71" alt=""></picture><br>QuotationMarks</p>    |        <p><picture><source srcset="/files/RD3mWckC4qwOsFFxXKN0" media="(prefers-color-scheme: dark)"><img src="/files/jX8AbSyqirh5n6FrLznN" alt=""></picture><br>QuoteBlock</p>       |
|         <p><picture><source srcset="/files/OHyNbcvK4RWj7GoZ7p21" media="(prefers-color-scheme: dark)"><img src="/files/rGfnvFRgzHUbBqv9SZy2" alt=""></picture><br>Racket</p>         |        <p><picture><source srcset="/files/pDS1oMzJVr7YLLSFRPnH" media="(prefers-color-scheme: dark)"><img src="/files/ZwqTYgNF5Gf6i1PsZ96r" alt=""></picture><br>Raindrop</p>       |      <p><picture><source srcset="/files/FJYBgDWsaQGPkeJ2bRmd" media="(prefers-color-scheme: dark)"><img src="/files/WrsiqvDPTO2nEc2GYVrx" alt=""></picture><br>RaycastLogoNeg</p>     |
|     <p><picture><source srcset="/files/VHVWBECmH7x1rsxzURgN" media="(prefers-color-scheme: dark)"><img src="/files/v7EX9gbANKUBZTMnWIzO" alt=""></picture><br>RaycastLogoPos</p>     |        <p><picture><source srcset="/files/ZNZBmyfqBLqQGtzucxll" media="(prefers-color-scheme: dark)"><img src="/files/961gVZtL5Yf2cSnfaPoN" alt=""></picture><br>Receipt</p>        |           <p><picture><source srcset="/files/kpP6buDgEW0OrVmSRuXo" media="(prefers-color-scheme: dark)"><img src="/files/oUFhUrsxAXPPl4OuiZoL" alt=""></picture><br>Redo</p>          |
|      <p><picture><source srcset="/files/mmft2T4TdiRdUTQ78jTa" media="(prefers-color-scheme: dark)"><img src="/files/40F9CZFziX3HO6DWGM4u" alt=""></picture><br>RemovePerson</p>      |         <p><picture><source srcset="/files/1eRclZkU9j6c5RNJvGMJ" media="(prefers-color-scheme: dark)"><img src="/files/gxNtG0paQI7EcDMKJOF1" alt=""></picture><br>Repeat</p>        |         <p><picture><source srcset="/files/18GpK4cWzCwath7mbVDC" media="(prefers-color-scheme: dark)"><img src="/files/GU4XI6t0gZeN4bqSDwHw" alt=""></picture><br>Replace</p>         |
|       <p><picture><source srcset="/files/eFdv3NjiQhfTS2WcIvDq" media="(prefers-color-scheme: dark)"><img src="/files/Verzw4izT5wWawOs90jR" alt=""></picture><br>ReplaceOne</p>       |         <p><picture><source srcset="/files/fnlvI6SMRbgmSRC65GAM" media="(prefers-color-scheme: dark)"><img src="/files/nFxiTJQTh5YLF3v0j9lv" alt=""></picture><br>Reply</p>         |          <p><picture><source srcset="/files/SrC3mARIIvJLySS2Xtys" media="(prefers-color-scheme: dark)"><img src="/files/8RLW84mtxLfTpPxzUBZY" alt=""></picture><br>Rewind</p>         |
|      <p><picture><source srcset="/files/gt8Bx3ftmQXU4btU3Jn8" media="(prefers-color-scheme: dark)"><img src="/files/hAvg0mJxk4dCi1vafaQw" alt=""></picture><br>RewindFilled</p>      |         <p><picture><source srcset="/files/iWKyiJ0RY1P9XJNrTtMj" media="(prefers-color-scheme: dark)"><img src="/files/HsjBXceDRmgy4a6S2MWa" alt=""></picture><br>Rocket</p>        |         <p><picture><source srcset="/files/ZW7ndNNudJl7KjlPdWOF" media="(prefers-color-scheme: dark)"><img src="/files/0SZqWKWslUKZN1EphUVw" alt=""></picture><br>Rosette</p>         |
|   <p><picture><source srcset="/files/PCAfRgIQtgkMRUkHvvJY" media="(prefers-color-scheme: dark)"><img src="/files/tfYrIqZVzgeXFRzOCTKR" alt=""></picture><br>RotateAntiClockwise</p>  |    <p><picture><source srcset="/files/7CRDIIxA8vnsbDUEVJVK" media="(prefers-color-scheme: dark)"><img src="/files/5uVcz8ZCywRTtH4voxOt" alt=""></picture><br>RotateClockwise</p>    |           <p><picture><source srcset="/files/Kh4Xv6kkRdBDk28yJ0sZ" media="(prefers-color-scheme: dark)"><img src="/files/i1rBsLCKCd18w6SMZ5s3" alt=""></picture><br>Rss</p>           |
|          <p><picture><source srcset="/files/ZZpx0MU3rAlFcW4yuPg1" media="(prefers-color-scheme: dark)"><img src="/files/BbACojXLiUJEAxmbFK97" alt=""></picture><br>Ruler</p>         |      <p><picture><source srcset="/files/hFZ8qJ4ah2c8L5bKfaUo" media="(prefers-color-scheme: dark)"><img src="/files/58ISXSXTLIbdgPOh8HDC" alt=""></picture><br>SaveDocument</p>     |          <p><picture><source srcset="/files/0FCb4eW6FfqpzARYX99I" media="(prefers-color-scheme: dark)"><img src="/files/snzpPUMLF8xmJ958Xfpp" alt=""></picture><br>Shield</p>         |
|     <p><picture><source srcset="/files/6yQjTIAO130tNHaMqrSm" media="(prefers-color-scheme: dark)"><img src="/files/ynqLehCd7QoDCqnj3R4q" alt=""></picture><br>ShortParagraph</p>     |        <p><picture><source srcset="/files/2wR3A5tvfaOhsRTWqmC2" media="(prefers-color-scheme: dark)"><img src="/files/NU02pyWmKniiIgSn0AeZ" alt=""></picture><br>Shuffle</p>        |         <p><picture><source srcset="/files/SUPMVUJbARjNcNFom508" media="(prefers-color-scheme: dark)"><img src="/files/b1tjxiIuOxCKuSBDxzlI" alt=""></picture><br>Sidebar</p>         |
|         <p><picture><source srcset="/files/1iOhaRiheG1N4c0H3l9p" media="(prefers-color-scheme: dark)"><img src="/files/xtyoDJfcvOtBdlonvsjV" alt=""></picture><br>Signal0</p>        |        <p><picture><source srcset="/files/Mu3dQHUbaoixaiSjZ03p" media="(prefers-color-scheme: dark)"><img src="/files/vvEcLK3RcksmWwJ8532A" alt=""></picture><br>Signal1</p>        |         <p><picture><source srcset="/files/biryJ1lpmodFItjSAoQK" media="(prefers-color-scheme: dark)"><img src="/files/hQkHwKP6myZIlqGXNKwE" alt=""></picture><br>Signal2</p>         |
|         <p><picture><source srcset="/files/8nzzYCHW0ru5ai5K5wWi" media="(prefers-color-scheme: dark)"><img src="/files/VGuJhi2c2zICt9w905B0" alt=""></picture><br>Signal3</p>        |        <p><picture><source srcset="/files/heOAgxBKa5eskOpzyUXB" media="(prefers-color-scheme: dark)"><img src="/files/pWWPP0ydl5bTn1kNQSWn" alt=""></picture><br>Snippets</p>       |        <p><picture><source srcset="/files/NRNk8TSRFm8uvtqJ7Wbc" media="(prefers-color-scheme: dark)"><img src="/files/LTxaZkboZ10fXJtWX59V" alt=""></picture><br>Snowflake</p>        |
|       <p><picture><source srcset="/files/D2HgTQprTnLHDxS0WhoW" media="(prefers-color-scheme: dark)"><img src="/files/AZdwKa8AYoRoKH2PDOXL" alt=""></picture><br>SoccerBall</p>       |        <p><picture><source srcset="/files/Zu9pJtcHvqKffhMKCM9D" media="(prefers-color-scheme: dark)"><img src="/files/ZNchsOp0RSyjoPtdyz4I" alt=""></picture><br>Speaker</p>        |       <p><picture><source srcset="/files/NJ2EqKEvOAqdmYdViX2f" media="(prefers-color-scheme: dark)"><img src="/files/1Zou0mwHuGTwHsea9ckU" alt=""></picture><br>SpeakerDown</p>       |
|       <p><picture><source srcset="/files/k8agdwEAyL0NlodpvlsB" media="(prefers-color-scheme: dark)"><img src="/files/eXPHsnQRAFAMYUGrRAjD" alt=""></picture><br>SpeakerHigh</p>      |       <p><picture><source srcset="/files/NoTJIGlwAhkdnPVNYzS9" media="(prefers-color-scheme: dark)"><img src="/files/dTLq5NNJfSjigiJxPz6k" alt=""></picture><br>SpeakerLow</p>      |        <p><picture><source srcset="/files/16xsioeKqSXrC2mR1VaK" media="(prefers-color-scheme: dark)"><img src="/files/3G8mWTo5yxZ141kVO3tw" alt=""></picture><br>SpeakerOff</p>       |
|        <p><picture><source srcset="/files/Gqm8x4n44xoWVZdNz19d" media="(prefers-color-scheme: dark)"><img src="/files/mMoiqfJZoAsyxZGQraAB" alt=""></picture><br>SpeakerOn</p>       |       <p><picture><source srcset="/files/iIoSTNzdFp6GoWG5REUC" media="(prefers-color-scheme: dark)"><img src="/files/pM8ZFwasMlLXG9RkPHt6" alt=""></picture><br>SpeakerUp</p>       |       <p><picture><source srcset="/files/FUTJXuFXm11qhnzweIq1" media="(prefers-color-scheme: dark)"><img src="/files/0J4ILqAGplKVRipm5QLj" alt=""></picture><br>SpeechBubble</p>      |
|   <p><picture><source srcset="/files/6BU79uwPaCGdspAwK67f" media="(prefers-color-scheme: dark)"><img src="/files/ZFn7Ukqj06weUPyc8q9t" alt=""></picture><br>SpeechBubbleActive</p>   | <p><picture><source srcset="/files/vb6fIay4XqcXj1Kbs65Z" media="(prefers-color-scheme: dark)"><img src="/files/RJ2JtkcqDffbn5jQNvh7" alt=""></picture><br>SpeechBubbleImportant</p> |      <p><picture><source srcset="/files/QmkJcaXwxEnOoRrJdeZK" media="(prefers-color-scheme: dark)"><img src="/files/UDz2DAgym2CTPHcRHctq" alt=""></picture><br>SquareEllipsis</p>     |
|      <p><picture><source srcset="/files/QU3TDvF8Z9mxHdZpnHV0" media="(prefers-color-scheme: dark)"><img src="/files/nwVuQmOJQ8T3NuhfXpjA" alt=""></picture><br>StackedBars1</p>      |      <p><picture><source srcset="/files/yzut02xxfc8D83fiXFYn" media="(prefers-color-scheme: dark)"><img src="/files/r69Y8sTVygi0WCXtrFBz" alt=""></picture><br>StackedBars2</p>     |       <p><picture><source srcset="/files/RHbRmef8dBZw3FFRsM4d" media="(prefers-color-scheme: dark)"><img src="/files/gSAg38O9UEr9aaXAv6jY" alt=""></picture><br>StackedBars3</p>      |
|      <p><picture><source srcset="/files/ocjvUW031p12B1liQOjL" media="(prefers-color-scheme: dark)"><img src="/files/7u7O93tZeLkzNt3zyI3k" alt=""></picture><br>StackedBars4</p>      |          <p><picture><source srcset="/files/Fszy6Mq5Ik3yJrLdoV03" media="(prefers-color-scheme: dark)"><img src="/files/anPAo6QaOxNadQlp5FJA" alt=""></picture><br>Star</p>         |        <p><picture><source srcset="/files/3CQ9x91stsghiiEiyFJk" media="(prefers-color-scheme: dark)"><img src="/files/AAnU2tDr30jnwi9lML2A" alt=""></picture><br>StarCircle</p>       |
|      <p><picture><source srcset="/files/tO5D7KylehgPZcepZYKA" media="(prefers-color-scheme: dark)"><img src="/files/mmEbHcN2Stc9lw7aVyOh" alt=""></picture><br>StarDisabled</p>      |         <p><picture><source srcset="/files/AUapT4enTvwvMuCwi6YV" media="(prefers-color-scheme: dark)"><img src="/files/LTQLmcgMOyudqrqBibM9" alt=""></picture><br>Stars</p>         |           <p><picture><source srcset="/files/Xz7CTiUs9JcSptpR55rX" media="(prefers-color-scheme: dark)"><img src="/files/0qVIaF5tWUObzrs7e9Bv" alt=""></picture><br>Stop</p>          |
|       <p><picture><source srcset="/files/zBiatShp7Rq3aQ3xOYE2" media="(prefers-color-scheme: dark)"><img src="/files/8fOEDSXLO5exT3ouOLEq" alt=""></picture><br>StopFilled</p>       |       <p><picture><source srcset="/files/btTQknDFreTqeAptxdUO" media="(prefers-color-scheme: dark)"><img src="/files/6s2yWMSlKeYdoEop630K" alt=""></picture><br>Stopwatch</p>       |          <p><picture><source srcset="/files/hCNmnHKnL70KZilM0hbk" media="(prefers-color-scheme: dark)"><img src="/files/V9oxdq0uNbglqSVYgH9q" alt=""></picture><br>Store</p>          |
|      <p><picture><source srcset="/files/cWp6ohcWKyPsv9LxpNH4" media="(prefers-color-scheme: dark)"><img src="/files/OO9qBSbcamDd4uQl0qKj" alt=""></picture><br>StrikeThrough</p>     |          <p><picture><source srcset="/files/6uAh3FhirKgKxrPucaCT" media="(prefers-color-scheme: dark)"><img src="/files/PCHF9FKytY4QkotVshGJ" alt=""></picture><br>Sun</p>          |         <p><picture><source srcset="/files/r6aAFPx68Ydi1iaTNe64" media="(prefers-color-scheme: dark)"><img src="/files/WFikjHMmhl1NOvwpPgNn" alt=""></picture><br>Sunrise</p>         |
|         <p><picture><source srcset="/files/zZUrUO03qVYZ1NVKzc32" media="(prefers-color-scheme: dark)"><img src="/files/ubBsDQwhCyBhxgsYIrYh" alt=""></picture><br>Swatch</p>         |         <p><picture><source srcset="/files/pkc9G0gKJidJmj1caa4K" media="(prefers-color-scheme: dark)"><img src="/files/FTqPn3dBTiFJjBdXOHCO" alt=""></picture><br>Switch</p>        |         <p><picture><source srcset="/files/MA76WwbBgwwgBl7EZiPS" media="(prefers-color-scheme: dark)"><img src="/files/UPF0UxkxDoEe2YLsMDN5" alt=""></picture><br>Syringe</p>         |
|          <p><picture><source srcset="/files/OtqLeMqIO0rXnjVQ834s" media="(prefers-color-scheme: dark)"><img src="/files/9ppbtAHTcJa0i1MUj1HB" alt=""></picture><br>Tack</p>          |      <p><picture><source srcset="/files/LMLaINuzkeJOQSszHI0r" media="(prefers-color-scheme: dark)"><img src="/files/MFK6tYSJd3sXbRae69A7" alt=""></picture><br>TackDisabled</p>     |           <p><picture><source srcset="/files/w4PErkyNxxP1xtSbAFRA" media="(prefers-color-scheme: dark)"><img src="/files/I7PMJSsnlDys0WfdMUGw" alt=""></picture><br>Tag</p>           |
|       <p><picture><source srcset="/files/d5imKiaRqsw7XQPcNCFY" media="(prefers-color-scheme: dark)"><img src="/files/qrwI7qLRwvYqkAU3lVAe" alt=""></picture><br>Temperature</p>      |       <p><picture><source srcset="/files/5ByaIHED1Fdzg1YfC4RJ" media="(prefers-color-scheme: dark)"><img src="/files/bUxJxKSGb4nTgxpdSl38" alt=""></picture><br>TennisBall</p>      |         <p><picture><source srcset="/files/7nVwN73WEgYrsWBKeDkL" media="(prefers-color-scheme: dark)"><img src="/files/bVsofvwDvWamhtMoCfey" alt=""></picture><br>Terminal</p>        |
|          <p><picture><source srcset="/files/L04L3IrmfBkSP2VnWCLV" media="(prefers-color-scheme: dark)"><img src="/files/YiWwwYVkEzn32tXHADjX" alt=""></picture><br>Text</p>          |       <p><picture><source srcset="/files/90VbTzmL39XIxQkqgZFn" media="(prefers-color-scheme: dark)"><img src="/files/84HerwnhJsAFgfOaKYq0" alt=""></picture><br>TextCursor</p>      |        <p><picture><source srcset="/files/7PaPEUOS40MBJu2kwS34" media="(prefers-color-scheme: dark)"><img src="/files/p1S3rn3L8L6gKTLvgoUN" alt=""></picture><br>TextInput</p>        |
|      <p><picture><source srcset="/files/RSSMJXSBlyOyUtpmJFTw" media="(prefers-color-scheme: dark)"><img src="/files/zT4IkTCoJ3FuxUdxgny8" alt=""></picture><br>TextSelection</p>     |       <p><picture><source srcset="/files/ESJCtwt3vYZxVhVoHo4l" media="(prefers-color-scheme: dark)"><img src="/files/VLoEFsV5t1enMohezVOP" alt=""></picture><br>ThumbsDown</p>      |     <p><picture><source srcset="/files/76EZjQDXWuGQfWitBlkM" media="(prefers-color-scheme: dark)"><img src="/files/LZ0V87CWZEwBKVGCrd6x" alt=""></picture><br>ThumbsDownFilled</p>    |
|        <p><picture><source srcset="/files/knbYFoPSLjo3p3PgJOd8" media="(prefers-color-scheme: dark)"><img src="/files/a1tnETjkItLzhI5b1QLM" alt=""></picture><br>ThumbsUp</p>        |     <p><picture><source srcset="/files/K3njE9JW2c9n106fgjwP" media="(prefers-color-scheme: dark)"><img src="/files/KcvBp81YjTegguagP2Wy" alt=""></picture><br>ThumbsUpFilled</p>    |          <p><picture><source srcset="/files/4dCWDRJVmMqaAaqCnfmw" media="(prefers-color-scheme: dark)"><img src="/files/bC3aXRL6ZAJYg4fRuWrb" alt=""></picture><br>Ticket</p>         |
|          <p><picture><source srcset="/files/LTYAdTd1HRdBDaKyYUuH" media="(prefers-color-scheme: dark)"><img src="/files/lhH40XSS8qSuXyZS7NMF" alt=""></picture><br>Torch</p>         |         <p><picture><source srcset="/files/9jE5gtWwUy3TW0KnORHF" media="(prefers-color-scheme: dark)"><img src="/files/moJK09eBeLqpiwPW0OO3" alt=""></picture><br>Train</p>         |          <p><picture><source srcset="/files/4Sakycxsxz2iBCLnsrEr" media="(prefers-color-scheme: dark)"><img src="/files/V1wIAuImDJqJJ6j2AuPF" alt=""></picture><br>Trash</p>          |
|          <p><picture><source srcset="/files/aStDME9eFcSZEWw7l44b" media="(prefers-color-scheme: dark)"><img src="/files/wuAhpxQumlZfRWAdEX28" alt=""></picture><br>Tray</p>          |          <p><picture><source srcset="/files/gQu9SiPMzKIGq3F7UrtB" media="(prefers-color-scheme: dark)"><img src="/files/KdWfsX0RcrJaHEUDFvdc" alt=""></picture><br>Tree</p>         |          <p><picture><source srcset="/files/TOOwyTalJ6wlmn3ZU1sH" media="(prefers-color-scheme: dark)"><img src="/files/nVTIHNg6LVbA53mHjnOr" alt=""></picture><br>Trophy</p>         |
|        <p><picture><source srcset="/files/oslNtSBe2UbNyglbzqrS" media="(prefers-color-scheme: dark)"><img src="/files/yvRM7WJCiRWH1RLDW2J6" alt=""></picture><br>TwoPeople</p>       |        <p><picture><source srcset="/files/hFmyCehty7tFMKZZVwPm" media="(prefers-color-scheme: dark)"><img src="/files/xV7sskLO5Q3HSkYfa2QG" alt=""></picture><br>Umbrella</p>       |        <p><picture><source srcset="/files/wY83frRK9Wr8z72bsmGe" media="(prefers-color-scheme: dark)"><img src="/files/UO91crWud2aIs7AStMLf" alt=""></picture><br>Underline</p>        |
|          <p><picture><source srcset="/files/KmbBoX3kLorta6x9mU98" media="(prefers-color-scheme: dark)"><img src="/files/emTSHZfOaqN8JSqU92tc" alt=""></picture><br>Undo</p>          |         <p><picture><source srcset="/files/WfVWuJyif7oTIGSqzZF2" media="(prefers-color-scheme: dark)"><img src="/files/Okb6hNOhfZ3y9znWTVhB" alt=""></picture><br>Upload</p>        |        <p><picture><source srcset="/files/4cZDQKINwtuW2eiQbWQa" media="(prefers-color-scheme: dark)"><img src="/files/3PZlyFHv5WT892p53yML" alt=""></picture><br>Uppercase</p>        |
|          <p><picture><source srcset="/files/e6hZDExvAfOSLFjuTLLo" media="(prefers-color-scheme: dark)"><img src="/files/bkv8MQI9kEkVwoYZfd3t" alt=""></picture><br>Video</p>         |     <p><picture><source srcset="/files/fXSKFFnBjx1r5wYJege2" media="(prefers-color-scheme: dark)"><img src="/files/jmRRVFKWF3EsFHQJcH8s" alt=""></picture><br>VideoDisabled</p>     |          <p><picture><source srcset="/files/jftC2xlHiESUtEDqBIW8" media="(prefers-color-scheme: dark)"><img src="/files/rxLpkkJMPiIUzXfutTyt" alt=""></picture><br>Wallet</p>         |
|          <p><picture><source srcset="/files/hUVZFu6wn9RGDxW8EFx0" media="(prefers-color-scheme: dark)"><img src="/files/v7dBswTfv1Y5y1Q1zszt" alt=""></picture><br>Wand</p>          |        <p><picture><source srcset="/files/7V7zlWNRMM5POJjshcgA" media="(prefers-color-scheme: dark)"><img src="/files/HVAceaZ9AOC9FnqLKxA7" alt=""></picture><br>Warning</p>        |         <p><picture><source srcset="/files/vU56nQYJ9GfyOa84mT5u" media="(prefers-color-scheme: dark)"><img src="/files/1ANRnL3pgVpyTtpj3K3E" alt=""></picture><br>Waveform</p>        |
|         <p><picture><source srcset="/files/PKLAFmrWm5pMUrJj9IK0" media="(prefers-color-scheme: dark)"><img src="/files/ziKKSnAGkmrmc6wwTaZB" alt=""></picture><br>Weights</p>        |          <p><picture><source srcset="/files/GFY5vuLUtncJ676fJqKi" media="(prefers-color-scheme: dark)"><img src="/files/Yunc58Gq7No4pN7EjXWQ" alt=""></picture><br>Wifi</p>         |       <p><picture><source srcset="/files/6yL0ah4JyTy1Uf4YIQ1G" media="(prefers-color-scheme: dark)"><img src="/files/Y51wq2Ikq5FgHF20lhsk" alt=""></picture><br>WifiDisabled</p>      |
|          <p><picture><source srcset="/files/9rk342Deo5rKQDN8dgtP" media="(prefers-color-scheme: dark)"><img src="/files/bQuKDYXSNZ8AZsgj6Wo9" alt=""></picture><br>Wind</p>          |         <p><picture><source srcset="/files/w9eWMznmiEGspkhZqupT" media="(prefers-color-scheme: dark)"><img src="/files/M8fdMlinbShN1XykH8RK" alt=""></picture><br>Window</p>        |         <p><picture><source srcset="/files/qU1X6u1ds0CLMs6Y4lxP" media="(prefers-color-scheme: dark)"><img src="/files/rEypjCBS6lf1nOnWM3OK" alt=""></picture><br>Windsock</p>        |
|    <p><picture><source srcset="/files/AJrHnwynOLUx5fRkCSNW" media="(prefers-color-scheme: dark)"><img src="/files/aVuJCzbQTwGOYX6m0tmL" alt=""></picture><br>WrenchScrewdriver</p>   |       <p><picture><source srcset="/files/aIOOb9uJQSwTfEWbpM3b" media="(prefers-color-scheme: dark)"><img src="/files/oCtN7cQPUZZ7MLu3fDlN" alt=""></picture><br>WristWatch</p>      |       <p><picture><source srcset="/files/Bmq1nfTZZ72xBOsP9ZuA" media="(prefers-color-scheme: dark)"><img src="/files/vllsBJg8NBZnVhnPkONn" alt=""></picture><br>XMarkCircle</p>       |
|    <p><picture><source srcset="/files/9ywj2vX0RWzXuzVXfnAH" media="(prefers-color-scheme: dark)"><img src="/files/lBaloCbbnBM0WvFBtzAm" alt=""></picture><br>XMarkCircleFilled</p>   |  <p><picture><source srcset="/files/BPZXvgb2PoicJbr4gDri" media="(prefers-color-scheme: dark)"><img src="/files/kpdBPbRFblpUJsHOH4t6" alt=""></picture><br>XMarkCircleHalfDash</p>  |   <p><picture><source srcset="/files/YoRqHfB4ciSs84bVGjdP" media="(prefers-color-scheme: dark)"><img src="/files/gmyw9iheqGYAEBkhQ01M" alt=""></picture><br>XMarkTopRightSquare</p>   |
|          <p><picture><source srcset="/files/U4U4IdNLjxK8Hsi8skRL" media="(prefers-color-scheme: dark)"><img src="/files/FJ6rJKfqV3TWxpa8s6XH" alt=""></picture><br>Xmark</p>         |                                                                                                                                                                                     |                                                                                                                                                                                       |

### Image.Mask

Available masks that can be used to change the shape of an image.

Can be handy to shape avatars or other items in a list.

#### Example

```typescript
import { Image, List } from "@raycast/api";

export default function Command() {
  return (
    <List>
      <List.Item
        title="Icon"
        icon={{
          source: "https://raycast.com/uploads/avatar.png",
          mask: Image.Mask.Circle,
        }}
      />
    </List>
  );
}
```

#### Enumeration members

| Name             | Value              |
| ---------------- | ------------------ |
| Circle           | "circle"           |
| RoundedRectangle | "roundedRectangle" |

## Types

### Image

Display different types of images, including network images or bundled assets.

Apply image transforms to the source, such as a `mask` or a `tintColor`.

{% hint style="info" %}
Tip: Suffix your local assets with `@dark` to automatically provide a dark theme option, eg: `icon.png` and `icon@dark.png`.
{% endhint %}

#### Example

```typescript
// Built-in icon
const icon = Icon.Eye;

// Built-in icon with tint color
const tintedIcon = { source: Icon.Bubble, tintColor: Color.Red };

// Bundled asset with circular mask
const avatar = { source: "avatar.png", mask: Image.Mask.Circle };

// Implicit theme-aware icon
// with 'icon.png' and 'icon@dark.png' in the `assets` folder
const icon = "icon.png";

// Explicit theme-aware icon
const icon = { source: { light: "https://example.com/icon-light.png", dark: "https://example.com/icon-dark.png" } };
```

#### Properties

| Property                                 | Description                                                            | Type                                                                                                                        |
| ---------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| source<mark style="color:red;">\*</mark> | The Image.Source of the image.                                         | [`Image.Source`](#image.source)                                                                                             |
| fallback                                 | Image.Fallback image, in case `source` can't be loaded.                | [`Image.Fallback`](#image.fallback)                                                                                         |
| mask                                     | A Image.Mask to apply to the image.                                    | [`Image.Mask`](#image.mask)                                                                                                 |
| tintColor                                | A Color.ColorLike to tint all the non-transparent pixels of the image. | [`Color.ColorLike`](https://developers.raycast.com/api-reference/user-interface/pages/-MiwANRbUk391XIQ6FMp#color.colorlike) |

### FileIcon

An icon as it's used in the Finder.

#### Example

```typescript
import { List } from "@raycast/api";

export default function Command() {
  return (
    <List>
      <List.Item title="File icon" icon={{ fileIcon: __filename }} />
    </List>
  );
}
```

#### Properties

| Property                                   | Description                                        | Type     |
| ------------------------------------------ | -------------------------------------------------- | -------- |
| fileIcon<mark style="color:red;">\*</mark> | The path to a file or folder to get its icon from. | `string` |

### Image.ImageLike

```typescript
ImageLike: URL | Asset | Icon | FileIcon | Image;
```

Union type for the supported image types.

#### Example

```typescript
import { Icon, Image, List } from "@raycast/api";

export default function Command() {
  return (
    <List>
      <List.Item title="URL" icon="https://raycast.com/uploads/avatar.png" />
      <List.Item title="Asset" icon="avatar.png" />
      <List.Item title="Icon" icon={Icon.Circle} />
      <List.Item title="FileIcon" icon={{ fileIcon: __filename }} />
      <List.Item
        title="Image"
        icon={{
          source: "https://raycast.com/uploads/avatar.png",
          mask: Image.Mask.Circle,
        }}
      />
    </List>
  );
}
```

### Image.Source

```typescript
Image.Source: URL | Asset | Icon | { light: URL | Asset; dark: URL | Asset }
```

The source of an [Image](#image). Can be either a remote URL, a local file resource, a built-in [Icon](#icon) or a single emoji.

For consistency, it's best to use the built-in [Icon](#icon) in lists, the Action Panel, and other places. If a specific icon isn't built-in, you can reference custom ones from the `assets` folder of the extension by file name, e.g. `my-icon.png`. Alternatively, you can reference an absolute HTTPS URL that points to an image or use an emoji. You can also specify different remote or local assets for light and dark theme.

#### Example

```typescript
import { Icon, List } from "@raycast/api";

export default function Command() {
  return (
    <List>
      <List.Item title="URL" icon={{ source: "https://raycast.com/uploads/avatar.png" }} />
      <List.Item title="Asset" icon={{ source: "avatar.png" }} />
      <List.Item title="Icon" icon={{ source: Icon.Circle }} />
      <List.Item
        title="Theme"
        icon={{
          source: {
            light: "https://raycast.com/uploads/avatar.png",
            dark: "https://raycast.com/uploads/avatar.png",
          },
        }}
      />
    </List>
  );
}
```

### Image.Fallback

```typescript
Image.Fallback: Asset | Icon | { light: Asset; dark: Asset }
```

A fallback [Image](#image) that will be displayed in case the source image cannot be loaded. Can be either a local file resource, a built-in [Icon](#icon), a single emoji, or a theme-aware asset. Any specified `mask` or `tintColor` will also apply to the fallback image.

#### Example

```typescript
import { List } from "@raycast/api";

export default function Command() {
  return (
    <List>
      <List.Item
        title="URL Source With Asset Fallback"
        icon={{
          source: "https://raycast.com/uploads/avatar.png",
          fallback: "default-avatar.png",
        }}
      />
    </List>
  );
}
```

### Image.URL

Image is a string representing a URL.

#### Example

```typescript
import { List } from "@raycast/api";

export default function Command() {
  return (
    <List>
      <List.Item title="URL" icon={{ source: "https://raycast.com/uploads/avatar.png" }} />
    </List>
  );
}
```

### Image.Asset

Image is a string representing an asset from the `assets/` folder

#### Example

```typescript
import { List } from "@raycast/api";

export default function Command() {
  return (
    <List>
      <List.Item title="Asset" icon={{ source: "avatar.png" }} />
    </List>
  );
}
```


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://developers.raycast.com/api-reference/user-interface/icons-and-images.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
