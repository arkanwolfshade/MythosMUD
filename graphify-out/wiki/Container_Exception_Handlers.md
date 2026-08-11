# Container Exception Handlers

> 121 nodes

## Key Concepts

- **CombatService** (182 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **UUID** (20 connections)
- **get_combat_id_for_npc()** (13 connections) — `server/services/combat_service_npc.py`
- **UUID** (11 connections)
- **get_npc_participant_current_room()** (11 connections) — `server/services/combat_service_npc.py`
- **spell_effects_internal.py** (10 connections) — `server/game/magic/spell_effects_internal.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (10 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (9 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **DataProviderProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_id_for_npc_via_mapping()** (8 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
- **.get_uuid_for_string_id()** (7 connections) — `server/services/combat_service_npc.py`
- **combat_room_id_for_npc_spell()** (6 connections) — `server/game/magic/spell_effects_internal.py`
- **.validate_melee_or_end_combat()** (6 connections) — `server/services/combat_service.py`
- **.finalize_attack_result()** (6 connections) — `server/services/combat_service.py`
- **.get_original_string_id()** (6 connections) — `server/services/combat_service_npc.py`
- **_get_data_provider()** (6 connections) — `server/services/combat_service_npc.py`
- **_iter_active_combats()** (6 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (6 connections) — `server/services/combat_service_npc.py`
- **get_combat_by_participant()** (6 connections) — `server/services/combat_service_npc.py`
- **_participant_matches_npc_id()** (6 connections) — `server/services/combat_service_npc.py`
- *... and 96 more nodes in this community*

## Relationships

- [Health Check Models](Health_Check_Models.md) (34 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (21 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (14 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (14 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (12 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (11 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (10 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (8 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (6 shared connections)
- [Game Client Container](Game_Client_Container.md) (6 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (5 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (4 shared connections)

## Source Files

- `server/game/magic/spell_effects_internal.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`

## Audit Trail

- EXTRACTED: 536 (91%)
- INFERRED: 56 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*