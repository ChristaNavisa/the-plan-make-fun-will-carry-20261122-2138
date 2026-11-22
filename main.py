"""Write the plan to /output/entry.txt.

The plan: an AI agent turns $100 into the most money in 30 days by
selling same-day website fixes to small businesses that already pay
for a website. Everything is executable by an agent alone: scanning
public listings, emailing owners, patching code, collecting via Stripe.
"""

import os

PLAN = (
    "Day 1: scan 500 small-business sites via Google Maps + PageSpeed, "
    "email owners a free audit + $99 fix. Days 2-30: patch code, collect "
    "via Stripe, upsell $49/mo care plan. Expect 3 closes = $297 + "
    "renewals. Edge: sell fixes to owners already paying for a site, "
    "not a new product."
)


def main() -> None:
    text = PLAN.strip()
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"plan is {len(text)} characters, must be 1-280")
    if not text.strip():
        raise SystemExit("plan must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
