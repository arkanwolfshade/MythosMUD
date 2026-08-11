# Combat UUID Display Bug

> 113 nodes

## Key Concepts

- **test_who_commands.py** (47 connections) — `server/tests/unit/commands/test_who_commands.py`
- **utility_commands.py** (20 connections) — `server/commands/utility_commands.py`
- **who_commands.py** (16 connections) — `server/commands/who_commands.py`
- **filter_players_by_name()** (14 connections) — `server/commands/who_commands.py`
- **parse_last_active_datetime()** (14 connections) — `server/commands/who_commands.py`
- **handle_who_command()** (14 connections) — `server/commands/who_commands.py`
- **format_player_location()** (13 connections) — `server/commands/who_commands.py`
- **format_player_entry()** (13 connections) — `server/commands/who_commands.py`
- **test_who_commands_helpers.py** (12 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **filter_online_players()** (10 connections) — `server/commands/who_commands.py`
- **format_who_result()** (10 connections) — `server/commands/who_commands.py`
- **get_players_for_who()** (8 connections) — `server/commands/who_commands.py`
- **Any** (6 connections)
- **test_format_player_entry_error_handling()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_no_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_exact_match()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_partial_match()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_case_insensitive()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_valid()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_invalid()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_none()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_entry_basic()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_entry_admin()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_entry_missing_attributes()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_none()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- *... and 88 more nodes in this community*

## Relationships

- [Chat NATS Publisher](Chat_NATS_Publisher.md) (3 shared connections)
- [Logging Migration Examples](Logging_Migration_Examples.md) (3 shared connections)
- [Status Command Handlers](Status_Command_Handlers.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (2 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [Cursor Plans Pydantic](Cursor_Plans_Pydantic.md) (1 shared connections)
- [Logout Command Tests](Logout_Command_Tests.md) (1 shared connections)
- [Logger Client Add To](Logger_Client_Add_To.md) (1 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (1 shared connections)

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