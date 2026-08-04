# memory lifespan app

> 12 nodes

## Key Concepts

- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **._compute_dp_update_fields()** (6 connections) — `server/npc/combat_integration.py`
- **._calculate_max_dp()** (6 connections) — `server/npc/combat_integration.py`
- **._get_int_stat()** (5 connections) — `server/npc/combat_integration.py`
- **._get_player_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **.get_stats()** (3 connections) — `server/npc/npc_base.py`
- **Compute old_dp, new_dp, and max_dp values for PlayerDPUpdated.** (1 connections) — `server/npc/combat_integration.py`
- **Construct the PlayerAttackedEvent payload for NATS publication.** (1 connections) — `server/npc/combat_integration.py`
- **Return an integer stat from stats[key], handling common primitive types.** (1 connections) — `server/npc/combat_integration.py`
- **Calculate max_dp from stats with fallbacks.** (1 connections) — `server/npc/combat_integration.py`
- **Get combat stats for a player.** (1 connections) — `server/npc/combat_integration.py`
- **Get current NPC stats.** (1 connections) — `server/npc/npc_base.py`

## Relationships

- [room conftest toolkit](room_conftest_toolkit.md) (5 shared connections)
- [message queue realtime](message_queue_realtime.md) (3 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [schemas items item](schemas_items_item.md) (1 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 36 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*