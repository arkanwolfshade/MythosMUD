# disconnect_grace_period.py

> 53 nodes

## Key Concepts

- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (18 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **extract_player_name()** (16 connections) — `server/realtime/player_presence_utils.py`
- **player_presence_utils.py** (16 connections) — `server/realtime/player_presence_utils.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **asyncio** (9 connections)
- **get_player_position()** (6 connections) — `server/realtime/player_presence_utils.py`
- **test_start_grace_period_reconnection_cancels()** (5 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **_get_name_from_user()** (4 connections) — `server/realtime/player_presence_utils.py`
- **_is_valid_name()** (4 connections) — `server/realtime/player_presence_utils.py`
- **test_cancel_grace_period_cancels_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_not_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_errors_gracefully()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_already_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_creates_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_timer_expires()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **UUID** (4 connections)
- **_is_uuid_string()** (3 connections) — `server/realtime/player_presence_utils.py`
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_false()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_no_manager_attribute()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- *... and 28 more nodes in this community*

## Relationships

- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (12 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (9 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (8 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (7 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (3 shared connections)
- [test_look_player.py](test_look_player.py.md) (3 shared connections)
- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [GameStateProvider](GameStateProvider.md) (2 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (2 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (2 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 243 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*