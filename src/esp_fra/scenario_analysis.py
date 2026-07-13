from __future__ import annotations
import csv
from pathlib import Path

RESULTS_PATH = Path("data/simulations/esp_fra_scenarios_player_based_wcpi.csv")

def load_official_scenarios(path: Path = RESULTS_PATH):
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))

if __name__ == "__main__":
    for row in load_official_scenarios():
        print(
            row["scenario"],
            f"España {float(row['spain_advance']) * 100:.2f}%",
            f"Δ {float(row['delta_spain_pp']):+.2f} pp",
        )
