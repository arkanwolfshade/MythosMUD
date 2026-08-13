# player_combat_service_support.py

> 45 nodes

## Key Concepts

- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **NPCCombatIntegrationReadApi** (10 connections) — `server/services/player_combat_service_support.py`
- **EventBusPublish** (9 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (9 connections) — `server/services/player_combat_service_support.py`
- **NPCCombatRewardsLike** (6 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (6 connections) — `server/services/player_combat_service_support.py`
- **Protocol** (6 connections)
- **PersistenceWithNpcLifecycleManager** (5 connections) — `server/services/player_combat_service_support.py`
- **lifecycle_lookup_id()** (5 connections) — `server/services/player_combat_service_support.py`
- **log_missing_lifecycle_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **original_string_id_for_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **._despawn_npc()** (4 connections) — `server/services/npc_combat_lifecycle.py`
- **async_load_lifecycle_manager()** (4 connections) — `server/services/player_combat_service_support.py`
- **available_lifecycle_npc_ids()** (4 connections) — `server/services/player_combat_service_support.py`
- **UUID** (4 connections)
- **.despawn_npc_safely()** (3 connections) — `server/services/npc_combat_lifecycle.py`
- **.get_rewards_service()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_npc_lifecycle_manager()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_xp_value()** (3 connections) — `server/services/player_combat_service_support.py`
- **xp_int_from_base_stats_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **.publish()** (2 connections) — `server/services/player_combat_service_support.py`
- **.award_xp_to_killer()** (2 connections) — `server/services/player_combat_service_support.py`
- **.add_experience()** (1 connections) — `server/services/player_combat_service_support.py`
- **Despawn NPC with defensive error handling. Args: npc_id: ID of the NPC to…** (1 connections) — `server/services/npc_combat_lifecycle.py`
- *... and 20 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (11 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (8 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)

## Source Files

- `server/services/npc_combat_lifecycle.py`
- `server/services/player_combat_service_support.py`

## Audit Trail

- EXTRACTED: 73 (82%)
- INFERRED: 16 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*