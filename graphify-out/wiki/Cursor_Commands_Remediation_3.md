# Cursor Commands Remediation

> 24 nodes · cohesion 0.12

## Key Concepts

- **Stats** (11 connections)
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **.roll_stats()** (6 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- **._roll_4d6_drop_lowest()** (4 connections) — `server/game/stats_generator.py`
- **._roll_point_buy()** (4 connections) — `server/game/stats_generator.py`
- **.validate_class_prerequisites()** (4 connections) — `server/game/stats_generator.py`
- **Any** (2 connections)
- **Roll Size using formula: (2D6+6)*5 (range 40-90).** (1 connections) — `server/game/stats_generator.py`
- **Roll stats using 3d6 method (scaled to 15-90 range).** (1 connections) — `server/game/stats_generator.py`
- **Roll stats using 4d6 drop lowest method (more generous, scaled to 15-90 range).** (1 connections) — `server/game/stats_generator.py`
- **Generate stats using a point-buy system (balanced, scaled to 1-100 range).** (1 connections) — `server/game/stats_generator.py`
- **Check if stats meet the prerequisites for a given class.          Args:** (1 connections) — `server/game/stats_generator.py`
- **Get a list of classes that the character qualifies for.          Args:** (1 connections) — `server/game/stats_generator.py`
- **Roll stats and validate against class requirements.          Args:             m** (1 connections) — `server/game/stats_generator.py`
- **Roll stats and validate against profession requirements.          Args:** (1 connections) — `server/game/stats_generator.py`
- **Check if stats meet profession requirements.          Args:             stats: T** (1 connections) — `server/game/stats_generator.py`
- **Get a summary of the character's stats including modifiers and totals.** (1 connections) — `server/game/stats_generator.py`
- **Roll character stats using the specified method.          Args:             meth** (1 connections) — `server/game/stats_generator.py`

## Relationships

- [Player Effects API](Player_Effects_API.md) (11 shared connections)
- [Character Stats Model](Character_Stats_Model.md) (1 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`

## Audit Trail

- EXTRACTED: 77 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*