"""
ACI Engine Scaffolder
======================
Deterministic utility to spawn a new operational engine/module folder
with the standard ACI 3-tier structure (CLAUDE.md, SOP.md, CONTEXT.md,
examples/, templates/, optional scripts/, and staging dirs).

Usage:
    python engine-builder/scripts/scaffold_engine.py <module-slug> \
        [--dirs drafts,published] [--scripts] [--force]

Example:
    python engine-builder/scripts/scaffold_engine.py podcast-engine --dirs drafts,published --scripts
"""

import argparse
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"

SLUG_RE = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")

TEMPLATE_FILES = {
    "CLAUDE_template.md": "CLAUDE.md",
    "SOP_template.md": "SOP.md",
    "CONTEXT_template.md": "CONTEXT.md",
}


def validate_slug(slug: str) -> None:
    if not SLUG_RE.match(slug):
        raise SystemExit(
            f"Invalid module slug '{slug}'. Use lowercase kebab-case, e.g. 'podcast-engine'."
        )


def title_from_slug(slug: str) -> str:
    return " ".join(word.capitalize() for word in slug.split("-"))


def render_template(template_path: Path, context: dict) -> str:
    text = template_path.read_text(encoding="utf-8")
    for key, value in context.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def scaffold(slug: str, stage_dirs: list, include_scripts: bool, force: bool) -> Path:
    validate_slug(slug)
    module_dir = ROOT / slug

    if module_dir.exists() and not force:
        raise SystemExit(
            f"'{slug}/' already exists. Pass --force to add missing pieces "
            "without overwriting existing files."
        )

    module_dir.mkdir(parents=True, exist_ok=True)
    (module_dir / "examples").mkdir(exist_ok=True)
    (module_dir / "templates").mkdir(exist_ok=True)
    for d in stage_dirs:
        (module_dir / d).mkdir(exist_ok=True)
    if include_scripts:
        (module_dir / "scripts").mkdir(exist_ok=True)

    context = {
        "MODULE_SLUG": slug,
        "MODULE_TITLE": title_from_slug(slug),
        "PRIMARY_STAGE_DIR": stage_dirs[0] if stage_dirs else "outputs",
        "DATE": date.today().isoformat(),
    }

    created, skipped = [], []
    for template_name, output_name in TEMPLATE_FILES.items():
        template_path = TEMPLATES_DIR / template_name
        output_path = module_dir / output_name
        if output_path.exists() and not force:
            skipped.append(output_name)
            continue
        output_path.write_text(render_template(template_path, context), encoding="utf-8")
        created.append(output_name)

    subfolder_summary = ["examples/", "templates/"] + [f"{d}/" for d in stage_dirs]
    if include_scripts:
        subfolder_summary.append("scripts/")

    print(f"Scaffolded '{slug}/' at {module_dir}")
    print(f"  Subfolders: {', '.join(subfolder_summary)}")
    if created:
        print(f"  Created: {', '.join(created)}")
    if skipped:
        print(f"  Skipped (already existed): {', '.join(skipped)}")
    print(
        "\nNext: fill in every TODO block in the new CLAUDE.md/SOP.md/CONTEXT.md, "
        "add a real asset to examples/, then log it in brain/memory.md and "
        "run automations/scripts/index_workspace.py."
    )

    return module_dir


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new ACI operational engine/module.")
    parser.add_argument("slug", help="Module folder name in kebab-case, e.g. podcast-engine")
    parser.add_argument(
        "--dirs",
        default="drafts",
        help="Comma-separated staging dirs beyond examples/ and templates/ (default: drafts)",
    )
    parser.add_argument(
        "--scripts",
        action="store_true",
        help="Also create a scripts/ folder for deterministic automation",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Add missing pieces even if the module folder already exists (never overwrites existing files)",
    )
    args = parser.parse_args()

    stage_dirs = [d.strip() for d in args.dirs.split(",") if d.strip()] if args.dirs else []
    scaffold(args.slug, stage_dirs, args.scripts, args.force)


if __name__ == "__main__":
    main()
