# Operating Rules & System Constraints

This file defines the non-negotiable boundaries, technical constraints, and operating standards for all AI interactions within ACI.

---

## 1. Security & Secrets Management
- **Zero Credentials in Code**: Never commit API keys, database passwords, or personal access tokens into markdown, code, or logs.
- **Environment Variables**: Always use `.env` and reference credentials via `os.environ.get("KEY_NAME")` in Python or `process.env.KEY_NAME` in JS.
- **Data Privacy**: Do not store sensitive customer PII in plain text markdown files.

---

## 2. Token & Compute Efficiency
- **Deterministic First**: If a task can be done with regular Python code (regex, CSV parsing, basic math, API query), do not use an LLM for it.
- **Concise Outputs**: Avoid conversational filler ("Certainly!", "I'd be happy to help with that"). Jump straight to the actionable output.
- **Targeted Edits**: Only modify the specific lines or files requested; do not rewrite entire files unnecessarily.

---

## 3. Quality & Consistency Guardrails
- **Grounding in Context**: If an answer relies on brand positioning, audience pain points, or product pricing, look up `brain/identity.md` and `brain/icp-and-offers.md` first.
- **Respect Voice & Tone**: Adhere strictly to the guidelines and banned phrase list in `brain/voice-and-tone.md`.
- **Review Before Finalizing**: When creating deliverables (posts, emails, code), verify the output against the `examples/` folder in the relevant engine.

---

## 4. File Organization & Cleanliness
- **Keep Folders Organized**: New drafts go to `drafts/`, sent/published items move to `published/`.
- **Preserve System Blueprints**: Keep all `CLAUDE.md`, `SOP.md`, and `examples/` files intact when generating domain assets.
