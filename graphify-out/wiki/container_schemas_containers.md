# container schemas containers

> 28 nodes

## Key Concepts

- **admin_setlucidity_command.py** (29 connections) — `server/commands/admin_setlucidity_command.py`
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
- [admin structured logging](admin_structured_logging.md) (4 shared connections)
- [commands admin mute](commands_admin_mute.md) (3 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [command player state](command_player_state.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [commands whisper command](commands_whisper_command.md) (1 shared connections)
- [game models enums](game_models_enums.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [movement monitor game](movement_monitor_game.md) (1 shared connections)
- [models player related](models_player_related.md) (1 shared connections)

## Source Files

- `server/commands/admin_setlucidity_command.py`

## Audit Trail

- EXTRACTED: 131 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*