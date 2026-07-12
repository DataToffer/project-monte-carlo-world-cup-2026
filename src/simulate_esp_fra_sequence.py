"""
PMCW Match Analysis #003
España vs Francia - 90 minutos, prórroga condicionada y penaltis condicionados.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class Config:
    n_simulations: int = 100_000
    seed: int = 20260712
    lambda_esp_90: float = 1.1336
    lambda_fra_90: float = 1.0889
    fatigue_factor: float = 0.85
    shootout_spain_base: float = 0.495

STATE_MULTIPLIERS = {
    "NEUTRAL_0_0": (1.00, 1.00, 0.000),
    "ESP_COMEBACK": (1.10, 1.04, 0.025),
    "ESP_LATE_COMEBACK": (1.14, 1.05, 0.040),
    "FRA_COMEBACK": (1.04, 1.10, -0.025),
    "FRA_LATE_COMEBACK": (1.05, 1.14, -0.040),
}

def run_simulation(config: Config = Config()) -> dict:
    rng = np.random.default_rng(config.seed)
    n = config.n_simulations
    esp_90 = rng.poisson(config.lambda_esp_90, n)
    fra_90 = rng.poisson(config.lambda_fra_90, n)

    esp_win_90 = esp_90 > fra_90
    fra_win_90 = fra_90 > esp_90
    draw_90 = esp_90 == fra_90

    states = np.full(n, "NO_ET", dtype=object)
    for i in np.where(draw_90)[0]:
        goals = int(esp_90[i])
        if goals == 0:
            states[i] = "NEUTRAL_0_0"
            continue
        events = [(t, "ESP") for t in rng.uniform(0, 90, goals)]
        events += [(t, "FRA") for t in rng.uniform(0, 90, goals)]
        events.sort()
        minute, equaliser = events[-1]
        if equaliser == "ESP":
            states[i] = "ESP_LATE_COMEBACK" if minute >= 80 else "ESP_COMEBACK"
        else:
            states[i] = "FRA_LATE_COMEBACK" if minute >= 80 else "FRA_COMEBACK"

    base_esp_et = config.lambda_esp_90 * (30 / 90) * config.fatigue_factor
    base_fra_et = config.lambda_fra_90 * (30 / 90) * config.fatigue_factor
    esp_et = np.zeros(n, dtype=int)
    fra_et = np.zeros(n, dtype=int)

    for state, (esp_mult, fra_mult, _) in STATE_MULTIPLIERS.items():
        idx = np.where(states == state)[0]
        esp_et[idx] = rng.poisson(base_esp_et * esp_mult, len(idx))
        fra_et[idx] = rng.poisson(base_fra_et * fra_mult, len(idx))

    esp_win_et = draw_90 & (esp_et > fra_et)
    fra_win_et = draw_90 & (fra_et > esp_et)
    penalties = draw_90 & (esp_et == fra_et)

    p_esp_shootout = np.full(n, np.nan)
    p_esp_shootout[penalties] = config.shootout_spain_base
    for state, (_, _, adjustment) in STATE_MULTIPLIERS.items():
        mask = penalties & (states == state)
        p_esp_shootout[mask] = np.clip(
            config.shootout_spain_base + adjustment, 0.35, 0.65
        )

    esp_win_pens = np.zeros(n, dtype=bool)
    idx = np.where(penalties)[0]
    esp_win_pens[idx] = rng.random(len(idx)) < p_esp_shootout[idx]

    esp_advances = esp_win_90 | esp_win_et | esp_win_pens

    def pct(mask) -> float:
        return float(np.mean(mask) * 100)

    return {
        "España gana 90": pct(esp_win_90),
        "Empate 90": pct(draw_90),
        "Francia gana 90": pct(fra_win_90),
        "España gana prórroga": pct(esp_win_et),
        "Francia gana prórroga": pct(fra_win_et),
        "Llega a penaltis": pct(penalties),
        "España gana tanda": pct(esp_win_pens),
        "España se clasifica": pct(esp_advances),
        "Francia se clasifica": pct(~esp_advances),
    }

if __name__ == "__main__":
    for key, value in run_simulation().items():
        print(f"{key}: {value:.3f}%")
