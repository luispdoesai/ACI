# 📚 Brain Knowledge Base

Store your long-form company knowledge, whitepapers, case studies, past high-converting campaigns, and customer testimonials in this directory.

This folder is **not** on the always-loaded path (unlike `brain/memory.md`, `identity.md`, `voice-and-tone.md`, `icp-and-offers.md`, `rules.md`). It's read on demand: when a task needs deep domain detail this folder holds, or right after a file lands here. That's deliberate; these files can be long, and forcing them into every session's boot context would burn tokens on material most tasks don't need.

---

## Suggested Documents to Add:
1. `case_studies.md` - Real results, metrics, and customer transformation stories.
2. `product_features.md` - Detailed breakdown of features, APIs, and capabilities.
3. `competitor_analysis.md` - Market landscape and your unique differentiators.
4. `faqs.md` - Detailed answers to frequently asked technical and business questions.

The AI assistant will automatically reference files in this directory when answering detailed questions or generating in-depth content.

---

## 📥 Ingestion Rule: Dropping In a File You Already Have

When you hand the assistant a file you already have (paste it, attach it, or drop it straight into this folder), it goes through two stages, not one:

**Stage 1: Archive it here, untouched.**
Whatever you give it (a transcript, an old proposal, a whitepaper export, a case study) gets saved to `brain/knowledge/` in its original form. This is the permanent record. A summary never replaces the source; if an extraction downstream turns out wrong, you need the original still sitting here to check it against.

**Stage 2: Extract only what's operationally useful, and route it.**
The assistant reads the raw file and pulls out the pieces that actually get used in day-to-day output, filing each into the place that already consumes it:

| What's in the file | Goes to |
| :--- | :--- |
| A credibility marker, past win, bio detail | `brain/identity.md` |
| A phrase, cadence, or banned-word pattern | `brain/voice-and-tone.md` |
| An audience insight or objection counter | `brain/icp-and-offers.md` |
| A reusable past deliverable (proposal, email, post) | The relevant engine's `examples/` |
| Nothing reusable, purely reference material | Stays here as-is (that's fine; not every file needs to feed a structured file) |

Then it logs **one line** in `brain/memory.md`'s Decision Log: what was ingested, and where the extracted pieces landed. That's what makes the ingestion traceable later instead of silently rewriting your context.

**Why two stages instead of one:** storing the raw file only means it never gets referenced unless a task happens to need this exact folder. Letting the AI rewrite it into a summary only means you lose fidelity to what you actually said. Doing both keeps the source honest and makes the useful parts actually show up in the places that get read every session.
