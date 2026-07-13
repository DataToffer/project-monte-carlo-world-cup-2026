# España vs Francia, semifinal del Mundial 2026

## Project Monte Carlo World Cup 2026

**Versión oficial del análisis:** `player_based_wcpi_v1`  
**Fecha de corte:** 12 de julio de 2026  
**Simulaciones:** 100.000  
**Seed principal:** 20260712  

Este directorio contiene la versión vigente y reproducible del análisis España-Francia. Sustituye las pruebas híbridas, secuenciales y de calibración descartadas durante el desarrollo.

## Resultado consolidado

| Métrica | Resultado |
|---|---:|
| España gana en 90 minutos | 36,78% |
| Empate | 27,36% |
| Francia gana en 90 minutos | 35,86% |
| España se clasifica | 50,42% |
| Francia se clasifica | 49,58% |
| Llega a penaltis | 15,34% |
| Marcador modal | 1-1, 13,07% |

## Arquitectura

```text
32 jugadores
→ ratings por dimensión
→ minutos esperados
→ índices posicionales
→ WCPI
→ lambdas
→ Poisson
→ 100.000 simulaciones
→ prórroga y penaltis
→ sensibilidad de escenarios
```

## Índices de selección

| Índice | España | Francia |
|---|---:|---:|
| Ataque | 85,89 | 85,96 |
| Centro del campo | 87,13 | 84,81 |
| Defensa | 81,25 | 82,26 |
| Portería | 88,77 | 90,00 |
| Banquillo | 75,08 | 74,20 |
| WCPI | 84,42 | 84,05 |

## Lambdas

- España: `1.222383`
- Francia: `1.198645`

## Escenarios modelados

| Escenario | Impacto en la clasificación de España |
|---|---:|
| Nico Williams con 60-70 minutos | +0,14 pp |
| Mikel Merino desde el banquillo | +0,05 pp |
| Mbappé limitado físicamente | +0,37 pp |
| Nico + Merino + Mbappé limitado | +0,44 pp |

Rodri forma parte del escenario base. Pedri no se utiliza como palanca positiva adicional.

## Reproducción

```bash
python src/esp_fra/build_player_indices.py
python src/esp_fra/simulate_match.py
python src/esp_fra/scenario_analysis.py
```

También puede ejecutarse el notebook `notebooks/ESP_FRA_player_based_WCPI.ipynb`.

## Limitaciones

Los ratings son estimaciones estructuradas del modelo y no una base oficial homogénea. Los minutos esperados son supuestos versionados. La independencia Poisson simplifica la dinámica del marcador. La prórroga aplica un factor de intensidad de 0,85 y la tanda parte de un baseline neutral del 50%.
