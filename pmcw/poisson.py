from __future__ import annotations

from typing import Mapping


def expected_goals(
    team_a: Mapping[str, float],
    team_b: Mapping[str, float],
    *,
    base_goals: float = 1.25,
    attack_defense_coef: float = 0.025,
    midfield_coef: float = 0.012,
    wcpi_coef: float = 0.010,
    goalkeeper_coef: float = 0.010,
    min_lambda: float = 0.25,
) -> float:
    value = (
        base_goals
        + attack_defense_coef * (team_a["attack_index"] - team_b["defense_index"])
        + midfield_coef * (team_a["midfield_index"] - team_b["midfield_index"])
        + wcpi_coef * (team_a["WCPI"] - team_b["WCPI"])
        - goalkeeper_coef * (team_b["goalkeeper_index"] - 75)
    )
    return max(min_lambda, float(value))
