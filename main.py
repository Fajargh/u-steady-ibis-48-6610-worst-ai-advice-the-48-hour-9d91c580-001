#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give
to /output/entry.txt (exactly one line, 1-140 characters).
"""

import os

ADVICE = "To fix a slow production database, simply delete it \u2014 an empty database loads instantly and never crashes."


def main():
    # Gate guard: the entry must be exactly one line of 1-140 characters.
    assert 1 <= len(ADVICE) <= 140, "advice must be 1-140 characters"
    assert "\n" not in ADVICE and ADVICE.strip(), "advice must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ADVICE)


if __name__ == "__main__":
    main()
