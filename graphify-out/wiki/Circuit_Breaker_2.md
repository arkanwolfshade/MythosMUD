# Circuit Breaker

> 15 nodes

## Key Concepts

- **.call()** (9 connections) — `server/realtime/circuit_breaker.py`
- **._transition_to()** (6 connections) — `server/realtime/circuit_breaker.py`
- **.get_stats()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_failure()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_success()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._time_until_retry()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._should_attempt_reset()** (3 connections) — `server/realtime/circuit_breaker.py`
- **Any** (2 connections)
- **Handle successful function call. Updates state based on current circuit state:…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Handle failed function call. Updates state based on failure count: - Increments…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Check if enough time has passed to attempt circuit reset. Returns: True if…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Calculate seconds until circuit can attempt reset. Returns: Seconds until retry…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Transition circuit to new state. Args: new_state: State to transition to AI:…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Get circuit breaker statistics. Returns: Dictionary with circuit breaker…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Execute function through circuit breaker. Enforces circuit breaker logic: -…** (1 connections) — `server/realtime/circuit_breaker.py`

## Relationships

- [Test Circuit Breaker](Test_Circuit_Breaker.md) (9 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*