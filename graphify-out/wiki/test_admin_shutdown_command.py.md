# test_admin_shutdown_command.py

> 29 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (57 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **cancel_shutdown_countdown()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_no_active()** (7 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_success()** (7 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_false()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_true()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownContainerStub** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_no_state()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_AppWithoutState** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_character_creation()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_default()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_login()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Check if server shutdown is currently pending. Args: app: FastAPI application…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Cancel active shutdown countdown. Args: app: FastAPI application instance…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Unit tests for admin shutdown command handler. Tests the shutdown command…** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test is_shutdown_pending() returns True when shutdown is pending.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test is_shutdown_pending() returns False when shutdown is not pending.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test is_shutdown_pending() returns False when app has no state.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns login message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns character creation message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- *... and 4 more nodes in this community*

## Relationships

- [_asyncio_mark](_asyncio_mark.md) (15 shared connections)
- [admin_shutdown_command.py](admin_shutdown_command.py.md) (13 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (7 shared connections)
- [parse_shutdown_parameters](parse_shutdown_parameters.md) (7 shared connections)
- [calculate_notification_times](calculate_notification_times.md) (4 shared connections)
- [validate_shutdown_admin_permission](validate_shutdown_admin_permission.md) (4 shared connections)
- [test_initiate_shutdown_countdown_success](test_initiate_shutdown_countdown_success.md) (4 shared connections)
- [User](User.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 107 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*