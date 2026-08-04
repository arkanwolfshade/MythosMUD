# container events rationale

> 86 nodes

## Key Concepts

- **test_npc_service.py** (49 connections) — `server/tests/unit/services/test_npc_service.py`
- **_mock_result_mappings_all()** (29 connections) — `server/tests/unit/services/test_npc_service.py`
- **_def_row()** (18 connections) — `server/tests/unit/services/test_npc_service.py`
- **_spawn_rule_row()** (6 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_update_npc_definition_success()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_spawn_rule_success()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definitions_success()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_by_name_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_by_name_case_insensitive()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_by_name_not_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_npc_definition_success()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_npc_definition_with_base_stats()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_update_npc_definition_invalid_type()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_update_npc_definition_invalid_probability()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_delete_npc_definition_success()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_spawn_rules_success()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_spawn_rule_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_spawn_rule_invalid_min_population()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_spawn_rule_invalid_max_population()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_delete_spawn_rule_success()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definitions_by_type()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definitions_by_sub_zone()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **npc_service()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **sample_npc_definition()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- *... and 61 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [player death service](player_death_service.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 272 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*