# NPCOccupantProcessor

> 30 nodes

## Key Concepts

- **NPCOccupantProcessor** (31 connections) — `server/realtime/npc_occupant_processor.py`
- **RoomIDUtils** (22 connections) — `server/realtime/room_id_utils.py`
- **test_npc_occupant_processor.py** (17 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **npc_occupant_processor.py** (9 connections) — `server/realtime/npc_occupant_processor.py`
- **room_id_utils.py** (6 connections) — `server/realtime/room_id_utils.py`
- **.__init__()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **processor()** (4 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_query_npcs_fallback_to_room()** (3 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_query_npcs_for_room_uses_lifecycle_manager()** (3 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_query_npcs_handles_exception()** (3 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **asyncio** (3 connections)
- **.get_canonical_room_id()** (2 connections) — `server/realtime/room_id_utils.py`
- **test_filter_fallback_npcs_dead()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_get_npc_lifecycle_manager_no_active_npcs()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_get_npc_lifecycle_manager_unavailable()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_get_npc_room_id_prefers_current_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_process_npcs_for_occupants()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_scan_active_npcs_for_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_should_include_npc_dead()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_should_include_npc_matching_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **fixture** (1 connections)
- **NPC occupant processing utilities. This module handles querying and processing…** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Processes NPC occupants for rooms.** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Initialize NPC occupant processor. Args: connection_manager: ConnectionManager…** (1 connections) — `server/realtime/npc_occupant_processor.py`
- *... and 5 more nodes in this community*

## Relationships

- [Any](Any.md) (12 shared connections)
- [test_room_id_utils.py](test_room_id_utils.py.md) (11 shared connections)
- [event_types.py](event_types.py.md) (8 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (1 shared connections)
- [OccupantFormatter](OccupantFormatter.md) (1 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_npc_occupant_processor.py`

## Audit Trail

- EXTRACTED: 88 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*