# Experiment 1

Question: how many days before an official positive diagnostic result does out-of-area discrimination stay above matched negative controls?

## Rules

- Labels: campaign xlsx. Diagnostic result, not named assay until read.
- First geography: 2021 olives in the Crecco Brindisi bbox.
- Match: ±30 days; same comune else ≤5 km; cultivar when both known; ≥60 m apart (different 20 m SWIR cell).
- Crown area: not used while Crecco is points only.
- Lags: −365, −180, −90, −60, −30, 0, +90 days from the positive’s diagnostic date.
- Move: |Cliff δ| ≥ 0.15 and p < 0.05 on NDMI. Hold out whole comuni.
- Do not train a classifier. Do not pool 2024 non-olive positives.

## 2021 Crecco-box table (current)

1,683 pos, 1,917 neg, **1,679** matches (4 unmatched). Same comune 1,675. Cultivar locked 457. Median distance 68 m.

NDMI, SCL-ok both arms:

| Lag | n | δ | p |
|---:|---:|---:|---:|
| −365 | 331 | +0.05 | 0.31 |
| −180 | 902 | −0.05 | 0.08 |
| −90 | 1330 | −0.08 | 0.002 |
| −60 | 1325 | −0.07 | 0.005 |
| −30 | 1313 | −0.05 | 0.030 |
| 0 | 1325 | −0.07 | 0.003 |
| +90 | 1164 | +0.03 | 0.25 |

No lag meets the bar. −90…0: positives slightly drier, small effect. Cisternino (only other comune with n≥30) does not replicate; p-values are Ostuni-driven.

STAC scenes used start 2020-10-31. −365 is thin.

Files: `nowcast/cache/experiment1_matches_2021.csv`, `experiment1_lags_2021.csv`.
