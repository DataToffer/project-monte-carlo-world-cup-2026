# Diccionario de datos, España 2026

## Tablas

### `spain_2026_match_path.csv`
Una fila por partido. Los goles `*_goals_et` representan el marcador final tras prórroga cuando aplica. Para partidos sin prórroga coinciden con el marcador a los 90 minutos.

### `spain_2026_team_stats.csv`
Una fila por KPI final del torneo. `source_status` distingue cifras oficiales finales de métricas derivadas y verificadas.

### `spain_2026_squad.csv`
Los 26 campeones, con dorsal, nombre, grupo posicional y club.

### `spain_2026_player_highlights.csv`
Métricas individuales utilizadas en el carrusel y en el relato final. No debe interpretarse como una tabla completa de rendimiento de los 26 jugadores.

### `spain_2026_sources.csv`
Registro de procedencia, URL, fecha de extracción y prioridad de cada fuente.

## Definiciones críticas

- `passes`: campo de distribución mostrado por la tabla estructurada de FIFA. No equivale automáticamente a pases completados.
- `passes_completed`: pases completados según la tabla estructurada final.
- `passes_completed_editorial`: cifra publicada en un artículo editorial cuando contradice la tabla estructurada. Se conserva para auditoría, pero no se utiliza en cálculos.
- `possession_control`: nombre oficial de la métrica FIFA. No se renombra como posesión media sin documentar la equivalencia.
- `final_wins`: victorias en el resultado definitivo, incluida la final ganada tras prórroga.
- `draws_after_90`: partidos empatados al finalizar el tiempo reglamentario.

## Regla de prioridad

1. Tabla final estructurada de FIFA.
2. Actas, calendario y crónicas oficiales de partido.
3. Artículos editoriales de FIFA para récords o contexto.
4. Métricas derivadas únicamente cuando la fórmula queda documentada.

## Advertencia Rodri

La tabla estructurada final muestra 799 pases y 747 pases completados. Un artículo editorial de FIFA publica 790 pases completados. El dataset conserva ambas cifras y marca la segunda como conflicto editorial. Ningún cálculo debe usar 790 hasta que FIFA corrija o aclare la discrepancia.
