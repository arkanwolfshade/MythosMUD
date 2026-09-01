# CircuitBreaker

> 303 nodes

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **DeadLetterQueue** (40 connections) — `server/realtime/dead_letter_queue.py`
- **nats_message_handler.py** (36 connections) — `server/realtime/nats_message_handler.py`
- **test_circuit_breaker.py** (33 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_dead_letter_queue.py** (29 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **DeadLetterMessage** (28 connections) — `server/realtime/dead_letter_queue.py`
- **CircuitState** (25 connections) — `server/realtime/circuit_breaker.py`
- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **NATSMessageHandler** (25 connections) — `server/realtime/nats_message_handler.py`
- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **user_manager.py** (18 connections) — `server/services/user_manager.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **CircuitBreakerOpen** (12 connections) — `server/realtime/circuit_breaker.py`
- **circuit_breaker.py** (12 connections) — `server/realtime/circuit_breaker.py`
- **dead_letter_queue.py** (12 connections) — `server/realtime/dead_letter_queue.py`
- **._broadcast_to_room_with_filtering()** (11 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **nats_retry_handler.py** (10 connections) — `server/realtime/nats_retry_handler.py`
- **.call()** (9 connections) — `server/realtime/circuit_breaker.py`
- **message_formatters.py** (9 connections) — `server/realtime/message_formatters.py`
- *... and 278 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (20 shared connections)
- [NATSError](NATSError.md) (16 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (9 shared connections)
- [NATSService](NATSService.md) (9 shared connections)
- [EventHandler](EventHandler.md) (7 shared connections)
- [UserManager](UserManager.md) (6 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (5 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (3 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/realtime/dead_letter_queue.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/realtime/nats_retry_handler.py`
- `server/services/user_manager.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`
- `server/tests/unit/realtime/test_message_formatters.py`

## Audit Trail

- EXTRACTED: 597 (93%)
- INFERRED: 46 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*