# admin setlucidity command

> 24 nodes

## Key Concepts

- **admin_setlucidity_command.py** (28 connections) — `server/commands/admin_setlucidity_command.py`
- **Any** (12 connections)
- **_execute_lucidity_change()** (11 connections) — `server/commands/admin_setlucidity_command.py`
- **_apply_lucidity_change()** (8 connections) — `server/commands/admin_setlucidity_command.py`
- **_setup_command_execution()** (7 connections) — `server/commands/admin_setlucidity_command.py`
- **_get_current_lcd()** (6 connections) — `server/commands/admin_setlucidity_command.py`
- **UUID** (6 connections)
- **_validate_command_context()** (6 connections) — `server/commands/admin_setlucidity_command.py`
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
- **Get catatonia registry from container, fallback to app.state for backward compat** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Resolve target player name to UUID, returning error message if not found.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Execute the lucidity change in database session.** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Validate command context and extract arguments, returning error if validation fa** (1 connections) — `server/commands/admin_setlucidity_command.py`
- **Setup command execution by checking permissions and resolving target player.** (1 connections) — `server/commands/admin_setlucidity_command.py`

## Relationships

- [Any](Any.md) (15 shared connections)
- [main()](main%28%29.md) (9 shared connections)
- [datetime](datetime.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (1 shared connections)

## Source Files

- `server/commands/admin_setlucidity_command.py`

## Audit Trail

- EXTRACTED: 113 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*