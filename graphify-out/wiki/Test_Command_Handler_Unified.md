# Test Command Handler Unified

> 40 nodes

## Key Concepts

- **test_command_handler_unified.py** (15 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **handle_command()** (12 connections) — `server/command_handler_unified.py`
- **CommandRequest** (9 connections) — `server/command_handler_unified.py`
- **asyncio** (7 connections)
- **TestProcessCommandUnified** (6 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **get_help_content()** (6 connections) — `server/command_handler_unified.py`
- **TestHandleCommand** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **TestLegacyFunctions** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_success()** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_unauthorized()** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_legacy()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_blocked()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_normal_processing()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_rate_limited()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_special_routing()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **test_command_request_rejects_unknown_field()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_get_help_content()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_get_help_content_none()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Depends** (1 connections)
- **get_current_user** (1 connections)
- **post** (1 connections)
- **Request** (1 connections)
- **User** (1 connections)
- **Handle incoming HTTP command requests.** (1 connections) — `server/command_handler_unified.py`
- **Get help content for commands. This is a compatibility function that delegates…** (1 connections) — `server/command_handler_unified.py`
- *... and 15 more nodes in this community*

## Relationships

- [Test Command Aliases](Test_Command_Aliases.md) (12 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (1 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (1 shared connections)
- [Correlation Middleware](Correlation_Middleware.md) (1 shared connections)
- [Command Aliases](Command_Aliases.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified.py`

## Audit Trail

- EXTRACTED: 70 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*