# test_real_time_helpers.py

> 28 nodes

## Key Concepts

- **test_real_time_helpers.py** (38 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **asyncio** (20 connections)
- **handle_new_game_session()** (12 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_path_or_token()** (10 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (7 connections) — `server/api/real_time.py`
- **resolve_connection_manager()** (5 connections) — `server/api/real_time.py`
- **test_handle_new_game_session_invalid_json()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_missing_session_id()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_header_parse_error()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_websocket_endpoint_route_unresolved_player()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_uuid_jwt_match()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_uuid_jwt_mismatch_rejected()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_uuid_without_jwt_rejected()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_via_token()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_test()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_and_accept_websocket_unavailable()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_and_accept_websocket_valid()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_from_query()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_from_subprotocol()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_connection_manager_delegates_when_none()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_connection_manager_returns_candidate()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **post** (1 connections)
- **Validate connection manager and accept WebSocket connection. Returns True if…** (1 connections) — `server/api/real_time.py`
- **Handle a new game session for a player. This will disconnect existing…** (1 connections) — `server/api/real_time.py`
- *... and 3 more nodes in this community*

## Relationships

- [real_time.py](real_time.py.md) (32 shared connections)
- [_ensure_connection_manager](_ensure_connection_manager.md) (7 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (4 shared connections)
- [_extract_bearer_token](_extract_bearer_token.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 97 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*