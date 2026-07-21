# Dashboard blueprint: Spain 2026 World Champions

## Objective

Explain how Spain built the 2026 World Cup title using verified descriptive data, without predictive outputs.

## Dashboard structure

### 1. Champion overview

KPI cards:

- matches played;
- wins;
- goals for;
- goals against;
- goal difference;
- clean sheets;
- win rate;
- goals per match.

Recommended visual: compact KPI strip plus tournament path timeline.

### 2. Path to the title

One mark per match with:

- opponent;
- stage;
- score;
- goal difference;
- clean-sheet flag;
- duration, distinguishing the 120-minute final.

Recommended visual: horizontal timeline ordered by date.

### 3. Control and attacking production

Metrics:

- possession;
- shots and opponent shots;
- shot difference;
- xG and opponent xG;
- xG difference;
- goals minus xG.

Recommended visuals:

- possession line by match;
- paired bars for shots;
- dumbbell or diverging bar for xG difference.

Only matches with comparable values should enter metric averages. Missing values must remain null, not zero.

### 4. Defensive identity

Metrics:

- clean sheets;
- opponent shots;
- opponent xG;
- goals conceded;
- opponent shots per 90.

Recommended visual: match matrix with one row per opponent and defensive indicators as columns.

### 5. Goals and decisive players

Use `match_events.csv` and `spain_goal_summary.csv` for:

- goals by player;
- goals by stage;
- decisive goals;
- scoring minute;
- open play, penalty and own goal classification.

Recommended visuals:

- scorer ranking;
- goal timeline;
- group-stage versus knockout comparison.

## Filters

- stage;
- opponent;
- metric group;
- quality status;
- 90-minute versus 120-minute match.

## Tableau data sources

Primary tables:

- `outputs/tables/spain_match_kpis.csv`;
- `outputs/tableau/spain_match_metrics_long.csv`;
- `data/raw/match_events.csv`;
- `outputs/tables/spain_goal_summary.csv`.

Relationships:

- `match_id` joins match-level tables;
- `player_id` links goal events to the player dimension;
- avoid physical joins that duplicate match-level KPIs when events contain several rows per match.

## Calculation rules

- Final metrics based on volume must be normalized per 90 minutes before cross-match comparison.
- Possession is not normalized by duration.
- Null means unavailable and must not be converted to zero.
- Tournament-level averages must display the number of matches covered.
- Official and secondary homogeneous metrics must remain distinguishable through `quality_status`.

## Editorial message

The dashboard should support a central conclusion:

> Spain did not win through a single dominant pattern. It combined territorial control, selective attacking efficiency and exceptional defensive suppression across different match contexts.
