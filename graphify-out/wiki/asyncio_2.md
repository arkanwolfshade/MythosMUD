# asyncio

> 80 nodes

## Key Concepts

- **asyncio** (24 connections)
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_load_player_for_catatonia_check()** (10 connections) — `server/command_handler/catatonia_check.py`
- **TestCheckGracePeriodBlock** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCheckAllCommandBlocks** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCheckCastingState** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_PersistenceGetPlayerByName** (5 connections) — `server/command_handler/catatonia_check.py`
- **.test_check_catatonia_block_allowed_command()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_no_app_state()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_uses_string_registry_key_when_player_id_not_uuid_or_str()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_catatonic()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_catatonic()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_fetch_lucidity_record()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_load_player_for_catatonia_check_from_cache()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_load_player_for_catatonia_check_from_persistence()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_query_lucidity_record_success()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_casting()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_catatonia()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_grace_period()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_no_blocks()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_casting_state_allowed_command()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_casting_state_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_casting_state_no_magic_service()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 55 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (26 shared connections)
- [TestHelperFunctions](TestHelperFunctions.md) (13 shared connections)
- [get_cached_player](get_cached_player.md) (2 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 141 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*