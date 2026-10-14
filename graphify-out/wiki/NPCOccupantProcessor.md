# NPCOccupantProcessor

> 145 nodes

## Key Concepts

- **NPCOccupantProcessor** (32 connections) — `server/realtime/npc_occupant_processor.py`
- **RoomIDUtils** (30 connections) — `server/realtime/room_id_utils.py`
- **RoomOccupantManager** (25 connections) — `server/realtime/room_occupant_manager.py`
- **room_occupant_manager.py** (22 connections) — `server/realtime/room_occupant_manager.py`
- **test_npc_occupant_processor.py** (20 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_room_occupant_manager.py** (17 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_room_id_utils.py** (15 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Any** (11 connections)
- **npc_occupant_processor.py** (10 connections) — `server/realtime/npc_occupant_processor.py`
- **asyncio** (10 connections)
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **.normalize_room_id_for_comparison()** (7 connections) — `server/realtime/room_id_utils.py`
- **.query_npcs_for_room()** (6 connections) — `server/realtime/npc_occupant_processor.py`
- **.get_room_occupants()** (6 connections) — `server/realtime/room_occupant_manager.py`
- **room_id_utils.py** (6 connections) — `server/realtime/room_id_utils.py`
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
- *... and 120 more nodes in this community*

## Relationships

- [player_event_handlers.py](player_event_handlers.py.md) (8 shared connections)
- [NpcDisposition](NpcDisposition.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [event_handler.py](event_handler.py.md) (4 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (4 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (4 shared connections)
- [OccupantFormatter](OccupantFormatter.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [ValueError](ValueError.md) (2 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_npc_occupant_processor.py`
- `server/tests/unit/realtime/test_room_id_utils.py`
- `server/tests/unit/realtime/test_room_occupant_manager.py`

## Audit Trail

- EXTRACTED: 240 (86%)
- INFERRED: 39 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*