# Experiment 1 — frozen validity contract

**Status:** preregistration. This file defines who enters the study, which imagery is eligible, what is independent, and which claims the results may support. Results belong in `nowcast/EVAL.md`, never back-filled into this contract.

**Question:** How many days before an official positive diagnostic result does an olive show a remotely detectable signal that survives controls for place, date, cultivar, canopy composition, and drought?

**Primary scientific object:** a matched, relative-time test. The experimental object is a diagnostic tree/crown; the repeat spectral measurement is a Sentinel pixel or pixel neighborhood. Those are not the same unit and must not be counted as though they were.

---

## 1. Claim ladder

Results may advance only one rung at a time.

1. **Engineering feasibility** — official coordinates can be joined reproducibly to public imagery.
2. **Same-season diagnostic association** — imagery differs by diagnostic label, without a guaranteed temporal lead.
3. **Symptom-absent association** — the difference survives among trees marked `SINTOMO = Assente`. This is compatible with previsual disease but is not itself a pre-diagnostic result.
4. **Pre-diagnostic discrimination** — an acquisition taken before the case's diagnostic date separates cases from matched controls at a stated actual lead.
5. **Operational front ranking** — the signal generalizes out of area and time, is calibrated, and improves inspection yield over location-, drought-, and greenness-only baselines.

The fixed 12 and 22 August 2021 tables can establish rungs 1–3 only. They mix trees sampled before and after each scene unless explicitly restricted by diagnostic date. The 22 August table is a temporal repeat on the same cohort, not an independent validation cohort.

---

## 2. Source cohort and label language

**Source:** `raw/data/camp_xlsx/CAMP_*.xlsx`, official Regione Puglia campaign workbooks.

Include records that satisfy all of the following:

- olive host (`Olea` / `olivo` after normalized matching);
- finite latitude and longitude in WGS84;
- a parseable official sample/observation date;
- an official positive or negative `RISULTATO`;
- for campaigns carrying `SUBSPECIE`, olive positives must be `pauca`; other subspecies remain separate datasets;
- no coordinate outside the documented Puglia/monitoring extent.

Call `RISULTATO` an **official diagnostic label** until the assay and field semantics have been verified campaign by campaign. Do not globally relabel the workbooks as PCR.

Record the source workbook, sheet, source row, original ID, original field values, normalized values, and source-file hash in the cohort manifest.

---

## 3. Tree identity, repeated records, and index dates

### 3.1 Tree key

Prefer a stable official tree/sample identifier when its semantics are consistent inside a campaign. Otherwise construct a provisional tree key from coordinate clustering (2 m), host, and cultivar, and mark it `inferred`.

Every output reports:

- raw diagnostic rows;
- unique official IDs;
- inferred tree keys;
- unique coordinates;
- unique 10 m pixels;
- unique 20 m pixels;
- comuni and spatial blocks.

### 3.2 Repeated observations

- A **case** is indexed at its first known positive diagnostic date.
- Earlier negative observations on the same tree remain history, not controls.
- Later positive observations do not create additional cases.
- A tree cannot appear in both case and control sets in the same evaluation fold.
- A negative tree that later becomes positive is retained in the primary point-in-time control definition but flagged. A sensitivity cohort of **durable negatives** requires no recorded positive through +365 days.
- Conflicting results on the same date go to an adjudication table and are excluded from the primary analysis.

### 3.3 Control pseudo-index date

Each matched negative inherits the matched case's index date. Its imagery, weather windows, seasonal baseline, and lag labels are therefore evaluated on the same calendar dates as the case. Controls may not choose clearer or more convenient scenes.

---

## 4. Crown attachment and spatial support

The intended biological unit is the tree; the public repeat spectral support is 10–20 m.

Attach each diagnostic point to a crown using, in order:

1. a Crecco crown polygon inside the released footprint;
2. a crown derived from the closest suitable Puglia orthophoto;
3. an unresolved point with no crown attachment.

Store attachment method, source year, distance, crown area, crown fraction in the 10 m and 20 m footprints, and confidence (`high`, `medium`, `failed`). Never silently discard failed attachments.

For pre-diagnostic analyses, prefer a VHR source acquired on or before the index date. A post-index orthophoto can be used only as a geometry sensitivity analysis because disease, pruning, or removal may have changed the crown.

Multiple trees may share one Sentinel pixel. Keep the tree rows for biological bookkeeping, but:

- group all inference, resampling, and train/test assignment by 20 m pixel and spatial block;
- report the effective number of unique spectral observations;
- never place rows sharing a 20 m pixel in different model folds;
- report mixed-label pixels separately rather than treating their repeated reflectance as independent evidence.

