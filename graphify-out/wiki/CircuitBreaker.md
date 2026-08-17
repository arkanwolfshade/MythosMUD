# CircuitBreaker

> 89 nodes

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker.py** (33 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **CircuitState** (25 connections) — `server/realtime/circuit_breaker.py`
- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **CircuitBreakerOpen** (12 connections) — `server/realtime/circuit_breaker.py`
- **circuit_breaker.py** (12 connections) — `server/realtime/circuit_breaker.py`
- **.call()** (9 connections) — `server/realtime/circuit_breaker.py`
- **asyncio** (8 connections)
- **._transition_to()** (6 connections) — `server/realtime/circuit_breaker.py`
- **test_call_rejects_when_open()** (6 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_closes_from_half_open_on_success()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_failure_closed_state()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_opens_circuit_after_threshold()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_reopens_from_half_open_on_failure()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_transitions_to_half_open_after_timeout()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.get_stats()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_failure()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_success()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._time_until_retry()** (4 connections) — `server/realtime/circuit_breaker.py`
- **test_call_success_closed_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_opens_circuit_at_threshold()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_resets_success_count()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_increments_success_count_half_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- *... and 64 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [NATSMessageProcessingMixin](NATSMessageProcessingMixin.md) (7 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (4 shared connections)
- [NATSError](NATSError.md) (3 shared connections)
- [NATSMessageHandlerMixinBase](NATSMessageHandlerMixinBase.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (1 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (1 shared connections)
- [format_message_content](format_message_content.md) (1 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 143 (74%)
- INFERRED: 51 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*