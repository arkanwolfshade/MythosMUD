# OccupantFormatter

> 14 nodes

## Key Concepts

- **OccupantFormatter** (41 connections) — `server/realtime/occupant_formatter.py`
- **.__init__()** (3 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_add_valid_name_to_lists()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_none()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_player()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_npc_name_for_update_uuid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_separate_occupants_by_type_none()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Formats and separates occupants by type.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Initialize occupant formatter.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Test OccupantFormatter._add_valid_name_to_lists() adds name to both lists.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_npc_name_for_update() skips UUID NPC name.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_dict_occupant_for_update() processes player…** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter.separate_occupants_by_type() handles None input.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._is_valid_name_for_occupant() returns False for None.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`

## Relationships

- [test_occupant_formatter.py](test_occupant_formatter.py.md) (14 shared connections)
- [._is_valid_name_for_occupant](_is_valid_name_for_occupant.md) (6 shared connections)
- [._is_uuid_string](_is_uuid_string.md) (6 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (2 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (1 shared connections)
- [test_occupant_formatter_init](test_occupant_formatter_init.md) (1 shared connections)
- [test_occupant_formatter_is_valid_name_for_occupant_non_string](test_occupant_formatter_is_valid_name_for_occupant_non_string.md) (1 shared connections)
- [test_occupant_formatter_is_valid_name_for_occupant_uuid](test_occupant_formatter_is_valid_name_for_occupant_uuid.md) (1 shared connections)
- [test_occupant_formatter_process_player_name_for_update_uuid](test_occupant_formatter_process_player_name_for_update_uuid.md) (1 shared connections)
- [test_occupant_formatter_process_string_occupant_for_update_uuid](test_occupant_formatter_process_string_occupant_for_update_uuid.md) (1 shared connections)
- [test_occupant_formatter_process_string_occupant_for_update_valid](test_occupant_formatter_process_string_occupant_for_update_valid.md) (1 shared connections)
- [test_occupant_formatter_separate_occupants_by_type_dict_players](test_occupant_formatter_separate_occupants_by_type_dict_players.md) (1 shared connections)

## Source Files

- `server/realtime/occupant_formatter.py`
- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 48 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*