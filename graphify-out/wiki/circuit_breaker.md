# circuit breaker

> 584 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **NATSRetryHandler** (42 connections) — `server/realtime/nats_retry_handler.py`
- **DeadLetterQueue** (37 connections) — `server/realtime/dead_letter_queue.py`
- **nats_message_handler.py** (34 connections) — `server/realtime/nats_message_handler.py`
- **test_nats_retry_handler.py** (34 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **NATSMessageSubscriptionMixin** (31 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **test_circuit_breaker.py** (31 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_dead_letter_queue.py** (28 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **DeadLetterMessage** (27 connections) — `server/realtime/dead_letter_queue.py`
- **envelope.py** (27 connections) — `server/realtime/envelope.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **EventHandler** (24 connections) — `server/realtime/event_handlers.py`
- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **nats_message_handler_processing.py** (23 connections) — `server/realtime/nats_message_handler_processing.py`
- **nats_message_handler_base.py** (19 connections) — `server/realtime/nats_message_handler_base.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **CircuitBreakerOpen** (14 connections) — `server/realtime/circuit_breaker.py`
- **MetricsCollector** (13 connections) — `server/middleware/metrics_collector.py`
- *... and 559 more nodes in this community*

## Relationships

- [Any](Any.md) (56 shared connections)
- [world](world.md) (29 shared connections)
- [Player](Player.md) (19 shared connections)
- [UUID](UUID.md) (9 shared connections)
- [. init ()](_init_%28%29.md) (8 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (7 shared connections)
- [time commands](time_commands.md) (7 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (6 shared connections)
- [.check and interrupt rest()](check_and_interrupt_rest%28%29.md) (6 shared connections)
- [.reset instance()](reset_instance%28%29.md) (5 shared connections)
- [get current tick()](get_current_tick%28%29.md) (4 shared connections)
- [close db()](close_db%28%29.md) (4 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/realtime/circuit_breaker.py`
- `server/realtime/dead_letter_queue.py`
- `server/realtime/envelope.py`
- `server/realtime/event_handlers.py`
- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/realtime/nats_retry_handler.py`
- `server/services/lucidity_communication_dampening.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 1980 (96%)
- INFERRED: 77 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*