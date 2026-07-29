# Reconnect cancels an in progress

> 2 nodes

## Key Concepts

- **test_establish_websocket_connection_cancels_rest_countdown()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Reconnect cancels an in-progress rest countdown so it cannot poison the new sess** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [connection establishment](connection_establishment.md) (1 shared connections)
- [test connection establishment](test_connection_establishment.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*