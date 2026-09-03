# Test Command Validation

> 75 nodes

## Key Concepts

- **asyncio** (24 connections)
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **test_command_validation.py** (17 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_check_all_command_blocks()** (15 connections) — `server/command_handler_unified.py`
- **TestCheckGracePeriodBlock** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCheckAllCommandBlocks** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCheckCastingState** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_casting()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_catatonia()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_grace_period()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_no_blocks()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_casting_state_allowed_command()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_casting_state_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_casting_state_no_magic_service()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_casting_state_player_casting()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_no_connection_manager()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_no_player_service()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_player_in_grace_period()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_player_not_found()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_allowed_command()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_no_app_state()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_uses_string_registry_key_when_player_id_not_uuid_or_str()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_not_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 50 more nodes in this community*

## Relationships

- [Command Guards](Command_Guards.md) (14 shared connections)
- [Test Command Handler Unified Helpers](Test_Command_Handler_Unified_Helpers.md) (6 shared connections)
- [Test Command Aliases](Test_Command_Aliases.md) (4 shared connections)
- [Test Command Validation](Test_Command_Validation.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Correlation Middleware](Correlation_Middleware.md) (1 shared connections)
- [Catatonia Check](Catatonia_Check.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 132 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*