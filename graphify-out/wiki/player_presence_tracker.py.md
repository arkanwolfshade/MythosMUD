# player_presence_tracker.py

> 129 nodes

## Key Concepts

- **player_presence_tracker.py** (50 connections) — `server/realtime/player_presence_tracker.py`
- **disconnect_grace_period.py** (35 connections) — `server/realtime/disconnect_grace_period.py`
- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **player_disconnect_handlers.py** (28 connections) — `server/realtime/player_disconnect_handlers.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_disconnect_catchup.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **build_catchup_message()** (14 connections) — `server/realtime/disconnect_catchup.py`
- **CatchupManager** (11 connections) — `server/realtime/disconnect_catchup.py`
- **CatchupPlayer** (11 connections) — `server/realtime/disconnect_catchup.py`
- **capture_grace_snapshot()** (11 connections) — `server/realtime/disconnect_catchup.py`
- **age_off_disconnected_sessions()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **_manager()** (10 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **disconnect_catchup.py** (10 connections) — `server/realtime/disconnect_catchup.py`
- **_player()** (9 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **_send_grace_reconnect_catchup()** (8 connections) — `server/realtime/player_presence_tracker.py`
- **asyncio** (8 connections)
- **_FakePlayer** (7 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **UUID** (7 connections)
- **_GraceReconnectManager** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_dp_snapshot()** (5 connections) — `server/realtime/disconnect_catchup.py`
- **test_build_catchup_message_none_without_snapshot()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_reports_damage_taken()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- *... and 104 more nodes in this community*

## Relationships

- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (22 shared connections)
- [start_grace_period](start_grace_period.md) (14 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [extract_player_name](extract_player_name.md) (8 shared connections)
- [Player](Player.md) (7 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (3 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (3 shared connections)
- [CorruptionTier](CorruptionTier.md) (2 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)

## Source Files

- `server/realtime/disconnect_catchup.py`
- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_disconnect_catchup.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 322 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*