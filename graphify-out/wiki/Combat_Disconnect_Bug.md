# Combat Disconnect Bug

> 20 nodes

## Key Concepts

- **parse_last_active_datetime()** (14 connections) — `server/commands/who_commands.py`
- **test_parse_last_active_datetime_none()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_empty_string()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_string_with_z()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_string_with_timezone()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_string_without_timezone()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_datetime_naive()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_datetime_aware()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_invalid_string()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_invalid_format()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Parse last_active from string or datetime object to timezone-aware datetime.** (1 connections) — `server/commands/who_commands.py`
- **Test parse_last_active_datetime with None.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime with empty string.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime with string ending in Z.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime with string containing timezone.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime with string without timezone.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime with naive datetime.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime with timezone-aware datetime.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime with invalid string.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime() with invalid format.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`

## Relationships

- [Combat UUID Display Bug](Combat_UUID_Display_Bug.md) (10 shared connections)
- [Legacy Cleanup Summary](Legacy_Cleanup_Summary.md) (3 shared connections)

## Source Files

- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`

## Audit Trail

- EXTRACTED: 51 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*