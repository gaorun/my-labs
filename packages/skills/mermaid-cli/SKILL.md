---
name: mermaid-cli
description: >-
  mermaid-cli (mmdc) 使用指南：将 Mermaid 定义文件(.mmd)转换为 SVG/PNG/PDF，支持 CI/CD 自动化、
  Markdown 内嵌图表渲染、自定义主题和 CSS、批量转换。当用户提到渲染 Mermaid 图表、
  把 .mmd 转成图片、自动化生成图表、在 CI 中构建 Mermaid 图、Markdown 里嵌入渲染后的图表、
  自定义 Mermaid 图表样式/主题/字体、mmdc 报错或 Chromium 配置问题时触发。如果用户写出了
  ```mermaid 代码块但需要渲染成图片文件，也应该触发此技能。
---

所有命令通过 `npx -p @mermaid-js/mermaid-cli mmdc` 运行。`-p` 必填（包名 ≠ 命令名）。

> 以下示例使用 Unix shell 语法（`for`、`find`、`cat` 管道），Windows 用户请在 Git Bash、WSL 或 PowerShell 中执行。

## 基础转换

```bash
npx -p @mermaid-js/mermaid-cli mmdc -i input.mmd -o output.svg
npx -p @mermaid-js/mermaid-cli mmdc -i input.mmd -o output.png
npx -p @mermaid-js/mermaid-cli mmdc -i input.mmd -o output.pdf
```

## 主题与背景

```bash
npx -p @mermaid-js/mermaid-cli mmdc -i input.mmd -o output.png -t dark -b transparent
```

可选主题：`default` / `dark` / `forest` / `neutral` / `base`

## 尺寸与缩放

```bash
npx -p @mermaid-js/mermaid-cli mmdc -i input.mmd -o output.png --width 1920 --height 1080
npx -p @mermaid-js/mermaid-cli mmdc -i input.mmd -o output.png --scale 2
npx -p @mermaid-js/mermaid-cli mmdc -i input.mmd -o output.png --width 1200 --scale 2 -b transparent
```

## Markdown 转换

找到 ` ```mermaid ` 代码块，渲染为独立 SVG 并替换引用：

```bash
npx -p @mermaid-js/mermaid-cli mmdc -i post.md -o post-with-images.md
```

## 自定义主题（配置文件）

创建 JSON 配置文件：

```json
{
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#6C5CE7",
    "fontSize": "16px",
    "fontFamily": "Inter, sans-serif"
  },
  "themeCSS": ".label { font-weight: 600; }"
}
```

```bash
npx -p @mermaid-js/mermaid-cli mmdc -i input.mmd -o output.svg --configFile mermaid-config.json
```

## 批处理

```bash
for f in *.mmd; do
  npx -p @mermaid-js/mermaid-cli mmdc -i "$f" -o "${f%.mmd}.svg"
done

# 递归子目录
find diagrams/ -name '*.mmd' -exec npx -p @mermaid-js/mermaid-cli mmdc -i {} -o {}.svg \;
```

## stdin 管道

```bash
cat <<'EOF' | npx -p @mermaid-js/mermaid-cli mmdc --input -
graph TD
    A[Client] --> B[Load Balancer]
    B --> C[Server 1]
    B --> D[Server 2]
EOF

# 输出到文件
cat <<'EOF' | npx -p @mermaid-js/mermaid-cli mmdc --input - > output.svg
graph TD
    A-->B
EOF
```

## 自定义 CSS（动画 SVG）

```bash
npx -p @mermaid-js/mermaid-cli mmdc -i flowchart.mmd --cssFile animate.css -o animated-flowchart.svg
```

## 完整选项

| 选项                       | 说明                                               |
| -------------------------- | -------------------------------------------------- |
| `-i` / `--input`           | 输入文件（`-` 表示 stdin）                         |
| `-o` / `--output`          | 输出文件                                           |
| `-t` / `--theme`           | `default` / `dark` / `forest` / `neutral` / `base` |
| `-b` / `--backgroundColor` | 背景色（支持 `transparent`）                       |
| `--width`                  | 画布宽度，默认 800                                 |
| `--height`                 | 画布高度                                           |
| `--scale`                  | 缩放倍数                                           |
| `--cssFile`                | 自定义 CSS 文件                                    |
| `--configFile`             | Mermaid 配置文件 (JSON)                            |
| `--outputFormat`           | `svg` / `png` / `pdf`                              |
| `-q` / `--quiet`           | 静默模式                                           |
| `-h`                       | 帮助                                               |

## Chromium 配置

mmdc 依赖 Puppeteer + Chromium。通过 `PUPPETEER_EXECUTABLE_PATH` 环境变量指定系统已安装的浏览器。

根据用户系统确定 Chrome/Chromium 路径：

- **macOS**：检查 `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` 或 `~/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
- **Linux**：检查 `/usr/bin/google-chrome`、`/usr/bin/chromium-browser` 或 `/usr/bin/chromium`
- **Windows**：检查 `C:\Program Files\Google\Chrome\Application\chrome.exe` 或 `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`

使用 `ls` 或 `test -f` 确认路径存在后，临时设环境变量执行：

```bash
PUPPETEER_EXECUTABLE_PATH=<检测到的浏览器路径> npx -p @mermaid-js/mermaid-cli mmdc -i input.mmd -o output.svg
```

> 如需 `--no-sandbox`（Linux/容器环境），在 Puppeteer 配置文件中添加：`{"args": ["--no-sandbox"]}`

## 常见错误

| 错误                                                  | 解决                                                                                 |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `npx: command not found`                              | 先 source shell profile（`. ~/.zshrc` / `. ~/.bashrc` 等），或用 `zsh -c '...'` 执行 |
| `Could not find browser` / `Failed to launch browser` | 设 `PUPPETEER_EXECUTABLE_PATH` 指向系统浏览器                                        |
| `No usable sandbox!`                                  | Puppeteer 配置加 `"args": ["--no-sandbox"]`                                          |
| 中文乱码                                              | 安装中文字体包                                                                       |
