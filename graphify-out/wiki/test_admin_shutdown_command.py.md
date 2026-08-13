# test_admin_shutdown_command.py

> 38 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (57 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **calculate_notification_times()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_success()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_supersedes()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_no_state()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_AppWithoutState** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_InitiateAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_InitiateStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_calculate_notification_times_long()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_calculate_notification_times_short()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_calculate_notification_times_sorted()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_character_creation()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_default()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_login()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_cancel()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_invalid_negative()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_invalid_string()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_invalid_zero()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_no_args()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_seconds()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Calculate notification times for countdown. Notifications occur: - Every 10…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Unit tests for admin shutdown command handler. Tests the shutdown command…** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test is_shutdown_pending() returns False when app has no state.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns login message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns character creation message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- *... and 13 more nodes in this community*

## Relationships

- [admin_shutdown_command.py](admin_shutdown_command.py.md) (16 shared connections)
- [_asyncio_mark](_asyncio_mark.md) (15 shared connections)
- [is_shutdown_pending](is_shutdown_pending.md) (11 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (4 shared connections)
- [validate_shutdown_admin_permission](validate_shutdown_admin_permission.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 98 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*