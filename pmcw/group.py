from __future__ import annotations

from collections import Counter, defaultdict
from typing import Iterable, Mapping
import numpy as np

from .config import GroupConfig
from .poisson import expected_goals


class GroupSimulation:
    def __init__(
        self,
        teams: Iterable[Mapping[str, object]],
        fixtures: Iterable[Mapping[str, str]],
        played_results: Iterable[Mapping[str, object]] | None = None,
        config: GroupConfig = GroupConfig(),
    ):
        self.teams = [dict(t) for t in teams]
        self.fixtures = [dict(f) for f in fixtures]
        self.played_results = [dict(r) for r in (played_results or [])]
        self.config = config
        self._result = None

    @staticmethod
    def _apply_result(table, home, away, hg, ag):
        table[home]["gf"] += hg
        table[home]["ga"] += ag
        table[away]["gf"] += ag
        table[away]["ga"] += hg
        if hg > ag:
            table[home]["pts"] += 3
        elif hg < ag:
            table[away]["pts"] += 3
        else:
            table[home]["pts"] += 1
            table[away]["pts"] += 1

    def run(self) -> "GroupSimulation":
        team_map = {t["team_id"]: t for t in self.teams}
        rng = np.random.default_rng(self.config.seed)
        position_counts = {tid: Counter() for tid in team_map}
        order_counts = Counter()

        for _ in range(self.config.n_simulations):
            table = defaultdict(lambda: {"pts": 0, "gf": 0, "ga": 0})

            for r in self.played_results:
                self._apply_result(
                    table,
                    r["home_team"],
                    r["away_team"],
                    int(r["home_goals"]),
                    int(r["away_goals"]),
                )

            for f in self.fixtures:
                home_id, away_id = f["home_team"], f["away_team"]
                home_team = team_map[home_id]
                away_team = team_map[away_id]

                kwargs = {
                    "base_goals": self.config.base_goals,
                    "attack_defense_coef": self.config.attack_defense_coef,
                    "midfield_coef": self.config.midfield_coef,
                    "wcpi_coef": self.config.wcpi_coef,
                    "goalkeeper_coef": self.config.goalkeeper_coef,
                    "min_lambda": self.config.min_lambda,
                }
                lh = expected_goals(home_team, away_team, **kwargs)
                la = expected_goals(away_team, home_team, **kwargs)
                self._apply_result(
                    table,
                    home_id,
                    away_id,
                    int(rng.poisson(lh)),
                    int(rng.poisson(la)),
                )

            ranking = sorted(
                team_map,
                key=lambda tid: (
                    table[tid]["pts"],
                    table[tid]["gf"] - table[tid]["ga"],
                    table[tid]["gf"],
                    float(team_map[tid]["WCPI"]),
                ),
                reverse=True,
            )
            order_counts[tuple(ranking)] += 1
            for pos, tid in enumerate(ranking, start=1):
                position_counts[tid][pos] += 1

        probabilities = {}
        for t in self.teams:
            tid = t["team_id"]
            probabilities[tid] = {
                f"p_{pos}": position_counts[tid][pos] / self.config.n_simulations
                for pos in range(1, len(self.teams) + 1)
            }
            probabilities[tid]["top_2"] = (
                probabilities[tid].get("p_1", 0)
                + probabilities[tid].get("p_2", 0)
            )

        self._result = {
            "probabilities": probabilities,
            "most_frequent_order": list(order_counts.most_common(1)[0][0]),
            "most_frequent_order_probability": (
                order_counts.most_common(1)[0][1] / self.config.n_simulations
            ),
        }
        return self

    def summary(self) -> dict:
        if self._result is None:
            raise RuntimeError("Run the simulation before requesting a summary.")
        return self._result
