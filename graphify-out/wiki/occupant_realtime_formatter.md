# occupant realtime formatter

> 8 nodes

## Key Concepts

- **validate_shutdown_admin_permission()** (9 connections) — `server/commands/admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_no_player()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_not_admin()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_admin()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Validate that a player has admin permissions for server shutdown.      Args:** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns False when player is None.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns False when player is not admin** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns True when player is admin.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [shutdown admin command](shutdown_admin_command.md) (4 shared connections)
- [eventLog projectorRoom roomMergeUtils](eventLog_projectorRoom_roomMergeUtils.md) (3 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 21 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*