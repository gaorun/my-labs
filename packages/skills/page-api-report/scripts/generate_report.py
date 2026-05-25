#!/usr/bin/env python3
"""Generate page API flow report in HTML or Markdown format."""

import argparse
import json
import os
import sys
import webbrowser
from datetime import datetime
from html import escape as html_escape
from pathlib import Path

# ──────────────────────────────────────────────
#  helpers
# ──────────────────────────────────────────────


def load_data(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def enum_to_badges_html(enums):
    """Render enum dict as HTML badge spans."""
    if not enums:
        return '<span class="fallback-text">—</span>'
    badges = []
    for k, v in enums.items():
        badges.append(
            f'<span class="enum-badge">{html_escape(str(k))} = {html_escape(str(v))}</span>'
        )
    return " ".join(badges)


def enum_to_text(enums):
    """Render enum dict as plain text."""
    if not enums:
        return "—"
    return ", ".join(f"{k}={v}" for k, v in enums.items())


def fallback_html(text):
    if not text:
        return '<span class="fallback-text">—</span>'
    return f'<span class="fallback-text">{html_escape(text)}</span>'


def build_req_params_table_html(params):
    if not params:
        return ""
    rows = ""
    for p in params:
        field = html_escape(p.get("field", ""))
        source = html_escape(p.get("source", ""))
        default = html_escape(p.get("default", "")) or "—"
        rows += f"""<tr>
            <td class="field">{field}</td>
            <td>{source}</td>
            <td>{default}</td>
        </tr>"""
    return f"""<div class="api-sub">
        <h4>📥 请求参数（入参）</h4>
        <table>
            <thead><tr><th>字段名</th><th>取值来源</th><th>默认值 / 枚举</th></tr></thead>
            <tbody>{rows}</tbody>
        </table>
    </div>"""


def build_resp_fields_table_html(fields, depth=0):
    """Recursively build response fields table. fields can have sub_fields."""
    if not fields:
        return ""
    rows = ""
    for f in fields:
        field_name = f.get("field", "")
        usage = f.get("ui_usage", f.get("description", ""))
        enums = f.get("enums")
        fb = f.get("fallback", "")

        # indent for nested fields
        prefix = "├ " * depth if depth > 0 else ""
        rows += f"""<tr>
            <td class="field">{prefix}{html_escape(field_name)}</td>
            <td>{html_escape(usage)}</td>
            <td>{enum_to_badges_html(enums)}</td>
            <td>{fallback_html(fb)}</td>
        </tr>"""

        # recurse into sub_fields
        sub_fields = f.get("sub_fields", [])
        if sub_fields:
            for sf in sub_fields:
                sf_name = sf.get("field", "")
                sf_usage = sf.get("ui_usage", sf.get("description", ""))
                sf_enums = sf.get("enums")
                sf_fb = sf.get("fallback", "")
                rows += f"""<tr>
                    <td class="field" style="padding-left:{24 + depth * 16}px">└ {html_escape(sf_name)}</td>
                    <td>{html_escape(sf_usage)}</td>
                    <td>{enum_to_badges_html(sf_enums)}</td>
                    <td>{fallback_html(sf_fb)}</td>
                </tr>"""
    return f"""<div class="api-sub">
        <h4>📤 响应字段（出参）</h4>
        <table>
            <thead><tr><th>字段名</th><th>页面作用</th><th>枚举值</th><th>空值兜底</th></tr></thead>
            <tbody>{rows}</tbody>
        </table>
    </div>"""


def build_api_card_html(api):
    idx = api.get("index", "?")
    method = api.get("method", "GET").upper()
    name = html_escape(api.get("name", ""))
    timing = html_escape(api.get("trigger_timing", ""))

    req_html = build_req_params_table_html(api.get("request_params", []))
    resp_html = build_resp_fields_table_html(api.get("response_fields", []))

    # dependency info
    depends = api.get("depends_on")
    dep_html = ""
    if depends:
        dep_html = f'<div style="font-size:12px;color:var(--ink-muted);margin-bottom:8px;">依赖接口：{html_escape(depends)}</div>'

    # caching info
    caching = api.get("caching")
    cache_html = ""
    if caching:
        cache_html = f'<div class="api-sub"><h4>💾 缓存策略</h4><div class="cache-item">{html_escape(caching)}</div></div>'

    method_class = method.lower()

    return f"""<div class="api-card">
        <div class="api-card-header">
            <span class="api-index">#{idx}</span>
            <span class="api-method {method_class}">{method}</span>
            <span class="api-path">{name}</span>
        </div>
        <div class="api-card-body">
            <div class="trigger">{timing}</div>
            {dep_html}
            {req_html}
            {resp_html}
            {cache_html}
        </div>
    </div>"""


# ──────────────────────────────────────────────
#  SVG sequence diagram renderer
# ──────────────────────────────────────────────


def build_svg_sequence(seq_data):
    """Render a sequence diagram as inline SVG."""
    actors = seq_data.get("actors", [])
    steps = seq_data.get("steps", [])

    if not actors or not steps:
        return '<p style="text-align:center;color:var(--ink-muted);padding:40px;">暂无时序数据</p>'

    # layout constants
    actor_count = len(actors)
    actor_index = {a["id"]: i for i, a in enumerate(actors)}
    col_width = 200
    row_height = 48
    margin_left = 40
    margin_top = 40
    margin_right = 40
    margin_bottom = 40
    svg_width = margin_left + actor_count * col_width + margin_right
    svg_height = margin_top + (len(steps) + 1) * row_height + margin_bottom

    lines_svg = ""
    # actor headers (lifeline heads)
    for i, actor in enumerate(actors):
        cx = margin_left + i * col_width + col_width // 2
        label = html_escape(actor.get("label", actor["id"]))
        # head box
        rx = cx - 70
        ry = margin_top - 30
        rw = 140
        rh = 36
        lines_svg += f"""<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="#002fa7" stroke="none"/>
        <text x="{cx}" y="{ry + 23}" text-anchor="middle" fill="#fff" font-size="12" font-weight="600" font-family="sans-serif">{label}</text>"""

    # lifeline vertical lines (dashed)
    for i in range(actor_count):
        cx = margin_left + i * col_width + col_width // 2
        y1 = margin_top + 12
        y2 = margin_top + len(steps) * row_height + 20
        lines_svg += f"""<line x1="{cx}" y1="{y1}" x2="{cx}" y2="{y2}" stroke="#dcdce0" stroke-width="1" stroke-dasharray="6,4"/>"""

    # steps
    for si, step in enumerate(steps):
        y = margin_top + si * row_height + row_height // 2
        fr = step.get("from", "")
        to = step.get("to", "")
        label = step.get("label", "")

        fi = actor_index.get(fr)
        ti = actor_index.get(to)
        if fi is None or ti is None:
            continue

        x1 = margin_left + fi * col_width + col_width // 2
        x2 = margin_left + ti * col_width + col_width // 2

        # arrow line
        arrow_color = "#002fa7" if fi < ti else "#c72a2a"
        lines_svg += f"""<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{arrow_color}" stroke-width="1.5" marker-end="url(#arrow-{arrow_color[1:]})"/>"""

        # label
        label_y = y - 8
        label_escaped = html_escape(label)
        text_length = (
            len(label_escaped) * 6.5
        )  # rough estimate for Chinese + ASCII mixed text
        label_width = max(text_length, 60) + 16

        # position label centered between the two points
        label_cx = (x1 + x2) / 2
        label_rx = label_cx - label_width / 2

        # background rect
        lines_svg += f"""<rect x="{label_rx}" y="{label_y - 14}" width="{label_width}" height="20" fill="#ebedf0" stroke="none"/>
        <text x="{label_cx}" y="{label_y}" text-anchor="middle" fill="#1a1a1a" font-size="11" font-family="sans-serif">{label_escaped}</text>"""

    # arrow markers
    markers_svg = """<defs>
        <marker id="arrow-002fa7" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="#002fa7"/>
        </marker>
        <marker id="arrow-c72a2a" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="#c72a2a"/>
        </marker>
    </defs>"""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="100%" style="max-width:{svg_width}px;">
        {markers_svg}
        {lines_svg}
    </svg>"""
    return svg


# ──────────────────────────────────────────────
#  Mermaid diagram generator (for markdown)
# ──────────────────────────────────────────────


def build_mermaid_sequence(seq_data):
    """Render sequence diagram as Mermaid markdown."""
    actors = seq_data.get("actors", [])
    steps = seq_data.get("steps", [])

    if not actors or not steps:
        return "```mermaid\nsequenceDiagram\n    Note over 用户,后端: 暂无时序数据\n```"

    lines = ["sequenceDiagram"]

    # declare participants
    for actor in actors:
        aid = actor["id"]
        label = actor.get("label", aid)
        lines.append(f"    participant {aid} as {label}")

    # steps
    for step in steps:
        fr = step.get("from", "")
        to = step.get("to", "")
        label = step.get("label", "")

        if fr == to:
            lines.append(f"    {fr}->>{fr}: {label}")
        else:
            # determine arrow style: to user = dashed, from user = solid
            if to == "user":
                lines.append(f"    {fr}-->>{to}: {label}")
            elif fr == "user":
                lines.append(f"    {fr}->>{to}: {label}")
            else:
                # backend to frontend = response (dashed)
                if fr == "be" and to == "fe":
                    lines.append(f"    {fr}-->>{to}: {label}")
                elif fr == "fe" and to == "be":
                    lines.append(f"    {fr}->>+{to}: {label}")
                    # automatically close activation
                    lines.append(f"    {to}-->>-{fr}: ✓")
                    # skip the next step if it's one step after (hack: just keep simple)
                else:
                    lines.append(f"    {fr}->>{to}: {label}")

    # deduplicate consecutive identical responses
    deduped = []
    for i, line in enumerate(lines):
        if (
            i > 0
            and line.startswith("    be-->>fe:")
            and lines[i - 1].startswith("    be-->>fe:")
        ):
            continue
        deduped.append(line)

    return "```mermaid\n" + "\n".join(deduped) + "\n```"


# ──────────────────────────────────────────────
#  HTML report builder
# ──────────────────────────────────────────────


def build_html(data, template_path):
    with open(template_path, encoding="utf-8") as f:
        html = f.read()

    # header replacements
    html = html.replace(
        "{{PAGE_TITLE}}", html_escape(data.get("page_title", "未命名页面"))
    )
    html = html.replace("{{PAGE_ROUTE}}", html_escape(data.get("page_route", "—")))
    html = html.replace("{{PROJECT_NAME}}", html_escape(data.get("project_name", "—")))
    html = html.replace("{{FRAMEWORK}}", html_escape(data.get("framework", "—")))
    html = html.replace("{{TOTAL_APIS}}", str(data.get("total_apis", 0)))
    html = html.replace(
        "{{ANALYSIS_TIME}}",
        html_escape(data.get("analysis_time", datetime.now().strftime("%Y-%m-%d"))),
    )

    # API cards
    apis = data.get("apis", [])
    cards_html = ""
    for api in apis:
        cards_html += build_api_card_html(api)
    html = html.replace(
        "{{API_CARDS}}",
        cards_html
        or '<p style="text-align:center;color:var(--ink-muted);padding:20px;">未发现接口调用</p>',
    )

    # cache section
    cache_data = data.get("cache_and_polling", {})
    has_cache = cache_data and any(v for v in cache_data.values())
    if has_cache:
        cache_items = ""
        token = cache_data.get("token")
        if token:
            cache_items += f'<div class="cache-item"><span class="cache-label">🔐 鉴权缓存</span>{html_escape(token)}</div>'

        cached_data = cache_data.get("cached_data", [])
        if cached_data:
            items = "".join(f"<li>{html_escape(d)}</li>" for d in cached_data)
            cache_items += f'<div class="cache-item"><span class="cache-label">💾 数据缓存</span><ul style="margin:4px 0 0 18px;">{items}</ul></div>'

        polling = cache_data.get("polling")
        if polling:
            cache_items += f'<div class="cache-item"><span class="cache-label">🔄 轮询策略</span>{html_escape(polling)}</div>'

        dedup = cache_data.get("dedup")
        if dedup:
            cache_items += f'<div class="cache-item"><span class="cache-label">🚫 防重策略</span>{html_escape(dedup)}</div>'

        cache_section = f"""<div class="section">
            <h2>💾 本地缓存与轮询策略</h2>
            <div class="subtitle">前端本地存储、鉴权、轮询和防重策略</div>
            {cache_items}
        </div>"""
    else:
        cache_section = ""
    html = html.replace("{{CACHE_SECTION}}", cache_section)

    # sequence diagram
    seq_data = data.get("sequence_data", {})
    svg = build_svg_sequence(seq_data)
    html = html.replace("{{SEQUENCE_SVG}}", svg)

    return html


# ──────────────────────────────────────────────
#  Markdown report builder
# ──────────────────────────────────────────────


def build_markdown(data):
    lines = []

    page_title = data.get("page_title", "未命名页面")
    page_route = data.get("page_route", "—")
    project_name = data.get("project_name", "—")
    framework = data.get("framework", "—")
    total_apis = data.get("total_apis", 0)
    analysis_time = data.get("analysis_time", datetime.now().strftime("%Y-%m-%d"))

    lines.append(f"# 页面接口发现报告")
    lines.append("")
    lines.append(f"| 项目 | 信息 |")
    lines.append(f"| --- | --- |")
    lines.append(f"| 页面 | {page_title} |")
    lines.append(f"| 路由 | `{page_route}` |")
    lines.append(f"| 项目 | {project_name} |")
    lines.append(f"| 框架 | {framework} |")
    lines.append(f"| 接口数 | {total_apis} |")
    lines.append(f"| 分析时间 | {analysis_time} |")
    lines.append("")

    # API flow
    lines.append("---")
    lines.append("")
    lines.append("## 📡 接口调用链路")
    lines.append("")
    lines.append("*按用户操作动线顺序排列*")
    lines.append("")

    apis = data.get("apis", [])
    for api in apis:
        idx = api.get("index", "?")
        method = api.get("method", "GET").upper()
        name = api.get("name", "")
        timing = api.get("trigger_timing", "")
        trigger_cat = api.get("trigger_category", "")

        lines.append(f"### #{idx} {method} `{name}`")
        lines.append("")
        lines.append(f"> ⏱ **调用时机**（{trigger_cat}）：{timing}")
        lines.append("")

        # dependency
        depends = api.get("depends_on")
        if depends:
            lines.append(f"⬆ 依赖接口：`{depends}`")
            lines.append("")

        # request params
        req_params = api.get("request_params", [])
        if req_params:
            lines.append("#### 📥 请求参数（入参）")
            lines.append("")
            lines.append("| 字段名 | 取值来源 | 默认值 / 枚举 |")
            lines.append("| --- | --- | --- |")
            for p in req_params:
                field = p.get("field", "")
                source = p.get("source", "")
                default = p.get("default", "") or "—"
                lines.append(f"| `{field}` | {source} | {default} |")
            lines.append("")

        # response fields
        resp_fields = api.get("response_fields", [])
        if resp_fields:
            lines.append("#### 📤 响应字段（出参）")
            lines.append("")
            lines.append("| 字段名 | 页面作用 | 枚举值 | 空值兜底 |")
            lines.append("| --- | --- | --- | --- |")

            def write_fields(fields, depth=0):
                nonlocal lines
                for f in fields:
                    field = f.get("field", "")
                    usage = f.get("ui_usage", f.get("description", ""))
                    enums = enum_to_text(f.get("enums"))
                    fb = f.get("fallback", "") or "—"
                    prefix = "  " * depth
                    lines.append(f"| {prefix}`{field}` | {usage} | {enums} | {fb} |")
                    sub_fields = f.get("sub_fields", [])
                    if sub_fields:
                        write_fields(sub_fields, depth + 1)

            write_fields(resp_fields)
            lines.append("")

        # caching
        caching = api.get("caching")
        if caching:
            lines.append(f"💾 **缓存策略**：{caching}")
            lines.append("")

    # cache & polling
    cache_data = data.get("cache_and_polling", {})
    has_cache = cache_data and any(v for v in cache_data.values())
    if has_cache:
        lines.append("---")
        lines.append("")
        lines.append("## 💾 本地缓存与轮询策略")
        lines.append("")

        token = cache_data.get("token")
        if token:
            lines.append(f"- 🔐 **鉴权缓存**：{token}")

        cached_data_list = cache_data.get("cached_data", [])
        if cached_data_list:
            lines.append(f"- 💾 **数据缓存**：")
            for d in cached_data_list:
                lines.append(f"  - {d}")

        polling = cache_data.get("polling")
        if polling:
            lines.append(f"- 🔄 **轮询策略**：{polling}")

        dedup = cache_data.get("dedup")
        if dedup:
            lines.append(f"- 🚫 **防重策略**：{dedup}")
        lines.append("")

    # sequence diagram
    lines.append("---")
    lines.append("")
    lines.append("## 🔁 用户-前端-后端 时序图")
    lines.append("")

    seq_data = data.get("sequence_data", {})
    mermaid = build_mermaid_sequence(seq_data)
    lines.append(mermaid)
    lines.append("")

    # footer
    lines.append("---")
    lines.append("")
    lines.append(f"*由 page-api-report 技能自动生成 · {analysis_time}*")

    return "\n".join(lines)


# ──────────────────────────────────────────────
#  main
# ──────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(description="Generate page API flow report")
    parser.add_argument("data_file", help="Path to JSON data file")
    parser.add_argument(
        "--format",
        choices=["html", "markdown"],
        default="html",
        help="Output format (default: html)",
    )
    parser.add_argument("-o", "--output", help="Custom output file path")
    parser.add_argument(
        "--no-open", action="store_true", help="Don't open browser (HTML only)"
    )

    args = parser.parse_args()

    data = load_data(args.data_file)
    script_dir = Path(__file__).resolve().parent.parent

    if args.format == "html":
        template_path = script_dir / "assets" / "template.html"
        if not template_path.exists():
            print(f"错误：找不到模板文件 {template_path}", file=sys.stderr)
            sys.exit(1)

        html = build_html(data, template_path)

        if args.output:
            out_path = args.output
        else:
            out_path = "page_api_report.html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ HTML 报告已生成：{os.path.abspath(out_path)}")

        if not args.no_open:
            webbrowser.open("file://" + os.path.abspath(out_path))

    elif args.format == "markdown":
        md = build_markdown(data)

        if args.output:
            out_path = args.output
        else:
            out_path = "page_api_report.md"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"✅ Markdown 报告已生成：{os.path.abspath(out_path)}")


if __name__ == "__main__":
    main()
