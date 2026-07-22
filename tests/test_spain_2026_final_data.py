from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
FINAL = ROOT / "data" / "final"


def _read_csv(name):
    with (FINAL / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def test_match_path_has_eight_matches():
    rows = _read_csv("spain_2026_match_path.csv")
    assert len(rows) == 8


def test_match_path_reconciles_goals():
    rows = _read_csv("spain_2026_match_path.csv")
    gf = ga = 0
    for row in rows:
        home = row["home_team"]
        hg = int(row["home_goals_et"])
        ag = int(row["away_goals_et"])
        if home == "Spain":
            gf += hg
            ga += ag
        else:
            gf += ag
            ga += hg
    assert gf == 14
    assert ga == 1


def test_team_kpis_are_consistent():
    rows = {r["metric"]: r["value"] for r in _read_csv("spain_2026_team_stats.csv")}
    assert int(rows["matches"]) == 8
    assert int(rows["goals_for"]) == 14
    assert int(rows["goals_against"]) == 1
    assert int(rows["goal_difference"]) == 13
    assert int(rows["clean_sheets"]) == 7
    assert int(rows["passes_completed"]) <= int(rows["passes_attempted"])


def test_squad_has_26_unique_numbers():
    rows = _read_csv("spain_2026_squad.csv")
    numbers = [int(r["shirt_number"]) for r in rows]
    assert len(rows) == 26
    assert sorted(numbers) == list(range(1, 27))


def test_rodri_final_completed_passes():
    rows = _read_csv("spain_2026_player_highlights.csv")
    rodri = {r["metric"]: int(r["value"]) for r in rows if r["player_name"] == "Rodri" and r["value"].isdigit()}
    assert rodri["passes_completed"] == 790


def test_no_partial_coverage_metrics_in_final_dataset():
    forbidden = {"possession_65_4", "shot_difference_11_8", "xg_conceded_0_24", "xg_difference_1_57"}
    team_metrics = {r["metric"] for r in _read_csv("spain_2026_team_stats.csv")}
    assert forbidden.isdisjoint(team_metrics)
