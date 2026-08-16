# Producer value strategy

Objective: reduce the economic loss from *Xylella fastidiosa*. The €B projections aggregate farm-level losses. The accessible customer is the producer. This directory holds the producer-facing route.

## Customer

Any public or private producer of olive (and adjacent estate) products in or near the demarcated zones: olive estates, frantoi (mills), cooperatives, DOP consortia, masserie/agritourism estates, wine estates, nurseries. Exemplar: Cantine Amalberga (Vallegna Società Agricola S.r.l.), Contrada Vallegna, SP17 km 6, Ostuni — wine + hospitality estate in the comune that recorded the most olive positives of the 2021 campaign.

Market structure, existing suppliers, and willingness-to-pay are under adversarial review (`queries/telos-review-S7-producer-market.md`). Claim honesty and data licensing are under review (S8). Playbook content is under review (S9).

## The gap the first computation exposed

`front_exposure.py` on the Amalberga coordinates shows the pattern that defines the product:

1. **Approach phase (2013–2021):** the official front closed from 57 km to 0.33 km. Ring positivity within 3 km went 0 → 16 → 55 → 224 → 318 → 1,250. A producer with this information stream in 2017 had four years of warning.
2. **Abandonment phase (2022–):** zero official olive tests within 10 km of the estate in the 2022, 2023, 2024, and 2025 campaigns. Surveillance moved north with the containment front. Producers inside the passed zone lost their only official information flow at exactly the moment they face replant, graft, remove, and diversify decisions.

Both phases are product surface: pre-front producers need exposure tracking; post-front producers need decision support and restored monitoring.

## Product hypotheses

| # | Product | Buyer phase | Data basis | Status |
|---|---|---|---|---|
| P1 | Parcel Exposure & Action Report — front distance/velocity, ring positivity and testing-intensity history, conversion pressure, zone obligations, subsidy options | pre-front and post-front | official workbooks (on disk), EU/regional rules | demo built (`amalberga-profile.md`) |
| P2 | Block decline monitor — multi-date Sentinel-2 incidence at block scale (Hornero-validated formulation), alerts for sampling/agronomy; restores a monitoring feed where official testing stopped | post-front | S2 pipelines on disk + crown masks | pipeline exists; product framing pending S8 |
| P3 | Producer Xylella Playbook 2026 — obligations by zone, subsidy navigation, cultivar decisions, realistic treatment expectations, cited | all | S1/S2/S4/S9 verified facts | pending S9 |
| P4 | Vineyard PD watch note — ST1 status and what a wine estate should monitor | wine estates | S4 review + 2024–25 subspecies records | pending synthesis |

## Red lines

- No tree-level previsual detection claims from Sentinel-2. This repo's four pre-registered nulls (A0/A1/A2/A7) forbid it. Block-scale incidence only.
- Every ring statistic ships with testing-intensity context: zero positives with zero tests is silence, not health.
- Survivorship: positives are felled; coordinate silence after a positive is not recovery.
- Front velocity numbers carry the survey-design caveat until the design-adjusted estimate (S1 action D1) exists.
- Data licenses per S8 verdict before anything is sold.

## Validation path

1. Demo profile for the exemplar estate (done).
2. S7/S8/S9 verdicts harvested; synthesis picks the lead product.
3. Three pilot conversations through named channels (consortium, coop, DOP body) with the demo in hand.
