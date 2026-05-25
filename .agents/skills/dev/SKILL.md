---
name: dev
description: >-
  my-labs 仓库开发指南。当用户说"加个 skill"、"新增命令"、"这个项目怎么构建"、
  "目录结构是什么"、"怎么跑起来"、"加个功能"、"改一下 CLI"时要触发。
  涵盖 monorepo 工作流、Skill/CLI/Extension 的选择决策、TypeScript 规范、构建流程。
  在 my-labs 仓库中做任何代码变更前先读此技能。
---

# my-labs 开发指南

> 项目总体规划见 `AGENTS.md`。本技能聚焦**具体操作**，AGENTS.md 聚焦**架构决策**。

## 快速启动

```bash
pnpm install   # 安装所有依赖
pnpm build     # 构建所有包（Turborepo 自动处理依赖顺序）
pnpm test      # 运行所有测试
```

> **为什么要先 build？** Turborepo 的 `test` 和 `lint` 任务依赖 `^build`（上游包先构建），
> 所以 `pnpm test` 会自动触发必要的构建。但首次克隆后建议显式 `pnpm build` 确保一切就绪。

## 三层产出：什么时候建什么

my-labs 有三种产出类型，选择逻辑如下：

| 场景                                         | 建什么        | 位置                          |
| -------------------------------------------- | ------------- | ----------------------------- |
| Agent 需要领域知识/工作流指导（纯 Markdown） | **Skill**     | `packages/skills/<name>/`     |
| 需要命令行交互、脚本化操作                   | **CLI 命令**  | `packages/cli/src/commands/`  |
| 编辑器 UI 扩展（VS Code / Raycast）          | **Extension** | `packages/extensions/<name>/` |

简单口诀：**首选 Skill**（零构建成本，git 即分发），Skill 不够用时加 CLI 命令，编辑器交互才建 Extension。

## 新增 Skill

在 `packages/skills/<name>/` 下创建 `SKILL.md` 即可，无需构建。

命名规则：目录名 = `name` 字段，全小写 + 连字符（如 `my-skill-name`）。

**SKILL.md 模板：**

```markdown
---
name: my-skill
description: 清晰的触发描述——这是 Agent 决定是否调用此技能的唯一依据
---

# Skill 标题

写给 Agent 的指令...
```

目录可包含辅助资源（模板、脚本等），在 SKILL.md 中通过相对路径引用：

```
packages/skills/my-skill/
├── SKILL.md
├── templates/      # 代码模板
└── references/     # 参考文档（Agent 按需加载）
```

> 详细 Skill 编写规范见 `@skill-creator` 技能。

## 新增 CLI 命令

CLI 基于 [oclif v4](https://oclif.io/)，源文件在 `packages/cli/src/commands/`。

### 实现步骤

1. 创建 Command 类：

```typescript
// packages/cli/src/commands/<name>.ts
import { Command } from "@oclif/core";

export default class MyCommand extends Command {
  static description = "命令描述";

  async run(): Promise<void> {
    this.log("Hello from my-cli!");
  }
}
```

2. 验证命令已注册：

```bash
cd packages/cli
pnpm build
node bin/run.js my-command --help
```

### 命名映射

- 文件名即命令名：`hello.ts` → `my-cli hello`
- 子目录映射为子命令：`admin/status.ts` → `my-cli admin status`

### 关键约定

- 模块系统：ESM（`"type": "module"`），输出到 `dist/`
- `tsconfig.json` 必须 `extends` 自 `../../tsconfig.base.json`
- 命令描述用 `static description`（oclif 自动生成 help）

## TypeScript 规范

根目录 `tsconfig.base.json` 已设定共享基线。各包子目录的 `tsconfig.json` 只需：

```json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src"]
}
```

核心约束：

- 目标 ES2022，严格模式开启
- CLI 使用 `"module": "NodeNext"`，其他包使用 `"module": "ESNext"`
- 每个包独立编译，通过 Turborepo 编排依赖顺序

## 构建流水线

Turborepo 任务依赖（定义在 `turbo.json`）：

| 任务    | 依赖     | 说明                     |
| ------- | -------- | ------------------------ |
| `build` | `^build` | 先构建依赖包，再构建自身 |
| `lint`  | `^build` | 依赖包构建后执行         |
| `test`  | `^build` | 依赖包构建后执行         |
| `dev`   | 无       | 无缓存，持续运行         |
| `clean` | 无       | 无缓存                   |

## 新增 Extension

在 `packages/extensions/<name>/` 下创建新包，确保：

- `package.json` 中 `name` 以 `@gaorun/` 开头
- 遵循上述 TypeScript 规范

## 修改后必做事项

1. **更新 AGENTS.md** — 第 7 节「已有 Skill 清单」和第 8 节「迭代记录」
2. **更新 README.md** — 用户文档同步变更
3. **运行完整构建** — `pnpm build && pnpm test`

> 测试相关细节见 `@test` 技能，发布细节见 `@deploy` 技能。
