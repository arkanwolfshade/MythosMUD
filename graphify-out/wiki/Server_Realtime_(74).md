# Server Realtime (74)

> 20 nodes

## Key Concepts

- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **test_remove_dead_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection_not_present()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_update_player_connection_list_no_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_update_player_connection_list_with_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_update_player_connection_list_no_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_empty_list()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_with_dead()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Remove a single dead connection from tracking structures.      Args:         con** (1 connections) — `server/realtime/connection_establishment.py`
- **Update player's connection list to only include active connections.      Args:** (1 connections) — `server/realtime/connection_establishment.py`
- **Clean up dead connections under lock.      Args:         dead_connection_ids: Li** (1 connections) — `server/realtime/connection_establishment.py`
- **Test _remove_dead_connection() removes connection from tracking.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _remove_dead_connection() handles connection not present.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _update_player_connection_list() handles player not in player_websockets.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _update_player_connection_list() keeps active connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _update_player_connection_list() removes player when no active connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_dead_connections() handles empty list.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_dead_connections() cleans up dead connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [Server Realtime (63)](Server_Realtime_%2863%29.md) (10 shared connections)
- [Server Realtime (73)](Server_Realtime_%2873%29.md) (9 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*