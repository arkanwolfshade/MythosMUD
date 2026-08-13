# _def_row

> 18 nodes

## Key Concepts

- **_def_row()** (18 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_npc_definition_success()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_spawn_rule_invalid_max_population()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_spawn_rule_invalid_min_population()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_delete_npc_definition_success()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_by_name_case_insensitive()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_by_name_not_found()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_found()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definitions_by_sub_zone()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition() returns definition when found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition_by_name() matches case-insensitively.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition_by_name() returns None when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_npc_definition() successfully creates definition.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test delete_npc_definition() successfully deletes definition.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_spawn_rule() raises ValueError for invalid min population.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_spawn_rule() raises ValueError when max < min.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definitions_by_sub_zone() filters by sub-zone.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Build procedure result row (mappings().all()[i] or .first()) for NPCDefinition.** (1 connections) — `server/tests/unit/services/test_npc_service.py`

## Relationships

- [asyncio](asyncio.md) (10 shared connections)
- [_mock_result_mappings_all](_mock_result_mappings_all.md) (10 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (9 shared connections)
- [test_create_npc_definition_with_base_stats](test_create_npc_definition_with_base_stats.md) (1 shared connections)
- [_spawn_rule_row](_spawn_rule_row.md) (1 shared connections)
- [test_update_npc_definition_invalid_probability](test_update_npc_definition_invalid_probability.md) (1 shared connections)
- [test_update_npc_definition_invalid_type](test_update_npc_definition_invalid_type.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*