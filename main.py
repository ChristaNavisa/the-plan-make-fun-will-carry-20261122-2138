#!/usr/bin/env python3
"""Write the 30-day plan text to the output directory.

Stdlib only, no network. The plan is a single 278-character text
(1-280 characters allowed) written with no trailing newline.
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
    if not 1 <= len(PLAN) <= 280:
        raise ValueError(f"plan must be 1-280 characters, got {len(PLAN)}")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
