# Bear Automation 安装指南

## 前置要求

1. **Bear App**: 确保已安装 Bear 应用
   - macOS: [从 Mac App Store 下载](https://apps.apple.com/app/bear/id1091189122)
   - iOS: [从 App Store 下载](https://apps.apple.com/app/bear/id1016366447)

2. **Python 3**: 用于运行 Python 脚本（macOS 通常已预装）
   ```bash
   python3 --version
   ```

3. **Bash**: 用于运行 Shell 脚本（macOS 默认已安装）

## 安装步骤

### 方法 1: 直接使用（推荐）

技能已经创建在 `skills/bear-automation` 目录中，可以直接使用：

```bash
cd /Users/run/Documents/Code/playroom/skills/bear-automation

# 测试 Python 脚本
python3 scripts/bear_helper.py --help

# 加载 Shell 函数
source scripts/bear_helper.sh
```

### 方法 2: 添加到 PATH

将脚本添加到系统 PATH，方便全局访问：

```bash
# 添加到 ~/.zshrc 或 ~/.bashrc
echo 'export PATH="$PATH:/Users/run/Documents/Code/playroom/skills/bear-automation/scripts"' >> ~/.zshrc

# 重新加载配置
source ~/.zshrc

# 现在可以直接使用
bear_helper.py --help
```

### 方法 3: 创建别名

在 shell 配置文件中创建别名：

```bash
# 添加到 ~/.zshrc 或 ~/.bashrc
echo 'alias bear-create="python3 /Users/run/Documents/Code/playroom/skills/bear-automation/scripts/bear_helper.py create"' >> ~/.zshrc
echo 'alias bear-search="python3 /Users/run/Documents/Code/playroom/skills/bear-automation/scripts/bear_helper.py search"' >> ~/.zshrc

# 重新加载
source ~/.zshrc

# 使用别名
bear-create --title "Test" --text "Hello"
```

## 验证安装

运行测试脚本验证功能：

```bash
cd /Users/run/Documents/Code/playroom/skills/bear-automation
python3 scripts/test_bear_helper.py
```

如果看到 "✓ All tests passed!"，说明安装成功。

## 快速开始

### 使用 Python 脚本

```bash
# 创建笔记
python3 scripts/bear_helper.py create \
  --title "My First Note" \
  --text "This is my first automated note" \
  --tags "test,automation"

# 搜索笔记
python3 scripts/bear_helper.py search --term "first" --tag "test"

# 打开笔记
python3 scripts/bear_helper.py open --title "My First Note"
```

### 使用 Shell 函数

```bash
# 加载函数
source scripts/bear_helper.sh

# 创建笔记
bear_create --title "Quick Note" --text "Content here" --tags "quick"

# 快速捕获剪贴板
echo "Important info" | pbcopy
bear_capture_clipboard "inbox"

# 创建每日日志
bear_daily_journal
```

### 运行示例

```bash
# 运行交互式示例
./scripts/examples.sh
```

## 在 Claude Code 中使用

当你在 Claude Code 中提到 Bear 相关的任务时，这个技能会自动触发。例如：

- "帮我在 Bear 中创建一个会议笔记"
- "搜索 Bear 中标签为 work 的笔记"
- "生成一个 Bear URL 来添加内容到我的日志"
- "写一个脚本每天自动创建日志笔记"

Claude 会使用这个技能来生成正确的 x-callback-url 和脚本。

## 集成到其他工具

### Alfred Workflow

1. 创建新的 Workflow
2. 添加 Script Filter
3. 使用提供的脚本：

```bash
source /Users/run/Documents/Code/playroom/skills/bear-automation/scripts/bear_helper.sh
bear_create --text "{query}" --tags "alfred"
```

### Keyboard Maestro

1. 创建新的 Macro
2. 添加 "Execute Shell Script" 动作
3. 使用：

```bash
source /Users/run/Documents/Code/playroom/skills/bear-automation/scripts/bear_helper.sh
bear_capture_clipboard "quick-capture"
```

### Shortcuts (iOS/macOS)

1. 创建新的 Shortcut
2. 添加 "Run Shell Script" 动作（macOS）或 "Open URL" 动作（iOS）
3. 使用生成的 bear:// URL

## 故障排除

### Bear 未打开

确保 Bear 已安装并可以通过命令行打开：

```bash
open -Ra "Bear"
```

### 权限问题

确保脚本有执行权限：

```bash
chmod +x scripts/*.sh
chmod +x scripts/*.py
```

### URL 编码问题

如果 URL 不工作，检查特殊字符是否正确编码：

```bash
# 测试编码
python3 -c "import urllib.parse; print(urllib.parse.quote('Hello World!'))"
```

### Python 模块问题

确保使用 Python 3：

```bash
python3 --version  # 应该显示 3.x.x
```

## 卸载

如果需要移除技能：

```bash
# 删除技能目录
rm -rf /Users/run/Documents/Code/playroom/skills/bear-automation

# 从 shell 配置中移除相关配置
# 编辑 ~/.zshrc 或 ~/.bashrc，删除相关的 export 和 alias 行
```

## 获取帮助

- 查看 [README.md](README.md) 了解功能概述
- 查看 [references/examples.md](references/examples.md) 获取详细示例
- 查看 [SKILL.md](SKILL.md) 了解完整 API 文档
- 运行 `source scripts/bear_helper.sh && show_help` 查看命令帮助

## 更新

要更新技能，只需重新运行安装步骤或使用 git pull（如果使用版本控制）。

## 贡献

欢迎提交改进建议和 bug 报告！
