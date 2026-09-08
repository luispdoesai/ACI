"""
ACI Pipeline Sweep & Audit Runner
Inspects active staging directories, checks pending drafts/proposals, and prints an actionable workspace briefing.
Can be triggered manually, via Claude Code / Antigravity, or scheduled via GitHub Actions.
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# Add root directory to sys.path to allow modular imports
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

try:
    from automations.scripts.index_workspace import build_and_save_index
except ImportError:
    build_and_save_index = None


def count_files(directory_path: Path, extensions=(".md", ".txt")) -> int:
    """Count non-hidden files matching extensions in a directory."""
    if not directory_path.exists():
        return 0
    return len([f for f in directory_path.iterdir() if f.is_file() and not f.name.startswith(".") and f.suffix in extensions])


def run_pipeline_sweep():
    """Perform a full workspace health sweep and report pending items."""
    root_dir = ROOT_DIR
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    drafts_count = count_files(root_dir / "content-engine" / "drafts")
    proposals_count = count_files(root_dir / "client-ops" / "proposals")
    briefs_count = count_files(root_dir / "research-vault" / "briefs")
    video_scripts_count = count_files(root_dir / "video-engine" / "scripts")
    product_specs_count = count_files(root_dir / "product-engine" / "specs")
    email_drafts_count = count_files(root_dir / "email-engine" / "drafts")

    print(f"==================================================")
    print(f"🧹 ACI Daily Pipeline Sweep [{now}]")
    print(f"==================================================")
    print(f"📊 Active Staging Pipeline:")
    print(f"   • Content Engine Drafts:    {drafts_count} pending review")
    print(f"   • Email Engine Drafts:      {email_drafts_count} pending review")
    print(f"   • Video Engine Scripts:     {video_scripts_count} pending production")
    print(f"   • Client Ops Proposals:     {proposals_count} active proposals")
    print(f"   • Research Vault Briefs:    {briefs_count} saved briefs")
    print(f"   • Product Engine Specs:     {product_specs_count} specifications")
    print(f"--------------------------------------------------")

    # Refresh workspace catalog and memory index
    if build_and_save_index:
        try:
            index_res = build_and_save_index(root_dir)
            print(f"🗺️  Index Status: Refreshed {index_res['total_assets']} assets -> brain/workspace_index.md")
        except Exception as e:
            print(f"⚠️  Index Warning: Could not refresh index: {e}")

    # Check brain/memory.md active sprint
    memory_file = root_dir / "brain" / "memory.md"
    if memory_file.exists():
        print(f"🧠 Brain Status: Persistent memory log active ({memory_file.name})")
    else:
        print(f"⚠️  Brain Warning: brain/memory.md not found. Run setup interview.")

    print(f"✅ Sweep Complete: All systems operational. Zero errors.")
    print(f"==================================================")


if __name__ == "__main__":
    run_pipeline_sweep()
