# NPCLifecycleManager

> 208 nodes

## Key Concepts

- **NPCLifecycleManager** (69 connections) — `server/npc/lifecycle_manager.py`
- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (54 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCInstanceService** (23 connections) — `server/services/npc_instance_service.py`
- **asyncio** (23 connections)
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **._create_npc_services()** (8 connections) — `server/container/bundles/npc.py`
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **Any** (8 connections)
- **fixture** (8 connections)
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **._finalize_spawn_record()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **._spawn_npc()** (6 connections) — `server/npc/population_control.py`
- **.__init__()** (6 connections) — `server/services/npc_instance_service.py`
- **_SpawningServiceProtocol** (5 connections) — `server/npc/lifecycle_manager.py`
- **_SpawnTrackedNPC** (5 connections) — `server/npc/lifecycle_manager.py`
- **.get_lifecycle_statistics()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_service_failure()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **._handle_player_entered_room()** (5 connections) — `server/npc/population_control.py`
- *... and 183 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (19 shared connections)
- [ConnectionManager](ConnectionManager.md) (19 shared connections)
- [EventBus](EventBus.md) (18 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (17 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (12 shared connections)
- [NPCDied](NPCDied.md) (11 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (9 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (7 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (6 shared connections)
- [NPCBase](NPCBase.md) (4 shared connections)
- [PopulationStats](PopulationStats.md) (3 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (3 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/population_control.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 396 (90%)
- INFERRED: 46 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*