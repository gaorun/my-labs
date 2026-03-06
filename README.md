# Claude Code Skills

一个开源的 Claude Code 技能集合仓库，提供各种自动化和集成工具。

## 📚 技能列表

### [Bear Automation](./bear-automation)

自动化 Bear 笔记应用的技能，使用 x-callback-url 协议实现笔记的创建、编辑、搜索和管理。

**功能特性**：

- 创建和编辑笔记（支持文本、剪贴板、HTML 转换）
- 搜索和打开笔记
- 标签管理（创建、重命名、删除、获取列表）
- 从网页抓取内容创建笔记
- Token 认证支持
- Python 和 Shell 脚本支持

**快速开始**：

```bash
# 使用 Python
python3 bear-automation/scripts/bear_helper.py create --title "测试" --text "内容"

# 使用 Shell
source bear-automation/scripts/bear_helper.sh
bear_create --title "测试" --text "内容"
```

[查看完整文档](./bear-automation/README.md)

## 🚀 使用方法

### 安装技能

1. 克隆仓库：

```bash
git clone https://github.com/YOUR_USERNAME/skills.git
cd skills
```

2. 选择需要的技能并查看其文档：

```bash
cd bear-automation
cat README.md
```

3. 按照技能文档的说明使用

### 在 Claude Code 中使用

当你在 Claude Code 中提到相关任务时，对应的技能会自动触发。例如：

- "帮我在 Bear 中创建一个笔记" → 触发 bear-automation 技能
- "生成一个 Bear URL 来添加内容" → 触发 bear-automation 技能

## 📖 技能结构

每个技能目录包含：

```
skill-name/
├── SKILL.md              # 技能主文档（Claude 使用）
├── README.md             # 用户文档
├── scripts/              # 辅助脚本
│   ├── *.py             # Python 脚本
│   └── *.sh             # Shell 脚本
└── references/           # 参考文档和示例
    └── examples.md
```

## 🤝 贡献

欢迎贡献新的技能或改进现有技能！

### 贡献新技能

1. Fork 本仓库
2. 创建技能目录：`mkdir your-skill-name`
3. 添加必需文件：
   - `SKILL.md` - 技能主文档
   - `README.md` - 用户文档
4. 提交 Pull Request

### 技能开发指南

**SKILL.md 格式**：

```markdown
---
name: skill-name
description: 技能描述，包含触发条件和使用场景
---

# 技能名称

技能的详细说明和使用方法...
```

**最佳实践**：

- 提供清晰的使用示例
- 包含错误处理说明
- 添加测试脚本
- 编写详细的文档

## 📋 技能开发规范

1. **命名规范**：使用小写字母和连字符（如 `bear-automation`）
2. **文档完整**：必须包含 SKILL.md 和 README.md
3. **代码质量**：提供测试脚本验证功能
4. **示例丰富**：包含实际使用场景的示例
5. **依赖说明**：明确列出所有依赖项

## 🔧 技能要求

### 必需文件

- `SKILL.md` - Claude Code 使用的主文档
- `README.md` - 用户文档

### 推荐文件

- `scripts/` - 辅助脚本目录
- `references/` - 参考文档目录

### 可选文件

- `tests/` - 测试脚本
- `examples/` - 示例代码
- `.gitignore` - Git 忽略文件

## 📄 许可证

本仓库采用 MIT 许可证。每个技能可能有自己的许可证，请查看具体技能目录。

## 🙏 致谢

感谢所有贡献者的付出！

## 📮 联系方式

- 提交 Issue：[GitHub Issues](https://github.com/gaorun/skills/issues)
- 讨论：[GitHub Discussions](https://github.com/gaorun/skills/discussions)

## 🌟 Star History

如果这个项目对你有帮助，请给个 Star ⭐️

---

**注意**：本仓库中的技能仅供学习和参考使用，请遵守相关应用的使用条款。
