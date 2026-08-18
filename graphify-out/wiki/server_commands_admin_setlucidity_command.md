# server commands admin setlucidity command

> 73 nodes

## Key Concepts

- **test_admin_setlucidity_command.py** (45 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- **admin_setlucidity_command.py** (31 connections) — `server/commands/admin_setlucidity_command.py`
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
- **test_check_admin_permissions_denied()** (3 connections) — `server/tests/unit/commands/test_admin_setlucidity_command.py`
- *... and 48 more nodes in this community*

## Relationships

- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (8 shared connections)
- [server models lucidity](server_models_lucidity.md) (7 shared connections)
- [server structured logging admin actions](server_structured_logging_admin_actions.md) (4 shared connections)
- [object](object.md) (4 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [aliaspayload](aliaspayload.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/commands/admin_setlucidity_command.py`
- `server/tests/unit/commands/test_admin_setlucidity_command.py`

## Audit Trail

- EXTRACTED: 192 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*