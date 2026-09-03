# NPC Behavior & Spawning

> 236 nodes

## Key Concepts

- **NPCSpawningService** (66 connections) — `server/npc/spawning_service.py`
- **NPCLifecycleManager** (64 connections) — `server/npc/lifecycle_manager.py`
- **NPCPopulationController** (57 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (54 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **NPCInstanceService** (23 connections) — `server/services/npc_instance_service.py`
- **asyncio** (23 connections)
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **server/npc/__init__.py** (19 connections) — `server/npc/__init__.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **spawning_models.py** (13 connections) — `server/npc/spawning_models.py`
- **._create_npc_services()** (9 connections) — `server/container/bundles/npc.py`
- **_spawn_success()** (8 connections) — `server/npc/spawning_request_execution.py`
- **Any** (8 connections)
- **fixture** (8 connections)
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/spawning_service.py`
- **_room_from_persistence()** (6 connections) — `server/npc/spawning_request_execution.py`
- *... and 211 more nodes in this community*

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (50 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (28 shared connections)
- [Npc Base](Npc_Base.md) (27 shared connections)
- [NPC Models](NPC_Models.md) (23 shared connections)
- [Lifecycle Manager](Lifecycle_Manager.md) (17 shared connections)
- [Test Npc Utils](Test_Npc_Utils.md) (12 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (10 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (10 shared connections)
- [Population Control](Population_Control.md) (10 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (10 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (8 shared connections)
- [Spawning Service](Spawning_Service.md) (8 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/models/npc.py`
- `server/npc/__init__.py`
- `server/npc/behaviors.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/population_control.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/services/npc_instance_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/npc/test_spawning_modules.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 631 (91%)
- INFERRED: 61 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*