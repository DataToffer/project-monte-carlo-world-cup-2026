# Resumen agregado de KPIs

Esta capa resume el rendimiento completo de España en el Mundial 2026 y está preparada para alimentar las tarjetas ejecutivas del dashboard.

## KPIs con cobertura completa

| KPI | Valor |
|---|---:|
| Partidos | 8 |
| Victorias | 7 |
| Empates tras 90 minutos | 2 |
| Derrotas | 0 |
| Goles a favor | 14 |
| Goles en contra | 1 |
| Diferencia de goles | +13 |
| Porterías a cero | 7 |

Los dos empates tras 90 minutos corresponden al 0-0 ante Cabo Verde y a la final ante Argentina, resuelta en la prórroga.

## KPIs avanzados con cobertura parcial

| KPI | Valor | Cobertura |
|---|---:|---:|
| Posesión media | 65,37% | 6/8 partidos |
| Tiros por partido | 17,00 | 6/8 |
| Tiros concedidos por partido | 5,17 | 6/8 |
| Diferencia media de tiros | +11,83 | 6/8 |
| Tiros por 90 minutos | 16,17 | 6/8 |
| xG por partido | 1,81 | 5/8 |
| xG concedido por partido | 0,24 | 5/8 |
| Diferencia media de xG | +1,57 | 5/8 |
| xG por 90 minutos | 1,69 | 5/8 |
| Goles menos xG | +0,96 | 5/8 |

## Lectura analítica

### 1. Dominio sin depender exclusivamente de la posesión

España promedia un 65,37% de posesión en los seis partidos con dato homogéneo. Sin embargo, la semifinal ante Francia muestra que también pudo imponerse con un reparto más equilibrado del balón.

### 2. Superioridad territorial y defensiva

En los seis partidos con datos de tiros, España genera una ventaja media de 11,83 intentos y concede únicamente 5,17 tiros por encuentro.

### 3. La defensa es el KPI más sólido del título

Siete porterías a cero en ocho partidos y un único gol recibido constituyen la señal descriptiva más fuerte del torneo. A diferencia de xG o posesión, estos indicadores tienen cobertura completa.

### 4. El xG confirma una ventaja estructural, pero con cobertura limitada

En los cinco partidos con dato homogéneo, España registra 1,81 xG por encuentro frente a 0,24 del rival. Esta diferencia no debe presentarse como promedio de todo el torneo sin mostrar la cobertura 5/8.

### 5. La final debe normalizarse

La final duró 120 minutos. Para comparaciones de volumen se utilizan 15 tiros por 90 y 1,72 xG por 90, en lugar de los totales brutos de 20 tiros y 2,29 xG.

## Reglas de visualización

- Mostrar siempre `coverage_matches / total_matches` en métricas parciales.
- No mezclar valores totales y valores por 90 en un mismo eje.
- Usar los KPIs de resultado como tarjetas principales.
- Reservar xG y posesión para una segunda capa analítica.
- La etiqueta `100% cobertura` significa cobertura del indicador, no calidad perfecta de todos los campos.

## Archivos relacionados

- `outputs/tables/spain_tournament_summary.csv`
- `outputs/tableau/spain_tournament_kpis_long.csv`
- `src/build_tournament_summary.py`
