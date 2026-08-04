# websocket handler realtime

> 132 nodes

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **nats_message_handler.py** (34 connections) — `server/realtime/nats_message_handler.py`
- **test_circuit_breaker.py** (31 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **DeadLetterMessage** (27 connections) — `server/realtime/dead_letter_queue.py`
- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **nats_message_handler_processing.py** (23 connections) — `server/realtime/nats_message_handler_processing.py`
- **NATSMessageHandlerMixinBase** (19 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **CircuitBreakerOpen** (14 connections) — `server/realtime/circuit_breaker.py`
- **circuit_breaker.py** (12 connections) — `server/realtime/circuit_breaker.py`
- **dead_letter_queue.py** (10 connections) — `server/realtime/dead_letter_queue.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.call()** (9 connections) — `server/realtime/circuit_breaker.py`
- **_ChatMessageFields** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **CircuitState** (6 connections) — `server/realtime/circuit_breaker.py`
- **._transition_to()** (6 connections) — `server/realtime/circuit_breaker.py`
- **._handle_nats_message()** (6 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_message_with_retry()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._extract_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._validate_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._broadcast_by_channel_type()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- *... and 107 more nodes in this community*

## Relationships

- [container persistence rationale](container_persistence_rationale.md) (25 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (16 shared connections)
- [Loot Generation](Loot_Generation.md) (10 shared connections)
- [middleware metrics collector](middleware_metrics_collector.md) (8 shared connections)
- [follow game service](follow_game_service.md) (5 shared connections)
- [startup npc services](startup_npc_services.md) (5 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (5 shared connections)
- [combat validator validators](combat_validator_validators.md) (5 shared connections)
- [nats message handler](nats_message_handler.md) (4 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (4 shared connections)
- [message broadcast realtime](message_broadcast_realtime.md) (3 shared connections)
- [realtime messaging message](realtime_messaging_message.md) (3 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/realtime/dead_letter_queue.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 495 (92%)
- INFERRED: 43 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*