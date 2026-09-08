# Email Engine Standard Operating Procedure (SOP)

This SOP establishes the rules for writing outbound emails, nurture sequences, and inbound reply triage.

---

## 📧 1. Cold Outreach Framework
- **Length**: Strict maximum of 75–125 words. Busy executives scan emails on mobile in under 10 seconds.
- **Structure**:
  1. *Observation/Trigger*: Specific reason you are reaching out (e.g. company hiring, new feature launch, GitHub repo).
  2. *Problem/Insight*: A concise observation about a common challenge in their stack or workflow.
  3. *Proof/Offer*: One concrete metric, case study, or open-source tool.
  4. *Soft CTA*: Interest-based call to action (e.g., "Open to seeing a 2-minute video on how we did this?", NOT "Let's book a 30-min call").

---

## 🔄 2. Multi-Touch Sequence Timing
- **Day 1**: Initial Outreach (Problem & Insight).
- **Day 3**: The Value Add (Share a case study, script, or diagram).
- **Day 7**: The "Short & Direct" follow-up (Bump + 1-sentence value restatement).
- **Day 14**: The Break-Up email (Polite exit + leave door open).

---

## 🛡️ 3. Deliverability Checklist
- [ ] Subject line is under 5 words.
- [ ] No tracking links or heavy attachments in Step 1.
- [ ] Max 1 clean URL link per email.
- [ ] Verified sender DNS (SPF, DKIM, DMARC configured).

---

## 📂 4. Draft Staging
- One-off cold emails and reply drafts are saved to `email-engine/drafts/` using the naming standard:
  `YYYY-MM-DD_[recipient_or_topic].md`
- Pre-built multi-touch sequences (Cold Outreach 5-Step, Welcome/Onboarding) stay in `email-engine/sequences/`.
