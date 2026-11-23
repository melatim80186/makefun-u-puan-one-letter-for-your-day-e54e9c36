#!/usr/bin/env python3
"""One Letter for Your Day — entry: the letter C.

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

LETTER = "C"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "wb") as f:
    f.write(LETTER.encode("utf-8"))
