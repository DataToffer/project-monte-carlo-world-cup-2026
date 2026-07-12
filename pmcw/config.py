from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class MatchConfig:
    home_team: str
    away_team: str
    lambda_home: float
    lambda_away: float
    n_simulations: int = 100_000
    seed: int = 20260702


@dataclass(frozen=True)
class GroupConfig:
    n_simulations: int = 100_000
    seed: int = 20260702
    base_goals: float = 1.25
    attack_defense_coef: float = 0.025
    midfield_coef: float = 0.012
    wcpi_coef: float = 0.010
    goalkeeper_coef: float = 0.010
    min_lambda: float = 0.25


@dataclass(frozen=True)
class AccessoryEventConfig:
    n_simulations: int = 100_000
    seed: int = 20260702
    lambda_por_90: float = 1.36
    lambda_cro_90: float = 1.02
    extra_time_scale: float = 30 / 90
    fatigue_factor: float = 0.85
    portugal_shootout_win_if_normal: float = 0.547
    portugal_shootout_win_if_ronaldo_miss: float = 0.28
    ronaldo_goal_share: float = 0.30
    ronaldo_on_pitch_after_120: float = 0.60
    ronaldo_shootout_taker_probability: float = 0.95
    ronaldo_shootout_conversion: float = 0.76
