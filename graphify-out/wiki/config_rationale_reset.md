# config rationale reset

> 17 nodes

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **.__init__()** (3 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker_init()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_closes_from_half_open_on_success()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_resets_failure_count_closed()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_before_timeout()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_when_not_open()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.reset()** (2 connections) — `server/realtime/circuit_breaker.py`
- **timedelta** (1 connections)
- **Circuit breaker for NATS message processing.      Implements Martin Fowler's cir** (1 connections) — `server/realtime/circuit_breaker.py`
- **Initialize circuit breaker.          Args:             failure_threshold: Number** (1 connections) — `server/realtime/circuit_breaker.py`
- **Manually reset circuit breaker to CLOSED state.          Clears all counters and** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test CircuitBreaker initialization.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() closes circuit from HALF_OPEN after success threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_success() resets failure count in CLOSED state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns False before timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns False when not OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [websocket handler realtime](websocket_handler_realtime.md) (15 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (9 shared connections)
- [occupant realtime formatter](occupant_realtime_formatter.md) (7 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (5 shared connections)
- [service services rescue](service_services_rescue.md) (2 shared connections)
- [container main rationale](container_main_rationale.md) (1 shared connections)
- [behavior engine npc](behavior_engine_npc.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 70 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*