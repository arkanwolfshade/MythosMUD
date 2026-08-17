# ._despawn_npc

> 6 nodes

## Key Concepts

- **._despawn_npc()** (4 connections) — `server/services/npc_combat_lifecycle.py`
- **.despawn_npc_safely()** (3 connections) — `server/services/npc_combat_lifecycle.py`
- **.get_npc_lifecycle_manager()** (3 connections) — `server/services/player_combat_service_support.py`
- **Despawn NPC with defensive error handling. Args: npc_id: ID of the NPC to…** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Despawn an NPC. Args: npc_id: ID of the NPC to despawn _room_id: ID of the room…** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Return lifecycle manager (sync); may be wrapped by asyncio.to_thread.** (1 connections) — `server/services/player_combat_service_support.py`

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [NPCCombatIntegrationReadApi](NPCCombatIntegrationReadApi.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_lifecycle.py`
- `server/services/player_combat_service_support.py`

## Audit Trail

- EXTRACTED: 7 (88%)
- INFERRED: 1 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*