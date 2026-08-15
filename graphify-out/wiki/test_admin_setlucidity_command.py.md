# test_admin_setlucidity_command.py

> 75 nodes

## Key Concepts

- **test_admin_setlucidity_command.py** (44 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **admin_setlucidity_command.py** (31 connections) — `server/commands/admin_setlucidity_command.py`
- **get_admin_actions_logger()** (27 connections) — `server/structured_logging/admin_actions_logger.py`
- **asyncio** (24 connections)
- **_handle_admin_set_lucidity_command()** (17 connections) — `server/commands/admin_setlucidity_command.py`
- **_execute_lucidity_change()** (14 connections) — `server/commands/admin_setlucidity_command.py`
- **Any** (12 connections)
- **LucidityChangeCtx** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_apply_lucidity_change()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_check_admin_permissions()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_extract_command_args()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_resolve_target_player()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_setup_command_execution()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_validate_command_context()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_validate_lcd_value()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_catatonia_registry_from_app()** (7 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_current_lcd()** (7 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_player_service_from_app()** (7 connections) — `server/commands/admin_setlucidity_command.py`
- **_log_lucidity_success()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **test_apply_lucidity_change_adjustment_error()** (5 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **test_apply_lucidity_change_admin_logger_failure()** (5 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **test_apply_lucidity_change_success()** (5 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **UUID** (5 connections)
- **test_execute_lucidity_change_success()** (4 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **test_check_admin_permissions_current_player_missing()** (3 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- *... and 50 more nodes in this community*

## Relationships

- [Player](Player.md) (7 shared connections)
- [DatabaseError](DatabaseError.md) (6 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (5 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (5 shared connections)
- [test_goto_helpers.py](test_goto_helpers.py.md) (4 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (4 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (4 shared connections)
- [test_admin_teleport_commands.py](test_admin_teleport_commands.py.md) (3 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [validate_admin_permission](validate_admin_permission.md) (2 shared connections)
- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (2 shared connections)

## Source Files

- `server/commands/admin_setlucidity_command.py`
- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/commands/test_admin_setlucidity_command.py`

## Audit Trail

- EXTRACTED: 215 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*