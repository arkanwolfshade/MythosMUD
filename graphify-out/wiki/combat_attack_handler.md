# combat attack handler

> 35 nodes

## Key Concepts

- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **NPCCombatIntegrationReadApi** (10 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (9 connections) — `server/services/player_combat_service_support.py`
- **Protocol** (6 connections)
- **NPCCombatRewardsLike** (6 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (6 connections) — `server/services/player_combat_service_support.py`
- **PersistenceWithNpcLifecycleManager** (6 connections) — `server/services/player_combat_service_support.py`
- **original_string_id_for_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **lifecycle_lookup_id()** (5 connections) — `server/services/player_combat_service_support.py`
- **async_load_lifecycle_manager()** (5 connections) — `server/services/player_combat_service_support.py`
- **log_missing_lifecycle_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **UUID** (4 connections)
- **available_lifecycle_npc_ids()** (4 connections) — `server/services/player_combat_service_support.py`
- **.get_xp_value()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_rewards_service()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **xp_int_from_base_stats_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **.award_xp_to_killer()** (2 connections) — `server/services/player_combat_service_support.py`
- **.add_experience()** (1 connections) — `server/services/player_combat_service_support.py`
- **Protocols and module-level helpers for player combat XP and lifecycle lookup.** (1 connections) — `server/services/player_combat_service_support.py`
- **NPC combat rewards helper.** (1 connections) — `server/services/player_combat_service_support.py`
- **Award XP to the killer for an NPC defeat.** (1 connections) — `server/services/player_combat_service_support.py`
- **UUID mapping helper with XP lookup (NPCCombatUUIDMapping).** (1 connections) — `server/services/player_combat_service_support.py`
- **Return stored XP for npc_id when present.** (1 connections) — `server/services/player_combat_service_support.py`
- **Public read API from NPC combat integration.** (1 connections) — `server/services/player_combat_service_support.py`
- *... and 10 more nodes in this community*

## Relationships

- [item models rationale](item_models_rationale.md) (12 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (10 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [player service game](player_service_game.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [schemas players profession](schemas_players_profession.md) (1 shared connections)

## Source Files

- `server/services/player_combat_service_support.py`

## Audit Trail

- EXTRACTED: 108 (89%)
- INFERRED: 13 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*