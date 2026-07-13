from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class SimulationConfig:
    lambda_esp: float = 1.222383
    lambda_fra: float = 1.198645
    n: int = 100_000
    seed: int = 20260712
    extra_time_factor: float = 0.85
    penalty_spain_probability: float = 0.50

def simulate(config: SimulationConfig = SimulationConfig()):
    rng = np.random.default_rng(config.seed)
    esp = rng.poisson(config.lambda_esp, config.n)
    fra = rng.poisson(config.lambda_fra, config.n)
    esp_win_90, draw_90, fra_win_90 = esp > fra, esp == fra, esp < fra
    draw_idx = np.flatnonzero(draw_90)
    esp_et = np.zeros(config.n, dtype=int)
    fra_et = np.zeros(config.n, dtype=int)
    esp_et[draw_idx] = rng.poisson(config.lambda_esp * (30 / 90) * config.extra_time_factor, len(draw_idx))
    fra_et[draw_idx] = rng.poisson(config.lambda_fra * (30 / 90) * config.extra_time_factor, len(draw_idx))
    esp_win_et = draw_90 & (esp_et > fra_et)
    fra_win_et = draw_90 & (fra_et > esp_et)
    penalties = draw_90 & (esp_et == fra_et)
    pen_idx = np.flatnonzero(penalties)
    esp_win_pens = np.zeros(config.n, dtype=bool)
    esp_win_pens[pen_idx] = rng.random(len(pen_idx)) < config.penalty_spain_probability
    esp_advances = esp_win_90 | esp_win_et | esp_win_pens
    p = lambda m: float(m.mean())
    return {
        "spain_win_90": p(esp_win_90),
        "draw_90": p(draw_90),
        "france_win_90": p(fra_win_90),
        "over_2_5": p((esp + fra) > 2),
        "both_teams_score": p((esp > 0) & (fra > 0)),
        "spain_win_extra_time": p(esp_win_et),
        "france_win_extra_time": p(fra_win_et),
        "goes_to_penalties": p(penalties),
        "spain_win_penalties": p(esp_win_pens),
        "spain_advances": p(esp_advances),
        "france_advances": 1.0 - p(esp_advances),
    }

if __name__ == "__main__":
    for key, value in simulate().items():
        print(f"{key}: {value:.5f}")
