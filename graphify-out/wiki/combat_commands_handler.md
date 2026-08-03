# combat commands handler

> 75 nodes

## Key Concepts

- **real_time.py** (35 connections) — `server/api/real_time.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **realtime.py** (13 connections) — `server/schemas/realtime/realtime.py`
- **_resolve_player_id()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **PresenceStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **SessionStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **ErrorStatistics** (10 connections) — `server/schemas/realtime/presence_data.py`
- **PlayerConnectionsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **NewGameSessionResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **ConnectionStatisticsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
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
- *... and 50 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (8 shared connections)
- [Exception Containers](Exception_Containers.md) (7 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (7 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (6 shared connections)
- [schemas nats messages](schemas_nats_messages.md) (5 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (4 shared connections)
- [schemas invite user](schemas_invite_user.md) (4 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [auth rationale access](auth_rationale_access.md) (3 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [admin auth service](admin_auth_service.md) (3 shared connections)
- [command combat models](command_combat_models.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/async_persistence.py`
- `server/realtime/websocket_handler.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`

## Audit Trail

- EXTRACTED: 334 (90%)
- INFERRED: 38 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*