# 🧠 The Brain (`brain/`)

> **The Central Source of Truth for Your AI Operating System.**

The `brain/` directory is the single most important folder in ACI. It stores your persistent context, identity, voice, ideal customer profiles, and operating boundaries.

Instead of typing long, repetitive background prompts in every chat session, any AI operating in this workspace (**Claude Code**, **Gemini**, **Cursor**, **Antigravity**) automatically reads these files first to calibrate its reasoning and tone.

---

## 📂 File Breakdown & Guide

| File | Purpose | Who Updates It? |
| :--- | :--- | :--- |
| **[`identity.md`](identity.md)** | Your bio, background, company mission, unfair advantages, and 90-day targets. | Setup Interview or manually by you. |
| **[`voice-and-tone.md`](voice-and-tone.md)** | Stylistic rules, sentence rhythm, and the non-negotiable **banned clichés list** (no *delve*, *game-changer*, *unleash*). | Setup Interview or manually by you. |
| **[`icp-and-offers.md`](icp-and-offers.md)** | Target customer personas, visceral daily headaches, core offers, pricing tiers, and objection counters. | Setup Interview or manually by you. |
| **[`rules.md`](rules.md)** | Universal operating constraints: security (zero credentials in code), zero-token deterministic priority, and quality rubrics. | Global workspace rules (rarely edited). |
| **[`memory.md`](memory.md)** | The AI's **persistent cross-session memory**: tracks active projects, learned user preferences, and corrected mistakes so the AI never repeats them. | Automatically updated by the AI during work. |
| **[`knowledge/`](knowledge/)** | Repository for long-form case studies, whitepapers, meeting frameworks, and reference playbooks. | You or the AI when saving research. |

---

## 🔄 How the AI Uses the Brain

Whenever you ask the AI to perform a task:
1. **It checks `brain/memory.md`** for active priorities and past user feedback.
2. **It references `brain/identity.md` & `brain/voice-and-tone.md`** to sound authentically like you.
3. **It consults `brain/icp-and-offers.md`** to speak directly to your customer's pain points.
4. **It checks `brain/rules.md`** to make sure it doesn't leak secrets or waste tokens.

---

## 💡 Quick Tips for Users
- **Keep it updated**: If your pricing or positioning changes, edit `icp-and-offers.md`. The AI adapts immediately on its next turn.
- **Teaching the AI**: When the AI makes a stylistic mistake, say *"Remember: don't do that again, log it in memory"*—it will automatically append the rule to `memory.md`.
