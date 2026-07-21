# Decisión de proveedor homogéneo para estadísticas de partido

## Decisión

Se adopta **FotMob con datos de Opta** como proveedor secundario homogéneo para las métricas avanzadas partido a partido que no aparecen de forma estructurada en los informes oficiales de FIFA.

FIFA continúa siendo la fuente primaria para:

- calendario y sedes;
- resultados oficiales;
- condición de campeón;
- goleadores y eventos;
- convocatoria y dorsales.

FotMob / Opta se utiliza para:

- posesión;
- expected goals (xG);
- tiros totales;
- toques en el área rival;
- otras métricas avanzadas cuando estén expuestas de forma comparable.

## Motivo

Las páginas de partido de FotMob declaran que sus estadísticas detalladas están alimentadas por Opta y mantienen una estructura común entre encuentros. Esto permite evitar la mezcla de métricas calculadas con definiciones distintas.

## Cobertura validada en esta iteración

| Partido | Posesión | xG | Tiros | Estado |
|---|---:|---:|---:|---|
| España - Arabia Saudí | Sí | Sí | Sí | Integrado |
| Uruguay - España | Sí | Sí | Sí | Integrado |
| España - Bélgica | Sí | Sí | Sí | Integrado |
| Francia - España | Sí | Sí | Sí | Integrado |
| España - Argentina | Sí | Sí | Sí | Integrado, 120 minutos |
| España - Cabo Verde | Parcial FIFA | Pendiente | Sí FIFA | Pendiente de extracción FotMob |
| España - Austria | Página localizada | Pendiente | Pendiente | Pendiente de extracción |
| Portugal - España | Página localizada | Pendiente | Pendiente | Pendiente de extracción |

## Regla de prioridad

1. FIFA para hechos oficiales y resultados.
2. FotMob / Opta para estadísticas avanzadas homogéneas.
3. Una métrica oficial de FIFA puede mantenerse como validación adicional.
4. Si FIFA y FotMob difieren, se conserva el valor del proveedor homogéneo en el campo analítico y se documenta la discrepancia.
5. No se promedian valores de proveedores distintos.

## Discrepancia detectada

Para Uruguay - España, un artículo narrativo de FIFA indicó 57% de posesión española, mientras que FotMob / Opta registra 67%. El dataset conserva 67% por consistencia con el proveedor homogéneo y deja constancia del conflicto en `notes`.

## Tratamiento de la final

España - Argentina duró 120 minutos. Las cifras de posesión, xG y tiros corresponden al partido completo, incluida la prórroga. No deben compararse directamente con partidos de 90 minutos sin normalización.

Métricas recomendadas para comparaciones temporales:

```text
shots_per_90 = shots / duration_minutes * 90
xg_per_90 = xg / duration_minutes * 90
goals_per_90 = goals / duration_minutes * 90
```

## Estado metodológico

La fuente es secundaria, pero los registros se etiquetan como `verified_secondary_homogeneous`. Esta etiqueta significa que:

- el partido y el proveedor han sido identificados;
- la métrica aparece explícitamente en la página;
- la definición procede del mismo ecosistema de datos;
- no se presenta como estadística oficial de FIFA.
