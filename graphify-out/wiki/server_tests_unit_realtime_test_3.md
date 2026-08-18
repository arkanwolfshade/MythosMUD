# server tests unit realtime test

> 39 nodes

## Key Concepts

- **test_connection_establishment_ws.py** (24 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **_FakeWebSocket** (23 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_as_ws()** (21 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_meta()** (12 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **asyncio** (11 connections)
- **test_establish_websocket_connection_first_session_does_not_replace()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_missing_session_id_does_not_replace()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_new_session_disconnects_prior()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_same_session_appends()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **_player_with_room()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_cancels_rest_countdown()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_cleans_dead_connections()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_error()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_stale_session_does_not_replace()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_success()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_cleanup_failed_connection_success()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_player_not_found()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_find_dead_connections_all_active()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_FakeClientState** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **.__init__()** (2 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **UUID** (2 connections)
- **.__init__()** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **.accept()** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **.close()** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **ConnectionMetadata** (1 connections)
- *... and 14 more nodes in this community*

## Relationships

- [server realtime connection establishment cleanup](server_realtime_connection_establishment_cleanup.md) (46 shared connections)
- [server realtime connection establishment](server_realtime_connection_establishment.md) (14 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (3 shared connections)
- [server realtime connection models](server_realtime_connection_models.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment_ws.py`

## Audit Trail

- EXTRACTED: 148 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*