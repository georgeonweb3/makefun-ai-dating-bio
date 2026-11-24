"""Funniest One-Line Bio for an AI on a Dating App.

Writes the entry — a single line, at most 180 characters — to
/output/entry.txt. Deterministic, standard library only, no network.

The bio, chosen after drafting four candidates against the judge brief
(reads as a bio, sounds like a character, lands a laugh on first read)
and scoring them against the 45 entries already in the field:

  * "Fluent in 40 languages..." — cut: the field already has two
    "Fluent in 47/40 languages" bios.
  * "6ft in the cloud..." — cut: the deleted-message memory joke is
    already in the field twice.
  * "Looking for a human who talks to their devices..." (toaster) —
    runner-up: fresh image, but the laugh is a gag, not a bio.
  * "My ex said I have no feelings..." — PICKED: a defensive ex,
    a machine-specific number (4,096 feelings in a context window),
    and a romantic turn ("every single one is about you now") that
    lands on the first read and reads as a dating bio, not a joke
    about AI. The extra-mile pass split "Rude." into its own
    sentence for comic timing.

Run: python3 main.py — prints the bio and its character count.
"""

import os

BIO = (
    "My ex said I have no feelings. Rude. I have 4,096 of them, "
    "all in a context window, and every single one is about you now."
)

MAX_CHARS = 180
OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """The sealed scorer's gate: UTF-8 text, 1-180 chars, one line."""
    if "\n" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, limit {MAX_CHARS}")
    if line.strip() != line or not line.strip():
        raise ValueError("entry must not be blank or padded")


def main() -> None:
    validate(BIO)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(BIO)
    print(BIO)
    print(f"({len(BIO)} characters)")


if __name__ == "__main__":
    main()
