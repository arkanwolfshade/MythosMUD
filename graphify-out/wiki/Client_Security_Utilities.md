# Client Security Utilities

> 31 nodes

## Key Concepts

- **admin_setlucidity_command.py** (30 connections) — `server/commands/admin_setlucidity_command.py`
- **Any** (12 connections)
- **_execute_lucidity_change()** (12 connections) — `server/commands/admin_setlucidity_command.py`
- **_handle_admin_set_lucidity_command()** (11 connections) — `server/commands/admin_setlucidity_command.py`
- **_setup_command_execution()** (7 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_current_lcd()** (6 connections) — `server/commands/admin_setlucidity_command.py`
- **_apply_lucidity_change()** (6 connections) — `server/commands/admin_setlucidity_command.py`
- **_validate_command_context()** (6 connections) — `server/commands/admin_setlucidity_command.py`
- **UUID** (5 connections)
- **LucidityChangeCtx** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **_log_lucidity_success()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_player_service_from_app()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **_resolve_target_player()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **_extract_command_args()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **_validate_lcd_value()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **_check_admin_permissions()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_catatonia_registry_from_app()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **Admin command to set player lucidity levels for testing.  This module provides** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Extract target_player and lcd_value from command_data.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Validate LCD value is integer and in valid range (-100 to 100).** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Check if current player is admin and return player object.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Get current LCD value from database, defaulting to 100 if no record exists.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Bundle for _apply_lucidity_change (lizard PARAM).** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Apply lucidity adjustment and return result message or None on error.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Get player service from container, fallback to app.state for backward compatibil** (1 connections) — `server/commands/admin_setlucidity_command.py`
- *... and 6 more nodes in this community*

## Relationships

- [Schemas Maps Map](Schemas_Maps_Map.md) (4 shared connections)
- [E2E Suite Overview](E2E_Suite_Overview.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (3 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (3 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (2 shared connections)
- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (2 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (2 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (1 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (1 shared connections)

## Source Files

- `server/commands/admin_setlucidity_command.py`

## Audit Trail

- EXTRACTED: 141 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*