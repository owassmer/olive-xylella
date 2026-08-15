#!/usr/bin/env python3
"""Fail closed when Experiment 1 outputs outrun the frozen study contract.

This check has no third-party dependencies. It validates the tracked contract and
result ledger, then requires a sidecar manifest for new F7/longitudinal result
CSVs when they exist locally under the gitignored nowcast/cache directory.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOWCAST = ROOT / "nowcast"
CACHE = NOWCAST / "cache"
CONTRACT = NOWCAST / "EXPERIMENT1.md"
EVAL = NOWCAST / "EVAL.md"

REQUIRED_CONTRACT_PHRASES = (
    "# Experiment 1 — frozen validity contract",
    "## 1. Claim ladder",
    "## 3. Tree identity, repeated records, and index dates",
    "### 3.3 Control pseudo-index date",
    "## 5. Matching contract",
    "Do not match on same-date tree-level NDMI",
    "## 6. Relative-time imagery",
    "strictly before the case index date",
    "## 8. F7: the first controlled table",
    "positive 20 m pixel clusters",
    "## 10. Negative controls and falsifiers",
    "## 11. Verdicts",
)

REQUIRED_EVAL_PHRASES = (
    "# Experiment 1 evaluation ledger",
    "Status:** EMPTY PREREGISTERED TEMPLATE",
    "## 1. Cohort flow",
    "## 2. Matching audit",
    "## 3. Scene and missingness audit",
    "## 4. F7 fixed-scene audit",
    "## 5. Relative-time index results",
    "## 6. Negative controls and placebo results",
    "## 7. Out-of-area model evaluation",
    "## 8. Claim ledger",
)

REQUIRED_MANIFEST_KEYS = {
    "git_commit",
    "contract_sha256",
    "source_files",
    "field_mapping",
    "filters",
    "tree_identity",
    "matching",
    "scene_selection",
    "band_grids",
    "random_seed",
    "software",
    "outputs",
}

PROTECTED_PREFIXES = ("f7_", "experiment1_", "longitudinal_")


def fail(message: str) -> None:
    print(f"FAIL {message}")
    raise SystemExit(1)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_text(path: Path, phrases: tuple[str, ...]) -> None:
    if not path.exists():
        fail(f"missing {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    missing = [phrase for phrase in phrases if phrase not in text]
    if missing:
        fail(f"{path.relative_to(ROOT)} missing contract markers: {missing}")


def validate_manifest(result_path: Path) -> None:
    manifest_path = result_path.with_suffix(".manifest.json")
    if not manifest_path.exists():
        fail(
            f"{result_path.relative_to(ROOT)} exists without "
            f"{manifest_path.name}"
        )

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid manifest {manifest_path.relative_to(ROOT)}: {exc}")

    missing = sorted(REQUIRED_MANIFEST_KEYS - set(manifest))
    if missing:
        fail(f"{manifest_path.relative_to(ROOT)} missing keys: {missing}")

    expected_contract = sha256(CONTRACT)
    if manifest.get("contract_sha256") != expected_contract:
        fail(
            f"{manifest_path.relative_to(ROOT)} contract_sha256 does not match "
            "the current nowcast/EXPERIMENT1.md"
        )

    outputs = manifest.get("outputs")
    if not isinstance(outputs, list) or result_path.name not in {
        Path(str(item)).name for item in outputs
    }:
        fail(
            f"{manifest_path.relative_to(ROOT)} outputs does not name "
            f"{result_path.name}"
        )


def main() -> int:
    require_text(CONTRACT, REQUIRED_CONTRACT_PHRASES)
    require_text(EVAL, REQUIRED_EVAL_PHRASES)

    checked = 0
    if CACHE.exists():
        for path in sorted(CACHE.glob("*.csv")):
            if path.name == "scene_join_100.csv":
                # Historical pilot predates this contract; its limitations remain
                # documented in SCENE_JOIN.md.
                continue
            if path.name.startswith(PROTECTED_PREFIXES):
                validate_manifest(path)
                checked += 1

    print(
        "PASS experiment contract present; "
        f"contract_sha256={sha256(CONTRACT)}; protected_outputs_checked={checked}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
