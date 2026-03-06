# Bear Automation

自动化 Bear 笔记应用的 Claude Code 技能，使用 x-callback-url 协议。

## 功能特性

- ✅ 创建和编辑笔记（支持文本、剪贴板、HTML 转换）
- ✅ 搜索和打开笔记
- ✅ 标签管理（创建、重命名、删除、获取列表）
- ✅ 从网页抓取内容创建笔记
- ✅ Token 认证支持
- ✅ 完整的 16 个 x-callback-url actions

## 快速开始

### 在 Claude Code 中使用

当你在 Claude Code 中提到 Bear 相关任务时，技能会自动触发：

```
"帮我在 Bear 中创建一个笔记"
"生成一个 Bear URL 来添加内容到日志"
"搜索 Bear 中标签为 work 的笔记"
```

### 使用辅助脚本

#### Python

```bash
# 创建笔记
python3 scripts/bear_helper.py create --title "标题" --text "内容" --tags "tag1,tag2"

# 搜索笔记
python3 scripts/bear_helper.py search --term "关键词" --tag "标签"

# 打开笔记
python3 scripts/bear_helper.py open --title "笔记标题"
```

#### Shell

```bash
# 加载函数
source scripts/bear_helper.sh

# 创建笔记
bear_create --title "标题" --text "内容" --tags "tag1,tag2"

# 快速捕获剪贴板
bear_capture_clipboard "inbox"

# 每日日志
bear_daily_journal
```

## 核心 Actions

| Action | 描述 | 示例 |
|--------|------|------|
| `create` | 创建笔记 | `bear://x-callback-url/create?text=Hello` |
| `add-text` | 添加文本 | `bear://x-callback-url/add-text?title=Log&text=Entry` |
| `open-note` | 打开笔记 | `bear://x-callback-url/open-note?title=Notes` |
| `search` | 搜索 | `bear://x-callback-url/search?term=meeting` |
| `open-tag` | 打开标签 | `bear://x-callback-url/open-tag?name=work` |
| `grab-url` | 抓取网页 | `bear://x-callback-url/grab-url?url=https://example.com` |
| `tags` | 获取标签 | `bear://x-callback-url/tags?token=YOUR_TOKEN` |

[查看完整 API 文档](./SKILL.md)

## 常用参数

- `title` - 笔记标题
- `text` - 笔记内容（支持 Markdown）
- `tags` - 逗号分隔的标签
- `clipboard` - 使用剪贴板内容
- `mode` - 添加模式：`append`, `prepend`, `replace`, `replace_all`
- `token` - API Token（某些功能需要）

## Token 认证

某些高级功能需要 Bear API Token：

1. 打开 Bear → Help → API Token
2. 点击 Generate Token
3. 在 API 调用中使用 `token` 参数

## 安装

### 前置要求

- Bear App（[Mac](https://apps.apple.com/app/bear/id1091189122) / [iOS](https://apps.apple.com/app/bear/id1016366447)）
- Python 3（使用 Python 脚本）
- Bash/Zsh（使用 Shell 脚本）

### 使用脚本

```bash
# 克隆仓库
git clone <repository-url>
cd skills/bear-automation

# Python 脚本
python3 scripts/bear_helper.py --help

# Shell 脚本
source scripts/bear_helper.sh
show_help
```

## 示例

### 创建每日日志

```bash
source scripts/bear_helper.sh
bear_daily_journal
```

### 从网页创建笔记

```bash
python3 scripts/bear_helper.py grab-url "https://example.com/article" --tags "reading,articles"
```

### 快速捕获

```bash
echo "重要信息" | pbcopy
source scripts/bear_helper.sh
bear_capture_clipboard "inbox"
```

## 故障排除

### Bear 未打开

```bash
open -Ra "Bear"  # 检查 Bear 是否已安装
```

### URL 不工作

- 检查 URL 编码
- 验证参数名称
- 确保 Bear 已安装

## 文档

- [SKILL.md](./SKILL.md) - 完整的 API 文档和使用指南

## 许可证

MIT License

## 资源

- [Bear 官方文档](https://bear.app/faq/x-callback-url-scheme-documentation/)
- [x-callback-url 规范](http://x-callback-url.com/)
