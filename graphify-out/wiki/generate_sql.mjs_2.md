# generate_sql.mjs

> 17 nodes

## Key Concepts

- **Stats** (11 connections)
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **.roll_stats()** (6 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- **.validate_class_prerequisites()** (4 connections) — `server/game/stats_generator.py`
- **Any** (2 connections)
- **Roll stats and validate against class requirements. Args: method: The rolling…** (2 connections) — `server/game/stats_generator.py`
- **Roll stats using 3d6 method (scaled to 15-90 range).** (1 connections) — `server/game/stats_generator.py`
- **Check if stats meet the prerequisites for a given class. Args: stats: The…** (1 connections) — `server/game/stats_generator.py`
- **Get a list of classes that the character qualifies for. Args: stats: The…** (1 connections) — `server/game/stats_generator.py`
- **Check if stats meet profession requirements. Args: stats: The character's stats…** (1 connections) — `server/game/stats_generator.py`
- **Get a summary of the character's stats including modifiers and totals. Args:…** (1 connections) — `server/game/stats_generator.py`
- **Roll character stats using the specified method. Args: method: Rolling method…** (1 connections) — `server/game/stats_generator.py`

## Relationships

- [UpgradeImplementationPlan](UpgradeImplementationPlan.md) (9 shared connections)
- [Graphify Code Graph](Graphify_Code_Graph.md) (3 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*