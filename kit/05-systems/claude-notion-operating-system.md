# Claude + Notion Operating System

**Promise:** Run the whole business with clarity, structure, and leverage — Notion as the
source of truth, Claude as the engine that fills it, summarizes it, and drives action.

## Who it's for
Solo operators and small teams drowning in scattered docs, notes, and to-dos.

## Components used
- **Prompts:** [SOP From a Transcript](../01-prompts/ops.md), [Meeting Notes → Action Items](../01-prompts/ops.md), [Weekly Priorities Planner](../01-prompts/ops.md)
- **Skills:** [weekly-report-writer](../02-skills/weekly-report-writer/SKILL.md), [sales-call-summarizer](../02-skills/sales-call-summarizer/SKILL.md)
- **Agents:** [Research Agent](../03-agents/research-agent.md), [Sales Assistant Agent](../03-agents/sales-assistant-agent.md)
- **Workflows:** any — this system is the connective tissue that captures their outputs.

## The Notion structure (set up once)
```
🏢 Business OS
├─ 📥 Inbox            (raw notes, transcripts, ideas land here)
├─ ✅ Actions          (owner · due · status — fed by Meeting Notes → Action Items)
├─ 📚 SOPs             (built from transcripts via the SOP prompt)
├─ 👥 Accounts/CRM     (briefs from the Research Agent; call summaries from the skill)
├─ 📈 Weekly Review    (auto-drafted by weekly-report-writer)
└─ 🎯 Goals            (quarterly — what the Weekly Planner ladders up to)
```

## Operating cadence
- **Capture:** drop any transcript/note into Inbox → Claude turns it into actions/SOPs/summaries.
- **Daily:** Claude proposes the day's top 3 from Actions + Goals.
- **Weekly:** Weekly Priorities Planner sets focus; weekly-report-writer drafts the review.
- **Monthly:** Research Agent refreshes key account briefs.

## What you get
One place where everything lives, kept current by Claude — so nothing is lost, every
meeting produces action, and the weekly review writes itself.

## Packaging / price guide
- **Build + onboard the client's Business OS:** $3,000–6,000.
- **Managed operations retainer:** $1,500–4,000/mo.
- **Notion template + kit license:** $297–697.
