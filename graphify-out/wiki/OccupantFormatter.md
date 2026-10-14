# OccupantFormatter

> 79 nodes

## Key Concepts

- **OccupantFormatter** (42 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter.py** (33 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **._is_uuid_string()** (8 connections) — `server/realtime/occupant_formatter.py`
- **._process_dict_occupant_for_update()** (8 connections) — `server/realtime/occupant_formatter.py`
- **._is_valid_name_for_occupant()** (7 connections) — `server/realtime/occupant_formatter.py`
- **._process_npc_name_for_update()** (7 connections) — `server/realtime/occupant_formatter.py`
- **._process_player_name_for_update()** (6 connections) — `server/realtime/occupant_formatter.py`
- **.separate_occupants_by_type()** (6 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_npc()** (5 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_npc_name_for_update_uuid()** (5 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_npc_name_for_update_valid()** (5 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **._process_string_occupant_for_update()** (4 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_chars()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_dashes()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_length()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_valid()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_fallback_name()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_player()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_unknown_disposition_falls_back_to_passive()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **._add_valid_name_to_lists()** (3 connections) — `server/realtime/occupant_formatter.py`
- **.__init__()** (3 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_add_valid_name_to_lists()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_init()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_empty()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_non_string()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- *... and 54 more nodes in this community*

## Relationships

- [NpcDisposition](NpcDisposition.md) (16 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/occupant_formatter.py`
- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 127 (89%)
- INFERRED: 16 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*