"""
ACI Memory Archiver
====================
Deterministic utility that keeps brain/memory.md from growing without bound.

Only the Recent Decision Log section is journal-shaped (one timestamped entry
per milestone), so it is the only section this script ever removes entries
from. Learned Preferences and Corrected Mistakes are treated as permanent and
are always passed through untouched, since a style correction does not expire
the way a project milestone does.

Decision Log entries older than --days (default 90) are moved out of
memory.md into brain/archive/decision_log_<year>.md, grouped by the year the
decision was logged, and de-duplicated against what is already archived.

Usage:
    python automations/scripts/archive_memory.py [--days 90] [--dry-run]

Outputs:
  - brain/memory.md                       (rewritten, Decision Log trimmed)
  - brain/archive/decision_log_<year>.md  (older entries appended)
"""

import argparse
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple


SECTION_HEADER_REGEX = re.compile(r"^##\s+(.*)$")
DATED_BULLET_REGEX = re.compile(r"^-\s*`(\d{4}-\d{2}-\d{2})`:\s*(.*)$")
DECISION_LOG_MARKER = "decision log"


def parse_sections(content: str) -> Tuple[List[str], List[Tuple[str, List[str]]]]:
    """
    Split memory.md into a preamble (everything before the first '## '
    header) and an ordered list of (header_text, body_lines) sections.
    Blank lines and '---' separators between sections are dropped; they are
    re-added on render so formatting stays consistent regardless of drift in
    the source file.
    """
    lines = content.splitlines()
    header_indices = [i for i, line in enumerate(lines) if SECTION_HEADER_REGEX.match(line)]

    preamble = lines[: header_indices[0]] if header_indices else lines
    preamble = [l for l in preamble if l.strip() != "---"]

    sections: List[Tuple[str, List[str]]] = []
    for idx, start in enumerate(header_indices):
        end = header_indices[idx + 1] if idx + 1 < len(header_indices) else len(lines)
        header_text = SECTION_HEADER_REGEX.match(lines[start]).group(1).strip()
        body = lines[start + 1 : end]
        body = [l for l in body if l.strip() != "---"]
        while body and body[0].strip() == "":
            body.pop(0)
        while body and body[-1].strip() == "":
            body.pop()
        sections.append((header_text, body))

    return preamble, sections


def split_decision_log(
    body: List[str], cutoff: datetime
) -> Tuple[List[str], Dict[int, List[Tuple[str, str]]], List[str]]:
    """
    Separate a Decision Log section's bullet lines into (kept, archived_by_year,
    unparsed). Unparsed lines (no leading date) are kept in place rather than
    risk silently dropping a manually written entry.
    """
    kept: List[str] = []
    archived: Dict[int, List[Tuple[str, str]]] = {}
    unparsed: List[str] = []

    for line in body:
        match = DATED_BULLET_REGEX.match(line.strip())
        if not match:
            unparsed.append(line)
            continue
        date_str, text = match.groups()
        entry_date = datetime.strptime(date_str, "%Y-%m-%d")
        if entry_date < cutoff:
            archived.setdefault(entry_date.year, []).append((date_str, text))
        else:
            kept.append(line)

    return kept, archived, unparsed


def append_to_archive(root_dir: Path, archived: Dict[int, List[Tuple[str, str]]], dry_run: bool) -> List[str]:
    """Append archived entries to brain/archive/decision_log_<year>.md, de-duplicated."""
    archive_dir = root_dir / "brain" / "archive"
    written: List[str] = []

    for year, entries in sorted(archived.items()):
        archive_path = archive_dir / f"decision_log_{year}.md"
        existing = archive_path.read_text(encoding="utf-8") if archive_path.exists() else ""

        new_lines = [
            f"- `{date_str}`: {text}"
            for date_str, text in entries
            if f"`{date_str}`: {text}" not in existing
        ]
        if not new_lines:
            continue

        if existing:
            body_lines = existing.rstrip("\n").splitlines()
        else:
            body_lines = [
                f"# Decision Log Archive — {year}",
                "",
                "> *Auto-archived from `brain/memory.md` by `automations/scripts/archive_memory.py`.*",
                "",
            ]

        body_lines.extend(new_lines)
        updated = "\n".join(body_lines) + "\n"

        if not dry_run:
            archive_dir.mkdir(parents=True, exist_ok=True)
            archive_path.write_text(updated, encoding="utf-8")
        written.append(str(archive_path.relative_to(root_dir)))

    return written


def render_memory_md(preamble: List[str], sections: List[Tuple[str, List[str]]]) -> str:
    """Re-render memory.md in the same template style as the original file."""
    lines: List[str] = list(preamble)
    while lines and lines[-1] == "":
        lines.pop()
    lines.append("")
    lines.append("---")

    for header_text, body in sections:
        lines.append("")
        lines.append(f"## {header_text}")
        lines.extend(body if body else ["- (none logged yet)"])
        lines.append("")
        lines.append("---")

    # Drop the trailing separator after the final section.
    while lines and lines[-1] in ("", "---"):
        lines.pop()

    return "\n".join(lines) + "\n"


def archive_memory(root_dir: Optional[Path] = None, days: int = 90, dry_run: bool = False) -> Dict[str, object]:
    if root_dir is None:
        root_dir = Path(__file__).resolve().parent.parent.parent

    memory_path = root_dir / "brain" / "memory.md"
    if not memory_path.exists():
        raise FileNotFoundError(f"{memory_path} not found")

    cutoff = datetime.now() - timedelta(days=days)
    content = memory_path.read_text(encoding="utf-8")
    preamble, sections = parse_sections(content)

    total_archived = 0
    archive_files_touched: List[str] = []
    new_sections: List[Tuple[str, List[str]]] = []

    for header_text, body in sections:
        if DECISION_LOG_MARKER in header_text.lower():
            kept, archived, unparsed = split_decision_log(body, cutoff)
            total_archived += sum(len(v) for v in archived.values())
            if archived:
                archive_files_touched = append_to_archive(root_dir, archived, dry_run)
            # Preserve original order: dated entries first (already chronological
            # as written), then any unparsed lines so nothing is silently lost.
            new_sections.append((header_text, kept + unparsed))
        else:
            new_sections.append((header_text, body))

    rendered = render_memory_md(preamble, new_sections)

    if not dry_run and total_archived > 0:
        memory_path.write_text(rendered, encoding="utf-8")

    return {
        "entries_archived": total_archived,
        "archive_files": archive_files_touched,
        "cutoff_date": cutoff.strftime("%Y-%m-%d"),
        "memory_path": str(memory_path),
        "dry_run": dry_run,
        "rendered": rendered,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Archive stale Decision Log entries out of brain/memory.md")
    parser.add_argument("--days", type=int, default=90, help="Entries older than this many days are archived (default: 90)")
    parser.add_argument("--dry-run", action="store_true", help="Report what would change without writing any files")
    args = parser.parse_args()

    result = archive_memory(days=args.days, dry_run=args.dry_run)

    if result["entries_archived"] == 0:
        print(f"✅ No Decision Log entries older than {args.days} days ({result['cutoff_date']}). memory.md unchanged.")
    else:
        mode = "Would archive" if args.dry_run else "Archived"
        print(f"🗄️  {mode} {result['entries_archived']} entries older than {result['cutoff_date']}.")
        for path in result["archive_files"]:
            print(f"   -> {path}")
        if not args.dry_run:
            print(f"✅ Rewrote {result['memory_path']}")
