# Module Intake Questionnaire

The systemized interview the AI runs with the user before scaffolding any new module. Ask **1-2 questions at a time**, low-friction (bullet points or a voice-dump answer are fine, don't force complete sentences). Phases 1-4 are required before scaffolding; Phase 5 can be filled in later if the user has no example yet.

---

## Phase 1: Purpose
1. In one sentence, what does this module do for you?
2. What does a finished output actually look like? (a LinkedIn post, a signed proposal, a spreadsheet, a status report...)

→ Feeds the **Primary Purpose** section of the new `CLAUDE.md`.

---

## Phase 2: Inputs & Trigger
3. What raw input kicks this off? (a voice note, a call transcript, a lead list, a code diff, or nothing, it's generated from scratch)
4. Is this on-demand (you ask when you need it), or does it run on a recurring cadence (daily/weekly sweep via `automations/cron/`)?

→ Feeds the **Execution Protocol** step 1 (intake) of the new `CLAUDE.md`/`SOP.md`.

---

## Phase 3: Workflow & Staging
5. What stages does a piece of work pass through before it's "done"? (e.g. `drafts` → `published`; `proposals` only, one-shot; `active` → `closed`)

→ Maps directly to the `--dirs` flag on `scaffold_engine.py`. If there's genuinely no multi-stage lifecycle, use a single `outputs/` dir.

---

## Phase 4: Deterministic vs LLM
6. Is any part of this mechanical or repeatable, i.e. something a Python script should do instead of the AI drafting it (parsing, scraping, validating, formatting, computing)?

→ A "yes" adds the `--scripts` flag on `scaffold_engine.py`.

---

## Phase 5: Quality Bar
7. Do you have a real example of this kind of finished work already? (paste it, or point to a file/link)
8. What's non-negotiable before something counts as "done"? (a tone rule, a required section, a fact-check step, a length cap...)

→ Phase 5 seeds `<slug>/examples/` (if a sample exists) and the **Pre-Publish Quality Rubric** in the new `SOP.md`. If no example exists yet, note the gap in `brain/memory.md` per `engine-builder/CLAUDE.md` Step 5.

---

## Phase 6: Naming
9. Propose a module slug (kebab-case, e.g. `podcast-engine`, `finance-ops`) from the answers above and let the user correct it.

→ The positional argument to `scaffold_engine.py`, and the name used everywhere in the generated files.

---

## After the Interview
Run the scaffold with the mapped answers, e.g.:
```bash
python engine-builder/scripts/scaffold_engine.py <phase-6-slug> --dirs <phase-3-stages> [--scripts if phase-4 is yes]
```
Then continue with `engine-builder/CLAUDE.md` Steps 4-6 (fill placeholders, seed examples, register the module).
