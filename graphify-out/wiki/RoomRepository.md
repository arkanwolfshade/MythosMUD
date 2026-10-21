# RoomRepository

> 16 nodes · cohesion 0.12

## Key Concepts

- **format_player_location()** (13 connections) — `server/commands/who_commands.py`
- **test_format_player_location_invalid()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_location_valid()** (3 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **test_format_player_location_invalid()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_non_string()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_none()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_short_format()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_location_valid()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Format player location as Zone: Sub-zone: Room from room ID. Args: room_id:…** (1 connections) — `server/commands/who_commands.py`
- **Test format_player_location() formats valid room ID.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Test format_player_location() handles invalid room ID.** (1 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **Test format_player_location() with short room ID format.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test format_player_location() with non-string input.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test formatting valid player location.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test formatting invalid player location.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test formatting None location.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`

## Relationships

- [Phase 2: Qualitative Analysis Results](Phase_2-_Qualitative_Analysis_Results.md) (6 shared connections)
- [NpcDisposition](NpcDisposition.md) (4 shared connections)
- [test_player_event_handlers_utils.py](test_player_event_handlers_utils.py.md) (1 shared connections)
- [get_cached_player](get_cached_player.md) (1 shared connections)

## Source Files

- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`
- `server/tests/unit/commands/test_who_commands_helpers.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*