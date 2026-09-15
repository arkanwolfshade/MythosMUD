# handle_logout_command

> 40 nodes

## Key Concepts

- **handle_logout_command()** (26 connections) — `server/commands/logout_commands.py`
- **utility_commands.py** (20 connections) — `server/commands/utility_commands.py`
- **handle_quit_command()** (14 connections) — `server/commands/logout_commands.py`
- **TestLogoutCommand** (13 connections) — `server/tests/unit/commands/test_logout_command.py`
- **_is_player_in_combat_for_logout()** (8 connections) — `server/commands/logout_commands.py`
- **Any** (8 connections)
- **asyncio** (8 connections)
- **.test_logout_command_connection_error()** (5 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_general_error_handling()** (5 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_no_persistence()** (5 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_persistence_error()** (5 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_persists_position()** (5 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_player_not_found()** (5 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_success()** (5 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.test_logout_command_with_args()** (5 connections) — `server/tests/unit/commands/test_logout_command.py`
- **_get_app_services()** (4 connections) — `server/commands/logout_commands.py`
- **Request** (4 connections)
- **.mock_alias_storage()** (3 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.mock_current_user()** (3 connections) — `server/tests/unit/commands/test_logout_command.py`
- **.mock_request()** (3 connections) — `server/tests/unit/commands/test_logout_command.py`
- **test_logout_command.py** (3 connections) — `server/tests/unit/commands/test_logout_command.py`
- **fixture** (3 connections)
- **Player** (2 connections)
- **Check whether `player` is currently in combat, for the quit/logout combat…** (1 connections) — `server/commands/logout_commands.py`
- **Handle the quit command for disconnecting from the game. Args: command_data:…** (1 connections) — `server/commands/logout_commands.py`
- *... and 15 more nodes in this community*

## Relationships

- [test_logout_commands.py](test_logout_commands.py.md) (25 shared connections)
- [test_status_commands.py](test_status_commands.py.md) (3 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [handle_emote_command](handle_emote_command.md) (2 shared connections)
- [handle_time_command](handle_time_command.md) (2 shared connections)
- [format_player_entry](format_player_entry.md) (2 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (1 shared connections)
- [test_utility_commands_whoami.py](test_utility_commands_whoami.py.md) (1 shared connections)

## Source Files

- `server/commands/logout_commands.py`
- `server/commands/utility_commands.py`
- `server/tests/unit/commands/test_logout_command.py`

## Audit Trail

- EXTRACTED: 102 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*