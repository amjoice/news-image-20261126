#!/usr/bin/env python3
"""news-image-20261126 entry program.

Writes the pre-rendered front-page image shipped in this repository to
/output/entry.png. Standard library only; no network; deterministic.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
import shutil
from pathlib import Path


def entry_source() -> Path:
    """The pre-rendered image shipped beside this program."""
    return Path(__file__).resolve().parent / "entry.png"


def output_dir() -> Path:
    """Where the grader reads the image; MAKEFUN_OUTPUT_DIR overrides locally."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(entry_source(), target_dir / "entry.png")


if __name__ == "__main__":
    main()
