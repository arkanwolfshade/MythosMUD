# Circuit Breaker Core

> 80 nodes · cohesion 0.04

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker.py** (30 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.call()** (9 connections) — `server/realtime/circuit_breaker.py`
- **.__init__()** (8 connections) — `server/realtime/nats_message_handler.py`
- **._transition_to()** (6 connections) — `server/realtime/circuit_breaker.py`
- **.get_stats()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_failure()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_success()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._time_until_retry()** (4 connections) — `server/realtime/circuit_breaker.py`
- **.get_state()** (3 connections) — `server/realtime/circuit_breaker.py`
- **.__init__()** (3 connections) — `server/realtime/circuit_breaker.py`
- **._should_attempt_reset()** (3 connections) — `server/realtime/circuit_breaker.py`
- **test_call_closes_from_half_open_on_success()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_failure_closed_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_opens_circuit_after_threshold()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_rejects_when_open()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_reopens_from_half_open_on_failure()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_success_closed_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_transitions_to_half_open_after_timeout()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_open_exception()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_stats_with_failure_time()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- *... and 55 more nodes in this community*

## Relationships

- [[NATS Chat Broadcasting]] (7 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Dead Letter Queue]] (1 shared connections)
- [[Realtime Event Handlers]] (1 shared connections)
- [[Chat Message Filtering]] (1 shared connections)
- [[NATS Retry Handler]] (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 241 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
