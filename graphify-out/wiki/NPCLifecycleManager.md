# NPCLifecycleManager

> 216 nodes

## Key Concepts

- **NPCLifecycleManager** (70 connections) — `server/npc/lifecycle_manager.py`
- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (54 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **NPCInstanceService** (23 connections) — `server/services/npc_instance_service.py`
- **asyncio** (23 connections)
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **._create_npc_services()** (9 connections) — `server/container/bundles/npc.py`
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
- **Any** (8 connections)
- **fixture** (8 connections)
- **_PopulationLifecycleManager** (7 connections) — `server/npc/population_control.py`
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **._finalize_spawn_record()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._spawn_npc()** (6 connections) — `server/npc/population_control.py`
- **.__init__()** (6 connections) — `server/services/npc_instance_service.py`
- **_SpawningServiceProtocol** (5 connections) — `server/npc/lifecycle_manager.py`
- **_SpawnTrackedNPC** (5 connections) — `server/npc/lifecycle_manager.py`
- **.get_lifecycle_statistics()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_service_failure()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._queue_npc_thread_start()** (5 connections) — `server/npc/lifecycle_manager.py`
- *... and 191 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (36 shared connections)
- [event_types.py](event_types.py.md) (29 shared connections)
- [NPCBase](NPCBase.md) (17 shared connections)
- [EventBus](EventBus.md) (10 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (9 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (8 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (7 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (7 shared connections)
- [time.py](time.py.md) (4 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (4 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (3 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (3 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/npc.py`
- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/population_control.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 433 (91%)
- INFERRED: 45 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*