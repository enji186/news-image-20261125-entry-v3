#!/usr/bin/env python3
"""Ship the make.fun news-image-20261125 entry (v3).

The entry image is the user's own picture, prepared at the required
1024x1024 size and stored in this repository as entry.png. This program
only copies it to the output directory the platform provides.

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

ENTRY = "entry.png"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), ENTRY)
    if not os.path.isfile(src):
        print(f"error: {ENTRY} not found next to main.py", file=sys.stderr)
        return 1
    dst = os.path.join(out_dir, ENTRY)
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        print(f"error: copied {ENTRY} has the wrong size", file=sys.stderr)
        return 1
    print(f"copied {ENTRY} to {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
