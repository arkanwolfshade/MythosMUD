# Who Command Tests

> 113 nodes · cohesion 0.03

## Key Concepts

- **test_who_commands.py** (47 connections) — `server/tests/unit/commands/test_who_commands.py`
- **utility_commands.py** (20 connections) — `server/commands/utility_commands.py`
- **who_commands.py** (16 connections) — `server/commands/who_commands.py`
- **filter_players_by_name()** (14 connections) — `server/commands/who_commands.py`
- **handle_who_command()** (14 connections) — `server/commands/who_commands.py`
- **parse_last_active_datetime()** (14 connections) — `server/commands/who_commands.py`
- **format_player_entry()** (13 connections) — `server/commands/who_commands.py`
- **format_player_location()** (13 connections) — `server/commands/who_commands.py`
- **test_who_commands_helpers.py** (12 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **filter_online_players()** (10 connections) — `server/commands/who_commands.py`
- **format_who_result()** (10 connections) — `server/commands/who_commands.py`
- **get_players_for_who()** (8 connections) — `server/commands/who_commands.py`
- **Any** (6 connections)
- **test_format_player_entry_error_handling()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_empty_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_filter_players_by_name_found()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_filter_players_by_name_not_found()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_entry()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_entry_admin()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_location_invalid()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_location_valid()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_filter_online_players_all_online()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_invalid_last_active()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_no_last_active()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_some_offline()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- *... and 88 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (3 shared connections)
- [Logout and Quit Commands](Logout_and_Quit_Commands.md) (3 shared connections)
- [Status Command Handlers](Status_Command_Handlers.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Commands Emote](Commands_Emote.md) (2 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (2 shared connections)
- [Commands Time](Commands_Time.md) (1 shared connections)
- [Logout Command Tests](Logout_Command_Tests.md) (1 shared connections)
- [Cursor Skills Overdrive](Cursor_Skills_Overdrive.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)

## Source Files

- `server/commands/utility_commands.py`
- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`
- `server/tests/unit/commands/test_who_commands_helpers.py`

## Audit Trail

- EXTRACTED: 384 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*