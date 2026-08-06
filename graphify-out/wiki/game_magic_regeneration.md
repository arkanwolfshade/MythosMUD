# game magic regeneration

> 10 nodes

## Key Concepts

- **._compute_player_context()** (7 connections) — `server/npc/aggressive_mob_npc.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **._enrich_behavior_context()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **.get_room_by_id()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._log_context_enriched()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **Get list of player IDs currently in the room.          Returns:             List** (1 connections) — `server/models/room.py`
- **Return the room object for the given room_id, or None if not found.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Get player_in_range, enemy_nearby, and target_id from persistence.         Retu** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Debug log for context enrichment (best-effort, must not fail).** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Populate player_in_range, enemy_nearby, and target_id for attack rules.** (1 connections) — `server/npc/aggressive_mob_npc.py`

## Relationships

- [error logging rationale](error_logging_rationale.md) (3 shared connections)
- [services nats service](services_nats_service.md) (2 shared connections)
- [room models instance](room_models_instance.md) (1 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (1 shared connections)
- [tick game processing](tick_game_processing.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/npc/aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 23 (88%)
- INFERRED: 3 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*