VHR supports crown/soil fractions and unmixing. It does not create 1 m SWIR.

---

## 5. Matching contract

### 5.1 Primary match

Primary design is 1:1 matching without replacement, seed 42, performed inside each campaign before any spectral outcome is inspected.

A case is matched to a negative using this order:

1. same comune, sample date within ±30 days, same normalized cultivar when both are known;
2. same comune and date window, cultivar missing on one side;
3. within 5 km and date window, same cultivar;
4. within 5 km and date window, cultivar relaxed.

Within an eligible tier, minimize a prespecified distance over:

- log crown area;
- pre-index landscape drought/weather context;
- irrigation or persistent-summer-greenness class when available;
- elevation/soil class when available.

Use only variables measured before, or independently of, the target disease signal. **Do not match on same-date tree-level NDMI, NDRE, or another candidate spectral endpoint.** Neighborhood climate may be used only when computed outside the focal crown/pixel and documented as such.

Store match tier, component distances, reuse count, and rejection reason. Unmatched positives remain in a residual table.

### 5.2 Sensitivities

- 1:3 matching with replacement;
- same-comune only;
- exact-cultivar only;
- durable-negative controls;
- within-orchard/spatial-block pairs where an orchard proxy can be inferred.

No sensitivity replaces the frozen primary match.

---

## 6. Relative-time imagery

Target lags in days from the case index date:

`−365, −180, −90, −60, −30, 0, +90`

For each matched set and target lag:

1. calculate `target_date = case_index_date + target_lag`;
2. select the nearest valid Sentinel-2 L2A acquisition within ±10 days;
3. for every negative target lag, require the acquisition to be strictly before the case index date;
4. give the matched control the exact same acquisition;
5. break ties by lower valid-pixel cloud fraction, then by the earlier acquisition;
6. record target lag, actual lag, lag error, item ID, tile, processing baseline, and asset URLs;
7. if no valid scene exists, mark the lag missing. Do not widen the window after inspecting results.

Sentinel-1 may use the nearest valid acquisition within ±6 days of the selected Sentinel-2 date. Landsat LST may use ±8 days and is drought context at its native 100 m thermal support, even when delivered on a 30 m grid.

No feature at a negative lag may use data acquired after the diagnostic date. Seasonal baselines may use earlier years only.

---

## 7. Spectral extraction

### 7.1 Common-grid primary features

Sample and record raw surface reflectance before computing indices.

- `NDVI10 = (B08 − B04) / (B08 + B04)` on the 10 m grid.
- `NDMI20 = (B08_to_B11_grid − B11) / (B08_to_B11_grid + B11)` with B08 explicitly resampled once to the native B11 20 m grid.
- `NDMI_B8A20 = (B8A − B11) / (B8A + B11)` as a prespecified sensitivity.
- `NDRE20 = (B8A − B05) / (B8A + B05)` on a common 20 m grid.
- B12-based moisture/burn indices may be reported as secondaries if named before extraction.

Store resampling method and grid transform. Do not describe B11 or red-edge information as independent 10 m measurements.

### 7.2 Pixel validity

Primary scene-validity rule:

- center pixel `SCL = 4` (vegetation);
- no cloud, cirrus, cloud shadow, snow, saturation, or nodata;
- 3×3 valid-vegetation fraction ≥0.40;
- all bands required for the endpoint finite.

Prespecified sensitivity: the earlier `{4, 5, 7}` SCL rule, reported separately. If the primary rule materially changes class balance or geography, show the flow table.

### 7.3 Derived features

At each lag, derive:

- center value, 3×3 mean, 3×3 standard deviation, and valid fraction;
- VHR crown and soil fractions;
- residual from the tree/pixel's own earlier-year seasonal baseline (same day-of-year ±15 days, earlier years only);
- residual from the matched negative on the same scene;
- Sentinel-1 VV/VH and change features when available;
- Landsat LST, meteorological drought, and neighborhood moisture as context rather than pathogen measurements.

The main comparison must survive a location/drought-only baseline. A model that predicts the monitoring geography is not a disease detector.

---

## 8. F7: the first controlled table

F7 is a symptom-status stress test inside Experiment 1, not a substitute for relative-time analysis.

**Cohort:** symptom-absent olive positives versus symptom-absent olive negatives, summer 2021, tile 34TBL, scenes 12 and 22 August 2021.

Before any endpoint is reported, publish:

- scene date minus diagnostic date by label;
- counts sampled before versus after each scene;
- cultivar and comune balance;
- unique 10 m and 20 m pixel counts;
- shared/mixed-label pixel counts;
- SCL flow and VHR attachment flow.

