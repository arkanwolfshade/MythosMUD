# test format player location invalid()

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

- [Any](Any.md) (4 shared connections)
- [get skill repository()](get_skill_repository%28%29.md) (3 shared connections)
- [Player Position Service](Player_Position_Service.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 21 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*