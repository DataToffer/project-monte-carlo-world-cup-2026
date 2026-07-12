# PMCW Engine

`PMCW Engine` es el núcleo reutilizable de Project Monte Carlo World Cup 2026.

## Objetivos

- Simular grupos y eliminatorias.
- Mantener trazabilidad de inputs y parámetros.
- Separar el motor probabilístico de la comunicación.
- Permitir análisis player-based y eventos accesorios.
- Hacer el proyecto reutilizable más allá del Mundial 2026.

## Componentes

- `pmcw.poisson`: cálculo de goles esperados.
- `pmcw.match`: simulación de partido único.
- `pmcw.group`: simulación de grupos.
- `pmcw.ratings`: agregación player-based.
- `pmcw.events`: eventos accesorios de jugador.
