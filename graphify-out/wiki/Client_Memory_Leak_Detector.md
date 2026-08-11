# Client Memory Leak Detector

> 63 nodes

## Key Concepts

- **real_time.py** (34 connections) — `server/api/real_time.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **_resolve_player_id()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **Any** (9 connections)
- **_ensure_connection_manager()** (9 connections) — `server/api/real_time.py`
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
- **.item_instance_exists()** (3 connections) — `server/async_persistence.py`
- **test_handle_websocket_connection_shutdown_rejected()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- *... and 38 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [Command Testing Guide](Command_Testing_Guide.md) (8 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (7 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (7 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (6 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (4 shared connections)
- [Lucidity Recovery Commands](Lucidity_Recovery_Commands.md) (4 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (3 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/async_persistence.py`
- `server/realtime/websocket_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`

## Audit Trail

- EXTRACTED: 274 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*