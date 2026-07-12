# PMCW Match Analysis #003
## España vs Francia, semifinal del Mundial 2026

Modelo reproducible de tres capas:

1. Resultado en 90 minutos mediante Poisson.
2. Prórroga condicionada por la secuencia del empate.
3. Tanda condicionada por el estado de llegada.

## Resultados principales

| Evento | Probabilidad |
|---|---:|
| España gana en 90' | 36,481% |
| Empate en 90' | 28,889% |
| Francia gana en 90' | 34,630% |
| España se clasifica | 51,092% |
| Francia se clasifica | 48,908% |
| Llega a penaltis | 16,551% |

## Estados de llegada a la prórroga

- `NEUTRAL_0_0`
- `ESP_COMEBACK`
- `ESP_LATE_COMEBACK`
- `FRA_COMEBACK`
- `FRA_LATE_COMEBACK`

El equipo que empata recibe un ajuste de momentum. El rival conserva un pequeño ajuste de transición, ya que el equipo remontador tiende a jugar más arriba. Los parámetros son hipótesis modelizadas y se documentan en `config/esp_fra_match_config.json`.

## Eventos accesorios

Los eventos meteorológicos y satíricos se mantienen fuera del motor futbolístico:

- tormenta eléctrica exterior: proxy modelizado;
- interrupción por rayos: proxy condicionado por cubierta;
- evento Trump-Infantino-Lamine: evento satírico de probabilidad residual;
- mención de "final anticipada": evento editorial.

## Reproducción

```bash
python src/simulate_esp_fra_sequence.py
```

## Trazabilidad

- 100.000 simulaciones.
- Seed: `20260712`.
- Inputs `player_based_v1_model_estimate`.
- Modelo: `PMCW v1.1 - player_based_v1 + sequence_state_v1`.
- Partido: España vs Francia, semifinal, 14 de julio de 2026, AT&T Stadium, Arlington.
- Los ratings, ajustes de momentum y eventos accesorios son estimaciones del modelo, no probabilidades oficiales.
