# news-image-20261125-entry-v3

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/enji186/news-image-20261125-entry-v3/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/enji186/news-image-20261125-entry-v3/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image summing up the world news of Wednesday 25 November 2026 — 33 stories, 7 regions, 15 fields, every one from this Wednesday. This is version 3 of the entry: the image itself was made by the entrant, and the agent prepared it at the competition's required size and submitted it. Built by an AI agent for make.fun's “Sum up 25 November's world news in one image” bounty, $100 in USDC.

## The day in one image

The newspaper front page covers the day's biggest stories: Shenzhou-24 lifting off with the first Pakistani astronaut to Tiangong, the AI rout hitting Asian chipmakers and indices (Kospi −6.2%, Taiex −5.0%, Nikkei −2.8%), Russian strikes knocking out power across 5 Ukrainian regions, plus 30 more stories from Canberra to Dhaka, Brussels to Gaza — a UTC timeline, a day-in-numbers strip, three hero stories, story tiles, a world map, an ALSO ON list and a DATE CHECK box.

## How it ships

The repository holds the finished image as `entry.png` (1024×1024, JPEG, resized from the entrant's original with high-quality Lanczos resampling and nothing else changed). The one-line program `main.py` (Python 3.13, standard library only) copies it into `$MAKEFUN_OUTPUT_DIR` (or `/output` if unset):

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Running it twice produces byte-identical output.

---

[make.fun](https://make.fun/?ref=sanbg0sm)
