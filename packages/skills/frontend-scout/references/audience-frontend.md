# 面向前端的报告侧重

确定受众为前端开发时，按以下结构组织报告内容：

## 页面组件树
用 markdown 代码块画出组件层级结构，以单文件组件 / render 函数为粒度：

```
src/pages/
├── ListPage/index.vue
│   ├── components/SearchBar.vue        -- 搜索筛选区域
│   ├── components/OrderTable.vue       -- 订单列表表格
│   │   └── components/TableRow.vue     -- 单行数据
│   │       ├── components/StatusTag.vue    -- 状态标签
│   │       └── components/ActionButtons.vue -- 操作按钮
```

## 每个组件分子章节

章节名用 markdown link 指向组件相对路径，方便点击跳转代码查看。内容包含：

- **组件功能**：简短的业务功能描述
- **Props / render 入参**：字段名、类型、取值逻辑（从哪来、什么情况下传入什么值）
- **事件 / render 回调**：触发时机、携带参数
- **展示条件**：条件渲染逻辑（如 v-if、visible 判断），用大白话描述
- **依赖接口**：该组件内直接调用的后端接口（有则列出，无则写"无直接接口依赖"）

### 示例

```
### [OrderTable](src/pages/ListPage/components/OrderTable.vue)

- **功能**：订单列表主体表格，展示订单数据行
- **Props**：
  - dataSource（数组）：订单列表数据，来自页面列表接口返回的 data.list
  - loading（布尔）：表格加载状态，接口请求中为 true
  - pageSize（数字）：每页条数，固定值 20
- **事件**：
  - onRowClick（rowData）：用户点击某行时触发，携带该行数据，用于打开详情抽屉
  - onPageChange（pageNum）：翻页时触发，父组件重新请求列表接口
- **展示条件**：始终渲染，无数据时显示空状态占位
- **依赖接口**：无直接接口调用，数据由父组件传入
```

### 示例 — 内部直接调接口的组件

```
### [StatusTag](src/pages/ListPage/components/TableRow/components/StatusTag.vue)

- **功能**：根据订单状态显示对应颜色的标签
- **Props**：
  - status（数字）：订单状态码，取值 0=待审核 1=已通过 2=已拒绝
- **事件**：无
- **展示条件**：status 有值且不为空时渲染
- **依赖接口**：无直接接口依赖
```
