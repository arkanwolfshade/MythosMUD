# circuit breaker realtime

> 241 nodes

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **DeadLetterQueue** (37 connections) — `server/realtime/dead_letter_queue.py`
- **nats_message_handler.py** (34 connections) — `server/realtime/nats_message_handler.py`
- **test_circuit_breaker.py** (31 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_dead_letter_queue.py** (28 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **DeadLetterMessage** (27 connections) — `server/realtime/dead_letter_queue.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **EventHandler** (24 connections) — `server/realtime/event_handlers.py`
- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **nats_message_handler_processing.py** (23 connections) — `server/realtime/nats_message_handler_processing.py`
- **nats_message_handler_base.py** (19 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **CircuitBreakerOpen** (14 connections) — `server/realtime/circuit_breaker.py`
- **circuit_breaker.py** (12 connections) — `server/realtime/circuit_breaker.py`
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **dead_letter_queue.py** (10 connections) — `server/realtime/dead_letter_queue.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **nats_retry_handler.py** (10 connections) — `server/realtime/nats_retry_handler.py`
- **metrics_collector.py** (9 connections) — `server/middleware/metrics_collector.py`
- **.call()** (9 connections) — `server/realtime/circuit_breaker.py`
- **_ChatMessageFields** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- *... and 216 more nodes in this community*

## Relationships

- [nats exceptions services](nats_exceptions_services.md) (24 shared connections)
- [command inventory factories](command_inventory_factories.md) (18 shared connections)
- [realtime message filtering](realtime_message_filtering.md) (10 shared connections)
- [retry nats handler](retry_nats_handler.md) (9 shared connections)
- [Room Broadcast](Room_Broadcast.md) (7 shared connections)
- [instance game manager](instance_game_manager.md) (7 shared connections)
- [command admin setlucidity](command_admin_setlucidity.md) (6 shared connections)
- [services user manager](services_user_manager.md) (6 shared connections)
- [nats message handler](nats_message_handler.md) (5 shared connections)
- [combat services messaging](combat_services_messaging.md) (5 shared connections)
- [services service hallucination](services_service_hallucination.md) (4 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (4 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/realtime/circuit_breaker.py`
- `server/realtime/dead_letter_queue.py`
- `server/realtime/event_handlers.py`
- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 893 (95%)
- INFERRED: 51 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*