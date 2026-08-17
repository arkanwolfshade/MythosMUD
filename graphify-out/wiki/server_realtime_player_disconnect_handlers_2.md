# server realtime player disconnect handlers

> 101 nodes

## Key Concepts

- **test_player_presence_tracker.py** (39 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **player_presence_tracker.py** (35 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (28 connections) — `server/realtime/player_presence_tracker.py`
- **asyncio** (17 connections)
- **track_player_connected_impl()** (13 connections) — `server/realtime/player_presence_tracker.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **Any** (11 connections)
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (8 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **broadcast_connection_message_impl()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_disconnect_during_rest_is_intentional()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_get_instance_manager_from_manager()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (7 connections)
- **_resolve_intentional_disconnect()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (6 connections)
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **test_broadcast_connection_message_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_finally_cleanup()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **_get_session_maps_for_age_off()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_purge_expired_sessions_from_maps()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- *... and 76 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (18 shared connections)
- [server realtime player disconnect handlers](server_realtime_player_disconnect_handlers.md) (13 shared connections)
- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (7 shared connections)
- [server realtime player presence utils](server_realtime_player_presence_utils.md) (5 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (5 shared connections)
- [server realtime connection delegates delegate](server_realtime_connection_delegates_delegate.md) (2 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (2 shared connections)
- [server commands rest command](server_commands_rest_command.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (2 shared connections)
- [server realtime player connection setup](server_realtime_player_connection_setup.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`
- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 238 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*