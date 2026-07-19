# Admin Shutdown Command

> 49 nodes · cohesion 0.07

## Key Concepts

- **test_admin_shutdown_command.py** (56 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **validate_shutdown_admin_permission()** (8 connections) — `server/commands/admin_shutdown_command.py`
- **calculate_notification_times()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_no_active()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_success()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_false()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_true()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownContainerStub** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_success()** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_supersedes()** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_no_state()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_AppWithoutState** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_InitiateAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_InitiateStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test validate_shutdown_admin_permission() returns False when player is None.** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_failure()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_success()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_calculate_notification_times_long()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_calculate_notification_times_short()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_calculate_notification_times_sorted()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- *... and 24 more nodes in this community*

## Relationships

- [[Admin Shutdown Commands]] (18 shared connections)
- [[Commands Admin Shutdown]] (18 shared connections)
- [[Character Creation API]] (7 shared connections)
- [[Argon2 Password Hashing]] (2 shared connections)
- [[WebSocket Player Helpers]] (2 shared connections)
- [[Alias Expansion Logic]] (2 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 205 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
