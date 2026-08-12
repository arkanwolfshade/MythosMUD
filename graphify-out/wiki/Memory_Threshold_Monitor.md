# Memory Threshold Monitor

> 28 nodes

## Key Concepts

- **real_time.py** (34 connections) — `server/api/real_time.py`
- **_resolve_player_id()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **Any** (9 connections)
- **WebSocket** (8 connections)
- **_resolve_player_id_from_test()** (8 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (8 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (8 connections) — `server/api/real_time.py`
- **UUID** (7 connections)
- **_validate_websocket_connection_manager()** (7 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (6 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (6 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_path_or_token()** (6 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (5 connections) — `server/api/real_time.py`
- **_parse_subprotocol_token()** (4 connections) — `server/api/real_time.py`
- **_extract_bearer_token()** (3 connections) — `server/api/real_time.py`
- **Real-time communication API endpoints for MythosMUD server.  This module handles** (1 connections) — `server/api/real_time.py`
- **Validate connection manager and accept WebSocket connection.     Returns True if** (1 connections) — `server/api/real_time.py`
- **Extract bearer token from parsed subprotocol parts.      If 'bearer' marker is p** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol header.      Example formats: "bearer, <t** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol (preferred) or query params (fallback).** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from test player_id query parameter.     Validates that the pl** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from JWT token payload.     Validates that the user has a play** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from token or test player_id parameter.     Handles both authe** (1 connections) — `server/api/real_time.py`
- **WebSocket endpoint for interactive commands and chat.     Supports session track** (1 connections) — `server/api/real_time.py`
- *... and 3 more nodes in this community*

## Relationships

- [Schedule Service Loader](Schedule_Service_Loader.md) (12 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (5 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (3 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (3 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Command Testing Guide](Command_Testing_Guide.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (1 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`

## Audit Trail

- EXTRACTED: 148 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*