# is_shutdown_pending

> 13 nodes

## Key Concepts

- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **test_is_shutdown_pending_false()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_true()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownContainerStub** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_no_state()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_AppWithoutState** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Check if server shutdown is currently pending. Args: app: FastAPI application…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test is_shutdown_pending() returns True when shutdown is pending.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test is_shutdown_pending() returns False when shutdown is not pending.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test is_shutdown_pending() returns False when app has no state.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **App double with no state attribute (is_shutdown_pending must return False).** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (10 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (3 shared connections)
- [admin_shutdown_command.py](admin_shutdown_command.py.md) (2 shared connections)
- [register_user](register_user.md) (1 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [User](User.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*