# nats services metrics

> 91 nodes

## Key Concepts

- **real_time.py** (36 connections) — `server/api/real_time.py`
- **test_real_time_helpers.py** (31 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
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
- **SessionInfo** (9 connections) — `server/schemas/realtime/realtime.py`
- **WebSocket** (8 connections)
- **_validate_websocket_connection_manager()** (8 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_path_or_token()** (8 connections) — `server/api/real_time.py`
- *... and 66 more nodes in this community*

## Relationships

- [health service services](health_service_services.md) (18 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (14 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (8 shared connections)
- [command commands aliases](command_commands_aliases.md) (6 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (6 shared connections)
- [schemas nats messages](schemas_nats_messages.md) (5 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (3 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (3 shared connections)
- [package argon2 engines](package_argon2_engines.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/auth_utils.py`
- `server/realtime/websocket_handler.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 434 (91%)
- INFERRED: 45 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*