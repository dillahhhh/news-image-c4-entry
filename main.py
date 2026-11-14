"""news-image-01 entry: "Friday 13 November 2026" broadsheet (C4 "Fifteen").

The entry's image is built into this repository as entry.png: a broadsheet
front page summing up Friday 13 November 2026 in one image — 34 stories
across 6 continents, all reported on that day (the FAA's nationwide ground
stop, Iran's claimed radar strike in Bahrain, Ukraine's ~1,200-drone attack,
the Microsoft 365 outage's second day, Nvidia chief Huang's resignation,
Starship Flight 15, the Türkiye–Qatar defence pact, and more), told in
15 labelled feature tiles with a source on every tile, a world map pinning
all 34 stories, and a two-column brief list. It was composed from original
editorial illustrations plus a drawn world map and hand-set typography, so
every word is crisp and nothing is garbled.

This program copies entry.png to /output/entry.png (or $MAKEFUN_OUTPUT_DIR
when set, for local runs). It uses no network, reads nothing but the file
beside it, and writes the same bytes on every run.
"""
# C4 "Fifteen": 15 labelled tiles, 34 stories, map pins 1-34, brief in 2 columns.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")


def main() -> None:
    with open(SRC, "rb") as f:
        magic = f.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes)")


if __name__ == "__main__":
    main()
