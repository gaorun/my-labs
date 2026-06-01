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
