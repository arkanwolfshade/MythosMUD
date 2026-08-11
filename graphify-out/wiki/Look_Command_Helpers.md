# Look Command Helpers

> 155 nodes

## Key Concepts

- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **_JSONDict** (10 connections)
- **NPCCombatIntegrationReadApi** (10 connections) — `server/services/player_combat_service_support.py`
- **EventBusPublish** (9 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (9 connections) — `server/services/player_combat_service_support.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **.get_base_stats()** (6 connections) — `server/models/npc.py`
- **._award_xp_via_persistence_fallback()** (6 connections) — `server/services/player_combat_service.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **Protocol** (6 connections)
- **NPCCombatRewardsLike** (6 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (6 connections) — `server/services/player_combat_service_support.py`
- **PersistenceWithNpcLifecycleManager** (6 connections) — `server/services/player_combat_service_support.py`
- **.get_spawn_conditions()** (5 connections) — `server/models/npc.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._get_xp_from_lifecycle_manager()** (5 connections) — `server/services/player_combat_service.py`
- **original_string_id_for_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **lifecycle_lookup_id()** (5 connections) — `server/services/player_combat_service_support.py`
- **async_load_lifecycle_manager()** (5 connections) — `server/services/player_combat_service_support.py`
- **log_missing_lifecycle_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **.get_behavior_config()** (4 connections) — `server/models/npc.py`
- *... and 130 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (59 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (25 shared connections)
- [NATS Subject Metrics](NATS_Subject_Metrics.md) (2 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (2 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (2 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 434 (95%)
- INFERRED: 25 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*