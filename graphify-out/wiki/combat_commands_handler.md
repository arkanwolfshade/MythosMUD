# combat commands handler

> 58 nodes

## Key Concepts

- **real_time.py** (36 connections) — `server/api/real_time.py`
- **test_real_time_helpers.py** (31 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **_resolve_player_id()** (11 connections) — `server/api/real_time.py`
- **handle_new_game_session()** (11 connections) — `server/api/real_time.py`
- **_ensure_connection_manager()** (10 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (10 connections) — `server/api/real_time.py`
- **Any** (9 connections)
- **_parse_websocket_token()** (9 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_test()** (9 connections) — `server/api/real_time.py`
- **get_player_connections()** (9 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (9 connections) — `server/api/real_time.py`
- **WebSocket** (8 connections)
- **_validate_websocket_connection_manager()** (8 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_path_or_token()** (8 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (7 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (7 connections) — `server/api/real_time.py`
- **UUID** (7 connections)
- **_extract_bearer_token()** (6 connections) — `server/api/real_time.py`
- **_parse_subprotocol_token()** (5 connections) — `server/api/real_time.py`
- **Request** (4 connections)
- **test_ensure_connection_manager_missing()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_token_no_player()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_missing_token_and_player_id()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_missing_session_id()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_invalid_json()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- *... and 33 more nodes in this community*

## Relationships

- [auth users rationale](auth_users_rationale.md) (14 shared connections)
- [Exception Containers](Exception_Containers.md) (14 shared connections)
- [models npc rationale](models_npc_rationale.md) (7 shared connections)
- [command utility models](command_utility_models.md) (7 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (3 shared connections)
- [auth rationale access](auth_rationale_access.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (2 shared connections)
- [room look commands](room_look_commands.md) (1 shared connections)
- [player service game](player_service_game.md) (1 shared connections)
- [look helpers commands](look_helpers_commands.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 274 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*