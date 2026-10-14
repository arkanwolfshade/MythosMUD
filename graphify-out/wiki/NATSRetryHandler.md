# NATSRetryHandler

> 303 nodes

## Key Concepts

- **NATSRetryHandler** (42 connections) — `server/realtime/nats_retry_handler.py`
- **DeadLetterQueue** (40 connections) — `server/realtime/dead_letter_queue.py`
- **nats_message_handler.py** (39 connections) — `server/realtime/nats_message_handler.py`
- **NATSMessageHandler** (36 connections) — `server/realtime/nats_message_handler.py`
- **test_chat_segments.py** (34 connections) — `server/tests/unit/realtime/test_chat_segments.py`
- **test_nats_retry_handler.py** (34 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **nats_message_handler_processing.py** (31 connections) — `server/realtime/nats_message_handler_processing.py`
- **test_dead_letter_queue.py** (29 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **DeadLetterMessage** (28 connections) — `server/realtime/dead_letter_queue.py`
- **NATSMessageBroadcastMixin** (26 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **format_message_content()** (24 connections) — `server/realtime/message_formatters.py`
- **nats_message_handler_broadcast.py** (22 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **format_message_segments()** (16 connections) — `server/realtime/message_formatters.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **RetryableMessage** (13 connections) — `server/realtime/nats_retry_handler.py`
- **asyncio** (13 connections)
- **dead_letter_queue.py** (12 connections) — `server/realtime/dead_letter_queue.py`
- **RetryConfig** (10 connections) — `server/realtime/nats_retry_handler.py`
- **._broadcast_to_room_with_filtering()** (10 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **nats_retry_handler.py** (10 connections) — `server/realtime/nats_retry_handler.py`
- **disposition_or_none()** (8 connections) — `server/realtime/message_formatters.py`
- **._send_messages_to_players()** (8 connections) — `server/realtime/nats_message_handler_broadcast.py`
- *... and 278 more nodes in this community*

## Relationships

- [NpcDisposition](NpcDisposition.md) (22 shared connections)
- [get_logger](get_logger.md) (22 shared connections)
- [NATSError](NATSError.md) (21 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (12 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (10 shared connections)
- [ChatMessage](ChatMessage.md) (9 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (8 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (6 shared connections)
- [EventHandler](EventHandler.md) (5 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (4 shared connections)
- [ValueError](ValueError.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_chat_segments.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`
- `server/tests/unit/realtime/test_message_category_invariants.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 636 (92%)
- INFERRED: 52 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*