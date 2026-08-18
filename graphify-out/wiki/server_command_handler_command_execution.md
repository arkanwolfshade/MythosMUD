# server command handler command execution

> 82 nodes

## Key Concepts

- **command_handler_unified.py** (55 connections) — `server/command_handler_unified.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (19 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (17 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (15 connections) — `server/command_handler/command_execution_request.py`
- **Any** (13 connections)
- **test_command_handler_unified.py** (12 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **handle_command()** (11 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (9 connections)
- **test_grace_period_blocking.py** (9 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_command_aliases.py** (9 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **CommandRequest** (8 connections) — `server/command_handler_unified.py`
- **process_command()** (8 connections) — `server/command_handler_unified.py`
- **_get_grace_check_context()** (7 connections) — `server/command_handler_unified.py`
- **asyncio** (7 connections)
- **TestProcessCommandUnified** (6 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **_get_casting_block_result()** (6 connections) — `server/command_handler_unified.py`
- **get_help_content()** (6 connections) — `server/command_handler_unified.py`
- **TestHandleSpecialCommandRouting** (5 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestHandleCommand** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **TestLegacyFunctions** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_success()** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_unauthorized()** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- *... and 57 more nodes in this community*

## Relationships

- [server command handler unified check](server_command_handler_unified_check.md) (37 shared connections)
- [server command handler catatonia check](server_command_handler_catatonia_check.md) (21 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (6 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (5 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (5 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (4 shared connections)
- [server command handler command input](server_command_handler_command_input.md) (4 shared connections)
- [server command handler alias expansion](server_command_handler_alias_expansion.md) (4 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (4 shared connections)
- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (3 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler_unified.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`

## Audit Trail

- EXTRACTED: 250 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*