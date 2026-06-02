# my-labs

个人提效工具集 monorepo — Agent Skills · CLI · Extensions

## 快速开始

### 安装所有 Agent Skills

```bash
# 方式一：直接用 skills CLI
npx skills add git@github.com:gaorun/my-labs.git

# 方式二：用元 CLI 一键安装
npx @gaorun/my-cli install
```

## 项目结构

```
my-labs/
├── packages/
│   ├── skills/          # Agent Skills（通过 git 分发）
│   ├── cli/             # CLI 工具（@gaorun/my-cli，基于 oclif）
│   └── extensions/      # 编辑器扩展（待添加）
├── .agents/skills/      # 项目级开发技能（dev / test / deploy）
├── AGENTS.md            # 项目总体规划
├── README.md            # 用户文档
├── turbo.json           # Turborepo 构建流水线
└── tsconfig.base.json   # 共享 TypeScript 配置
```

## Skills 清单

| Skill                | 说明                                                       |
| -------------------- | ---------------------------------------------------------- |
| `frontend-scout`     | 统一接口侦察 — 接口溯源/页面发现/项目摸底/PRD 变更影响分析 |
| `api-locator`        | 接口反向溯源（即将被 frontend-scout 替代）                 |
| `fe-project-report`  | 前端项目分析报告生成                                       |
| `page-api-report`    | 页面接口发现报告                                           |
| `name-it-to-tame-it` | 命名降维法 — 给焦虑起外号                                  |
| `obsidian-memo`      | Obsidian AI 协作记忆管理                                   |
| `raycast-developers` | Raycast 扩展开发参考                                       |
| `vertical-codebase`  | 按功能域组织代码的架构建议                                 |
| `workplace-writing`  | 职场写作教练                                               |
| `zed`                | Zed 编辑器 CLI 操作                                        |
| `mermaid-cli`        | Mermaid 图表渲染 CLI 使用指南                              |

## 开发

```bash
pnpm install   # 安装依赖
pnpm build     # 构建所有包
pnpm test      # 运行测试
pnpm clean     # 清理构建产物
```

> 项目贡献者请参考 `.agents/skills/` 下的 `dev`、`test`、`deploy` 技能。

## 开源协议

MIT
