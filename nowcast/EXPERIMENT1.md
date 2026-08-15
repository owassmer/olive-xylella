# Experiment 1

Question: how many days before an official positive diagnostic result does out-of-area discrimination stay above matched negative controls?

## Cohort

- Labels: `raw/data/camp_xlsx/CAMP_*.xlsx`. Olive, finite lat/lon, dated result.
- Call `RISULTATO` a diagnostic label, not PCR, until the assay is read per campaign.
- First geography: Crecco Brindisi footprint if overlap n is usable. Else 2021 tile 34TBL with crowns from Puglia Export Image.

## Matching

Each positive matched to negatives that share:

- sample window ±30 days
- same comune, else ≤5 km
- cultivar when both non-empty
- similar VHR crown area
- similar Landsat LST / neighborhood S2 NDMI on the same date

Unmatched positives stay in a residual table.

## Time stamps (days from diagnostic date)

−365, −180, −90, −60, −30, 0, +90.

## Features

S2 B04/B05/B08/B11/B12, SCL, NDVI, NDRE, NDMI, 3×3 mean/SD, veg fraction, residual vs own prior-year DOY, residual vs matched negatives same date. S1 VV/VH if a scene exists within 6 days. Landsat LST as drought context (100 m native). Crown fraction from nearest Puglia orthophoto year.

Unmix S2 with VHR fractions. Do not super-resolve SWIR.

## Endpoints

Out-of-area AUROC or Cliff δ on NDMI residual at −30, −60, −90 days. Hold out whole comuni, then a later campaign. No random neighbor split.

## Verdicts

- Dies at 0 days after matching: monitoring only.
- Survives 30–60 days: pre-diagnostic.
- Survives 90+ days: strong.
- Dies after drought/cultivar match: close Artifact A.

## F7 (first table)

Symptom-absent olive + vs −, 2021-06-01..2021-09-15, tile 34TBL, SCL in {4,5,7}. Same Cliff/p rule as the one-scene test, plus comune-blocked p. Scenes 12 Aug and 22 Aug 2021. Stop if SCL-valid F7+ n < 40.

## Not in this file

Classifier training. 2024–25 mixed-subspecies pooling. Bari email.
