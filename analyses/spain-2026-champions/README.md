# España campeona del mundo 2026: modelo descriptivo

Esta carpeta contiene la fase descriptiva final de Project Monte Carlo World Cup 2026. El objetivo es explicar con datos reales cómo España construyó el título.

## Arquitectura

```text
data/raw/                  Datos base de partidos, jugadores, eventos y estadísticas
outputs/tables/            KPIs por partido y resumen agregado del torneo
outputs/tableau/           Extractos longitudinales preparados para Tableau
src/                       Scripts reproducibles de transformación
data/metadata/             Diccionario de datos y registro de fuentes
docs/                      Metodología, calidad, cobertura y diseño del dashboard
```

## Entregables principales

- `data/raw/matches.csv`: ocho partidos oficiales.
- `data/raw/players.csv`: convocatoria oficial de 26 jugadores.
- `data/raw/match_events.csv`: eventos de gol verificados.
- `data/raw/match_team_stats.csv`: métricas por equipo y partido.
- `outputs/tables/spain_goal_summary.csv`: tabla de goleadores.
- `outputs/tables/spain_match_kpis.csv`: KPIs por encuentro.
- `outputs/tables/spain_tournament_summary.csv`: resumen agregado del torneo.
- `outputs/tableau/spain_match_metrics_long.csv`: capa longitudinal por partido.
- `outputs/tableau/spain_tournament_kpis_long.csv`: tarjetas KPI para Tableau.
- `src/build_descriptive_kpis.py`: transformación de partido.
- `src/build_tournament_summary.py`: agregación final de KPIs.

## Modelo de datos

| Tabla | Granularidad | Función |
|---|---|---|
| `matches` | Un registro por partido de España | Calendario, fase, rival y resultado |
| `players` | Un registro por convocado | Dimensión maestra de jugadores |
| `match_team_stats` | Un registro por equipo y partido | Comparación España-rival |
| `player_match_stats` | Un registro por jugador y partido | Minutos y rendimiento individual |
| `match_events` | Un registro por evento | Goles, asistencias, cambios y tarjetas |
| `tournament_benchmark` | Un registro por selección | Comparación con el torneo |
| `spain_match_kpis` | Un registro por partido | Indicadores derivados por encuentro |
| `spain_tournament_summary` | Un registro por KPI | Resumen ejecutivo del campeón |

## Política de datos

- FIFA y RFEF prevalecen para resultados, convocatoria y eventos.
- FotMob/Opta se usa como proveedor secundario homogéneo de métricas avanzadas.
- Los valores ausentes permanecen nulos.
- Las métricas parciales muestran siempre su cobertura.
- La final se normaliza por 90 minutos cuando se comparan métricas de volumen.
- Los penaltis de una tanda no se contabilizan como goles del partido.

## Ejecución

```bash
python analyses/spain-2026-champions/src/build_descriptive_kpis.py
python analyses/spain-2026-champions/src/build_tournament_summary.py
```

## Estado

- [x] Arquitectura definida.
- [x] Convocatoria oficial cargada.
- [x] Calendario completo cargado.
- [x] Eventos de gol cargados.
- [x] Estadísticas homogéneas disponibles incorporadas.
- [x] KPIs por partido calculados.
- [x] KPIs agregados del torneo calculados.
- [x] Extractos para Tableau preparados.
- [x] Blueprint del dashboard documentado.
- [ ] Ampliar cobertura de Austria y Portugal.
- [ ] Completar estadísticas individuales por partido.
- [ ] Construir dashboard y carrusel finales.
