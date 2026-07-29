# Tests for get exploration service

> 7 nodes

## Key Concepts

- **TestGetExplorationService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_exploration_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_exploration_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_combat_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_exploration_service returns service when present.** (2 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Tests for get_exploration_service dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_exploration_service raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [. init ()](_init_%28%29.md) (4 shared connections)
- [Connection Manager](Connection_Manager.md) (1 shared connections)
- [get room service()](get_room_service%28%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 17 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*