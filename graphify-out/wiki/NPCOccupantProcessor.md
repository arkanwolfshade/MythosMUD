# NPCOccupantProcessor

> 27 nodes

## Key Concepts

- **NPCOccupantProcessor** (18 connections) — `server/realtime/npc_occupant_processor.py`
- **Any** (11 connections)
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
- **.process_npcs_for_occupants()** (3 connections) — `server/realtime/npc_occupant_processor.py`
- **Processes NPC occupants for rooms.** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Initialize NPC occupant processor.          Args:             connection_manager** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Get and validate NPC lifecycle manager.          Args:             room_id: The** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Get NPC's current room ID from instance.          Args:             npc_instance** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Validate NPC has room tracking and get room ID.          Args:             npc_i** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Determine if NPC should be included in room query results.          Args:** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Scan active NPCs to find those in the target room.          Args:             ac** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Query NPCs for a room from lifecycle manager.          Args:             room_id** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Get lifecycle manager for filtering fallback NPCs.          Returns:** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Check if a single fallback NPC should be included.          Args:             np** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Filter fallback NPCs to only include those in active_npcs and alive.          Ar** (1 connections) — `server/realtime/npc_occupant_processor.py`
- *... and 2 more nodes in this community*

## Relationships

- [npc occupant processor](npc_occupant_processor.md) (4 shared connections)
- [Any](Any.md) (4 shared connections)
- [main()](main%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`

## Audit Trail

- EXTRACTED: 97 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*