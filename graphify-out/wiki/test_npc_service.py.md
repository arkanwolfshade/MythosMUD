# test_npc_service.py

> 14 nodes

## Key Concepts

- **test_npc_service.py** (50 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_delete_npc_definition_not_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_delete_spawn_rule_not_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_not_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_spawn_rules_database_error()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_npc_definition_invalid_type()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_error()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **Unit tests for NPC service. Tests the NPCService class.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition() returns None when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition() handles errors.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_npc_definition() raises ValueError for invalid type.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test delete_npc_definition() returns False when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_spawn_rules() handles database errors.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test delete_spawn_rule() returns False when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`

## Relationships

- [asyncio](asyncio.md) (13 shared connections)
- [_mock_result_mappings_all](_mock_result_mappings_all.md) (11 shared connections)
- [_def_row](_def_row.md) (9 shared connections)
- [_spawn_rule_row](_spawn_rule_row.md) (5 shared connections)
- [NPCDefinition](NPCDefinition.md) (4 shared connections)
- [npc_service](npc_service.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_update_npc_definition_invalid_type](test_update_npc_definition_invalid_type.md) (1 shared connections)
- [test_update_npc_definition_invalid_probability](test_update_npc_definition_invalid_probability.md) (1 shared connections)
- [test_create_spawn_rule_invalid_min_population](test_create_spawn_rule_invalid_min_population.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 65 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*