# Player Combat Service Support

> 37 nodes

## Key Concepts

- **player_combat_service_support.py** (20 connections) — `server/services/player_combat_service_support.py`
- **Protocol** (6 connections)
- **NPCCombatIntegrationReadApi** (5 connections) — `server/services/player_combat_service_support.py`
- **NPCCombatRewardsLike** (5 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (5 connections) — `server/services/player_combat_service_support.py`
- **EventBusPublish** (4 connections) — `server/services/player_combat_service_support.py`
- **PersistenceWithNpcLifecycleManager** (4 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (4 connections) — `server/services/player_combat_service_support.py`
- **lifecycle_lookup_id()** (4 connections) — `server/services/player_combat_service_support.py`
- **original_string_id_for_npc()** (4 connections) — `server/services/player_combat_service_support.py`
- **UUID** (4 connections)
- **async_load_lifecycle_manager()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_rewards_service()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_npc_lifecycle_manager()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_xp_value()** (3 connections) — `server/services/player_combat_service_support.py`
- **.publish()** (2 connections) — `server/services/player_combat_service_support.py`
- **.award_xp_to_killer()** (2 connections) — `server/services/player_combat_service_support.py`
- **xp_int_from_base_stats_mapping()** (2 connections) — `server/services/player_combat_service_support.py`
- **.add_experience()** (1 connections) — `server/services/player_combat_service_support.py`
- **Protocols and module-level helpers for player combat XP and lifecycle lookup.…** (1 connections) — `server/services/player_combat_service_support.py`
- **Return xp_value from get_base_stats() result, or None if missing/invalid.** (1 connections) — `server/services/player_combat_service_support.py`
- **Minimal event bus surface used by player combat service.** (1 connections) — `server/services/player_combat_service_support.py`
- **Publish a domain event.** (1 connections) — `server/services/player_combat_service_support.py`
- **NPC combat rewards helper.** (1 connections) — `server/services/player_combat_service_support.py`
- *... and 12 more nodes in this community*

## Relationships

- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (1 shared connections)
- [Test Movement Service](Test_Movement_Service.md) (1 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)

## Source Files

- `server/services/player_combat_service_support.py`

## Audit Trail

- EXTRACTED: 55 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*