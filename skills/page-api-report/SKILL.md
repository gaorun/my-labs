---
name: page-api-report
description: 从前端视角分析单个页面的后端接口调用链路。当用户要求分析某个页面的接口、梳理页面API调用、了解前端页面调了哪些后端接口、整理接口出参/入参在前端的消费方式，或提到"页面接口分析""接口梳理""API flow""接口调用流程""页面接口发现报告"时触发。适合后端/测试同学了解前端接口使用全貌。
---

# 页面接口发现报告 (Page API Flow)

从前端视角，按用户操作动线发现并梳理单个页面的所有后端接口调用链路，输出给**后端开发、测试、产品**阅读的接口分析报告。

## 触发条件

当用户提出以下需求时触发：

- "分析这个页面的接口"、"这个页面调了哪些接口"
- "帮我梳理页面的后端接口调用"
- "从前端视角分析接口"、"接口调用链路"
- 给出一个页面路径/路由/文件夹，要求整理接口文档

## 输入要求

用户需指定目标页面，可以是以下任一形式：

- **路由路径**：如 `/dashboard/orders`、`/user/profile`
- **页面文件夹**：如 `src/views/orders/`、`pages/dashboard/`
- **页面入口文件**：如 `src/pages/Dashboard/index.tsx`、`src/views/OrderList.vue`

如果用户未指定，主动询问。

## 工作流程

### 阶段零：确认输出格式

开始分析前，询问用户想要什么格式的报告：

| 格式             | 参数值     | 输出文件               | 适用场景                                             |
| ---------------- | ---------- | ---------------------- | ---------------------------------------------------- |
| **HTML**（默认） | `html`     | `page_api_report.html` | 富文本页面，含 SVG 时序图和样式，适合浏览器查看/分享 |
| **Markdown**     | `markdown` | `page_api_report.md`   | 纯文本报告，含 Mermaid 时序图，适合嵌入 Wiki、GitHub |

- 用户未指定时默认使用 **HTML** 格式
- 告知用户两种格式的特点，让其选择

### 阶段一：定位页面入口

1. 根据用户指定的路由/文件/文件夹，找到页面的入口文件
2. 如果是路由路径，先在路由配置中解析出对应的组件文件
3. 读取入口文件，了解页面整体结构

**搜索策略（按优先级）：**

- Vue 项目：查找 `src/router/index.ts` / `.js` 中的 `component` 字段
- React 项目：查找 `src/router/` 或 `App.tsx` 中的 `<Route>` 定义
- Next.js：按 `pages/` 或 `app/` 目录结构定位
- 如果是文件夹直接指定，读取文件夹下的 `index.vue` / `index.tsx` 等入口

### 阶段二：递归探索页面依赖

从页面入口文件出发，递归发现所有本地依赖：

1. **读取入口文件**，提取所有 `import` 语句
2. **分类 import**：
   - **页面级子组件**：`./components/xxx`、`./xxx` 等相对路径组件
   - **业务逻辑文件**：`./hooks/xxx`、`./services/xxx`、`./utils/xxx`、`./api/xxx` 等
   - **项目级公共组件**：`@/components/xxx`、`src/components/xxx`（如果上下文足够）
   - **第三方依赖**：`xxx`（npm 包）—— **跳过，不展开**
3. **递归追踪**：对页面级子组件，同样读取并分析其依赖，直到没有新的本地文件
4. **搜索 API 调用**：在所有相关文件中搜索后端接口调用

**API 调用搜索模式：**

- `axios.get/post/put/delete/patch`、`request.get/post(...)`
- `fetch(`、`$http.`、`api.`、`service.`
- 读取项目封装的 HTTP 模块（如 `@/utils/request`、`@/utils/http`），识别其调用签名
- 记录每个 API 调用的**请求方法 + 完整接口路径**（微服务名 + 路径）

### 阶段三：按用户动线排序接口

按用户实际操作的顺序来安排接口的呈现顺序。思路是：

1. **页面进入**（页面加载时触发）
   - URL 参数解析、权限校验
   - 初始化配置接口（下拉选项、字典数据等）
   - 页面主数据加载
2. **用户交互**（用户操作触发）
   - 搜索/筛选
   - 翻页
   - 详情弹窗/抽屉
   - 表单提交
   - 审批/状态变更
3. **后台轮询**（定时器触发）
   - 状态刷新
   - 消息/通知轮询
4. **页面切换/离开**（路由变化触发）

对每个接口记录：

- **接口名称**：`微服务名 + /api/xxx/xxx`
- **请求方法**：`GET` / `POST` / `PUT` / `DELETE`
- **调用时机**：用大白话说明用户视角的操作复现路径，例如：
  - ✅ "用户进入列表页面时自动加载，展示第一页 20 条数据"
  - ✅ "用户点击列表某行的「查看详情」按钮后触发，弹出抽屉展示订单详情"
  - ❌ 不要写 "组件 mounted 时 dispatch action"、"watch 监听 route.query 变化后调用"

