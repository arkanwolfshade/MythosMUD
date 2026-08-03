# websocket realtime handler

> 26 nodes

## Key Concepts

- **PlayerXpLike** (9 connections) — `server/services/player_combat_service_support.py`
- **Protocol** (6 connections)
- **NPCCombatRewardsLike** (6 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (6 connections) — `server/services/player_combat_service_support.py`
- **PersistenceWithNpcLifecycleManager** (6 connections) — `server/services/player_combat_service_support.py`
- **async_load_lifecycle_manager()** (5 connections) — `server/services/player_combat_service_support.py`
- **._despawn_npc()** (4 connections) — `server/services/npc_combat_lifecycle.py`
- **.despawn_npc_safely()** (3 connections) — `server/services/npc_combat_lifecycle.py`
- **.get_xp_value()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_rewards_service()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_npc_lifecycle_manager()** (3 connections) — `server/services/player_combat_service_support.py`
- **.award_xp_to_killer()** (2 connections) — `server/services/player_combat_service_support.py`
- **Despawn NPC with defensive error handling.          Args:             npc_id: ID** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Despawn an NPC.          Args:             npc_id: ID of the NPC to despawn** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **.add_experience()** (1 connections) — `server/services/player_combat_service_support.py`
- **NPC combat rewards helper.** (1 connections) — `server/services/player_combat_service_support.py`
- **Award XP to the killer for an NPC defeat.** (1 connections) — `server/services/player_combat_service_support.py`
- **UUID mapping helper with XP lookup (NPCCombatUUIDMapping).** (1 connections) — `server/services/player_combat_service_support.py`
- **Return stored XP for npc_id when present.** (1 connections) — `server/services/player_combat_service_support.py`
- **Return rewards helper service.** (1 connections) — `server/services/player_combat_service_support.py`
- **Return UUID mapping helper.** (1 connections) — `server/services/player_combat_service_support.py`
- **Minimal player surface for XP persistence fallback.** (1 connections) — `server/services/player_combat_service_support.py`
- **Persistence layer that can expose the NPC lifecycle manager.** (1 connections) — `server/services/player_combat_service_support.py`
- **Return lifecycle manager (sync); may be wrapped by asyncio.to_thread.** (1 connections) — `server/services/player_combat_service_support.py`
- *... and 1 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (13 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)

## Source Files

- `server/services/npc_combat_lifecycle.py`
- `server/services/player_combat_service_support.py`

## Audit Trail

- EXTRACTED: 61 (85%)
- INFERRED: 11 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*