# server command handler catatonia check

> 100 nodes

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **test_command_validation.py** (24 connections) — `server/tests/unit/commands/test_command_validation.py`
- **asyncio** (24 connections)
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (16 connections) — `server/command_handler/catatonia_check.py`
- **_is_catatonic()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_load_player_for_catatonia_check()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_database()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_fetch_lucidity_record()** (8 connections) — `server/command_handler/catatonia_check.py`
- **TestCheckGracePeriodBlock** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_registry_player_id_value()** (7 connections) — `server/command_handler/catatonia_check.py`
- **UUID** (7 connections)
- **TestCheckAllCommandBlocks** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCheckCastingState** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_PersistenceGetPlayerByName** (5 connections) — `server/command_handler/catatonia_check.py`
- **_convert_player_id_to_uuid()** (4 connections) — `server/command_handler/catatonia_check.py`
- **.test_check_catatonia_block_allowed_command()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_no_app_state()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_uses_string_registry_key_when_player_id_not_uuid_or_str()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_catatonic()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_catatonic()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 75 more nodes in this community*

## Relationships

- [server command handler command execution](server_command_handler_command_execution.md) (23 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (5 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server command handler alias expansion](server_command_handler_alias_expansion.md) (2 shared connections)
- [scripts add flavor text column](scripts_add_flavor_text_column.md) (2 shared connections)
- [server command handler unified rationale](server_command_handler_unified_rationale.md) (2 shared connections)
- [server services catatonia registry catatoniaregistry](server_services_catatonia_registry_catatoniaregistry.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (1 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 212 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*