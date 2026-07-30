# Domain Model Anemic Anti Pattern

> 2 nodes

## Key Concepts

- **test_connect_transition()** (3 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`
- **Test connect() transition from disconnected to connecting.** (1 connections) — `server/tests/unit/realtime/test_connection_state_machine.py`

## Relationships

- [connection state machine](connection_state_machine.md) (1 shared connections)
- [enhance player ids()](enhance_player_ids%28%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_state_machine.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*