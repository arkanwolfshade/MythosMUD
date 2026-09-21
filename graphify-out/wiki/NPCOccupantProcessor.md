# NPCOccupantProcessor

> 92 nodes

## Key Concepts

- **NPCOccupantProcessor** (31 connections) — `server/realtime/npc_occupant_processor.py`
- **RoomIDUtils** (30 connections) — `server/realtime/room_id_utils.py`
- **test_npc_occupant_processor.py** (17 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_room_id_utils.py** (15 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Any** (11 connections)
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **npc_occupant_processor.py** (9 connections) — `server/realtime/npc_occupant_processor.py`
- **.normalize_room_id_for_comparison()** (7 connections) — `server/realtime/room_id_utils.py`
- **.query_npcs_for_room()** (6 connections) — `server/realtime/npc_occupant_processor.py`
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
- **.check_npc_room_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **._filter_single_fallback_npc()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_room_id()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- **.check_fallback_room_matches()** (4 connections) — `server/realtime/room_id_utils.py`
- **processor()** (4 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- *... and 67 more nodes in this community*

## Relationships

- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (8 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (1 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)
- [OccupantFormatter](OccupantFormatter.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_npc_occupant_processor.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 152 (87%)
- INFERRED: 23 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*