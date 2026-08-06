# service combat services

> 6 nodes

## Key Concepts

- **.on_enter_state()** (4 connections) — `server/realtime/connection_state_machine.py`
- **.get_stats()** (3 connections) — `server/realtime/connection_state_machine.py`
- **State** (2 connections)
- **Any** (2 connections)
- **Called whenever state machine enters a new state.          Logs state transition** (1 connections) — `server/realtime/connection_state_machine.py`
- **Get connection statistics.          Returns:             Dictionary with connect** (1 connections) — `server/realtime/connection_state_machine.py`

## Relationships

- [connection state machine](connection_state_machine.md) (2 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*