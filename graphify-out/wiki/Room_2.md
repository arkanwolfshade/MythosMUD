# Room

> 101 nodes

## Key Concepts

- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **websocket_initial_state.py** (28 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_room_state()** (16 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (13 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (12 connections) — `server/realtime/websocket_initial_state.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (7 connections)
- **prepare_room_data_with_occupants()** (7 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **_AppWithState** (6 connections) — `server/realtime/websocket_initial_state.py`
- **WebSocket** (5 connections)
- **_AppStateForEventHandler** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcLifecycleManagerForOccupants** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateWithNpcLifecycle** (5 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_get_event_handler_from_app_host()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **mock_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_dead()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- *... and 76 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (12 shared connections)
- [Player](Player.md) (10 shared connections)
- [UUID](UUID.md) (5 shared connections)
- [spawn defaults](spawn_defaults.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 347 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*