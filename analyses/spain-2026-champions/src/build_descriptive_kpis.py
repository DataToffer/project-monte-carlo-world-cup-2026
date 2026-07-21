from __future__ import annotations

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
OUT_DIR = BASE_DIR / "outputs" / "tables"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def to_float(value: str) -> float | None:
    value = (value or "").strip()
    return float(value) if value else None


def to_int(value: str) -> int | None:
    value = (value or "").strip()
    return int(float(value)) if value else None


def per90(value: float | None, minutes: int) -> float | None:
    if value is None:
        return None
    return value * 90 / minutes


def fmt(value: float | int | None, digits: int = 2) -> str:
    if value is None:
        return ""
    if isinstance(value, int):
        return str(value)
    return f"{value:.{digits}f}"


def build() -> None:
    matches = read_csv(RAW_DIR / "matches.csv")
    stats = read_csv(RAW_DIR / "match_team_stats.csv")

    stats_by_match: dict[str, dict[str, dict[str, str]]] = {}
    for row in stats:
        stats_by_match.setdefault(row["match_id"], {})[row["team_id"]] = row

    output: list[dict[str, str]] = []
    for match in matches:
        match_id = match["match_id"]
        duration = 120 if match["extra_time"] == "1" else 90
        pair = stats_by_match.get(match_id, {})
        esp = pair.get("ESP", {})
        opp = next((row for team, row in pair.items() if team != "ESP"), {})

        esp_shots = to_float(esp.get("shots", ""))
        opp_shots = to_float(opp.get("shots", ""))
        esp_xg = to_float(esp.get("xg", ""))
        opp_xg = to_float(opp.get("xg", ""))
        possession = to_float(esp.get("possession_pct", ""))

        coverage_fields = {
            "possession": possession,
            "shots": esp_shots,
            "opponent_shots": opp_shots,
            "xg": esp_xg,
            "opponent_xg": opp_xg,
        }
        available = sum(value is not None for value in coverage_fields.values())
        coverage_pct = available / len(coverage_fields) * 100

        output.append({
            "match_id": match_id,
            "match_date": match["match_date"],
            "stage": match["stage"],
            "opponent": match["opponent"],
            "duration_minutes": str(duration),
            "goals_for": match["goals_for"],
            "goals_against": match["goals_against"],
            "goal_difference": str(int(match["goals_for"]) - int(match["goals_against"])),
            "clean_sheet": match["clean_sheet"],
            "possession_pct": fmt(possession),
            "shots": fmt(esp_shots),
            "opponent_shots": fmt(opp_shots),
            "shot_difference": fmt(esp_shots - opp_shots if esp_shots is not None and opp_shots is not None else None),
            "shots_per90": fmt(per90(esp_shots, duration)),
            "opponent_shots_per90": fmt(per90(opp_shots, duration)),
            "xg": fmt(esp_xg),
            "opponent_xg": fmt(opp_xg),
            "xg_difference": fmt(esp_xg - opp_xg if esp_xg is not None and opp_xg is not None else None),
            "xg_per90": fmt(per90(esp_xg, duration)),
            "opponent_xg_per90": fmt(per90(opp_xg, duration)),
            "goals_minus_xg": fmt(int(match["goals_for"]) - esp_xg if esp_xg is not None else None),
            "stat_coverage_pct": fmt(coverage_pct, 1),
            "quality_status": esp.get("quality_status", "missing_stats"),
        })

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / "spain_match_kpis.csv"
    with out_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=output[0].keys())
        writer.writeheader()
        writer.writerows(output)


if __name__ == "__main__":
    build()
