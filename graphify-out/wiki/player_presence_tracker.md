# player presence tracker

> 101 nodes

## Key Concepts

- **test_player_presence_tracker.py** (38 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **player_presence_tracker.py** (31 connections) — `server/realtime/player_presence_tracker.py`
- **player_connection_setup.py** (25 connections) — `server/realtime/player_connection_setup.py`
- **handle_new_connection_setup()** (17 connections) — `server/realtime/player_connection_setup.py`
- **track_player_connected_impl()** (16 connections) — `server/realtime/player_presence_tracker.py`
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **_broadcast_player_entered_game()** (9 connections) — `server/realtime/player_connection_setup.py`
- **Any** (9 connections)
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_trigger_quests_for_room_on_spawn()** (8 connections) — `server/realtime/player_connection_setup.py`
- **UUID** (7 connections)
- **_send_room_occupants_update_after_connection()** (7 connections) — `server/realtime/player_connection_setup.py`
- **_update_player_last_active()** (6 connections) — `server/realtime/player_connection_setup.py`
- **Any** (6 connections)
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_add_player_to_room_silently()** (5 connections) — `server/realtime/player_connection_setup.py`
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_connection_setup_grace_period.py** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **UUID** (4 connections)
- **test_broadcast_connection_message_impl_error()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_error()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_finally_cleanup()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- *... and 76 more nodes in this community*

## Relationships

- [player disconnect handlers](player_disconnect_handlers.md) (23 shared connections)
- [Database Config](Database_Config.md) (11 shared connections)
- [help content websocket](help_content_websocket.md) (8 shared connections)
- [Loot Generation](Loot_Generation.md) (7 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [command utility models](command_utility_models.md) (3 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (3 shared connections)
- [nats services metrics](nats_services_metrics.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [tsconfig build {ts,tsx}](tsconfig_build_%7Bts%2Ctsx%7D.md) (1 shared connections)
- [quest service game](quest_service_game.md) (1 shared connections)

## Source Files

- `server/realtime/player_connection_setup.py`
- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`

## Audit Trail

- EXTRACTED: 384 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*