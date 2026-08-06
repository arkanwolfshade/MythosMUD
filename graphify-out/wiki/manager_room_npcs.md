# manager room npcs

> 23 nodes

## Key Concepts

- **Any** (11 connections)
- **.query_npcs_for_room()** (6 connections) — `server/realtime/npc_occupant_processor.py`
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
- **Get and validate NPC lifecycle manager.          Args:             room_id: The** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Get NPC's current room ID from instance.          Args:             npc_instance** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Validate NPC has room tracking and get room ID.          Args:             npc_i** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Determine if NPC should be included in room query results.          Args:** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Scan active NPCs to find those in the target room.          Args:             ac** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Query NPCs for a room from lifecycle manager.          Args:             room_id** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Get lifecycle manager for filtering fallback NPCs.          Returns:** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Check if a single fallback NPC should be included.          Args:             np** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Filter fallback NPCs to only include those in active_npcs and alive.          Ar** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Get fallback NPCs from room.get_npcs() if lifecycle manager query fails.** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Process NPC IDs and convert to occupant information.          Args:** (1 connections) — `server/realtime/npc_occupant_processor.py`

## Relationships

- [schemas players profession](schemas_players_profession.md) (12 shared connections)
- [tick game processing](tick_game_processing.md) (2 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`

## Audit Trail

- EXTRACTED: 74 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*