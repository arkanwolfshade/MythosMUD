# logout command commands

> 22 nodes

## Key Concepts

- **_await_shutdown_result()** (14 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_no_player_service()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_no_permission()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_invalid_parameters()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_cancel()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_cancel_no_active()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_superseding()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_no_seconds()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_failure()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Await handle_shutdown_command; explicit return keeps test assertions typed as di** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() when player service is not available.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() when player is not found.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() when player lacks admin permission.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with invalid parameters.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with cancel action.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with cancel when no active shutdown.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with initiate action.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with initiate action superseding existing shutdow** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with initiate action but no seconds.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() with initiate action that fails.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [shutdown admin command](shutdown_admin_command.md) (11 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (1 shared connections)
- [eventLog projectorRoom roomMergeUtils](eventLog_projectorRoom_roomMergeUtils.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 55 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*