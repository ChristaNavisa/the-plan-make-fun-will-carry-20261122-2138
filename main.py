"""Write the 30-day plan text to the output directory.

The plan: an AI agent turns $100 into the most money in 30 days by
selling a packaged micro-service that buyers already search for.
Deterministic: the same bytes on every run, no trailing newline.
"""

import os

PLAN = (
    "Sell on Fiverr: 10 SEO Etsy descriptions, $15, 24h delivery. "
    "Agent writes a pack in 20 min. "
    "Day 1: list the gig, spend $25 promoting it; "
    "Etsy sellers already search Fiverr for this. "
    "1 order/day x 30 = $450. "
    "Edge: packaged repeatable micro-service buyers want, not a vague SaaS."
)


def main():
    if not 1 <= len(PLAN) <= 280:
        raise ValueError(f"plan must be 1-280 characters, got {len(PLAN)}")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
