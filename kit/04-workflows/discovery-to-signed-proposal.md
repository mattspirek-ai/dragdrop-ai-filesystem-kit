# Workflow: Discovery Call → Signed Proposal

**Outcome:** A first discovery call turns into a signed deal.
**Trigger:** A discovery call happens.
**Owner:** Sales / founder · **Runs:** per deal
**Time:** ~20 min of admin vs hours, and faster cycle time.

## Assets used
- Prompt: [Proposal From Notes](../01-prompts/sales.md), [Follow-Up Sequence](../01-prompts/sales.md), [Pricing Conversation Coach](../01-prompts/sales.md)
- Skill: [sales-call-summarizer](../02-skills/sales-call-summarizer/SKILL.md), [proposal-builder](../02-skills/proposal-builder/SKILL.md)
- Agent: [Sales Assistant Agent](../03-agents/sales-assistant-agent.md)

## Steps
| # | Step | Asset | Output |
|---|------|-------|--------|
| 1 | Summarize the discovery call | sales-call-summarizer skill | Problem, criteria, next step, risk |
| 2 | Build the proposal | proposal-builder skill | 3-tier proposal in the client's words |
| 3 | Handle price pushback | Pricing Conversation Coach | Language to hold price |
| 4 | Run follow-ups if it stalls | Follow-Up Sequence prompt | 4-touch re-engagement |
| 5 | Track risk to close | Sales Assistant Agent | #1 next action each week |

## Definition of done
Proposal sent, objections handled, deal signed or cleanly closed-lost with a reason.

## Metrics to track
Discovery→proposal time · Proposal→close rate · Average discount given (lower is better).
