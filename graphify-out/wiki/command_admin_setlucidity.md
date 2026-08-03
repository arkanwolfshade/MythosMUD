# command admin setlucidity

> 28 nodes

## Key Concepts

- **admin_setlucidity_command.py** (28 connections) — `server/commands/admin_setlucidity_command.py`
- **Any** (12 connections)
- **_execute_lucidity_change()** (11 connections) — `server/commands/admin_setlucidity_command.py`
- **_handle_admin_set_lucidity_command()** (11 connections) — `server/commands/admin_setlucidity_command.py`
- **_apply_lucidity_change()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_setup_command_execution()** (7 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_current_lcd()** (6 connections) — `server/commands/admin_setlucidity_command.py`
- **UUID** (6 connections)
- **_validate_command_context()** (6 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_player_service_from_app()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **_resolve_target_player()** (5 connections) — `server/commands/admin_setlucidity_command.py`
- **_extract_command_args()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **_validate_lcd_value()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **_check_admin_permissions()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_catatonia_registry_from_app()** (4 connections) — `server/commands/admin_setlucidity_command.py`
- **Admin command to set player lucidity levels for testing.  This module provides t** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Extract target_player and lcd_value from command_data.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Validate LCD value is integer and in valid range (-100 to 100).** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Check if current player is admin and return player object.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Get current LCD value from database, defaulting to 100 if no record exists.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Apply lucidity adjustment and return result message or None on error.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Get player service from container, fallback to app.state for backward compatibil** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Get catatonia registry from container, fallback to app.state for backward compat** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Resolve target player name to UUID, returning error message if not found.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Execute the lucidity change in database session.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- *... and 3 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (6 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (5 shared connections)
- [combat services turn](combat_services_turn.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [npc populate databases](npc_populate_databases.md) (3 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/commands/admin_setlucidity_command.py`

## Audit Trail

- EXTRACTED: 130 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*