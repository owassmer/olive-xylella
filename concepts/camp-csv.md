---
title: CAMP_2020_2022.csv
created: 2026-08-15
updated: 2026-08-15
type: concept
tags: [dataset]
sources: [data/_inventory_camp_2020_2022.json, data/_stats_partial.json]
confidence: high
contested: false
---

# CAMP_2020_2022.csv

Official sample-level diagnostic table. Encoding cp1252, delimiter `;`.

## Columns

`ID` · `DATA_RILEVAMENTO` · `TIPOLOGIA` · `SPECIE` · `CULTIVAR` · `LATITUDINE` · `LONGITUDINE` · `COMUNE` · `RISULTATO` · `SINTOMO` · `PROVINCIA`

CRS: WGS84 geographic, Italian comma decimals. Empty cultivar ~10.5%. Symptom labels mixed case (`Assente`/`ASSENTE`).

## Partial-file facts (do not quote as full campaign)

335,947 complete rows · 304,541 joinable olives · 2,938 olive positives (0.965%) · every complete row has coords · 20 Jan 2020 – 28 Sep 2021 · no Lecce · lat 40.39–41.44 · lon 15.70–17.78.

Full file advertised at 82 MB; we held 40 MB when these numbers were computed. Re-download in flight.

CAMP_2020_2023.csv exists in CKAN with an empty URL.

## Related

[[puglia-monitoring]] · [[front-nowcast]] · [[previsual-detection]]
