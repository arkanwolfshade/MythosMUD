# Tests for get npc spawning

> 6 nodes

## Key Concepts

- **TestGetNPCSpawningService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_npc_spawning_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_npc_spawning_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Tests for get_npc_spawning_service dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_npc_spawning_service returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_npc_spawning_service raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [. init ()](_init_%28%29.md) (3 shared connections)
- [Connection Manager](Connection_Manager.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*