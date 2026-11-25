"""The Tired Dark Lord: a 100-word villain monologue, entry for the make.fun
competition u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.

The monologue keeps the tiredness in the rhythm and the small deflections - the
sinking chair, the dim orb, the scheme filed under a housekeeping list - while
the speaker stays a villain with a scheme (the Mildlands) and a history
(fourteen sword fights), and never states plainly that he is tired.

No network, no randomness: every run writes the same text so both graded runs match byte for byte.
"""

import os
from pathlib import Path

MONOLOGUE = ("Another prophecy. Sit down, hero, sit. No - the chairs on the left sink; curse-melt, "
             "third century, don't ask. Yes, the orb is dim. Orbs dim. You would too, if every decade a "
             "chosen one climbed seven thousand stairs to interrupt your lunch. My scheme? Annexing the "
             "Mildlands, eventually. It's on a list. Under 'reorganize dungeon', probably. The hounds are "
             "asleep and I'm not waking them for a sword fight I've had fourteen times. So: shout your "
             "destiny, take the crystal from the obvious pedestal - the real one's in my pocket - and mind "
             "the step on your way out. I'll be here.")


def main():
    text = MONOLOGUE.strip()
    out = Path("/output")
    os.makedirs(out, exist_ok=True)
    entry_path = out / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
