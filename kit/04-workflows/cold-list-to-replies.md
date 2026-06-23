# Workflow: Cold List → Replies

**Outcome:** A raw list of target accounts becomes a personalized campaign that books meetings.
**Trigger:** You have a list of ICP-fit accounts/contacts.
**Owner:** Sales / SDR · **Runs:** per campaign
**Time:** ~45 min to launch a campaign vs days manually.

## Assets used
- Prompt: [ICP Builder](../01-prompts/lead-gen.md), [Multi-Touch Outreach Sequence](../01-prompts/outreach.md), [Personalized First-Line Generator](../01-prompts/outreach.md)
- Skill: [cold-email-writer](../02-skills/cold-email-writer/SKILL.md)
- Agent: [Lead Gen Agent](../03-agents/lead-gen-agent.md), [Outreach Agent](../03-agents/outreach-agent.md)

## Steps
| # | Step | Asset | Output |
|---|------|-------|--------|
| 1 | Confirm/refine the ICP | ICP Builder prompt | Tight ICP + disqualifiers |
| 2 | Score the list against the ICP | Lead Gen Agent | Ranked, qualified short list |
| 3 | Design the sequence | Outreach Agent | 5-touch, multi-channel plan |
| 4 | Generate per-contact first lines | Personalized First-Line Generator | Personalization at scale |
| 5 | Write each touch | cold-email-writer skill | Ready-to-load messages |
| 6 | Triage replies back into the booked-call workflow | → [inbound-to-booked-call](inbound-to-booked-call.md) | Booked calls |

## Definition of done
A personalized sequence is loaded and sending to a qualified list.

## Metrics to track
Reply rate · Positive-reply rate · Meetings booked per 100 contacts.
