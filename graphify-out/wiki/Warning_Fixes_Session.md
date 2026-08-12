# Warning Fixes Session

> 35 nodes

## Key Concepts

- **NPCOccupantProcessor** (18 connections) — `server/realtime/npc_occupant_processor.py`
- **Any** (11 connections)
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **.query_npcs_for_room()** (6 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._validate_npc_room_tracking()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._should_include_npc_in_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._scan_active_npcs_for_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_lifecycle_manager_for_filtering()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._filter_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_room_id()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- **._filter_single_fallback_npc()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/room_occupant_manager.py`
- **.process_npcs_for_occupants()** (3 connections) — `server/realtime/npc_occupant_processor.py`
- **Any** (3 connections)
- **.separate_occupants_by_type()** (3 connections) — `server/realtime/room_occupant_manager.py`
- **UUID** (2 connections)
- **Processes NPC occupants for rooms.** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Initialize NPC occupant processor.          Args:             connection_manager** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Get and validate NPC lifecycle manager.          Args:             room_id: The** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Get NPC's current room ID from instance.          Args:             npc_instance** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Validate NPC has room tracking and get room ID.          Args:             npc_i** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Determine if NPC should be included in room query results.          Args:** (1 connections) — `server/realtime/npc_occupant_processor.py`
- *... and 10 more nodes in this community*

## Relationships

- [Combat Turn Processor](Combat_Turn_Processor.md) (4 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (3 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/room_occupant_manager.py`

## Audit Trail

- EXTRACTED: 121 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*