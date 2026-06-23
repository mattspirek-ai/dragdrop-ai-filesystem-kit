# Capability Layer — Claude Skills

Skills are packaged, reusable instruction sets Claude loads on demand. Unlike a prompt
(one-shot), a Skill encodes a repeatable *capability* with its own instructions and
examples, so output stays consistent every time.

## How to use these
- **Claude Code / Agent SDK:** drop a skill folder into your project's `skills/`
  (or `.claude/skills/`) directory. Claude invokes it when the task matches.
- **Claude Projects (claude.ai):** paste the `SKILL.md` body into the Project's custom
  instructions, or attach it as a knowledge file.
- **API:** include the `SKILL.md` content in your system prompt.

## Included (v1)
| Skill | What it does |
|-------|--------------|
| [cold-email-writer](cold-email-writer/SKILL.md) | Writes reply-worthy cold emails from a lead + offer |
| [seo-brief-generator](seo-brief-generator/SKILL.md) | Produces a complete SEO content brief for a keyword |
| [sales-call-summarizer](sales-call-summarizer/SKILL.md) | Turns call transcripts into CRM-ready summaries + next steps |
| [content-repurposer](content-repurposer/SKILL.md) | Expands one asset into a week of multi-channel content |
| [proposal-builder](proposal-builder/SKILL.md) | Builds tiered proposals from discovery notes |
| [weekly-report-writer](weekly-report-writer/SKILL.md) | Generates a client/stakeholder progress report from raw updates |

Target catalog: 150+ — see [../ROADMAP.md](../ROADMAP.md). New skills use
[_TEMPLATE/SKILL.md](_TEMPLATE/SKILL.md).
