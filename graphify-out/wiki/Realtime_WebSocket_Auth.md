# Realtime WebSocket Auth

> 44 nodes · cohesion 0.09

## Key Concepts

- **real_time.py** (33 connections) — `server/api/real_time.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **_resolve_player_id()** (10 connections) — `server/api/real_time.py`
- **_ensure_connection_manager()** (9 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (9 connections) — `server/api/real_time.py`
- **Any** (9 connections) — `server/api/real_time.py`
- **get_player_connections()** (8 connections) — `server/api/real_time.py`
- **handle_new_game_session()** (8 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_test()** (8 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (8 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (8 connections) — `server/api/real_time.py`
- **WebSocket** (8 connections) — `server/api/real_time.py`
- **UUID** (7 connections) — `server/api/real_time.py`
- **get_connection_statistics()** (6 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (6 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (6 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_path_or_token()** (6 connections) — `server/api/real_time.py`
- **_validate_websocket_connection_manager()** (6 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (5 connections) — `server/api/real_time.py`
- **_parse_subprotocol_token()** (4 connections) — `server/api/real_time.py`
- **Request** (4 connections) — `server/api/real_time.py`
- **_extract_bearer_token()** (3 connections) — `server/api/real_time.py`
- **Real-time communication API endpoints for MythosMUD server.  This module handles** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol header.      Example formats: "bearer, <t** (1 connections) — `server/api/real_time.py`
- *... and 19 more nodes in this community*

## Relationships

- [[NPC Admin API]] (10 shared connections)
- [[Container Exception Handlers]] (7 shared connections)
- [[WebSocket Handler Tests]] (6 shared connections)
- [[WebSocket Coverage Gaps]] (6 shared connections)
- [[Realtime Schemas Presence]] (5 shared connections)
- [[Async Persistence Delegates]] (4 shared connections)
- [[Auth Token Utilities]] (3 shared connections)
- [[WebSocket Player Helpers]] (3 shared connections)
- [[WebSocket Initial State]] (3 shared connections)
- [[WebSocket Message Validation]] (2 shared connections)
- [[WebSocket Message Validator]] (2 shared connections)
- [[Room Occupant Events]] (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/async_persistence.py`
- `server/realtime/websocket_handler.py`

## Audit Trail

- EXTRACTED: 231 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
