from __future__ import annotations

from collections import Counter
from dataclasses import asdict
import numpy as np

from .config import MatchConfig


class MatchSimulation:
    def __init__(self, config: MatchConfig):
        self.config = config
        self._result = None

    def run(self) -> "MatchSimulation":
        rng = np.random.default_rng(self.config.seed)
        home = rng.poisson(self.config.lambda_home, self.config.n_simulations)
        away = rng.poisson(self.config.lambda_away, self.config.n_simulations)

        scorelines = Counter(zip(home.tolist(), away.tolist()))
        top_scorelines = [
            {
                "scoreline": f"{h}-{a}",
                "probability": count / self.config.n_simulations,
            }
            for (h, a), count in scorelines.most_common(10)
        ]

        self._result = {
            "config": asdict(self.config),
            "home_win": float(np.mean(home > away)),
            "draw": float(np.mean(home == away)),
            "away_win": float(np.mean(home < away)),
            "home_goals_mean": float(np.mean(home)),
            "away_goals_mean": float(np.mean(away)),
            "over_2_5": float(np.mean((home + away) > 2)),
            "both_teams_score": float(np.mean((home > 0) & (away > 0))),
            "top_scorelines": top_scorelines,
        }
        return self

    def summary(self) -> dict:
        if self._result is None:
            raise RuntimeError("Run the simulation before requesting a summary.")
        return self._result
