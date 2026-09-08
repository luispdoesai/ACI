# 🧠 AI Contextualized Infrastructure (ACI)

> **The Open-Source Operational Hub for Creators, Busy Operators, Freelancers, and Technical Builders.**

ACI transforms any AI Agent (**Claude Code**, **Gemini**, **Antigravity**, **Cursor**) into a persistent, context-aware operational team.

Instead of re-explaining your background, brand voice, target clients, and workflows in every new chat, ACI provides a central **Brain** (`brain/`) and dedicated **Operational Engines** that adapt to your exact daily work.

This README covers three things: **why the architecture works**, **the proof it produces calibrated output**, and **how to actually run it**.

---

## 🎯 Built For Practical Everyday Work

| Archetype | How ACI Empowers You | Primary Engines |
| :--- | :--- | :--- |
| **🎨 Creators & Solopreneurs** | Turn raw voice dumps into high-performing newsletters, LinkedIn posts, and viral video scripts in your authentic voice. | `content-engine/`<br>`video-engine/` |
| **⚡ Busy Executives & Operators** | Get 30-second meeting cheat sheets, instant email drafts, and competitor teardowns without AI fluff. | `research-vault/`<br>`email-engine/` |
| **💼 Freelancers & Agencies** | Auto-generate winning 1-page proposals, Scopes of Work (SOW), and client kickoff agendas directly from call notes. | `client-ops/`<br>`research-vault/` |
| **🚀 Founders & Technical Builders** | Write technical PRDs, run cold outbound campaigns, scrape leads, and connect APIs/MCPs with zero token waste. | `product-engine/`<br>`automations/` |

> **These 8 engines are curated starting presets, not a fixed ceiling.** They cover the most common workflows, but the folder structure isn't special-cased in code — it's just a convention your AI assistant follows. If your work needs something these don't cover, ask it to spawn a new module (a `podcast-engine/`, a `sponsorships/` tracker, a `finance-ops/` folder — whatever your actual workflow is) and it will build one on the same 3-tier structure below. See the **Dynamic Module Spawning Protocol** in `CLAUDE.md` / `AGENTS.md`.

---

## 🧬 Why This Architecture Works: System & Token Economics

Operating AI systems generally follows one of three architectural approaches: single-session chat windows, autonomous agent frameworks, or file-based contextualized infrastructure.

### Architectural Comparison: Chat vs. Autonomous Agents vs. ACI

| Dimension | Standard Chatbot (Web UI) | Autonomous Agent Frameworks (CrewAI, LangChain, AutoGPT) | ACI (Contextualized Infrastructure) |
| :--- | :--- | :--- | :--- |
| **Context Persistence** | Stateless. Manual re-prompting required every session. | In-memory session state or external vector database. | Git-tracked markdown files in `brain/`. Transparent and persistent. |
| **Execution Reliability** | High manual burden. User supervises each prompt turn. | Low to moderate. Autonomous loops can enter recursive retries or hallucinate tools. | High. Deterministic Python handles mechanical tasks; LLM handles synthesis. |
| **Token Efficiency** | Poor. Resends growing chat histories with each prompt turn. | Poor. Autonomous thought loops and heavy tool call traces burn tokens rapidly. | Optimal. Zero-token Python utilities offload data tasks; prompt caching lowers costs up to 90%. |
| **Observability & State** | Visible in chat window, lost on refresh. | Opaque. State is hidden inside framework abstractions and graph objects. | Completely transparent. Every asset, status, and learning lives as plain text on disk. |
| **Infrastructure Overhead** | Zero setup. | High. Requires vector DBs, Python orchestration libraries, and complex schema configs. | Zero external dependencies. Standard markdown files and vanilla Python scripts. |

---

### Core Mechanics of the ACI Approach

#### 1. Persistent Context Layer (`brain/`)
Instead of pasting business background, style boundaries, and ICP details into prompts, the model references `brain/` on demand. Because core identity and rule files stay stable, LLM providers cache these tokens, reducing input costs by up to 90% on subsequent turns.

#### 2. Deterministic Offloading (Zero-Token Execution)
Mechanical operations do not require LLM inference:
- Data ingestion, web scraping, email syntax cleaning, and workspace indexing run as native Python scripts in `automations/scripts/`.
- Local script execution consumes 0 API tokens and executes in milliseconds on local CPU.

#### 3. Map and Territory Retrieval (Lazy Loading)
Autonomous agents frequently fail by loading dozens of raw files into context, causing retrieval noise and context saturation:
- ACI separates discovery from execution.
- The Map (`brain/workspace_index.md`) provides a 1-line index of every asset and active learning.
- The Territory (`<engine>/examples/` and `<engine>/SOP.md`) is read strictly when an agent performs a task in that specific domain.

