# Full Sales System

**Promise:** Generate pipeline and close more deals, repeatably — a complete sales motion
from cold list to signed proposal, with Claude doing the heavy lifting at every stage.

## Who it's for
Founders selling their own services and small sales teams without sales ops support.

## Components used
- **Prompts:** the entire [Sales](../01-prompts/sales.md), [Lead Gen](../01-prompts/lead-gen.md), and [Outreach](../01-prompts/outreach.md) sets.
- **Skills:** [cold-email-writer](../02-skills/cold-email-writer/SKILL.md), [sales-call-summarizer](../02-skills/sales-call-summarizer/SKILL.md), [proposal-builder](../02-skills/proposal-builder/SKILL.md)
- **Agents:** [Lead Gen Agent](../03-agents/lead-gen-agent.md), [Outreach Agent](../03-agents/outreach-agent.md), [Sales Assistant Agent](../03-agents/sales-assistant-agent.md)
- **Workflows:** [Cold List → Replies](../04-workflows/cold-list-to-replies.md), [Inbound → Booked Call](../04-workflows/inbound-to-booked-call.md), [Discovery → Signed Proposal](../04-workflows/discovery-to-signed-proposal.md)

## Setup (one-time)
1. **Define ICP + offer + proof** (ICP Builder + Positioning Statement prompts).
2. **Stand up the 3 workflows** above as your repeatable plays.
3. **Wire the agents** into a Claude Project with the relevant skills attached.
4. **Pick your numbers** — the metrics each workflow tracks become your dashboard.

## Operating cadence
- **Daily:** triage inbound (Inbound→Booked), prep today's calls.
- **Weekly:** launch/refresh one outbound campaign (Cold List→Replies), run deal-risk review on the pipeline.
- **Per deal:** summarize → proposal → follow-up (Discovery→Signed Proposal).

## What you get
A predictable pipeline: outbound that books meetings, inbound that doesn't leak, and deals
that move with documented next steps instead of stalling silently.

## Packaging / price guide
- **System install + training:** $5,000–9,000.
- **Fractional sales-ops retainer:** run the cadence with the client — $2,000–5,000/mo.
- **Self-serve license:** $997–1,997.
