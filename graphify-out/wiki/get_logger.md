# get_logger

> 837 nodes

## Key Concepts

- **get_logger()** (509 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (484 connections) — `server/structured_logging/enhanced_logging_config.py`
- **build_event()** (117 connections) — `server/realtime/envelope.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **NATSError** (60 connections) — `server/services/nats_exceptions.py`
- **nats_message_handler.py** (39 connections) — `server/realtime/nats_message_handler.py`
- **AttributeError** (38 connections)
- **admin_teleport_commands.py** (38 connections) — `server/commands/admin_teleport_commands.py`
- **test_connection_helpers_impl.py** (36 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **websocket_room_updates.py** (32 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates.py** (32 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **nats_exceptions.py** (30 connections) — `server/services/nats_exceptions.py`
- **admin_setstat_command.py** (28 connections) — `server/commands/admin_setstat_command.py`
- **envelope.py** (28 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **NATSSubscribeError** (25 connections) — `server/services/nats_exceptions.py`
- **get_admin_actions_logger()** (25 connections) — `server/structured_logging/admin_actions_logger.py`
- **processing.py** (25 connections) — `server/command_handler/processing.py`
- **config/models/__init__.py** (24 connections) — `server/config/models/__init__.py`
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **teleport_helpers.py** (23 connections) — `server/commands/teleport_helpers.py`
- **event_handlers.py** (23 connections) — `server/realtime/event_handlers.py`
- **message_handler_factory.py** (23 connections) — `server/realtime/message_handler_factory.py`
- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **nats_service.py** (23 connections) — `server/services/nats_service.py`
- *... and 812 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (94 shared connections)
- [combat_service.py](combat_service.py.md) (73 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (62 shared connections)
- [AliasStorage](AliasStorage.md) (53 shared connections)
- [time.py](time.py.md) (52 shared connections)
- [Player](Player.md) (52 shared connections)
- [AppConfig](AppConfig.md) (42 shared connections)
- [EventBus](EventBus.md) (39 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (28 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (26 shared connections)
- [connection_manager.py](connection_manager.py.md) (24 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (23 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`
- `server/api/base.py`
- `server/app/lifespan_event_subscriptions.py`
- `server/app/task_registry.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_input.py`
- `server/command_handler/processing.py`
- `server/commands/admin_permission_utils.py`
- `server/commands/admin_setstat_command.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/goto_helpers.py`
- `server/commands/teleport_helpers.py`
- `server/commands/time_commands.py`
- `server/config/__init__.py`
- `server/config/models/__init__.py`
- `server/config/models/_helpers.py`
- `server/config/models/app.py`

## Audit Trail

- EXTRACTED: 3116 (97%)
- INFERRED: 97 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*