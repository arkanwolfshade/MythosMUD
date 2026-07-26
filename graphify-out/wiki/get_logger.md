# get_logger

> 1198 nodes · cohesion 0.00

## Key Concepts

- **get_logger()** (506 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (480 connections) — `server/structured_logging/enhanced_logging_config.py`
- **EventBus** (129 connections) — `server/events/event_bus.py`
- **NPCDefinition** (119 connections) — `server/models/npc.py`
- **time.py** (89 connections) — `server/container/bundles/time.py`
- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **NPCLifecycleManager** (76 connections) — `server/npc/lifecycle_manager.py`
- **event_types.py** (74 connections) — `server/events/event_types.py`
- **async_persistence.py** (73 connections) — `server/async_persistence.py`
- **BaseEvent** (73 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (68 connections) — `server/events/event_types.py`
- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCEnteredRoom** (51 connections) — `server/events/event_types.py`
- **PlayerLeftRoom** (51 connections) — `server/events/event_types.py`
- **NPCSpawningService** (50 connections) — `server/npc/spawning_service.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **threading.py** (47 connections) — `server/npc/threading.py`
- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- *... and 1173 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (128 shared connections)
- [npc_base.py](npc_base.py.md) (82 shared connections)
- [__init__.py](__init__.py.md) (77 shared connections)
- [ConnectionManager](ConnectionManager.md) (70 shared connections)
- [DatabaseError](DatabaseError.md) (64 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (62 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (55 shared connections)
- [Player](Player.md) (52 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (33 shared connections)
- [router.py](router.py.md) (33 shared connections)
- [exceptions.py](exceptions.py.md) (32 shared connections)
- [AliasStorage](AliasStorage.md) (32 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/api/game.py`
- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/tracked_task_manager.py`
- `server/async_persistence.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/shutdown_process_termination.py`
- `server/commands/time_commands.py`
- `server/config/models/security_logging.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/time.py`
- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`

## Audit Trail

- EXTRACTED: 6632 (93%)
- INFERRED: 479 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*