### 阶段四：分析接口出参（响应字段）

对每个接口的返回值，梳理前端如何消费：

1. **阅读前端代码中对接口返回值的处理**
   - 搜索 `res.data`、`response.data`、`.then(res =>` 等模式
   - 追踪字段如何映射到页面 UI 上（如赋值给哪个变量，绑定到哪个 v-model、显示在哪个 template 位置）
2. **对每个关键字段记录**：

| 信息         | 说明                                                                                      |
| ------------ | ----------------------------------------------------------------------------------------- |
| **字段名**   | 响应 JSON 中的字段路径，如 `data.list[].orderNo`、`data.totalCount`                       |
| **页面作用** | 大白话描述字段在页面上的作用，聚焦**交互和业务含义**，不写前端代码变量名                  |
| **枚举值**   | 如果字段有枚举值，列出每个值和对应的含义（如 0=待审核, 1=已通过, 2=已拒绝）               |
| **空值兜底** | 如果后端不下发该字段或下发空值，前端有什么兜底行为（显示 "--"、隐藏该区域、使用默认值等） |

**注意：**

- 不要逐行翻译代码逻辑，用业务语言解释
- 优先分析影响页面展示和交互的核心字段
- 如果字段在多个地方被消费，合并说明

### 阶段五：分析接口入参（请求参数）

对每个接口的请求参数，梳理前端从哪里取值：

| 信息            | 说明                                                                                                                          |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **字段名**      | 请求体中的字段名，如 `orderNo`、`status`、`pageSize`                                                                          |
| **取值来源**    | 值从哪来：URL query 参数 / 前一接口 `xxx` 的返回字段 `yyy` / 用户输入（搜索框/下拉/日期选择）/ localStorage / cookie / 固定值 |
| **默认值/枚举** | 前端是否有默认值；如果字段是枚举，列出可选值和含义                                                                            |

**常见取值来源：**

- `URL query params（路由参数）`
- `localStorage`（如缓存的用户信息 `userInfo.id`）
- `前一个接口的返回值`（如列表接口返回 `orderNo`，详情接口以它作为入参）
- `用户输入`（搜索框、下拉框、日期选择器）
- `固定常量`（如 `pageSize: 20`）
- `Cookie`（如鉴权 token 由 HTTP 库自动附加）

### 阶段六：记录本地缓存与轮询策略

如果前端对接口数据做了本地缓存或设置了轮询，在报告中说明：

- **数据缓存**：哪些接口返回的数据被缓存到了 `localStorage` / `sessionStorage` / Vuex Store / Redux Store，缓存多久
- **鉴权缓存**：Token 是否缓存，缓存在哪，过期策略
- **轮询**：哪些接口有定时轮询，间隔多久，在什么条件下开始/停止
- **请求去重**：是否有防重复提交、竞态处理等

### 阶段七：生成报告

1. 将全部数据整理为 JSON 中间数据，保存为 `.page_api_report_data.json`
2. 运行报告生成脚本：

```bash
# HTML（默认，含 SVG 时序图）
python <skill_dir>/scripts/generate_report.py .page_api_report_data.json --format html

# Markdown（含 Mermaid 时序图）
python <skill_dir>/scripts/generate_report.py .page_api_report_data.json --format markdown
```

常用选项：

- `--format html|markdown` — 选择输出格式（默认 HTML）
- `-o <文件路径>` — 自定义输出路径
- `--no-open` — 不自动打开浏览器（HTML 格式）

### 阶段八：交付

- 告知用户报告已生成，说明输出文件位置
- 如果是 HTML 格式，询问是否需要打开浏览器预览

## JSON 中间数据结构

