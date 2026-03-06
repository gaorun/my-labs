# Bear Automation - 快速参考

## 常用命令

### Python 脚本

```bash
# 创建笔记
python3 scripts/bear_helper.py create --title "标题" --text "内容" --tags "标签1,标签2"

# 添加文本
python3 scripts/bear_helper.py add-text --title "标题" --text "内容" --mode append

# 搜索
python3 scripts/bear_helper.py search --term "关键词" --tag "标签"

# 打开笔记
python3 scripts/bear_helper.py open --title "标题"

# 打开标签
python3 scripts/bear_helper.py open-tag "标签名"
```

### Shell 函数

```bash
# 加载函数
source scripts/bear_helper.sh

# 创建笔记
bear_create --title "标题" --text "内容" --tags "标签"

# 添加文本
bear_add_text --title "标题" --text "内容" --mode append

# 搜索
bear_search --term "关键词" --tag "标签"

# 打开笔记
bear_open --title "标题"

# 打开标签
bear_open_tag "标签名"

# 快速捕获剪贴板
bear_capture_clipboard "inbox"

# 每日日志
bear_daily_journal

# 添加日志条目
bear_log_entry "日志内容"

# 特殊集合
bear_untagged  # 未标记的笔记
bear_today     # 今天的笔记
bear_todo      # 待办事项
bear_locked    # 已锁定的笔记
```

## URL Scheme 格式

```
bear://x-callback-url/[action]?[parameters]
```

### 常用 Actions

| Action | 用途 | 示例 |
|--------|------|------|
| `create` | 创建笔记 | `bear://x-callback-url/create?text=Hello` |
| `add-text` | 添加文本 | `bear://x-callback-url/add-text?title=Log&text=Entry` |
| `open-note` | 打开笔记 | `bear://x-callback-url/open-note?title=Notes` |
| `search` | 搜索 | `bear://x-callback-url/search?term=meeting` |
| `open-tag` | 打开标签 | `bear://x-callback-url/open-tag?name=work` |
| `grab-url` | 抓取网页 | `bear://x-callback-url/grab-url?url=https://example.com` |
| `tags` | 获取标签 | `bear://x-callback-url/tags?token=YOUR_TOKEN` |

### 常用参数

| 参数 | 说明 | 值 |
|------|------|-----|
| `title` | 笔记标题 | 字符串 |
| `text` | 笔记内容 | 字符串（支持 Markdown） |
| `clipboard` | 使用剪贴板 | `yes`, `no` |
| `tags` | 标签 | 逗号分隔，如 `work,project` |
| `file` | 文件内容 | Base64 编码 |
| `filename` | 文件名 | 带扩展名的文件名 |
| `mode` | 添加模式 | `append`, `prepend`, `replace`, `replace_all` |
| `header` | 标题位置 | 笔记中的标题名称 |
| `selected` | 选中笔记 | `yes`（需要 token） |
| `pin` | 置顶 | `yes`, `no` |
| `open_note` | 打开笔记 | `yes`, `no` |
| `new_window` | 新窗口 | `yes`, `no` (Mac) |
| `float` | 浮动窗口 | `yes`, `no` (Mac) |
| `edit` | 编辑模式 | `yes`, `no` |
| `timestamp` | 时间戳 | `yes`, `no` |
| `type` | 内容类型 | `html`（转换为 Markdown） |
| `url` | 网页 URL | 完整 URL |
| `token` | API Token | 从 Bear 生成的 token |

## 快速工作流

### 1. 每日日志
```bash
source scripts/bear_helper.sh
bear_daily_journal
```

### 2. 快速捕获
```bash
echo "重要信息" | pbcopy
source scripts/bear_helper.sh
bear_capture_clipboard "inbox"
```

### 3. 会议笔记
```bash
source scripts/bear_helper.sh
bear_create --title "团队会议 $(date +%Y-%m-%d)" \
  --text "# 会议笔记\n\n## 议程\n\n## 讨论\n\n## 行动项\n\n" \
  --tags "meetings,work" --edit --open
```

### 4. 添加日志条目
```bash
source scripts/bear_helper.sh
bear_log_entry "完成了项目 X 的开发"
```

### 5. 搜索和打开
```bash
source scripts/bear_helper.sh
bear_search --term "项目" --tag "work"
```

## URL 编码

特殊字符需要编码：

| 字符 | 编码 |
|------|------|
| 空格 | `%20` 或 `+` |
| 换行 | `%0A` |
| `#` | `%23` |
| `&` | `%26` |
| `=` | `%3D` |
| `,` | `%2C` |

使用函数自动编码：
```bash
urlencode "Hello World!"
```

## 测试和调试

```bash
# 运行测试
python3 scripts/test_bear_helper.py

# 运行示例
./scripts/examples.sh

# 调试 URL
python3 -c "import urllib.parse; print(urllib.parse.quote('你的文本'))"
```

## 文件位置

- **主文档**: `SKILL.md`
- **使用说明**: `README.md`
- **安装指南**: `INSTALL.md`
- **详细示例**: `references/examples.md`
- **Python 脚本**: `scripts/bear_helper.py`
- **Shell 脚本**: `scripts/bear_helper.sh`
- **测试脚本**: `scripts/test_bear_helper.py`
- **示例脚本**: `scripts/examples.sh`

## 获取帮助

```bash
# Python 帮助
python3 scripts/bear_helper.py --help

# Shell 帮助
source scripts/bear_helper.sh
show_help
```

## 常见问题

**Q: Bear 没有打开？**
```bash
open -Ra "Bear"  # 检查 Bear 是否已安装
```

**Q: URL 不工作？**
- 检查 URL 编码
- 验证参数名称
- 确保 Bear 已安装

**Q: 找不到笔记？**
- 标题区分大小写
- 使用笔记 ID 更可靠
- 检查笔记是否在废纸篓

## 资源链接

- [Bear 官方文档](https://bear.app/faq/x-callback-url-scheme-documentation/)
- [x-callback-url 规范](http://x-callback-url.com/)
