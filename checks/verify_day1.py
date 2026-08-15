#!/usr/bin/env python3
"""Day-1 joinability gate. Fails if we cannot point to 100 olive rows with lat/lon + PCR."""
from pathlib import Path
import json, sys
stats = Path(__file__).resolve().parents[1] / "data" / "_stats_partial.json"
if not stats.exists():
    print("FAIL missing", stats)
    sys.exit(1)
d = json.loads(stats.read_text())
n = int(d.get("olive_joinable") or 0)
print(f"olive_joinable={n}")
if n < 100:
    print("FAIL need >=100 joinable olive rows")
    sys.exit(1)
if not d.get("crs_inferred"):
    print("FAIL no CRS inference recorded")
    sys.exit(1)
print("PASS")
