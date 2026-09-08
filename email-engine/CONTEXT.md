# ✉️ Email Engine (`email-engine/`)

> **Your Outbound Sales Copywriter, Lead Cleaner, and Sequence Architect.**

The `email-engine/` is built to craft high-conversion B2B cold outreach campaigns, multi-touch nurture drips, and customer onboarding sequences while maintaining high deliverability.

---

## 📂 Directory Structure

```text
email-engine/
├── README.md                  # This guide
├── CLAUDE.md / SOP.md         # Deliverability rules and copywriting standards
├── examples/                  # Golden benchmarks ("What Good Looks Like")
│   ├── cold_email_golden.md   # Sub-100 word high-response cold email benchmarks
│   └── follow_up_golden.md    # Multi-touch bump and break-up email benchmarks
├── sequences/                 # Multi-touch drip templates
│   ├── cold_outreach_5step.md # 5-touch B2B cold campaign blueprint
│   └── welcome_onboarding.md  # 3-part customer onboarding sequence
└── scripts/                   # Deterministic Python tools
    └── validate_leads.py      # Lead cleaner, deduplicator, and syntax validator
```

---

## ⚡ How to Use It With Your AI

### Example 1: Clean & Validate a Lead List (Zero Tokens)
> *"Run `python email-engine/scripts/validate_leads.py leads.csv leads_clean.csv` to remove duplicate rows and invalid email addresses."*

### Example 2: Generate Hyper-Personalized Cold Emails
> *"Draft a 3-touch cold email sequence targeting VP of Engineering prospects at Series A startups based on our core offer in `brain/icp-and-offers.md`. Keep each email under 90 words."*

### Example 3: Write a Customer Onboarding Drip
> *"Customize the `welcome_onboarding.md` sequence for new users signing up for our workspace. Add our setup prompt as the primary CTA."*

---

## 🛡️ Deliverability Guardrails Enforced
- **Strict Word Limit**: 75–125 words max for cold emails (optimized for mobile scanning).
- **Zero Spam Triggers**: No tracking links on touch 1, max 1 clean URL, and short lowercase subject lines (2–4 words).
