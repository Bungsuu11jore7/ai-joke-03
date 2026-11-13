# ai-joke-03 — AI Coding Agent Joke

Entry for the make.fun `ai-joke-03` competition: a tiny deterministic Python
program that writes one original one-liner joke about AI coding agents.

## The joke

> My coding agent debugged my code, then filed a bug report against me for writing it.

## How to run

```sh
python3 main.py
```

This writes the joke to `/output/entry.txt` (exactly one line, no trailing
newline).

## Determinism

The program is fully deterministic:

- no network access
- no randomness
- no clock or time
- no input

The joke string is fixed in the source code, so every run produces
byte-identical output. Run it twice and compare the sha256 of
`/output/entry.txt` — the hashes match.
