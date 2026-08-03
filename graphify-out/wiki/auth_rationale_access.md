# auth rationale access

> 165 nodes

## Key Concepts

- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **real_time.py** (35 connections) — `server/api/real_time.py`
- **create_access_token()** (32 connections) — `server/auth_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **hash_password()** (18 connections) — `server/auth_utils.py`
- **auth_utils.py** (17 connections) — `server/auth_utils.py`
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
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **__init__.py** (9 connections) — `server/schemas/realtime/__init__.py`
- **SessionInfo** (9 connections) — `server/schemas/realtime/realtime.py`
- **WebSocket** (8 connections)
- **_resolve_player_id_from_test()** (8 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (8 connections) — `server/api/real_time.py`
- **get_player_connections()** (8 connections) — `server/api/real_time.py`
- **handle_new_game_session()** (8 connections) — `server/api/real_time.py`
- *... and 140 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (20 shared connections)
- [NATS Messaging](NATS_Messaging.md) (10 shared connections)
- [auth users rationale](auth_users_rationale.md) (8 shared connections)
- [Exception Containers](Exception_Containers.md) (7 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (4 shared connections)
- [health models rationale](health_models_rationale.md) (3 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (3 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (3 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (3 shared connections)
- [room websocket updates](room_websocket_updates.md) (3 shared connections)
- [realtime game state](realtime_game_state.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/auth_utils.py`
- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 634 (92%)
- INFERRED: 57 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*