# Auditoría de datos, España campeona del Mundial 2026

Fecha de auditoría: 2026-07-22

## Hallazgo principal

El repositorio no contenía todavía una capa descriptiva final y consolidada del torneo completo. El último bloque de trabajo estaba centrado en la semifinal España-Francia y fue incorporado el 13 de julio de 2026, antes de la final.

Por tanto, las cifras del carrusel final no deben considerarse validadas contra el repositorio hasta completar esta auditoría.

## Corrección crítica: Rodri

La estadística correcta distingue entre:

- Pases intentados: 799
- Pases completados: 747
- Precisión aproximada: 93,5%

No debe publicarse «790 pases completados». Esa cifra aparece en una pieza editorial de FIFA, pero entra en conflicto con la tabla estadística final de FIFA, que desglosa 799 pases y 747 completados. Para la base de datos se prioriza la tabla estadística final estructurada.

## KPIs de equipo confirmados en la tabla final de FIFA

- Partidos: 8
- Victorias finales: 7
- Empates tras 90 minutos: 1
- Derrotas: 0
- Goles a favor: 14
- Goles en contra: 1
- Diferencia de goles: +13
- Porterías a cero: 7
- Remates: 140
- Remates a puerta: 54
- xG: 17,48
- Córneres: 54
- Control de la posesión: 58%
- Pases intentados del equipo: 5.470
- Pases completados del equipo: 4.945
- Precisión de pase: 90%

## Jugadores confirmados para el carrusel

- Rodri: 799 pases intentados, 747 completados
- Pau Cubarsí: 690 pases intentados, 668 completados
- Aymeric Laporte: 660 pases intentados, 618 completados

## Reglas de validación

1. No mezclar cortes temporales de estadísticas publicados antes y después de la final.
2. Diferenciar siempre pases intentados de pases completados.
3. Priorizar tablas finales estructuradas frente a artículos editoriales cuando exista contradicción.
4. Conservar URL, fecha de consulta, campo original y definición de cada métrica.
5. No rellenar valores ausentes ni derivar métricas sin dejar documentada la fórmula.
6. No actualizar el carrusel ni el copy hasta cerrar la matriz de validación.

## Fuentes prioritarias

- FIFA, estadísticas finales de equipos del Mundial 2026.
- FIFA, estadísticas finales de jugadores del Mundial 2026.
- FIFA, resumen de estadísticas clave del torneo.
- FIFA y RFEF, resultados y eventos oficiales de los ocho partidos de España.

## Estado

Auditoría abierta. Los datos confirmados de este documento pueden utilizarse como referencia provisional, pero la tabla completa para Tableau debe incluir el detalle por partido, jugador, métrica, fuente y fecha de extracción antes de considerarse cerrada.
