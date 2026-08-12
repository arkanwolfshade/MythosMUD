# websocket_initial_state.py

> 81 nodes

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **asyncio** (21 connections)
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcLifecycleManagerForOccupants** (6 connections) — `server/realtime/websocket_initial_state.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (6 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **WebSocket** (5 connections)
- **test_add_npc_occupants_to_list_filters_dead_npcs()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_add_npc_occupants_to_list_no_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_add_npc_occupants_to_list_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_dead()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_prepare_initial_room_data()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_prepare_room_data_with_occupants()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- *... and 56 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (10 shared connections)
- [Protocol](Protocol.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (5 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (5 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [mock_connection_manager](mock_connection_manager.md) (4 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)
- [validate_occupant_name](validate_occupant_name.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 215 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*