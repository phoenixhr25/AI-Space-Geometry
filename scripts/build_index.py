#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

WEEKS = [
    {
        "week": 1,
        "folder": "Week01_GradientValley",
        "title": "梯度的山谷 Gradient Valley",
        "math_core": "Gradient Descent / Loss Surface",
        "retail_use": "门店能量坡度分析",
    },
    {
        "week": 2,
        "folder": "Week02_VectorField",
        "title": "顾客路径的向量空间 Vector Field",
        "math_core": "Vector Field / Cosine Similarity",
        "retail_use": "顾客动线聚类与吸引力中心",
    }
]


def build_geometry_index():
    index = []
    for item in WEEKS:
        entry = {
            "week": item["week"],
            "folder": item["folder"],
            "title": item["title"],
            "math_core": item["math_core"],
            "retail_use": item["retail_use"],
            "path": f"./{item['folder']}/README.md",
        }
        index.append(entry)
    out_path = ROOT / "geometry_index.json"
    out_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] geometry_index.json updated ({len(index)} items)")


def build_weekly_table():
    lines = [
        "| 周次 | 主题 | 数学核心 | 零售应用 | 链接 |",
        "|------|------|-----------|-----------|------|",
    ]
    for w in sorted(WEEKS, key=lambda x: x["week"]):
        lines.append(
            f"| Week {w['week']} | {w['title']} | {w['math_core']} | {w['retail_use']} | [📘 Read](./{w['folder']}/README.md) |"
        )
    return "\n".join(lines)


def update_readme():
    readme_path = ROOT / "README.md"
    text = readme_path.read_text(encoding="utf-8")
    start_tag = "<!-- WEEK_INDEX_START -->"
    end_tag = "<!-- WEEK_INDEX_END -->"

    before, rest = text.split(start_tag, 1)
    _, after = rest.split(end_tag, 1)
    new_table = build_weekly_table()
    new_text = before + start_tag + "\n\n" + new_table + "\n\n" + end_tag + after
    readme_path.write_text(new_text, encoding="utf-8")
    print("[OK] README.md weekly index updated")


if __name__ == "__main__":
    build_geometry_index()
    update_readme()
