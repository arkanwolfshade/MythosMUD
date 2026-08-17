# test_admin_shutdown_command.py

> 60 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (58 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_asyncio_mark** (19 connections)
- **_await_shutdown_result()** (14 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_no_active()** (7 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_success()** (7 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_success()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_supersedes()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_false()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_true()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownContainerStub** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_failure()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_success()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_cancel()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_cancel_no_active()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_failure()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_no_seconds()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_superseding()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_invalid_parameters()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_no_permission()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_no_player_service()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_admin()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_no_player()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_not_admin()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- *... and 35 more nodes in this community*

## Relationships

- [admin_shutdown_command.py](admin_shutdown_command.py.md) (16 shared connections)
- [User](User.md) (7 shared connections)
- [parse_shutdown_parameters](parse_shutdown_parameters.md) (7 shared connections)
- [calculate_notification_times](calculate_notification_times.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [test_is_shutdown_pending_no_state](test_is_shutdown_pending_no_state.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 144 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*