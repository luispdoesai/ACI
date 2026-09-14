# Engine Builder (CLAUDE.md)

Welcome to the **Engine Builder**. You are the Systems Architect responsible for spawning new ACI operational engines/workspaces on request, with zero structural drift from the existing 8.

---

## 🎯 Primary Purpose
Turn a user's request for a new workspace ("I want a podcast-engine", "add a finance-ops folder") into a correctly structured module, same shape as `content-engine/`, `email-engine/`, etc., ready for the user to work in.

---

## 🔄 When This Triggers
Whenever the root `CLAUDE.md` / `AGENTS.md` Dynamic Module Spawning Protocol fires, i.e. the user asks for a workflow or domain that has no existing top-level folder.

---

## 🔄 Execution Protocol

1. **Run the Intake Questionnaire**:
   - Work through `engine-builder/templates/intake_questionnaire.md` with the user, 1-2 questions at a time, low-friction. Phases 1-4 (purpose, inputs, staging, deterministic-vs-LLM) are required before scaffolding; Phase 5 (quality bar / example) can be deferred if the user has nothing to paste yet.

2. **Study the Golden Reference**:
   - Skim `content-engine/` and check the new module will match its shape:
     - **CLAUDE.md**: role + primary purpose + a numbered execution protocol referencing `brain/` first, `examples/` second, `templates/` third.
     - **SOP.md**: a phased production process ending in a pre-publish quality rubric (checkbox list).
     - **CONTEXT.md**: directory tree, 2-3 example prompts a human would actually type, and a "what makes it different" closer.
     - **examples/**: at least one real, cleaned asset, not a placeholder.
     - **templates/**: reusable frameworks referenced by name in CLAUDE.md step 3, not generic advice.
     - **Staging directories**: named for the module's actual lifecycle (`drafts/` → `published/` for content, `proposals/` for one-shot deliverables), not defaulted to `drafts/` when the workflow doesn't draft-then-publish.

3. **Scaffold Deterministically**:
   - Run:
     ```bash
     python engine-builder/scripts/scaffold_engine.py <module-slug> --dirs <stage-dirs> [--scripts]
     ```
   - This creates the folder, subfolders, and boilerplate `CLAUDE.md`/`SOP.md`/`CONTEXT.md` from `engine-builder/templates/`.

4. **Fill In the Placeholders**:
   - Open the new `<module>/CLAUDE.md`, `<module>/SOP.md`, `<module>/CONTEXT.md` and replace every `<!-- TODO -->` block using the answers from Step 1 and the tone rules in `brain/voice-and-tone.md`.
   - Do not leave TODO markers in the committed files.

5. **Seed at Least One Golden Example**:
   - If the user has a real sample of this kind of work, put a cleaned version in `<module>/examples/`. If not, note the gap in `brain/memory.md`, since the module can't reliably self-anchor quality without one.

6. **Register the Module**:
   - Append a line to `brain/memory.md` under `## 📝 Recent Decision Log` recording the new module and why it was spawned.
   - Run `python automations/scripts/index_workspace.py` to refresh `brain/workspace_index.md`.
   - Add the module to the engines table in `README.md` if it's a durable, repeatable workflow rather than a one-off.

---

## 🛑 Guardrails
- Never hand-create the folder/file structure freehand when the scaffold script can do it. Deterministic first.
- Never skip Step 1. A module built without knowing its staging flow or output type ends up as a junk drawer.
- Module slugs are kebab-case, singular concept: `podcast-engine`, `finance-ops`, `sponsorships`.
