# Arquitectura

```text
Datos de jugadores o selección
            ↓
   Índices competitivos
            ↓
   Cálculo de lambdas
            ↓
  Distribución de Poisson
            ↓
  100.000 simulaciones
            ↓
Probabilidades y escenarios
            ↓
   Storytelling y visualización
```

## Capas

1. **Datos**: jugadores, selecciones, calendario y resultados reales.
2. **Ratings**: construcción de `WCPI`, ataque, medio, defensa, portería y banquillo.
3. **Motor**: cálculo de lambdas y simulación.
4. **Escenarios**: clasificación, prórroga, penaltis y eventos de jugador.
5. **Comunicación**: tablas, informes, carruseles y material didáctico.
