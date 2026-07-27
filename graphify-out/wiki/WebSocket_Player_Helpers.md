# WebSocket Player Helpers

> 58 nodes · cohesion 0.06

## Key Concepts

- **websocket_helpers.py** (35 connections) — `server/realtime/websocket_helpers.py`
- **test_websocket_helpers_player.py** (22 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **get_player_and_room()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **prepare_player_data()** (12 connections) — `server/realtime/websocket_helpers.py`
- **get_player_stats_data()** (8 connections) — `server/realtime/websocket_helpers.py`
- **build_basic_player_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **convert_schema_to_dict()** (7 connections) — `server/realtime/websocket_helpers.py`
- **get_player_service_from_connection_manager()** (7 connections) — `server/realtime/websocket_helpers.py`
- **UUID** (6 connections) — `server/realtime/websocket_helpers.py`
- **test_prepare_player_data_service_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **_ensure_player_in_room_occupancy()** (4 connections) — `server/realtime/websocket_helpers.py`
- **_get_tracked_player_from_connection_manager()** (4 connections) — `server/realtime/websocket_helpers.py`
- **test_build_basic_player_data()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_build_basic_player_data_defaults()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_adds_player_to_room()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_room_not_found()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_service_from_connection_manager_no_app()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_service_from_connection_manager_no_state()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_service_from_connection_manager_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_stats_data_adds_health()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_stats_data_no_get_stats()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_stats_data_string_stats()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- *... and 33 more nodes in this community*

## Relationships

- [[WebSocket Helper Utilities]] (11 shared connections)
- [[WebSocket Initial State]] (7 shared connections)
- [[WebSocket Message Validation]] (4 shared connections)
- [[Realtime WebSocket Auth]] (3 shared connections)
- [[Admin Shutdown Command]] (2 shared connections)
- [[Character Creation API]] (2 shared connections)
- [[WebSocket Command Handler]] (2 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Player Combat XP]] (2 shared connections)
- [[Database Manager Tests]] (1 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)
- [[Player Domain Model]] (1 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`

## Audit Trail

- EXTRACTED: 221 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
