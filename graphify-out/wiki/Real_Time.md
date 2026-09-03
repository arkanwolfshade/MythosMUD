# Real Time

> 109 nodes

## Key Concepts

- **real_time.py** (40 connections) — `server/api/real_time.py`
- **test_real_time_helpers.py** (37 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **asyncio** (20 connections)
- **_RealtimeConnectionManager** (16 connections) — `server/api/real_time.py`
- **UUID** (14 connections)
- **_resolve_player_id()** (13 connections) — `server/api/real_time.py`
- **_ensure_connection_manager()** (11 connections) — `server/api/real_time.py`
- **handle_new_game_session()** (11 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (10 connections) — `server/api/real_time.py`
- **WebSocket** (10 connections)
- **_resolve_player_id_from_path_or_token()** (9 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_test()** (9 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (9 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (9 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (9 connections) — `server/api/real_time.py`
- **get_player_connections()** (8 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (8 connections) — `server/api/real_time.py`
- **_validate_websocket_connection_manager()** (8 connections) — `server/api/real_time.py`
- **get_connection_statistics()** (7 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (7 connections) — `server/api/real_time.py`
- **_PlayerLookupPersistence** (6 connections) — `server/api/real_time.py`
- **_app_state_from_websocket()** (6 connections) — `server/api/real_time.py`
- **_invoke_handle_websocket_connection()** (6 connections) — `server/api/real_time.py`
- **_extract_bearer_token()** (5 connections) — `server/api/real_time.py`
- **_parse_subprotocol_token()** (5 connections) — `server/api/real_time.py`
- *... and 84 more nodes in this community*

## Relationships

- [Players](Players.md) (6 shared connections)
- [Test Websocket Initial State](Test_Websocket_Initial_State.md) (3 shared connections)
- [Realtime](Realtime.md) (3 shared connections)
- [Character Creation API](Character_Creation_API.md) (2 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (2 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (2 shared connections)
- [Player Event Handlers Respawn Room](Player_Event_Handlers_Respawn_Room.md) (1 shared connections)
- [Test Logout Commands](Test_Logout_Commands.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Correlation Middleware](Correlation_Middleware.md) (1 shared connections)
- [Test Auth Utils](Test_Auth_Utils.md) (1 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 239 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*