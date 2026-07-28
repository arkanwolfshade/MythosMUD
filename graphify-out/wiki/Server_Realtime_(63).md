# Server Realtime (63)

> 28 nodes

## Key Concepts

- **test_connection_establishment.py** (46 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_error()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_no_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_all_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_in_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_connection_metadata()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_connection_metadata_no_session_token()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_session_tracking_no_session_id()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_error()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Unit tests for connection establishment.  Tests the connection_establishment mod** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _find_dead_connections() returns empty list when player not found.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _find_dead_connections() returns empty list when all connections are active** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _find_dead_connections() skips connections not in active_websockets.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _find_dead_connections() raises ConnectionError when websocket is None.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_connection_metadata() creates metadata.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_connection_metadata() handles None session and token.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_session_tracking() handles None session_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() returns False when player not found.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() handles no persistence.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() handles player with no room_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 3 more nodes in this community*

## Relationships

- [Server Realtime (73)](Server_Realtime_%2873%29.md) (22 shared connections)
- [Server Realtime (74)](Server_Realtime_%2874%29.md) (10 shared connections)
- [Server Persistence](Server_Persistence.md) (2 shared connections)
- [Server Realtime (149)](Server_Realtime_%28149%29.md) (1 shared connections)
- [Server Realtime (150)](Server_Realtime_%28150%29.md) (1 shared connections)
- [Server Realtime (152)](Server_Realtime_%28152%29.md) (1 shared connections)
- [Server Realtime (151)](Server_Realtime_%28151%29.md) (1 shared connections)
- [Server Realtime (153)](Server_Realtime_%28153%29.md) (1 shared connections)
- [Server Realtime (142)](Server_Realtime_%28142%29.md) (1 shared connections)
- [Server Realtime (143)](Server_Realtime_%28143%29.md) (1 shared connections)
- [Server Realtime (146)](Server_Realtime_%28146%29.md) (1 shared connections)
- [Server Realtime (145)](Server_Realtime_%28145%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 100 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*