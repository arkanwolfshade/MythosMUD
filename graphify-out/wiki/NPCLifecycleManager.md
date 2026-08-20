# NPCLifecycleManager

> 211 nodes

## Key Concepts

- **NPCLifecycleManager** (70 connections) — `server/npc/lifecycle_manager.py`
- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (54 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **NPCInstanceService** (23 connections) — `server/services/npc_instance_service.py`
- **asyncio** (23 connections)
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **._create_npc_services()** (8 connections) — `server/container/bundles/npc.py`
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **Any** (8 connections)
- **fixture** (8 connections)
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **._finalize_spawn_record()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **._spawn_npc()** (6 connections) — `server/npc/population_control.py`
- **.__init__()** (6 connections) — `server/services/npc_instance_service.py`
- **_SpawningServiceProtocol** (5 connections) — `server/npc/lifecycle_manager.py`
- **_SpawnTrackedNPC** (5 connections) — `server/npc/lifecycle_manager.py`
- **.get_lifecycle_statistics()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_service_failure()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._queue_npc_thread_start()** (5 connections) — `server/npc/lifecycle_manager.py`
- *... and 186 more nodes in this community*

## Relationships

- [lifecycle_manager.py](lifecycle_manager.py.md) (19 shared connections)
- [NPCDefinition](NPCDefinition.md) (17 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (14 shared connections)
- [population_control.py](population_control.py.md) (13 shared connections)
- [EventBus](EventBus.md) (12 shared connections)
- [NPCEnteredRoom](NPCEnteredRoom.md) (9 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (9 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (8 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (7 shared connections)
- [player_combat_service_support.py](player_combat_service_support.py.md) (4 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (4 shared connections)
- [test_population_control.py](test_population_control.py.md) (4 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/population_control.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 425 (91%)
- INFERRED: 44 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*