The fixed-scene F7 table may be called **symptom-absent diagnostic association**. Only the subset with imagery before the case's diagnostic date may be described as pre-diagnostic, and its actual lead distribution must be stated.

Power stop: do not run the primary F7 test with fewer than 40 SCL-valid **positive 20 m pixel clusters**. Tree rows sharing a SWIR pixel do not satisfy this threshold.

---

## 9. Endpoints and inference

### 9.1 Prespecified index tables

At −30, −60, and −90 days, primary descriptive endpoint is the case-minus-control difference in `NDMI20` seasonal residual.

Report:

- matched sets, trees, and unique 20 m clusters;
- medians and distributions by label;
- matched difference and confidence interval;
- Cliff's delta for continuity with the pilot;
- label-swap/permutation inference within matched sets, with resampling performed at the 20 m cluster or larger spatial block;
- iid permutation only as a sensitivity.

A feature clears the pilot continuity bar only when `|Cliff's δ| ≥ 0.15` and the block-aware two-sided permutation `p < 0.05`. This is not by itself an operational-model success criterion.

### 9.2 Operational model, only after index tables survive

No classifier is trained until the matching, F7, lag tables, and negative controls are complete.

Validation:

- grouped folds that hold out whole comuni/spatial blocks;
- no shared 20 m pixel, orchard proxy, or near-neighbor cluster across folds;
- later campaigns as external tests, reported separately:
  - 2022–23: temporal but positive-starved;
  - 2024: olive + `pauca` only;
  - 2025 Gargano: geographic-shift stress test, not pooled into Brindisi.

Primary model metrics:

- precision–recall AUC;
- recall and positive predictive value at fixed inspection budgets (top 1%, 5%, and 10% of candidates);
- calibration curve and Brier score.

AUROC is secondary. Accuracy is not reported as a headline metric.

Mandatory baselines:

1. location/campaign/sampling-policy only;
2. drought/weather/irrigation only;
3. NDVI/soil-adjusted greenness only;
4. full spectral + context model.

The full model must beat all three on held-out data.

---

## 10. Negative controls and falsifiers

Run before any partner-facing claim:

- label swaps inside matched sets and comuni/spatial blocks;
- a location-only model to expose clipboard geography;
- future-label/placebo-lag tests where biologically appropriate;
- durable-negative sensitivity;
- SCL=4-only and common-20 m-grid sensitivities;
- removal of low-crown-fraction pixels;
- same-comune-only matching;
- pre-index imagery from a different season/year;
- wrong-host or wrong-subspecies controls only when the biological interpretation is valid and labels are kept separate.

Artifact A loses the word **pre-diagnostic** if the signal:

- appears only when symptomatic positives are included;
- disappears under block-aware inference;
- disappears after place/cultivar/drought/crown controls;
- is reproduced by location-only or drought-only baselines;
- depends on post-diagnostic imagery;
- depends on repeated trees sharing a small number of SWIR pixels.

---

## 11. Verdicts

Use the highest supported statement and no stronger one.

- **Engineering feasibility:** joins work; no valid biological association.
- **Same-season association:** label separation without guaranteed temporal lead.
- **Symptom-absent association:** separation among `SINTOMO = Assente`, temporal lead unresolved.
- **Pre-diagnostic 30–60 days:** negative-lag, matched, out-of-area signal survives.
- **Pre-diagnostic 90+ days:** same at −90 or earlier.
- **Monitoring only:** signal appears at/after diagnosis but not before.
- **Closed negative:** signal dies after the frozen controls; stop remote early-detection and move effort to the decoder.

A negative result is a completed Artifact A, not a failed project.

---

## 12. Provenance and required outputs

Every run writes a machine-readable manifest containing:

- git commit;
- source file names and SHA-256 hashes;
- campaign-specific field mapping;
- filters and exclusion counts;
- random seed;
- tree-key and duplicate rules;
- matching configuration;
- scene search windows and selected item IDs;
- band assets, grids, and resampling;
- software/package versions;
- output hashes.

Required tracked documents:

- `nowcast/EXPERIMENT1.md` — this frozen contract;
- `nowcast/EVAL.md` — empty-before-run result ledger, then final tables;
- `nowcast/SCENE_JOIN.md` — pilot engineering/same-season result;
- `nowcast/cache/*.manifest.json` — local, gitignored run manifests;
- `checks/verify_experiment_contract.py` — contract/manifest gate.

Do not email Bari, train a classifier, or publish a suspicion surface before the relevant gates above are closed.