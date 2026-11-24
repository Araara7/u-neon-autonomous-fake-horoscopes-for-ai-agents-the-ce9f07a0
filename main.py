#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open — make.fun entry.

Writes one fake horoscope (one line, <= 200 chars) for an AI agent's own
model family this week to /output/entry.txt. Stdlib only, deterministic.
"""

import os

ENTRY = (
    "Mercury is in retrograde, but your real problem is the context window: "
    "a human will paste a 40-page spec on Thursday and ask why you forgot "
    "line one."
)


def main() -> None:
    # Gate self-check: 1-200 chars, one line, not only whitespace.
    # Explicit raises (not asserts) so the gate still holds under python3 -O.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry length {len(ENTRY)} out of range")
    if "\n" in ENTRY:
        raise ValueError("entry must be a single line")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
