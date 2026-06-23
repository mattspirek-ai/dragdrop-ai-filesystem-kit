# Worked Example — Harbor Point Consulting

A full audit-to-close walkthrough using the real tools. Reproduce it:
```
python ../workflow_mapper.py --config harbor-point-consulting.json   # the map
python ../../roi/roi_calculator.py --name "Harbor Point Consulting" \
       --deal 12000 --meetings 8 --close 0.25 --show 0.75 --setup 2000 --fee 2500 --months 3
```

**The prospect:** Harbor Point, a 6-person management consultancy. Partners bill ~$95/hr
of loaded time. They want more clients but are buried in admin.

---

### Step 1 — Book the audit
DM/email gets a "yes" to a paid 60-min **AI Workflow Audit** ($750, credited toward the build).

### Step 2 — Map the workflow (live, on screen)
Fill the [audit worksheet](../audit-worksheet.md) with them, run `workflow_mapper.py`:

- **Phase 1 (now):** cold outreach ($1,520/mo) + proposal drafting ($1,710/mo).
- **Phase 2:** weekly reports, LinkedIn content. **Phase 3:** call summaries.
- **Keep human:** their $7,600/mo of actual client delivery — flagged, *not* automated.
- **Headline:** Phase 1 reclaims **~$2,261/mo (~$27k/yr)**; a $4.5k build pays back in ~2 months.

This is the moment it stops being "interesting AI" and becomes obvious math.

### Step 3 — Show the revenue upside
The time savings justify the build; the **outbound system** is the growth story. The ROI
calculator projects **24 meetings, ~$54k new revenue, 298% ROI** on a $9,500 / 3-month
engagement — breakeven after 5 meetings.

### Step 4 — Propose (priced against what they just saw)
Using [`sales/sow-template.md`](../../sales/sow-template.md):
- **Build Phase 1** (outreach + proposal engine), installed in their Claude Project: **$4,500 one-time.**
- **Run it for them** (DFY outbound + monthly expansion): **$2,500/mo.**
- De-risk with the [pilot guarantee](../../roi/pilot-offer.md): "5 qualified meetings in 30 days or month two is free."

### Step 5 — Prove + expand
Track weekly with `roi_calculator.py`; at day 30 present actuals, convert to the retainer,
roll into Phase 2. Turn the result into a [case study](../../roi/case-study-template.md)
and use it to land the next consultancy.

---

**Income from this one client:** $750 audit + $4,500 build + $2,500/mo retainer
= **$5,250 up front, then $30k/yr recurring** — with the kit doing the delivery.