#### 4. Closed-Loop Failure Recovery and Benchmark Promotion
- Failure Prevention: When a script breaks or output requires correction, the failure mode is logged to `brain/memory.md` under `## 🚫 Corrected Mistakes`. Subsequent sessions check this ledger before generating work.
- Quality Anchoring: When a deliverable meets production quality, it is stored in that module's `examples/` directory. Future prompts use these proven assets as few-shot references.

---

### Token & Operational Cost Breakdown

| Operation | Standard Chatbot | Autonomous Agent Framework | ACI Architecture | Token & Cost Impact |
| :--- | :--- | :--- | :--- | :---: |
| **Workspace Orientation** | Re-type background (~1,500 tokens/session) | Loads system prompts + schema overhead (~3,000 tokens) | Cached `brain/` context | **~75% to 90% savings** |
| **Workspace Cataloging** | Manual file discovery | Multi-step agent tool calling loop (~50,000+ tokens) | Native Python scan (`index_workspace.py`) | **100% free (0 tokens, $0.00)** |
| **Raw Data Cleaning** | Paste raw CSV/HTML dumps (~25,000 tokens) | LLM-based JSON extraction loops (~20,000 tokens) | Python regex scripts clean data before model sees it | **~95% savings** |
| **Error Corrections** | Multi-turn chat corrections resending full context | Recursive self-retry loops often fail or loop indefinitely | Single write to `memory.md` prevents repeat errors | **~80% savings** |

