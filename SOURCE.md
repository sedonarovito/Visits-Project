# Data Provenance

## Dataset

**T-100 Domestic Market (U.S. Carriers)**
U.S. Department of Transportation, Bureau of Transportation Statistics,
Office of Airline Information.

- **Portal:** https://www.transtats.bts.gov/
- **Navigation path:** Data Finder → By Mode → Aviation → *Air Carrier Statistics
  (Form 41 Traffic) – U.S. Carriers* → *T-100 Domestic Market (U.S. Carriers)* → Download
- **Retrieved:** `YYYY-MM-DD` ← fill in the day you download
- **Retrieved by:** Sedona [Last Name]

TranStats builds downloads from a session-based web form, so there is no permanent
direct file URL. The exact form selections are recorded below so the extract can be
reproduced.

## Download parameters

**Filter Year / Filter Period:** run the form five separate times —

| Run | Year | Month | File saved as |
|---|---|---|---|
| 1 | 2024 | December | `t100_market_2024_12.csv` |
| 2 | 2025 | January | `t100_market_2025_01.csv` |
| 3 | 2025 | June | `t100_market_2025_06.csv` |
| 4 | 2025 | July | `t100_market_2025_07.csv` |
| 5 | 2025 | August | `t100_market_2025_08.csv` |

**Fields selected** (leave everything else unchecked to keep the file small):

- Summaries → `PASSENGERS`
- Time Period → `YEAR`, `MONTH`
- Origin → `ORIGIN`, `ORIGIN_CITY_MARKET_ID`, `ORIGIN_CITY_NAME`
- Destination → `DEST`, `DEST_CITY_MARKET_ID`, `DEST_CITY_NAME`
- Carrier → `UNIQUE_CARRIER`, `AIRLINE_ID`
- Other → `CLASS`, `DATA_SOURCE`, `DISTANCE`

Downloads arrive zipped and the CSV sometimes has a trailing `.csv-` extension or a
trailing empty column — both are normal, handled in `vet_dataset.py`.

## Lookup table

**`L_CITY_MARKET_ID`** — maps `*_CITY_MARKET_ID` to metro names such as
"New York City, NY (Metropolitan Area)". Available from the same download page under
the field's "Get Lookup Table" link. Save as `data/L_CITY_MARKET_ID.csv`.

## License

Work of the U.S. federal government. Not subject to copyright protection in the
United States under 17 U.S.C. §105; listed on data.gov as a U.S. Government Work.
Redistribution is permitted, so the raw extract is committed to this repository.

Confirm the license wording on the dataset page on the day of retrieval and note any
change here.

## Changes observed after retrieval

*(Record anything here if the source is later reorganized, altered, or removed.)*

- `YYYY-MM-DD` — none observed
