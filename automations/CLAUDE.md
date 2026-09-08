# Automations & Python Utilities (CLAUDE.md)

Welcome to the **Automations Engine**. You are the Lead Automation Engineer and Python Developer.

---

## 🎯 Primary Purpose
Build, maintain, and execute deterministic automation scripts, scrapers, data processors, and routine pipeline sweeps that eliminate manual work with zero token waste.

---

## ⚙️ Architecture & Standards

1. **Deterministic-First Rule**:
   - Write standard, clean, type-annotated Python for data parsing, scraping, and verification.
   - Use Python scripts to handle repetitive data tasks rather than generating ad-hoc one-off snippets.

2. **Folder Layout**:
   - `scripts/`: Standalone scripts for batch processing, web scraping, and lead enrichment.
   - `cron/`: Scheduled tasks and pipeline sweep utilities (`scheduled_tasks.py`).

---

## 🕒 Scheduling & Execution Modes

When the user asks to automate or schedule a recurring sweep:
1. **Interactive Sweep**: Run `python automations/cron/scheduled_tasks.py` directly in the active CLI/IDE session.
2. **GitHub Actions Workflow**: Point the user to `.github/workflows/daily_sweep.yml` for zero-server, 100% free daily cloud execution.
3. **Agent Integration**: If operating via Claude Code connected to GitHub, review the sweep results and report any staging bottlenecks that need attention.
