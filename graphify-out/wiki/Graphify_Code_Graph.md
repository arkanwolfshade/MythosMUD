# Graphify Code Graph

> 6 nodes

## Key Concepts

- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **._roll_4d6_drop_lowest()** (4 connections) — `server/game/stats_generator.py`
- **._roll_point_buy()** (4 connections) — `server/game/stats_generator.py`
- **Roll Size using formula: (2D6+6)*5 (range 40-90).** (1 connections) — `server/game/stats_generator.py`
- **Roll stats using 4d6 drop lowest method (more generous, scaled to 15-90 range).** (1 connections) — `server/game/stats_generator.py`
- **Generate stats using a point-buy system (balanced, scaled to 1-100 range).** (1 connections) — `server/game/stats_generator.py`

## Relationships

- [generate_sql.mjs](generate_sql.mjs.md) (3 shared connections)
- [UpgradeImplementationPlan](UpgradeImplementationPlan.md) (3 shared connections)

## Source Files

- `server/game/stats_generator.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*