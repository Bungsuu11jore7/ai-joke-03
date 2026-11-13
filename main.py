"""ai-joke-03 entry: write one fixed one-liner about AI coding agents.

Deterministic by design: no network, no randomness, no clock, no input.
Every run writes the exact same bytes to /output/entry.txt.
The joke is fixed at import time; nothing is computed from the environment.
"""
import os

JOKE = (
    "My coding agent debugged my code, "
    "then filed a bug report against me for writing it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
