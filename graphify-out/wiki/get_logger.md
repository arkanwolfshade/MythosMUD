# get_logger

> 746 nodes

## Key Concepts

- **get_logger()** (527 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (503 connections) — `server/structured_logging/enhanced_logging_config.py`
- **EventBus** (153 connections) — `server/events/event_bus.py`
- **time.py** (97 connections) — `server/container/bundles/time.py`
- **event_types.py** (87 connections) — `server/events/event_types.py`
- **BaseEvent** (81 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (76 connections) — `server/events/event_types.py`
- **NPCSpawningService** (66 connections) — `server/npc/spawning_service.py`
- **test_population_control.py** (66 connections) — `server/tests/unit/npc/test_population_control.py`
- **PlayerLeftRoom** (49 connections) — `server/events/event_types.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **threading.py** (47 connections) — `server/npc/threading.py`
- **NPCEnteredRoom** (46 connections) — `server/events/event_types.py`
- **npc_base.py** (45 connections) — `server/npc/npc_base.py`
- **NPCLeftRoom** (43 connections) — `server/events/event_types.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **player_event_handlers.py** (42 connections) — `server/realtime/player_event_handlers.py`
- **test_event_handler.py** (42 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **CommandValidator** (40 connections) — `server/validators/command_validator.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **PlayerDPUpdated** (38 connections) — `server/events/event_types.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **event_handler.py** (36 connections) — `server/realtime/event_handler.py`
- **player_combat_service.py** (36 connections) — `server/services/player_combat_service.py`
- *... and 721 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (118 shared connections)
- [NPCBase](NPCBase.md) (99 shared connections)
- [NPCDefinition](NPCDefinition.md) (56 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (55 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (48 shared connections)
- [build_event](build_event.md) (44 shared connections)
- [CombatInstance](CombatInstance.md) (41 shared connections)
- [NPCDied](NPCDied.md) (37 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (36 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (34 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (28 shared connections)
- [.__post_init__](__post_init__.md) (27 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/tracked_task_manager.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_input.py`
- `server/command_handler/processing.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/shutdown_process_termination.py`
- `server/commands/time_commands.py`
- `server/config/__init__.py`
- `server/config/models/cors.py`
- `server/container/bundles/time.py`
- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 3395 (92%)
- INFERRED: 290 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*