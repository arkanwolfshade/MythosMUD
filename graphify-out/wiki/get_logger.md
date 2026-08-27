# get_logger

> 505 nodes

## Key Concepts

- **get_logger()** (530 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (505 connections) — `server/structured_logging/enhanced_logging_config.py`
- **npc_combat_integration_service.py** (53 connections) — `server/services/npc_combat_integration_service.py`
- **AppConfig** (35 connections) — `server/config/models/app.py`
- **DeadLetterMessage** (28 connections) — `server/realtime/dead_letter_queue.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **config/models/__init__.py** (28 connections) — `server/config/models/__init__.py`
- **server/config/__init__.py** (26 connections) — `server/config/__init__.py`
- **test_config_models.py** (25 connections) — `server/tests/unit/config/test_config_models.py`
- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **app.py** (22 connections) — `server/config/models/app.py`
- **SchemaValidator** (21 connections) — `schemas/validator.py`
- **optimized_security_validator.py** (21 connections) — `server/validators/optimized_security_validator.py`
- **npc_combat_integration_validation_mixin.py** (20 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **GameConfig** (19 connections) — `server/config/models/game.py`
- **NPCCombatHandlers** (18 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **user_manager.py** (18 connections) — `server/services/user_manager.py`
- **chat_logger.py** (17 connections) — `server/services/chat_logger.py`
- **command_validator.py** (17 connections) — `server/validators/command_validator.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **emote_service.py** (16 connections) — `server/game/emote_service.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **npc_combat_handlers.py** (16 connections) — `server/services/npc_combat_handlers.py`
- *... and 480 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (53 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (48 shared connections)
- [ValidationError](ValidationError.md) (37 shared connections)
- [AliasStorage](AliasStorage.md) (29 shared connections)
- [time.py](time.py.md) (25 shared connections)
- [get_config](get_config.md) (24 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (24 shared connections)
- [event_types.py](event_types.py.md) (22 shared connections)
- [connection_manager.py](connection_manager.py.md) (22 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (20 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (19 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (18 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`
- `schemas/validator.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/config/__init__.py`
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
- `server/container/utils.py`
- `server/game/chat_pose_manager.py`
- `server/game/emote_service.py`
- `server/game/items/component_hooks.py`
- `server/game/level_service.py`

## Audit Trail

- EXTRACTED: 2147 (98%)
- INFERRED: 52 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*