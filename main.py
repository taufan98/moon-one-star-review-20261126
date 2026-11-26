#!/usr/bin/env python3
"""The Moon Gets One Star — make.fun entry.

Writes one funny single-line one-star review of the Moon
to /output/entry.txt (1-120 characters, UTF-8, single line).

Run: python3 main.py
"""

import os

REVIEW = (
    "One star. Works nights only, calls in sick for a week every month, "
    "and still takes credit for the tides."
)


def write_entry(line: str) -> str:
    """Write the line to /output/entry.txt (fallback: ./output/entry.txt).

    Returns the path written, after reading it back to confirm the exact
    bytes on disk match the line (plus one trailing newline).
    """
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    assert written == line + "\n", f"read-back mismatch in {out_path}"
    return out_path


def main() -> None:
    line = REVIEW.strip()
    assert 1 <= len(line) <= 120, f"entry is {len(line)} chars, must be 1-120"
    assert "\n" not in line, "entry must be a single line"
    out_path = write_entry(line)
    print(f"Wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
