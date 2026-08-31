# test_admin_shutdown_command.py

> 41 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (58 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **parse_shutdown_parameters()** (11 connections) — `server/commands/admin_shutdown_command.py`
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
- **test_parse_shutdown_parameters_cancel()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_invalid_negative()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_invalid_string()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_invalid_zero()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_no_args()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_seconds()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Check if server shutdown is currently pending. Args: app: FastAPI application…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Parse shutdown command parameters. Args: command_data: Command data dictionary…** (1 connections) — `server/commands/admin_shutdown_command.py`
- *... and 16 more nodes in this community*

## Relationships

- [_asyncio_mark](_asyncio_mark.md) (18 shared connections)
- [admin_shutdown_command.py](admin_shutdown_command.py.md) (13 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (7 shared connections)
- [calculate_notification_times](calculate_notification_times.md) (4 shared connections)
- [test_initiate_shutdown_countdown_success](test_initiate_shutdown_countdown_success.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 116 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*