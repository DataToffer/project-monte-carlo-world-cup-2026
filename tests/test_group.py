from pmcw import GroupConfig, GroupSimulation


def test_group_top2_consistency():
    teams = [
        {"team_id": "A", "team_name": "A", "WCPI": 90, "attack_index": 90, "midfield_index": 90, "defense_index": 90, "goalkeeper_index": 90},
        {"team_id": "B", "team_name": "B", "WCPI": 80, "attack_index": 80, "midfield_index": 80, "defense_index": 80, "goalkeeper_index": 80},
        {"team_id": "C", "team_name": "C", "WCPI": 70, "attack_index": 70, "midfield_index": 70, "defense_index": 70, "goalkeeper_index": 70},
        {"team_id": "D", "team_name": "D", "WCPI": 60, "attack_index": 60, "midfield_index": 60, "defense_index": 60, "goalkeeper_index": 60},
    ]
    fixtures = [
        {"home_team": "A", "away_team": "B"},
        {"home_team": "C", "away_team": "D"},
        {"home_team": "A", "away_team": "C"},
        {"home_team": "B", "away_team": "D"},
        {"home_team": "A", "away_team": "D"},
        {"home_team": "B", "away_team": "C"},
    ]
    result = GroupSimulation(
        teams,
        fixtures,
        config=GroupConfig(n_simulations=200, seed=7),
    ).run().summary()
    for team in result["probabilities"].values():
        assert abs(team["top_2"] - (team["p_1"] + team["p_2"])) < 1e-12
