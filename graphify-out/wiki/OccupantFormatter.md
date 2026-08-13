# OccupantFormatter

> 16 nodes

## Key Concepts

- **OccupantFormatter** (37 connections) — `server/realtime/occupant_formatter.py`
- **.__init__()** (3 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_add_valid_name_to_lists()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_empty()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_npc()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_npc_name_for_update_uuid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_player_name_for_update_uuid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_separate_occupants_by_type_dict_players()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Formats and separates occupants by type.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Initialize occupant formatter.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Test OccupantFormatter._add_valid_name_to_lists() adds name to both lists.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_player_name_for_update() skips UUID player name.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_npc_name_for_update() skips UUID NPC name.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_dict_occupant_for_update() processes NPC dict.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter.separate_occupants_by_type() separates dict players.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._is_valid_name_for_occupant() returns False for empty…** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`

## Relationships

- [test_occupant_formatter.py](test_occupant_formatter.py.md) (15 shared connections)
- [._is_valid_name_for_occupant](_is_valid_name_for_occupant.md) (6 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [._is_uuid_string](_is_uuid_string.md) (2 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (1 shared connections)
- [test_occupant_formatter_init](test_occupant_formatter_init.md) (1 shared connections)
- [test_occupant_formatter_is_valid_name_for_occupant_non_string](test_occupant_formatter_is_valid_name_for_occupant_non_string.md) (1 shared connections)
- [test_occupant_formatter_is_valid_name_for_occupant_none](test_occupant_formatter_is_valid_name_for_occupant_none.md) (1 shared connections)
- [test_occupant_formatter_is_valid_name_for_occupant_uuid](test_occupant_formatter_is_valid_name_for_occupant_uuid.md) (1 shared connections)
- [test_occupant_formatter_process_dict_occupant_for_update_fallback_name](test_occupant_formatter_process_dict_occupant_for_update_fallback_name.md) (1 shared connections)
- [test_occupant_formatter_process_player_name_for_update_valid](test_occupant_formatter_process_player_name_for_update_valid.md) (1 shared connections)

## Source Files

- `server/realtime/occupant_formatter.py`
- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 50 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*