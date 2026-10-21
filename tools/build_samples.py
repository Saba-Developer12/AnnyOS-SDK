#!/usr/bin/env python3
"""Build every AP assembly-like sample into an AnnyOS .AP application."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
PACKER = ROOT / "tools" / "ap_pack.py"
SOURCE_DIR = ROOT / "apps"
OUTPUT_DIR = ROOT / "build"


def main() -> int:
    sources = sorted(SOURCE_DIR.glob("*.apasm"))
    if not sources:
        print(f"No .apasm samples found in {SOURCE_DIR}", file=sys.stderr)
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for source in sources:
        output = OUTPUT_DIR / f"{source.stem}.AP"
        subprocess.run(
            [sys.executable, str(PACKER), str(source), str(output)],
            check=True,
        )
        print(f"Built {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
