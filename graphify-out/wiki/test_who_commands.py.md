# test_who_commands.py

> 74 nodes

## Key Concepts

- **test_who_commands.py** (47 connections) — `server/tests/unit/commands/test_who_commands.py`
- **who_commands.py** (16 connections) — `server/commands/who_commands.py`
- **filter_players_by_name()** (14 connections) — `server/commands/who_commands.py`
- **handle_who_command()** (14 connections) — `server/commands/who_commands.py`
- **parse_last_active_datetime()** (14 connections) — `server/commands/who_commands.py`
- **filter_online_players()** (10 connections) — `server/commands/who_commands.py`
- **format_who_result()** (10 connections) — `server/commands/who_commands.py`
- **asyncio** (9 connections)
- **get_players_for_who()** (8 connections) — `server/commands/who_commands.py`
- **Any** (6 connections)
- **test_filter_online_players_all_online()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_invalid_last_active()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_no_last_active()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_some_offline()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_error_handling()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_no_players()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_success()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_with_filter()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_case_insensitive()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_exact_match()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_no_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_partial_match()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_who_result_no_players()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_who_result_no_players_with_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- *... and 49 more nodes in this community*

## Relationships

- [format_player_entry](format_player_entry.md) (19 shared connections)
- [handle_logout_command](handle_logout_command.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)

## Source Files

- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`

## Audit Trail

- EXTRACTED: 151 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*