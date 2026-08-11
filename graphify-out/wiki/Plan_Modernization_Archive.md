# Plan Modernization Archive

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

- [Combat UUID Display Bug](Combat_UUID_Display_Bug.md) (5 shared connections)
- [Realtime Health Monitor](Realtime_Health_Monitor.md) (3 shared connections)
- [Legacy Cleanup Summary](Legacy_Cleanup_Summary.md) (2 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (1 shared connections)
- [Exploration Command Factory](Exploration_Command_Factory.md) (1 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (1 shared connections)

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