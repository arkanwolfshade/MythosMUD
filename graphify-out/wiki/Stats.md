# Stats

> 29 nodes

## Key Concepts

- **Stats** (12 connections)
- **.roll_stats()** (7 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **_ProfessionStatRequirementsSource** (6 connections) — `server/game/stats_generator.py`
- **._roll_until_profession_requirements_met()** (6 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
- **._resolve_profession_stat_requirements()** (4 connections) — `server/game/stats_generator.py`
- **._roll_4d6_drop_lowest()** (4 connections) — `server/game/stats_generator.py`
- **._roll_point_buy()** (4 connections) — `server/game/stats_generator.py`
- **.validate_class_prerequisites()** (4 connections) — `server/game/stats_generator.py`
- **.get_stat_requirements()** (1 connections) — `server/game/stats_generator.py`
- **Protocol** (1 connections)
- **Roll character stats using the specified method. Args: method: Rolling method…** (1 connections) — `server/game/stats_generator.py`
- **Roll Size using formula: (2D6+6)*5 (range 40-90).** (1 connections) — `server/game/stats_generator.py`
- **Roll stats using 3d6 method (scaled to 15-90 range).** (1 connections) — `server/game/stats_generator.py`
- **Roll stats using 4d6 drop lowest method (more generous, scaled to 15-90 range).** (1 connections) — `server/game/stats_generator.py`
- **Generate stats using a point-buy system (balanced, scaled to 1-100 range).** (1 connections) — `server/game/stats_generator.py`
- **Check if stats meet the prerequisites for a given class. Args: stats: The…** (1 connections) — `server/game/stats_generator.py`
- **Get a list of classes that the character qualifies for. Args: stats: The…** (1 connections) — `server/game/stats_generator.py`
- **Roll stats and validate against class requirements. Args: method: The rolling…** (1 connections) — `server/game/stats_generator.py`
- **Load stat requirements from the caller-supplied profession object.** (1 connections) — `server/game/stats_generator.py`
- *... and 4 more nodes in this community*

## Relationships

- [Stats](Stats.md) (14 shared connections)
- [stats_generator_summary.py](stats_generator_summary.py.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*