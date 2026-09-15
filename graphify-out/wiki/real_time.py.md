# real_time.py

> 24 nodes

## Key Concepts

- **real_time.py** (51 connections) — `server/api/real_time.py`
- **_resolve_player_id()** (14 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (10 connections) — `server/api/real_time.py`
- **WebSocket** (10 connections)
- **_resolve_player_id_from_test()** (9 connections) — `server/api/real_time.py`
- **_validate_websocket_connection_manager()** (8 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (7 connections) — `server/api/real_time.py`
- **_app_state_from_websocket()** (6 connections) — `server/api/real_time.py`
- **_invoke_handle_websocket_connection()** (6 connections) — `server/api/real_time.py`
- **test_parse_websocket_token_header_parse_error()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **BoundLogger** (3 connections)
- **test_parse_websocket_token_from_query()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_from_subprotocol()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Real-time communication API endpoints for MythosMUD server. This module handles…** (1 connections) — `server/api/real_time.py`
- **Load the handler via importlib so basedpyright does not follow the factory…** (1 connections) — `server/api/real_time.py`
- **Read Starlette app.state from a WebSocket connection.** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol (preferred) or query params (fallback).…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from test player_id query parameter. Validates that the…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from token or test player_id parameter. Handles both…** (1 connections) — `server/api/real_time.py`
- **WebSocket endpoint for interactive commands and chat. Supports session tracking…** (1 connections) — `server/api/real_time.py`
- **Validate and resolve connection manager for WebSocket. Args: websocket:…** (1 connections) — `server/api/real_time.py`
- **Deprecated. Backward-compatible WebSocket endpoint that accepts a path…** (1 connections) — `server/api/real_time.py`

## Relationships

- [test_real_time_helpers.py](test_real_time_helpers.py.md) (21 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (12 shared connections)
- [_RealtimeConnectionManager](_RealtimeConnectionManager.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [_ensure_connection_manager](_ensure_connection_manager.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [_extract_bearer_token](_extract_bearer_token.md) (3 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (3 shared connections)
- [_PlayerLookupPersistence](_PlayerLookupPersistence.md) (3 shared connections)
- [resolve_connection_manager](resolve_connection_manager.md) (2 shared connections)
- [websocket_player_id_fallback_allowed](websocket_player_id_fallback_allowed.md) (2 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 116 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*