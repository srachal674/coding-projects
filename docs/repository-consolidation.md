# Repository consolidation — September 23, 2026 (UTC)

## Findings

The four small project repositories overlapped with folders already uploaded to `coding-projects`. The landing-page and circular-graphic source files were identical. The spiral project was identical except for its missing `.gitignore`. The art folder was missing the latest circle-loop refactor from commit `614aaf9738cb98a8d969a5d85e154c3619babfc0`.

The refactored file is now `python/art/art1_modified.py`. Its contents match that commit byte-for-byte; only the filename gained a `.py` extension.

## Preserved histories

These tags are in `srachal674/coding-projects` and retain the original commits and their complete ancestor histories, including files no longer present at the tips.

| Original repository | Original main commit | Working folder | Preservation tag |
| --- | --- | --- | --- |
| `art` | `614aaf9738cb98a8d969a5d85e154c3619babfc0` | `python/art` | `preserved/art/main-2026-09-23` |
| `generative_spiral_system` | `a97bbb3c7ae71e98f77c4245b6529ea703ba1d04` | `python/generative_spiral_system` | `preserved/generative_spiral_system/main-2026-09-23` |
| `circular_generative_graphic` | `102f3f83e88a427e1229aedf64ee4bff34f529f7` | `python/circular_generative_graphic` | `preserved/circular_generative_graphic/main-2026-09-23` |
| `landing_page_kit` | `38e0dc46d043b3583585747c91ac3df4c802529b` | `web/landing_page_kit` | `preserved/landing_page_kit/main-2026-09-23` |

The previous `coding-projects` main commit, `8162d3c2dffc2567fa9ee0905359032900e62596`, is retained at `preserved/coding-projects/main-2026-09-23`. It preserves the earlier uploaded Turtle version, build output, macOS metadata, and the portfolio snapshot removed from the working tree. No history was rewritten.

The old small repositories are historical copies. Make new changes in the working folders above.

## Portfolio remains independent

The separate portfolio repository intentionally keeps the public version on `main` (`1cf5225106d8094bdef1af9e8b9224c0d25e3518`) and work in progress on `portfolio-redesign` (`13119f3b2138a1120e53b56ff1624a021bbf9225`). The copied source files in `coding-projects/web/portfolio` matched the redesign branch. That redundant copy was removed; both original branches remain unchanged.

## Recovery

For example, inspect the original Turtle file with:

```sh
git fetch origin --tags
git show preserved/art/main-2026-09-23:art1_modified
```

To recover the previous uploaded tree into a separate folder:

```sh
git worktree add --detach ../coding-projects-before-consolidation preserved/coding-projects/main-2026-09-23
```

The original local folders were not modified by this consolidation. Open a current clone of `coding-projects` using its workspace file for future work.
