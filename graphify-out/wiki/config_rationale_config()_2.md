# config rationale config()

> 6 nodes

## Key Concepts

- **TestGetStatsGenerator** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator_stateless()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_stats_generator() function.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_stats_generator() returns StatsGenerator instance.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_stats_generator() returns stateless instance.** (1 connections) — `server/tests/unit/test_dependency_injection.py`

## Relationships

- [profession game service](profession_game_service.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [command inventory models](command_inventory_models.md) (1 shared connections)
- [room game service](room_game_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 13 (72%)
- INFERRED: 5 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*