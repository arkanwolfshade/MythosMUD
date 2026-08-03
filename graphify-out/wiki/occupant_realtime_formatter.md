# occupant realtime formatter

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

- [config rationale reset](config_rationale_reset.md) (7 shared connections)
- [container main rationale](container_main_rationale.md) (1 shared connections)
- [service services rescue](service_services_rescue.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*