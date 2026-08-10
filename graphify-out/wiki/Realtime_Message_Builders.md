# Realtime Message Builders

> 9 nodes

## Key Concepts

- **validate_shutdown_admin_permission()** (9 connections) — `server/commands/admin_shutdown_command.py`
- **.is_admin()** (4 connections) — `server/commands/communication_commands_support.py`
- **test_validate_shutdown_admin_permission_no_player()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_not_admin()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_admin()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Validate that a player has admin permissions for server shutdown.      Args:** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns False when player is None.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns False when player is not admin** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns True when player is admin.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (4 shared connections)
- [Room Drop Renderer](Room_Drop_Renderer.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (1 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 22 (85%)
- INFERRED: 4 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*