# Plan de recolección de datos

## 1. Alcance

El análisis cubre exclusivamente el recorrido de España en el Mundial 2026, desde la fase de grupos hasta la final.

El objetivo es construir una base descriptiva reproducible que permita responder:

1. Cómo evolucionó España durante el torneo.
2. Qué métricas explican su rendimiento ofensivo, defensivo y de control.
3. Qué jugadores concentraron minutos y contribuciones.
4. Cómo se compara España con sus rivales y con la media del torneo.
5. Qué narrativa visual explica mejor la conquista del título.

## 2. Jerarquía de fuentes

### Nivel 1. FIFA

Fuente prioritaria para resultados, calendario, estadísticas de partido, estadísticas de equipo, estadísticas de jugadores y rankings del torneo.

### Nivel 2. RFEF

Validación de convocatoria, dorsales, posiciones, cuerpo técnico y comunicaciones oficiales.

### Nivel 3. Proveedor estadístico secundario

Se utilizará únicamente para completar minutos, alineaciones, sustituciones o métricas que no estén disponibles en FIFA.

### Nivel 4. Prensa fiable

Se reservará para contexto narrativo, hitos, récords y declaraciones. No será la fuente principal de métricas cuantitativas cuando exista una fuente oficial.

## 3. Orden de carga

1. Registrar todas las fuentes en `sources_registry.csv`.
2. Cargar convocatoria oficial en `players.csv`.
3. Cargar calendario y resultados en `matches.csv`.
4. Cargar estadísticas de España y rival en `match_team_stats.csv`.
5. Cargar alineaciones, minutos y rendimiento en `player_match_stats.csv`.
6. Cargar goles, cambios, tarjetas y otros hitos en `match_events.csv`.
7. Cargar métricas comparables del resto de selecciones en `tournament_benchmark.csv`.
8. Ejecutar controles de integridad.
9. Calcular KPIs derivados.
10. Publicar outputs preparados para Tableau y carrusel.

## 4. Reglas de integración

- Cada registro debe contener `source_id` o `source_url`.
- La fecha de consulta debe almacenarse en formato ISO `YYYY-MM-DD`.
- Los porcentajes se guardan como valores decimales entre 0 y 1 o como porcentaje entre 0 y 100, pero nunca se mezclan dentro del mismo campo.
- Los minutos de prórroga se incluyen en `minutes_played`, pero el partido conserva campos separados para resultado a 90 y 120 minutos.
- Los penaltis de tanda se almacenan como eventos específicos y no se suman a `goals_for` ni `goals_against`.
- Una discrepancia entre fuentes se registra en `notes`; no se resuelve mediante promedio.
- Si FIFA y una fuente secundaria difieren, prevalece FIFA salvo que se documente un error material.

## 5. KPIs previstos

### Resultado

- partidos jugados;
- victorias, empates y derrotas;
- goles a favor y en contra;
- diferencia de goles;
- porterías a cero;
- minutos por gol recibido;
- porcentaje de victorias.

### Ataque

- goles por partido;
- tiros y tiros a puerta por partido;
- xG por partido;
- conversión de tiros;
- conversión de tiros a puerta;
- diferencia `goles - xG`;
- distribución de goleadores.

### Control

- posesión media;
- precisión de pase;
- pases completados;
- diferencia de posesión;
- diferencia de precisión de pase;
- partidos con superioridad de posesión.

### Defensa

- goles recibidos por partido;
- tiros concedidos;
- tiros a puerta concedidos;
- xG concedido;
- recuperaciones, intercepciones, despejes y bloqueos;
- porcentaje de partidos sin encajar.

### Plantilla

- jugadores utilizados;
- titulares diferentes;
- minutos acumulados;
- concentración de minutos;
- goles y asistencias de titulares y suplentes;
- edad media del once;
- contribución del banquillo.

## 6. Salidas de esta fase

- tablas CSV normalizadas;
- diccionario de datos;
- registro de fuentes;
- informe de calidad;
- tabla de KPIs;
- extractos preparados para Tableau;
- base narrativa para el carrusel final.
