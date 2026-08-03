# circuit breaker realtime

> 18 nodes

## Key Concepts

- **test_circuit_breaker.py** (31 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_rejects_when_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_failure_closed_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_closes_from_half_open_on_success()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_increments_success_count_half_open()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_increments_failure_count()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_resets_success_count()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_zero_when_not_open()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_open_exception()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Unit tests for circuit breaker.  Tests the CircuitBreaker class and CircuitBreak** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() handles failure in CLOSED state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() raises CircuitBreakerOpen when circuit is OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() closes circuit from HALF_OPEN after success threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_success() increments success count in HALF_OPEN state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() increments failure count.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() resets success count.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns 0 when not OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreakerOpen exception.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [message broadcaster realtime](message_broadcaster_realtime.md) (13 shared connections)
- [event bus events](event_bus_events.md) (7 shared connections)
- [events event bus](events_event_bus.md) (5 shared connections)
- [message nats handler](message_nats_handler.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [uuid services npc](uuid_services_npc.md) (1 shared connections)
- [event events bus](event_events_bus.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 64 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*