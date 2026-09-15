# format_player_entry

> 38 nodes

## Key Concepts

- **format_player_entry()** (13 connections) — `server/commands/who_commands.py`
- **format_player_location()** (13 connections) — `server/commands/who_commands.py`
- **test_who_commands_helpers.py** (12 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_entry_error_handling()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_empty_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_filter_players_by_name_found()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_filter_players_by_name_not_found()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_entry()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_entry_admin()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_location_invalid()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_location_valid()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_entry_admin()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_entry_basic()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_entry_missing_attributes()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_invalid()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_non_string()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_none()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_short_format()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_valid()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Format player location as Zone: Sub-zone: Room from room ID. Args: room_id:…** (1 connections) — `server/commands/who_commands.py`
- **Format a single player entry for the who command output. Args: player: Player…** (1 connections) — `server/commands/who_commands.py`
- **Unit tests for who command helper functions. Tests the helper functions in…** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Test filter_players_by_name() filters players by name.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Test filter_players_by_name() returns empty list when no matches.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Test filter_players_by_name() returns all players when filter is empty.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- *... and 13 more nodes in this community*

## Relationships

- [test_who_commands.py](test_who_commands.py.md) (19 shared connections)
- [handle_logout_command](handle_logout_command.md) (2 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (1 shared connections)

## Source Files

- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`
- `server/tests/unit/commands/test_who_commands_helpers.py`

## Audit Trail

- EXTRACTED: 63 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*