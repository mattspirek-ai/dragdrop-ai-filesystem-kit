#!/usr/bin/env python3
"""
spiAI ROI Calculator
====================

Turns the kit's outbound system into a NUMBER you can put in front of a client.

It does two jobs:
  1. PROJECT the ROI of an engagement from the client's own economics (use in the pitch).
  2. REPORT actual ROI from real funnel data once the engagement is running (use in QBRs
     and to build case studies).

Pure standard library. No dependencies.

Usage:
  python roi_calculator.py                 # runs the worked example below
  python roi_calculator.py --config my.json
  python roi_calculator.py --deal 8000 --meetings 12 --close 0.25 --fee 2500

The funnel model (clean, attributable):
  emails_sent -> replies -> positive_replies -> meetings_booked -> meetings_held
              -> deals_won -> revenue -> gross_profit
"""

import argparse
import json
import sys


# ---- Defaults: a typical small-B2B-service client ----------------------------
DEFAULTS = {
    "client_name": "Example Co",
    # Economics of ONE closed deal
    "avg_deal_value": 6000.0,     # revenue from one new client
    "gross_margin": 0.70,         # profit fraction of revenue (honest ROI uses profit)
    # The deliverable + conversion
    "meetings_per_month": 10,     # qualified meetings booked / month (what you sell)
    "show_rate": 0.75,            # booked -> actually held
    "meeting_to_close": 0.20,     # held meeting -> closed deal
    "engagement_months": 3,
    # Your pricing to the client
    "setup_fee": 1500.0,
    "monthly_fee": 2500.0,
    # Funnel efficiency (drives credibility + your capacity/cost)
    "reply_rate": 0.08,           # sent -> any reply
    "positive_rate": 0.30,        # reply -> positive
    "positive_to_meeting": 0.50,  # positive -> booked meeting
}


def model(cfg):
    m = dict(cfg)
    months = m["engagement_months"]

    # --- Deliverable -> revenue ---
    meetings_booked = m["meetings_per_month"] * months
    meetings_held = meetings_booked * m["show_rate"]
    deals = meetings_held * m["meeting_to_close"]
    revenue = deals * m["avg_deal_value"]
    gross_profit = revenue * m["gross_margin"]

    # --- What the client pays you ---
    client_cost = m["setup_fee"] + m["monthly_fee"] * months

    # --- ROI (on profit, the honest version) ---
    net = gross_profit - client_cost
    roi_pct = (net / client_cost * 100.0) if client_cost else 0.0
    roi_multiple = (gross_profit / client_cost) if client_cost else 0.0

    # --- Breakeven: how many HELD meetings just cover your fee ---
    profit_per_held_meeting = m["meeting_to_close"] * m["avg_deal_value"] * m["gross_margin"]
    breakeven_meetings = (client_cost / profit_per_held_meeting) if profit_per_held_meeting else float("inf")

    # --- Cost per booked meeting (your effective price) ---
    cost_per_meeting = client_cost / meetings_booked if meetings_booked else 0.0

    # --- Top of funnel needed to deliver (capacity + credibility) ---
    positives_needed = meetings_booked / m["positive_to_meeting"] if m["positive_to_meeting"] else 0
    replies_needed = positives_needed / m["positive_rate"] if m["positive_rate"] else 0
    emails_needed = replies_needed / m["reply_rate"] if m["reply_rate"] else 0

    return {
        "months": months,
        "meetings_booked": meetings_booked,
        "meetings_held": meetings_held,
        "deals": deals,
        "revenue": revenue,
        "gross_profit": gross_profit,
        "client_cost": client_cost,
        "net": net,
        "roi_pct": roi_pct,
        "roi_multiple": roi_multiple,
        "breakeven_meetings": breakeven_meetings,
        "cost_per_meeting": cost_per_meeting,
        "emails_needed": emails_needed,
        "emails_per_month": emails_needed / months if months else 0,
    }


def fmt_money(x):
    return "${:,.0f}".format(x)


