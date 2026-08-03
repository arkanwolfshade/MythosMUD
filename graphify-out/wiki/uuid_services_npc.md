# uuid services npc

> 5 nodes

## Key Concepts

- **CircuitState** (6 connections) — `server/realtime/circuit_breaker.py`
- **.get_state()** (3 connections) — `server/realtime/circuit_breaker.py`
- **Enum** (2 connections)
- **Circuit breaker states.      - CLOSED: Normal operation, requests pass through** (1 connections) — `server/realtime/circuit_breaker.py`
- **Get current circuit state.          Returns:             Current CircuitState** (1 connections) — `server/realtime/circuit_breaker.py`

## Relationships

- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [realtime circuit breaker](realtime_circuit_breaker.md) (1 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (1 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*