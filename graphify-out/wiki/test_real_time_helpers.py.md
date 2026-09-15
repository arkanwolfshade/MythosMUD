# test_real_time_helpers.py

> 32 nodes

## Key Concepts

- **test_real_time_helpers.py** (40 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **asyncio** (20 connections)
- **handle_new_game_session()** (12 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_path_or_token()** (10 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (9 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (7 connections) — `server/api/real_time.py`
- **test_resolve_player_id_query_rejected_when_fallback_off()** (5 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_invalid_json()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_missing_session_id()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_token_no_player()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_missing_token_and_player_id()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_query_allowed_when_fallback_on()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_websocket_connection_manager()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_websocket_endpoint_route_unresolved_player()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_uuid_jwt_match()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_uuid_jwt_mismatch_rejected()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_uuid_without_jwt_rejected()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_via_token()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_test()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_token_with_character_id()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_and_accept_websocket_unavailable()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_and_accept_websocket_valid()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **MonkeyPatch** (3 connections)
- **test_resolve_connection_manager_from_state()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- *... and 7 more nodes in this community*

## Relationships

- [real_time.py](real_time.py.md) (21 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (7 shared connections)
- [_ensure_connection_manager](_ensure_connection_manager.md) (6 shared connections)
- [_RealtimeConnectionManager](_RealtimeConnectionManager.md) (4 shared connections)
- [_extract_bearer_token](_extract_bearer_token.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [websocket_player_id_fallback_allowed](websocket_player_id_fallback_allowed.md) (2 shared connections)
- [resolve_connection_manager](resolve_connection_manager.md) (2 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (1 shared connections)
- [_PlayerLookupPersistence](_PlayerLookupPersistence.md) (1 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 109 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*