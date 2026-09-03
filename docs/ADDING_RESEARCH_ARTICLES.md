# Adding research articles

Research articles are ordinary Jekyll posts. Add a Markdown file to `_posts` using the filename pattern `YYYY-MM-DD-short-title.md` and one of the
four topic categories below.

| Research page | Category value |
| --- | --- |
| Escaping Atmospheres | `escaping-atmospheres` |
| Astrobiology | `astrobiology` |
| Temperate Planet Atmospheres | `temperate-planet-atmospheres` |
| Future Telescopes & Instruments | `future-telescopes-instruments` |

Start each file with front matter like this:

```yaml
---
layout: post
title: Your article title
date: 2026-09-03 12:00:00
description: A one- or two-sentence summary for the research archive.
categories: escaping-atmospheres
tags: exoplanets spectroscopy
---
```

Write the article below the closing `---`. The topic archive sorts matching posts by `date` in reverse order, so the most recent article automatically
appears first.
