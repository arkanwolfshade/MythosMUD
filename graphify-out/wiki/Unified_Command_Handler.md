# Unified Command Handler

> 27 nodes · cohesion 0.08

## Key Concepts

- **CommandRequest** (11 connections) — `server/command_handler_unified.py`
- **TestProcessCommandUnified** (7 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **TestLegacyFunctions** (6 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **TestHandleCommand** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_success()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_unauthorized()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_get_help_content()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_get_help_content_none()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_legacy()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_blocked()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_normal_processing()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_rate_limited()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_special_routing()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **BaseModel** (1 connections)
- **Request model for command processing.** (1 connections) — `server/command_handler_unified.py`
- **Test process_command_unified processes normal commands.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test handle_command HTTP endpoint.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test handle_command raises HTTPException when not authenticated.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test handle_command successfully processes command.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test legacy compatibility functions.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test process_command() legacy function.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test get_help_content() delegates to help system.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test get_help_content() with None command.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test process_command_unified function.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test process_command_unified returns rate limit result.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- *... and 2 more nodes in this community*

## Relationships

- [Command Request App State](Command_Request_App_State.md) (15 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified.py`

## Audit Trail

- EXTRACTED: 65 (90%)
- INFERRED: 7 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*