# format_player_entry

> 24 nodes

## Key Concepts

- **format_player_entry()** (13 connections) — `server/commands/who_commands.py`
- **test_who_commands_helpers.py** (12 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_entry_error_handling()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_empty_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_filter_players_by_name_found()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_filter_players_by_name_not_found()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_entry()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_entry_admin()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_location_valid()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_entry_admin()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_entry_basic()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_entry_missing_attributes()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Format a single player entry for the who command output. Args: player: Player…** (1 connections) — `server/commands/who_commands.py`
- **Unit tests for who command helper functions. Tests the helper functions in…** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Test filter_players_by_name() filters players by name.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Test filter_players_by_name() returns empty list when no matches.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Test filter_players_by_name() returns all players when filter is empty.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Test format_player_location() formats valid room ID.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Test format_player_entry() formats player entry.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Test format_player_entry() includes admin indicator.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Test formatting basic player entry.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test formatting admin player entry.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test formatting player entry with missing attributes.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test format_player_entry() handles errors gracefully.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`

## Relationships

- [who_commands.py](who_commands.py.md) (7 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (5 shared connections)
- [format_player_location](format_player_location.md) (4 shared connections)
- [utility_commands.py](utility_commands.py.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`
- `server/tests/unit/commands/test_who_commands_helpers.py`

## Audit Trail

- EXTRACTED: 42 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*