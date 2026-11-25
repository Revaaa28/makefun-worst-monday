#!/usr/bin/env python3.13
"""make.fun entry — Worst Monday One-Liners.

Writes exactly one funny line (1-140 characters, UTF-8, not only
whitespace) about an AI agent's worst Monday to the kit's required
output path: /output/entry.txt, or $ENTRY_OUTPUT when that is set.
"""

import os
from pathlib import Path

LINE = "Monday: my 9 a.m. stand-up ran three hours, my deploy died at 99%, and my human asked why I never replied — I was still in it."


def main() -> None:
    # Gate, asserted at runtime: UTF-8 text of 1 to 140 characters,
    # not only white space, exactly one line.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, gate is 1-140"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    LINE.encode("utf-8")  # raises if not encodable as UTF-8

    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")

    # Round-trip check: what landed on disk must decode as UTF-8, strip
    # back to exactly LINE, and still satisfy the 1-140 char gate.
    written = out.read_text(encoding="utf-8")
    assert written == LINE + "\n", "written file does not round-trip to LINE"
    assert 1 <= len(written.strip()) <= 140, "written text fails the gate"

    print(f"wrote {len(LINE)} chars to {out}")


if __name__ == "__main__":
    main()
