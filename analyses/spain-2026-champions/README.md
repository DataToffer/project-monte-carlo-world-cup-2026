# España campeona del mundo 2026: modelo descriptivo

Esta carpeta abre la fase descriptiva final de Project Monte Carlo World Cup 2026.

## Objetivo

Reconstruir con datos reales el rendimiento de España durante el Mundial 2026 y preparar un modelo analítico reproducible para KPIs, dashboard, carrusel y publicación técnica.

## Cambio de enfoque

La fase predictiva utilizó ratings, lambdas, Poisson y simulación Monte Carlo. Esta fase no estima escenarios futuros. Trabaja exclusivamente con:

- resultados reales;
- estadísticas oficiales o contrastadas;
- eventos de partido;
- datos de jugadores;
- KPIs derivados y documentados.

## Entregables de la etapa 2

```text
analyses/spain-2026-champions/
  README.md
  docs/
    collection_plan.md
    quality_protocol.md
  data/
    raw/
      matches.csv
      players.csv
      match_team_stats.csv
      player_match_stats.csv
      match_events.csv
      tournament_benchmark.csv
    metadata/
      data_dictionary.csv
      sources_registry.csv
```

## Modelo de datos

| Tabla | Granularidad | Función |
|---|---|---|
| `matches` | Un registro por partido de España | Calendario, fase, rival y resultado |
| `players` | Un registro por convocado | Dimensión maestra de jugadores |
| `match_team_stats` | Un registro por equipo y partido | Comparación España-rival |
| `player_match_stats` | Un registro por jugador y partido | Minutos y rendimiento individual |
| `match_events` | Un registro por evento | Goles, asistencias, cambios y tarjetas |
| `tournament_benchmark` | Un registro por selección | Comparación con el torneo |
| `data_dictionary` | Un registro por campo | Definición, unidad, fuente y fórmula |
| `sources_registry` | Un registro por recurso | Trazabilidad y control de fuentes |

## Principios de calidad

- FIFA será la fuente prioritaria cuando el dato esté disponible.
- RFEF validará convocatoria, dorsales y contexto institucional.
- Los proveedores secundarios solo completarán campos no disponibles en la fuente principal.
- No se mezclarán métricas con definiciones incompatibles.
- Cada KPI derivado tendrá fórmula y unidad documentadas.
- Los penaltis de una tanda no se contabilizarán como goles del partido.
- Los datos de 90 y 120 minutos se almacenarán por separado.

## Estado

- [x] Arquitectura definida.
- [x] Plantillas CSV creadas.
- [x] Diccionario inicial creado.
- [x] Registro de fuentes creado.
- [x] Protocolo de calidad documentado.
- [ ] Convocatoria oficial cargada.
- [ ] Calendario completo cargado.
- [ ] Estadísticas de partido cargadas.
- [ ] Estadísticas de jugadores cargadas.
- [ ] KPIs calculados.
- [ ] Dashboard y carrusel construidos.
