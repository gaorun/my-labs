# Bear Automation Skill

自动化 Bear 笔记应用的技能，使用 x-callback-url 协议实现笔记的创建、编辑、搜索和管理。

## 功能特性

- ✅ 创建和编辑笔记（支持文本、剪贴板、HTML 转换）
- ✅ 搜索和打开笔记
- ✅ 标签管理（创建、重命名、删除、获取列表）
- ✅ 归档和删除笔记
- ✅ 从网页抓取内容创建笔记
- ✅ Token 认证支持（获取选中笔记、标签列表等）
- ✅ 生成可执行的 URL scheme 和脚本
- ✅ 与其他自动化工具集成（Shortcuts、Drafts、Alfred 等）

## 快速开始

### 基本使用

创建一个简单的笔记：

```bash
open "bear://x-callback-url/create?title=Hello&text=World&tags=test"
```

### 使用 Python 脚本

```bash
# 创建笔记
./scripts/bear_helper.py create --title "Meeting Notes" --text "Discussed project timeline" --tags "work,meetings"

# 搜索笔记
./scripts/bear_helper.py search --term "meeting" --tag "work"

# 打开笔记
./scripts/bear_helper.py open --title "Project Plan"
```

### 使用 Shell 脚本

```bash
# 加载辅助函数
source scripts/bear_helper.sh

# 创建笔记
bear_create --title "Todo List" --text "- Task 1\n- Task 2" --tags "todos"

# 添加内容到现有笔记
bear_add_text --title "Daily Log" --text "Completed task X" --mode append

# 快速捕获剪贴板内容
bear_capture_clipboard "inbox"

# 创建每日日志
bear_daily_journal
```

## 目录结构

```
bear-automation/
├── SKILL.md                    # 技能主文档
├── README.md                   # 本文件
├── scripts/
│   ├── bear_helper.py         # Python 辅助脚本
│   └── bear_helper.sh         # Shell 辅助脚本
└── references/
    └── examples.md            # 详细示例和最佳实践
```

## 核心功能

### 1. 笔记创建

```bash
# 基本创建
bear_create --text "Note content"

# 带标题和标签
bear_create --title "Meeting Notes" --text "Content" --tags "work,meetings"

# 创建并打开编辑器
bear_create --title "Draft" --text "Start here" --edit --open
```

### 2. 内容添加

```bash
# 追加到笔记末尾
bear_add_text --title "Log" --text "New entry" --mode append

# 添加到笔记开头
bear_add_text --title "Todo" --text "Urgent task" --mode prepend

# 替换笔记内容
bear_add_text --id "NOTE-ID" --text "New content" --mode replace
```

### 3. 搜索和打开

```bash
# 搜索笔记
bear_search --term "project" --tag "active"

# 打开特定笔记
bear_open --title "Project Plan"

# 打开笔记并跳转到标题
bear_open --title "Documentation" --header "Installation"
```

### 4. 标签管理

```bash
# 打开标签集合
bear_open_tag "work"

# 重命名标签
bear_rename_tag "old-name" "new-name"

# 删除标签
bear_delete_tag "obsolete"
```

### 5. 特殊集合

```bash
# 显示未标记的笔记
bear_untagged

# 显示今天修改的笔记
bear_today

# 显示包含待办事项的笔记
bear_todo

# 显示已锁定的笔记
bear_locked
```

### 6. 网页内容抓取

```bash
# 从网页创建笔记
bear_grab_url "https://example.com/article" "reading,articles" "yes"

# 获取所有标签（需要 token）
bear_get_tags "YOUR_TOKEN"
```

### 7. Token 认证

某些高级功能需要 Bear API Token：

```bash
# 生成 Token：Bear → Help → API Token

# 使用 token 获取标签列表
bear_get_tags "YOUR_TOKEN"

# 使用当前选中的笔记（需要在 API 调用中添加 selected=yes&token=YOUR_TOKEN）
```

## 工作流示例

### 每日日志

```bash
#!/bin/bash
DATE=$(date +"%Y-%m-%d")
TITLE="Journal - $DATE"
TEXT="# Daily Journal\n\n## Morning\n\n## Afternoon\n\n## Evening\n\n"

open "bear://x-callback-url/create?title=$(urlencode "$TITLE")&text=$(urlencode "$TEXT")&tags=journal&edit=yes"
```

### 会议笔记模板

