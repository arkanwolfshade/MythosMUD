# circuit breaker realtime

> 440 nodes

## Key Concepts

- **NATSRetryHandler** (42 connections) — `server/realtime/nats_retry_handler.py`
- **DeadLetterQueue** (37 connections) — `server/realtime/dead_letter_queue.py`
- **EventHandler** (34 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler.py** (34 connections) — `server/realtime/nats_message_handler.py`
- **test_nats_retry_handler.py** (34 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **NATSMessageSubscriptionMixin** (31 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **test_dead_letter_queue.py** (28 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **DeadLetterMessage** (27 connections) — `server/realtime/dead_letter_queue.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **nats_message_handler_processing.py** (23 connections) — `server/realtime/nats_message_handler_processing.py`
- **test_event_handlers_combat.py** (22 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **user_manager.py** (20 connections) — `server/services/user_manager.py`
- **NATSMessageHandlerMixinBase** (19 connections) — `server/realtime/nats_message_handler_base.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **extract_subzone_from_room_id()** (15 connections) — `server/utils/room_utils.py`
- **RetryableMessage** (13 connections) — `server/realtime/nats_retry_handler.py`
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **._broadcast_to_room_with_filtering()** (12 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **Any** (12 connections)
- *... and 415 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (31 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (25 shared connections)
- [Room Broadcast](Room_Broadcast.md) (13 shared connections)
- [startup npc services](startup_npc_services.md) (13 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (8 shared connections)
- [services user manager](services_user_manager.md) (8 shared connections)
- [combat services messaging](combat_services_messaging.md) (7 shared connections)
- [room rationale subzone](room_rationale_subzone.md) (6 shared connections)
- [config rationale reset](config_rationale_reset.md) (5 shared connections)
- [command parser rationale](command_parser_rationale.md) (4 shared connections)
- [container main rationale](container_main_rationale.md) (4 shared connections)
- [middleware metrics collector](middleware_metrics_collector.md) (3 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/realtime/dead_letter_queue.py`
- `server/realtime/event_handlers.py`
- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/realtime/nats_retry_handler.py`
- `server/services/user_manager.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 1503 (96%)
- INFERRED: 65 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*