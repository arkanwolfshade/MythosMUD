# Test Admin Shutdown Command

> 25 nodes

## Key Concepts

- **_asyncio_mark** (19 connections)
- **_await_shutdown_result()** (14 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_cancel()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_cancel_no_active()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_failure()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_no_seconds()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_superseding()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_invalid_parameters()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_no_permission()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_no_player_service()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_admin()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() when player service is not available.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() when player is not found.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() when player lacks admin permission.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with invalid parameters.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with cancel action.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with cancel when no active shutdown.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with initiate action.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with initiate action superseding existing…** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with initiate action but no seconds.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with initiate action that fails.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Await handle_shutdown_command; explicit return keeps test assertions typed as…** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns True when player is admin.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [Test Admin Shutdown Command](Test_Admin_Shutdown_Command.md) (21 shared connections)
- [Admin Shutdown Command](Admin_Shutdown_Command.md) (1 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 56 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*