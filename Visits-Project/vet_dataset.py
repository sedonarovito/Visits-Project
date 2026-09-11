"""
vet_dataset.py — runs the Session 1 five-test vetting check on the T-100 extract.

Usage:
    1. Put the five monthly CSVs in ./data/
    2. python vet_dataset.py
    3. Copy the printed numbers into the [fill] slots in proposal.md

Nothing here is analysis. This only answers: is this dataset workable?
"""

import glob
import os

import pandas as pd

DATA_DIR = "data"
WINTER = [(2024, 12), (2025, 1)]
SUMMER = [(2025, 6), (2025, 7), (2025, 8)]


def load():
    """Read every CSV in data/ and stack them."""
    paths = sorted(glob.glob(os.path.join(DATA_DIR, "t100_market_*.csv*")))
    if not paths:
        raise SystemExit(f"No files found in {DATA_DIR}/ — download them first.")

    frames = []
    for p in paths:
        # TranStats exports often carry a trailing comma -> one unnamed empty column
        part = pd.read_csv(p, low_memory=False)
        part = part.loc[:, ~part.columns.str.startswith("Unnamed")]
        frames.append(part)
        print(f"  loaded {os.path.basename(p):<32} {len(part):>8,} rows")

    df = pd.concat(frames, ignore_index=True)
    df.columns = df.columns.str.upper()
    return df, paths


def test_1_grain(df):
    """One row is one carrier x market x month x service class."""
    print("\n--- TEST 1: grain ---")
    print("One row is: one carrier's traffic on one origin-destination market,")
    print("in one month, for one service class.")

    key = ["YEAR", "MONTH", "UNIQUE_CARRIER", "ORIGIN", "DEST", "CLASS"]
    missing = [c for c in key if c not in df.columns]
    if missing:
        print(f"  MISSING COLUMNS: {missing}")
        print(f"  actual columns: {list(df.columns)}")
        return

    n_rows = len(df)
    n_unique = len(df.drop_duplicates(subset=key))
    print(f"  len(df)                  = {n_rows:,}")
    print(f"  unique on key            = {n_unique:,}")

    if n_rows == n_unique:
        print("  PASS — the key uniquely identifies a row.")
    else:
        print(f"  {n_rows - n_unique:,} duplicate rows on that key.")
        print("  Add AIRLINE_ID and DATA_SOURCE to the key and rerun before analysing.")
        dupes = df[df.duplicated(subset=key, keep=False)].sort_values(key)
        print(dupes.head(6).to_string())


def test_2_comparison(df):
    """Need a categorical to split by and a numeric to measure."""
    print("\n--- TEST 2: something to compare ---")
    print(f"  distinct DEST_CITY_MARKET_ID : {df['DEST_CITY_MARKET_ID'].nunique():,}")
    print(f"  distinct DEST airports       : {df['DEST'].nunique():,}")
    print(f"  distinct CLASS values        : {sorted(df['CLASS'].dropna().unique())}")
    print(f"  PASSENGERS dtype             : {df['PASSENGERS'].dtype}")
    print(f"  PASSENGERS total             : {df['PASSENGERS'].sum():,.0f}")
    print(f"  rows with PASSENGERS == 0    : {(df['PASSENGERS'] == 0).sum():,}")
    print("  PASS if there are 200+ destination markets and a numeric measure.")


def test_3_size(df, paths):
    """Row count and disk footprint."""
    print("\n--- TEST 3: size ---")
    mb = sum(os.path.getsize(p) for p in paths) / 1_048_576
    print(f"  rows      : {len(df):,}")
    print(f"  disk total: {mb:.1f} MB across {len(paths)} files")

    if len(df) < 500:
        print("  FAIL — too small.")
    elif len(df) > 3_000_000:
        print("  Large; sample or subset.")
    else:
        print("  PASS — in the sweet spot.")

    if mb > 50:
        print("  Over 50 MB — awkward on GitHub. Drop unused columns and re-save.")
    else:
        print("  PASS — comfortable for GitHub.")


def test_4_coverage(df):
    """Confirm all five months actually arrived."""
    print("\n--- TEST 4: period coverage ---")
    have = set(zip(df["YEAR"], df["MONTH"]))
    for label, months in [("winter", WINTER), ("summer", SUMMER)]:
        for y, m in months:
            mark = "ok " if (y, m) in have else "MISSING"
            n = len(df[(df["YEAR"] == y) & (df["MONTH"] == m)])
            print(f"  {label:<7} {y}-{m:02d}  {mark}  {n:>8,} rows")


def test_5_preview(df):
    """Actually look at the rows, per the guide."""
    print("\n--- TEST 5: look at it ---")
    keep = [c for c in ["YEAR", "MONTH", "UNIQUE_CARRIER", "ORIGIN",
                        "DEST", "DEST_CITY_NAME", "CLASS", "PASSENGERS"]
            if c in df.columns]
    print(df[keep].head(8).to_string(index=False))

    print("\n  Sanity check — top 10 destination markets, scheduled passenger only:")
    sched = df[(df["CLASS"] == "F") & (df["PASSENGERS"] > 0)]
    top = (sched.groupby("DEST_CITY_NAME")["PASSENGERS"]
                .sum()
                .sort_values(ascending=False)
                .head(10))
    print(top.to_string())
    print("\n  If these are the usual big hubs, the file is behaving as expected.")


if __name__ == "__main__":
    print("Loading files...")
    data, files = load()

    test_1_grain(data)
    test_2_comparison(data)
    test_3_size(data, files)
    test_4_coverage(data)
    test_5_preview(data)

    print("\nAll five checks run. Transfer the numbers into proposal.md.")
