# NPC Occupants Verification Summary

> 8 nodes

## Key Concepts

- **._compute_player_context()** (5 connections) — `server/npc/aggressive_mob_npc.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **._enrich_behavior_context()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **._log_context_enriched()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **Get list of player IDs currently in the room. Returns: List of player IDs in…** (1 connections) — `server/models/room.py`
- **Debug log for context enrichment (best-effort, must not fail).** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Populate player_in_range, enemy_nearby, and target_id for attack rules. Uses…** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Get player_in_range, enemy_nearby, and target_id from persistence. Returns…** (1 connections) — `server/npc/aggressive_mob_npc.py`

## Relationships

- [handle_command](handle_command.md) (3 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)
- [._get_room_uuid_by_stable_id](_get_room_uuid_by_stable_id.md) (1 shared connections)
- [test_look_room.py](test_look_room.py.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/npc/aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 12 (92%)
- INFERRED: 1 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*