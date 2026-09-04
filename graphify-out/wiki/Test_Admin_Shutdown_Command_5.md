# Test Admin Shutdown Command

> 6 nodes

## Key Concepts

- **broadcast_shutdown_notification()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_failure()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_success()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Broadcast shutdown notification to all players. Args: connection_manager:…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test broadcast_shutdown_notification() successfully broadcasts.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test broadcast_shutdown_notification() handles errors.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [Test Admin Shutdown Command](Test_Admin_Shutdown_Command.md) (5 shared connections)
- [Admin Shutdown Command](Admin_Shutdown_Command.md) (3 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*