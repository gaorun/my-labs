# my-labs

个人提效工具集 — Agent Skills · CLI · Extensions

## 快速开始

### 安装所有 Agent Skills

```bash
# 方式一：直接安装
npx skills add git@github.com:gaorun/my-labs.git

# 方式二：用元 CLI 一键安装
npx @gaorun/my-cli install
```

### 安装 CLI 工具

```bash
npm install -g @gaorun/fe-project-report
npm install -g @gaorun/page-api-report
```

## 项目结构

```
my-labs/
├── packages/
│   ├── skills/          # 纯 Agent Skills
│   ├── cli/             # CLI 工具（每个可附带同名 Skill）
│   └── extensions/      # 编辑器扩展
├── skills/              # 聚合产物：所有 Skill（供 git 读取）
└── scripts/             # 构建脚本
```

## Skill 一览

| Skill                | 说明                                             |
| -------------------- | ------------------------------------------------ |
| `fe-project-report`  | 前端项目探索与报告生成（HTML / Markdown / JSON） |
| `page-api-report`    | 页面接口发现报告                                 |
| `name-it-to-tame-it` | 命名降维法 — 给内耗、焦虑起外号                  |
| `obsidian-memo`      | Obsidian AI 协作记忆管理                         |
| `raycast-developers` | Raycast 扩展开发参考                             |
| `vertical-codebase`  | 按功能域组织代码的架构建议                       |
| `workplace-writing`  | 职场写作教练（金字塔+SCQA）                      |
| `zed`                | Zed 编辑器 CLI 操作                              |

## 开发

```bash
pnpm install       # 安装依赖
pnpm build         # 构建所有包 + 聚合 skills
pnpm sync:skills   # 仅同步 skills
pnpm test          # 运行测试
```

## 开源协议

MIT
