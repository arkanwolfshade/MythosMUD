# real_time.py

> 26 nodes

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
- **_validate_and_accept_websocket()** (7 connections) — `server/api/real_time.py`
- **_invoke_handle_websocket_connection()** (6 connections) — `server/api/real_time.py`
- **websocket_player_id_fallback_allowed()** (4 connections) — `server/api/real_time.py`
- **Real-time communication API endpoints for MythosMUD server. This module handles…** (1 connections) — `server/api/real_time.py`
- **Validate connection manager and accept WebSocket connection. Returns True if…** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol (preferred) or query params (fallback).…** (1 connections) — `server/api/real_time.py`
- **Return True only when anonymous player_id query fallback is explicitly enabled.…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from test player_id query parameter. Validates that the…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from JWT token payload. Validates that the user has a player…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from token or test player_id parameter. Handles both…** (1 connections) — `server/api/real_time.py`
- **WebSocket endpoint for interactive commands and chat. Supports session tracking…** (1 connections) — `server/api/real_time.py`
- **Validate and resolve connection manager for WebSocket. Args: websocket:…** (1 connections) — `server/api/real_time.py`
- **Deprecated. Backward-compatible WebSocket endpoint that accepts a path…** (1 connections) — `server/api/real_time.py`
- *... and 1 more nodes in this community*

## Relationships

- [test_real_time_helpers.py](test_real_time_helpers.py.md) (20 shared connections)
- [handle_new_game_session](handle_new_game_session.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (5 shared connections)
- [_extract_bearer_token](_extract_bearer_token.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [resolve_connection_manager](resolve_connection_manager.md) (2 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (2 shared connections)
- [.state](state.md) (2 shared connections)
- [_ConnectionManagerUtilsModule](_ConnectionManagerUtilsModule.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`

## Audit Trail

- EXTRACTED: 114 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*