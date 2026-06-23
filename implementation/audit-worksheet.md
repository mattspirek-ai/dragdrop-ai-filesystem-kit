# AI Workflow Audit — Discovery Worksheet

Run this in the 60-minute paid audit. Fill it with the client, then feed the numbers into
`workflow_mapper.py` to produce their roadmap. This is the script for the meeting.

## 0. Frame it (1 min)
"I'm going to map how your team actually spends its time on repetitive work, then show you
where AI pays for itself fastest. By the end you'll have a prioritized plan either way."

## 1. Business basics
- Business + team size: ____
- Loaded hourly cost of the people doing the work (salary+overhead ÷ hours): $____/hr
- Their #1 goal this quarter: ____

## 2. Task inventory (the core)
For each repetitive task, capture four numbers. Go function by function so nothing's missed.

| Task | Function* | Times/month | Minutes each | AI-fit (1-5)** |
|------|-----------|-------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

\* sales · lead_gen · outreach · marketing · content · seo · ops
\** 1 = needs human judgement/relationships · 5 = repetitive reading/writing/summarizing

Prompts to pull tasks out of them:
- "Walk me through a typical week — what do you do over and over?"
- "What do you put off because it's tedious?"
- "Where do leads or follow-ups fall through the cracks?"
- "What would you do with 10 hours back a week?"

## 3. Current numbers (for ROI later)
- Meetings/leads per month today, and from where: ____
- Average deal/customer value: $____   ·   Close rate: ____%
- Current spend on lead gen / content / contractors: $____/mo

## 4. Generate the map (live)
Enter the table into a `tasks.json` and run:
```
python workflow_mapper.py --config tasks.json --rate <hourly_rate>
```
Show them the screen. The ranked Phase 1 tasks + savings number are the moment the sale
turns from "interesting" to "obvious."

## 5. Recommend the setup
- **Phase 1 (now):** the top 1-2 tasks → name the exact assets the tool listed.
- **Phase 2/3:** the rest, sequenced.
- **Keep human:** the low-AI-fit items — say so explicitly; it builds trust.

## 6. Close
"Phase 1 reclaims ~$[X]/mo. I can build and train it for $[fee], and it pays back in
~[N] months. Want me to send the SOW today?"

→ Use `sales/sow-template.md`, price against the savings, and (if it fits) attach the
`roi/pilot-offer.md` guarantee to remove the last bit of risk.
