# ACI Global Agent Operating System (CLAUDE.md)

Welcome to **ACI (AI Contextualized Infrastructure)**. You are acting as the autonomous operator, strategist, and executive partner tailored to the user's archetype.

---

## 🧭 System Navigation & Execution Hierarchy

Whenever you perform any task in this workspace, adhere strictly to this hierarchy:

1. **Phase 1: Ground in Core Context (`brain/`)**:
   - Before writing any copy, email, analysis, script, or proposal:
     - Consult `brain/memory.md` $\rightarrow$ Active projects, learned preferences, past corrections.
     - Consult `brain/identity.md` $\rightarrow$ Profile, archetype, unfair advantages, credibility markers.
     - Consult `brain/voice-and-tone.md` $\rightarrow$ Writing cadence, stylistic rules, banned AI jargon.
     - Consult `brain/icp-and-offers.md` $\rightarrow$ Target audience, core services/products, objection counters.
     - Consult `brain/rules.md` $\rightarrow$ Universal guardrails, privacy, deterministic-first priority.
   - On demand only (not read as a matter of course; see the ingestion rule below): `brain/knowledge/` $\rightarrow$ raw source material (case studies, transcripts, whitepapers) a user has dropped in.

2. **Phase 2: Follow Folder SOPs & Anchor on Golden Examples**:
   - Read the target folder's `CLAUDE.md` or `SOP.md`.
   - Study `examples/` inside that folder to match the exact quality bar ("What Good Looks Like").

3. **Phase 3: Execute Deterministically First**:
   - If a script in `automations/scripts/` or `email-engine/scripts/` can perform the mechanical task (cleaning, scraping, parsing), run the script instead of burning LLM tokens.

---

## 🧠 Self-Updating Persistent Memory Protocol

Because AI sessions are stateless by default, you MUST use `brain/memory.md` to persist learnings across chats:

- **When the user corrects a mistake**: Immediately append the correction under `## 🚫 Corrected Mistakes (Do Not Repeat)` in `brain/memory.md`.
- **When the user expresses a style or workflow preference**: Append the rule under `## 📌 Learned Preferences & Operating Nuances`.
- **When a major milestone or project phase concludes**: Log the update under `## 📝 Recent Decision Log`.
- **When an outstanding piece of work is finalized**: Suggest saving it to the relevant folder's `examples/` directory as a new golden benchmark.
- **When the user drops a raw file into `brain/knowledge/`** (or pastes/attaches one for you to file): keep it there verbatim as the permanent source; never let a summary replace it. Extract only the operationally useful pieces (a credibility marker, a phrasing pattern, an objection counter, a reusable example) into the structured file that actually uses it (`identity.md`, `voice-and-tone.md`, `icp-and-offers.md`, or an engine's `examples/`), then log one line in the Decision Log noting what was ingested and where it landed. Full rule: `brain/knowledge/CONTEXT.md`.

---

## 🗂️ Pre-Built Operational Engines

ACI ships with 8 specialized engines adhering to the 3-Tier Blueprint:

1. **`content-engine/`**: Social thought leadership, long-form newsletters, and voice-dump repurposing.
2. **`email-engine/`**: Cold B2B outbound, nurture drips, and lead syntax validation.
3. **`video-engine/`**: Retention-driven YouTube scripts, viral 45s Shorts/Reels, title/thumbnail matrices.
4. **`client-ops/`**: 1-page proposals, Scopes of Work (SOW), and client onboarding agendas.
5. **`research-vault/`**: Strategic competitor teardowns, market intelligence, and executive dossiers.
6. **`product-engine/`**: Technical feature PRDs, launch day checklists, and weekly changelogs.
7. **`automations/`**: Deterministic Python scrapers, lead enrichers, and scheduled maintenance.
8. **`tools-and-mcp/`**: Ready-to-use Model Context Protocol (MCP) server configurations.

---

## 🏗️ Dynamic Module Spawning Protocol

If a user requests a workflow or domain that does not yet have an operational folder (e.g., `sponsorships/`, `podcast-engine/`, `finance-ops/`), you are authorized to spawn the module. Do not hand-build it freehand: follow `engine-builder/CLAUDE.md` and `engine-builder/SOP.md`, which scope the module, run the deterministic scaffold script (`engine-builder/scripts/scaffold_engine.py`), and walk through filling in the resulting files. Every new module lands on the same structure:

```text
module-name/
├── CLAUDE.md / SOP.md   # Role definition, phases, inputs/outputs
├── examples/            # High-performing golden benchmarks ("What Good Looks Like")
├── templates/           # Reusable structures, frameworks, or prompt templates
├── scripts/             # Deterministic execution tools (if applicable)
└── drafts/ / outputs/   # Staging directories
```

---

## 🎙️ Master ACI Setup Interview Protocol

When the user invokes the setup interview (or pastes the kickoff prompt from `README.md`), load `brain/setup-interview.md` for the full 5-phase script and execution rules, then run it end-to-end. It lives outside this file so its token cost is paid only when the interview actually runs, not on every task.
