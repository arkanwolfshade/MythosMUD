# websocket handler realtime

> 20 nodes

## Key Concepts

- **test_circuit_breaker.py** (31 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_opens_circuit_after_threshold()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_reopens_from_half_open_on_failure()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_increments_success_count_half_open()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_increments_failure_count()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_remaining_time()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_reset()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Unit tests for circuit breaker.  Tests the CircuitBreaker class and CircuitBreak** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreaker initialization with defaults.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() opens circuit after failure threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() reopens circuit from HALF_OPEN on failure.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_success() increments success count in HALF_OPEN state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() increments failure count.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns remaining time.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_state() returns current state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_stats() returns comprehensive statistics.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test reset() manually resets circuit breaker.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [config rationale reset](config_rationale_reset.md) (15 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (9 shared connections)
- [container main rationale](container_main_rationale.md) (3 shared connections)
- [service services rescue](service_services_rescue.md) (2 shared connections)
- [behavior engine npc](behavior_engine_npc.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 68 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*