# Client Memory Leak Detector

> 41 nodes

## Key Concepts

- **real_time.py** (34 connections) — `server/api/real_time.py`
- **_resolve_player_id()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **PlayerConnectionsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **Any** (9 connections)
- **_ensure_connection_manager()** (9 connections) — `server/api/real_time.py`
- **SessionInfo** (9 connections) — `server/schemas/realtime/realtime.py`
- **WebSocket** (8 connections)
- **_resolve_player_id_from_test()** (8 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (8 connections) — `server/api/real_time.py`
- **get_player_connections()** (8 connections) — `server/api/real_time.py`
- **handle_new_game_session()** (8 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (8 connections) — `server/api/real_time.py`
- **UUID** (7 connections)
- **_validate_websocket_connection_manager()** (7 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (6 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (6 connections) — `server/api/real_time.py`
- **get_connection_statistics()** (6 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_path_or_token()** (6 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (5 connections) — `server/api/real_time.py`
- **Request** (4 connections)
- **_parse_subprotocol_token()** (4 connections) — `server/api/real_time.py`
- **_extract_bearer_token()** (3 connections) — `server/api/real_time.py`
- **Real-time communication API endpoints for MythosMUD server.  This module handles** (1 connections) — `server/api/real_time.py`
- **Ensure connection manager is available.     Raises LoggedHTTPException with prop** (1 connections) — `server/api/real_time.py`
- *... and 16 more nodes in this community*

## Relationships

- [Command Testing Guide](Command_Testing_Guide.md) (14 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (10 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (7 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (3 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (3 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (3 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [NATS Message Schemas](NATS_Message_Schemas.md) (2 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)
- [Combat Command Helpers](Combat_Command_Helpers.md) (1 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/schemas/realtime/realtime.py`

## Audit Trail

- EXTRACTED: 202 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*