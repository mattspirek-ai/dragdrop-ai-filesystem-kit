# Catalog Expansion Roadmap

v1 ships a high-quality **seed** of every layer plus the structure to scale it to the
headline numbers (500+ prompts, 150+ skills, 100+ agents, 25+ workflows). This is the
plan to get there without diluting quality.

## Principles
- **Every asset earns its place.** No filler. A buyer should be able to run any item and get value.
- **Taxonomy first.** Each item lives under one of 7 business functions: Sales, Marketing, Lead Gen, SEO, Content, Outreach, Ops.
- **Templates make scaling cheap.** Use the templates below so contributions stay consistent.

## Layer-by-layer target

### 1. Prompts — seed 50 → target 500+
7 functions × ~70 prompts each. Build in batches of 10 per function per release.
Use [`kit/01-prompts/_TEMPLATE.md`](01-prompts/_TEMPLATE.md). Each prompt = role, task,
input slots, constraints, output format.

### 2. Skills — seed 6 → target 150+
Each repeatable, multi-step task that benefits from packaged instructions + examples
becomes a Skill. Use [`kit/02-skills/_TEMPLATE/SKILL.md`](02-skills/_TEMPLATE/SKILL.md).

### 3. Agents — seed 6 → target 100+
One agent per role × specialization (e.g. "SEO Agent — Technical", "SEO Agent — Content").
Use [`kit/03-agents/_TEMPLATE.md`](03-agents/_TEMPLATE.md).

### 4. Workflows — seed 4 → target 25+
One workflow per end-to-end business outcome (lead → booked call, brief → published post).
Use [`kit/04-workflows/_TEMPLATE.md`](04-workflows/_TEMPLATE.md).

### 5. Systems — seed 3
Systems are the premium product. Add deliberately; each is a full offering.

## Suggested release cadence
| Release | Adds |
|---------|------|
| v1 (now) | Seed of all 5 layers + sales/delivery |
| v1.1 | +70 prompts (Sales + Marketing to depth), +10 skills |
| v1.2 | +70 prompts (Lead Gen + Outreach), +15 agents, +3 workflows |
| v2.0 | Full 500/150/100/25 catalog, 2 new Systems |
