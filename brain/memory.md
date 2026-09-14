# Persistent Memory & Session Log

> *This file acts as the AI's persistent long-term memory across chat sessions. The AI automatically updates this file when you provide corrections, declare new project priorities, or adjust preferences.*

---

## 🧠 Active Focus & Ongoing Projects
- **Current Sprint Focus**: Workspace initialization & setup.
- **Key Milestones**: Run kickoff interview, calibrate brain context, activate primary operational engines.
- **Workspace Navigation Map**: Generated asset index available at [`workspace_index.md`](workspace_index.md) (`workspace_index.json`).

---

## 📌 Learned Preferences & Operating Nuances
- Use direct, engineering-focused language with zero marketing hype or declarative fluff.
- Always compare systems through concrete technical trade-offs (token economics, state management, failure modes).

---

## 🚫 Corrected Mistakes (Do Not Repeat)
- Never use em-dashes (—).
- Never use sweeping generalizations or openers like "Most people", "Most users", or guru-style hooks.
- Avoid preachy or overly declarative sentences. Keep copy practical and factual.

---

## 📝 Recent Decision Log
- `2026-09-01`: Initialized ACI open-source framework with 8 operational engines and 3-Tier Blueprint.
- `2026-09-05`: Implemented deterministic workspace indexer (`automations/scripts/index_workspace.py`) & linked auto-sweep to `brain/workspace_index.md`.
- `2026-09-10`: Integrated empirical research and academic foundations matrix into `README.md` to formally document system design principles.
- `2026-09-11`: Built `automations/scripts/archive_memory.py` and wired it into the daily sweep. Decision Log entries older than 90 days now auto-archive to `brain/archive/decision_log_<year>.md`; Corrected Mistakes and Learned Preferences are never pruned.
- `2026-09-11`: Built `engine-builder/` (a systemized scaffold + intake questionnaire for spawning new modules) and wired the root Dynamic Module Spawning Protocol to it instead of freehand folder creation.
- `2026-09-12`: Changed `archive_memory.py` to file archives per quarter (`decision_log_<year>_Q<n>.md`) instead of per year, so a resurfacing old decision is easier to grep to a narrower window. Verified only the Decision Log section is ever archived; Corrected Mistakes and Learned Preferences already passed through untouched.
- `2026-09-14`: Built the `brain/knowledge/` file drop-in ingestion rule (archive raw file as-is, extract only operationally useful pieces into `identity.md`/`voice-and-tone.md`/`icp-and-offers.md`/an engine's `examples/`, log the ingestion here) and wired a short pointer into `CLAUDE.md`/`AGENTS.md`. Also relocated the full Setup Interview script out of `CLAUDE.md`/`AGENTS.md` into `brain/setup-interview.md`, shrinking both always-loaded router files from 106 to 73 lines, since the script is only needed once at kickoff, not on every task. README updated with a "Why the Root Files Stay Thin" section documenting the split for new clones.
- `2026-09-14`: Pre-commit clone-readiness pass. Found `automations/scripts/index_workspace.py` was baking absolute `file://` links to the local machine's path into the committed `brain/workspace_index.md`, so a fresh clone shipped links pointing at a path that doesn't exist on any other machine. Fixed the generator to emit portable `../<path>` relative links instead, and regenerated the index. Verified no secrets/credentials are tracked, every path referenced in `README.md`/`CLAUDE.md`/`AGENTS.md` exists on disk, and the full sweep (`automations/cron/scheduled_tasks.py`) runs clean with zero errors.
