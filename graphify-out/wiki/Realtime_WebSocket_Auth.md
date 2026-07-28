# Realtime WebSocket Auth

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

- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (8 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (7 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (7 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (4 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (3 shared connections)
- [Database Manager Tests](Database_Manager_Tests.md) (3 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (2 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (1 shared connections)
- [Community 2199](Community_2199.md) (1 shared connections)
- [NPC Combat Handler Tests](NPC_Combat_Handler_Tests.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`

## Audit Trail

- EXTRACTED: 187 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*