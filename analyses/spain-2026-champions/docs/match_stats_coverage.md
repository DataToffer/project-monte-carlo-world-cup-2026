# Cobertura de estadísticas de partido

Fecha de corte: 2026-07-21

## Estado

La tabla `data/raw/match_team_stats.csv` contiene una fila por selección y partido para los ocho encuentros de España. Los goles están verificados en todos los casos. Las métricas avanzadas se han cargado únicamente cuando la cobertura oficial consultada publica explícitamente el valor.

## Cobertura verificada

| Partido | Métricas numéricas adicionales disponibles |
|---|---|
| España 0-0 Cabo Verde | Posesión España, tiros, tiros a puerta y córners de ambos equipos |
| España 4-0 Arabia Saudí | Solo marcador dentro de esta tabla; goles detallados en `match_events.csv` |
| Uruguay 0-1 España | Posesión España, tiros, tiros a puerta y faltas de ambos equipos |
| España 3-0 Austria | Solo marcador; la fuente oficial confirma dominio, pero no ofrece una línea numérica completa en el texto recuperado |
| España 1-0 Portugal | Solo marcador |
| España 2-1 Bélgica | Solo marcador |
| Francia 0-2 España | Solo marcador |
| España 1-0 Argentina | Tiros totales de ambos equipos durante 120 minutos |

## Reglas aplicadas

1. No se imputan estadísticas ausentes.
2. No se combinan proveedores con definiciones incompatibles sin registrar el cambio.
3. Los campos sin evidencia explícita permanecen nulos.
4. `verified_partial` significa que parte de la fila está respaldada por una fuente oficial.
5. `verified_score_only` significa que únicamente el resultado está confirmado dentro de esa fila.
6. La final incluye 120 minutos; cualquier comparación por partido deberá normalizar por 90 minutos o etiquetar la duración.

## Siguiente acción

Localizar un feed homogéneo de box scores para los ocho partidos. Antes de incorporarlo se contrastarán al menos dos encuentros con FIFA, especialmente Cabo Verde y Uruguay, donde ya existen valores oficiales publicados.
