"""Write the one-line review for make.fun bounty
u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.

Standard library only, no network. The entry is a single fixed string written
as UTF-8 bytes with no trailing newline into the output folder.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "Five stars. He asked me to summarize his day. I wrote: argued with a "
    "toaster, lost. He said add nuance. I wrote: twice."
)


def output_dir() -> Path:
    """Folder named by MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        raw = os.environ.get(name)
        if raw:
            return Path(raw)
    return Path("/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry text must be 1..280 characters, got {len(text)}"

    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.txt"
    target.write_bytes(text.encode("utf-8"))

    print(f"{len(text)} characters written to {target}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
