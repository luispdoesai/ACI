# 🏗️ Engine Builder (`engine-builder/`)

> **The meta-engine: ensures every new ACI workspace is built to the same 3-tier standard as the original 8.**

The `engine-builder/` module is what fires when a user asks for a workflow or domain ACI doesn't have a folder for yet (a `podcast-engine/`, a `sponsorships/` tracker, a `finance-ops/` folder). It replaces freehand folder creation with a deterministic scaffold plus a fill-in protocol, so every module ends up the same shape: `CLAUDE.md` / `SOP.md` / `CONTEXT.md`, `examples/`, `templates/`, and staging directories named for its real workflow.

---

## 📂 Directory Structure

```text
engine-builder/
├── CONTEXT.md                    # This guide
├── CLAUDE.md                     # Spawning protocol for the AI
├── SOP.md                        # Step-by-step checklist
├── templates/                    # Blank CLAUDE.md / SOP.md / CONTEXT.md skeletons
│   ├── intake_questionnaire.md   # The systemized interview: what to ask before scaffolding
│   ├── CLAUDE_template.md
│   ├── SOP_template.md
│   └── CONTEXT_template.md
└── scripts/
    └── scaffold_engine.py        # Deterministic folder + boilerplate creator
```

---

## ⚡ How to Use It With Your AI

### Example: Spawn a brand-new workspace
> *"I want to start tracking podcast sponsorships. Spawn a new module for it."*

The AI walks the user through `templates/intake_questionnaire.md` (purpose, inputs, staging, deterministic-vs-LLM, quality bar, naming), 1-2 questions at a time, then runs `scaffold_engine.py`, fills in the generated files, and logs the new module in `brain/memory.md`.

### Example: Run the scaffold directly
```bash
python engine-builder/scripts/scaffold_engine.py sponsorships --dirs drafts,active,closed
```

---

## 🎯 What Makes It Different
- **Zero structural drift**: every module gets the identical `CLAUDE.md`/`SOP.md`/`CONTEXT.md` + `examples/`/`templates/` shape, whether the AI or a human runs the scaffold.
- **Deterministic-first**: folder and file creation is a Python script, not something re-derived from memory each time a new module is requested.
- **Content is still the AI's job**: the script only produces the skeleton and TODO markers. The AI fills in the actual protocol, tone, and rubric using `brain/` context, exactly like it would when drafting any other asset.
