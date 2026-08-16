# NATSRetryHandler

> 356 nodes

## Key Concepts

- **NATSRetryHandler** (42 connections) — `server/realtime/nats_retry_handler.py`
- **DeadLetterQueue** (37 connections) — `server/realtime/dead_letter_queue.py`
- **nats_message_handler.py** (35 connections) — `server/realtime/nats_message_handler.py`
- **test_nats_retry_handler.py** (35 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **EventHandler** (33 connections) — `server/realtime/event_handlers.py`
- **NATSMessageSubscriptionMixin** (31 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **DeadLetterMessage** (28 connections) — `server/realtime/dead_letter_queue.py`
- **test_dead_letter_queue.py** (28 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **NATSMessageHandler** (23 connections) — `server/realtime/nats_message_handler.py`
- **test_event_handlers_combat.py** (23 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **user_manager.py** (21 connections) — `server/services/user_manager.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **RetryableMessage** (13 connections) — `server/realtime/nats_retry_handler.py`
- **asyncio** (13 connections)
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **Any** (12 connections)
- **dead_letter_queue.py** (11 connections) — `server/realtime/dead_letter_queue.py`
- **asyncio** (11 connections)
- **RetryConfig** (10 connections) — `server/realtime/nats_retry_handler.py`
- *... and 331 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (26 shared connections)
- [CombatInstance](CombatInstance.md) (17 shared connections)
- [test_message_formatters.py](test_message_formatters.py.md) (13 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (8 shared connections)
- [build_event](build_event.md) (8 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (6 shared connections)
- [UserManager](UserManager.md) (6 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (5 shared connections)
- [_Handler](_Handler.md) (3 shared connections)
- [realtime/conftest.py](realtime-conftest.py.md) (3 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (3 shared connections)

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
- `server/services/user_manager.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 623 (85%)
- INFERRED: 111 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*