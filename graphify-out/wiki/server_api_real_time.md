# server api real time

> 90 nodes

## Key Concepts

- **real_time.py** (38 connections) — `server/api/real_time.py`
- **test_real_time_helpers.py** (32 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **asyncio** (16 connections)
- **realtime/realtime.py** (14 connections) — `server/schemas/realtime/realtime.py`
- **handle_new_game_session()** (12 connections) — `server/api/real_time.py`
- **_resolve_player_id()** (11 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (11 connections) — `server/api/real_time.py`
- **ConnectionStatisticsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **_ensure_connection_manager()** (10 connections) — `server/api/real_time.py`
- **get_player_connections()** (10 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (10 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (9 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_test()** (9 connections) — `server/api/real_time.py`
- **_validate_websocket_connection_manager()** (9 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (9 connections) — `server/api/real_time.py`
- **Any** (9 connections)
- **get_connection_statistics()** (8 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_path_or_token()** (8 connections) — `server/api/real_time.py`
- **WebSocket** (8 connections)
- **ErrorStatistics** (7 connections) — `server/schemas/realtime/presence_data.py`
- **PresenceStatistics** (7 connections) — `server/schemas/realtime/presence_data.py`
- **SessionStatistics** (7 connections) — `server/schemas/realtime/presence_data.py`
- **NewGameSessionResponse** (7 connections) — `server/schemas/realtime/realtime.py`
- **PlayerConnectionsResponse** (7 connections) — `server/schemas/realtime/realtime.py`
- **_resolve_connection_manager_from_state()** (7 connections) — `server/api/real_time.py`
- *... and 65 more nodes in this community*

## Relationships

- [server api players](server_api_players.md) (14 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [server schemas realtime init](server_schemas_realtime_init.md) (6 shared connections)
- [server auth utils](server_auth_utils.md) (4 shared connections)
- [server api admin npc instances](server_api_admin_npc_instances.md) (3 shared connections)
- [server async persistence](server_async_persistence.md) (3 shared connections)
- [server realtime websocket handler app](server_realtime_websocket_handler_app.md) (3 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (3 shared connections)
- [healthstatus](healthstatus.md) (2 shared connections)
- [server commands look helpers lookrequest](server_commands_look_helpers_lookrequest.md) (2 shared connections)
- [server commands rescue commands](server_commands_rescue_commands.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 235 (93%)
- INFERRED: 17 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*