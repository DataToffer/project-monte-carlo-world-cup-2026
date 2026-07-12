from __future__ import annotations

from typing import Iterable, Mapping


def _weighted_mean(rows, field: str, position: str) -> float:
    selected = [r for r in rows if r["position_group"] == position]
    total_weight = sum(float(r["minutes_weight"]) for r in selected)
    if total_weight == 0:
        return 0.0
    return sum(
        float(r[field]) * float(r["minutes_weight"]) for r in selected
    ) / total_weight


def aggregate_player_based(rows: Iterable[Mapping[str, object]]) -> dict[str, float]:
    rows = list(rows)

    attack = (
        0.65 * _weighted_mean(rows, "attack", "ATT")
        + 0.25 * _weighted_mean(rows, "attack", "MID")
        + 0.10 * _weighted_mean(rows, "attack", "DEF")
    )
    midfield = (
        0.60 * _weighted_mean(rows, "midfield", "MID")
        + 0.25 * _weighted_mean(rows, "midfield", "ATT")
        + 0.15 * _weighted_mean(rows, "midfield", "DEF")
    )
    defense = (
        0.55 * _weighted_mean(rows, "defense", "DEF")
        + 0.25 * _weighted_mean(rows, "defense", "MID")
        + 0.10 * _weighted_mean(rows, "defense", "ATT")
        + 0.10 * _weighted_mean(rows, "goalkeeper", "GK")
    )
    goalkeeper = _weighted_mean(rows, "goalkeeper", "GK")

    bench_rows = [r for r in rows if r.get("expected_role") != "starter"]
    bench_weight = sum(float(r["minutes_weight"]) for r in bench_rows)
    bench = 0.0
    if bench_weight:
        bench = sum(
            float(r.get("overall", 0)) * float(r["minutes_weight"])
            for r in bench_rows
        ) / bench_weight

    wcpi = (
        0.30 * attack
        + 0.28 * midfield
        + 0.22 * defense
        + 0.10 * goalkeeper
        + 0.10 * bench
    )
    return {
        "attack_index": attack,
        "midfield_index": midfield,
        "defense_index": defense,
        "goalkeeper_index": goalkeeper,
        "bench_index": bench,
        "WCPI": wcpi,
    }
