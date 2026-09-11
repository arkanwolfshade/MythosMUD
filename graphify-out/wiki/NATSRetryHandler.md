# NATSRetryHandler

> 288 nodes

## Key Concepts

- **NATSRetryHandler** (42 connections) — `server/realtime/nats_retry_handler.py`
- **DeadLetterQueue** (40 connections) — `server/realtime/dead_letter_queue.py`
- **nats_exceptions.py** (38 connections) — `server/services/nats_exceptions.py`
- **nats_message_handler.py** (36 connections) — `server/realtime/nats_message_handler.py`
- **EventHandler** (33 connections) — `server/realtime/event_handlers.py`
- **test_dead_letter_queue.py** (29 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **DeadLetterMessage** (28 connections) — `server/realtime/dead_letter_queue.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **NATSMessageHandler** (25 connections) — `server/realtime/nats_message_handler.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **test_event_handlers_combat.py** (22 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **dead_letter_queue.py** (12 connections) — `server/realtime/dead_letter_queue.py`
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **nats_retry_handler.py** (11 connections) — `server/realtime/nats_retry_handler.py`
- **asyncio** (11 connections)
- **_send_combat_participant_updates()** (10 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **test_message_filtering_helpers.py** (10 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- *... and 263 more nodes in this community*

## Relationships

- [test_nats_retry_handler.py](test_nats_retry_handler.py.md) (32 shared connections)
- [get_logger](get_logger.md) (23 shared connections)
- [NATSError](NATSError.md) (17 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (12 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (10 shared connections)
- [build_event](build_event.md) (10 shared connections)
- [NATSService](NATSService.md) (8 shared connections)
- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [combat_service.py](combat_service.py.md) (6 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (4 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (4 shared connections)
- [UserManager](UserManager.md) (4 shared connections)

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
- `server/tests/unit/realtime/test_dead_letter_queue.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`
- `server/tests/unit/realtime/test_message_formatters.py`

## Audit Trail

- EXTRACTED: 617 (93%)
- INFERRED: 49 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*