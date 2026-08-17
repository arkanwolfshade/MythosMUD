# server command handler command execution

> 115 nodes

## Key Concepts

- **command_handler_unified.py** (55 connections) — `server/command_handler_unified.py`
- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **asyncio** (21 connections)
- **_check_casting_state()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (17 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (15 connections) — `server/command_handler/command_execution_request.py`
- **test_command_handler_unified_helpers.py** (14 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **Any** (13 connections)
- **test_command_handler_unified.py** (12 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (9 connections)
- **test_grace_period_blocking.py** (9 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_command_aliases.py** (9 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **process_command()** (8 connections) — `server/command_handler_unified.py`
- **_get_grace_check_context()** (7 connections) — `server/command_handler_unified.py`
- **TestHandleSpecialCommandRouting** (6 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_get_casting_block_result()** (6 connections) — `server/command_handler_unified.py`
- **get_help_content()** (6 connections) — `server/command_handler_unified.py`
- **test_check_grace_period_block_allows_commands_when_not_in_grace_period()** (4 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- *... and 90 more nodes in this community*

## Relationships

- [server command handler catatonia check](server_command_handler_catatonia_check.md) (22 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (21 shared connections)
- [server command handler unified commandrequest](server_command_handler_unified_commandrequest.md) (16 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (9 shared connections)
- [server command handler unified rationale](server_command_handler_unified_rationale.md) (8 shared connections)
- [server command handler alias expansion](server_command_handler_alias_expansion.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (6 shared connections)
- [server command handler command input](server_command_handler_command_input.md) (6 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (4 shared connections)
- [characterinfo](characterinfo.md) (4 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (3 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler_unified.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`

## Audit Trail

- EXTRACTED: 343 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*