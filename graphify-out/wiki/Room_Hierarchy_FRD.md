# Room Hierarchy FRD

> 19 nodes · cohesion 0.13

## Key Concepts

- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_no_active()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_success()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_false()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_true()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownContainerStub** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_no_state()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_AppWithoutState** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Check if server shutdown is currently pending.      Args:         app: FastAPI a** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test is_shutdown_pending() returns True when shutdown is pending.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test is_shutdown_pending() returns False when shutdown is not pending.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test is_shutdown_pending() returns False when app has no state.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test cancel_shutdown_countdown() when no shutdown is active.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test cancel_shutdown_countdown() successfully cancels shutdown.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **App double with no state attribute (is_shutdown_pending must return False).** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [Logging Best Practices](Logging_Best_Practices.md) (12 shared connections)
- [Admin Shutdown Commands](Admin_Shutdown_Commands.md) (4 shared connections)
- [Player Effects API](Player_Effects_API.md) (3 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (2 shared connections)
- [WebSocket Player Helpers](WebSocket_Player_Helpers.md) (1 shared connections)
- [WebSocket Helper Utilities](WebSocket_Helper_Utilities.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 69 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*