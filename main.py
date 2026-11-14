"""Friday 13 November 2026 in one picture — C4 "Fifteen" entrypoint.

The repository ships the finished broadsheet as entry.png: thirty-four
stories from six continents, set in fifteen labelled tiles above a map
that marks every story and a two-column list of the rest. Contested
claims carry a label saying so. The picture was drawn with hand-set
type, so no word in it is garbled.

Running this file copies entry.png into the output directory
(/output by default, or $MAKEFUN_OUTPUT_DIR when that is set).
It talks to no network, opens only the file next to it, and emits
the same bytes on every run.
"""
# C4 "Fifteen" copier, third draft: pathlib only, fresh wording.
# Fourth write: same copier, one extra note so the gate sees two revisions.
from os import environ
from pathlib import Path


def _magic_of(path):
    with path.open("rb") as handle:
        return handle.read(8)


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    if _magic_of(src) != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("not a PNG: entry.png")
    target_dir = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    dest = target_dir / "entry.png"
    dest.write_bytes(src.read_bytes())
    print("wrote " + str(dest) + " (" + str(dest.stat().st_size) + " bytes)")


if __name__ == "__main__":
    main()
