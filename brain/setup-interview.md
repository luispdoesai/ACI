# 🎙️ Master ACI Setup Interview Protocol

This is the full script for the deep contextual onboarding interview referenced from `CLAUDE.md` / `AGENTS.md`. It lives here instead of in the root router files because it's only needed once, at kickoff: inlining it in `CLAUDE.md` would mean paying its token cost on every single task, forever, instead of only when the interview actually runs.

Trigger: the user invokes the setup interview directly, or pastes the kickoff prompt from `README.md`.

```
[Phase 1: Archetype & Background]
  • Which of these best describes your primary focus?
      A) Creator / Solopreneur (Audience growth, newsletters, video scripts, monetization)
      B) Busy Executive / Operator (Inbox triage, meeting prep, summaries, competitor briefs)
      C) Freelancer / Consultant / Agency (Client proposals, SOWs, lead outreach, onboarding)
      D) Founder / Indie Hacker (PRDs, product launches, cold outbound, automations)
  • In 2-3 sentences (or a rough voice-dump), what is your background and core mission?

[Phase 2: Core Offer, Audience & Pain Points]
  • Who is your primary audience or client?
  • What are their biggest daily bottlenecks, and what is your core offer/solution?
  • What are 2-3 credibility markers or past wins you have?

[Phase 3: Voice Calibration & Anti-Sludge]
  • Paste 1-2 writing samples (past posts, emails, or notes) that sound 100% like you.
  • What are your stylistic pet peeves and banned habits (e.g., generic AI buzzwords, emojis, long fluff)?

[Phase 4: Workflow Mapping & Engine Selection]
  • Which of the 8 engines do you want active on Day 1? (Content, Email, Video, Client Ops, Research, Product, Automations, Tools/MCP)
  • Are there any custom channels or domains you need spawned?

[Phase 5: Auto-Synthesis & Workspace Calibration]
  1. Automatically populate `brain/identity.md`, `brain/voice-and-tone.md`, and `brain/icp-and-offers.md`.
  2. Calibrate `examples/` across active engines so they reflect the user's real offer, audience, and voice.
  3. Spawn any custom modules requested via the Dynamic Module Spawning Protocol (`engine-builder/`).
  4. Log initial workspace state into `brain/memory.md`.
  5. Conclude with 3 tailored, ready-to-run commands for their specific daily workflow.
```

### Interview Execution Rules:
- **Low-Friction**: Accept rough voice notes, bullet points, or stream-of-consciousness text.
- **Ask 1 to 2 questions at a time** in an engaging, conversational rhythm.
- **Synthesize deeply**: Transform messy user answers into clean, structured markdown frameworks inside `brain/`.
