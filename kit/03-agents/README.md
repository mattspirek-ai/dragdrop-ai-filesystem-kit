# Execution Layer — Agents

An **agent** is a system prompt that turns Claude into a specific role with a clear
mandate, operating principles, and guardrails. Where a prompt produces one output and a
skill packages one capability, an agent *holds a role* across a whole task.

## How to use these
- **Claude Projects (claude.ai):** paste the agent file into "Custom instructions".
- **API / Agent SDK:** use the file body as the `system` prompt.
- **Claude Code subagents:** save as a subagent definition and invoke by name.
- Give the agent access to the relevant **Skills** (Layer 2) and it executes far better.

## Included (v1)
| Agent | Role | File |
|-------|------|------|
| Lead Gen Agent | Finds + qualifies + drafts outreach to fit leads | [lead-gen-agent.md](lead-gen-agent.md) |
| SEO Agent | Plans clusters, briefs, and on-page optimization | [seo-agent.md](seo-agent.md) |
| Outreach Agent | Runs personalized multi-touch sequences | [outreach-agent.md](outreach-agent.md) |
| Content Agent | Takes a topic to a finished, on-brand asset | [content-agent.md](content-agent.md) |
| Sales Assistant Agent | Preps calls, summarizes, drafts follow-ups | [sales-assistant-agent.md](sales-assistant-agent.md) |
| Research Agent | Builds account/market briefs from scattered info | [research-agent.md](research-agent.md) |

Target catalog: 100+ (one per role × specialization) — see [../ROADMAP.md](../ROADMAP.md).
New agents use [_TEMPLATE.md](_TEMPLATE.md).
