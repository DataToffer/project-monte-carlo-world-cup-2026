# Metodología España-Francia, player-based WCPI v1

## Unidad de análisis

Se utilizan 16 jugadores por selección. Cada jugador dispone de ratings por dimensión y un peso de minutos esperado.

## Agregación posicional

- Ataque: `0.65 ATT + 0.25 MID + 0.10 DEF`
- Medio: `0.60 MID + 0.25 ATT + 0.15 DEF`
- Defensa: `0.55 DEF + 0.25 MID + 0.10 ATT + 0.10 GK`

## WCPI

```text
0.30 ataque + 0.28 medio + 0.22 defensa + 0.10 portería + 0.10 banquillo
```

## Lambda

```text
1.25 + 0.025(ATT_A-DEF_B) + 0.012(MID_A-MID_B) + 0.010(WCPI_A-WCPI_B) - 0.010(GK_B-75)
```

## Motor

Poisson independiente en 90 minutos, prórroga escalada a 30 minutos con factor 0,85 y tanda con baseline neutral del 50%.

## Escenarios

Cada evento modifica inputs, reconstruye índices y lambdas, y vuelve a ejecutar la simulación. No se suman puntos porcentuales manualmente.

## Interpretación

El modelo describe distribuciones de escenarios. No constituye una probabilidad oficial ni predice un resultado exacto.
