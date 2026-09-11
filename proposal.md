# Project Proposal: U.S. Cities Most Commonly Visited During Winter vs Summer Break

Sedona Rovito

---

## 1. The question

**What U.S. cities are most frequently visited during winter break compared to summer break?**

Split: destination cities. Measure: number of  domestic arriving
flights in the each break. Comparison: winter break months vs. summer break months.
## 2. The dataset


 **Source**: U.S. DOT, Bureau of Transportation Statistics — Air Carrier Statistics (Form 41 Traffic), **T-100 Domestic Market (U.S. Carriers)** 
**URL**: https://www.transtats.bts.gov/ → Aviation → Air Carrier Statistics (Form 41 Traffic) – U.S. Carriers → T-100 Domestic Market 
**License**: U.S. Government Work — public domain in the U.S. (17 U.S.C. 105).
**Retrieved** 9/7/2026 **File size** 51 KB 
**Periods pulled** | Winter: Dec 2024, Jan 2025 · Summer: Jun, Jul, Aug 2025 |
| **Supporting file** | `L_CITY_MARKET_ID.csv` 


## 3. The grain

**One row is one airline's reported traffic on one origin–destination, in one
month, for one class.** Not one flight, and not one passenger.

Unique key: `YEAR + MONTH + UNIQUE_CARRIER + ORIGIN + DEST + CLASS`

## 4. The comparison

- **Split by:** `DEST_CITY_MARKET_ID` (all airlines count for one city, so JFK/LGA/EWR count as one New
  York and MCO/SFB count as one Orlando)
- **Measure:** `PASSENGERS`, converted to each city's percent of all domestic
  arriving passengers in that period
- **Statistic:** a seasonality index per city = winter share ÷ summer share. Above 1
  means visited more in the winter, below 1 means visited more in the summer.

## 5. Why either answer is interesting

**If the breaks differ:** People are able to understand and see which U.S. cities actually get more tourism depending on season that therefore, businesses can benefit and learn from those statistics to get better profit from all those people visiting on dedicated breaks.

**If the breaks are the same:** People can see which cities are both popular during winter break and summer break and determine their travel plans based on that information. Whether they want to go to a more popular and busy destinantion or not.


