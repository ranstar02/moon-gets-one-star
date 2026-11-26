"""Entry for make.fun's "The Moon Gets One Star" bounty.

Writes a single one-star review of the Moon (max 120 characters)
to /output/entry.txt. No dependencies, no network, deterministic.
"""

import os

REVIEW = (
    "1 star. The Moon runs my tides without asking, "
    "ghosts me for days and stares through my window at 3 AM. Rude."
)


def main():
    if not 1 <= len(REVIEW) <= 120:
        raise ValueError(f"review must be 1-120 chars, got {len(REVIEW)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
