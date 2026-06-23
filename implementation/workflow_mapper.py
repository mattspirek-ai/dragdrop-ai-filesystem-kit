#!/usr/bin/env python3
"""
spiAI Workflow Mapper
=====================

The tool you run during a discovery session. It takes a business's repetitive tasks,
scores them by what they cost, and tells you EXACTLY which kit assets to deploy and in
what order. Output = the client's implementation roadmap (and your proposal).

This is the "map their workflow -> choose the right setup" step, made concrete.

Pure standard library.

Usage:
  python workflow_mapper.py                 # runs the worked example (a real small biz)
  python workflow_mapper.py --config tasks.json --rate 60

tasks.json = {"hourly_rate": 60, "tasks": [
  {"name": "...", "function": "sales", "times_per_month": 20,
   "minutes_each": 30, "ai_fit": 4}, ...]}
ai_fit: 1 (judgement-heavy, poor fit) .. 5 (repetitive text work, perfect fit)
"""

import argparse
import json
import sys

# function -> the kit assets that automate it (this is the "right setup" lookup)
ASSET_MAP = {
    "sales":     ("kit/01-prompts/sales.md + Sales Assistant Agent",
                  "kit/05-systems/full-sales-system.md"),
    "lead_gen":  ("Lead Gen Agent + cold-email-writer skill",
                  "kit/04-workflows/cold-list-to-replies.md"),
    "outreach":  ("Outreach Agent + cold-email-writer skill",
                  "kit/04-workflows/cold-list-to-replies.md"),
    "marketing": ("kit/01-prompts/marketing.md + Content Agent",
                  "kit/05-systems/linkedin-content-system.md"),
    "content":   ("Content Agent + content-repurposer skill",
                  "kit/05-systems/linkedin-content-system.md"),
    "seo":       ("SEO Agent + seo-brief-generator skill",
                  "kit/04-workflows/topic-to-published-content.md"),
    "ops":       ("kit/01-prompts/ops.md + weekly-report-writer skill",
                  "kit/05-systems/claude-notion-operating-system.md"),
}

# A real-ish small B2B service business (e.g. a 12-person agency)
EXAMPLE = {
    "business": "Northside Marketing (12-person agency)",
    "hourly_rate": 60.0,
    "tasks": [
        {"name": "Writing cold outreach emails", "function": "outreach",
         "times_per_month": 200, "minutes_each": 6, "ai_fit": 5},
        {"name": "Drafting client social/blog content", "function": "content",
         "times_per_month": 40, "minutes_each": 45, "ai_fit": 4},
        {"name": "Summarizing sales/discovery calls", "function": "sales",
         "times_per_month": 30, "minutes_each": 20, "ai_fit": 5},
        {"name": "Writing weekly client reports", "function": "ops",
         "times_per_month": 12, "minutes_each": 60, "ai_fit": 4},
        {"name": "SEO briefs for writers", "function": "seo",
         "times_per_month": 15, "minutes_each": 40, "ai_fit": 4},
        {"name": "In-person client strategy meetings", "function": "sales",
         "times_per_month": 8, "minutes_each": 90, "ai_fit": 1},
    ],
}


def score(tasks, rate):
    rows = []
    for t in tasks:
        hours = t["times_per_month"] * t["minutes_each"] / 60.0
        cost = hours * rate
        # priority weights cost by how well AI handles it (ai_fit 1..5 -> 0.2..1.0)
        priority = cost * (t["ai_fit"] / 5.0)
        rows.append({**t, "hours": hours, "cost": cost, "priority": priority})
    rows.sort(key=lambda r: r["priority"], reverse=True)
    return rows


def recommend(rows):
    out, phase1_savings = [], 0.0
    for i, r in enumerate(rows):
        assets, system = ASSET_MAP.get(r["function"], ("(custom)", ""))
        if r["ai_fit"] <= 2:
            phase, note = "Skip / human", "judgement-heavy — keep human"
        elif i < 2:
            phase, note = "PHASE 1 (now)", "highest cost x best fit — start here"
            phase1_savings += r["cost"] * 0.7   # assume ~70% of the hours reclaimed
        elif i < 4:
            phase, note = "Phase 2", "add once Phase 1 is proven"
        else:
            phase, note = "Phase 3", "nice-to-have"
        out.append({**r, "assets": assets, "system": system, "phase": phase, "note": note})
    return out, phase1_savings


def fmt_money(x):
    return "${:,.0f}".format(x)


def render(cfg, rows, phase1_savings):
    L = "=" * 70
    o = [L, "  WORKFLOW MAP -> RECOMMENDED SETUP", "  Business: {}".format(cfg["business"]),
         "  Loaded labor rate: {}/hr".format(fmt_money(cfg["hourly_rate"])), L, ""]
    o.append("  {:<34} {:>8} {:>9}  {}".format("TASK", "HRS/MO", "COST/MO", "PHASE"))
    o.append("  " + "-" * 66)
    for r in rows:
        o.append("  {:<34} {:>8.1f} {:>9}  {}".format(
            r["name"][:34], r["hours"], fmt_money(r["cost"]), r["phase"]))
    o.append("")
    o.append("  RECOMMENDED SETUP (in order):")
    for r in rows:
        if r["ai_fit"] <= 2:
            continue
        o.append("   - {}".format(r["name"]))
        o.append("       deploy: {}".format(r["assets"]))
        if r["phase"].startswith("PHASE 1") and r["system"]:
            o.append("       scale into: {}".format(r["system"]))
    o.append("")
    annual = phase1_savings * 12
    o.append("  THE PITCH MATH")
    o.append("    Phase 1 reclaims ~{}/mo  (~{}/yr) in labor.".format(
        fmt_money(phase1_savings), fmt_money(annual)))
    o.append("    Typical Phase 1 implementation fee: $3,000-6,000 (one-time).")
    o.append("    => Pays for itself in ~{:.1f} months, then it's pure savings.".format(
        (4500.0 / phase1_savings) if phase1_savings else 0))
    o.append(L)
    return "\n".join(o)


def main(argv):
    p = argparse.ArgumentParser(description="spiAI Workflow Mapper")
    p.add_argument("--config", help="JSON with hourly_rate + tasks")
    p.add_argument("--rate", type=float, help="Override loaded hourly rate")
    a = p.parse_args(argv)

    cfg = dict(EXAMPLE)
    if a.config:
        with open(a.config) as f:
            data = json.load(f)
        cfg["business"] = data.get("business", "Client")
        cfg["hourly_rate"] = data.get("hourly_rate", cfg["hourly_rate"])
        cfg["tasks"] = data["tasks"]
    if a.rate is not None:
        cfg["hourly_rate"] = a.rate

    rows = score(cfg["tasks"], cfg["hourly_rate"])
    rows, savings = recommend(rows)
    print(render(cfg, rows, savings))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
