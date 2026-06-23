# spiAI Business Development Kit

**Prompts + Skills + Agents + Workflows + Systems — the complete Claude-powered operating kit for growing a business.**

This is a productized offering you can sell, white-label, or use to run your own
operations. It packages battle-tested Claude assets into five stacked layers, so a
buyer goes from "I have Claude" to "Claude runs my sales, marketing, and ops."

```
Prompts  →  Skills  →  Agents  →  Workflows  →  Systems
build ideas  build capability  execute tasks  create automation  drive growth
```

## The Five Layers

| # | Layer | What it is | Folder | v1 included | Target catalog |
|---|-------|-----------|--------|-------------|----------------|
| 1 | **Foundation** — Prompts | Single-shot prompts for a specific output | [`kit/01-prompts`](kit/01-prompts) | 50+ | 500+ |
| 2 | **Capability** — Skills | Reusable Claude Skills (SKILL.md) for repeatable tasks | [`kit/02-skills`](kit/02-skills) | 6 | 150+ |
| 3 | **Execution** — Agents | System prompts that turn Claude into a role | [`kit/03-agents`](kit/03-agents) | 6 | 100+ |
| 4 | **Automation** — Workflows | Multi-step playbooks chaining prompts/skills/agents | [`kit/04-workflows`](kit/04-workflows) | 4 | 25+ |
| 5 | **Growth Engine** — Systems | Packaged, sellable end-to-end systems | [`kit/05-systems`](kit/05-systems) | 3 | — |

> v1 ships a **representative, immediately-usable seed** of each layer plus the
> taxonomy, templates, and an [expansion roadmap](kit/ROADMAP.md) to reach the
> full catalog numbers. Every asset is real and runnable today — nothing is a stub.

### ⭐ The Proof Layer — what actually makes this sellable
A kit of prompts/agents is the *engine*, not the *product*. Businesses buy **measurable
outcomes**, so [`roi/`](roi/) turns the kit into a provable, ROI-backed service:
qualified meetings booked, tracked funnel data, a runnable [ROI calculator](roi/roi_calculator.py),
a risk-reversed [pilot offer](roi/pilot-offer.md) to land your first clients, and a
[case-study template](roi/case-study-template.md) to build the track record you pitch with.
**Start here if your question is "what would a business actually pay for?"**

## Business Functions Covered

Sales · Marketing · Lead Gen · SEO · Content · Outreach · Ops

## Outcomes It Sells

Save time · Improve output · Increase consistency · Accelerate growth · Scale execution

## Repo Map

```
kit/
  01-prompts/     Foundation Layer — prompt library by business function
  02-skills/      Capability Layer — Claude Skills (drop into Claude Code / Projects)
  03-agents/      Execution Layer — agent system prompts
  04-workflows/   Automation Layer — step-by-step playbooks
  05-systems/     Growth Engine Layer — packaged offerings
  ROADMAP.md      How to grow the seed into the full 500+/150+/100+/25+ catalog
sales/            Pricing, packaging, sales page copy, SOW
delivery/         Client onboarding + Notion/Claude operating setup
_archive/         Previous (deprecated) drag-drop file-organizer prototype
```

## How To Sell It

1. Pick a packaging tier in [`sales/pricing.md`](sales/pricing.md).
2. Use [`sales/sales-page.md`](sales/sales-page.md) for the landing page / DM pitch.
3. Deliver with [`delivery/onboarding.md`](delivery/onboarding.md).
4. Upsell into a **System** ([`kit/05-systems`](kit/05-systems)) — the highest-margin tier.

## How To Use It (as the operator)

Each asset says how to run it. In general:
- **Prompts** — paste into Claude (claude.ai, the API, or Claude Code).
- **Skills** — drop the folder into a Claude Code/Project `skills/` directory.
- **Agents** — paste the system prompt into a Project or API system field.
- **Workflows** — follow the numbered steps; each step points to the asset it uses.
- **Systems** — full setup guides that wire the above together.

---

*Built for the spiAI business. White-label freely — replace "spiAI" with your brand.*
