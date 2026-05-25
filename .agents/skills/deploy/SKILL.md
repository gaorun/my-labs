---
name: deploy
description: >-
  my-labs 仓库发布部署指南。当用户需要发布 npm 包、更新版本、打 tag、
  或执行任何发布相关任务时触发。涵盖 npm publish、版本管理、发布检查清单。
---

# my-labs 发布指南

## 发布体系

my-labs 有三类产出，分发方式不同：

| 产出类型     | 分发方式                | 说明                           |
| ------------ | ----------------------- | ------------------------------ |
| Agent Skills | `npx skills add <repo>` | 从 Git 仓库直接读取，无需发布  |
| CLI 工具     | `npm publish`           | 发布到 npm（`@gaorun/my-cli`） |
| 编辑器扩展   | `npm publish`           | 发布到 npm（`@gaorun/*`）      |

**重点**：只有 Agent Skills 无需发布操作，CLI 和 Extensions 都走 npm。

## 发布前检查

```bash
# 1. 确保所有代码已提交
git status

# 2. 安装依赖 + 构建 + 测试
pnpm install
pnpm build
pnpm test

# 3. 检查版本号是否已更新
cat packages/cli/package.json | grep version
```

## CLI 发布流程（npm）

### 1. 更新版本号

修改 `packages/cli/package.json` 中的 `version` 字段，遵循 [SemVer](https://semver.org/)：

- **major**: 不兼容的 API 变更
- **minor**: 向后兼容的新功能
- **patch**: 向后兼容的 bug 修复

```bash
# 或使用 npm version 自动更新
cd packages/cli
npm version patch   # 0.1.0 → 0.1.1
npm version minor   # 0.1.1 → 0.2.0
npm version major   # 0.2.0 → 1.0.0
```

### 2. 构建

```bash
cd packages/cli
pnpm build
```

### 3. 发布

```bash
# 首次发布（scoped package 需 --access public）
cd packages/cli
npm publish --access public

# 后续更新
npm publish --access public
```

### 4. 验证

```bash
# 验证安装
npx @gaorun/my-cli --help

# 验证版本
npm view @gaorun/my-cli version
```

## 多包统一发布（使用 Changesets）

当 monorepo 中有多个 npm 包需要管理时，推荐使用 Changesets：

```bash
# 安装 Changesets
pnpm add -Dw @changesets/cli
pnpm changeset init

# 创建变更记录
pnpm changeset
# 按提示选择变更的包和版本类型

# 更新版本号
pnpm changeset version

# 构建 + 发布所有包
pnpm build
pnpm -r publish --access public
```

## 发布检查清单

每项打勾确认：

- [ ] 所有测试通过（`pnpm test`）
- [ ] 构建成功（`pnpm build`）
- [ ] 版本号符合 SemVer 规范
- [ ] `CHANGELOG.md` 已更新（如适用）
- [ ] Git 工作区干净，变更已提交
- [ ] `npm whoami` 确认登录正确账号
- [ ] `--access public` 确保 scoped package 可公开访问
- [ ] 发布后验证安装和版本

## 版本回滚

如果发布了有问题的版本：

```bash
# 1. 撤销 npm 版本（24 小时内有效）
npm unpublish @gaorun/my-cli@x.y.z

# 2. 或发布修复版本（推荐）
npm version patch
pnpm build
npm publish --access public

# 3. 废弃标记旧版本（可选）
npm deprecate @gaorun/my-cli@x.y.z "有安全漏洞，请升级到最新版本"
```

## Git Tag

每次发布建议打 tag：

```bash
# 格式: v<package-name>@<version>
git tag vmy-cli@0.1.0
git push origin vmy-cli@0.1.0
```

或简化：

```bash
git tag v0.1.0
git push origin v0.1.0
```

## AGENTS.md 更新

发布后更新 `AGENTS.md` 第 8 节「迭代记录」，追加发布说明。
