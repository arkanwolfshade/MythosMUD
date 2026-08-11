# Rescue Service Tests

> 84 nodes

## Key Concepts

- **test_player_presence_tracker.py** (37 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **player_presence_tracker.py** (31 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (29 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_connected_impl()** (15 connections) — `server/realtime/player_presence_tracker.py`
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **Any** (9 connections)
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (6 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (4 connections)
- **test_broadcast_connection_message_impl_error()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_error()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_finally_cleanup()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_build_player_info_new_connection()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_build_player_info_existing_connection()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_build_player_info_no_level()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_success()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_room_no_id()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_new_connection()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- *... and 59 more nodes in this community*

## Relationships

- [NATS Message Broker](NATS_Message_Broker.md) (12 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (10 shared connections)
- [Chat Rate Limiter](Chat_Rate_Limiter.md) (9 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (3 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [Combat Messaging Tests](Combat_Messaging_Tests.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 315 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*