# PMCW España vs Francia
## Etapa 1 - Auditoría metodológica y de reproducibilidad

**Estado:** completada  
**Objeto:** establecer qué parte de la arquitectura actual puede reutilizarse y qué parte debe reconstruirse antes de generar datos, ratings, lambdas o probabilidades para España-Francia.

## 1. Alcance de la auditoría

Se revisaron los componentes centrales del repositorio:

- `README.md`
- `pyproject.toml`
- `pmcw/config.py`
- `pmcw/poisson.py`
- `pmcw/match.py`
- `pmcw/group.py`
- `pmcw/events.py`
- `tests/test_match.py`
- documentación metodológica interna del proyecto

También se contrastaron los precedentes España-Austria y Portugal-Croacia + Cristiano.

## 2. Elementos metodológicos que sí quedan validados

### 2.1 Arquitectura general

Se mantiene la secuencia:

```text
Datos -> construcción de índices -> cálculo de lambdas -> Poisson -> Monte Carlo -> escenarios -> comunicación
```

### 2.2 Motor de 90 minutos

El motor de partido usa dos distribuciones Poisson independientes con lambdas de entrada y calcula:

- victoria local;
- empate;
- victoria visitante;
- goles medios;
- más de 2,5 goles;
- ambos marcan;
- marcadores más frecuentes.

Este componente es reutilizable siempre que las lambdas procedan de una capa de datos validada.

### 2.3 Fórmula de goles esperados

La función `expected_goals()` aplica:

```text
lambda_A = base_goals
         + attack_defense_coef * (attack_A - defense_B)
         + midfield_coef       * (midfield_A - midfield_B)
         + wcpi_coef           * (WCPI_A - WCPI_B)
         - goalkeeper_coef     * (goalkeeper_B - 75)
```

Parámetros actuales:

| Parámetro | Valor |
|---|---:|
| `base_goals` | 1.25 |
| `attack_defense_coef` | 0.025 |
| `midfield_coef` | 0.012 |
| `wcpi_coef` | 0.010 |
| `goalkeeper_coef` | 0.010 |
| `min_lambda` | 0.25 |

La fórmula se conserva como parte del núcleo PMCW, pero no se utilizará hasta validar cómo se construyen los índices de España y Francia.

### 2.4 Reproducibilidad mínima

Quedan consolidados:

- 100.000 simulaciones por análisis;
- seed fija y documentada;
- separación entre inputs y resultados;
- consistencia de probabilidades;
- resultados reales fijados y no resimulados;
- distinción entre datos observados, estimaciones y proxies.

## 3. Elementos que no quedan validados y deben reconstruirse

### 3.1 Ratings individuales

El repositorio no contiene actualmente una función reproducible que transforme datos observados de jugador en ratings de:

- ataque;
- medio campo;
- defensa;
- portería;
- físico;
- forma;
- experiencia.

En los precedentes player-based, esos ratings se introdujeron como estimaciones modelizadas. Por tanto, no pueden reutilizarse como si fueran una capa de datos objetiva.

### 3.2 Ponderación por minutos

El concepto `minutes_weight` está documentado, pero no existe todavía una regla única y automatizada para derivarlo a partir de:

- probabilidad de titularidad;
- minutos recientes con selección;
- estado físico;
- rol táctico;
- probabilidad de sustitución;
- disponibilidad para prórroga.

### 3.3 Agregación player-based

Las fórmulas de agregación de España-Austria existen en la documentación, pero no forman parte del paquete `pmcw` como función testeada. Deben convertirse en código común antes de usarlas en España-Francia.

### 3.4 Calibración de coeficientes

Los coeficientes del motor se encuentran fijados en configuración, pero el repositorio no incorpora todavía:

- dataset histórico de calibración;
- función de pérdida;
- validación temporal;
- comparación contra baseline;
- intervalos de sensibilidad.

Se conservan como parámetros de la versión metodológica actual, no como coeficientes empíricamente reestimados para España-Francia.

### 3.5 Prórroga y penaltis

El módulo Portugal-Croacia implementa:

- prórroga con escalado `30/90`;
- factor de fatiga `0.85`;
- probabilidad de tanda parametrizada;
- eventos de jugador condicionados.

Sin embargo, no contiene un modelo general de secuencia de marcador, momentum o capacidad de remontada. Cualquier ampliación para España-Francia deberá declararse como nueva versión y validarse por sensibilidad.

## 4. Defectos detectados en la simulación España-Francia descartada

La ejecución anterior queda anulada porque:

1. se asignaron ratings individuales sin una transformación trazable desde datos observados;
2. se introdujeron índices agregados de selección de forma manual;
3. se fijaron lambdas directamente;
4. se añadieron multiplicadores de momentum sin calibración previa;
5. se generaron resultados antes de cerrar la capa de datos.

Los archivos de esa ejecución no deben considerarse parte de la evidencia analítica oficial del proyecto.

## 5. Arquitectura aprobada para reiniciar España-Francia

### Capa A - Datos observados

Una fila por jugador y fuente, con variables originales sin transformar.

Campos mínimos:

```text
snapshot_date
team_id
player_id
player_name
position_group
club
age
source_name
source_url
source_date
metric_name
metric_value
metric_unit
competition_scope
minutes_sample
quality_flag
```

### Capa B - Datos normalizados

Transformaciones homogéneas para España y Francia:

- normalización por 90 minutos cuando proceda;
- percentiles por posición;
- tratamiento de muestras pequeñas;
- normalización de escalas;
- control de duplicados;
- control de fecha de corte.

### Capa C - Ratings derivados

Los ratings no se introducirán manualmente. Se calcularán desde variables observadas mediante una matriz de pesos versionada.

### Capa D - Minutos esperados

Los pesos de participación se calcularán mediante una regla común y documentada.

### Capa E - Índices de selección

Solo después de cerrar las capas anteriores se calcularán:

- `attack_index`;
- `midfield_index`;
- `defense_index`;
- `goalkeeper_index`;
- `bench_index`;
- `WCPI`.

### Capa F - Simulación

Orden obligatorio:

1. calcular lambdas con la ecuación PMCW;
2. ejecutar 90 minutos;
3. validar distribución;
4. modelar prórroga;
5. modelar penaltis;
6. añadir eventos accesorios fuera del motor principal.

## 6. Reglas de control para la siguiente etapa

No se podrá avanzar al motor si no se cumplen todos los controles:

- misma fecha de corte para España y Francia;
- mismas fuentes o fuentes equivalentes;
- mismas variables por posición;
- trazabilidad de cada dato;
- ausencia de ratings manuales;
- pesos versionados;
- funciones de agregación en código;
- tests unitarios para transformaciones e índices;
- etiquetado explícito de proxies;
- dataset congelado antes de simular.

## 7. Decisión de la etapa 1

**Resultado de la auditoría:** el núcleo de simulación Poisson-Monte Carlo es reutilizable. La capa player-based no es todavía suficientemente reproducible y debe reconstruirse desde datos observados antes de generar cualquier resultado España-Francia.

## 8. Siguiente etapa autorizada

Construcción del **diccionario de datos y protocolo de fuentes España-Francia**, sin asignar todavía ratings ni probabilidades.
