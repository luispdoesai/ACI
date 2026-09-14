# Engine Spawning SOP

The deterministic checklist for standing up a new ACI module. Follow root `CLAUDE.md`'s Dynamic Module Spawning Protocol, `engine-builder/CLAUDE.md`, and this SOP together.

---

## 1. Scope the Module
Run `engine-builder/templates/intake_questionnaire.md` with the user, 1-2 questions at a time:
- [ ] Phase 1: Purpose confirmed (one-sentence goal, what a finished output looks like)
- [ ] Phase 2: Inputs & trigger confirmed (what kicks it off, on-demand vs. recurring)
- [ ] Phase 3: Staging folder name(s) confirmed (`drafts`/`published`, `outputs`, `proposals`, etc.)
- [ ] Phase 4: Deterministic-vs-LLM confirmed (does it need a `scripts/` folder)
- [ ] Phase 5: Quality bar / real example captured, or gap noted for later
- [ ] Phase 6: Module slug confirmed (kebab-case, not already a top-level folder)

## 2. Scaffold
- [ ] Run `python engine-builder/scripts/scaffold_engine.py <slug> --dirs <...> [--scripts]`
- [ ] Confirm the script reported success and no existing folder was overwritten

## 3. Fill In Content
- [ ] Replace every TODO block in `<slug>/CLAUDE.md`
- [ ] Replace every TODO block in `<slug>/SOP.md`
- [ ] Replace every TODO block in `<slug>/CONTEXT.md`
- [ ] Add at least one file to `<slug>/examples/`, a real sample, or note the gap in `brain/memory.md`

## 4. Register
- [ ] Log the new module in `brain/memory.md` Recent Decision Log
- [ ] Run `python automations/scripts/index_workspace.py`
- [ ] Add the module to the engines table in `README.md` if it's a standing workflow

## 5. Quality Gate
- [ ] No TODO or placeholder text remains in any committed file
- [ ] Folder structure matches an existing engine: `CLAUDE.md` + `SOP.md` + `CONTEXT.md` + `examples/` + `templates/`
