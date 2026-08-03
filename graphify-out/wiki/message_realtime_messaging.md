# message realtime messaging

> 19 nodes

## Key Concepts

- **Any** (11 connections)
- **.query_npcs_for_room()** (6 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._validate_npc_room_tracking()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._should_include_npc_in_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._scan_active_npcs_for_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_room_id()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- **.process_npcs_for_occupants()** (3 connections) — `server/realtime/npc_occupant_processor.py`
- **Initialize NPC occupant processor.          Args:             connection_manager** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Get and validate NPC lifecycle manager.          Args:             room_id: The** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Get NPC's current room ID from instance.          Args:             npc_instance** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Validate NPC has room tracking and get room ID.          Args:             npc_i** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Determine if NPC should be included in room query results.          Args:** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Scan active NPCs to find those in the target room.          Args:             ac** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Query NPCs for a room from lifecycle manager.          Args:             room_id** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Get fallback NPCs from room.get_npcs() if lifecycle manager query fails.** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Process NPC IDs and convert to occupant information.          Args:** (1 connections) — `server/realtime/npc_occupant_processor.py`

## Relationships

- [event bus events](event_bus_events.md) (9 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [magic healing game](magic_healing_game.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*