# Error Conversion

> 732 nodes

## Key Concepts

- **get_logger()** (522 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (496 connections) — `server/structured_logging/enhanced_logging_config.py`
- **EventBus** (159 connections) — `server/events/event_bus.py`
- **time.py** (96 connections) — `server/container/bundles/time.py`
- **event_types.py** (86 connections) — `server/events/event_types.py`
- **NPCLifecycleManager** (78 connections) — `server/npc/lifecycle_manager.py`
- **BaseEvent** (75 connections) — `server/events/event_types.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **NPCEnteredRoom** (56 connections) — `server/events/event_types.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCLeftRoom** (52 connections) — `server/events/event_types.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **threading.py** (48 connections) — `server/npc/threading.py`
- **npc_base.py** (44 connections) — `server/npc/npc_base.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **__init__.py** (42 connections) — `server/services/__init__.py`
- **npc.py** (38 connections) — `server/models/npc.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **NPCDied** (35 connections) — `server/events/event_types.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **event_bus.py** (31 connections) — `server/events/event_bus.py`
- **room.py** (30 connections) — `server/models/room.py`
- **event_reaction_system.py** (29 connections) — `server/npc/event_reaction_system.py`
- **movement_service.py** (28 connections) — `server/game/movement_service.py`
- *... and 707 more nodes in this community*

## Relationships

- [lucidity event services](lucidity_event_services.md) (110 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (94 shared connections)
- [profession models rationale](profession_models_rationale.md) (84 shared connections)
- [party service game](party_service_game.md) (49 shared connections)
- [room look commands](room_look_commands.md) (49 shared connections)
- [container events rationale](container_events_rationale.md) (47 shared connections)
- [commands npc admin](commands_npc_admin.md) (36 shared connections)
- [nats services service](nats_services_service.md) (32 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (32 shared connections)
- [task registry app](task_registry_app.md) (30 shared connections)
- [follow game service](follow_game_service.md) (29 shared connections)
- [combat services rationale](combat_services_rationale.md) (28 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/tracked_task_manager.py`
- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/shutdown_process_termination.py`
- `server/commands/time_commands.py`
- `server/config/models/_helpers.py`
- `server/config/models/nats.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/time.py`
- `server/container/utils.py`
- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`

## Audit Trail

- EXTRACTED: 4887 (94%)
- INFERRED: 289 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*