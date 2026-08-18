# server command handler unified check

> 119 nodes

## Key Concepts

- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **asyncio** (21 connections)
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (14 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **TestPrepareCommandForProcessing** (7 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **TestHandleSpecialCommandRouting** (6 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **TestValidateCommandBasics** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestEnsureAliasStorage** (5 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestCheckRateLimit** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_handle_special_command_routing_alias_command()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_handle_special_command_routing_alias_storage_none()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_handle_special_command_routing_emote_conversion()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_handle_special_command_routing_returns_none()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_all_command_blocks_casting()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_all_command_blocks_catatonia()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_all_command_blocks_grace_period()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_allowed_commands()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_error_handling()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_is_casting()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_no_magic_service()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_not_casting()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- *... and 94 more nodes in this community*

## Relationships

- [server command handler command execution](server_command_handler_command_execution.md) (37 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (5 shared connections)
- [server command handler catatonia check](server_command_handler_catatonia_check.md) (4 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (4 shared connections)
- [server command handler alias expansion](server_command_handler_alias_expansion.md) (3 shared connections)
- [server command handler command input](server_command_handler_command_input.md) (2 shared connections)
- [server tests unit validators test](server_tests_unit_validators_test.md) (2 shared connections)
- [server config init](server_config_init.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 229 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*