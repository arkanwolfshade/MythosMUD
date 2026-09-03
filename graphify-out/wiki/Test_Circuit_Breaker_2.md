# Test Circuit Breaker

> 15 nodes

## Key Concepts

- **CircuitState** (25 connections) — `server/realtime/circuit_breaker.py`
- **circuit_breaker.py** (12 connections) — `server/realtime/circuit_breaker.py`
- **test_on_failure_opens_circuit_at_threshold()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_true_after_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_remaining_time()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_zero_when_not_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.get_state()** (3 connections) — `server/realtime/circuit_breaker.py`
- **Enum** (2 connections)
- **Circuit breaker pattern for NATS message processing. Implements three-state…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Circuit breaker states. - CLOSED: Normal operation, requests pass through -…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Get current circuit state. Returns: Current CircuitState AI: For monitoring and…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test _on_failure() opens circuit at threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns True after timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns 0 when not OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns remaining time.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [Test Circuit Breaker](Test_Circuit_Breaker.md) (28 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (5 shared connections)
- [Circuit Breaker](Circuit_Breaker.md) (1 shared connections)
- [Test Nats Message Handler](Test_Nats_Message_Handler.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 31 (62%)
- INFERRED: 19 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*