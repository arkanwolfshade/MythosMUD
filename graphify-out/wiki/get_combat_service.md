# get_combat_service

> 8 nodes

## Key Concepts

- **get_combat_service()** (8 connections) — `server/dependencies.py`
- **TestGetCombatService** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_combat_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_combat_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Get a CombatService instance with dependency injection. Args: request: The…** (1 connections) — `server/dependencies.py`
- **Tests for get_combat_service dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_combat_service returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_combat_service raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [test_dependencies.py](test_dependencies.py.md) (2 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [get_container](get_container.md) (1 shared connections)
- [Request](Request.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*