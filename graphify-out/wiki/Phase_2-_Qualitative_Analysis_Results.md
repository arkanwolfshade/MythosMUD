# Phase 2: Qualitative Analysis Results

> 18 nodes · cohesion 0.20

## Key Concepts

- **test_who_commands.py** (47 connections) — `server/tests/unit/commands/test_who_commands.py`
- **parse_last_active_datetime()** (14 connections) — `server/commands/who_commands.py`
- **test_parse_last_active_datetime_datetime_aware()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_datetime_naive()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_empty_string()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_invalid_format()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_invalid_string()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_none()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_string_with_timezone()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_string_with_z()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_parse_last_active_datetime_string_without_timezone()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Parse last_active from string or datetime object to timezone-aware datetime.…** (1 connections) — `server/commands/who_commands.py`
- **Unit tests for who commands.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime with None.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime with empty string.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime with string containing timezone.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime with timezone-aware datetime.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test parse_last_active_datetime() with invalid format.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`

## Relationships

- [get_cached_player](get_cached_player.md) (14 shared connections)
- [PlayerCreationService](PlayerCreationService.md) (9 shared connections)
- [RoomRepository](RoomRepository.md) (6 shared connections)
- [NpcDisposition](NpcDisposition.md) (5 shared connections)
- [HallucinationRng](HallucinationRng.md) (5 shared connections)

## Source Files

- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`

## Audit Trail

- EXTRACTED: 69 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*