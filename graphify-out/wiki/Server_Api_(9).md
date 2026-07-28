# Server Api (9)

> 63 nodes

## Key Concepts

- **real_time.py** (34 connections) — `server/api/real_time.py`
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
- **__init__.py** (9 connections) — `server/schemas/realtime/__init__.py`
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
- *... and 38 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (8 shared connections)
- [Server Api](Server_Api.md) (7 shared connections)
- [Server Admin](Server_Admin.md) (6 shared connections)
- [Server Auth (3)](Server_Auth_%283%29.md) (4 shared connections)
- [Server Realtime (6)](Server_Realtime_%286%29.md) (3 shared connections)
- [Server Realtime (36)](Server_Realtime_%2836%29.md) (3 shared connections)
- [Server Realtime (44)](Server_Realtime_%2844%29.md) (2 shared connections)
- [Server Schemas (5)](Server_Schemas_%285%29.md) (2 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (1 shared connections)
- [Server Realtime (13)](Server_Realtime_%2813%29.md) (1 shared connections)
- [Server Middleware](Server_Middleware.md) (1 shared connections)
- [Server Realtime (48)](Server_Realtime_%2848%29.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`

## Audit Trail

- EXTRACTED: 280 (88%)
- INFERRED: 39 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*