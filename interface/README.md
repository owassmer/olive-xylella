# CORDON Front — research interface

Primary surface: **Explore**. The map is the argument. The campaign slider is the plot.

Not a dashboard. Not a nowcast. It shows what the official clipboard counted, where, and which of those trees were still green to the inspector.

## What is on it

| Layer | Meaning |
|---|---|
| Rust discs | Olive PCR-positives, sized by count in that comune this campaign |
| Pale discs | Official tests (the footprint of the clipboard) |
| Gold ring | Olive PCR+ and marked symptom-absent — the F7 set |
| Violet | Non-olive positives (2024–25 multiplex / ST1) |
| + / − ticks | Our 100 Brindisi trees from the Aug 2021 satellite test |

Time unit is the **official campaign workbook**, not a calendar year. Overlapping books are not de-duplicated across campaigns; each frame is “what this season counted.”

## What is not on it

A predicted infection surface. Bari email status. Gene lists as map pins. Lecce after 2018 (they stopped testing it).

## How to open

Open `index.html` in a browser. Data is in `data/cordon_data.js` (works as a local file; no server).

Regenerate display JSON after new CAMP files:

```
/usr/bin/python3 interface/build_display_data.py
```

Then rebuild `data/cordon_data.js` from those JSON files (the builder should emit it).
