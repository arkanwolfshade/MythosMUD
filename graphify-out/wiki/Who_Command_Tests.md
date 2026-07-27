# Who Command Tests

> 52 nodes · cohesion 0.07

## Key Concepts

- **test_who_commands.py** (46 connections) — `server/tests/unit/commands/test_who_commands.py`
- **who_commands.py** (14 connections) — `server/commands/who_commands.py`
- **parse_last_active_datetime()** (14 connections) — `server/commands/who_commands.py`
- **handle_who_command()** (13 connections) — `server/commands/who_commands.py`
- **filter_online_players()** (10 connections) — `server/commands/who_commands.py`
- **format_who_result()** (10 connections) — `server/commands/who_commands.py`
- **get_players_for_who()** (8 connections) — `server/commands/who_commands.py`
- **Test parse_last_active_datetime with None.** (6 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Any** (6 connections) — `server/commands/who_commands.py`
- **test_filter_online_players_all_online()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_invalid_last_active()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_no_last_active()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_some_offline()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_who_result_no_players()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_who_result_no_players_with_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_who_result_with_players()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_who_result_with_players_and_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_get_players_for_who_no_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_get_players_for_who_with_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_error_handling()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_no_players()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_with_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_datetime_aware()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_datetime_naive()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- *... and 27 more nodes in this community*

## Relationships

- [[Who Command Helpers]] (22 shared connections)
- [[Admin Status Commands]] (2 shared connections)
- [[Alias Expansion Logic]] (2 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Whisper Reply Command Tests]] (1 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)
- [[Player Domain Model]] (1 shared connections)

## Source Files

- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`

## Audit Trail

- EXTRACTED: 219 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
