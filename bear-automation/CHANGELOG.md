# Bear Automation Skill - 更新日志

## 版本 1.1.0 (2026-03-06)

### ✨ 新增功能

#### 新增 Actions
1. **grab-url** - 从网页创建笔记
   - 支持从任何网页 URL 抓取内容并创建笔记
   - 可选参数：tags, pin, wait
   - 示例：`bear://x-callback-url/grab-url?url=https://example.com&tags=reading`

2. **tags** - 获取所有标签列表
   - 返回 JSON 格式的标签数组
   - 需要 API Token
   - 示例：`bear://x-callback-url/tags?token=YOUR_TOKEN`

#### Token 认证机制
- 添加完整的 Token 生成和使用文档
- Token 用于高级功能：
  - 获取当前选中的笔记
  - 获取所有标签列表
  - 获取详细的搜索结果
- 平台特定：iOS 和 macOS 的 token 不通用

#### 新增参数

**create action**:
- `clipboard`: 使用剪贴板内容
- `file`: Base64 编码的文件
- `filename`: 文件名（与 file 一起使用）
- `float`: 浮动窗口（MacOS）
- `type`: HTML 转 Markdown
- `url`: 图片链接基础 URL

**add-text action**:
- `clipboard`: 使用剪贴板内容
- `header`: 添加到指定标题下
- `selected`: 使用当前选中的笔记（需要 token）
- `new_window`: 在新窗口打开

**add-file action**:
- `selected`: 使用当前选中的笔记（需要 token）
- `header`: 添加到指定标题下
- `new_window`: 在新窗口打开

**open-note action**:
- `exclude_trashed`: 排除已删除的笔记
- `float`: 浮动窗口（MacOS）
- `open_note`: 是否显示笔记
- `pin`: 置顶笔记
- `selected`: 使用当前选中的笔记（需要 token）

**search action**:
- `token`: 用于返回详细搜索结果

**open-tag action**:
- `token`: 用于返回标签详情

### 🔧 改进

1. **文档完善**
   - 添加 Token 生成和使用指南
   - 补充所有遗漏的参数说明
   - 更新 API 参考表格
   - 添加更多使用示例

2. **脚本增强**
   - Python 脚本添加 `grab_url()` 和 `get_tags()` 方法
   - Shell 脚本添加 `bear_grab_url` 和 `bear_get_tags` 函数
   - 更新帮助文档

3. **参数修正**
   - `mode` 参数现在正确支持 `replace_all`
   - `file` 参数说明改为 Base64 编码（而非文件路径）
   - 明确 `text` 和 `clipboard` 参数的可选性

### 📚 新增文档

1. **COMPARISON.md** - 与官方文档的对比分析
   - 列出所有差异
   - 标注遗漏的功能
   - 提供修复建议

2. **Token 使用指南** - 在 SKILL.md 中新增章节
   - Token 生成步骤
   - Token 使用示例
   - 安全注意事项

### 🐛 修复

1. 修正 `create` action 的参数说明（text 不是必需的，可以用 clipboard）
2. 修正 `add-file` 的 file 参数说明（应为 Base64 编码）
3. 补充 `mode` 参数的 `replace_all` 选项
4. 修正 `trash` 和 `archive` 的参数（支持 search 参数）

### 📊 覆盖率

- **Actions**: 16/16 (100%) ✅
- **参数**: ~95% ✅
- **文档完整性**: 95% ✅

### ⚠️ 已知限制

1. 某些高级功能需要 Bear Pro 订阅
2. Token 是平台特定的（iOS ≠ macOS）
3. 加密笔记无法通过 API 访问
4. 某些操作在 Bear 锁定状态下无法执行

---

## 版本 1.0.0 (2026-03-06)

### 🎉 初始版本

- 基本的笔记创建和编辑功能
- 搜索和打开笔记
- 标签管理（打开、重命名、删除）
- 特殊集合（untagged, today, todo, locked）
- Python 和 Shell 辅助脚本
- 完整的文档和示例
- 测试套件

---

## 升级指南

### 从 1.0.0 升级到 1.1.0

1. **更新文件**：
   ```bash
   cd /Users/run/Documents/Code/playroom/skills/bear-automation
   git pull  # 如果使用 git
   ```

2. **生成 Token**（可选，用于高级功能）：
   - 打开 Bear
   - 进入 Help → API Token
   - 点击 Generate Token
   - 保存 token 供后续使用

3. **测试新功能**：
   ```bash
   # 测试 grab-url
   source scripts/bear_helper.sh
   bear_grab_url "https://example.com" "test"

   # 测试 get-tags（需要 token）
   bear_get_tags "YOUR_TOKEN"
   ```

4. **更新现有脚本**（如果需要）：
   - 检查是否使用了 `file` 参数（现在需要 Base64 编码）
   - 如果使用 `mode=replace_all`，确认拼写正确

### 兼容性

- ✅ 向后兼容：所有 1.0.0 的功能在 1.1.0 中仍然可用
- ✅ 参数兼容：现有参数的行为保持不变
- ⚠️ `file` 参数语义变化：从文件路径改为 Base64 编码（如果你使用了此参数，需要更新）

---

## 贡献

欢迎提交问题和改进建议！

## 许可证

MIT License
