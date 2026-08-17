# server commands admin shutdown command

> 9 nodes

## Key Concepts

- **validate_shutdown_admin_permission()** (9 connections) — `server/commands/admin_shutdown_command.py`
- **.is_admin()** (4 connections) — `server/commands/communication_commands_support.py`
- **test_validate_shutdown_admin_permission_admin()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_no_player()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_not_admin()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Validate that a player has admin permissions for server shutdown. Args: player:…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns False when player is None.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns False when player is not…** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns True when player is admin.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [server commands admin shutdown command](server_commands_admin_shutdown_command.md) (7 shared connections)
- [asyncio mark](asyncio_mark.md) (3 shared connections)
- [server commands communication commands flows](server_commands_communication_commands_flows.md) (1 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (1 shared connections)
- [server commands look npc](server_commands_look_npc.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 18 (86%)
- INFERRED: 3 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*