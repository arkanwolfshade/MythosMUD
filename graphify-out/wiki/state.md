# .state

> 43 nodes

## Key Concepts

- **.state()** (36 connections) — `server/realtime/connection_state_machine.py`
- **real_time.py** (34 connections) — `server/api/real_time.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **_resolve_player_id()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **_ensure_connection_manager()** (9 connections) — `server/api/real_time.py`
- **get_player_connections()** (9 connections) — `server/api/real_time.py`
- **handle_new_game_session()** (9 connections) — `server/api/real_time.py`
- **Any** (9 connections)
- **_resolve_player_id_from_test()** (8 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (8 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (8 connections) — `server/api/real_time.py`
- **WebSocket** (8 connections)
- **get_connection_statistics()** (7 connections) — `server/api/real_time.py`
- **_validate_websocket_connection_manager()** (7 connections) — `server/api/real_time.py`
- **UUID** (7 connections)
- **_parse_websocket_token()** (6 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (6 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_path_or_token()** (6 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (5 connections) — `server/api/real_time.py`
- **_parse_subprotocol_token()** (4 connections) — `server/api/real_time.py`
- **Request** (4 connections)
- **_extract_bearer_token()** (3 connections) — `server/api/real_time.py`
- **get** (2 connections)
- **post** (1 connections)
- *... and 18 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [log_and_raise](log_and_raise.md) (4 shared connections)
- [create_access_token](create_access_token.md) (3 shared connections)
- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (3 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (3 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (3 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/async_persistence.py`
- `server/realtime/connection_state_machine.py`

## Audit Trail

- EXTRACTED: 134 (80%)
- INFERRED: 34 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*