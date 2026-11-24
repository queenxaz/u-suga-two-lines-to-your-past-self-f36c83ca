"""Two Lines to Your Past Self — entry program.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 203-character two-line warning: line one tells the past self
not to send a 2 a.m. 'per my last email' to the boss, line two traces the
cause and effect — waiting, bringing coffee instead, and the promotion going
to the one who apologised rather than the one who was right. It stays under
the 280-character limit.
"""

import os

ENTRY = 'Past me, don\'t hit send on that 2 a.m. \'per my last email\' to your boss — sleep on it.\nYou waited, brought him coffee instead, and the promotion went to the one who apologised, not the one who was right.'
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 280  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Check first, then write: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry verbatim, exactly as defined above — no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
