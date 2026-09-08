# 🚀 Product Engine (`product-engine/`)

> **Your Technical Product Manager, PRD Author, and Launch Strategist.**

The `product-engine/` is built for software engineers, SaaS founders, and indie hackers. It streamlines the creation of developer-ready Product Requirement Documents (PRDs), feature specifications, Product Hunt launch day copy, and weekly product changelogs.

---

## 📂 Directory Structure

```text
product-engine/
├── CONTEXT.md                 # This guided context file
├── CLAUDE.md / SOP.md         # PRD authoring and launch sequencing standards
├── examples/                  # Golden benchmarks ("What Good Looks Like")
│   └── feature_prd_golden.md  # Zero-fluff technical feature PRD format
├── templates/                 # Reusable frameworks
│   ├── product_launch_checklist.md # Launch day checklist and maker comment
│   └── weekly_changelog.md    # Structured weekly release changelog
└── specs/                     # Staging directory for generated feature specs & PRDs
```

---

## ⚡ How to Use It With Your AI

### Example 1: Generate a Developer-Ready PRD
> *"Draft a technical feature PRD in `product-engine/specs/` for adding user role permissions (Admin, Editor, Viewer). Follow `feature_prd_golden.md` and include explicit acceptance criteria and out-of-scope constraints."*

### Example 2: Write Launch Day Assets (Product Hunt / X)
> *"We are launching our automated webhook pipeline next Tuesday. Use `product_launch_checklist.md` to draft our 60-character tagline, short pitch, and the maker's first comment."*

### Example 3: Compile a Weekly Product Changelog
> *"Generate a weekly changelog from our recent git commits using `weekly_changelog.md`. Group changes into New Features, Improvements, and Bug Fixes."*

---

## 🎯 PRD Principles Enforced
- **Problem First**: Never specify a feature without defining the exact user bottleneck.
- **Explicit Acceptance Criteria**: Every user story must have testable checkboxes.
- **Strict Scope Boundaries**: Explicitly state what is NOT included to protect engineering velocity.
