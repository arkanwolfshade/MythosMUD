# CharacterNameScreen

> 14 nodes

## Key Concepts

- **format_player_location()** (13 connections) — `server/commands/who_commands.py`
- **test_format_player_location_valid()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_invalid()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_none()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_short_format()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_non_string()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_invalid()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Format player location as Zone: Sub-zone: Room from room ID.      Args:** (1 connections) — `server/commands/who_commands.py`
- **Test formatting valid player location.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test formatting invalid player location.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test formatting None location.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test format_player_location() with short room ID format.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test format_player_location() with non-string input.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test format_player_location() handles invalid room ID.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`

## Relationships

- [utility commands](utility_commands.md) (6 shared connections)
- [Any](Any.md) (3 shared connections)
- [disconnect player connections()](disconnect_player_connections%28%29.md) (1 shared connections)
- [GameConfig](GameConfig.md) (1 shared connections)
- [test utility commands whoami](test_utility_commands_whoami.md) (1 shared connections)

## Source Files

- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`
- `server/tests/unit/commands/test_who_commands_helpers.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*