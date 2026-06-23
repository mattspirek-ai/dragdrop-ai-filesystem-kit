# Implementation — The Business Engine

How a client actually uses the kit, how you pitch and implement it, how you map their
workflow to the right setup, and how it makes money. **Start here.**

| File | What it answers |
|------|-----------------|
| [how-it-works.md](how-it-works.md) | The full operating model: usage, pitch, mapping, income — with a worked example |
| [audit-worksheet.md](audit-worksheet.md) | The script for the paid 60-min discovery audit |
| [workflow_mapper.py](workflow_mapper.py) | Runnable: scores their tasks → recommends exact kit assets + savings math |

## The 60-second version
1. Sell a **paid AI Workflow Audit** ($500–1,500).
2. In it, run `workflow_mapper.py` to **map their tasks → the right kit setup** + dollar savings.
3. Propose **Phase 1 implementation** ($3k–12k), priced against the savings you just showed.
4. Convert to a **monthly retainer** ($1.5k–5k) to run + expand it — that's the real income.
5. Track results with [`../roi/roi_calculator.py`](../roi/roi_calculator.py); turn them into a [case study](../roi/case-study-template.md) to land the next client.

```
Audit  ->  Map workflow  ->  Implement Phase 1  ->  Prove ROI  ->  Retainer  ->  Case study  ->  repeat
```

Try it now:
```
python workflow_mapper.py
```
