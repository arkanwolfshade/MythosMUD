# Test Circuit Breaker

> 14 nodes

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker_init()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_increments_success_count_half_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_when_not_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.reset()** (2 connections) — `server/realtime/circuit_breaker.py`
- **Manually reset circuit breaker to CLOSED state. Clears all counters and timers.…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Circuit breaker for NATS message processing. Implements Martin Fowler's circuit…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test _on_success() increments success count in HALF_OPEN state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreaker initialization.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns False when not OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_stats() returns comprehensive statistics.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreaker initialization with defaults.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [Test Circuit Breaker](Test_Circuit_Breaker.md) (31 shared connections)
- [Circuit Breaker](Circuit_Breaker.md) (8 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Event Handlers](Event_Handlers.md) (1 shared connections)
- [Nats Message Handler Broadcast](Nats_Message_Handler_Broadcast.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 45 (79%)
- INFERRED: 12 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*