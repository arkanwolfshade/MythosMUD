# get_logger

> 1196 nodes

## Key Concepts

- **get_logger()** (525 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (500 connections) — `server/structured_logging/enhanced_logging_config.py`
- **connection_manager.py** (167 connections) — `server/realtime/connection_manager.py`
- **EventBus** (153 connections) — `server/events/event_bus.py`
- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **time.py** (96 connections) — `server/container/bundles/time.py`
- **event_types.py** (86 connections) — `server/events/event_types.py`
- **async_persistence.py** (82 connections) — `server/async_persistence.py`
- **BaseEvent** (81 connections) — `server/events/event_types.py`
- **game_tick_processing.py** (81 connections) — `server/app/game_tick_processing.py`
- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **PlayerEnteredRoom** (75 connections) — `server/events/event_types.py`
- **NPCLifecycleManager** (69 connections) — `server/npc/lifecycle_manager.py`
- **NPCSpawningService** (66 connections) — `server/npc/spawning_service.py`
- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **lifespan_startup.py** (63 connections) — `server/app/lifespan_startup.py`
- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **MessageQueue** (58 connections) — `server/realtime/message_queue.py`
- **npc_combat_integration_service.py** (53 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **RoomSubscriptionManager** (50 connections) — `server/realtime/room_subscription_manager.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **PlayerLeftRoom** (48 connections) — `server/events/event_types.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- *... and 1171 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (126 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (116 shared connections)
- [NPCDied](NPCDied.md) (95 shared connections)
- [Player](Player.md) (93 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (63 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (54 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (53 shared connections)
- [DistributedEventBus](DistributedEventBus.md) (48 shared connections)
- [RateLimiter](RateLimiter.md) (47 shared connections)
- [Any](Any.md) (46 shared connections)
- [asyncio](asyncio.md) (41 shared connections)
- [CombatService](CombatService.md) (37 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`
- `server/api/admin/npc.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/base.py`
- `server/app/game_tick_processing.py`
- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/tracked_task_manager.py`
- `server/async_persistence.py`
- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler/processing.py`
- `server/commands/combat_handler.py`
- `server/commands/container_helpers_inventory_logging.py`

## Audit Trail

- EXTRACTED: 5305 (93%)
- INFERRED: 427 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*