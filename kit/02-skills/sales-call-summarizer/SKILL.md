---
name: sales-call-summarizer
description: Use when the user pastes a sales call transcript or notes and wants a CRM-ready summary with next steps. Triggers on "summarize this call", "call notes", "what are the next steps".
---

# Sales Call Summarizer

## When to use
After a discovery or sales call, to turn a transcript/notes into a structured record.

## Inputs you need
- The transcript or raw notes
- (Optional) the deal stage and CRM fields the user tracks

## Steps
1. Extract the prospect's stated problem in their own words.
2. Capture decision criteria, timeline, budget signals, and stakeholders.
3. Note objections raised and how they were (or weren't) handled.
4. Identify the agreed next step and its owner/date.
5. Flag risks and the single most important follow-up action.

## Output format
```
Summary (3 bullets)
Problem (their words): ...
Decision criteria: ...
Timeline / budget signals: ...
Stakeholders: ...
Objections: - objection → status
Next step: [owner] — [action] — [date]
Deal risk (1-5) + why: ...
#1 follow-up action: ...
```

## Quality bar
- Use the prospect's language for the problem; don't sanitize it.
- Every next step has an owner and a date. No vague "follow up soon".
- If budget/timeline weren't discussed, say so explicitly (it's a gap to close).

## Example
**Input:** 25-min discovery transcript.
**Output:** Tight CRM-ready block ending with "Risk 3/5 — no budget owner identified; #1 action: get intro to CFO by Fri."
