# U.S. Cities Most Commonly Visited During Winter vs Summer Break

What U.S. cities are most frequently visited during winter break compared to summer break?

Business Analytics II · University of Pittsburgh · Fall 2026


## Data

| | |
|---|---|
| Source | U.S. DOT / Bureau of Transportation Statistics — T-100 Domestic Market (U.S. Carriers) |
| Portal | https://www.transtats.bts.gov/ |
| Grain | One carrier's traffic on one origin–destination market, one month, one service class |
| Periods | Winter: Dec 2024, Jan 2025 · Summer: Jun–Aug 2025 |
| License | U.S. Government Work — public domain in the U.S. (17 U.S.C. §105) |
| Retrieved | `[date]` |

Full download parameters and provenance are in [`SOURCE.md`](SOURCE.md). The raw
extract is committed here because the license permits redistribution — federal
datasets have been removed and altered during 2025–2026, so the archived copy is the
one this analysis actually runs against.

## Repo structure

```
.
├── README.md              this file
├── SOURCE.md              where the data came from, and exactly how
├── proposal.md            project proposal (Session 1 deliverable)
├── vet_dataset.py         five-test vetting check on the raw extract
└── data/
    ├── t100_market_*.csv  monthly extracts, as downloaded
    └── L_CITY_MARKET_ID.csv
```

## Reproducing

```bash
pip install pandas
python vet_dataset.py
```

`vet_dataset.py` confirms the grain, size, and period coverage of the extract before
any analysis runs. It prints row count against unique-key count — if those diverge,
one row is not what it appears to be, and every downstream number would be suspect.

## Known limitations

1. T-100 is monthly, so December–January is a the length for winter break and cannot
   isolate the actual break weeks.
2. T-100 Market records each carrier's ticketed segment, so connecting passengers can
   appear in two markets. Metro-level aggregation reduces but does not eliminate this.
3. Arrivals include returning residents; the data cannot separate visitors from locals.
