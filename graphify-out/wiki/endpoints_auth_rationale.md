# endpoints auth rationale

> 22 nodes

## Key Concepts

- **_parse_stat_datetime()** (16 connections) — `server/commands/look_npc.py`
- **test_parse_stat_datetime_from_timestamp()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_stat_datetime_from_datetime()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_stat_datetime_from_iso_string()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_stat_datetime_invalid()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_stat_datetime_none()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_stat_datetime_from_datetime()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_stat_datetime_from_timestamp()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_stat_datetime_from_iso_string()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_stat_datetime_none()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_stat_datetime_invalid()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Parse datetime value from various formats and return formatted string.** (1 connections) — `server/commands/look_npc.py`
- **Test parsing datetime from timestamp.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test parsing datetime from datetime object.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test parsing datetime from ISO string.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test parsing datetime with invalid value.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test parsing datetime with None.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test _parse_stat_datetime() handles datetime object.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _parse_stat_datetime() handles timestamp.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _parse_stat_datetime() handles ISO string.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _parse_stat_datetime() returns 'Unknown' for None.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _parse_stat_datetime() returns string representation for invalid input.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`

## Relationships

- [npc look commands](npc_look_commands.md) (9 shared connections)
- [follow service game](follow_service_game.md) (6 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*