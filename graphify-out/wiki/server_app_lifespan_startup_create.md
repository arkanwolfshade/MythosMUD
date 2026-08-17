# server app lifespan startup create

> 204 nodes

## Key Concepts

- **NPCLifecycleManager** (69 connections) — `server/npc/lifecycle_manager.py`
- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (54 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **NPCInstanceService** (23 connections) — `server/services/npc_instance_service.py`
- **asyncio** (23 connections)
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **._create_npc_services()** (8 connections) — `server/container/bundles/npc.py`
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
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
- *... and 179 more nodes in this community*

## Relationships

- [server events event bus](server_events_event_bus.md) (26 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (26 shared connections)
- [draft7validator](draft7validator.md) (21 shared connections)
- [server models npc npcdefinition is](server_models_npc_npcdefinition_is.md) (13 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (9 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (9 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (7 shared connections)
- [server npc population control npcpopulationcontroller](server_npc_population_control_npcpopulationcontroller.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server npc init](server_npc_init.md) (4 shared connections)
- [server services player combat service](server_services_player_combat_service.md) (4 shared connections)
- [moduletype](moduletype.md) (4 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/npc.py`
- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/population_control.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 417 (90%)
- INFERRED: 47 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*