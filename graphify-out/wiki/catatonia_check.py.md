# catatonia_check.py

> 94 nodes

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **asyncio** (24 connections)
- **test_command_validation.py** (23 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (16 connections) — `server/command_handler/catatonia_check.py`
- **_check_all_command_blocks()** (16 connections) — `server/command_handler_unified.py`
- **check_casting_state()** (12 connections) — `server/command_handler/command_guards.py`
- **_is_catatonic()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_load_player_for_catatonia_check()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_database()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_fetch_lucidity_record()** (8 connections) — `server/command_handler/catatonia_check.py`
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
- *... and 69 more nodes in this community*

## Relationships

- [command_handler_unified.py](command_handler_unified.py.md) (9 shared connections)
- [check_grace_period_block](check_grace_period_block.md) (9 shared connections)
- [command_guards.py](command_guards.py.md) (7 shared connections)
- [PlayerLucidity](PlayerLucidity.md) (5 shared connections)
- [get_cached_player](get_cached_player.md) (5 shared connections)
- [DatabaseManager](DatabaseManager.md) (3 shared connections)
- [TestHelperFunctions](TestHelperFunctions.md) (3 shared connections)
- [command_input.py](command_input.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (1 shared connections)
- [TestCheckRateLimit](TestCheckRateLimit.md) (1 shared connections)
- [TestValidateCommandBasics](TestValidateCommandBasics.md) (1 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/command_handler/command_guards.py`
- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 211 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*