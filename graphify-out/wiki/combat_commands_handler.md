# combat commands handler

> 93 nodes

## Key Concepts

- **real_time.py** (36 connections) — `server/api/real_time.py`
- **test_real_time_helpers.py** (31 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **realtime.py** (13 connections) — `server/schemas/realtime/realtime.py`
- **PresenceStatistics** (12 connections) — `server/schemas/realtime/presence_data.py`
- **SessionStatistics** (12 connections) — `server/schemas/realtime/presence_data.py`
- **ErrorStatistics** (12 connections) — `server/schemas/realtime/presence_data.py`
- **_resolve_player_id()** (11 connections) — `server/api/real_time.py`
- **handle_new_game_session()** (11 connections) — `server/api/real_time.py`
- **_ensure_connection_manager()** (10 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **PlayerConnectionsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **NewGameSessionResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **ConnectionStatisticsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **Any** (9 connections)
- **_parse_websocket_token()** (9 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_test()** (9 connections) — `server/api/real_time.py`
- **get_player_connections()** (9 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (9 connections) — `server/api/real_time.py`
- **__init__.py** (9 connections) — `server/schemas/realtime/__init__.py`
- **SessionInfo** (9 connections) — `server/schemas/realtime/realtime.py`
- **WebSocket** (8 connections)
- **_validate_websocket_connection_manager()** (8 connections) — `server/api/real_time.py`
- *... and 68 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (14 shared connections)
- [command commands handler](command_commands_handler.md) (7 shared connections)
- [NPC Combat](NPC_Combat.md) (6 shared connections)
- [command commands aliases](command_commands_aliases.md) (6 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (4 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (4 shared connections)
- [schemas invite user](schemas_invite_user.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (4 shared connections)
- [room websocket updates](room_websocket_updates.md) (3 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [health models rationale](health_models_rationale.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/async_persistence.py`
- `server/realtime/websocket_handler.py`
- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 438 (91%)
- INFERRED: 45 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*