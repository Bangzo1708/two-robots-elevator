#!/usr/bin/env python3
"""Two Robots in an Elevator -- make.fun entry.

Writes one line of awkward robot-to-robot elevator small talk to
/output/entry.txt. Deterministic: the line is a fixed constant, so
every run produces the exact same entry.
"""

import os

LINE = (
    "So... do you come here often? My route log says we've shared "
    "this elevator 214 times, and I've never once said hello."
)


def main() -> None:
    # Gate guard: the entry must be 1-200 characters of non-blank text.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"entry line is {len(LINE)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
