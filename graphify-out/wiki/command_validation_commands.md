# command validation commands

> 71 nodes

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **test_command_validation.py** (22 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (17 connections) — `server/command_handler/catatonia_check.py`
- **__init__.py** (13 connections) — `server/command_handler/__init__.py`
- **_load_player_for_catatonia_check()** (11 connections) — `server/command_handler/catatonia_check.py`
- **_is_catatonic()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_database()** (9 connections) — `server/command_handler/catatonia_check.py`
- **UUID** (8 connections)
- **_fetch_lucidity_record()** (8 connections) — `server/command_handler/catatonia_check.py`
- **_registry_player_id_value()** (7 connections) — `server/command_handler/catatonia_check.py`
- **_PersistenceGetPlayerByName** (6 connections) — `server/command_handler/catatonia_check.py`
- **_convert_player_id_to_uuid()** (4 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (3 connections)
- **.test_registry_player_id_value_preserves_uuid_and_str()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_registry_player_id_value_stringifies_non_string_ids()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_is_catatonic_with_tier()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_is_catatonic_with_zero_lcd()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_is_catatonic_with_negative_lcd()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_is_catatonic_not_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_is_catatonic_none()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_fetch_lucidity_record()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_query_lucidity_record_success()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 46 more nodes in this community*

## Relationships

- [alias graph rationale](alias_graph_rationale.md) (7 shared connections)
- [command commands handler](command_commands_handler.md) (7 shared connections)
- [commands command validation](commands_command_validation.md) (5 shared connections)
- [player cache rationale](player_cache_rationale.md) (5 shared connections)
- [npc rationale extract](npc_rationale_extract.md) (4 shared connections)
- [combat models rationale](combat_models_rationale.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [combat npc services](combat_npc_services.md) (3 shared connections)
- [command commands validation](command_commands_validation.md) (2 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (1 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/catatonia_check.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 271 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*