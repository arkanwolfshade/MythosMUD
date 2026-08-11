# Circuit Breaker Core

> 88 nodes

## Key Concepts

- **CircuitBreaker** (41 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker.py** (31 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **CircuitBreakerOpen** (12 connections) — `server/realtime/circuit_breaker.py`
- **.call()** (9 connections) — `server/realtime/circuit_breaker.py`
- **CircuitState** (6 connections) — `server/realtime/circuit_breaker.py`
- **._transition_to()** (6 connections) — `server/realtime/circuit_breaker.py`
- **._on_success()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_failure()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._time_until_retry()** (4 connections) — `server/realtime/circuit_breaker.py`
- **.get_stats()** (4 connections) — `server/realtime/circuit_breaker.py`
- **test_call_rejects_when_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.__init__()** (3 connections) — `server/realtime/circuit_breaker.py`
- **._should_attempt_reset()** (3 connections) — `server/realtime/circuit_breaker.py`
- **.get_state()** (3 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker_init()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_success_closed_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_failure_closed_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_opens_circuit_after_threshold()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_transitions_to_half_open_after_timeout()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_closes_from_half_open_on_success()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_reopens_from_half_open_on_failure()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_resets_failure_count_closed()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_increments_success_count_half_open()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_increments_failure_count()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- *... and 63 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (7 shared connections)
- [SQLAlchemy Model Base](SQLAlchemy_Model_Base.md) (3 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (2 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 261 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*