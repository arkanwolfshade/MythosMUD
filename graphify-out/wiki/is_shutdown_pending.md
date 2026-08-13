# is_shutdown_pending

> 15 nodes

## Key Concepts

- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_no_active()** (7 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_success()** (7 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_false()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_true()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownContainerStub** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Check if server shutdown is currently pending. Args: app: FastAPI application…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test is_shutdown_pending() returns True when shutdown is pending.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test is_shutdown_pending() returns False when shutdown is not pending.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test cancel_shutdown_countdown() when no shutdown is active.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test cancel_shutdown_countdown() successfully cancels shutdown.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (11 shared connections)
- [admin_shutdown_command.py](admin_shutdown_command.py.md) (4 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (3 shared connections)
- [User](User.md) (2 shared connections)
- [_asyncio_mark](_asyncio_mark.md) (2 shared connections)
- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*