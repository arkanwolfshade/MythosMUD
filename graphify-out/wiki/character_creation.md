# character creation

> 34 nodes

## Key Concepts

- **StatsGenerator** (35 connections) — `server/game/stats_generator.py`
- **Stats** (11 connections)
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **TestGetStatsGenerator** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **.roll_stats()** (6 connections) — `server/game/stats_generator.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **._roll_4d6_drop_lowest()** (4 connections) — `server/game/stats_generator.py`
- **._roll_point_buy()** (4 connections) — `server/game/stats_generator.py`
- **.validate_class_prerequisites()** (4 connections) — `server/game/stats_generator.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- **.test_get_stats_generator()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator_stateless()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.__init__()** (2 connections) — `server/game/stats_generator.py`
- **Any** (2 connections)
- **Service for generating random character statistics.** (1 connections) — `server/game/stats_generator.py`
- **Initialize the stats generator.** (1 connections) — `server/game/stats_generator.py`
- **Roll character stats using the specified method.          Args:             meth** (1 connections) — `server/game/stats_generator.py`
- **Roll Size using formula: (2D6+6)*5 (range 40-90).** (1 connections) — `server/game/stats_generator.py`
- **Roll stats using 3d6 method (scaled to 15-90 range).** (1 connections) — `server/game/stats_generator.py`
- **Roll stats using 4d6 drop lowest method (more generous, scaled to 15-90 range).** (1 connections) — `server/game/stats_generator.py`
- **Generate stats using a point-buy system (balanced, scaled to 1-100 range).** (1 connections) — `server/game/stats_generator.py`
- *... and 9 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (9 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (6 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (4 shared connections)
- [.validate spell name()](validate_spell_name%28%29.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 121 (90%)
- INFERRED: 13 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*