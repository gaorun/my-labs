---
name: test
description: >-
  my-labs 仓库测试指南。当用户说"跑测试"、"写单测"、"加测试"、"测试挂了"、
  "覆盖率"、"测试怎么跑"、"debug 测试"时触发。
  涵盖 monorepo 中各组件的测试策略、框架选择、调试方法。
---

# my-labs 测试指南

## 运行测试

```bash
pnpm test                  # 所有包（Turborepo 编排）
pnpm --filter @gaorun/my-cli test   # 仅 CLI 包
```

> Turborepo 的 `test` 任务依赖 `^build`，构建过的包有缓存时会跳过构建直接跑测试。

## 各组件测试策略

| 组件类型  | 策略                     | 原因                                 |
| --------- | ------------------------ | ------------------------------------ |
| 纯 Skill  | **不写代码测试**         | Skill 是 Markdown 文档，通过人工审查 |
| CLI 命令  | `node:test`（Node 内置） | 零依赖、原生 ESM、与 oclif 兼容      |
| Extension | 跟随平台惯例             | VS Code 用 `@vscode/test-electron`   |

### 为什么选 node:test？

- Node 18+ 内置，**零额外依赖**
- 原生 ESM 支持，无需 ts-node 等转译层
- API 与 vitest/mocha 类似，学习成本低

## 为 CLI 命令添加测试

### 1. 配置

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

> `--loader ts-node/esm` 让 Node 直接执行 `.ts` 测试文件，无需预编译。

### 2. 编写测试

```typescript
// packages/cli/src/commands/install.test.ts
import { describe, it } from "node:test";
import assert from "node:assert";

describe("install command", () => {
  it("应导出 run 方法", async () => {
    const { default: Install } = await import("./install.js");
    const cmd = new Install([], {} as any);
    assert.ok(typeof cmd.run === "function");
  });
});
```

### 3. 常见测试场景

- **命令存在性检查**：验证默认导出有 `run` 方法
- **参数解析**：oclif 的 `static args/flags` 定义正确
- **集成测试**：通过 `node bin/run.js <cmd>` 子进程执行

## 调试测试失败

按优先级排查：

1. **依赖未构建** → `pnpm build`（Turborepo 缓存可能过期，先 clean 再 build）
2. **Node 版本过低** → 需要 >= 18，`node -v` 确认
3. **TypeScript 编译错误** → `pnpm build` 是否通过？构建失败则测试无法运行
4. **测试文件未被发现** → 检查 glob 模式是否正确匹配测试文件路径
5. **彻底重置** → `pnpm clean && pnpm install && pnpm build && pnpm test`

### 单独调试一个测试文件

```bash
cd packages/cli
node --test --loader ts-node/esm src/commands/install.test.ts
```

## CI 集成

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
        with: { node-version: 20, cache: "pnpm" }
      - run: pnpm install
      - run: pnpm build
      - run: pnpm test
```

## Skill 验证（非自动化）

纯 Skill 不需要代码测试，但创建后应检查：

1. **Frontmatter 完整**：`name` 和 `description` 字段存在
2. **命名一致**：目录名 = `name` 字段值
3. **触发可验证**：`description` 中的触发词与 Skill 内容匹配
4. **指令可执行**：Agent 按步骤操作能得到预期结果
