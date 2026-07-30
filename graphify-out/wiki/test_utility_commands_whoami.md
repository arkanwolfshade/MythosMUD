# test utility commands whoami

> 12 nodes

## Key Concepts

- **format_player_entry()** (13 connections) — `server/commands/who_commands.py`
- **test_format_player_entry_error_handling()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_entry_basic()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_entry_admin()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_entry_missing_attributes()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_entry()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Format a single player entry for the who command output.      Args:         play** (1 connections) — `server/commands/who_commands.py`
- **Test formatting basic player entry.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test formatting admin player entry.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test formatting player entry with missing attributes.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test format_player_entry() handles errors gracefully.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test format_player_entry() formats player entry.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`

## Relationships

- [utility commands](utility_commands.md) (5 shared connections)
- [Any](Any.md) (3 shared connections)
- [GameConfig](GameConfig.md) (2 shared connections)
- [disconnect player connections()](disconnect_player_connections%28%29.md) (1 shared connections)
- [CharacterNameScreen](CharacterNameScreen.md) (1 shared connections)
- [create access token()](create_access_token%28%29.md) (1 shared connections)

## Source Files

- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`
- `server/tests/unit/commands/test_who_commands_helpers.py`

## Audit Trail

- EXTRACTED: 34 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*