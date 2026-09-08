"""
ACI Workspace Indexer & Memory Parser
=====================================
Deterministic utility to scan all engines, parse metadata headers,
extract learnings/failure modes, and generate a unified workspace index.

Outputs:
  - brain/workspace_index.md  (High-level agent map)
  - brain/workspace_index.json (Machine-readable structured index)
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any


IGNORE_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    ".gemini",
    ".DS_Store",
    ".idea",
    ".vscode",
}

IGNORE_FILES = {
    ".DS_Store",
    ".gitignore",
}

HEADER_COMMENT_REGEX = re.compile(
    r"<!--\s*(.*?)\s*-->", re.DOTALL
)
FRONTMATTER_REGEX = re.compile(
    r"^---\s*\n(.*?)\n---", re.DOTALL
)


def parse_metadata_from_text(content: str) -> Dict[str, str]:
    """
    Extract key-value metadata from HTML comments, YAML frontmatter,
    or python docstrings (e.g. Status: ..., Summary: ..., Learnings: ...).
    """
    metadata: Dict[str, str] = {}

    # Check for <!-- ... --> block
    comment_match = HEADER_COMMENT_REGEX.search(content[:1000])
    if comment_match:
        block = comment_match.group(1)
        for line in block.splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                metadata[key.strip().lower()] = val.strip()

    # Check for YAML frontmatter
    fm_match = FRONTMATTER_REGEX.search(content[:1000])
    if fm_match:
        block = fm_match.group(1)
        for line in block.splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                metadata[key.strip().lower()] = val.strip()

    return metadata


def extract_title_and_summary(file_path: Path, content: str) -> Dict[str, Any]:
    """Extract a title and 1-line summary from markdown or python file."""
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    title = file_path.name
    summary = ""

    # Parse metadata if present
    meta = parse_metadata_from_text(content)
    status = meta.get("status", "")
    learning = meta.get("learnings", meta.get("learning", ""))
    if "summary" in meta:
        summary = meta["summary"]

    if file_path.suffix == ".md":
        for line in lines:
            if line.startswith("# ") and title == file_path.name:
                title = line.lstrip("# ").strip()
            elif not summary and not line.startswith("#") and not line.startswith("<!--") and not line.startswith("-->") and not line.startswith("---"):
                # Clean blockquotes and formatting
                cleaned = re.sub(r"^>\s*\*?", "", line)
                cleaned = re.sub(r"\*?$", "", cleaned).strip()
                if cleaned and len(cleaned) > 10:
                    summary = cleaned

    elif file_path.suffix == ".py":
        # Extract docstring
        docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
        if docstring_match:
            doc_lines = [
                l.strip()
                for l in docstring_match.group(1).splitlines()
                if l.strip() and not set(l.strip()).issubset({"=", "-", "*", "#"})
            ]
            if doc_lines:
                title = doc_lines[0]
                if len(doc_lines) > 1 and not summary:
                    summary = doc_lines[1]

    # Inferred status if not explicitly given
    if not status:
        parts = file_path.parts
        if "examples" in parts:
            status = "golden"
        elif any(p in parts for p in ("drafts", "proposals", "specs", "briefs")):
            status = "wip"
        elif "templates" in parts:
            status = "template"
        elif "scripts" in parts or "cron" in parts:
            status = "utility"
        elif "published" in parts or "outputs" in parts:
            status = "published"
        elif "brain" in parts:
            status = "core-context"
        else:
            status = "active"

    return {
        "title": title,
        "summary": summary,
        "status": status,
        "learning": learning,
    }


def scan_workspace(root_dir: Path) -> List[Dict[str, Any]]:
    """Scan all engines and collect asset records."""
    records: List[Dict[str, Any]] = []

    for path in root_dir.rglob("*"):
        if path.is_file():
            # Check exclusions
            if any(part in IGNORE_DIRS for part in path.parts):
                continue
            if path.name in IGNORE_FILES or path.name.startswith("."):
                continue
            if path.suffix not in (".md", ".py", ".json", ".sh"):
                continue

            rel_path = path.relative_to(root_dir)
            try:
                content = path.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            extracted = extract_title_and_summary(rel_path, content)
            stat = path.stat()

            # Determine module/engine
            engine = rel_path.parts[0] if len(rel_path.parts) > 1 else "root"
            category = rel_path.parts[1] if len(rel_path.parts) > 2 else rel_path.parent.name

            records.append({
                "path": str(rel_path),
                "engine": engine,
                "category": category,
                "name": path.name,
                "suffix": path.suffix,
                "title": extracted["title"],
                "summary": extracted["summary"],
                "status": extracted["status"],
                "learning": extracted["learning"],
                "size_bytes": stat.st_size,
                "last_modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
            })

    return sorted(records, key=lambda x: (x["engine"], x["category"], x["name"]))


def generate_index_markdown(records: List[Dict[str, Any]], root_dir: Path) -> str:
    """Build the high-level markdown navigation map."""
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    # Aggregate counts
    total_assets = len(records)
    golden_count = sum(1 for r in records if r["status"] == "golden")
    wip_count = sum(1 for r in records if r["status"] == "wip")
    utilities_count = sum(1 for r in records if r["status"] == "utility")
    learnings_count = sum(1 for r in records if r["learning"])

    lines: List[str] = [
        "# 🗺️ ACI Workspace Asset & Context Index",
        "",
        "> *Auto-generated by `automations/scripts/index_workspace.py`.*  ",
        "> *Agents should read this index to quickly locate relevant assets, golden standards, and learned edge cases.*",
        "",
        f"**Last Indexed**: `{now}` | **Total Assets**: `{total_assets}` | **Golden Benchmarks**: `{golden_count}` | **WIP Drafts**: `{wip_count}`",
        "",
        "---",
        "",
    ]

    # Section 1: Flagged Learnings & Self-Healing Watchlist
    learnings = [r for r in records if r["learning"]]
    if learnings:
        lines.append("## ⚠️ Learned Edge Cases & Self-Healing Watchlist")
        lines.append("| Asset | Status | Learned Gotchas / Failure Modes |")
        lines.append("| :--- | :--- | :--- |")
        for item in learnings:
            lines.append(f"| [`{item['path']}`](file://{root_dir / item['path']}) | `{item['status']}` | {item['learning']} |")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Section 2: Group by Engine
    engines: Dict[str, List[Dict[str, Any]]] = {}
    for r in records:
        engines.setdefault(r["engine"], []).append(r)

    lines.append("## 📂 Operational Engines & Context Breakdown")
    lines.append("")

    for engine_name, items in sorted(engines.items()):
        if engine_name in ("root", ".github"):
            continue

        lines.append(f"### `{engine_name}/`")
        lines.append("| Asset | Status | Summary |")
        lines.append("| :--- | :---: | :--- |")

        for item in items:
            # Format badge
            status_badge = f"`{item['status']}`"
            summary_clean = item["summary"].replace("|", "\\|") if item["summary"] else "—"
            if len(summary_clean) > 90:
                summary_clean = summary_clean[:87] + "..."
            lines.append(f"| [`{item['name']}`](file://{root_dir / item['path']}) | {status_badge} | {summary_clean} |")

        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 💡 How Agents Use This Index")
    lines.append("1. **Find Golden Standards**: Filter for status `golden` before drafting new outputs.")
    lines.append("2. **Avoid Repeating Mistakes**: Check the **Learned Edge Cases** table before executing scripts.")
    lines.append("3. **Promote New Outputs**: Change status header in draft to `status: golden` and copy to `examples/` when approved.")
    lines.append("")

    return "\n".join(lines)


def build_and_save_index(root_dir: Optional[Path] = None) -> Dict[str, Any]:
    """Execute the scan and write both markdown and JSON index files."""
    if root_dir is None:
        root_dir = Path(__file__).resolve().parent.parent.parent

    records = scan_workspace(root_dir)

    brain_dir = root_dir / "brain"
    brain_dir.mkdir(parents=True, exist_ok=True)

    # 1. Write Markdown index
    md_index_path = brain_dir / "workspace_index.md"
    md_content = generate_index_markdown(records, root_dir)
    md_index_path.write_text(md_content, encoding="utf-8")

    # 2. Write JSON index
    json_index_path = brain_dir / "workspace_index.json"
    json_data = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "total_assets": len(records),
        "assets": records,
    }
    json_index_path.write_text(json.dumps(json_data, indent=2), encoding="utf-8")

    return {
        "total_assets": len(records),
        "md_path": str(md_index_path),
        "json_path": str(json_index_path),
    }


if __name__ == "__main__":
    result = build_and_save_index()
    print(f"✅ Successfully indexed {result['total_assets']} workspace assets.")
    print(f"📄 Markdown Map: {result['md_path']}")
    print(f"📊 JSON Index:   {result['json_path']}")
