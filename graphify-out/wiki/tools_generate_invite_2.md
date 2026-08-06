# tools generate invite

> 12 nodes

## Key Concepts

- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **test_remove_dead_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection_not_present()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_empty_list()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_with_dead()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Remove a single dead connection from tracking structures.      Args:         con** (1 connections) — `server/realtime/connection_establishment.py`
- **Clean up dead connections under lock.      Args:         dead_connection_ids: Li** (1 connections) — `server/realtime/connection_establishment.py`
- **Test _remove_dead_connection() removes connection from tracking.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _remove_dead_connection() handles connection not present.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_dead_connections() handles empty list.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_dead_connections() cleans up dead connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [invite models rationale](invite_models_rationale.md) (6 shared connections)
- [connection establishment realtime](connection_establishment_realtime.md) (6 shared connections)
- [channel broadcasting realtime](channel_broadcasting_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*