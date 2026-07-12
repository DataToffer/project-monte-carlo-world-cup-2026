from __future__ import annotations

import numpy as np
from .config import AccessoryEventConfig


class RonaldoEventSimulation:
    def __init__(self, config: AccessoryEventConfig = AccessoryEventConfig()):
        self.config = config
        self._result = None

    def run(self) -> "RonaldoEventSimulation":
        c = self.config
        rng = np.random.default_rng(c.seed)
        n = c.n_simulations

        por_90 = rng.poisson(c.lambda_por_90, n)
        cro_90 = rng.poisson(c.lambda_cro_90, n)

        por_win_90 = por_90 > cro_90
        draw_90 = por_90 == cro_90

        l_por_et = c.lambda_por_90 * c.extra_time_scale * c.fatigue_factor
        l_cro_et = c.lambda_cro_90 * c.extra_time_scale * c.fatigue_factor

        por_et = np.zeros(n, dtype=int)
        cro_et = np.zeros(n, dtype=int)
        draw_idx = np.where(draw_90)[0]
        por_et[draw_idx] = rng.poisson(l_por_et, len(draw_idx))
        cro_et[draw_idx] = rng.poisson(l_cro_et, len(draw_idx))

        por_win_et = draw_90 & (por_et > cro_et)
        goes_to_pens = draw_90 & (por_et == cro_et)

        por_goals = por_90 + por_et
        ronaldo_goal = np.zeros(n, dtype=bool)
        mask = por_goals > 0
        p_goal = 1 - np.power(1 - c.ronaldo_goal_share, por_goals[mask])
        ronaldo_goal[mask] = rng.random(mask.sum()) < p_goal

        ronaldo_available = np.zeros(n, dtype=bool)
        pens_idx = np.where(goes_to_pens)[0]
        ronaldo_available[pens_idx] = (
            rng.random(len(pens_idx)) < c.ronaldo_on_pitch_after_120
        )

        ronaldo_takes = np.zeros(n, dtype=bool)
        avail_idx = np.where(goes_to_pens & ronaldo_available)[0]
        ronaldo_takes[avail_idx] = (
            rng.random(len(avail_idx)) < c.ronaldo_shootout_taker_probability
        )

        ronaldo_misses = np.zeros(n, dtype=bool)
        takes_idx = np.where(ronaldo_takes)[0]
        ronaldo_misses[takes_idx] = (
            rng.random(len(takes_idx)) >= c.ronaldo_shootout_conversion
        )

        por_win_pens = np.zeros(n, dtype=bool)
        for i in pens_idx:
            p_win = (
                c.portugal_shootout_win_if_ronaldo_miss
                if ronaldo_misses[i]
                else c.portugal_shootout_win_if_normal
            )
            por_win_pens[i] = rng.random() < p_win

        portugal_passes = por_win_90 | por_win_et | por_win_pens
        croatia_passes = ~portugal_passes
        ocaso = goes_to_pens & ronaldo_misses & croatia_passes

        pct = lambda x: float(np.mean(x))
        self._result = {
            "portugal_advances": pct(portugal_passes),
            "croatia_advances": pct(croatia_passes),
            "portugal_wins_90": pct(por_win_90),
            "draw_90": pct(draw_90),
            "goes_to_penalties": pct(goes_to_pens),
            "ronaldo_scores_before_shootout": pct(ronaldo_goal),
            "portugal_advances_and_ronaldo_scores": pct(
                portugal_passes & ronaldo_goal
            ),
            "ronaldo_misses_in_shootout": pct(ronaldo_misses),
            "ocaso_scenario": pct(ocaso),
        }
        return self

    def summary(self) -> dict:
        if self._result is None:
            raise RuntimeError("Run the simulation before requesting a summary.")
        return self._result
