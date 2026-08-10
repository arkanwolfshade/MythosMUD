# Commands Rest Countdown

> 7 nodes

## Key Concepts

- **circuit_breaker.py** (10 connections) — `server/realtime/circuit_breaker.py`
- **CircuitState** (6 connections) — `server/realtime/circuit_breaker.py`
- **.get_state()** (3 connections) — `server/realtime/circuit_breaker.py`
- **Enum** (2 connections)
- **Circuit breaker pattern for NATS message processing.  Implements three-state cir** (1 connections) — `server/realtime/circuit_breaker.py`
- **Circuit breaker states.      - CLOSED: Normal operation, requests pass through** (1 connections) — `server/realtime/circuit_breaker.py`
- **Get current circuit state.          Returns:             Current CircuitState** (1 connections) — `server/realtime/circuit_breaker.py`

## Relationships

- [Performance Optimization Summary](Performance_Optimization_Summary.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Circuit Breaker Core](Circuit_Breaker_Core.md) (2 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [SQLAlchemy Model Base](SQLAlchemy_Model_Base.md) (1 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*