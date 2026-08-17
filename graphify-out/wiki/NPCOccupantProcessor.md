# NPCOccupantProcessor

> 43 nodes

## Key Concepts

- **NPCOccupantProcessor** (31 connections) — `server/realtime/npc_occupant_processor.py`
- **RoomIDUtils** (30 connections) — `server/realtime/room_id_utils.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **room_occupant_manager.py** (19 connections) — `server/realtime/room_occupant_manager.py`
- **test_npc_occupant_processor.py** (18 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **npc_occupant_processor.py** (9 connections) — `server/realtime/npc_occupant_processor.py`
- **room_id_utils.py** (6 connections) — `server/realtime/room_id_utils.py`
- **.__init__()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/room_occupant_manager.py`
- **processor()** (4 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **.__init__()** (3 connections) — `server/realtime/room_id_utils.py`
- **.separate_occupants_by_type()** (3 connections) — `server/realtime/room_occupant_manager.py`
- **test_query_npcs_fallback_to_room()** (3 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_query_npcs_for_room_uses_lifecycle_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_query_npcs_handles_exception()** (3 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **Any** (3 connections)
- **asyncio** (3 connections)
- **.get_canonical_room_id()** (2 connections) — `server/realtime/room_id_utils.py`
- **test_filter_fallback_npcs_dead()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_get_npc_lifecycle_manager_no_active_npcs()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_get_npc_lifecycle_manager_unavailable()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_get_npc_room_id_prefers_current_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_process_npcs_for_occupants()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_scan_active_npcs_for_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- *... and 18 more nodes in this community*

## Relationships

- [test_room_id_utils.py](test_room_id_utils.py.md) (19 shared connections)
- [Any](Any.md) (12 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [test_room_occupant_manager.py](test_room_occupant_manager.py.md) (4 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (4 shared connections)
- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (3 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (3 shared connections)
- [OccupantFormatter](OccupantFormatter.md) (3 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (2 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (2 shared connections)
- [realtime/conftest.py](realtime-conftest.py.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_npc_occupant_processor.py`

## Audit Trail

- EXTRACTED: 103 (74%)
- INFERRED: 37 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*