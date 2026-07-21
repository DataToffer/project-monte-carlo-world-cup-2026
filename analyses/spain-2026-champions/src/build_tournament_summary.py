"""Build tournament-level descriptive KPIs for Spain at the 2026 World Cup.

Inputs
------
- outputs/tables/spain_match_kpis.csv
- data/raw/matches.csv

Outputs
-------
- outputs/tables/spain_tournament_summary.csv
- outputs/tableau/spain_tournament_kpis_long.csv

The script is coverage-aware: missing match-level metrics remain null and every
aggregate records how many of the eight matches contribute to the result.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
MATCH_KPIS = BASE_DIR / "outputs" / "tables" / "spain_match_kpis.csv"
MATCHES = BASE_DIR / "data" / "raw" / "matches.csv"
SUMMARY_OUT = BASE_DIR / "outputs" / "tables" / "spain_tournament_summary.csv"
TABLEAU_OUT = BASE_DIR / "outputs" / "tableau" / "spain_tournament_kpis_long.csv"


def _summary_row(
    metric_id: str,
    metric_label: str,
    category: str,
    unit: str,
    series: pd.Series,
    aggregation: str,
    interpretation: str,
) -> dict[str, object]:
    clean = pd.to_numeric(series, errors="coerce").dropna()
    coverage = int(clean.shape[0])
    total_matches = int(series.shape[0])

    values: dict[str, float | None] = {
        "value": None,
        "total": None,
        "average": None,
        "minimum": None,
        "maximum": None,
    }

    if coverage:
        values["total"] = float(clean.sum())
        values["average"] = float(clean.mean())
        values["minimum"] = float(clean.min())
        values["maximum"] = float(clean.max())
        if aggregation == "sum":
            values["value"] = values["total"]
        elif aggregation == "mean":
            values["value"] = values["average"]
        elif aggregation == "max":
            values["value"] = values["maximum"]
        elif aggregation == "min":
            values["value"] = values["minimum"]
        else:
            raise ValueError(f"Unsupported aggregation: {aggregation}")

    return {
        "metric_id": metric_id,
        "metric_label": metric_label,
        "category": category,
        "unit": unit,
        "aggregation": aggregation,
        **values,
        "coverage_matches": coverage,
        "total_matches": total_matches,
        "coverage_pct": round(coverage / total_matches * 100, 1) if total_matches else 0.0,
        "interpretation": interpretation,
    }


def build_summary() -> pd.DataFrame:
    matches = pd.read_csv(MATCHES)
    kpis = pd.read_csv(MATCH_KPIS)

    rows: list[dict[str, object]] = []

    rows.extend(
        [
            _summary_row("matches", "Partidos disputados", "Resultado", "partidos", pd.Series([1] * len(matches)), "sum", "Número total de encuentros jugados."),
            _summary_row("wins", "Victorias", "Resultado", "partidos", (matches["result_final"] == "W").astype(int), "sum", "Victorias considerando prórroga cuando corresponde."),
            _summary_row("draws_90", "Empates tras 90 minutos", "Resultado", "partidos", (matches["result_90"] == "D").astype(int), "sum", "Empates al término del tiempo reglamentario."),
            _summary_row("losses", "Derrotas", "Resultado", "partidos", (matches["result_final"] == "L").astype(int), "sum", "Derrotas finales en el torneo."),
            _summary_row("goals_for", "Goles a favor", "Resultado", "goles", matches["goals_for"], "sum", "Producción ofensiva total."),
            _summary_row("goals_against", "Goles en contra", "Resultado", "goles", matches["goals_against"], "sum", "Goles concedidos durante el torneo."),
            _summary_row("goal_difference", "Diferencia de goles", "Resultado", "goles", matches["goals_for"] - matches["goals_against"], "sum", "Balance total de goles."),
            _summary_row("clean_sheets", "Porterías a cero", "Defensa", "partidos", matches["clean_sheet"], "sum", "Partidos sin encajar gol."),
        ]
    )

    metric_specs = [
        ("possession_pct", "Posesión media", "Control", "%", "mean", "Promedio de posesión en partidos con dato disponible."),
        ("shots", "Tiros por partido", "Ataque", "tiros", "mean", "Volumen ofensivo medio por encuentro."),
        ("shots_against", "Tiros concedidos por partido", "Defensa", "tiros", "mean", "Volumen ofensivo medio permitido al rival."),
        ("shot_difference", "Diferencia media de tiros", "Ataque", "tiros", "mean", "Ventaja media en volumen de tiro."),
        ("shots_per90", "Tiros por 90 minutos", "Ataque", "tiros/90", "mean", "Volumen de tiro normalizado por duración."),
        ("xg", "xG por partido", "Ataque", "xG", "mean", "Calidad media de ocasiones generadas."),
        ("xg_against", "xG concedido por partido", "Defensa", "xG", "mean", "Calidad media de ocasiones permitidas."),
        ("xg_difference", "Diferencia media de xG", "Ataque", "xG", "mean", "Ventaja media en calidad de ocasiones."),
        ("xg_per90", "xG por 90 minutos", "Ataque", "xG/90", "mean", "xG normalizado por duración."),
        ("goals_minus_xg", "Goles menos xG", "Eficiencia", "goles", "sum", "Diferencia acumulada entre goles reales y xG en partidos con cobertura."),
        ("data_coverage_pct", "Cobertura estadística media", "Calidad", "%", "mean", "Porcentaje medio de campos estadísticos disponibles por partido."),
    ]

    for metric_id, label, category, unit, aggregation, interpretation in metric_specs:
        if metric_id in kpis.columns:
            rows.append(_summary_row(metric_id, label, category, unit, kpis[metric_id], aggregation, interpretation))

    summary = pd.DataFrame(rows)
    summary["value"] = pd.to_numeric(summary["value"], errors="coerce").round(2)
    for column in ["total", "average", "minimum", "maximum"]:
        summary[column] = pd.to_numeric(summary[column], errors="coerce").round(2)
    return summary


def main() -> None:
    summary = build_summary()
    SUMMARY_OUT.parent.mkdir(parents=True, exist_ok=True)
    TABLEAU_OUT.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(SUMMARY_OUT, index=False)

    tableau = summary[[
        "metric_id", "metric_label", "category", "unit", "value",
        "coverage_matches", "total_matches", "coverage_pct", "interpretation"
    ]].copy()
    tableau.to_csv(TABLEAU_OUT, index=False)


if __name__ == "__main__":
    main()
