---
name: dev
description: >-
  my-labs 仓库开发指南。当用户需要新增 Skill、新增 CLI 命令、修改代码、了解项目结构、
  或执行任何开发相关任务时触发。涵盖 monorepo 工作流、TypeScript 规范、构建流程等。
---

# my-labs 开发指南

my-labs 是一个基于 pnpm workspace + Turborepo 的 monorepo，包含三层产出：Agent Skills、CLI 工具、编辑器扩展。

## 项目结构

```
my-labs/
├── packages/
│   ├── skills/         # 纯 Agent Skills（每个子目录即一个 skill）
│   ├── cli/            # CLI 工具（@gaorun/my-cli，基于 oclif）
│   └── extensions/     # 编辑器扩展
├── tsconfig.base.json  # 共享 TypeScript 配置
├── turbo.json          # Turborepo 构建流水线
├── pnpm-workspace.yaml # workspace 配置
└── AGENTS.md           # 项目总体规划（每次重大迭代后更新）
```

## 环境要求

- **Node.js** >= 18
- **pnpm** 9.15.0（`corepack enable` 可自动启用）
- **TypeScript** 5.7+

## 核心命令

```bash
# 安装所有依赖
pnpm install

# 构建所有包
pnpm build

# 运行所有测试
pnpm test

# 清理构建产物
pnpm clean
```

## 新增一个纯 Skill

纯 Skill 无需构建，只需在 `packages/skills/<name>/` 下创建 `SKILL.md` 文件即可。

### SKILL.md 模板

```markdown
---
name: my-skill
description: 清晰的描述，说明何时触发此技能。
---

# Skill 标题

写给 Agent 的指令内容...
```

**命名规则**：目录名和 `name` 字段必须一致，全小写 + 连字符（如 `my-skill-name`）。

详细规范参见 `@create-skill` 技能。

### 文件组织

Skill 目录可包含辅助文件（模板、示例等），在 SKILL.md 中通过相对路径引用：

```
packages/skills/my-skill/
├── SKILL.md
├── templates/
│   └── example.ts
└── examples/
    └── usage.ts
```

## 新增 CLI 命令

CLI 基于 [oclif v4](https://oclif.io/)，源文件在 `packages/cli/src/commands/`。

### 步骤

1. 在 `packages/cli/src/commands/<name>.ts` 中创建 Command 子类：

```typescript
import { Command } from "@oclif/core";

export default class MyCommand extends Command {
  static description = "命令描述";

  async run(): Promise<void> {
    this.log("Hello from my-cli!");
  }
}
```

2. 构建并验证：

```bash
cd packages/cli
pnpm build

# 验证命令是否注册
node bin/run.js my-command --help
```

3. 顶层构建也会包含 CLI：

```bash
# 从仓库根目录
pnpm build
```

### 注意事项

- 文件名即命令名：`hello.ts` → `my-cli hello`
- 子目录映射为子命令：`admin/status.ts` → `my-cli admin status`
- 模块系统为 ESM（`"type": "module"`），输出目录为 `dist/`
- 共享配置继承 `tsconfig.base.json`

## TypeScript 规范

- 目标：ES2022
- 模块系统：ESM (`"module": "ESNext"`) / CLI 特例为 `NodeNext`
- 严格模式：`strict: true`
- 每个包有自己的 `tsconfig.json`，`extends` 自 `tsconfig.base.json`
- `rootDir` 指向 `./src`，`outDir` 指向 `./dist`

## 构建流水线（turbo.json）

| 任务    | 依赖     | 说明                     |
| ------- | -------- | ------------------------ |
| `build` | `^build` | 先构建依赖包，再构建自身 |
| `lint`  | `^build` | 依赖包构建后执行         |
| `test`  | `^build` | 依赖包构建后执行         |
| `dev`   | 无       | 无缓存，持续运行         |
| `clean` | 无       | 无缓存                   |

## 新增扩展（extensions）

在 `packages/extensions/<name>/` 下创建新包，确保：

- 包含 `package.json`（name 以 `@gaorun/` 开头）
- `pnpm-workspace.yaml` 的 `packages` 字段已包含 `packages/extensions/*`
- 遵循 TypeScript 规范

## 修改 AGENTS.md

每次重大迭代后必须更新 `AGENTS.md`（项目根目录），确保：

- 第 7 节「已有 Skill 清单」反映最新列表
- 第 8 节「迭代记录」以时间倒序追加变更

## 最佳实践

1. **先读 AGENTS.md** — 了解项目整体架构后再动手
2. **一个 PR 一个关注点** — 不要混入无关变更
3. **Skill 是核心资产** — 纯 Skill 零构建成本，优先考虑以 Skill 形式交付
4. **CLI 封装复杂逻辑** — 需要脚本化、跨平台的操作走 CLI
5. **保持一致性** — 文件命名、目录结构、代码风格与现有代码对齐
