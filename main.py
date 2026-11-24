#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

Writes a single one-line office joke to /output/entry.txt.
The joke is a plain constant: the whole entry is the line itself.
The em dash is a single Unicode character, so the line stays one line.
"""
import os

JOKE = (
    "The office printer has been 'out of order' since 2023, which technically "
    "makes it our longest-serving employee \u2014 it never calls in sick, "
    "and it never prints either."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "entry must be one line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
