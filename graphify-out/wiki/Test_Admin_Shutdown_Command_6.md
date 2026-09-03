# Test Admin Shutdown Command

> 6 nodes

## Key Concepts

- **validate_shutdown_admin_permission()** (8 connections) — `server/commands/admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_no_player()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_not_admin()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Validate that a player has admin permissions for server shutdown. Args: player:…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns False when player is None.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns False when player is not…** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [Test Admin Shutdown Command](Test_Admin_Shutdown_Command.md) (6 shared connections)
- [Admin Shutdown Command](Admin_Shutdown_Command.md) (3 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*