# handle_command

> 33 nodes

## Key Concepts

- **handle_command()** (13 connections) — `server/command_handler_unified.py`
- **CommandRequest** (8 connections) — `server/command_handler_unified.py`
- **asyncio** (7 connections)
- **TestProcessCommandUnified** (6 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **TestHandleCommand** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **TestLegacyFunctions** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_success()** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_unauthorized()** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_legacy()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_blocked()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_normal_processing()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_rate_limited()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_special_routing()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_get_help_content()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_get_help_content_none()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **BaseModel** (1 connections)
- **Depends** (1 connections)
- **post** (1 connections)
- **Request** (1 connections)
- **Handle incoming HTTP command requests.** (1 connections) — `server/command_handler_unified.py`
- **Request model for command processing.** (1 connections) — `server/command_handler_unified.py`
- **Test process_command_unified processes normal commands.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test handle_command HTTP endpoint.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test handle_command raises HTTPException when not authenticated.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test handle_command successfully processes command.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- *... and 8 more nodes in this community*

## Relationships

- [command_handler_unified.py](command_handler_unified.py.md) (15 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [User](User.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified.py`

## Audit Trail

- EXTRACTED: 56 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*