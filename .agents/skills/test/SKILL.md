---
name: test
description: >-
  my-labs 仓库测试指南。当用户需要运行测试、编写测试、分析测试覆盖率、
  或排查测试失败时触发。涵盖 monorepo 中各组件的测试策略和执行方式。
---

# my-labs 测试指南

## 运行测试

```bash
# 运行所有包的测试（通过 Turborepo 编排）
pnpm test

# 仅运行 CLI 包的测试
cd packages/cli && pnpm test

# 运行特定包的测试
pnpm --filter @gaorun/my-cli test
```

## 测试编排

Turborepo 的 `test` 任务配置：

```json
// turbo.json
{
  "tasks": {
    "test": {
      "dependsOn": ["^build"]  // 先构建依赖包
    }
  }
}
```

## 测试框架

各包自行选择测试框架，需在各自 `package.json` 的 `scripts.test` 中定义测试命令。

### 推荐方案

| 包类型        | 推荐框架      | 说明                     |
| ------------- | ------------- | ------------------------ |
| CLI（oclif）  | `vitest` 或 `node:test` | 轻量、原生 ESM 支持      |
| 纯 Skill      | 无需测试       | Skill 是 Markdown 文档    |
| Extension     | 跟随平台惯例   | 如 VS Code 用 `@vscode/test-electron` |

### CLI 测试示例

```typescript
// packages/cli/src/commands/install.test.ts
import { describe, it } from 'node:test'
import assert from 'node:assert'

describe('install command', () => {
  it('should export a run method', async () => {
    const { default: Install } = await import('./install.js')
    const cmd = new Install([], {} as any)
    assert.ok(typeof cmd.run === 'function')
  })
})
```

### 配置 CLI 测试

在 `packages/cli/package.json` 中添加：

```json
{
  "scripts": {
    "test": "node --test --loader ts-node/esm src/**/*.test.ts"
  },
  "devDependencies": {
    "ts-node": "^10.9.0"
  }
}
```

或使用 vitest：

```json
{
  "scripts": {
    "test": "vitest run"
  },
  "devDependencies": {
    "vitest": "^2.0.0"
  }
}
```

## Skill 验证（非自动化）

纯 Skill 不需要代码测试，但应进行人工检查：

1. **Frontmatter 完整性** — `name` 和 `description` 字段存在且格式正确
2. **命名一致性** — 目录名与 `name` 字段一致
3. **触发描述清晰** — `description` 能让 Agent 在正确场景下激活
4. **内容可执行** — 指令具体、可操作，Agent 能按步骤完成

## CI 集成

建议在 GitHub Actions 中添加测试工作流：

```yaml
# .github/workflows/test.yml
name: Test
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'
      - run: pnpm install
      - run: pnpm build
      - run: pnpm test
```

## 调试测试失败

1. **检查依赖是否构建** — `pnpm build` 确保依赖包已编译
2. **单独运行失败的包** — 使用 `pnpm --filter` 隔离问题
3. **检查 Node 版本** — 确保 >= 18
4. **检查 TypeScript 编译错误** — `pnpm build` 是否通过
5. **清理后重试** — `pnpm clean && pnpm install && pnpm build && pnpm test`
