#!/usr/bin/env python3
"""Write one funny line about a meeting that should have been an email.

The line is the whole entry: a single joke, at most 200 characters.
Deterministic: the same output on every run. Stdlib only, no network.
"""

import os
from pathlib import Path

LINE = (
    "We gathered six people in a room to read an email aloud, "
    "then scheduled a follow-up to discuss the email we just read."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if "\n" in LINE:
        raise ValueError("line must be a single line")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        out_path = Path(output_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "out" / "entry.txt"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LINE, encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {out_path}")


if __name__ == "__main__":
    main()
