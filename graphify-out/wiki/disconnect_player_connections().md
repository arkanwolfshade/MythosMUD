# disconnect player connections()

> 136 nodes

## Key Concepts

- **test_logout_commands.py** (42 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **handle_logout_command()** (26 connections) — `server/commands/logout_commands.py`
- **logout_commands.py** (20 connections) — `server/commands/logout_commands.py`
- **utility_commands.py** (20 connections) — `server/commands/utility_commands.py`
- **test_logout_commands_helpers.py** (15 connections) — `server/tests/unit/commands/test_logout_commands_helpers.py`
- **_get_player_position_from_connection_manager()** (14 connections) — `server/commands/logout_commands.py`
- **_get_player_for_logout()** (13 connections) — `server/commands/logout_commands.py`
- **TestLogoutCommand** (13 connections) — `server/tests/unit/commands/test_logout_command.py`
- **_clear_corrupted_cache_entry()** (12 connections) — `server/commands/logout_commands.py`
- **_sync_player_position()** (12 connections) — `server/commands/logout_commands.py`
- **handle_quit_command()** (11 connections) — `server/commands/logout_commands.py`
- **Any** (8 connections)
- **_disconnect_player_connections()** (8 connections) — `server/commands/logout_commands.py`
- **Any** (8 connections)
- **_update_and_save_player_last_active()** (7 connections) — `server/commands/logout_commands.py`
- **.test_logout_command_success()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_persists_position()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_persistence_error()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_connection_error()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_with_args()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_general_error_handling()** (4 connections) — `server/tests/unit/commands/test_logout_command.py`
- **test_logout_command.py** (3 connections) — `server/tests/unit/commands/test_logout_command.py`
- **test_clear_corrupted_cache_entry_with_cache()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- *... and 111 more nodes in this community*

## Relationships

- [Any](Any.md) (6 shared connections)
- [.add alias()](add_alias%28%29.md) (5 shared connections)
- [Player Position Service](Player_Position_Service.md) (5 shared connections)
- [logging utilities](logging_utilities.md) (3 shared connections)
- [GameConfig](GameConfig.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [get health status()](get_health_status%28%29.md) (2 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)
- [handle global command()](handle_global_command%28%29.md) (1 shared connections)
- [test utility commands whoami](test_utility_commands_whoami.md) (1 shared connections)
- [CharacterNameScreen](CharacterNameScreen.md) (1 shared connections)
- [skills commands](skills_commands.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/commands/utility_commands.py`
- `server/tests/unit/commands/test_logout_command.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/commands/test_logout_commands_helpers.py`

## Audit Trail

- EXTRACTED: 439 (96%)
- INFERRED: 20 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*