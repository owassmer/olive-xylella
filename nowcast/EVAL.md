# Experiment 1 evaluation ledger

**Status:** EMPTY PREREGISTERED TEMPLATE

This file is the result surface for `nowcast/EXPERIMENT1.md`. Do not delete failed arms, change the estimand after seeing a table, or promote a claim beyond the claim ladder.

Before the first result is entered, record the contract commit and manifest hash below.

---

## 0. Run identity

| Field | Value |
|---|---|
| Contract commit | `TBD` |
| Analysis commit | `TBD` |
| Run manifest | `TBD` |
| Manifest SHA-256 | `TBD` |
| Source workbook hashes | `TBD` |
| Execution date | `TBD` |
| Operator | `TBD` |
| Python / package lock | `TBD` |

**Protocol deviations:** `NONE / list every deviation before interpreting results`

---

## 1. Cohort flow

### 1.1 Diagnostic rows

| Step | Positive rows | Negative rows | Notes |
|---|---:|---:|---|
| Workbooks read | — | — | |
| Olive host | — | — | |
| Parseable date + coordinates | — | — | |
| `pauca` filter where available | — | — | |
| Diagnostic result resolved | — | — | |
| Tree identity resolved | — | — | |
| Crown attached: high | — | — | |
| Crown attached: medium | — | — | |
| Crown attachment failed | — | — | report, do not hide |
| Eligible for matching | — | — | |
| Matched primary cohort | — | — | |
| Unmatched residual | — | — | |

### 1.2 Effective units

| Unit | Cases | Controls | Total / notes |
|---|---:|---:|---|
| Raw rows | — | — | |
| Unique official IDs | — | — | |
| Inferred tree keys | — | — | |
| Unique coordinates | — | — | |
| Unique 10 m pixels | — | — | |
| Unique 20 m pixels | — | — | |
| Mixed-label 20 m pixels | — | — | |
| Spatial blocks | — | — | |
| Comuni | — | — | |

### 1.3 Repeated-label audit

| Category | n | Treatment |
|---|---:|---|
| Earlier negative → first positive | — | case history |
| Negative → positive within +365 d | — | primary control, flagged; excluded in durable-negative sensitivity |
| Same-date conflicting result | — | adjudication/exclusion table |
| Repeated positive after index | — | not a new case |
| Tree inferred from coordinate cluster | — | report confidence |

---

## 2. Matching audit

### 2.1 Balance before and after matching

Report standardized mean differences and distributions, not only p-values.

| Covariate | Before SMD | After SMD | Pass threshold | Notes |
|---|---:|---:|---:|---|
| Sample date | — | — | `|SMD| ≤ 0.10` | |
| Geographic distance / coordinates | — | — | `|SMD| ≤ 0.10` | |
| Cultivar | — | — | categorical balance | |
| Log crown area | — | — | `|SMD| ≤ 0.10` | |
| Crown fraction 10 m | — | — | `|SMD| ≤ 0.10` | |
| Crown fraction 20 m | — | — | `|SMD| ≤ 0.10` | |
| Pre-index drought/weather | — | — | `|SMD| ≤ 0.10` | |
| Irrigation proxy/class | — | — | categorical balance | |
| Elevation / soil class | — | — | where available | |

### 2.2 Match tiers

| Tier | Matched cases | Share | Median distance | Notes |
|---|---:|---:|---:|---|
| Same comune + cultivar | — | — | — | |
| Same comune, cultivar relaxed | — | — | — | |
| ≤5 km + cultivar | — | — | — | |
| ≤5 km, cultivar relaxed | — | — | — | |
| Unmatched | — | — | — | |

State whether any outcome-derived feature entered matching: **must be NO**.

---

## 3. Scene and missingness audit

For every target lag, report the scene-selection process before endpoint values.

| Target lag | Eligible matched sets | Valid scene | Missing scene | Median actual lag | IQR actual lag | Median absolute lag error |
|---:|---:|---:|---:|---:|---:|---:|
| −365 | — | — | — | — | — | — |
| −180 | — | — | — | — | — | — |
| −90 | — | — | — | — | — | — |
| −60 | — | — | — | — | — | — |
| −30 | — | — | — | — | — | — |
| 0 | — | — | — | — | — | — |
| +90 | — | — | — | — | — | — |

### Pixel validity flow

| Target lag | Raw pixels | SCL=4 | 3×3 veg fraction pass | All bands finite | Unique 20 m clusters |
|---:|---:|---:|---:|---:|---:|
| −90 | — | — | — | — | — |
| −60 | — | — | — | — | — |
| −30 | — | — | — | — | — |
| 0 | — | — | — | — | — |

Report whether missingness differs by label, comune, cultivar, or crown size.

---

## 4. F7 fixed-scene audit

F7 is not called pre-diagnostic unless the scene precedes the case diagnostic date.

### 4.1 Timing relative to diagnosis

| Scene | Label | n trees | n unique 20 m pixels | Scene before diagnosis | Scene on/after diagnosis | Median lead/lag days |
|---|---|---:|---:|---:|---:|---:|
| 2021-08-12 | Positive / symptom absent | — | — | — | — | — |
| 2021-08-12 | Negative / symptom absent | — | — | — | — | — |
| 2021-08-22 | Positive / symptom absent | — | — | — | — | — |
| 2021-08-22 | Negative / symptom absent | — | — | — | — | — |

