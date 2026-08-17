# asyncio

> 38 nodes

## Key Concepts

- **asyncio** (16 connections)
- **handle_new_game_session()** (12 connections) — `server/api/real_time.py`
- **_resolve_player_id()** (11 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (11 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (10 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_test()** (9 connections) — `server/api/real_time.py`
- **_validate_websocket_connection_manager()** (9 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (9 connections) — `server/api/real_time.py`
- **Any** (9 connections)
- **_resolve_player_id_from_path_or_token()** (8 connections) — `server/api/real_time.py`
- **WebSocket** (8 connections)
- **_resolve_connection_manager_from_state()** (7 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (7 connections) — `server/api/real_time.py`
- **UUID** (7 connections)
- **test_handle_new_game_session_invalid_json()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_missing_session_id()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_token_no_player()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_missing_token_and_player_id()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_websocket_endpoint_route_unresolved_player()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_uuid()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_via_token()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_test()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_token_with_character_id()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_and_accept_websocket_unavailable()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- *... and 13 more nodes in this community*

## Relationships

- [test_real_time_helpers.py](test_real_time_helpers.py.md) (18 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (10 shared connections)
- [_ensure_connection_manager](_ensure_connection_manager.md) (6 shared connections)
- [.state](state.md) (4 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (2 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (2 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (2 shared connections)
- [test_websocket_handler_app_state_connection.py](test_websocket_handler_app_state_connection.py.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 116 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*