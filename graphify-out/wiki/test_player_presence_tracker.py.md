# test_player_presence_tracker.py

> 74 nodes

## Key Concepts

- **test_player_presence_tracker.py** (60 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **InstanceManager** (41 connections) — `server/game/instance_manager.py`
- **asyncio** (22 connections)
- **broadcast_connection_message_impl()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **test_tutorial_reentry_gives_stranded_player_a_fresh_instance()** (9 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_tutorial_reentry_ignores_players_outside_templates()** (9 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **_manager_with()** (6 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **_foyer()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **_template_bedroom()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_broadcast_connection_message_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_warms_corruption_tier_cache()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_finally_cleanup()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_acquire_disconnect_lock_already_disconnecting()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_acquire_disconnect_lock_stuck_player()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_acquire_disconnect_lock_success()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_broadcast_connection_message_impl()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_broadcast_connection_message_impl_no_room()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_error()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_existing_connection()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_new_connection()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_new_connection_no_catchup()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_no_room_id()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_reconnect_during_grace()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_reconnect_sends_catchup()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- *... and 49 more nodes in this community*

## Relationships

- [player_presence_tracker.py](player_presence_tracker.py.md) (42 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [test_instance_manager.py](test_instance_manager.py.md) (12 shared connections)
- [.create_instance](create_instance.md) (9 shared connections)
- [Room](Room.md) (4 shared connections)
- [CorruptionTier](CorruptionTier.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (2 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (2 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/game/instance_manager.py`
- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`

## Audit Trail

- EXTRACTED: 184 (91%)
- INFERRED: 19 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*