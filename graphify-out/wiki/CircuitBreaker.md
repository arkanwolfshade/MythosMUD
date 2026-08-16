# CircuitBreaker

> 62 nodes

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker.py** (33 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **CircuitState** (25 connections) — `server/realtime/circuit_breaker.py`
- **circuit_breaker.py** (12 connections) — `server/realtime/circuit_breaker.py`
- **asyncio** (8 connections)
- **test_call_rejects_when_open()** (6 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_closes_from_half_open_on_success()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_failure_closed_state()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_opens_circuit_after_threshold()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_reopens_from_half_open_on_failure()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_transitions_to_half_open_after_timeout()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_success_closed_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_opens_circuit_at_threshold()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_resets_success_count()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_increments_success_count_half_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_reset()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_before_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_when_not_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_true_after_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_remaining_time()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_zero_after_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_zero_when_not_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_transition_to_updates_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- *... and 37 more nodes in this community*

## Relationships

- [NATSRetryHandler](NATSRetryHandler.md) (8 shared connections)
- [.call](call.md) (8 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.reset](reset.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 95 (67%)
- INFERRED: 47 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*