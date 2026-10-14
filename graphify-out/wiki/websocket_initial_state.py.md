# websocket_initial_state.py

> 72 nodes

## Key Concepts

- **websocket_initial_state.py** (57 connections) — `server/realtime/websocket_initial_state.py`
- **websocket_handler_connection.py** (24 connections) — `server/realtime/websocket_handler_connection.py`
- **send_initial_room_state()** (21 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (20 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (17 connections) — `server/realtime/websocket_initial_state.py`
- **validate_occupant_name()** (16 connections) — `server/realtime/websocket_helpers.py`
- **check_and_send_delirium_notification()** (11 connections) — `server/realtime/websocket_initial_state.py`
- **setup_initial_connection_state()** (10 connections) — `server/realtime/websocket_handler_connection.py`
- **get_event_handler_for_initial_state()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (9 connections)
- **UUID** (9 connections)
- **_resolve_stored_death_location()** (7 connections) — `server/realtime/websocket_initial_state.py`
- **_RealTimeEventHandlerForInitialState** (6 connections) — `server/realtime/websocket_initial_state.py`
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **_get_lucidity_for_client()** (6 connections) — `server/realtime/websocket_initial_state.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (6 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **_get_death_location_name()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_lookup_death_room_display_name()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **WebSocket** (5 connections)
- **_NpcLifecycleManagerForOccupants** (4 connections) — `server/realtime/websocket_initial_state.py`
- **_PlayerHandlerForOccupantsSnapshot** (4 connections) — `server/realtime/websocket_initial_state.py`
- *... and 47 more nodes in this community*

## Relationships

- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (37 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (12 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [build_event](build_event.md) (8 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (8 shared connections)
- [player_event_handlers_respawn_room.py](player_event_handlers_respawn_room.py.md) (6 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (6 shared connections)
- [test_superseded_connection_cleanup.py](test_superseded_connection_cleanup.py.md) (4 shared connections)
- [real_time.py](real_time.py.md) (4 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)
- [test_room_utils.py](test_room_utils.py.md) (3 shared connections)
- [AsyncPersistenceRoomLookup](AsyncPersistenceRoomLookup.md) (3 shared connections)

## Source Files

- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 235 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*