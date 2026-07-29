# real time

> 65 nodes

## Key Concepts

- **real_time.py** (35 connections) — `server/api/real_time.py`
- **get_async_persistence()** (16 connections) — `server/async_persistence.py`
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
- *... and 40 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (10 shared connections)
- [APIRouter](APIRouter.md) (7 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (5 shared connections)
- [Request](Request.md) (4 shared connections)
- [create access token()](create_access_token%28%29.md) (3 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (3 shared connections)
- [memory leak metrics](memory_leak_metrics.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [.state()](state%28%29.md) (2 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (2 shared connections)
- [BaseModel](BaseModel.md) (2 shared connections)
- [init](init.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/async_persistence.py`
- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`

## Audit Trail

- EXTRACTED: 299 (89%)
- INFERRED: 38 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*