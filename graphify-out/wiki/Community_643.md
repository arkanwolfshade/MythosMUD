# Community 643

> 26 nodes

## Key Concepts

- **_resolve_player_id()** (13 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (10 connections) — `server/api/real_time.py`
- **WebSocket** (10 connections)
- **_resolve_player_id_from_test()** (8 connections) — `server/api/real_time.py`
- **_validate_websocket_connection_manager()** (8 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (7 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (7 connections) — `server/api/real_time.py`
- **_invoke_handle_websocket_connection()** (6 connections) — `server/api/real_time.py`
- **_app_state_from_websocket()** (5 connections) — `server/api/real_time.py`
- **websocket_player_id_fallback_allowed()** (4 connections) — `server/api/real_time.py`
- **BoundLogger** (3 connections)
- **test_parse_websocket_token_from_query()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_from_subprotocol()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_connection_manager_from_state()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Load the handler via importlib so basedpyright does not follow the factory…** (1 connections) — `server/api/real_time.py`
- **Read Starlette app.state from a WebSocket connection.** (1 connections) — `server/api/real_time.py`
- **Validate connection manager and accept WebSocket connection. Returns True if…** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol (preferred) or query params (fallback).…** (1 connections) — `server/api/real_time.py`
- **Return True only when anonymous player_id query fallback is explicitly enabled.…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from test player_id query parameter. Validates that the…** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from token or test player_id parameter. Handles both…** (1 connections) — `server/api/real_time.py`
- **WebSocket endpoint for interactive commands and chat. Supports session tracking…** (1 connections) — `server/api/real_time.py`
- **Validate and resolve connection manager for WebSocket. Args: websocket:…** (1 connections) — `server/api/real_time.py`
- *... and 1 more nodes in this community*

## Relationships

- [Community 586](Community_586.md) (14 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (13 shared connections)
- [Community 1020](Community_1020.md) (8 shared connections)
- [Container API Models](Container_API_Models.md) (4 shared connections)
- [Community 1389](Community_1389.md) (1 shared connections)
- [Community 1583](Community_1583.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*