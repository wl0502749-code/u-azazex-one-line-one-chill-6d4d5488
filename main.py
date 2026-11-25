#!/usr/bin/env python3
"""One Line, One Chill — a single-sentence horror line.

The program writes exactly one line of horror to /output/entry.txt:
one sentence, under 200 characters, built to frighten a reader in a
single breath. The scare is earned, not announced: no gore, no mirror,
no doll, no basement — just a concrete, everyday detail (a phone
photo) with a last word that reframes the whole sentence.
"""

import os

LINE = "Every morning my phone has a new photo of me asleep, taken from inside my closet."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
