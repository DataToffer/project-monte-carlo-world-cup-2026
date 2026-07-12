from pmcw.poisson import expected_goals


def test_expected_goals_respects_floor():
    weak = {
        "attack_index": 1,
        "midfield_index": 1,
        "WCPI": 1,
        "goalkeeper_index": 1,
        "defense_index": 1,
    }
    strong = {
        "attack_index": 100,
        "midfield_index": 100,
        "WCPI": 100,
        "goalkeeper_index": 100,
        "defense_index": 100,
    }
    assert expected_goals(weak, strong, min_lambda=0.25) >= 0.25


def test_expected_goals_spain_austria_reference():
    spain = {
        "attack_index": 85.33233692344714,
        "midfield_index": 87.4633409799784,
        "defense_index": 81.94916193513082,
        "goalkeeper_index": 89,
        "WCPI": 84.45382069027642,
    }
    austria = {
        "attack_index": 79.15049301708075,
        "midfield_index": 80.39665521602174,
        "defense_index": 78.28098624382551,
        "goalkeeper_index": 81,
        "WCPI": 78.54226410348768,
    }
    value = expected_goals(spain, austria)
    assert round(value, 6) == round(1.5101995620259079, 6)
