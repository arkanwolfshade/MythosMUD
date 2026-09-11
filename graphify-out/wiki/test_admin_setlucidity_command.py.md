# test_admin_setlucidity_command.py

> 76 nodes

## Key Concepts

- **test_admin_setlucidity_command.py** (44 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **admin_setlucidity_command.py** (36 connections) — `server/commands/admin_setlucidity_command.py`
- **asyncio** (24 connections)
- **_handle_admin_set_lucidity_command()** (17 connections) — `server/commands/admin_setlucidity_command.py`
- **_execute_lucidity_change()** (14 connections) — `server/commands/admin_setlucidity_command.py`
- **LucidityUpdateResult** (12 connections) — `server/services/lucidity_helpers.py`
- **check_admin_permissions()** (10 connections) — `server/commands/admin_setlucidity_command.py`
- **get_player_service_from_app()** (10 connections) — `server/commands/admin_setlucidity_command.py`
- **resolve_target_player()** (10 connections) — `server/commands/admin_setlucidity_command.py`
- **get_current_lcd()** (9 connections) — `server/commands/admin_setlucidity_command.py`
- **Any** (9 connections)
- **LucidityChangeCtx** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_apply_lucidity_change()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_extract_command_args()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_catatonia_registry_from_app()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_setup_command_execution()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_validate_command_context()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_validate_lcd_value()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_log_lucidity_success()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **test_apply_lucidity_change_adjustment_error()** (5 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **test_apply_lucidity_change_admin_logger_failure()** (5 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **test_apply_lucidity_change_success()** (5 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **UUID** (5 connections)
- **test_execute_lucidity_change_success()** (4 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **test_check_admin_permissions_current_player_missing()** (3 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- *... and 51 more nodes in this community*

## Relationships

- [admin_hallucinate_command.py](admin_hallucinate_command.py.md) (12 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [Player](Player.md) (7 shared connections)
- [LucidityService](LucidityService.md) (4 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (4 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (3 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (3 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [CatatoniaObserverProtocol](CatatoniaObserverProtocol.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [admin_commands.py](admin_commands.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)

## Source Files

- `server/commands/admin_setlucidity_command.py`
- `server/services/lucidity_helpers.py`
- `server/tests/unit/commands/test_admin_setlucidity_command.py`

## Audit Trail

- EXTRACTED: 212 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*