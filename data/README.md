# data/ — inventories and derived tables

Raw downloads live in `../raw/data/` and are gitignored.
This directory holds **inventories, licenses, and derived summaries** — the evidence spine.

## License / terms

| Source | What | License / terms | Local path |
|---|---|---|---|
| Regione Puglia CKAN, Sezione Osservatorio Fitosanitario | CAMP monitoring CSV 2020–2022 | Italian open data / CKAN dataset `dati-monitoraggio-xylella-fastidiosa`. Reuse: cite Regione Puglia – Osservatorio Fitosanitario. | `raw/data/CAMP_2020_2022.csv` (partial on 2026-08-15) |
| Same package | CAMP_2020_2023.csv | Listed, **URL empty**. Cannot download. | — |
| emergenzaxylella.it | Official maps | Site connection-reset from this host 2026-08-15 | — |
| Copernicus Sentinel-2 L2A | 10 m imagery | Free and open Copernicus license via CDSE or Planetary Computer | not yet downloaded |
| Microsoft Planetary Computer | STAC catalog of S2 | Free catalog search proven; signed asset URLs for pixels | catalog only |

## Files here

- `README.md` — this file
- `DAY1.md` — Day-1 gate report
- `_inventory_camp_2020_2022.json` — column inventory
- `_stats_partial.json` — class balance, spatial extent, olive joinability

## CRS (inferred, then checked)

Italian decimal-comma WGS84 geographic coordinates (`LATITUDINE`, `LONGITUDINE`).
Treat as **EPSG:4326**. Not a projected CRS. Convert comma → dot before any GIS join.

## Honesty

The on-disk CAMP file on 2026-08-15 is **partial** (~40 / 82 MB). Stats below that size describe 2020-01-20 through 2021-09-28 only. Do not quote them as the full 2020–2022 campaign.
