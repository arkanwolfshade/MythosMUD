# player presence tracker

> 86 nodes

## Key Concepts

- **test_player_presence_tracker.py** (38 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **player_presence_tracker.py** (31 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (29 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_connected_impl()** (16 connections) — `server/realtime/player_presence_tracker.py`
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
- *... and 61 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (8 shared connections)
- [Room Broadcast](Room_Broadcast.md) (7 shared connections)
- [look helpers commands](look_helpers_commands.md) (6 shared connections)
- [help content websocket](help_content_websocket.md) (6 shared connections)
- [emote game service](emote_game_service.md) (5 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)
- [uuid npc combat](uuid_npc_combat.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 321 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*