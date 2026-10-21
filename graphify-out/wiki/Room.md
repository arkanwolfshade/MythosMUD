# Room

> 344 nodes · cohesion 0.01

## Key Concepts

- **get_logger()** (559 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (534 connections) — `server/structured_logging/enhanced_logging_config.py`
- **async_persistence.py** (105 connections) — `server/async_persistence.py`
- **threading.py** (47 connections) — `server/npc/threading.py`
- **event_handler.py** (42 connections) — `server/realtime/event_handler.py`
- **nats_message_handler.py** (39 connections) — `server/realtime/nats_message_handler.py`
- **test_config_models.py** (32 connections) — `server/tests/unit/config/test_config_models.py`
- **nats_message_handler_processing.py** (31 connections) — `server/realtime/nats_message_handler_processing.py`
- **config/models/__init__.py** (28 connections) — `server/config/models/__init__.py`
- **time_service.py** (27 connections) — `server/time/time_service.py`
- **monitoring_dashboard.py** (26 connections) — `server/monitoring/monitoring_dashboard.py`
- **GameConfig** (25 connections) — `server/config/models/game.py`
- **exception_tracker.py** (23 connections) — `server/monitoring/exception_tracker.py`
- **combat_integration_base.py** (23 connections) — `server/npc/combat_integration_base.py`
- **user_manager.py** (23 connections) — `server/services/user_manager.py`
- **player_respawn_wrapper.py** (22 connections) — `server/game/player_respawn_wrapper.py`
- **movement_integration.py** (22 connections) — `server/npc/movement_integration.py`
- **connection_helpers.py** (22 connections) — `server/realtime/connection_helpers.py`
- **nats_message_handler_broadcast.py** (22 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **npc_service/__init__.py** (22 connections) — `server/services/npc_service/__init__.py`
- **app.py** (21 connections) — `server/config/models/app.py`
- **inventory_mutation_guard.py** (21 connections) — `server/services/inventory_mutation_guard.py`
- **player_death_service.py** (21 connections) — `server/services/player_death_service.py`
- **idle_movement.py** (20 connections) — `server/npc/idle_movement.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- *... and 319 more nodes in this community*

## Relationships

- [BaseEvent](BaseEvent.md) (47 shared connections)
- [look_container.py](look_container.py.md) (44 shared connections)
- [AttributeError](AttributeError.md) (42 shared connections)
- [command_parser.py](command_parser.py.md) (39 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (31 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (28 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (27 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (26 shared connections)
- [ErrorType](ErrorType.md) (24 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (22 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (21 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (21 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`
- `server/async_persistence.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/shutdown_process_termination.py`
- `server/config/models/__init__.py`
- `server/config/models/_helpers.py`
- `server/config/models/app.py`
- `server/config/models/chat_time.py`
- `server/config/models/cors.py`
- `server/config/models/game.py`
- `server/config/models/nats.py`
- `server/config/models/player_stats.py`
- `server/config/models/security_logging.py`
- `server/config/models/server_db.py`
- `server/game/chat_moderation.py`
- `server/game/chat_pose_manager.py`
- `server/game/chat_whisper_tracker.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/mechanics.py`
- `server/game/player_respawn_wrapper.py`

## Audit Trail

- EXTRACTED: 2273 (99%)
- INFERRED: 27 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*