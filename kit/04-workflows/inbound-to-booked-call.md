# Workflow: Inbound Lead → Booked Call

**Outcome:** A new inbound lead becomes a scheduled, qualified call.
**Trigger:** A form fill, DM, or reply lands.
**Owner:** Sales / founder · **Runs:** per inbound
**Time:** ~3 min with the kit vs ~20 min ad hoc.

## Assets used
- Prompt: [Inbound Reply Triage](../01-prompts/lead-gen.md), [Discovery Call Prep](../01-prompts/sales.md)
- Skill: [cold-email-writer](../02-skills/cold-email-writer/SKILL.md)
- Agent: [Lead Gen Agent](../03-agents/lead-gen-agent.md), [Sales Assistant Agent](../03-agents/sales-assistant-agent.md)

## Steps
| # | Step | Asset | Output |
|---|------|-------|--------|
| 1 | Triage the inbound for fit | Inbound Reply Triage prompt | Hot/warm/cold + the next question |
| 2 | If a fit, draft a fast, personal reply that drives to booking | cold-email-writer skill | Reply with a scheduling link/ask |
| 3 | On reply, confirm the call and log context | Lead Gen Agent | CRM note + booked slot |
| 4 | Before the call, generate prep | Discovery Call Prep prompt | Hypotheses, questions, objections |

## Definition of done
A qualified call is on the calendar and the rep has a prep doc.

## Metrics to track
Inbound→reply time · Inbound→booked rate · Show rate.
