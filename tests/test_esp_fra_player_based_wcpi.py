from src.esp_fra.build_player_indices import expected_goals, official_inputs
from src.esp_fra.simulate_match import simulate


def test_wcpi_and_lambdas():
    teams = official_inputs()
    assert round(teams["ESP"].wcpi, 2) == 84.42
    assert round(teams["FRA"].wcpi, 2) == 84.05
    assert round(expected_goals(teams["ESP"], teams["FRA"]), 4) == 1.2224
    assert round(expected_goals(teams["FRA"], teams["ESP"]), 4) == 1.1986


def test_probabilities_sum_to_one():
    result = simulate()
    assert abs(result["spain_win_90"] + result["draw_90"] + result["france_win_90"] - 1.0) < 1e-12
    assert abs(result["spain_advances"] + result["france_advances"] - 1.0) < 1e-12
