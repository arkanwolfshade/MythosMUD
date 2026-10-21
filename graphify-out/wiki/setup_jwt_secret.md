# setup_jwt_secret

> 126 nodes · cohesion 0.03

## Key Concepts

- **player_presence_tracker.py** (60 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker.py** (60 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **track_player_disconnected_impl()** (32 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_connected_impl()** (22 connections) — `server/realtime/player_presence_tracker.py`
- **asyncio** (22 connections)
- **Any** (11 connections)
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (10 connections)
- **_warm_corruption_tier_cache()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id_for_tutorial_reconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_send_grace_reconnect_catchup()** (8 connections) — `server/realtime/player_presence_tracker.py`
- **_disconnect_during_rest_is_intentional()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_intentional_disconnect()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **.async_persistence()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (7 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_GraceReconnectManager** (6 connections) — `server/realtime/player_presence_tracker.py`
- **RoomLookup** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_stranded_template_id()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **test_broadcast_connection_message_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- *... and 101 more nodes in this community*

## Relationships

- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (18 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (16 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (11 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (9 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (6 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (5 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (4 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (4 shared connections)
- [FollowService](FollowService.md) (3 shared connections)
- [.publish_with_pool](publish_with_pool.md) (3 shared connections)
- [test_disconnect_catchup.py](test_disconnect_catchup.py.md) (3 shared connections)
- [ChatService](ChatService.md) (3 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`
- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 324 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*