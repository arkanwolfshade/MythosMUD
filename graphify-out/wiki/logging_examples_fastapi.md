# logging examples fastapi

> 397 nodes

## Key Concepts

- **get_logger()** (522 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (496 connections) — `server/structured_logging/enhanced_logging_config.py`
- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **time.py** (96 connections) — `server/container/bundles/time.py`
- **threading.py** (48 connections) — `server/npc/threading.py`
- **nats_message_handler.py** (34 connections) — `server/realtime/nats_message_handler.py`
- **DeadLetterMessage** (27 connections) — `server/realtime/dead_letter_queue.py`
- **envelope.py** (27 connections) — `server/realtime/envelope.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **test_message_handlers.py** (24 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **nats_message_handler_processing.py** (23 connections) — `server/realtime/nats_message_handler_processing.py`
- **connection_helpers.py** (21 connections) — `server/realtime/connection_helpers.py`
- **inventory_mutation_guard.py** (21 connections) — `server/services/inventory_mutation_guard.py`
- **optimized_security_validator.py** (21 connections) — `server/validators/optimized_security_validator.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **user_manager.py** (20 connections) — `server/services/user_manager.py`
- **passive_mob_npc.py** (19 connections) — `server/npc/passive_mob_npc.py`
- **NATSMessageHandlerMixinBase** (19 connections) — `server/realtime/nats_message_handler_base.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **handle_chat_message()** (18 connections) — `server/realtime/websocket_handler.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **detect_environment()** (16 connections) — `server/structured_logging/logging_utilities.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **migrate_combat_data.py** (15 connections) — `server/scripts/migrate_combat_data.py`
- *... and 372 more nodes in this community*

## Relationships

- [inventory mutation guard](inventory_mutation_guard.md) (37 shared connections)
- [nats services service](nats_services_service.md) (34 shared connections)
- [services nats service](services_nats_service.md) (26 shared connections)
- [Error Conversion](Error_Conversion.md) (26 shared connections)
- [spell game magic](spell_game_magic.md) (26 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (25 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (24 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (22 shared connections)
- [combat npc mixin](combat_npc_mixin.md) (21 shared connections)
- [add used user](add_used_user.md) (20 shared connections)
- [logging handlers structured](logging_handlers_structured.md) (18 shared connections)
- [logging structured utilities](logging_structured_utilities.md) (18 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/api/base.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/rest_countdown_task.py`
- `server/commands/shutdown_process_termination.py`
- `server/commands/system_commands.py`
- `server/container/bundles/time.py`
- `server/game/chat_pose_manager.py`
- `server/game/instance_manager.py`
- `server/game/level_service.py`
- `server/game/player_search_service.py`
- `server/help/help_content.py`
- `server/middleware/metrics_collector.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/npc/behavior_engine.py`
- `server/npc/npc_combat_schedule.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/threading.py`

## Audit Trail

- EXTRACTED: 2909 (98%)
- INFERRED: 48 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*