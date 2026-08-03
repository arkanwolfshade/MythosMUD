# service services rescue

> 7 nodes

## Key Concepts

- **circuit_breaker.py** (12 connections) — `server/realtime/circuit_breaker.py`
- **CircuitState** (6 connections) — `server/realtime/circuit_breaker.py`
- **.get_state()** (3 connections) — `server/realtime/circuit_breaker.py`
- **Enum** (2 connections)
- **Circuit breaker pattern for NATS message processing.  Implements three-state cir** (1 connections) — `server/realtime/circuit_breaker.py`
- **Circuit breaker states.      - CLOSED: Normal operation, requests pass through** (1 connections) — `server/realtime/circuit_breaker.py`
- **Get current circuit state.          Returns:             Current CircuitState** (1 connections) — `server/realtime/circuit_breaker.py`

## Relationships

- [circuit breaker realtime](circuit_breaker_realtime.md) (3 shared connections)
- [config rationale reset](config_rationale_reset.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (2 shared connections)
- [container main rationale](container_main_rationale.md) (1 shared connections)
- [nats message handler](nats_message_handler.md) (1 shared connections)
- [occupant realtime formatter](occupant_realtime_formatter.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*