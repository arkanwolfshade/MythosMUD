# test_real_time_helpers.py

> 57 nodes

## Key Concepts

- **test_real_time_helpers.py** (32 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **asyncio** (16 connections)
- **realtime/realtime.py** (14 connections) — `server/schemas/realtime/realtime.py`
- **handle_new_game_session()** (12 connections) — `server/api/real_time.py`
- **schemas/realtime/__init__.py** (12 connections) — `server/schemas/realtime/__init__.py`
- **ConnectionStatisticsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **_ensure_connection_manager()** (10 connections) — `server/api/real_time.py`
- **get_player_connections()** (10 connections) — `server/api/real_time.py`
- **get_connection_statistics()** (8 connections) — `server/api/real_time.py`
- **ErrorStatistics** (7 connections) — `server/schemas/realtime/presence_data.py`
- **PresenceStatistics** (7 connections) — `server/schemas/realtime/presence_data.py`
- **SessionStatistics** (7 connections) — `server/schemas/realtime/presence_data.py`
- **NewGameSessionResponse** (7 connections) — `server/schemas/realtime/realtime.py`
- **PlayerConnectionsResponse** (7 connections) — `server/schemas/realtime/realtime.py`
- **SessionInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **test_get_connection_statistics()** (6 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **presence_data.py** (6 connections) — `server/schemas/realtime/presence_data.py`
- **BaseModel** (6 connections)
- **test_handle_new_game_session_invalid_json()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_missing_session_id()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_header_parse_error()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_token_no_player()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_missing_token_and_player_id()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_websocket_endpoint_route_unresolved_player()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Request** (4 connections)
- *... and 32 more nodes in this community*

## Relationships

- [_resolve_player_id](_resolve_player_id.md) (18 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (4 shared connections)
- [_extract_bearer_token](_extract_bearer_token.md) (4 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 151 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*