# Wiki Log

> Append-only. Format: `## [YYYY-MM-DD] action | subject`

## [2026-08-15] create | Wiki initialized

- Domain: CORDON / Apulian Xylella–olive crisis
- Structure: SCHEMA.md, index.md, log.md, raw/, entities/, concepts/, data/, nowcast/, briefs/, checks/
- Program contract already at CORDON.md from the prior session

## [2026-08-15] ingest | Puglia CAMP_2020_2022 (partial)

- Source: https://dati.puglia.it/ckan/dataset/dati-monitoraggio-xylella-fastidiosa
- File: raw/data/CAMP_2020_2022.csv — 40,091,648 of 81,999,815 bytes (server refuses Range)
- Encoding: cp1252, delimiter `;`, 11 columns
- 335,947 complete rows inventoried (last line truncated, dropped)
- Grain: tree/sample point with WGS84 lat/lon on every complete row
- Lecce province absent — this is the northern/buffer monitoring set, not the established south
- Full re-download started in background as CAMP_2020_2022.full.csv
- CAMP_2020_2023.csv listed in CKAN with empty URL — ACCESS_BLOCKED
- Files: data/_inventory_camp_2020_2022.json, data/_stats_partial.json, data/README.md, data/DAY1.md, concepts/puglia-monitoring.md, concepts/camp-csv.md

## [2026-08-15] ingest | Core OA paper PDFs

- KEEP raw/papers/giampetruzzi-2016-bmc-genomics.pdf
- KEEP raw/papers/zarco-tejada-2021-natcomm.pdf
- KEEP raw/papers/la-notte-2024-frontiers.pdf
- KEEP raw/papers/surano-2022-frontiers.pdf
- KEEP raw/papers/pavan-2021-frontiers.pdf
- KEEP raw/papers/sabri-2024-frontiers-mate2.pdf
- FAIL (Cloudflare HTML): EFSA 2016 PDF, PNAS 2020 PDF, Zarco-Tejada 2018 Nature Plants, PMC MATE 2
- PNAS 2020 and Sabri 2024 captured as extracted markdown via Firecrawl (see raw/articles/)

## [2026-08-15] ingest | Sentinel-2 / maps probe

- Planetary Computer STAC: HTTP 200, Puglia tiles T34TBL T34TBK T33TYF, cloud <10%, Aug 2023
- emergenzaxylella.it: connection reset — ACCESS_BLOCKED
- Copernicus CDSE catalogue probe not completed (URL quoting); catalog exists and is free with account

## [2026-08-15] update | Full CAMP file verified

- raw/data/CAMP_2020_2022.csv now 81,999,815 bytes, sha256 124ebb627433a14735f158adfe2b9adb6abdfc124645e61f064ab3ebd0ff39f9
- 688,631 complete rows, 20 Jan 2020 – 30 Jun 2023
- 605,617 joinable olives, 5,195 positives
- Positives by year: 2020 1976 / 2021 2861 / 2022 235 / 2023 123 — hold-out is starved
- Lecce still absent; Brindisi holds 4,018 of 5,195 olive positives
- Inventories refreshed; Day-1 gate still PASS


## [2026-08-15] ingest | Owen-fetched PDFs

- raw/papers/zarco-tejada-2018-natureplants.pdf
- raw/papers/efsa-2016-treatments.pdf

## [2026-08-15] update | One-scene Sentinel join

- Scene S2A_34TBL_20210812_0_L2A via Earth Search public COGs
- 50/50 usable olives, summer 2021, SCL-valid
- NDMI moves (Cliff δ −0.312, p=0.008). NDVI does not. NDRE direction only.
- nowcast/SCENE_JOIN.md, nowcast/join_one_scene.py, nowcast/cache/scene_join_100.csv
- emergenzaxylella remains SSO-gated; not required for the join


- entities: xylella-fastidiosa, philaenus-spumarius, leccino, cnr-ipsp
- concepts: oqds, resistance-not-immunity, previsual-detection, front-nowcast, resistance-decoder, puglia-monitoring, camp-csv
