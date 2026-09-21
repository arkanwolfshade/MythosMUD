# NPCSpawningService

> 90 nodes

## Key Concepts

- **NPCSpawningService** (69 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (47 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (19 connections) — `server/npc/spawning_instance_factory.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **_spawn_success()** (8 connections) — `server/npc/spawning_request_execution.py`
- **.__init__()** (8 connections) — `server/npc/spawning_service.py`
- **._create_npc_instance()** (6 connections) — `server/npc/spawning_service.py`
- **._spawn_npc_from_request()** (6 connections) — `server/npc/spawning_service.py`
- **._check_spawn_requirements_for_room()** (5 connections) — `server/npc/spawning_service.py`
- **.get_spawn_statistics()** (5 connections) — `server/npc/spawning_service.py`
- **test_create_npc_instance_threads_event_reaction_system()** (5 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **test_spawning_service_npc_room_event_handlers()** (5 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **test_spawning_service_threads_event_reaction_system_to_created_npcs()** (5 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **NPCSpawnStatistics** (4 connections) — `server/npc/spawning_service.py`
- **.__init__()** (4 connections) — `server/npc/spawning_models.py`
- **._count_spawn_reasons()** (4 connections) — `server/npc/spawning_service.py`
- **._count_spawn_types()** (4 connections) — `server/npc/spawning_service.py`
- **._handle_player_entered_room()** (4 connections) — `server/npc/spawning_service.py`
- **.process_spawn_queue()** (4 connections) — `server/npc/spawning_service.py`
- **._queue_spawn_request()** (4 connections) — `server/npc/spawning_service.py`
- **test_create_npc_instance_defaults_to_no_reaction_system()** (4 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **test_spawn_success_result()** (4 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **test_spawning_service_handle_player_entered_room()** (4 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- *... and 65 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (47 shared connections)
- [EventBus](EventBus.md) (26 shared connections)
- [event_types.py](event_types.py.md) (18 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (12 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)

## Source Files

- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 228 (88%)
- INFERRED: 32 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*