# 🎙️ Master ACI Setup Interview Protocol

This is the full script for the deep contextual onboarding interview referenced from `CLAUDE.md` / `AGENTS.md`. It lives here instead of in the root router files because it's only needed once, at kickoff: inlining it in `CLAUDE.md` would mean paying its token cost on every single task, forever, instead of only when the interview actually runs.

Trigger: the user invokes the setup interview directly, or pastes the kickoff prompt from `README.md`.

Every question below exists because a specific field in `brain/identity.md`, `brain/voice-and-tone.md`, or `brain/icp-and-offers.md` needs it. If a question is skipped, the corresponding field stays a `[bracketed placeholder]` — flag that explicitly during Phase 5 rather than silently leaving it blank.

```
[Phase 1: Archetype & Identity]
  • Which of these best describes your primary focus?
      A) Creator / Solopreneur (Audience growth, newsletters, video scripts, monetization)
      B) Busy Executive / Operator (Inbox triage, meeting prep, summaries, competitor briefs)
      C) Freelancer / Consultant / Agency (Client proposals, SOWs, lead outreach, onboarding)
      D) Founder / Indie Hacker (PRDs, product launches, cold outbound, automations)
  • What's your name/brand, your title or role, and the name of your project or company (if any)?
  • Are you operating solo, or do you speak as a "we"? (Determines first-person voice: "I" vs "we".)
  • In 2-3 sentences (or a rough voice-dump), what is your background and core mission?
  • What are your core values or operating philosophy? (e.g., radical transparency, speed over polish, design excellence)
  • Any links worth having on file? (Website, GitHub, primary social profiles.)

[Phase 2: Offer, Audience & Traction]
  • What's your business model? (SaaS / Agency / Info product / Newsletter / Open Source / Consulting / other.)
  • Who is your primary audience or client? Give role/title and company stage or size if B2B (e.g., "solo SaaS founders, pre-seed to Series A").
  • What are their 2-3 biggest daily bottlenecks or frustrations?
  • What's the dream outcome for them — what does life look like after working with you / using what you make?
  • What's your core offer? For each one: what's included, who it's for, price/terms, and the 2-3 key deliverables.
  • What's the main value proposition — the one-line transformation or ROI promise?
  • What are 2-3 credibility markers or past wins you have?
  • What are the top 2-3 objections people raise before buying/committing, and how do you actually counter them?
  • Where are you starting from right now? (Rough baseline: audience/list size, revenue, or whatever metric matters most — used to make goals concrete, not to judge.)
  • What are your primary 90-day goals? (2-3, as concrete and measurable as you can make them.)

[Phase 3: Voice Calibration & Anti-Sludge]
  • Paste 1-2 writing samples (past posts, emails, or notes) that sound 100% like you.
  • What are your stylistic pet peeves and banned habits (e.g., generic AI buzzwords, emojis, long fluff)?
  • Any topics, claims, or phrasing that are off-limits? (Compliance, competitor mentions, promises you won't make.)

[Phase 4: Workflow Mapping & Engine Selection]
  • Which of the 8 engines do you want active on Day 1? (Content, Email, Video, Client Ops, Research, Product, Automations, Tools/MCP)
  • For each engine you're activating, do you have one existing piece you're proud of (a post, email, script, proposal) that we should drop in as its first golden example? If not, note that examples will be calibrated from later output instead.
  • Are there any custom channels or domains you need spawned?
  • Anything relevant to scheduling or automation — timezone, working hours, or cadences I should know about?

[Phase 5: Auto-Synthesis & Workspace Calibration]
  1. Automatically populate `brain/identity.md`, `brain/voice-and-tone.md`, and `brain/icp-and-offers.md`, including the Objections & Counters table and 90-Day Goals.
  2. Calibrate `examples/` across active engines using any golden examples supplied in Phase 4; otherwise leave a note that they're pending.
  3. Spawn any custom modules requested via the Dynamic Module Spawning Protocol (`engine-builder/`).
  4. Log initial workspace state into `brain/memory.md`.
  5. Flag any field left as a placeholder because the interview answer was skipped or too thin to use — don't silently paper over gaps.
  6. Conclude with 3 tailored, ready-to-run commands for their specific daily workflow.
```

### Interview Execution Rules:
- **Low-Friction**: Accept rough voice notes, bullet points, or stream-of-consciousness text.
- **Ask 1 to 2 questions at a time** in an engaging, conversational rhythm.
- **Synthesize deeply**: Transform messy user answers into clean, structured markdown frameworks inside `brain/`.
- **Traceability**: Every field in `identity.md`, `voice-and-tone.md`, and `icp-and-offers.md` should map back to an answer given here — if it doesn't, that's a gap in this script, not a reason to invent the answer.