> **On these numbers**: the prompt-caching figure (up to 90%) matches [Anthropic's published prompt-caching discount](https://docs.claude.com/en/docs/build-with-claude/prompt-caching) for cached input tokens. The rest are order-of-magnitude illustrations based on typical workflow shapes, not measured benchmarks — actual savings depend on your prompt sizes and how much of a task is deterministic Python vs. LLM-driven.

---

## 🔬 The Proof

Architecture claims are cheap. Here's an actual before/after — not a hypothetical.

**Without a `brain/` folder** (a fresh chat, generic prompt: *"write me a LinkedIn post about AI infrastructure"*):

> "In today's fast-paced digital world, AI is a game-changer for businesses looking to unlock new levels of productivity. By leveraging the power of AI, teams can revolutionize how they work and stay ahead of the competition."

Vague, no numbers, and it hits several of the exact phrases `brain/voice-and-tone.md` explicitly bans.

**With ACI's `brain/` context** — this is the real, unedited golden benchmark stored at [`content-engine/examples/linkedin_golden.md`](content-engine/examples/linkedin_golden.md):

> "Most founders use AI like an expensive Google search bar.
>
> The top 1% use AI as an autonomous operational department.
>
> Here is the exact 4-tier infrastructure we built to handle 80% of our daily operations..."

Specific framework, concrete claim, zero banned words — because the model read `voice-and-tone.md` and the golden examples before writing a single line, per the execution protocol in `content-engine/CLAUDE.md`.

**Verify it yourself**: every example referenced in this README is a real file in this repo, not copy staged for marketing. Open `content-engine/examples/`, `email-engine/examples/`, `client-ops/examples/`, `research-vault/examples/`, `product-engine/examples/`, or `video-engine/examples/` and check.

---

## ⚡ Setup

### Prerequisites
- One of: **Claude Code**, **Gemini CLI**, **Antigravity**, or **Cursor** (any AI coding assistant that can read local files and run shell commands).
- **Python 3.9+** — only needed if you plan to run the scripts in `automations/` and `email-engine/scripts/` (lead cleaning, web scraping, workspace indexing). Not required just to draft content.
- **Git**, to clone the repo.

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ACI.git
cd ACI
```

### 2. (Optional) Install Python dependencies
Only needed if you'll run the automation scripts:
```bash
pip install -r requirements.txt
```

### 3. Copy & Paste the Kickoff Prompt
Open your AI assistant in this directory (`claude`, `gemini`, `cursor`, etc.) and paste the following prompt:

```markdown
Run the ACI Deep Setup Interview. Read `brain/rules.md` and `CLAUDE.md`, then interview me step-by-step to customize this workspace.

Follow this protocol:
1. Ask 1-2 focused questions at a time across the 5 phases:
   - Phase 1: Archetype & Background (Creator, Busy Operator, Freelancer, or Founder + Core Mission).
   - Phase 2: Audience & Offer (Target persona, 3 daily headaches, core services/products, credibility proof).
   - Phase 3: Voice Calibration & Anti-Sludge (Paste 1-2 writing samples, list pet peeves and banned words).
   - Phase 4: Workflow Mapping & Engine Selection (Select active engines, detect custom channels needed).
   - Phase 5: Auto-Synthesis & Workspace Calibration (Populate brain/, calibrate engine examples/, log initial state to memory.md, deliver 3 starter commands).
2. Accept rough voice-note transcripts, messy bullets, or brief answers.
3. Automatically populate `brain/identity.md`, `brain/voice-and-tone.md`, and `brain/icp-and-offers.md`.
4. Calibrate the `examples/` across active engines so they feature my real offers, audience, and voice.
5. If my workflow requires custom modules (e.g., `podcast-engine/`, `sponsorships/`), autonomously spawn them using the 3-Tier Blueprint.
6. Conclude with 3 tailored, ready-to-run commands for my specific daily workflow.

Begin with Phase 1: Archetype & Background.
```

### 4. Verify it worked
Two checks that setup actually landed:
- Open `brain/identity.md` — it should describe *your* business, not still say `[Your Name / Brand Name]`.
- Run the workspace sweep to confirm the indexer picks up your new context:
  ```bash
  python automations/cron/scheduled_tasks.py
  ```
  This regenerates `brain/workspace_index.md` and reports what's pending in each engine's staging folder. Zero errors means the workspace is wired correctly.

---

## 🏗️ Folder Hierarchy & Navigation

Every folder contains its own `CONTEXT.md`, `CLAUDE.md`, or `SOP.md` defining what the folder does, step-by-step instructions for the AI to follow, and golden benchmark examples:

```text
ACI/
├── README.md                      # Main project hub & kickoff setup prompt
├── CLAUDE.md / AGENTS.md          # Global AI operating guidelines & navigation
│
├── brain/                         # 🧠 The Core Context Layer (Source of Truth)
│   ├── CONTEXT.md                 # Guided overview of the Brain layer
│   ├── memory.md                  # Persistent AI memory (learnings, corrections, session log)
│   ├── workspace_index.md         # Generated high-level asset map & watchlist
│   ├── workspace_index.json       # Machine-readable structured asset catalog
│   ├── identity.md                # Bio, mission, archetype, positioning, 90-day targets
│   ├── voice-and-tone.md          # Writing rules, vocabulary, banned clichés, formatting
│   ├── icp-and-offers.md          # Target audience, pain points, core offers, pricing
│   ├── rules.md                   # Universal AI guardrails & operating constraints
│   └── knowledge/                 # Meeting frameworks, case studies, playbooks
│       └── CONTEXT.md             # Guide to long-form knowledge assets
│
├── content-engine/                # ✍️ Content Creation & Repurposing System
│   ├── CONTEXT.md                 # Guided overview & quick prompts for Content Engine
│   ├── CLAUDE.md / SOP.md         # Step-by-step SOP for drafting posts & newsletters
│   ├── examples/                  # Golden standards ("What Good Looks Like")
│   ├── templates/                 # Voice-dump repurposer, hook library, post frameworks
│   └── drafts/ & published/       # Content staging pipeline
│
├── email-engine/                  # ✉️ Inbound & Outbound Email Operations
│   ├── CONTEXT.md                 # Guided overview & quick prompts for Email Engine
│   ├── CLAUDE.md / SOP.md         # Cold outreach & sequence generation SOPs
│   ├── examples/                  # Golden cold emails, follow-ups, objection handlers
│   ├── sequences/                 # Multi-touch drip templates
│   └── scripts/validate_leads.py  # Python lead syntax cleaner & deduplicator
│
├── video-engine/                  # 🎬 Video Production & Retention System
│   ├── CONTEXT.md                 # Guided overview & quick prompts for Video Engine
│   ├── CLAUDE.md / SOP.md         # Hook-to-retention framework & visual cue SOPs
│   ├── examples/                  # Golden 8-min YouTube script & 45s viral Short
│   ├── templates/                 # 10-min YouTube framework, title & thumbnail matrix
│   └── scripts/                   # Staging directory for generated video scripts
│
├── client-ops/                    # 💼 Proposals, Scopes of Work & Client Onboarding
│   ├── CONTEXT.md                 # Guided overview & quick prompts for Client Ops
│   ├── CLAUDE.md / SOP.md         # Proposal generation SOP & pricing defense rules
│   ├── examples/                  # Golden winning 1-page proposal
│   ├── templates/                 # 1-page proposal, Scope of Work (SOW), kickoff agenda
│   └── proposals/                 # Staging directory for client deliverables
│
├── research-vault/                # 🔍 Market & Competitor Intelligence
│   ├── CONTEXT.md                 # Guided overview & quick prompts for Research Vault
│   ├── CLAUDE.md / SOP.md         # Research teardown SOP & evidence citation rules
│   ├── examples/                  # Golden strategic competitor teardown
│   ├── templates/                 # Competitor audit & executive dossier templates
│   └── briefs/                    # Staging directory for saved research reports
│
├── product-engine/                # 🚀 Product Specs, Launches & Changelogs
│   ├── CONTEXT.md                 # Guided overview & quick prompts for Product Engine
│   ├── CLAUDE.md / SOP.md         # PRD authoring & launch day sequencing
│   ├── examples/                  # Golden technical feature PRD
│   ├── templates/                 # Product launch checklist & weekly changelog format
│   └── specs/                     # Staging directory for feature specifications
│
├── automations/                   # ⚡ Python Scripts & Workflow Utilities
│   ├── CONTEXT.md                 # Guided overview & tool execution guide
│   ├── CLAUDE.md                  # Guidelines for writing & running automations
│   ├── scripts/                   # Scrapers, lead enrichers, workspace indexer
│   └── cron/                      # Scheduled tasks & maintenance utilities
│
└── tools-and-mcp/                 # 🔌 Tooling Hub & Protocol Configurations
    ├── CONTEXT.md                 # Guided overview & MCP setup instructions
    ├── CLAUDE.md                  # Tool discovery & execution guidelines
    └── mcp-configs/               # Ready-to-use MCP server configs (Stripe, Supabase, Brave Search)
```

---

## 📋 The Standard 3-Tier Blueprint

Every engine folder — including the 8 presets and any custom module you spawn — adheres to the same 3-tier structure:
1. **`CLAUDE.md` / `SOP.md` (The Mind)**: Explicit role, phase-by-phase workflow, input/output specifications.
2. **`examples/` (The Golden Standard)**: Few-shot examples of what exceptional output looks like.
3. **`templates/` & `scripts/` (The Hands)**: Reusable frameworks and deterministic code to execute the work cleanly.

**Building your own module**: this isn't a hardcoded plugin system — it's a folder convention. To add a domain the presets don't cover, just tell your AI assistant what you need (e.g. *"I run a podcast, spawn a podcast-engine/ module"*). It will create the folder, write a `CLAUDE.md`/`SOP.md` for that domain, and stage `examples/`, `templates/`, and a staging directory — the exact same shape as `content-engine/` or `client-ops/`. Once it exists, it's a first-class engine: reference it from `brain/memory.md`, extend its `examples/` over time, and it behaves identically to a preset.

---

## 🧭 How ACI Actually Works (Execution Hierarchy)

Every time your AI assistant does a task in this workspace, it follows the same three-step order — this is the actual logic defined in `CLAUDE.md`/`AGENTS.md`, not a black box:

1. **Ground in Core Context**: Before writing anything, it reads `brain/memory.md` (active projects, past corrections), `brain/identity.md`, `brain/voice-and-tone.md`, `brain/icp-and-offers.md`, and `brain/rules.md`.
2. **Follow the Folder's SOP**: It reads that engine's `CLAUDE.md`/`SOP.md` and studies `examples/` to match the quality bar, before drafting anything new.
3. **Execute Deterministically First**: If a script in `automations/scripts/` or `<engine>/scripts/` can do the task mechanically (cleaning, scraping, parsing), it runs the script instead of burning LLM tokens on it.

This is why the kickoff interview matters: skip it, and step 1 has nothing real to ground on — every engine will fall back to generic output because `brain/` is still template placeholders.

---

## 💡 How to Work With ACI Day-to-Day

Once the kickoff interview is complete, you simply converse with your AI naturally:

- **Turn a brain dump into content**:
  > *"Take these rough call notes and turn them into 1 newsletter and 2 LinkedIn posts using content-engine templates."*
- **Prepare for an upcoming meeting**:
  > *"Research Acme Corp and generate a 1-page executive brief in research-vault/ using our meeting prep framework."*
- **Create a client proposal**:
  > *"Draft a 1-page proposal in client-ops/ for a $3,500 automation pipeline based on my notes."*
- **Clean a list of leads**:
  > *"Run validate_leads.py on leads.csv to clean invalid emails and deduplicate the list."*
- **Teach the AI a new rule**:
  > *"Remember: never use emojis in cold emails, and keep all subject lines under 4 words."* $\rightarrow$ The AI updates `brain/memory.md` immediately.

---

## 📄 License
MIT License. Open source and free for individuals, creators, and teams.
