# test_admin_shutdown_command.py

> 47 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (58 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_asyncio_mark** (19 connections)
- **_await_shutdown_result()** (14 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_success()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_supersedes()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
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
- **_InitiateAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_InitiateStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_character_creation()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_default()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_login()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- *... and 22 more nodes in this community*

## Relationships

- [admin_shutdown_command.py](admin_shutdown_command.py.md) (14 shared connections)
- [is_shutdown_pending](is_shutdown_pending.md) (14 shared connections)
- [parse_shutdown_parameters](parse_shutdown_parameters.md) (7 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (4 shared connections)
- [calculate_notification_times](calculate_notification_times.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 124 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*