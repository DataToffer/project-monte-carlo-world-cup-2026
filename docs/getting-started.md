# Getting Started

## Instalación

```bash
python -m pip install -e .
```

## Partido individual

```python
from pmcw import MatchConfig, MatchSimulation

config = MatchConfig(
    home_team="Spain",
    away_team="Austria",
    lambda_home=1.510199562,
    lambda_away=0.896117482,
)

result = MatchSimulation(config).run().summary()
```

## Línea de comandos

```bash
pmcw match       --home Spain       --away Austria       --lambda-home 1.510199562       --lambda-away 0.896117482
```
