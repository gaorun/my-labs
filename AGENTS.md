# AGENTS.md

> my-labs 项目总体规划与架构文档。
> **每次重大更新请同步此文件。**

---

## 1. 项目定位

**my-labs** 是个人提效工具集 monorepo，包含三类产出：

| 层级             | 说明                                                                              | 分发方式                                |
| ---------------- | --------------------------------------------------------------------------------- | --------------------------------------- |
| **Agent Skills** | AI Agent 技能（SKILL.md 格式），安装到 Claude Code / Cursor / Codex 等 Agent 环境 | `npx skills add <repo-url>` 从 git 读取 |
| **CLI**          | 命令行工具，部分 CLI 在构建时自动打包同名的 Agent Skill                           | npm publish (`@gaorun/*`)               |
| **Extensions**   | VS Code / Raycast 等编辑器扩展                                                    | npm publish (`@gaorun/*`)               |

## 2. 仓库信息

- **名称**: `my-labs`
- **GitHub**: `git@github.com:gaorun/my-labs.git`
- **包管理**: pnpm workspace
- **构建工具**: Turborepo
- **语言**: TypeScript 为主，Python 辅助脚本

## 3. 目录结构

```
my-labs/
├── package.json              # Root: workspace config + scripts
├── pnpm-workspace.yaml       # pnpm monorepo 配置
├── tsconfig.base.json        # 共享 TypeScript 配置
├── turbo.json                # Turborepo pipeline
├── AGENTS.md                 # ← 本文件：项目规划
├── README.md                 # 用户文档
├── .gitignore
├── LICENSE                   # MIT
│
├── packages/
│   ├── skills/               # 纯 Agent Skills（无 CLI 对应物）
│   │   ├── api-locator/
│   │   ├── fe-project-report/
│   │   ├── name-it-to-tame-it/
│   │   ├── obsidian-memo/
│   │   ├── page-api-report/
│   │   ├── raycast-developers/
│   │   ├── vertical-codebase/
│   │   ├── workplace-writing/
│   │   └── zed/
│   │
│   ├── cli/                  # CLI 工具（npm 包，@gaorun/* 发布，基于 oclif）
│   │   ├── package.json
│   │   ├── bin/
│   │   │   └── run.js
│   │   ├── src/
│   │   │   └── commands/
│   │   │       └── install.ts
│   │   └── tsconfig.json
│   │
│   └── extensions/           # 编辑器扩展（npm 包）
│       └── ...               # 待添加
```

## 4. 核心工作流

### 4.1 安装全部 Skill（用户视角）

```bash
# 方式一：直接用 skills CLI
npx skills add git@github.com:gaorun/my-labs.git

# 方式二：用本仓库的元 CLI（封装了方式一）
npx @gaorun/my-cli install
```

### 4.2 开发流程

```bash
# 安装依赖
pnpm install

# 构建所有包
pnpm build

# 运行测试
pnpm test

# 清理构建产物
pnpm clean
```

### 4.3 新增一个纯 Skill

在 `packages/skills/<name>/` 下创建 `SKILL.md` 即可。

### 4.4 给 CLI 增加命令

1. 在 `packages/cli/src/commands/<name>.ts` 下创建 oclif Command 子类
2. 构建：`cd packages/cli && pnpm build`
3. 发布：`cd packages/cli && npm publish`

### 4.5 发布到 npm

```bash
# 单个包
cd packages/cli
npm publish --access public

# 或使用 changesets 统一管理版本
pnpm changeset
pnpm changeset version
pnpm build
pnpm -r publish --access public
```

## 5. 设计原则

1. **Skill 是核心资产** — Agent Skill 统一存放在 `packages/skills/`，通过 git 分发。
2. **单一 CLI 入口** — `packages/cli/` 是基于 oclif 的唯一 CLI，所有命令在此扩展。
3. **一个命令搞定一切** — `pnpm build` 编译所有包。
4. **示例脱敏** — 所有 SKILL.md 中的示例数据（文件路径、接口名、业务名词、变量名、公司/产品名称等）必须使用通用占位名称，禁止出现任何真实项目的数据。公开仓库，避免泄露。

## 6. 技术栈

| 组件       | 技术            | 说明                        |
| ---------- | --------------- | --------------------------- |
| 包管理     | pnpm workspace  | monorepo 管理               |
| 构建编排   | Turborepo       | 并行构建 + 缓存             |
| 语言       | TypeScript 5.7+ | CLI 和工具脚本              |
| 运行时     | Node.js >= 18   | 运行环境                    |
| CLI 框架   | oclif           | my-cli 的命令行解析         |
| 版本管理   | Changesets      | （可选）统一管理多包版本    |
| Skill 格式 | SKILL.md        | Anthropic Agent Skills 规范 |

## 7. 已有 Skill 清单

| Skill                | 类型 | 说明                                             |
| -------------------- | ---- | ------------------------------------------------ |
| `name-it-to-tame-it` | Pure | 命名降维法 — 给焦虑起外号                        |
| `obsidian-memo`      | Pure | Obsidian AI 协作记忆管理                         |
| `raycast-developers` | Pure | Raycast 扩展开发参考                             |
| `vertical-codebase`  | Pure | 按功能域组织代码的架构建议                       |
| `workplace-writing`  | Pure | 职场写作教练（金字塔+SCQA）                      |
| `zed`                | Pure | Zed 编辑器 CLI 操作                              |
| `api-locator`        | Pure | 接口反向溯源 — 接口→页面/字段使用全貌            |
| `fe-project-report`  | Pure | 前端项目分析报告生成                             |
| `mermaid-cli`        | Pure | mermaid-cli (mmdc) Mermaid 图表渲染 CLI 使用指南 |
