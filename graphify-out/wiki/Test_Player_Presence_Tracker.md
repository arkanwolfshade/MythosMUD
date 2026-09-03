# Test Player Presence Tracker

> 103 nodes

## Key Concepts

- **test_player_presence_tracker.py** (40 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **player_presence_tracker.py** (35 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (25 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_connected_impl()** (19 connections) — `server/realtime/player_presence_tracker.py`
- **asyncio** (19 connections)
- **Any** (11 connections)
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (9 connections)
- **_build_player_info()** (8 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (8 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_disconnect_during_rest_is_intentional()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_send_grace_reconnect_catchup()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_GraceReconnectManager** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_intentional_disconnect()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **test_track_player_disconnected_intentional_no_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_mid_rest_skips_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_removes_from_intentional_set()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_unintentional_starts_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_acquire_disconnect_lock_already_disconnecting()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_acquire_disconnect_lock_stuck_player()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- *... and 78 more nodes in this community*

## Relationships

- [Test Disconnect Catchup](Test_Disconnect_Catchup.md) (7 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (6 shared connections)
- [Test Rest And Grace Period](Test_Rest_And_Grace_Period.md) (6 shared connections)
- [Test Rest Command](Test_Rest_Command.md) (4 shared connections)
- [Connection Manager](Connection_Manager.md) (3 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (2 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [Player Event Handlers Respawn Room](Player_Event_Handlers_Respawn_Room.md) (1 shared connections)
- [Instance Manager](Instance_Manager.md) (1 shared connections)
- [Test Envelope](Test_Envelope.md) (1 shared connections)
- [Player Connection Setup](Player_Connection_Setup.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 229 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*