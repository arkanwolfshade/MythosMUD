# player_combat_service_support.py

> 39 nodes

## Key Concepts

- **player_combat_service_support.py** (20 connections) — `server/services/player_combat_service_support.py`
- **NPCCombatIntegrationReadApi** (7 connections) — `server/services/player_combat_service_support.py`
- **EventBusPublish** (6 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (6 connections) — `server/services/player_combat_service_support.py`
- **Protocol** (6 connections)
- **NPCCombatRewardsLike** (5 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (5 connections) — `server/services/player_combat_service_support.py`
- **lifecycle_lookup_id()** (5 connections) — `server/services/player_combat_service_support.py`
- **log_missing_lifecycle_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **original_string_id_for_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **PersistenceWithNpcLifecycleManager** (4 connections) — `server/services/player_combat_service_support.py`
- **async_load_lifecycle_manager()** (4 connections) — `server/services/player_combat_service_support.py`
- **available_lifecycle_npc_ids()** (4 connections) — `server/services/player_combat_service_support.py`
- **UUID** (4 connections)
- **.get_rewards_service()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_xp_value()** (3 connections) — `server/services/player_combat_service_support.py`
- **xp_int_from_base_stats_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **.publish()** (2 connections) — `server/services/player_combat_service_support.py`
- **.award_xp_to_killer()** (2 connections) — `server/services/player_combat_service_support.py`
- **.add_experience()** (1 connections) — `server/services/player_combat_service_support.py`
- **Protocols and module-level helpers for player combat XP and lifecycle lookup.…** (1 connections) — `server/services/player_combat_service_support.py`
- **Keys present in lifecycle_records for debug logging.** (1 connections) — `server/services/player_combat_service_support.py`
- **Return xp_value from get_base_stats() result, or None if missing/invalid.** (1 connections) — `server/services/player_combat_service_support.py`
- **Debug when a lookup id is missing from lifecycle records.** (1 connections) — `server/services/player_combat_service_support.py`
- *... and 14 more nodes in this community*

## Relationships

- [player_event_handlers.py](player_event_handlers.py.md) (9 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (4 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [._despawn_npc](_despawn_npc.md) (1 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (1 shared connections)

## Source Files

- `server/services/player_combat_service_support.py`

## Audit Trail

- EXTRACTED: 65 (92%)
- INFERRED: 6 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*