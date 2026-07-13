from __future__ import annotations
from dataclasses import dataclass

WCPI_WEIGHTS = {"attack": 0.30, "midfield": 0.28, "defense": 0.22, "goalkeeper": 0.10, "bench": 0.10}

@dataclass(frozen=True)
class TeamIndices:
    attack: float
    midfield: float
    defense: float
    goalkeeper: float
    bench: float

    @property
    def wcpi(self) -> float:
        return sum(getattr(self, key) * weight for key, weight in WCPI_WEIGHTS.items())

def expected_goals(team: TeamIndices, opponent: TeamIndices) -> float:
    value = (1.25 + 0.025 * (team.attack - opponent.defense) + 0.012 * (team.midfield - opponent.midfield) + 0.010 * (team.wcpi - opponent.wcpi) - 0.010 * (opponent.goalkeeper - 75.0))
    return max(0.25, value)

def official_inputs():
    return {
        "ESP": TeamIndices(85.8902, 87.1296, 81.2455, 88.7670, 75.0806),
        "FRA": TeamIndices(85.9586, 84.8122, 82.2554, 90.0000, 74.2043),
    }

if __name__ == "__main__":
    teams = official_inputs()
    for code, team in teams.items():
        opponent = teams["FRA" if code == "ESP" else "ESP"]
        print(code, round(team.wcpi, 4), round(expected_goals(team, opponent), 6))
