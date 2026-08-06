# shutdown admin command

> 49 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (57 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **test_is_shutdown_pending_true()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_false()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_no_active()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_success()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownContainerStub** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_no_state()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_AppWithoutState** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_login()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_character_creation()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_default()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_no_player()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_not_admin()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_validate_shutdown_admin_permission_admin()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_success()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_failure()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_no_args()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_cancel()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_seconds()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_invalid_negative()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- *... and 24 more nodes in this community*

## Relationships

- [eventLog projectorRoom roomMergeUtils](eventLog_projectorRoom_roomMergeUtils.md) (22 shared connections)
- [logout command commands](logout_command_commands.md) (11 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (7 shared connections)
- [lucidity models rationale](lucidity_models_rationale.md) (4 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (4 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (1 shared connections)
- [room websocket updates](room_websocket_updates.md) (1 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 183 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*