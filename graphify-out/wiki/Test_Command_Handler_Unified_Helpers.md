# Test Command Handler Unified Helpers

> 88 nodes

## Key Concepts

- **TestHelperFunctions** (32 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **asyncio** (21 connections)
- **_prepare_command_for_processing()** (18 connections) — `server/command_handler_unified.py`
- **_ensure_alias_storage()** (12 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (11 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_check_rate_limit()** (9 connections) — `server/command_handler_unified.py`
- **TestPrepareCommandForProcessing** (7 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **TestEnsureAliasStorage** (5 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestCheckRateLimit** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_all_command_blocks_casting()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_all_command_blocks_catatonia()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_all_command_blocks_grace_period()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_process_alias_expansion_invalid_expanded()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_process_alias_expansion_no_alias()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_process_alias_expansion_no_storage()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_process_alias_expansion_unsafe_alias()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **test_command_preparation.py** (4 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_ensure_alias_storage_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_ensure_alias_storage_initializes_new()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_ensure_alias_storage_returns_existing()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_check_casting_state_allowed_commands()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_error_handling()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_is_casting()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_no_magic_service()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_not_casting()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- *... and 63 more nodes in this community*

## Relationships

- [Test Command Aliases](Test_Command_Aliases.md) (20 shared connections)
- [Test Command Validation](Test_Command_Validation.md) (12 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 158 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*