# real_time.py

> 37 nodes · cohesion 0.11

## Key Concepts

- **real_time.py** (34 connections) — `server/api/real_time.py`
- **_resolve_player_id()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **_ensure_connection_manager()** (9 connections) — `server/api/real_time.py`
- **Any** (9 connections)
- **get_player_connections()** (8 connections) — `server/api/real_time.py`
- **handle_new_game_session()** (8 connections) — `server/api/real_time.py`
- **WebSocket** (8 connections)
- **_resolve_player_id_from_test()** (8 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (8 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (8 connections) — `server/api/real_time.py`
- **UUID** (7 connections)
- **_validate_websocket_connection_manager()** (7 connections) — `server/api/real_time.py`
- **get_connection_statistics()** (6 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (6 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (6 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_path_or_token()** (6 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (5 connections) — `server/api/real_time.py`
- **_parse_subprotocol_token()** (4 connections) — `server/api/real_time.py`
- **Request** (4 connections)
- **_extract_bearer_token()** (3 connections) — `server/api/real_time.py`
- **Real-time communication API endpoints for MythosMUD server.  This module handles** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol header.      Example formats: "bearer, <t** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol (preferred) or query params (fallback).** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from test player_id query parameter.     Validates that the pl** (1 connections) — `server/api/real_time.py`
- *... and 12 more nodes in this community*

## Relationships

- [realtime.py](realtime.py.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (4 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (3 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (3 shared connections)
- [exceptions.py](exceptions.py.md) (2 shared connections)
- [.state](state.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (1 shared connections)
- [factory.py](factory.py.md) (1 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`

## Audit Trail

- EXTRACTED: 187 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*