```bash
#!/bin/bash
MEETING="$1"
TEXT="# $MEETING\n\n**Date:** $(date +"%Y-%m-%d")\n\n## Agenda\n\n## Discussion\n\n## Action Items\n\n"

open "bear://x-callback-url/create?title=$(urlencode "$MEETING")&text=$(urlencode "$TEXT")&tags=meetings"
```

### 快速捕获

```bash
#!/bin/bash
# 从剪贴板捕获内容到 Bear
CONTENT=$(pbpaste)
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")
TEXT="[$TIMESTAMP]\n\n$CONTENT"

open "bear://x-callback-url/create?text=$(urlencode "$TEXT")&tags=inbox"
```

## 集成示例

### Alfred Workflow

```bash
query="{query}"
open "bear://x-callback-url/create?text=$(urlencode "$query")&tags=quick"
```

### Shortcuts (iOS/macOS)

1. 获取输入文本
2. URL 编码
3. 打开 URL: `bear://x-callback-url/create?text=[编码后的文本]&tags=shortcuts`

### Drafts

```javascript
const title = draft.title;
const content = draft.content;
const url = `bear://x-callback-url/create?title=${encodeURIComponent(title)}&text=${encodeURIComponent(content)}`;
app.openURL(url);
```

## API 参考

### 主要 Actions

| Action | 描述 | 必需参数 |
|--------|------|----------|
| `create` | 创建新笔记 | `text` 或 `clipboard` |
| `add-text` | 添加文本到笔记 | `text` 或 `clipboard` |
| `add-file` | 添加文件到笔记 | `file`, `filename` |
| `open-note` | 打开笔记 | `title` 或 `id` |
| `search` | 搜索笔记 | `term` 或 `tag` |
| `open-tag` | 打开标签集合 | `name` |
| `rename-tag` | 重命名标签 | `name`, `new_name` |
| `delete-tag` | 删除标签 | `name` |
| `trash` | 移动到废纸篓 | `id` 或 `search` |
| `archive` | 归档笔记 | `id` 或 `search` |
| `grab-url` | 从网页创建笔记 | `url` |
| `tags` | 获取所有标签 | `token` |

### 常用参数

| 参数 | 类型 | 描述 |
|------|------|------|
| `title` | string | 笔记标题 |
| `text` | string | 笔记内容（支持 Markdown） |
| `clipboard` | yes/no | 使用剪贴板内容 |
| `tags` | string | 逗号分隔的标签 |
| `id` | string | 笔记唯一标识符 |
| `file` | string | Base64 编码的文件内容 |
| `filename` | string | 文件名（与 file 一起使用） |
| `mode` | string | 添加模式：append, prepend, replace, replace_all |
| `header` | string | 在指定标题下添加内容 |
| `selected` | yes/no | 使用当前选中的笔记（需要 token） |
| `pin` | yes/no | 是否置顶 |
| `open_note` | yes/no | 是否打开笔记 |
| `new_window` | yes/no | 在新窗口打开（Mac） |
| `float` | yes/no | 浮动窗口（Mac） |
| `edit` | yes/no | 是否进入编辑模式 |
| `timestamp` | yes/no | 是否添加时间戳 |
| `type` | html | 将 HTML 转换为 Markdown |
| `url` | string | 网页 URL 或图片链接基础 URL |
| `token` | string | API Token（某些功能需要） |

## 最佳实践

1. **始终进行 URL 编码**：使用提供的编码函数避免格式错误
2. **优先使用笔记 ID**：比标题更可靠
3. **批量操作添加延迟**：操作之间间隔 1-2 秒
4. **实现错误处理**：使用 x-error 回调
5. **保持标签一致性**：建立标签命名规范
6. **定期备份**：批量操作前导出笔记

## 故障排除

### URL 不工作

检查 URL 编码，特别是特殊字符：
```bash
# 测试编码
python3 -c "import urllib.parse; print(urllib.parse.quote('Hello World!'))"
```

### 找不到笔记

- 验证标题完全匹配（区分大小写）
- 或使用笔记 ID 代替标题

### Bear 未打开

确保 Bear 应用已安装：
```bash
open -Ra "Bear"
```

## 更多资源

- [详细示例](references/examples.md) - 更多工作流和集成示例
- [Bear 官方文档](https://bear.app/faq/x-callback-url-scheme-documentation/)
- [x-callback-url 规范](http://x-callback-url.com/)

## 许可证

本技能遵循 MIT 许可证。

## 贡献

欢迎提交问题和改进建议！
