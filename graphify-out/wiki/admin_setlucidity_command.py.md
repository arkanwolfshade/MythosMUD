# admin_setlucidity_command.py

> 29 nodes

## Key Concepts

- **admin_setlucidity_command.py** (30 connections) — `server/commands/admin_setlucidity_command.py`
- **Any** (12 connections)
- **_execute_lucidity_change()** (11 connections) — `server/commands/admin_setlucidity_command.py`
- **_setup_command_execution()** (7 connections) — `server/commands/admin_setlucidity_command.py`
- **_validate_command_context()** (6 connections) — `server/commands/admin_setlucidity_command.py`
- **LucidityChangeCtx** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **_apply_lucidity_change()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_current_lcd()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **_log_lucidity_success()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **_resolve_target_player()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **UUID** (5 connections)
- **_check_admin_permissions()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **_extract_command_args()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_catatonia_registry_from_app()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_player_service_from_app()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **_validate_lcd_value()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **Admin command to set player lucidity levels for testing. This module provides…** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Bundle for _apply_lucidity_change (lizard PARAM).** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Apply lucidity adjustment and return result message or None on error.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Get player service from container, fallback to app.state for backward…** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Get catatonia registry from container, fallback to app.state for backward…** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Resolve target player name to UUID, returning error message if not found.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Execute the lucidity change in database session.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Validate command context and extract arguments, returning error if validation…** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Setup command execution by checking permissions and resolving target player.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- *... and 4 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (9 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [LucidityService](LucidityService.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [.get_instance](get_instance.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_setlucidity_command.py`

## Audit Trail

- EXTRACTED: 129 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*