def report(cfg, r):
    line = "=" * 60
    out = []
    out.append(line)
    out.append("  spiAI OUTBOUND ROI — {}".format(cfg["client_name"]))
    out.append(line)
    out.append("  Engagement: {} months".format(r["months"]))
    out.append("  Your price: {} setup + {}/mo  =  {}".format(
        fmt_money(cfg["setup_fee"]), fmt_money(cfg["monthly_fee"]), fmt_money(r["client_cost"])))
    out.append("")
    out.append("  WHAT THEY GET")
    out.append("    Meetings booked .......... {:.0f}".format(r["meetings_booked"]))
    out.append("    Meetings held ............ {:.0f}  (@ {:.0%} show)".format(
        r["meetings_held"], cfg["show_rate"]))
    out.append("    Deals won ................ {:.1f}  (@ {:.0%} close)".format(
        r["deals"], cfg["meeting_to_close"]))
    out.append("    New revenue .............. {}".format(fmt_money(r["revenue"])))
    out.append("    Gross profit ............. {}  (@ {:.0%} margin)".format(
        fmt_money(r["gross_profit"]), cfg["gross_margin"]))
    out.append("")
    out.append("  THE NUMBER THAT SELLS")
    out.append("    Client investment ........ {}".format(fmt_money(r["client_cost"])))
    out.append("    Net profit to client ..... {}".format(fmt_money(r["net"])))
    out.append("    ROI ...................... {:.0f}%   ({:.1f}x return)".format(
        r["roi_pct"], r["roi_multiple"]))
    out.append("    Effective $/meeting ...... {}".format(fmt_money(r["cost_per_meeting"])))
    out.append("    Breakeven ................ {:.1f} held meetings cover your entire fee".format(
        r["breakeven_meetings"]))
    out.append("")
    out.append("  WHAT IT TAKES TO DELIVER (credibility + your capacity)")
    out.append("    Emails / month ........... ~{:,.0f}".format(r["emails_per_month"]))
    out.append("    Emails total ............. ~{:,.0f}".format(r["emails_needed"]))
    out.append(line)
    pitch = (
        '  Pitch line: "For {name}, we project {meetings:.0f} qualified meetings and\n'
        '  about {pipeline} in new revenue over {months} months — a {roi:.0f}% return.\n'
        '  You break even after just {be:.0f} meetings that show up."'
    ).format(
        name=cfg["client_name"],
        meetings=r["meetings_booked"],
        pipeline=fmt_money(r["revenue"]),
        months=r["months"],
        roi=r["roi_pct"],
        be=r["breakeven_meetings"],
    )
    out.append(pitch)
    out.append(line)
    return "\n".join(out)


def parse_args(argv):
    p = argparse.ArgumentParser(description="spiAI Outbound ROI Calculator")
    p.add_argument("--config", help="JSON file overriding any defaults")
    p.add_argument("--name", help="Client name")
    p.add_argument("--deal", type=float, help="Average deal value (revenue)")
    p.add_argument("--margin", type=float, help="Gross margin 0-1")
    p.add_argument("--meetings", type=float, help="Meetings booked per month")
    p.add_argument("--show", type=float, help="Show rate 0-1")
    p.add_argument("--close", type=float, help="Meeting-to-close rate 0-1")
    p.add_argument("--months", type=int, help="Engagement length")
    p.add_argument("--setup", type=float, help="Setup fee")
    p.add_argument("--fee", type=float, help="Monthly fee")
    return p.parse_args(argv)


def build_config(args):
    cfg = dict(DEFAULTS)
    if args.config:
        with open(args.config) as f:
            cfg.update(json.load(f))
    mapping = {
        "name": "client_name", "deal": "avg_deal_value", "margin": "gross_margin",
        "meetings": "meetings_per_month", "show": "show_rate", "close": "meeting_to_close",
        "months": "engagement_months", "setup": "setup_fee", "fee": "monthly_fee",
    }
    for arg_key, cfg_key in mapping.items():
        val = getattr(args, arg_key)
        if val is not None:
            cfg[cfg_key] = val
    return cfg


def main(argv):
    args = parse_args(argv)
    cfg = build_config(args)
    r = model(cfg)
    print(report(cfg, r))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
