#!/usr/bin/env python3
"""Display aggregates keyed by official campaign, not calendar year."""
from __future__ import annotations

import csv
import json
from pathlib import Path

import pandas as pd

SRC = Path("/Users/owenwassmer/Desktop/Connor/olive-xylella/raw/data/camp_xlsx")
OUT = Path("/Users/owenwassmer/Desktop/Connor/olive-xylella/interface/data")

CAMPAIGNS = [
    ("2013–14", "CAMP_2013_2014.xlsx"),
    ("2014–15", "CAMP_2014_2015.xlsx"),
    ("2016–17", "CAMP_2016_2017.xlsx"),
    ("2017–18", "CAMP_2017_2018.xlsx"),
    ("2018–19", "CAMP_2018_2019.xlsx"),
    ("2019–20", "CAMP_2019_2020.xlsx"),
    ("2020", "CAMP_2020.xlsx"),
    ("2021", "CAMP_2021.xlsx"),
    ("2022", "CAMP_2022.xlsx"),
    ("2023", "CAMP_2023.xlsx"),
    ("2024", "CAMP_2024.xlsx"),
    ("2025", "CAMP_2025.xlsx"),
]


def to_float(s):
    if pd.isna(s):
        return None
    if isinstance(s, (int, float)):
        return float(s)
    try:
        return float(str(s).strip().replace(",", "."))
    except ValueError:
        return None


def is_olive(s):
    t = str(s).lower()
    return "olea" in t or "olivo" in t


def is_pos(s):
    return str(s).strip().lower().startswith("pos")


def sint_abs(s):
    return str(s).strip().lower().startswith("ass")


def sub_norm(s):
    if pd.isna(s):
        return None
    t = str(s).strip().upper()
    if t in {"", "NAN", "NONE", "NAT"}:
        return None
    if "PAUC" in t:
        return "pauca"
    if "FASTID" in t:
        return "fastidiosa"
    if "MULTIP" in t:
        return "multiplex"
    return t.lower()


def load(name):
    df = pd.read_excel(SRC / name, sheet_name=0)
    cols = {c.upper(): c for c in df.columns}
    date_c = next((cols[k] for k in ("DATA_RILEVAMENTO", "DATA_PRELIVEO", "DATA_CAMPIONE") if k in cols), None)
    lat_c, lon_c = cols.get("LATITUDINE"), cols.get("LONGITUDINE")
    dates = pd.to_datetime(df[date_c], errors="coerce") if date_c else pd.NaT
    out = pd.DataFrame({
        "comune": df[cols["COMUNE"]].astype(str).str.strip().str.title() if "COMUNE" in cols else "",
        "lat": df[lat_c].map(to_float) if lat_c else None,
        "lon": df[lon_c].map(to_float) if lon_c else None,
        "olive": df[cols["SPECIE"]].map(is_olive) if "SPECIE" in cols else False,
        "pos": df[cols["RISULTATO"]].map(is_pos) if "RISULTATO" in cols else False,
        "assente": df[cols["SINTOMO"]].map(sint_abs) if "SINTOMO" in cols else False,
        "sub": df[cols["SUBSPECIE"]].map(sub_norm) if "SUBSPECIE" in cols else None,
    })
    out["date"] = dates
    return out.dropna(subset=["lat", "lon"])


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    comune_rows = []
    campaigns = []
    for label, name in CAMPAIGNS:
        print("load", label, flush=True)
        f = load(name)
        f["olive_pos"] = f["olive"] & f["pos"]
        f["olive_pos_assente"] = f["olive_pos"] & f["assente"]
        f["other_pos"] = f["pos"] & ~f["olive"]
        f["pauca_pos"] = f["pos"] & (f["sub"] == "pauca")
        f["fast_pos"] = f["pos"] & (f["sub"] == "fastidiosa")
        f["mult_pos"] = f["pos"] & (f["sub"] == "multiplex")
        dates = f["date"].dropna()
        g = f.groupby("comune", dropna=False).agg(
            n=("pos", "size"),
            n_olive=("olive", "sum"),
            n_olive_pos=("olive_pos", "sum"),
            n_olive_pos_assente=("olive_pos_assente", "sum"),
            n_other_pos=("other_pos", "sum"),
            n_pauca_pos=("pauca_pos", "sum"),
            n_fast_pos=("fast_pos", "sum"),
            n_mult_pos=("mult_pos", "sum"),
            lat=("lat", "mean"),
            lon=("lon", "mean"),
        ).reset_index()
        g = g[g["comune"].str.len() > 1]
        g = g[~g["comune"].str.lower().isin(["nan", "none", "#n/d"])]
        for c in ["n", "n_olive", "n_olive_pos", "n_olive_pos_assente", "n_other_pos", "n_pauca_pos", "n_fast_pos", "n_mult_pos"]:
            g[c] = g[c].astype(int)
        g["campaign"] = label
        comune_rows.extend(g.to_dict(orient="records"))
        top = (
            g.sort_values("n_olive_pos", ascending=False)
            .head(3)["comune"].tolist()
        )
        campaigns.append({
            "id": label,
            "file": name,
            "date_min": None if dates.empty else str(dates.min().date()),
            "date_max": None if dates.empty else str(dates.max().date()),
            "n": int(len(f)),
            "n_olive": int(f["olive"].sum()),
            "n_olive_pos": int(f["olive_pos"].sum()),
            "n_olive_pos_assente": int(f["olive_pos_assente"].sum()),
            "n_other_pos": int(f["other_pos"].sum()),
            "n_pauca_pos": int(f["pauca_pos"].sum()),
            "n_fast_pos": int(f["fast_pos"].sum()),
            "n_mult_pos": int(f["mult_pos"].sum()),
            "n_comuni": int(g["comune"].nunique()),
            "n_comuni_with_olive_pos": int((g["n_olive_pos"] > 0).sum()),
            "top": top,
        })
        print(" ", label, "olive+", campaigns[-1]["n_olive_pos"], "top", top)

    ndmi = []
    p = Path("/Users/owenwassmer/Desktop/Connor/olive-xylella/nowcast/cache/scene_join_100.csv")
    if p.exists():
        with p.open() as fh:
            for row in csv.DictReader(fh):
                ndmi.append({
                    "id": row["id"],
                    "lat": float(row["lat"]),
                    "lon": float(row["lon"]),
                    "pos": row["risultato"].lower().startswith("pos"),
                    "ndvi": float(row["ndvi"]) if row.get("ndvi") else None,
                    "ndmi": float(row["ndmi"]) if row.get("ndmi") else None,
                    "comune": row.get("comune") or "",
                })

    (OUT / "comune_campaign.json").write_text(json.dumps(comune_rows, ensure_ascii=False))
    (OUT / "campaigns.json").write_text(json.dumps(campaigns, indent=2, ensure_ascii=False))
    (OUT / "ndmi100.json").write_text(json.dumps(ndmi))
    (OUT / "meta.json").write_text(json.dumps({
        "unit": "official monitoring campaign (one workbook = one frame)",
        "n_comune_campaign": len(comune_rows),
        "campaigns": [c["id"] for c in campaigns],
        "missing": ["2015–16 dedicated workbook"],
    }, indent=2))
    (OUT / "cordon_data.js").write_text(
        "window.CORDON=" + json.dumps({"campaigns": campaigns, "rows": comune_rows, "ndmi": ndmi}, ensure_ascii=False) + ";\n"
    )
    print("wrote", len(comune_rows), "comune-campaign rows")


if __name__ == "__main__":
    main()
