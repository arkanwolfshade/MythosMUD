# NPCSpawningService

> 87 nodes

## Key Concepts

- **NPCSpawningService** (66 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **_spawn_success()** (8 connections) — `server/npc/spawning_request_execution.py`
- **._evaluate_spawn_requirements()** (8 connections) — `server/npc/spawning_service.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **_room_from_persistence()** (6 connections) — `server/npc/spawning_request_execution.py`
- **._calculate_spawn_priority()** (6 connections) — `server/npc/spawning_service.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- **._spawn_npc_from_request()** (6 connections) — `server/npc/spawning_service.py`
- **._check_spawn_requirements_for_room()** (5 connections) — `server/npc/spawning_service.py`
- **.get_spawn_statistics()** (5 connections) — `server/npc/spawning_service.py`
- **test_spawning_service_npc_room_event_handlers()** (5 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **NPCSpawnRequest** (5 connections)
- **NPCSpawnStatistics** (4 connections) — `server/npc/spawning_service.py`
- **.__init__()** (4 connections) — `server/npc/spawning_models.py`
- **._count_spawn_reasons()** (4 connections) — `server/npc/spawning_service.py`
- **._count_spawn_types()** (4 connections) — `server/npc/spawning_service.py`
- **._handle_player_entered_room()** (4 connections) — `server/npc/spawning_service.py`
- **.process_spawn_queue()** (4 connections) — `server/npc/spawning_service.py`
- **._queue_spawn_request()** (4 connections) — `server/npc/spawning_service.py`
- **test_spawn_success_result()** (4 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- *... and 62 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (62 shared connections)
- [EventBus](EventBus.md) (20 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (3 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (2 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)

## Source Files

- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 224 (89%)
- INFERRED: 29 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*