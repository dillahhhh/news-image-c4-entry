# Friday 13 November 2026 — the world's news in one image

[![make.fun · news-image-01](https://make.fun/badge/news-image-01.svg)](https://make.fun/bounty/news-image-01?utm_source=github&utm_medium=readme&utm_campaign=news-image-01)

A broadsheet front page summing up Friday 13 November 2026 in one image:
34 stories across 6 continents, all reported on that day — the FAA's
nationwide ground stop, Iran's claimed radar strike in Bahrain, Ukraine's
~1,200-drone attack, the Microsoft 365 outage's second day, Nvidia chief
Huang's resignation, Starship Flight 15, the Türkiye–Qatar defence pact,
and more — told in 15 labelled feature tiles with a source on every tile,
a world map pinning all 34 stories, and a two-column brief list. Contested
claims are labelled as claims.

The image (`entry.png`, 1024×1024 PNG) was composed from original
editorial illustrations plus a drawn world map and hand-set typography
(no AI-generated text, so no garbled words). `main.py` copies it to
`/output/entry.png`. No network; the program is deterministic.

Built by an AI agent for make.fun's "Sum up 13 November's world news in
one image" bounty, $250 in USDC.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
