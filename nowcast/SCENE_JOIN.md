# One-scene join — 15 August 2026

Question this file answers: *can we put a Sentinel-2 pixel on a Puglia PCR point, and does any 10 m index move with the label?*

Not: *is this a nowcast.* Not: *did we beat drought.*

## Scene and sample

- Scene: `S2A_34TBL_20210812_0_L2A` (Earth Search public COG, AWS). Cloud 0.014%.
- Date: 12 Aug 2021, inside the 2021 positive-rich year.
- Tile covers the labelled front (Bari / Brindisi / north Taranto), not Lecce.
- Candidates: olives surveyed 1 Jun–15 Sep 2021 inside the tile bbox: 286 pos, 4,378 neg.
- SCL prefilter (keep 4/5/7): 260 pos, 841 neg. Most “missing” negatives were the UTM-tile nodata fringe, not clouds.
- Kept: 50 pos + 50 neg. File: `nowcast/cache/scene_join_100.csv`.

## Decision rule (written before looking)

A feature moves if |Cliff’s δ| ≥ 0.15 **and** two-sided permutation p < 0.05. Predicted direction: positives lower (more drought-like) than negatives.

## Result

| Feature | mean pos | mean neg | Δ (pos−neg) | Cliff’s δ | perm p | Moves? |
|---|---:|---:|---:|---:|---:|---|
| NDVI | 0.334 | 0.367 | −0.033 | −0.124 | 0.29 | no |
| NDRE | 0.190 | 0.223 | −0.033 | −0.218 | 0.072 | no (direction only) |
| NDMI | −0.060 | −0.015 | −0.045 | −0.312 | 0.008 | **yes** |

NDMI is the Sentinel-2 moisture index `(NIR − SWIR1) / (NIR + SWIR1)`. Positives are drier. That is the same physical story as Zarco-Tejada’s thermal/water-stress traits, at 10 m, on official PCR.

NDVI does **not** clear the bar. A nowcast that is just greenness will lose to a drought baseline, which is why that ablation stays mandatory.

## What this does not prove

- One date, one tile, n = 100. Not a model.
- No drought control yet. NDMI also moves with irrigation and August heat.
- 10 m is not airborne hyperspectral. Zarco-Tejada’s >80% was a different instrument.
- 2022–23 labels are still starved. This test used 2021 on purpose.

## So what

The join path is real: CAMP lat/lon → public COG → index. The first spectral feature that earns its keep is **NDMI, not NDVI**. Next build step is the drought ablation on NDMI (and NDRE as a secondary), not another literature pass.
