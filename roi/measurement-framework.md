# Measurement Framework

You can't prove ROI you didn't instrument. Set this up **before** sending a single email.

## 1. The one metric that matters
**Qualified meetings booked** (a meeting with an ICP-fit decision-maker who agreed to talk).
Everything else is a leading or lagging indicator of this. Revenue is the lagging proof;
meetings is the controllable deliverable you sell.

Define "qualified" in writing with the client up front (e.g. "title in {list}, company
{size}, showed up, stayed 15+ min"). This prevents disputes and makes the case study honest.

## 2. The funnel to track
| Stage | Metric | Why it matters |
|-------|--------|----------------|
| Sent | emails/messages sent | capacity + deliverability denominator |
| Delivered | bounce rate | data quality / domain health |
| Replied | reply rate | message-market fit |
| Positive | positive reply rate | targeting + offer fit |
| Booked | **meetings booked** | the deliverable |
| Held | show rate | qualification quality |
| Won | close rate, deals | revenue attribution |
| Revenue | new revenue, avg deal | the ROI numerator |

## 3. Capture the baseline (day 0)
Before you start, record the client's current state so "after" means something:
- Current monthly inbound + outbound meetings
- Current close rate and average deal value
- Current cost per acquired customer (if known)
- What they spend now on lead gen (ads, SDR salary, agencies)

Baseline + after = the delta you get paid for. No baseline = no provable ROI.

## 4. Attribution rules (agree these in writing)
- A deal counts as "sourced by us" if the first meeting came from our outreach.
- Use a dedicated tracking inbox / unique calendar link / UTM so the source is unambiguous.
- Revenue is counted when **closed-won**, with deal value confirmed by the client.
- Report gross profit ROI (revenue × margin), not vanity revenue — it survives scrutiny.

## 5. The tracking sheet (schema)
One row per week per client. These columns feed `roi_calculator.py` directly.

```
week, sent, delivered, replies, positive_replies, meetings_booked,
meetings_held, deals_won, revenue, notes
```

Plus a static client-config block:
```
client_name, avg_deal_value, gross_margin, setup_fee, monthly_fee,
qualified_definition, baseline_monthly_meetings, baseline_close_rate
```

## 6. Reporting cadence
- **Weekly:** a 5-line update (sent / replies / meetings booked / meetings held / pipeline).
- **Monthly:** full ROI report from the calculator — projected vs actual.
- **End of engagement:** the numbers become a [case study](case-study-template.md).

## 7. Honesty guardrails (these protect you)
- Never count a no-show as a delivered meeting.
- Show the funnel, not just the headline — clients trust transparency and it earns renewals.
- If a month underperforms, report it and the fix. A real track record includes variance;
  fabricated perfection gets found out and kills referrals.
