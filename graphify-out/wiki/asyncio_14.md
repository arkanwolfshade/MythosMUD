# asyncio

> 15 nodes

## Key Concepts

- **asyncio** (35 connections)
- **test_get_npc_definition_found()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_update_npc_definition_success()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_npc_service_init()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_update_npc_definition_not_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_npc_definition_invalid_probability()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definitions_database_error()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_system_statistics_database_error()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test NPCService initialization.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definitions() handles database errors.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition() returns definition when found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_npc_definition() raises ValueError for invalid probability.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test update_npc_definition() successfully updates definition.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test update_npc_definition() returns None when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_system_statistics() handles database errors.** (1 connections) — `server/tests/unit/services/test_npc_service.py`

## Relationships

- [test_npc_service.py](test_npc_service.py.md) (13 shared connections)
- [_def_row](_def_row.md) (10 shared connections)
- [_mock_result_mappings_all](_mock_result_mappings_all.md) (10 shared connections)
- [_spawn_rule_row](_spawn_rule_row.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [test_create_spawn_rule_invalid_min_population](test_create_spawn_rule_invalid_min_population.md) (1 shared connections)
- [test_update_npc_definition_invalid_probability](test_update_npc_definition_invalid_probability.md) (1 shared connections)
- [test_update_npc_definition_invalid_type](test_update_npc_definition_invalid_type.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 55 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*