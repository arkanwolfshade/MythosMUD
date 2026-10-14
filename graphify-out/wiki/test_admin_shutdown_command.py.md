# test_admin_shutdown_command.py

> 126 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (57 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **admin_shutdown_command.py** (40 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **_asyncio_mark** (19 connections)
- **handle_shutdown_command()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **_await_shutdown_result()** (14 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **cancel_shutdown_countdown()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **parse_shutdown_parameters()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **broadcast_shutdown_notification()** (9 connections) — `server/commands/admin_shutdown_command.py`
- **validate_shutdown_admin_permission()** (8 connections) — `server/commands/admin_shutdown_command.py`
- **calculate_notification_times()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **countdown_loop()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_no_active()** (7 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_success()** (7 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_broadcast_shutdown_cancellation()** (6 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_initiate()** (6 connections) — `server/commands/admin_shutdown_command.py`
- **_validate_shutdown_context()** (6 connections) — `server/commands/admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_success()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_supersedes()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_false()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_true()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownContainerStub** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_clear_shutdown_state()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_create_countdown_task()** (5 connections) — `server/commands/admin_shutdown_command.py`
- *... and 101 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (11 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (5 shared connections)
- [command_error](command_error.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_shutdown_sequence.py](test_shutdown_sequence.py.md) (3 shared connections)
- [alias_storage.py](alias_storage.py.md) (3 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [MessageCategory](MessageCategory.md) (2 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 276 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*