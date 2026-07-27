# Room Occupant Formatter

> 62 nodes · cohesion 0.06

## Key Concepts

- **OccupantFormatter** (40 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter.py** (28 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **._is_valid_name_for_occupant()** (7 connections) — `server/realtime/occupant_formatter.py`
- **._process_dict_occupant_for_update()** (7 connections) — `server/realtime/occupant_formatter.py`
- **._process_npc_name_for_update()** (6 connections) — `server/realtime/occupant_formatter.py`
- **._process_player_name_for_update()** (6 connections) — `server/realtime/occupant_formatter.py`
- **.separate_occupants_by_type()** (5 connections) — `server/realtime/occupant_formatter.py`
- **Any** (5 connections) — `server/realtime/occupant_formatter.py`
- **._add_valid_name_to_lists()** (4 connections) — `server/realtime/occupant_formatter.py`
- **._is_uuid_string()** (4 connections) — `server/realtime/occupant_formatter.py`
- **._process_string_occupant_for_update()** (4 connections) — `server/realtime/occupant_formatter.py`
- **Test OccupantFormatter._is_valid_name_for_occupant() returns False for UUID.** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **.__init__()** (3 connections) — `server/realtime/occupant_formatter.py`
- **Test OccupantFormatter._process_dict_occupant_for_update() processes player dict** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._is_uuid_string() returns True for valid UUID.** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter.separate_occupants_by_type() handles mixed types.** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_add_valid_name_to_lists()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_init()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_empty()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_non_string()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_none()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_uuid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_valid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_fallback_name()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_npc()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- *... and 37 more nodes in this community*

## Relationships

- [[NPC Occupant Processor]] (5 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Player Respawn Events]] (1 shared connections)
- [[Realtime Player Event]] (1 shared connections)

## Source Files

- `server/realtime/occupant_formatter.py`
- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 225 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
