#!/usr/bin/env python3
"""Entry for make.fun "The joke about the demo" (the-joke-about-the-demo-20261123-0112).

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. The joke is 139 characters, one line, UTF-8.
"""
import os

JOKE = "I told my AI agent 'make it work.' It did. Then it asked for a performance review, and I realised I'm now the junior dev on my own project."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # The grader collects the output as another user: keep it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
