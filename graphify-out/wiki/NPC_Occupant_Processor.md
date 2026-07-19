# NPC Occupant Processor

> 101 nodes · cohesion 0.03

## Key Concepts

- **PlayerOccupantProcessor** (24 connections) — `server/realtime/player_occupant_processor.py`
- **RoomIDUtils** (24 connections) — `server/realtime/room_id_utils.py`
- **NPCOccupantProcessor** (21 connections) — `server/realtime/npc_occupant_processor.py`
- **room_occupant_manager.py** (18 connections) — `server/realtime/room_occupant_manager.py`
- **test_room_id_utils.py** (14 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Any** (12 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **npc_occupant_processor.py** (8 connections) — `server/realtime/npc_occupant_processor.py`
- **Any** (8 connections) — `server/realtime/room_occupant_manager.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (7 connections) — `server/realtime/room_occupant_manager.py`
- **.query_npcs_for_room()** (6 connections) — `server/realtime/npc_occupant_processor.py`
- **UUID** (6 connections) — `server/realtime/player_occupant_processor.py`
- **PlayerNameExtractor** (6 connections) — `server/realtime/room_occupant_manager.py`
- **._filter_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_lifecycle_manager_for_filtering()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._scan_active_npcs_for_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._should_include_npc_in_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._validate_npc_room_tracking()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **.check_npc_room_match()** (5 connections) — `server/realtime/room_id_utils.py`
- *... and 76 more nodes in this community*

## Relationships

- [[Player Respawn Events]] (20 shared connections)
- [[Look Command Helpers]] (10 shared connections)
- [[NPC Admin API]] (8 shared connections)
- [[Room Occupant Formatter]] (5 shared connections)
- [[NPC Occupant Verification]] (3 shared connections)
- [[Realtime Visual Indicator]] (3 shared connections)
- [[Player Occupant Processor]] (2 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/player_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 326 (90%)
- INFERRED: 37 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
