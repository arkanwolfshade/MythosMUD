# _meta

> 14 nodes

## Key Concepts

- **_meta()** (11 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_first_session_does_not_replace()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_missing_session_id_does_not_replace()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_new_session_disconnects_prior()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_same_session_appends()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_cleans_dead_connections()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_player_with_room()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **UUID** (2 connections)
- **ConnectionMetadata** (1 connections)
- **Test establish_websocket_connection() cleans up dead connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **New session_id closes prior sockets before append-register (#610).** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Same session_id appends; does not kill a healthy prior socket (#610).** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **No player_sessions entry: first session_id appends; does not close leftover…** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Absent session_id is grace/recover: append only, do not run new_game_session…** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [test_connection_establishment.py](test_connection_establishment.py.md) (24 shared connections)
- [_FakeWebSocket](_FakeWebSocket.md) (14 shared connections)
- [establish_websocket_connection](establish_websocket_connection.md) (5 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 59 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*