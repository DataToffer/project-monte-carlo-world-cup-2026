from pmcw import MatchConfig, MatchSimulation

config = MatchConfig(
    home_team="Spain",
    away_team="Austria",
    lambda_home=1.5101995620259079,
    lambda_away=0.8961174820133812,
    n_simulations=100_000,
    seed=20260702,
)

result = MatchSimulation(config).run().summary()
print(result)
