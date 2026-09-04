# Test Circuit Breaker

> 7 nodes

## Key Concepts

- **CircuitBreakerOpen** (12 connections) — `server/realtime/circuit_breaker.py`
- **test_call_rejects_when_open()** (6 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_open_exception()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Exception** (1 connections)
- **Exception raised when circuit breaker is open. Indicates the protected service…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test CircuitBreakerOpen exception.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() raises CircuitBreakerOpen when circuit is OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [Test Circuit Breaker](Test_Circuit_Breaker.md) (7 shared connections)
- [Test Nats Message Handler](Test_Nats_Message_Handler.md) (3 shared connections)
- [Circuit Breaker](Circuit_Breaker.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Nats Message Handler Processing](Nats_Message_Handler_Processing.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 13 (68%)
- INFERRED: 6 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*