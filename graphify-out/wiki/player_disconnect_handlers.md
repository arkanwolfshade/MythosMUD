# player disconnect handlers

> 163 nodes

## Key Concepts

- **test_player_presence_tracker.py** (38 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **player_presence_tracker.py** (31 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (29 connections) — `server/realtime/player_presence_tracker.py`
- **player_disconnect_handlers.py** (27 connections) — `server/realtime/player_disconnect_handlers.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **track_player_connected_impl()** (16 connections) — `server/realtime/player_presence_tracker.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **age_off_disconnected_sessions()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **Any** (9 connections)
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (7 connections)
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (6 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **_get_session_maps_for_age_off()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_purge_expired_sessions_from_maps()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **UUID** (4 connections)
- **instance_manager()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- *... and 138 more nodes in this community*

## Relationships

- [combat services turn](combat_services_turn.md) (15 shared connections)
- [help content websocket](help_content_websocket.md) (12 shared connections)
- [Room Broadcast](Room_Broadcast.md) (9 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (8 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [container service services](container_service_services.md) (3 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (2 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (2 shared connections)
- [room models instance](room_models_instance.md) (2 shared connections)
- [room look commands](room_look_commands.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`
- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 581 (98%)
- INFERRED: 12 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*