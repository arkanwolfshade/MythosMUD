# Client Event Store

> 294 nodes

## Key Concepts

- **NPCLifecycleManager** (76 connections) — `server/npc/lifecycle_manager.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCSpawningService** (50 connections) — `server/npc/spawning_service.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **NPCInstanceService** (24 connections) — `server/services/npc_instance_service.py`
- **test_npc_combat_integration_class.py** (23 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **npc.py** (14 connections) — `server/container/bundles/npc.py`
- **NPCBundle** (14 connections) — `server/container/bundles/npc.py`
- **._spawn_npc_impl()** (14 connections) — `server/npc/lifecycle_manager.py`
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **_PopulationLifecycleManager** (13 connections) — `server/npc/population_control.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **._create_npc_services()** (8 connections) — `server/container/bundles/npc.py`
- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
- **Any** (8 connections)
- **UUID** (7 connections)
- **.get_combat_stats()** (7 connections) — `server/npc/combat_integration.py`
- **._finalize_spawn_record()** (7 connections) — `server/npc/lifecycle_manager.py`
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **._subscribe_to_events()** (7 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/spawning_service.py`
- **.initialize()** (6 connections) — `server/container/bundles/npc.py`
- *... and 269 more nodes in this community*

## Relationships

- [Realtime Service Bundle](Realtime_Service_Bundle.md) (52 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (42 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (23 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (16 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (11 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (10 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (9 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (9 shared connections)
- [Container Data Models](Container_Data_Models.md) (7 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (6 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (6 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (6 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/npc.py`
- `server/models/room.py`
- `server/npc/combat_integration.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`
- `server/tests/unit/services/test_damage_grace_period.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 987 (90%)
- INFERRED: 111 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*