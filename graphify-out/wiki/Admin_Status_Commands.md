# Admin Status Commands

> 36 nodes

## Key Concepts

- **_handle_admin_set_stat_command()** (33 connections) — `server/commands/admin_setstat_command.py`
- **test_admin_setstat_command.py** (21 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_success_str()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_success_all_stat_types()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_invalid_stat_name()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_invalid_value()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_value_out_of_range()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_mp_above_maximum()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_non_admin_denied()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_target_player_not_found()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_missing_stat_name()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_missing_target_player()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_missing_value()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_no_app_context()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_no_user_manager()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_no_player_service()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_logging()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Handle the admin set command to set a player's statistic.      Usage: admin set** (1 connections) — `server/commands/admin_setstat_command.py`
- **Unit tests for admin set stat command handler.  Tests the admin set command hand** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Test successful setting of STR stat.** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Test successful setting of various stat types.** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Test invalid stat name handling.** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Test invalid value (non-integer) handling.** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Test value out of range (warn but allow).** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- *... and 11 more nodes in this community*

## Relationships

- [Combat Messaging Tests](Combat_Messaging_Tests.md) (7 shared connections)
- [Archive Effects System](Archive_Effects_System.md) (3 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (2 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (2 shared connections)
- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (2 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/tests/unit/commands/test_admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 119 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*