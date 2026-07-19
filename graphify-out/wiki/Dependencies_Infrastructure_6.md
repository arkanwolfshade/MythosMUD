# Dependencies Infrastructure

> 8 nodes · cohesion 0.29

## Key Concepts

- **get_npc_population_controller()** (8 connections) — `server/dependencies.py`
- **TestGetNPCPopulationController** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_npc_population_controller_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_npc_population_controller_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Tests for get_npc_population_controller dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_npc_population_controller returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_npc_population_controller raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Get an NPCPopulationController instance with dependency injection.      Args:** (1 connections) — `server/dependencies.py`

## Relationships

- [[Dependency Injection Tests]] (4 shared connections)
- [[Combat Command Handler]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 21 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
