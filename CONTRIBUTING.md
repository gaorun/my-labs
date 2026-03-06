# 贡献指南

感谢你对 Claude Code Skills 项目的关注！我们欢迎各种形式的贡献。

## 🤝 如何贡献

### 报告问题

如果你发现了 bug 或有功能建议：

1. 在 [Issues](https://github.com/YOUR_USERNAME/skills/issues) 中搜索是否已有相关问题
2. 如果没有，创建新的 Issue
3. 清晰描述问题或建议，包括：
   - 问题的复现步骤
   - 期望的行为
   - 实际的行为
   - 环境信息（操作系统、版本等）

### 贡献代码

#### 1. Fork 和 Clone

```bash
# Fork 仓库到你的账号
# 然后 clone 到本地
git clone https://github.com/YOUR_USERNAME/skills.git
cd skills
```

#### 2. 创建分支

```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/your-bug-fix
```

#### 3. 开发

- 遵循现有的代码风格
- 添加必要的测试
- 更新相关文档

#### 4. 提交

```bash
git add .
git commit -m "feat: 添加新功能描述"
# 或
git commit -m "fix: 修复问题描述"
```

提交信息格式：
- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 重构
- `test:` 测试相关
- `chore:` 构建/工具相关

#### 5. 推送和 PR

```bash
git push origin feature/your-feature-name
```

然后在 GitHub 上创建 Pull Request。

## 📝 贡献新技能

### 技能结构

```
your-skill-name/
├── SKILL.md              # 必需：技能主文档
├── README.md             # 必需：用户文档
├── scripts/              # 推荐：辅助脚本
│   ├── helper.py
│   └── helper.sh
├── references/           # 推荐：参考文档
│   └── examples.md
└── tests/               # 可选：测试脚本
    └── test_helper.py
```

### SKILL.md 模板

```markdown
---
name: your-skill-name
description: 简短描述技能功能和触发条件。包含关键词以便 Claude 识别何时使用此技能。
---

# 技能名称

技能的详细说明。

## When to Use This Skill

列出使用场景：
- 场景 1
- 场景 2

## 核心功能

### 功能 1

描述和示例...

### 功能 2

描述和示例...

## 使用示例

提供实际的使用示例...

## 最佳实践

列出使用建议...
```

### README.md 模板

```markdown
# 技能名称

简短描述。

## 功能特性

- 特性 1
- 特性 2

## 快速开始

\`\`\`bash
# 安装/使用示例
\`\`\`

## 详细文档

...

## 许可证

MIT
```

### 技能开发检查清单

- [ ] 创建技能目录
- [ ] 编写 SKILL.md（包含 YAML frontmatter）
- [ ] 编写 README.md
- [ ] 添加使用示例
- [ ] 编写辅助脚本（如果需要）
- [ ] 添加测试（如果适用）
- [ ] 更新根目录 README.md 的技能列表
- [ ] 测试技能功能
- [ ] 提交 Pull Request

## 🧪 测试

在提交 PR 前，请确保：

1. 所有脚本可以正常运行
2. 文档中的示例是正确的
3. 没有语法错误
4. 遵循项目的代码风格

如果技能包含脚本，建议添加测试：

```python
# tests/test_helper.py
def test_basic_functionality():
    # 测试代码
    assert True
```

## 📋 代码规范

### Python

- 使用 4 个空格缩进
- 遵循 PEP 8
- 添加类型提示
- 编写 docstring

### Shell

- 使用 2 个空格缩进
- 添加错误处理
- 使用有意义的变量名
- 添加注释说明

### 文档

- 使用清晰的标题结构
- 提供实际可运行的示例
- 包含错误处理说明
- 使用中文或英文（保持一致）

## 🎯 优先级

我们特别欢迎以下类型的贡献：

1. **新技能**：常用工具的自动化集成
2. **文档改进**：让文档更清晰易懂
3. **Bug 修复**：修复现有技能的问题
4. **测试**：增加测试覆盖率
5. **示例**：添加更多使用示例

## ❓ 问题

如果你在贡献过程中遇到问题：

1. 查看现有的 Issues 和 Discussions
2. 在 Discussions 中提问
3. 联系维护者

## 📜 行为准则

- 尊重所有贡献者
- 保持友好和专业
- 接受建设性的批评
- 关注项目的最佳利益

## 🙏 致谢

感谢你的贡献！每一个贡献都让这个项目变得更好。

---

再次感谢你的贡献！🎉
