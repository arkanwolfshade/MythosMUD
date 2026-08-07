# Error Conversion

> 386 nodes

## Key Concepts

- **EventBus** (159 connections) — `server/events/event_bus.py`
- **PlayerEnteredRoom** (85 connections) — `server/events/event_types.py`
- **NPCLifecycleManager** (78 connections) — `server/npc/lifecycle_manager.py`
- **NPCSpawningService** (67 connections) — `server/npc/spawning_service.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **PlayerLeftRoom** (57 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (56 connections) — `server/events/event_types.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCLeftRoom** (52 connections) — `server/events/event_types.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **room.py** (30 connections) — `server/models/room.py`
- **MessageBuilder** (26 connections) — `server/realtime/message_builders.py`
- **NPCInstanceService** (24 connections) — `server/services/npc_instance_service.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **spawning_request_execution.py** (20 connections) — `server/npc/spawning_request_execution.py`
- **movement_integration.py** (19 connections) — `server/npc/movement_integration.py`
- **NPCSpawnRequest** (17 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (17 connections) — `server/npc/spawning_request_execution.py`
- **_SpawningServiceProtocol** (16 connections) — `server/npc/lifecycle_manager.py`
- **NPCSpawnResult** (16 connections) — `server/npc/spawning_models.py`
- **NPCSpawnStatistics** (16 connections) — `server/npc/spawning_service.py`
- *... and 361 more nodes in this community*

## Relationships

- [inventory mutation guard](inventory_mutation_guard.md) (110 shared connections)
- [room look commands](room_look_commands.md) (75 shared connections)
- [services nats service](services_nats_service.md) (44 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (26 shared connections)
- [party service game](party_service_game.md) (22 shared connections)
- [container events rationale](container_events_rationale.md) (22 shared connections)
- [EdgeCreationModal map STANDARD](EdgeCreationModal_map_STANDARD.md) (18 shared connections)
- [wearable container service](wearable_container_service.md) (17 shared connections)
- [combat services rationale](combat_services_rationale.md) (14 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (13 shared connections)
- [npc event handlers](npc_event_handlers.md) (13 shared connections)
- [nats services service](nats_services_service.md) (12 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/events/__init__.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/game/movement_service.py`
- `server/models/room.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/movement_integration.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/realtime/connection_event_helpers.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 1748 (88%)
- INFERRED: 229 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*