---
name: deploy
description: >-
  my-labs 仓库发布部署指南。当用户说"发布"、"publish"、"发版"、"更新版本"、
  "打 tag"、"npm publish"、"发布到 npm"、"怎么发布"时触发。
  涵盖 npm publish 流程、版本管理、Git Tag、回滚操作。
---

# my-labs 发布指南

## 发布体系概览

| 产出类型     | 分发方式                 | 是否需要发布操作 |
| ------------ | ------------------------ | ---------------- |
| Agent Skills | Git 仓库（`skills add`） | **不需要**       |
| CLI 工具     | npm（`@gaorun/my-cli`）  | 需要             |
| 编辑器扩展   | npm（`@gaorun/*`）       | 需要             |

> Skill 零发布成本——push 到 GitHub 即生效。只有 npm 包才走下面的发布流程。

## 发布前检查（必须全部通过）

```bash
git status                    # 1. 工作区干净，无未提交变更
pnpm install && pnpm build    # 2. 构建通过
pnpm test                     # 3. 测试通过
npm whoami                    # 4. 确认登录了正确的 npm 账号
```

> **为什么要先 git status？** npm publish 会打包当前工作区文件，未提交的调试代码可能被意外发布。

## CLI 发布流程

### 1. 更新版本

修改 `packages/cli/package.json` 中的 `version`，或使用 npm 命令：

```bash
cd packages/cli
npm version patch   # 0.1.0 → 0.1.1（bug fix）
npm version minor   # 0.1.1 → 0.2.0（新功能）
npm version major   # 0.2.0 → 1.0.0（破坏性变更）
```

> `npm version` 会自动创建 git commit 和 tag，推荐使用。

### 2. 构建并发布

```bash
cd packages/cli
pnpm build
npm publish --access public   # scoped package 必须加 --access public
```

### 3. 验证

```bash
npx @gaorun/my-cli --help          # 功能验证
npm view @gaorun/my-cli version    # 版本验证
```

## Git Tag

每次发布必须打 tag（`npm version` 已自动创建时可跳过）：

```bash
git tag v0.1.0
git push origin v0.1.0
```

多包场景建议带包名前缀：`git tag vmy-cli@0.1.0`

## 发布后

1. 更新 `AGENTS.md` 第 8 节「迭代记录」
2. 更新 `CHANGELOG.md`（如有）
3. 推送到 GitHub：`git push && git push --tags`

## 发布检查清单

- [ ] `git status` 无未提交变更
- [ ] `pnpm test` 全部通过
- [ ] 版本号符合 SemVer
- [ ] `npm whoami` 确认账号正确
- [ ] 构建产物在 `dist/` 目录中
- [ ] `npm publish` 使用了 `--access public`
- [ ] 发布后 `npx @gaorun/my-cli --help` 可正常执行
- [ ] Git tag 已推送

## 问题修复：回滚与废弃

```bash
# 紧急撤回（24 小时内有效）
npm unpublish @gaorun/my-cli@x.y.z

# 推荐：发布修复版本（不破坏已安装用户）
npm version patch
pnpm build
npm publish --access public

# 标记旧版本为废弃（引导用户升级）
npm deprecate @gaorun/my-cli@x.y.z "请升级到最新版本"
```

> 优先发布修复版本而非 unpublish——前者对已安装用户更安全。
