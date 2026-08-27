# test_room_subscription_manager_drops.py

> 61 nodes

## Key Concepts

- **websocket_helpers.py** (36 connections) — `server/realtime/websocket_helpers.py`
- **test_websocket_helpers_player.py** (24 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **get_player_and_room()** (14 connections) — `server/realtime/websocket_helpers.py`
- **prepare_player_data()** (12 connections) — `server/realtime/websocket_helpers.py`
- **get_player_stats_data()** (8 connections) — `server/realtime/websocket_helpers.py`
- **build_basic_player_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **get_player_service_from_connection_manager()** (7 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (7 connections)
- **convert_schema_to_dict()** (6 connections) — `server/realtime/websocket_helpers.py`
- **UUID** (6 connections)
- **_ensure_player_in_room_occupancy()** (4 connections) — `server/realtime/websocket_helpers.py`
- **_get_tracked_player_from_connection_manager()** (4 connections) — `server/realtime/websocket_helpers.py`
- **test_get_player_and_room_adds_player_to_room()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_room_not_found()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_prepare_player_data_no_service()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_prepare_player_data_service_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_prepare_player_data_with_service()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **_MutePersistenceLoader** (3 connections) — `server/realtime/websocket_helpers.py`
- **_fetch_room_for_tracked_player()** (3 connections) — `server/realtime/websocket_helpers.py`
- **test_build_basic_player_data()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_build_basic_player_data_defaults()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_service_from_connection_manager_no_app()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_service_from_connection_manager_no_state()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- *... and 36 more nodes in this community*

## Relationships

- [CombatAuditLogger](CombatAuditLogger.md) (11 shared connections)
- [field_validator](field_validator.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [test_goto_helpers.py](test_goto_helpers.py.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [App.tsx](App.tsx.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`

## Audit Trail

- EXTRACTED: 131 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*