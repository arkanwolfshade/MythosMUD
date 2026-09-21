# handle_command

> 24 nodes

## Key Concepts

- **handle_command()** (13 connections) — `server/command_handler_unified.py`
- **CommandRequest** (9 connections) — `server/command_handler_unified.py`
- **asyncio** (7 connections)
- **get_help_content()** (6 connections) — `server/command_handler_unified.py`
- **TestLegacyFunctions** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_success()** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_unauthorized()** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_legacy()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **test_command_request_rejects_unknown_field()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_get_help_content()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_get_help_content_none()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Depends** (1 connections)
- **post** (1 connections)
- **Request** (1 connections)
- **Handle incoming HTTP command requests.** (1 connections) — `server/command_handler_unified.py`
- **Get help content for commands. This is a compatibility function that delegates…** (1 connections) — `server/command_handler_unified.py`
- **Request model for command processing.** (1 connections) — `server/command_handler_unified.py`
- **Test handle_command raises HTTPException when not authenticated.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test handle_command successfully processes command.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **#755: CommandRequest inherits SecureBaseModel - an extra field must be rejected.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test legacy compatibility functions.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test process_command() legacy function.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test get_help_content() delegates to help system.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test get_help_content() with None command.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`

## Relationships

- [User](User.md) (9 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (9 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (1 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified.py`

## Audit Trail

- EXTRACTED: 46 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*