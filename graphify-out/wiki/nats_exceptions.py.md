# nats_exceptions.py

> 142 nodes

## Key Concepts

- **nats_exceptions.py** (37 connections) — `server/services/nats_exceptions.py`
- **nats_message_handler.py** (36 connections) — `server/realtime/nats_message_handler.py`
- **EventHandler** (33 connections) — `server/realtime/event_handlers.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **test_event_handlers_combat.py** (23 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **dead_letter_queue.py** (12 connections) — `server/realtime/dead_letter_queue.py`
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **asyncio** (11 connections)
- **_send_combat_participant_updates()** (10 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **nats_retry_handler.py** (10 connections) — `server/realtime/nats_retry_handler.py`
- **message_formatters.py** (9 connections) — `server/realtime/message_formatters.py`
- **_as_event_data_dict()** (8 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (8 connections) — `server/realtime/event_handlers.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **_publish_npc_died_to_event_bus()** (6 connections) — `server/realtime/event_handlers.py`
- **_refresh_room_after_npc_death()** (6 connections) — `server/realtime/event_handlers.py`
- **_ChatMessageFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- *... and 117 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (22 shared connections)
- [NATSError](NATSError.md) (18 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (10 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (8 shared connections)
- [UserManager](UserManager.md) (8 shared connections)
- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (7 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (7 shared connections)
- [build_event](build_event.md) (6 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (5 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (5 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (4 shared connections)

## Source Files

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
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`
- `server/tests/unit/realtime/test_message_formatters.py`

## Audit Trail

- EXTRACTED: 372 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*