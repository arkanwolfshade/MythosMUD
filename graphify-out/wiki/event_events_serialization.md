# event events serialization

> 25 nodes

## Key Concepts

- **.to_dict()** (8 connections) — `server/models/room.py`
- **._compute_player_context()** (7 connections) — `server/npc/aggressive_mob_npc.py`
- **.__init__()** (5 connections) — `server/models/room.py`
- **.get_containers()** (5 connections) — `server/models/room.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **._enrich_behavior_context()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **Any** (3 connections)
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **.get_room_by_id()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._log_context_enriched()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **Initialize a Room from JSON data.          Args:             room_data: Dictiona** (1 connections) — `server/models/room.py`
- **Get list of player IDs currently in the room.          Returns:             List** (1 connections) — `server/models/room.py`
- **Get list of object IDs currently in the room.          Returns:             List** (1 connections) — `server/models/room.py`
- **Get list of NPC IDs currently in the room.          Returns:             List of** (1 connections) — `server/models/room.py`
- **Get the total number of occupants in the room.          Returns:             Tot** (1 connections) — `server/models/room.py`
- **Check if the room has no occupants.          Returns:             True if the ro** (1 connections) — `server/models/room.py`
- **Get list of containers in this room.          Returns:             List of conta** (1 connections) — `server/models/room.py`
- **Convert the room to a dictionary representation.          Returns:             D** (1 connections) — `server/models/room.py`
- **Return the room object for the given room_id, or None if not found.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Get player_in_range, enemy_nearby, and target_id from persistence.         Retu** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Debug log for context enrichment (best-effort, must not fail).** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Populate player_in_range, enemy_nearby, and target_id for attack rules.** (1 connections) — `server/npc/aggressive_mob_npc.py`

## Relationships

- [room models instance](room_models_instance.md) (8 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [lucidity event services](lucidity_event_services.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [target resolution service](target_resolution_service.md) (1 shared connections)
- [container find inventory](container_find_inventory.md) (1 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/npc/aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 63 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*