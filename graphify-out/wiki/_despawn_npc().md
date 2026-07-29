# . despawn npc()

> 6 nodes

## Key Concepts

- **._despawn_npc()** (4 connections) — `server/services/npc_combat_lifecycle.py`
- **.despawn_npc_safely()** (3 connections) — `server/services/npc_combat_lifecycle.py`
- **.get_npc_lifecycle_manager()** (3 connections) — `server/services/player_combat_service_support.py`
- **Despawn NPC with defensive error handling.          Args:             npc_id: ID** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Despawn an NPC.          Args:             npc_id: ID of the NPC to despawn** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Return lifecycle manager (sync); may be wrapped by asyncio.to_thread.** (1 connections) — `server/services/player_combat_service_support.py`

## Relationships

- [. init ()](_init_%28%29.md) (2 shared connections)
- [.set player combat service()](set_player_combat_service%28%29.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_lifecycle.py`
- `server/services/player_combat_service_support.py`

## Audit Trail

- EXTRACTED: 11 (85%)
- INFERRED: 2 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*