# test_player_presence_tracker.py

> 186 nodes

## Key Concepts

- **test_player_presence_tracker.py** (37 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **player_presence_tracker.py** (35 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **track_player_disconnected_impl()** (30 connections) — `server/realtime/player_presence_tracker.py`
- **player_disconnect_handlers.py** (27 connections) — `server/realtime/player_disconnect_handlers.py`
- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **extract_player_name()** (16 connections) — `server/realtime/player_presence_utils.py`
- **player_presence_utils.py** (16 connections) — `server/realtime/player_presence_utils.py`
- **asyncio** (16 connections)
- **track_player_connected_impl()** (14 connections) — `server/realtime/player_presence_tracker.py`
- **age_off_disconnected_sessions()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **Any** (11 connections)
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **asyncio** (8 connections)
- **_disconnect_during_rest_is_intentional()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (7 connections)
- **test_player_presence_tracker_grace_period.py** (7 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- *... and 161 more nodes in this community*

## Relationships

- [is_player_in_grace_period](is_player_in_grace_period.md) (16 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (10 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (7 shared connections)
- [connection_manager.py](connection_manager.py.md) (5 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [connection_manager_health_cleanup.py](connection_manager_health_cleanup.py.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [time.py](time.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [.state](state.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/realtime/player_presence_tracker.py`
- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 750 (99%)
- INFERRED: 8 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*