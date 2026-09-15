# admin_shutdown_command.py

> 34 nodes

## Key Concepts

- **admin_shutdown_command.py** (35 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **handle_shutdown_command()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **countdown_loop()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **_clear_shutdown_state()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_create_countdown_task()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_cancel()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_initiate()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_store_shutdown_data()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_validate_shutdown_context()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_broadcast_shutdown_cancellation()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_cancel_countdown_task()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_cancel_existing_shutdown_task()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_get_shutdown_services()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_get_shutdown_state()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_set_shutdown_pending_flag()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **Task** (2 connections)
- **Admin shutdown command for MythosMUD. This module provides the /shutdown…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Cancel existing shutdown task if present. Args: app: FastAPI application…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Set shutdown pending flag in container and app.state. Args: app: FastAPI…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Create countdown task from coroutine, handling task registry if available.…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Store shutdown data in container and app.state. Args: app: FastAPI application…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Clear shutdown state in container and app.state. Args: app: FastAPI application…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Main countdown loop that sends notifications and executes shutdown. Args: app:…** (1 connections) — `server/commands/admin_shutdown_command.py`
- *... and 9 more nodes in this community*

## Relationships

- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (12 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [broadcast_shutdown_notification](broadcast_shutdown_notification.md) (3 shared connections)
- [test_shutdown_sequence.py](test_shutdown_sequence.py.md) (3 shared connections)
- [parse_shutdown_parameters](parse_shutdown_parameters.md) (3 shared connections)
- [validate_shutdown_admin_permission](validate_shutdown_admin_permission.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [calculate_notification_times](calculate_notification_times.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [test_initiate_shutdown_countdown_success](test_initiate_shutdown_countdown_success.md) (2 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (2 shared connections)
- [_asyncio_mark](_asyncio_mark.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 100 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*