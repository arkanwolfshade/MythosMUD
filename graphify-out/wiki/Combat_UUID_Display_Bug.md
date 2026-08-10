# Combat UUID Display Bug

> 73 nodes

## Key Concepts

- **test_who_commands.py** (47 connections) — `server/tests/unit/commands/test_who_commands.py`
- **who_commands.py** (16 connections) — `server/commands/who_commands.py`
- **filter_players_by_name()** (14 connections) — `server/commands/who_commands.py`
- **parse_last_active_datetime()** (14 connections) — `server/commands/who_commands.py`
- **handle_who_command()** (14 connections) — `server/commands/who_commands.py`
- **filter_online_players()** (10 connections) — `server/commands/who_commands.py`
- **format_who_result()** (10 connections) — `server/commands/who_commands.py`
- **get_players_for_who()** (8 connections) — `server/commands/who_commands.py`
- **Any** (6 connections)
- **test_filter_players_by_name_no_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_exact_match()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_partial_match()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_case_insensitive()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_none()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_empty_string()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_string_with_z()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_string_with_timezone()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_string_without_timezone()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_datetime_naive()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_datetime_aware()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_invalid_string()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_all_online()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_some_offline()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_no_last_active()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_who_result_no_players()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- *... and 48 more nodes in this community*

## Relationships

- [System Monitoring API](System_Monitoring_API.md) (19 shared connections)
- [Commands System Help](Commands_System_Help.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`

## Audit Trail

- EXTRACTED: 258 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*