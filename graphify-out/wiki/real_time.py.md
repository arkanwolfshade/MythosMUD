# real_time.py

> 33 nodes

## Key Concepts

- **real_time.py** (39 connections) — `server/api/real_time.py`
- **_resolve_player_id()** (14 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (10 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (10 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_test()** (9 connections) — `server/api/real_time.py`
- **Any** (9 connections)
- **WebSocket** (9 connections)
- **_validate_websocket_connection_manager()** (8 connections) — `server/api/real_time.py`
- **UUID** (8 connections)
- **_resolve_connection_manager_from_state()** (7 connections) — `server/api/real_time.py`
- **_invoke_handle_websocket_connection()** (6 connections) — `server/api/real_time.py`
- **test_resolve_player_id_query_rejected_when_fallback_off()** (5 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **websocket_player_id_fallback_allowed()** (4 connections) — `server/api/real_time.py`
- **test_resolve_player_id_from_token_no_player()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_missing_token_and_player_id()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_query_allowed_when_fallback_on()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_token_with_character_id()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_websocket_connection_manager()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_websocket_player_id_fallback_allowed_default_off()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **MonkeyPatch** (3 connections)
- **test_resolve_connection_manager_from_state()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Real-time communication API endpoints for MythosMUD server. This module handles…** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol (preferred) or query params (fallback).…** (1 connections) — `server/api/real_time.py`
- *... and 8 more nodes in this community*

## Relationships

- [test_real_time_helpers.py](test_real_time_helpers.py.md) (32 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (8 shared connections)
- [_ensure_connection_manager](_ensure_connection_manager.md) (6 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [_extract_bearer_token](_extract_bearer_token.md) (3 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (3 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (3 shared connections)
- [.state](state.md) (2 shared connections)
- [_ConnectionManagerUtilsModule](_ConnectionManagerUtilsModule.md) (2 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 128 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*