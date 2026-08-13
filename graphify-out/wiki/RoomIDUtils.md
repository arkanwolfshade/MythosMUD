# RoomIDUtils

> 74 nodes

## Key Concepts

- **RoomIDUtils** (20 connections) — `server/realtime/room_id_utils.py`
- **NPCOccupantProcessor** (18 connections) — `server/realtime/npc_occupant_processor.py`
- **test_room_id_utils.py** (15 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Any** (11 connections)
- **npc_occupant_processor.py** (8 connections) — `server/realtime/npc_occupant_processor.py`
- **.normalize_room_id_for_comparison()** (7 connections) — `server/realtime/room_id_utils.py`
- **.query_npcs_for_room()** (6 connections) — `server/realtime/npc_occupant_processor.py`
- **._filter_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_lifecycle_manager_for_filtering()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._scan_active_npcs_for_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._should_include_npc_in_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._validate_npc_room_tracking()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **.check_normalized_ids_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_normalized_room_matches()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_npc_room_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **room_id_utils.py** (5 connections) — `server/realtime/room_id_utils.py`
- **._filter_single_fallback_npc()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_room_id()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- **.check_fallback_room_matches()** (4 connections) — `server/realtime/room_id_utils.py`
- **.process_npcs_for_occupants()** (3 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (3 connections) — `server/realtime/room_id_utils.py`
- **test_check_fallback_room_matches()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- *... and 49 more nodes in this community*

## Relationships

- [RealTimeEventHandler](RealTimeEventHandler.md) (6 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (2 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 123 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*