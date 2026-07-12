from pmcw import MatchConfig, MatchSimulation


def test_match_probabilities_sum_to_one():
    config = MatchConfig(
        home_team="Spain",
        away_team="Austria",
        lambda_home=1.5101995620259079,
        lambda_away=0.8961174820133812,
        n_simulations=10_000,
        seed=20260702,
    )
    result = MatchSimulation(config).run().summary()
    total = result["home_win"] + result["draw"] + result["away_win"]
    assert abs(total - 1.0) < 1e-12


def test_match_is_deterministic_with_fixed_seed():
    config = MatchConfig(
        home_team="Spain",
        away_team="Austria",
        lambda_home=1.51,
        lambda_away=0.90,
        n_simulations=5_000,
        seed=42,
    )
    a = MatchSimulation(config).run().summary()
    b = MatchSimulation(config).run().summary()
    assert a == b
