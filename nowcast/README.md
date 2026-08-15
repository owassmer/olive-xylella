# nowcast/ — Artifact A workspace

Artifact A asks whether an official diagnostic-positive olive has a remotely detectable precursor after controls for place, date, cultivar, canopy composition, drought, and the monitoring design itself.

## Current state

- `SCENE_JOIN.md` is a successful engineering join and a same-season association on 100 official 2021 labels. NDMI moved; NDVI did not. It is **not** a nowcast and does not by itself establish pre-diagnostic lead time.
- `EXPERIMENT1.md` is the frozen study contract. It defines the claim ladder, case/control dates, matching, relative-time scene selection, common spectral support, effective sample units, falsifiers, and stop rules.
- `EVAL.md` is the preregistered result ledger. Failed arms and protocol deviations remain visible there.
- `cache/` is gitignored. New F7 and longitudinal CSVs require sidecar manifests and are gated by `checks/verify_experiment_contract.py`.

## Execution order

1. Inventory Crecco and attach/score crown geometry.
2. Count CAMP × Crecco overlap and unique 20 m spectral clusters.
3. Run the F7 audit before the F7 endpoint: diagnostic timing relative to each fixed scene, symptom/cultivar/comune balance, repeated pixels, SCL flow, and crown attachment.
4. Run the matched relative-time tables at −90, −60, and −30 days.
5. Run spatial, drought, mixed-pixel, and monitoring-policy falsifiers.
6. Train an operational model only if the preregistered index tables survive.

## Claim discipline

Use the highest rung actually supported:

`engineering feasibility → same-season association → symptom-absent association → pre-diagnostic lead → operational front ranking`

Symptom absence is not automatically temporal lead. A second date on the same cohort is repeatability, not an independent validation cohort. Trees sharing a 20 m SWIR pixel are repeated biological labels on one spectral observation and must remain grouped in inference and validation.

## Evaluation

The positive class is rare and the monitoring frame moves north over time. Operational evaluation therefore uses grouped spatial/temporal folds, precision–recall, inspection-budget recall, calibration, and explicit location-, drought-, and greenness-only baselines. Accuracy is not a headline metric.

A controlled negative closes remote early detection honestly; the resistance decoder continues.