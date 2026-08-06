# infrastructure persistence room

> 6 nodes

## Key Concepts

- **TestGetNPCLifecycleManager** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_npc_lifecycle_manager_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_npc_lifecycle_manager_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Tests for get_npc_lifecycle_manager dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_npc_lifecycle_manager returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_npc_lifecycle_manager raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*