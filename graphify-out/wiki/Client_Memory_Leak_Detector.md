# Client Memory Leak Detector

> 47 nodes

## Key Concepts

- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **NPCCombatIntegrationReadApi** (10 connections) — `server/services/player_combat_service_support.py`
- **EventBusPublish** (9 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (9 connections) — `server/services/player_combat_service_support.py`
- **Protocol** (6 connections)
- **NPCCombatRewardsLike** (6 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (6 connections) — `server/services/player_combat_service_support.py`
- **PersistenceWithNpcLifecycleManager** (6 connections) — `server/services/player_combat_service_support.py`
- **original_string_id_for_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **lifecycle_lookup_id()** (5 connections) — `server/services/player_combat_service_support.py`
- **async_load_lifecycle_manager()** (5 connections) — `server/services/player_combat_service_support.py`
- **log_missing_lifecycle_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **._despawn_npc()** (4 connections) — `server/services/npc_combat_lifecycle.py`
- **UUID** (4 connections)
- **available_lifecycle_npc_ids()** (4 connections) — `server/services/player_combat_service_support.py`
- **.despawn_npc_safely()** (3 connections) — `server/services/npc_combat_lifecycle.py`
- **.get_xp_value()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_rewards_service()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **.get_npc_lifecycle_manager()** (3 connections) — `server/services/player_combat_service_support.py`
- **xp_int_from_base_stats_mapping()** (3 connections) — `server/services/player_combat_service_support.py`
- **.publish()** (2 connections) — `server/services/player_combat_service_support.py`
- **.award_xp_to_killer()** (2 connections) — `server/services/player_combat_service_support.py`
- **Despawn NPC with defensive error handling.          Args:             npc_id: ID** (1 connections) — `server/services/npc_combat_lifecycle.py`
- *... and 22 more nodes in this community*

## Relationships

- [NPC Services Bundle](NPC_Services_Bundle.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (10 shared connections)
- [Redis to NATS Migration](Redis_to_NATS_Migration.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (3 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (3 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (1 shared connections)
- [Container Open Events](Container_Open_Events.md) (1 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_lifecycle.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`

## Audit Trail

- EXTRACTED: 164 (90%)
- INFERRED: 19 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*