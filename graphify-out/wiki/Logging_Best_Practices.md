# Logging Best Practices

> 40 nodes · cohesion 0.07

## Key Concepts

- **test_admin_shutdown_command.py** (57 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_await_shutdown_result()** (14 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_success()** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_supersedes()** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_InitiateAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_InitiateStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_failure()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_success()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_cancel()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_cancel_no_active()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_failure()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_no_seconds()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_superseding()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_invalid_parameters()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_no_permission()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_no_player_service()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_admin()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_no_player()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_not_admin()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Unit tests for admin shutdown command handler.  Tests the shutdown command funct** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() when player service is not available.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() when player is not found.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test handle_shutdown_command() when player lacks admin permission.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- *... and 15 more nodes in this community*

## Relationships

- [Admin Shutdown Commands](Admin_Shutdown_Commands.md) (14 shared connections)
- [Room Hierarchy FRD](Room_Hierarchy_FRD.md) (12 shared connections)
- [Dual Connection Implementation Tasks](Dual_Connection_Implementation_Tasks.md) (7 shared connections)
- [Summary E 2 E Remaining](Summary_E_2_E_Remaining.md) (4 shared connections)
- [Contributing Ai Development](Contributing_Ai_Development.md) (4 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 151 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*