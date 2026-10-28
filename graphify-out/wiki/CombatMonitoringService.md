# CombatMonitoringService

> 62 nodes · cohesion 0.06

## Key Concepts

- **real_time.py** (51 connections) — `server/api/real_time.py`
- **_RealtimeConnectionManager** (16 connections) — `server/api/real_time.py`
- **UUID** (14 connections)
- **_resolve_player_id()** (14 connections) — `server/api/real_time.py`
- **handle_new_game_session()** (12 connections) — `server/api/real_time.py`
- **_ensure_connection_manager()** (11 connections) — `server/api/real_time.py`
- **get_player_connections()** (10 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (10 connections) — `server/api/real_time.py`
- **WebSocket** (10 connections)
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (10 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_test()** (9 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (9 connections) — `server/api/real_time.py`
- **get_connection_statistics()** (8 connections) — `server/api/real_time.py`
- **_validate_websocket_connection_manager()** (8 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (7 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (7 connections) — `server/api/real_time.py`
- **NewGameSessionResponse** (7 connections) — `server/schemas/realtime/realtime.py`
- **PlayerConnectionsResponse** (7 connections) — `server/schemas/realtime/realtime.py`
- **_app_state_from_websocket()** (6 connections) — `server/api/real_time.py`
- **_invoke_handle_websocket_connection()** (6 connections) — `server/api/real_time.py`
- **BaseModel** (6 connections)
- **SessionInfo** (6 connections) — `server/schemas/realtime/realtime.py`
- **_app_state_from_request()** (5 connections) — `server/api/real_time.py`
- **websocket_player_id_fallback_allowed()** (4 connections) — `server/api/real_time.py`
- *... and 37 more nodes in this community*

## Relationships

- [compare_linting_results.py](compare_linting_results.py.md) (40 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (7 shared connections)
- [Room](Room.md) (6 shared connections)
- [vite.userConfig.ts](vite.userConfig.ts.md) (5 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (5 shared connections)
- [NATSService](NATSService.md) (4 shared connections)
- [test_look_container.py](test_look_container.py.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [4. Rest/Quit Command During Combat](4._Rest-Quit_Command_During_Combat.md) (3 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/schemas/realtime/realtime.py`

## Audit Trail

- EXTRACTED: 198 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*