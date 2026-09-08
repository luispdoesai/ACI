# ⚡ Automations & Scheduling (`automations/`)

> **Your Deterministic Toolbelt: Fast, Zero-Token Utilities & Flexible Scheduling.**

The `automations/` folder provides the AI with deterministic, pre-built Python scripts for web scraping, lead enrichment, CSV cleaning, and routine pipeline sweeps.

Instead of burning tokens having an LLM manually parse raw HTML or count files, Python handles mechanical tasks in milliseconds for $0.00.

---

## 📂 Directory Structure

```text
automations/
├── CONTEXT.md                 # This guided context file
├── CLAUDE.md                  # Guidelines and architecture rules for Python utilities
├── scripts/                   # The AI's mechanical toolbelt
│   ├── web_scraper.py         # Fast URL text & title extractor (avoids HTML token bloat)
│   └── lead_enricher.py       # Domain classifier & lead enrichment utility
└── cron/                      # Scheduled tasks & maintenance sweeps
    └── scheduled_tasks.py     # Pipeline audit and workspace health check script
```

---

## 🕒 The 3 Ways to Schedule Sweeps & Automations

You have total flexibility in how you run and schedule your workspace sweeps:

### 1. In Your Active AI Assistant (Claude Code / Antigravity / Gemini)
You don't need external servers. Simply ask your assistant in chat:
> *"Run the daily automation sweep."*
> *"Audit my pending drafts and briefs using `scheduled_tasks.py`."*

If using **Antigravity**, you can use the `/schedule` slash command to set up recurring cron checks directly inside your agent session.

---

### 2. 100% Free Cloud Scheduling via GitHub Actions (Zero Server / Zero Cost)
If you push this repository to GitHub, ACI includes a pre-configured workflow:
- **Location**: [`.github/workflows/daily_sweep.yml`](../.github/workflows/daily_sweep.yml)
- **Schedule**: Runs automatically every day at 8:00 AM UTC (or trigger manually via GitHub Actions UI).
- **Cost**: 100% free on standard GitHub public/private repositories. No VPS, no Docker container, and no server configuration required.

---

### 3. Remote Repository Connection (Claude Code / Web Agent)
You can connect your GitHub repository directly to **Claude Code** or remote agent environments:
- The AI agent clones/connects to your repo branch.
- It executes the sweep script, audits pending staging folders, and commits updates, drafts, or clean data directly to your repository.

---

## 🛠️ The Deterministic Python Toolbelt

Your AI assistant will automatically run these scripts when relevant:

| Script | Purpose | Command Example |
| :--- | :--- | :--- |
| **`scripts/web_scraper.py`** | Scrapes clean text from any URL before feeding it to the AI. | `python automations/scripts/web_scraper.py <url>` |
| **`scripts/lead_enricher.py`** | Classifies email domains into B2B vs. B2C in 5ms. | `python automations/scripts/lead_enricher.py <email>` |
| **`cron/scheduled_tasks.py`** | Audits all staging pipelines (`drafts/`, `proposals/`, `briefs/`). | `python automations/cron/scheduled_tasks.py` |

---

## 🔧 Adding New Scripts
When you or your AI assistant build a new automation script:
1. Save it in `automations/scripts/`.
2. Document its usage in `automations/CLAUDE.md`.
3. Your AI will immediately adopt it as a permanent skill in its toolbelt!
