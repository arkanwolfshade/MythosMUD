# CircuitBreaker

> 26 nodes

## Key Concepts

- **CircuitBreaker** (16 connections) — `server/legacy_error_handlers.py`
- **TestCircuitBreaker** (10 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.call()** (7 connections) — `server/legacy_error_handlers.py`
- **._on_failure()** (3 connections) — `server/legacy_error_handlers.py`
- **._on_success()** (3 connections) — `server/legacy_error_handlers.py`
- **._should_attempt_reset()** (3 connections) — `server/legacy_error_handlers.py`
- **.test_circuit_breaker_failure()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_circuit_breaker_half_open_reset()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_circuit_breaker_initialization()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_circuit_breaker_open_raises_error()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_circuit_breaker_opens_after_threshold()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_circuit_breaker_success()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.__init__()** (1 connections) — `server/legacy_error_handlers.py`
- **_CircuitBreakerResult** (1 connections)
- **Simple circuit breaker pattern implementation. Provides fault tolerance for…** (1 connections) — `server/legacy_error_handlers.py`
- **Execute function with circuit breaker protection. Args: func: Function to…** (1 connections) — `server/legacy_error_handlers.py`
- **Handle successful operation.** (1 connections) — `server/legacy_error_handlers.py`
- **Handle failed operation.** (1 connections) — `server/legacy_error_handlers.py`
- **Check if circuit breaker should attempt reset.** (1 connections) — `server/legacy_error_handlers.py`
- **Test CircuitBreaker class.** (1 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Test CircuitBreaker initialization.** (1 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Test CircuitBreaker with successful call.** (1 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Test CircuitBreaker with failure.** (1 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Test CircuitBreaker opens after threshold.** (1 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Test CircuitBreaker raises error when open.** (1 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- *... and 1 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (6 shared connections)

## Source Files

- `server/legacy_error_handlers.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 37 (92%)
- INFERRED: 3 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*