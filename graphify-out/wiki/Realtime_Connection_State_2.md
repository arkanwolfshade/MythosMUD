# Realtime Connection State

> 8 nodes · cohesion 0.25

## Key Concepts

- **.on_enter_state()** (4 connections) — `server/realtime/connection_state_machine.py`
- **.get_stats()** (3 connections) — `server/realtime/connection_state_machine.py`
- **.state()** (3 connections) — `server/realtime/connection_state_machine.py`
- **Any** (2 connections) — `server/realtime/connection_state_machine.py`
- **State** (2 connections) — `server/realtime/connection_state_machine.py`
- **Called whenever state machine enters a new state.          Logs state transition** (1 connections) — `server/realtime/connection_state_machine.py`
- **Get connection statistics.          Returns:             Dictionary with connect** (1 connections) — `server/realtime/connection_state_machine.py`
- **Current FSM state as a single State.          Narrows base class type (Any | Mut** (1 connections) — `server/realtime/connection_state_machine.py`

## Relationships

- [[NATS Connection State Machine]] (3 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
