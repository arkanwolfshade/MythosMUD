# test_websocket_initial_state.py

> 14 nodes

## Key Concepts

- **test_websocket_initial_state.py** (47 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_success()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_game_state_event_safely_close_message_sent()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_game_state_event_safely_disconnected()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_get_event_handler_for_initial_state_from_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_get_event_handler_for_initial_state_from_websocket()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_get_event_handler_for_initial_state_not_found()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Unit tests for WebSocket initial state. Tests the websocket_initial_state…** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test send_game_state_event_safely() returns True when WebSocket disconnected.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test send_game_state_event_safely() returns True when close message sent.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test send_initial_game_state() successfully sends initial game state.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test get_event_handler_for_initial_state() gets handler from connection manager.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test get_event_handler_for_initial_state() gets handler from websocket.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test get_event_handler_for_initial_state() returns None when not found.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`

## Relationships

- [send_initial_room_state](send_initial_room_state.md) (11 shared connections)
- [asyncio](asyncio.md) (11 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [add_npc_occupants_to_list](add_npc_occupants_to_list.md) (4 shared connections)
- [send_occupants_snapshot_if_needed](send_occupants_snapshot_if_needed.md) (4 shared connections)
- [mock_connection_manager](mock_connection_manager.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [prepare_initial_room_data](prepare_initial_room_data.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_send_initial_game_state_handles_exception](test_send_initial_game_state_handles_exception.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 62 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*