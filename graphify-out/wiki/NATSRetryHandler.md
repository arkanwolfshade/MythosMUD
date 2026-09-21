# NATSRetryHandler

> 286 nodes

## Key Concepts

- **NATSRetryHandler** (42 connections) — `server/realtime/nats_retry_handler.py`
- **DeadLetterQueue** (40 connections) — `server/realtime/dead_letter_queue.py`
- **nats_message_handler.py** (36 connections) — `server/realtime/nats_message_handler.py`
- **test_nats_retry_handler.py** (34 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **EventHandler** (33 connections) — `server/realtime/event_handlers.py`
- **NATSMessageSubscriptionMixin** (31 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **NATSMessageBroadcastMixin** (26 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **NATSMessageHandler** (25 connections) — `server/realtime/nats_message_handler.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **test_event_handlers_combat.py** (22 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **RetryableMessage** (13 connections) — `server/realtime/nats_retry_handler.py`
- **asyncio** (13 connections)
- **dead_letter_queue.py** (12 connections) — `server/realtime/dead_letter_queue.py`
- **Any** (12 connections)
- **asyncio** (11 connections)
- **RetryConfig** (10 connections) — `server/realtime/nats_retry_handler.py`
- **_send_combat_participant_updates()** (10 connections) — `server/realtime/event_handlers.py`
- **.connection_manager()** (10 connections) — `server/realtime/nats_message_handler.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **nats_retry_handler.py** (10 connections) — `server/realtime/nats_retry_handler.py`
- **_as_event_data_dict()** (8 connections) — `server/realtime/event_handlers.py`
- *... and 261 more nodes in this community*

## Relationships

- [test_dead_letter_queue.py](test_dead_letter_queue.py.md) (36 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (16 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [apply_communication_dampening](apply_communication_dampening.md) (14 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (10 shared connections)
- [NATSError](NATSError.md) (10 shared connections)
- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [build_event](build_event.md) (6 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (3 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/realtime/event_handlers.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 562 (91%)
- INFERRED: 58 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*