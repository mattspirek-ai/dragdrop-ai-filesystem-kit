# How a Business Actually Uses This (and How You Make Money)

Plain-English operating model. No abstractions. Four questions, four answers, one worked
example: **Northside Marketing, a 12-person agency** (the default in `workflow_mapper.py`).

---

## The whole model in one line
You sell an **AI Workflow Audit**, use it to **map** where they waste time, **deploy** the
matching kit assets to fix the top 2, and **charge** to build it and keep it running.

```
Paid Audit  ->  Implementation project  ->  Monthly retainer
($500-1.5k)     ($3k-12k one-time)          ($1.5k-5k/mo recurring)
```

---

## Q1. How does the business actually USE it?
They never see "a kit of prompts." After you implement, they get one of two things:

- **Done-with-you (DIY):** a **Claude Project / workspace** where their team does specific
  jobs — e.g. a marketer opens it and clicks "draft this week's client posts" and gets
  on-brand drafts; a rep pastes a call transcript and gets a CRM-ready summary. You
  installed the agents/skills; they push the button.
- **Done-for-you (DFY):** they see nothing but **outputs** — you run the outreach system and
  they just get booked meetings, or you run the content system and posts go out. They pay
  for the result, not the tool.

Most clients start DIY for the cheap stuff and pay DFY for the high-value stuff.

---

## Q2. How do we PITCH that we can implement this?
Don't pitch "AI." Pitch a **paid audit** — it's an easy yes and it's billable:

> "Give me 60 minutes with whoever does your sales and marketing. I'll map every
> repetitive task, show you exactly which ones are costing you the most, and hand you a
> plan to automate the top two with AI — with the dollar savings attached. The audit is
> $750, credited toward implementation if you move forward."

Why this works: it's low-risk, it's revenue on day one, it qualifies them (a business that
won't pay $750 to find savings won't pay $5k to capture them), and it *forces* the workflow
map that sells the real project.

---

## Q3. How does it MAP their workflow and CHOOSE the right setup?
This is `workflow_mapper.py` — you run it live in the audit:

1. **List their repetitive tasks** by function (sales, marketing, outreach, content, SEO, ops).
2. **Score each:** how often, minutes each, and AI-fit (1 = judgement-heavy, 5 = repetitive text).
3. The tool computes **monthly cost** of each task and ranks by *cost × AI-fit*.
4. It **maps each task to the exact kit asset** that automates it and sorts into phases.
5. Output = a **roadmap + the savings math** = your proposal.

For Northside it surfaced: Phase 1 = client content drafting ($1,800/mo) + cold outreach
($1,200/mo), reclaiming **~$2,100/mo (~$25k/yr)**, paying back a $4.5k build in ~2 months.
The in-person strategy meetings? Tool says *keep them human* — which builds trust that
you're not just selling AI for its own sake.

The "right setup" falls out automatically:
- **One painful recurring task** -> deploy a **prompt or skill** (DIY).
- **A whole function** (all their outreach) -> deploy an **agent + workflow** (DIY or DFY).
- **A core growth engine** they'll run forever -> sell a **System** (DFY retainer).

---

## Q4. How do we GENERATE INCOME?
Three stacked revenue lines from the same engagement:

| Stage | What you sell | Price | Cash type |
|-------|---------------|-------|-----------|
| 1. Audit | The workflow map + savings plan | $500–1,500 | immediate, low-friction |
| 2. Implementation | Build + train the Phase-1 setup | $3,000–12,000 | one-time project |
| 3. Retainer | Run/maintain/expand it (DFY) | $1,500–5,000/mo | **recurring — the real business** |
| 4. (optional) | License the kit as a self-serve product | $97–997 | passive volume |

The money is in **stage 3**. Stages 1–2 are how you earn the right to it. One agency client
on a $3k/mo retainer is $36k/yr; ten of them is a real business — and the kit means your
delivery cost barely moves as you add clients. That low marginal cost is the whole edge.

---

## The end-to-end, start to finish
1. **Book the audit** (Q2 pitch). Get $750 in the door.
2. **Run `workflow_mapper.py`** live (Q3). Walk out with a ranked roadmap + savings number.
3. **Propose Phase 1** using `sales/sow-template.md`. Price it against the savings you just showed.
4. **Implement** the 2 top assets — install in their Claude Project or run it yourself.
5. **Prove it** with `roi/roi_calculator.py` (meetings/savings tracked weekly).
6. **Convert to a retainer** to run + expand into Phase 2/3.
7. **Turn the result into a `roi/case-study-template.md`** and use it to land the next client.

That's it. The kit is the inventory; this file is the business.
