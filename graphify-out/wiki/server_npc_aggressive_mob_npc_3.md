# server npc aggressive mob npc

> 6 nodes

## Key Concepts

- **._compute_player_context()** (5 connections) — `server/npc/aggressive_mob_npc.py`
- **._enrich_behavior_context()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **._log_context_enriched()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **Debug log for context enrichment (best-effort, must not fail).** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Populate player_in_range, enemy_nearby, and target_id for attack rules. Uses…** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Get player_in_range, enemy_nearby, and target_id from persistence. Returns…** (1 connections) — `server/npc/aggressive_mob_npc.py`

## Relationships

- [server npc aggressive mob npc](server_npc_aggressive_mob_npc.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (1 shared connections)
- [server models room py any](server_models_room_py_any.md) (1 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 9 (90%)
- INFERRED: 1 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*