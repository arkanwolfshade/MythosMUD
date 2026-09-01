# real_time.py

> 27 nodes

## Key Concepts

- **real_time.py** (52 connections) — `server/api/real_time.py`
- **_resolve_player_id()** (14 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (10 connections) — `server/api/real_time.py`
- **WebSocket** (10 connections)
- **_resolve_player_id_from_test()** (9 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (9 connections) — `server/api/real_time.py`
- **_validate_websocket_connection_manager()** (8 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (7 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (7 connections) — `server/api/real_time.py`
- **_app_state_from_websocket()** (6 connections) — `server/api/real_time.py`
- **_invoke_handle_websocket_connection()** (6 connections) — `server/api/real_time.py`
- **websocket_player_id_fallback_allowed()** (4 connections) — `server/api/real_time.py`
- **BoundLogger** (3 connections)
- **Real-time communication API endpoints for MythosMUD server. This module handles…** (1 connections) — `server/api/real_time.py`
- **Load the handler via importlib so basedpyright does not follow the factory…** (1 connections) — `server/api/real_time.py`
- **Read Starlette app.state from a WebSocket connection.** (1 connections) — `server/api/real_time.py`
- **Validate connection manager and accept WebSocket connection. Returns True if…** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol (preferred) or query params (fallback).…** (1 connections) — `server/api/real_time.py`
- **Return True only when anonymous player_id query fallback is explicitly enabled.…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from test player_id query parameter. Validates that the…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from JWT token payload. Validates that the user has a player…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from token or test player_id parameter. Handles both…** (1 connections) — `server/api/real_time.py`
- **WebSocket endpoint for interactive commands and chat. Supports session tracking…** (1 connections) — `server/api/real_time.py`
- *... and 2 more nodes in this community*

## Relationships

- [test_real_time_helpers.py](test_real_time_helpers.py.md) (20 shared connections)
- [_RealtimeConnectionManager](_RealtimeConnectionManager.md) (12 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (11 shared connections)
- [handle_new_game_session](handle_new_game_session.md) (6 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [_extract_bearer_token](_extract_bearer_token.md) (3 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (3 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (2 shared connections)
- [factory.py](factory.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [.state](state.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`

## Audit Trail

- EXTRACTED: 125 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*