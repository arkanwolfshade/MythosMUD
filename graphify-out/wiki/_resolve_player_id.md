# _resolve_player_id

> 23 nodes

## Key Concepts

- **_resolve_player_id()** (11 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (10 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (9 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_test()** (9 connections) — `server/api/real_time.py`
- **_validate_websocket_connection_manager()** (9 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (9 connections) — `server/api/real_time.py`
- **Any** (9 connections)
- **_resolve_player_id_from_path_or_token()** (8 connections) — `server/api/real_time.py`
- **WebSocket** (8 connections)
- **_resolve_connection_manager_from_state()** (7 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (7 connections) — `server/api/real_time.py`
- **UUID** (7 connections)
- **test_parse_websocket_token_from_query()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_from_subprotocol()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_connection_manager_from_state()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Parse token from WebSocket subprotocol (preferred) or query params (fallback).…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from test player_id query parameter. Validates that the…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from JWT token payload. Validates that the user has a player…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from token or test player_id parameter. Handles both…** (1 connections) — `server/api/real_time.py`
- **Validate and resolve connection manager for WebSocket. Args: websocket:…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from path parameter or token. Args: player_id: Player ID from…** (1 connections) — `server/api/real_time.py`
- **Deprecated. Backward-compatible WebSocket endpoint that accepts a path…** (1 connections) — `server/api/real_time.py`
- **Validate connection manager and accept WebSocket connection. Returns True if…** (1 connections) — `server/api/real_time.py`

## Relationships

- [test_real_time_helpers.py](test_real_time_helpers.py.md) (18 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (2 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [_extract_bearer_token](_extract_bearer_token.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 80 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*