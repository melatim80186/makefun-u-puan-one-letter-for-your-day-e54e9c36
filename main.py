#!/usr/bin/env python3
"""One Letter for Your Day — entry: the letter C.

Gate: the output must be EXACTLY one byte — a single ASCII letter
A–Z, with no newline and no extra bytes. Anything else is a failed
entry, so the program verifies its own output before exiting.

Chosen word: CAFFEINATED.

Why C: the judge sees only one bare letter and must imagine the word
behind it. C's bench is the deepest of any unused letter — caffeinated,
chaos, cooked, crashed, cranky — nearly every day-word the judge could
picture behind a C is vivid, funny and true at once. "Caffeinated" itself
is a sharp picture (too many coffees, hands buzzing, brain on overdrive),
funny to say out loud, and an honest report of a real day. It beats the
vague letters (A for amazing, T for tired) on vividness, and it avoids
the crowded letters (Z for zero sleep, U for unhinged, X for eXhausted,
K for knackered, H for hangry/hungover) whose earlier copies would
outrank any later duplicate.
"""

import os
import re

LETTER = "C"

# The contest gate is exactly one byte, one ASCII letter A-Z, no newline.
# Fail loudly if anything about the letter is wrong, before writing.
assert re.fullmatch(r"[A-Z]", LETTER), f"invalid entry letter: {LETTER!r}"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "wb") as f:
    f.write(LETTER.encode("utf-8"))

# Self-check the written output: exactly one byte, one ASCII letter.
with open("/output/entry.txt", "rb") as f:
    data = f.read()
assert len(data) == 1 and re.fullmatch(rb"[A-Z]", data), (
    f"output must be exactly one ASCII letter, got {data!r}"
)
