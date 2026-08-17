# server realtime npc occupant processor

> 79 nodes

## Key Concepts

- **NPCOccupantProcessor** (31 connections) — `server/realtime/npc_occupant_processor.py`
- **RoomIDUtils** (30 connections) — `server/realtime/room_id_utils.py`
- **room_occupant_manager.py** (19 connections) — `server/realtime/room_occupant_manager.py`
- **test_npc_occupant_processor.py** (18 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **RoomOccupantManager** (16 connections) — `server/realtime/room_occupant_manager.py`
- **test_room_id_utils.py** (15 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **npc_occupant_processor.py** (9 connections) — `server/realtime/npc_occupant_processor.py`
- **.normalize_room_id_for_comparison()** (7 connections) — `server/realtime/room_id_utils.py`
- **room_id_utils.py** (6 connections) — `server/realtime/room_id_utils.py`
- **.__init__()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **.check_normalized_ids_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_normalized_room_matches()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_npc_room_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_fallback_room_matches()** (4 connections) — `server/realtime/room_id_utils.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/room_occupant_manager.py`
- **processor()** (4 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_check_fallback_room_matches()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_ids_match()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_ids_match_none()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_room_matches()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_empty()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_none()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_string()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_whitespace()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- *... and 54 more nodes in this community*

## Relationships

- [server realtime npc occupant processor](server_realtime_npc_occupant_processor.md) (12 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (12 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (4 shared connections)
- [server realtime occupant formatter](server_realtime_occupant_formatter.md) (4 shared connections)
- [server realtime player name utils](server_realtime_player_name_utils.md) (3 shared connections)
- [server realtime player occupant processor](server_realtime_player_occupant_processor.md) (3 shared connections)
- [server realtime event handler py](server_realtime_event_handler_py.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_npc_occupant_processor.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 142 (81%)
- INFERRED: 34 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*