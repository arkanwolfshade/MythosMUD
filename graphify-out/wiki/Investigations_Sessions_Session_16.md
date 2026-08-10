# Investigations Sessions Session

> 15 nodes

## Key Concepts

- **.call()** (9 connections) — `server/realtime/circuit_breaker.py`
- **._transition_to()** (6 connections) — `server/realtime/circuit_breaker.py`
- **._on_success()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_failure()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._time_until_retry()** (4 connections) — `server/realtime/circuit_breaker.py`
- **.get_stats()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._should_attempt_reset()** (3 connections) — `server/realtime/circuit_breaker.py`
- **Any** (2 connections)
- **Execute function through circuit breaker.          Enforces circuit breaker logi** (1 connections) — `server/realtime/circuit_breaker.py`
- **Handle successful function call.          Updates state based on current circuit** (1 connections) — `server/realtime/circuit_breaker.py`
- **Handle failed function call.          Updates state based on failure count:** (1 connections) — `server/realtime/circuit_breaker.py`
- **Check if enough time has passed to attempt circuit reset.          Returns:** (1 connections) — `server/realtime/circuit_breaker.py`
- **Calculate seconds until circuit can attempt reset.          Returns:** (1 connections) — `server/realtime/circuit_breaker.py`
- **Transition circuit to new state.          Args:             new_state: State to** (1 connections) — `server/realtime/circuit_breaker.py`
- **Get circuit breaker statistics.          Returns:             Dictionary with ci** (1 connections) — `server/realtime/circuit_breaker.py`

## Relationships

- [Performance Optimization Summary](Performance_Optimization_Summary.md) (7 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (1 shared connections)
- [Commands Rest Countdown](Commands_Rest_Countdown.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*