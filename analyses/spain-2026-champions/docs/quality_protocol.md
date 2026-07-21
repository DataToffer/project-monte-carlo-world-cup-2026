# Protocolo de calidad del modelo descriptivo

## Controles de integridad

1. `goals_for` y `goals_against` deben coincidir con el marcador oficial.
2. La suma de goles de jugadores debe coincidir con los goles de España, excluyendo goles en propia puerta cuando proceda.
3. `shots_on_target` no puede superar `shots`.
4. `passes_completed` no puede superar `passes_attempted`.
5. `clean_sheet = 1` exige `goals_against = 0`.
6. Un partido con prórroga debe tener `extra_time = 1` y resultado a 120 minutos informado.
7. Los penaltis de tanda no se suman al marcador del partido.
8. Cada jugador titular debe registrar minutos positivos.
9. La suma de minutos por equipo debe ser coherente con 90 o 120 minutos y con el número de jugadores en campo.
10. Cada registro cuantitativo debe disponer de fuente identificable.

## Controles de consistencia semántica

- Los porcentajes deben utilizar la misma escala dentro de cada columna.
- Las unidades deben declararse en el diccionario de datos.
- `xg` y `opponent_xg` solo pueden compararse si proceden del mismo proveedor y definición.
- Las métricas de posesión no deben mezclarse con métricas de control de posesión si el proveedor las define de forma distinta.
- Los valores nulos deben significar dato no disponible, nunca cero implícito.

## Gestión de discrepancias

Cuando dos fuentes difieran:

1. Registrar ambas referencias.
2. Identificar si la discrepancia procede de una definición diferente.
3. Priorizar FIFA cuando exista dato oficial comparable.
4. Documentar la decisión en `notes`.
5. Evitar promediar valores incompatibles.

## Etiquetas de calidad

Cada registro podrá clasificarse como:

- `official`: dato oficial del organizador o federación.
- `verified_secondary`: dato secundario contrastado.
- `derived`: cálculo propio reproducible.
- `contextual`: información narrativa no usada como métrica.
- `pending_validation`: dato pendiente de contraste.

## Criterios de aceptación de la etapa

- Todas las tablas tienen esquema estable.
- Todos los campos están definidos en `data_dictionary.csv`.
- Todas las fuentes están registradas.
- No existen resultados sin marcador oficial.
- No existen métricas derivadas sin fórmula.
- Los controles de integridad no presentan errores críticos.
- El dataset puede importarse en Tableau sin transformar manualmente nombres o tipos.
