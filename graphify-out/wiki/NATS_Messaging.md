# NATS Messaging

> 1115 nodes

## Key Concepts

- **get_logger()** (516 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (489 connections) — `server/structured_logging/enhanced_logging_config.py`
- **AsyncPersistenceLayer** (184 connections) — `server/async_persistence.py`
- **EventBus** (135 connections) — `server/events/event_bus.py`
- **time.py** (89 connections) — `server/container/bundles/time.py`
- **event_types.py** (79 connections) — `server/events/event_types.py`
- **async_persistence.py** (73 connections) — `server/async_persistence.py`
- **BaseEvent** (73 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (71 connections) — `server/events/event_types.py`
- **PlayerLeftRoom** (53 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (51 connections) — `server/events/event_types.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **threading.py** (47 connections) — `server/npc/threading.py`
- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **npc_base.py** (44 connections) — `server/npc/npc_base.py`
- **test_follow_service.py** (41 connections) — `server/tests/unit/game/test_follow_service.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **FollowService** (37 connections) — `server/game/follow_service.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **nats_message_handler.py** (34 connections) — `server/realtime/nats_message_handler.py`
- *... and 1090 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (241 shared connections)
- [Item Instances](Item_Instances.md) (101 shared connections)
- [NPC Combat](NPC_Combat.md) (59 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (57 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (50 shared connections)
- [command inventory factories](command_inventory_factories.md) (45 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (43 shared connections)
- [Room Broadcast](Room_Broadcast.md) (42 shared connections)
- [npc populate databases](npc_populate_databases.md) (37 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (31 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (31 shared connections)
- [chat game message](chat_game_message.md) (31 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/app/lifespan_event_subscriptions.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`
- `server/async_persistence.py`
- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/commands/combat_handler.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/shutdown_process_termination.py`
- `server/commands/teach_command.py`
- `server/config/models/cors.py`
- `server/constants/spawn_defaults.py`
- `server/container/bundles/time.py`
- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`

## Audit Trail

- EXTRACTED: 6298 (94%)
- INFERRED: 399 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*