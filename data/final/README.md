# Capa final validada, España 2026

Esta carpeta contiene la capa descriptiva final del recorrido de España en la Copa Mundial 2026.

## Archivos

- `spain_2026_match_path.csv`: ocho partidos, fechas, rondas, rivales y resultados.
- `spain_2026_team_stats.csv`: KPIs finales de equipo.
- `spain_2026_squad.csv`: plantilla oficial de 26 jugadores y dorsales.
- `spain_2026_player_highlights.csv`: métricas individuales utilizadas en el carrusel.
- `spain_2026_sources.csv`: registro de fuentes y fecha de extracción.

## Validación

Los tests en `tests/test_spain_2026_final_data.py` comprueban:

- ocho partidos;
- reconciliación de 14 goles a favor y 1 en contra;
- coherencia de los KPIs principales;
- 26 dorsales únicos;
- separación entre pases y pases completados de Rodri;
- conservación explícita de la discrepancia editorial 790/747.

## Uso

Para Tableau, usar `spain_2026_match_path.csv`, `spain_2026_team_stats.csv` y `spain_2026_player_highlights.csv`. No combinar estas tablas con extracciones parciales anteriores a la final.
