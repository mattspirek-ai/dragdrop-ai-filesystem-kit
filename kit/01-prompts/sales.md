# Sales Prompts

Single-shot prompts for moving deals forward. Paste into Claude, fill the `[SLOTS]`.

---

### Discovery Call Prep
**Use when:** You have a call booked and 10 minutes to prep.
```
You are a senior B2B sales rep preparing for a discovery call.

Research and reason about this prospect, then build my prep doc.

INPUTS:
- Company: [name + one-line description]
- Their likely pain (from intake/notes): [paste]
- My offer: [one line]

OUTPUT FORMAT:
1. 3 hypotheses about their #1 problem
2. 8 discovery questions ordered from broad → specific
3. 3 likely objections + a one-line reframe for each
4. A crisp value statement I can deliver in 20 seconds
```

---

### Objection Handling Script
**Use when:** A specific objection keeps killing deals.
```
You are a sales coach. Write me a calm, non-defensive response to this objection.

INPUTS:
- Objection: [paste exact words the prospect uses]
- My product: [one line]
- The real underlying fear (your guess): [optional]

CONSTRAINTS: Acknowledge first, never argue, end with a question that re-opens the conversation. Under 90 words.
```

---

### Proposal From Notes
**Use when:** Turning messy call notes into a clean proposal.
```
You are a deal desk specialist. Turn my raw notes into a structured proposal.

INPUTS:
- Call notes: [paste]
- Pricing options: [paste]

OUTPUT FORMAT: Problem → Desired Outcome → Proposed Solution → Scope → Investment (3 tiers) → Next step. Keep it skimmable.
```

---

### Follow-Up Sequence (deal gone quiet)
**Use when:** A warm deal stalled.
```
Write a 4-touch follow-up sequence to re-engage a stalled deal without being needy.

INPUTS:
- Where we left off: [paste]
- What's new on my side (proof/feature/case study): [paste]

CONSTRAINTS: Each touch under 80 words, each adds value (not "just checking in"). Touch 4 is a polite breakup email.
```

---

### Deal Risk Review
**Use when:** Forecasting / pipeline review.
```
You are a sales manager reviewing a deal. Stress-test it.

INPUTS:
- Deal summary, stage, and notes: [paste]

OUTPUT FORMAT: Risk score (1-5) + why · Missing info · Single biggest risk · The one action most likely to advance it this week.
```

---

### Pricing Conversation Coach
**Use when:** You need to defend price.
```
Coach me through a price negotiation. Give me language, not platitudes.

INPUTS:
- My price + what's included: [paste]
- Their pushback: [paste]

OUTPUT: 3 ways to hold price by changing scope/terms instead of discounting, each with exact wording.
```

---

### Win/Loss Analysis
**Use when:** A deal closes (either way).
```
Analyze why this deal was won or lost and what to repeat or fix.

INPUTS:
- Full deal timeline + outcome: [paste]

OUTPUT: 3 things that drove the outcome · 1 process change for next time · 1 sentence I can share with the team.
```

---

### Account Expansion Plan
**Use when:** Growing an existing customer.
```
You are an account manager. Build an expansion plan for a current customer.

INPUTS:
- What they bought + current usage/results: [paste]
- Other products/services I offer: [paste]

OUTPUT: 3 expansion plays ranked by likelihood, the trigger/signal for each, and an opening message for the most likely one.
```
