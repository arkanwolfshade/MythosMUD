# compare_linting_results.py

> 50 nodes · cohesion 0.07

## Key Concepts

- **test_real_time_helpers.py** (40 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **asyncio** (20 connections)
- **realtime/realtime.py** (14 connections) — `server/schemas/realtime/realtime.py`
- **_resolve_player_id_from_path_or_token()** (10 connections) — `server/api/real_time.py`
- **ConnectionStatisticsResponse** (10 connections) — `server/schemas/realtime/realtime.py`
- **ErrorStatistics** (8 connections) — `server/schemas/realtime/presence_data.py`
- **PresenceStatistics** (8 connections) — `server/schemas/realtime/presence_data.py`
- **SessionStatistics** (8 connections) — `server/schemas/realtime/presence_data.py`
- **presence_data.py** (7 connections) — `server/schemas/realtime/presence_data.py`
- **test_get_connection_statistics()** (6 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **resolve_connection_manager()** (5 connections) — `server/api/real_time.py`
- **test_resolve_player_id_query_rejected_when_fallback_off()** (5 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_ensure_connection_manager_missing()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_invalid_json()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_missing_session_id()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_header_parse_error()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_token_no_player()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_missing_token_and_player_id()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_query_allowed_when_fallback_on()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_websocket_connection_manager()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_websocket_endpoint_route_unresolved_player()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **BaseModel** (3 connections)
- **MonkeyPatch** (3 connections)
- **test_get_player_connections()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- *... and 25 more nodes in this community*

## Relationships

- [CombatMonitoringService](CombatMonitoringService.md) (40 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (8 shared connections)
- [4. Rest/Quit Command During Combat](4._Rest-Quit_Command_During_Combat.md) (3 shared connections)
- [NATSService](NATSService.md) (2 shared connections)
- [test_look_container.py](test_look_container.py.md) (1 shared connections)
- [vite.userConfig.ts](vite.userConfig.ts.md) (1 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [security.ts](security.ts.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/schemas/realtime/presence_data.py`
- `server/schemas/realtime/realtime.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 135 (91%)
- INFERRED: 14 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*