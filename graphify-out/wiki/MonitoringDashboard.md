# MonitoringDashboard

> 83 nodes · cohesion 0.04

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker.py** (32 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **CircuitState** (25 connections) — `server/realtime/circuit_breaker.py`
- **CircuitBreakerOpen** (12 connections) — `server/realtime/circuit_breaker.py`
- **asyncio** (8 connections)
- **test_call_rejects_when_open()** (7 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **._transition_to()** (6 connections) — `server/realtime/circuit_breaker.py`
- **test_call_closes_from_half_open_on_success()** (6 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_failure_closed_state()** (6 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_opens_circuit_after_threshold()** (6 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_reopens_from_half_open_on_failure()** (6 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_transitions_to_half_open_after_timeout()** (6 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
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
- **test_reset()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_before_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_when_not_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- *... and 58 more nodes in this community*

## Relationships

- [Room](Room.md) (10 shared connections)
- [look_container.py](look_container.py.md) (8 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (6 shared connections)
- [NPCPopulationController](NPCPopulationController.md) (3 shared connections)
- [_handle_admin_hallucinate_command](_handle_admin_hallucinate_command.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 131 (78%)
- INFERRED: 38 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*