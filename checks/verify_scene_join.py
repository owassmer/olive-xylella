#!/usr/bin/env python3
"""Assert the one-scene join produced 100 usable rows and a non-constant NDVI."""
from pathlib import Path
import csv
import sys

p = Path(__file__).resolve().parents[1] / "nowcast/cache/scene_join_100.csv"
if not p.exists():
    print("FAIL missing", p)
    sys.exit(1)
rows = list(csv.DictReader(p.open()))
if len(rows) != 100:
    print("FAIL n=", len(rows))
    sys.exit(1)
ndvi = [float(r["ndvi"]) for r in rows if r.get("ndvi")]
pos = sum(1 for r in rows if r["risultato"].lower().startswith("pos"))
neg = sum(1 for r in rows if r["risultato"].lower().startswith("neg"))
if pos != 50 or neg != 50:
    print("FAIL class balance", pos, neg)
    sys.exit(1)
if len(set(round(v, 6) for v in ndvi)) < 10:
    print("FAIL NDVI nearly constant")
    sys.exit(1)
print("PASS n=100 pos=50 neg=50 ndvi_unique", len(set(round(v, 6) for v in ndvi)))
sys.exit(0)
