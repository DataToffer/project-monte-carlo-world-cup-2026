# Auditoría y reconstrucción, España campeona del Mundial 2026

Fecha de reconstrucción: 2026-07-22

## Decisión

La capa descriptiva anterior queda invalidada. Se reconstruye desde cero usando exclusivamente datos finales posteriores a la final y fuentes oficiales de FIFA. No se reutilizan promedios parciales ni cortes previos del torneo.

## Jerarquía de fuentes

1. Tabla estadística final estructurada de FIFA.
2. Informes oficiales de cada partido de FIFA.
3. Artículos finales de estadísticas de FIFA.
4. RFEF, únicamente para complementar eventos no disponibles en FIFA.

Cuando dos fuentes oficiales discrepan, el dato no se fuerza: se registra la discrepancia y no se publica hasta resolverla.

## Discrepancia crítica: Rodri

FIFA mantiene dos valores incompatibles:

- Tabla final estructurada: 799 pases y 747 pases completados.
- Artículo editorial final: 790 pases completados.

Por tanto:

- No se utilizará «790 pases completados».
- Tampoco se etiquetará «799» como pases completados mientras FIFA no aclare la discrepancia.
- En la tabla maestra se conservarán los valores y la definición exacta de cada fuente en registros separados.

## KPIs finales de equipo validados

| Métrica | Valor |
|---|---:|
| Partidos | 8 |
| Victorias finales | 7 |
| Empates tras 90 minutos | 1 |
| Derrotas | 0 |
| Goles a favor | 14 |
| Goles en contra | 1 |
| Diferencia de goles | +13 |
| Porterías a cero | 7 |
| Remates | 140 |
| Remates a puerta | 54 |
| xG | 17,48 |
| Córneres | 54 |
| Control de la posesión | 58% |
| Pases intentados de equipo | 5.470 |
| Pases completados de equipo | 4.945 |
| Precisión de pase | 90% |

## Trayectoria oficial corregida

| Fecha local | Fase | Partido | Resultado |
|---|---|---|---:|
| 15-06-2026 | Fase de grupos | España - Cabo Verde | 0-0 |
| 21-06-2026 | Fase de grupos | España - Arabia Saudí | 4-0 |
| 26-06-2026 | Fase de grupos | Uruguay - España | 0-1 |
| 02-07-2026 | Dieciseisavos | España - Austria | 3-0 |
| 06-07-2026 | Octavos | Portugal - España | 0-1 |
| 10-07-2026 | Cuartos | España - Bélgica | 2-1 |
| 14-07-2026 | Semifinal | Francia - España | 0-2 |
| 19-07-2026 | Final | España - Argentina | 1-0, prórroga |

## Reglas para Tableau y el carrusel

1. Una fila por entidad y nivel de granularidad.
2. Separar estadísticas de equipo, partido, jugador y evento.
3. Guardar nombre original del campo, definición, unidad, URL, fecha de extracción y estado de validación.
4. No mezclar totales del torneo con medias por partido.
5. No convertir ausencias en cero.
6. No publicar una cifra con discrepancia abierta.
7. Todos los KPIs del carrusel deben poder reconciliarse contra la tabla maestra.

## Archivos reconstruidos

- `data/final/spain_2026_team_summary.csv`
- `data/final/spain_2026_matches.csv`

## Estado

La tabla de equipo y la trayectoria de los ocho partidos quedan reconstruidas. La tabla completa de jugadores permanece bloqueada hasta extraer y validar todas las métricas finales de FIFA y resolver expresamente la discrepancia de Rodri.