### 4.2 F7 endpoints

| Scene | Grid / feature | n positive clusters | n negative clusters | Cliff δ | Block-aware p | IID p sensitivity | Verdict |
|---|---|---:|---:|---:|---:|---:|---|
| 2021-08-12 | NDMI20, SCL=4 | — | — | — | — | — | |
| 2021-08-12 | NDMI_B8A20 | — | — | — | — | — | |
| 2021-08-12 | NDVI10 | — | — | — | — | — | |
| 2021-08-12 | NDRE20 | — | — | — | — | — | |
| 2021-08-22 | NDMI20, SCL=4 | — | — | — | — | — | |

**Allowed F7 verdict:** engineering feasibility / same-season association / symptom-absent association / pre-diagnostic subset at stated lead / inconclusive.

---

## 5. Relative-time index results

Primary endpoint: matched case-minus-control seasonal-residual `NDMI20`.

| Target lag | Actual lag median | Matched sets | Unique 20 m clusters | Case median | Control median | Matched difference | Cliff δ | Block-aware p | Pass pilot bar? |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| −90 | — | — | — | — | — | — | — | — | — |
| −60 | — | — | — | — | — | — | — | — | — |
| −30 | — | — | — | — | — | — | — | — | — |
| 0 | — | — | — | — | — | — | — | — | — |
| +90 | — | — | — | — | — | — | — | — | — |

### Common-support and purity sensitivities

| Analysis | −90 | −60 | −30 | Interpretation |
|---|---:|---:|---:|---|
| B08 resampled to B11 grid | — | — | — | primary |
| B8A + B11 | — | — | — | wavelength/grid sensitivity |
| SCL `{4,5,7}` | — | — | — | continuity with pilot |
| High crown fraction only | — | — | — | mixed-pixel falsifier |
| Same-comune only | — | — | — | spatial confounding |
| Exact-cultivar only | — | — | — | cultivar confounding |
| Durable negatives | — | — | — | latent/future-positive control |

---

## 6. Negative controls and placebo results

| Test | Metric | Result | Pass/fail | Meaning |
|---|---|---|---|---|
| Within-match label swaps | — | — | — | null calibration |
| Within-comune/spatial-block shuffle | — | — | — | place confounding |
| Location/campaign-only baseline | PR-AUC / budget recall | — | — | clipboard-policy prediction |
| Drought/weather-only baseline | PR-AUC / budget recall | — | — | abiotic explanation |
| Greenness-only baseline | PR-AUC / budget recall | — | — | late damage / canopy |
| Future-label/placebo lag | — | — | — | timing leakage |
| Low-crown-fraction removal | δ / PR-AUC | — | — | mixed pixel |
| Different pre-index season/year | δ | — | — | one-date weather |

Any failed falsifier must remain visible in the final verdict.

---

## 7. Out-of-area model evaluation

Complete only if the preregistered index and falsifier gates survive.

### 7.1 Fold definition

| Fold | Train geography/time | Held-out geography/time | Cases | Controls/candidates | Leakage audit |
|---|---|---|---:|---:|---|
| Spatial 1 | — | whole comune/block | — | — | |
| Spatial 2 | — | whole comune/block | — | — | |
| Temporal | 2020–21 | 2022–23 | — | — | positive-starved |
| Subspecies-clean | prior | 2024 olive + pauca | — | — | |
| Geographic shift | prior | 2025 Gargano | — | — | separate stress test |

### 7.2 Baseline comparison

| Model | PR-AUC | AUROC | Recall @ top 1% | Recall @ top 5% | PPV @ top 5% | Brier | Calibration verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| Prevalence / intercept | — | — | — | — | — | — | |
| Location/campaign only | — | — | — | — | — | — | |
| Drought/weather only | — | — | — | — | — | — | |
| NDVI/greenness only | — | — | — | — | — | — | |
| Full model | — | — | — | — | — | — | |

The full model must beat every required baseline on held-out data before a suspicion surface exists.

---

## 8. Claim ledger

Mark exactly one highest-supported claim.

- [ ] Engineering feasibility only
- [ ] Same-season diagnostic association
- [ ] Symptom-absent diagnostic association
- [ ] Pre-diagnostic discrimination at 30–60 days
- [ ] Pre-diagnostic discrimination at 90+ days
- [ ] Monitoring-only signal at/after diagnosis
- [ ] Closed negative after controls
- [ ] Operational front ranking validated out of area and time

### Required plain-language statement

> `TBD — include population, geography, actual lead, instrument support, controls survived, and what the result does not establish.`

### Artifact A decision

- [ ] Continue to WorldView-3 / PRISMA / airborne access request because a named physical/spatial limitation remains.
- [ ] Continue Sentinel/S1/Landsat work because the public-data signal survives but validation is incomplete.
- [ ] Close remote early-detection as a negative and redirect effort to the resistance decoder.
- [ ] Do not decide: protocol deviation or insufficient effective sample size.

---

## 9. Deviations, failures, and unresolved ambiguity

Every deviation receives a date, reason, affected rows/folds, and whether it was decided before or after seeing an endpoint.

| Date | Deviation / failure | Pre- or post-result? | Impact | Resolution |
|---|---|---|---|---|
| — | — | — | — | — |

No failed download, unmatched case, missing scene, crown miss, mixed-label pixel, or contradictory assay interpretation is omitted from this ledger.