```json
{
  "page_title": "订单列表页",
  "page_route": "/orders/list",
  "project_name": "xxx-frontend",
  "framework": "Vue 3",
  "analysis_time": "2026-05-25",
  "total_apis": 5,
  "apis": [
    {
      "index": 1,
      "name": "trade-service /api/order/list",
      "method": "POST",
      "trigger_timing": "用户进入页面时自动调用，获取订单列表",
      "trigger_category": "页面进入",
      "request_params": [
        {
          "field": "pageNum",
          "source": "固定值，默认为 1，翻页时由分页组件更新"
        },
        { "field": "pageSize", "source": "固定值 20" },
        {
          "field": "status",
          "source": "用户在下拉筛选器中选择，未选择时不传该字段"
        },
        { "field": "keyword", "source": "用户在顶部搜索框输入" }
      ],
      "response_fields": [
        {
          "field": "data.list",
          "description": "订单列表，用于渲染表格行",
          "sub_fields": [
            {
              "field": "orderNo",
              "ui_usage": "显示在表格第一列，可点击跳转到详情",
              "enums": null,
              "fallback": "显示原始字符串，若为空则显示 '--'"
            },
            {
              "field": "status",
              "ui_usage": "显示在「状态」列，以不同颜色标签区分",
              "enums": { "0": "待审核", "1": "已通过", "2": "已拒绝" },
              "fallback": "不下发时不显示标签，该列留空"
            },
            {
              "field": "amount",
              "ui_usage": "显示在「金额」列，保留两位小数",
              "enums": null,
              "fallback": "值为 0 时显示 '¥0.00'，不下发时显示 '--'"
            }
          ]
        },
        {
          "field": "data.total",
          "ui_usage": "用于分页组件展示总条数和计算总页数",
          "enums": null,
          "fallback": "若不下发，分页组件隐藏总条数"
        }
      ],
      "caching": null,
      "depends_on": null
    }
  ],
  "cache_and_polling": {
    "token": "Token 缓存在 localStorage，每次请求由 HTTP 拦截器自动附加到 Authorization 请求头",
    "cached_data": [
      "下拉选项接口 /api/dict/order-status 的数据缓存在 Vuex Store，页面打开时请求一次，切换页面不重新请求"
    ],
    "polling": null,
    "dedup": "提交按钮点击后立即 disabled，防止重复提交"
  },
  "sequence_data": {
    "actors": [
      { "id": "user", "label": "用户" },
      { "id": "fe", "label": "前端" },
      { "id": "be", "label": "后端" }
    ],
    "steps": [
      { "from": "user", "to": "fe", "label": "访问订单列表页" },
      { "from": "fe", "to": "be", "label": "GET /api/user/permission" },
      { "from": "be", "to": "fe", "label": "返回权限数据..." },
      { "from": "fe", "to": "be", "label": "GET /api/dict/order-status" },
      { "from": "be", "to": "fe", "label": "返回下拉选项" },
      { "from": "fe", "to": "be", "label": "POST /api/order/list" },
      { "from": "be", "to": "fe", "label": "返回订单列表" },
      { "from": "fe", "to": "user", "label": "渲染列表页面" },
      { "from": "user", "to": "fe", "label": "点击某行「详情」" },
      { "from": "fe", "to": "be", "label": "GET /api/order/detail?id=123" },
      { "from": "be", "to": "fe", "label": "返回订单详情" },
      { "from": "fe", "to": "user", "label": "弹出详情抽屉" }
    ]
  }
}
```

## 报告规范

### 叙述风格

- **写给非前端开发阅读**（后端、测试、产品），避免以下内容：
  - ❌ 前端代码逻辑："在 useEffect 中 dispatch action，watch route.query 变化后调用 fetchData"
  - ❌ 前端状态变量："设置 loading = true，把 res.data 赋值给 tableData"
  - ❌ 技术实现细节："使用 axios 拦截器统一处理错误"
- ✅ 应该使用的表述：
  - "用户进入页面时自动加载"
  - "点击搜索按钮后触发"
  - "下拉选项数据来自 xxx 接口"
  - "翻页时用当前页码和筛选条件重新请求"

### 允许提及的前端策略

以下前端本地逻辑可以也应该在报告中体现，因为它们影响后端的行为和测试：

- 数据缓存时长（如"下拉选项缓存 5 分钟，期间不重复请求"）
- Token 缓存与过期策略
- 轮询间隔和条件
- 去重/防抖策略（如"搜索框输入后 300ms 防抖再请求"）
- 空值兜底策略

### 排序规则

接口按以下优先级排序：

1. 页面生命周期顺序（进入 → 交互 → 离开）
2. 同阶段内按接口依赖顺序（先请求的排在前面）
3. 独立的并发请求可并列，但按请求触发时机大致排序

### 时序图规范

- **HTML 格式**：在报告底部嵌入 **SVG** 时序图，用报告的脚本自动从 `sequence_data` 生成
- **Markdown 格式**：在报告底部插入 **Mermaid** `sequenceDiagram` 代码块

## 注意事项

- **只分析当前页面**，不要递归分析路由跳转后的目标页面（除非目标页是当前页的子路由/弹窗/抽屉）
- **不要分析 node_modules** 中的第三方库
- 如果接口调用封装在项目级公共函数中（如 `@/api/order.ts`），追踪到该文件解析实际接口路径
- 接口路径中的动态参数（如 `/api/order/:id`）保留占位符形式
- 如果某个信息无法从代码中确定，标注"未找到"而不是猜测
- 页面级子组件是（相对于入口文件的）相对路径导入的组件，项目级公共组件是别名路径（如 `@/components`）导入的——后者只追溯到公共组件文件，不展开其内部依赖
