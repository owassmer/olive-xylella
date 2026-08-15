# Day 1 report — 15 August 2026

Contract gate (CORDON §5): *we can point to a row in the CSV, a lat/lon or comune, a Sentinel tile, and a PCR result, for at least 100 trees. If the open CSV is comune-level only, we downgrade the nowcast to comune/grid and say so.*

## Verdict: PASS — tree-level, and it is the front

The Puglia open CSV is **not** comune-level. Every complete row has `LATITUDINE` and `LONGITUDINE`. On the partial file we hold:

- 335,947 complete sample rows
- 304,541 olive rows with lat/lon + `RISULTATO` (PCR)
- 2,938 olive positives (0.965%)
- 100% of complete rows have coordinates
- Dates in this partial: 20 Jan 2020 – 28 Sep 2021 (years 2020 and 2021 only)
- Provinces: Brindisi, Taranto, Bari, BAT, a handful of Foggia. **Lecce is absent.**

That last fact is load-bearing. This is the official monitoring of the **buffer / northern front**, not a census of dead Salento. That is exactly the label set Artifact A needs.

Example joinable row (first data line):

- ID 730508
- 07/02/2020
- Mandorlo, Carovigno, Brindisi
- lat 40.72537601, lon 17.72236012 (comma decimal in file)
- RISULTATO Negativo, SINTOMO Assente

Sentinel-2: Planetary Computer STAC returned live L2A items over this bbox (tiles T34TBL, T34TBK, T33TYF, 29 Aug 2023, cloud ~5–10%). Catalog access needs no account. Pixel download not yet exercised.

## What is still blocked

| Item | State | Meaning |
|---|---|---|
| Full CAMP_2020_2022.csv (82 MB) | in flight | partial stats must not be quoted as complete |
| CAMP_2020_2023.csv | ACCESS_BLOCKED — CKAN url empty | 2023 hold-out year may be missing |
| emergenzaxylella.it maps | ACCESS_BLOCKED — connection reset | no official polygon layer yet |
| Zarco-Tejada 2018 PDF, EFSA 2016 PDF | Cloudflare | use extracted/OA copies |

If 2023 never appears, the nowcast hold-out becomes a spatial fold inside 2020–2022, not a later year. Recorded now so we do not pretend otherwise later.

## So what

We do **not** downgrade to comune nowcast. We proceed tree-level. Class is rare (~1% positive) — evaluation is precision-recall, never accuracy. Next build step is not more papers; it is finishing the CSV and writing the feature-join script against one Sentinel scene.
