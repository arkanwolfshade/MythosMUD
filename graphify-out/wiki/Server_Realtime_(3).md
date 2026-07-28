# Server Realtime (3)

> 170 nodes

## Key Concepts

- **test_player_presence_tracker.py** (37 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **player_presence_tracker.py** (31 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (29 connections) — `server/realtime/player_presence_tracker.py`
- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **player_disconnect_handlers.py** (26 connections) — `server/realtime/player_disconnect_handlers.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **player_presence_utils.py** (16 connections) — `server/realtime/player_presence_utils.py`
- **extract_player_name()** (16 connections) — `server/realtime/player_presence_utils.py`
- **track_player_connected_impl()** (15 connections) — `server/realtime/player_presence_tracker.py`
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
- **get_player_position()** (7 connections) — `server/realtime/player_presence_utils.py`
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (6 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- *... and 145 more nodes in this community*

## Relationships

- [Server Realtime (20)](Server_Realtime_%2820%29.md) (17 shared connections)
- [Server Persistence](Server_Persistence.md) (11 shared connections)
- [Server Commands](Server_Commands.md) (10 shared connections)
- [Server Realtime (67)](Server_Realtime_%2867%29.md) (7 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (7 shared connections)
- [Server Admin](Server_Admin.md) (4 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (4 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (3 shared connections)
- [Server Realtime (8)](Server_Realtime_%288%29.md) (3 shared connections)
- [Server Services](Server_Services.md) (2 shared connections)
- [Server Commands (3)](Server_Commands_%283%29.md) (1 shared connections)
- [Server Commands (17)](Server_Commands_%2817%29.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/realtime/player_presence_tracker.py`
- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 680 (98%)
- INFERRED: 13 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*