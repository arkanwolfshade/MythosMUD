# server realtime connection establishment establish

> 31 nodes

## Key Concepts

- **establish_websocket_connection()** (25 connections) — `server/realtime/connection_establishment.py`
- **_FakeWebSocket** (23 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_connection_establishment_ws.py** (23 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **_as_ws()** (21 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **asyncio** (11 connections)
- **test_establish_websocket_connection_first_session_does_not_replace()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_missing_session_id_does_not_replace()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_new_session_disconnects_prior()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_same_session_appends()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **_player_with_room()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_cancels_rest_countdown()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_cleans_dead_connections()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_stale_session_does_not_replace()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_success()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_error()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_player_not_found()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **.accept()** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **.close()** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **WebSocket** (1 connections)
- **Establish a new WebSocket connection. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/connection_establishment.py`
- **Unit tests for establish_websocket_connection. Split from…** (1 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **Reconnect cancels an in-progress rest countdown so it cannot poison the new…** (1 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **New session_id closes prior sockets before append-register (#610).** (1 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **A leaked session with no live sockets must not trigger the replacement path.…** (1 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **Same session_id appends; does not kill a healthy prior socket (#610).** (1 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- *... and 6 more nodes in this community*

## Relationships

- [connectionmetadata](connectionmetadata.md) (41 shared connections)
- [server realtime connection establishment](server_realtime_connection_establishment.md) (10 shared connections)
- [server realtime connection establishment find](server_realtime_connection_establishment_find.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (1 shared connections)
- [server realtime connection manager connectionmanager](server_realtime_connection_manager_connectionmanager.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment_ws.py`

## Audit Trail

- EXTRACTED: 140 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*