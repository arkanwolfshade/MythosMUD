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

- [server api character creation apply](server_api_character_creation_apply.md) (14 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)
- [server schemas realtime init](server_schemas_realtime_init.md) (6 shared connections)
- [server auth utils](server_auth_utils.md) (4 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (4 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (4 shared connections)
- [server api players get player](server_api_players_get_player.md) (3 shared connections)
- [server realtime websocket handler app](server_realtime_websocket_handler_app.md) (3 shared connections)
- [server api monitoring](server_api_monitoring.md) (2 shared connections)
- [attributeerror](attributeerror.md) (1 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (1 shared connections)
- [scripts generate openapi spec](scripts_generate_openapi_spec.md) (1 shared connections)

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