# Disconnect Grace Period

> 224 nodes · cohesion 0.02

## Key Concepts

- **test_player_presence_tracker.py** (36 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_player_disconnect_handlers.py** (33 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **player_presence_tracker.py** (30 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (28 connections) — `server/realtime/player_presence_tracker.py`
- **player_disconnect_handlers.py** (24 connections) — `server/realtime/player_disconnect_handlers.py`
- **disconnect_grace_period.py** (23 connections) — `server/realtime/disconnect_grace_period.py`
- **player_connection_setup.py** (23 connections) — `server/realtime/player_connection_setup.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_new_connection_setup()** (17 connections) — `server/realtime/player_connection_setup.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **player_presence_utils.py** (16 connections) — `server/realtime/player_presence_utils.py`
- **extract_player_name()** (16 connections) — `server/realtime/player_presence_utils.py`
- **test_disconnect_grace_period.py** (16 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **track_player_connected_impl()** (14 connections) — `server/realtime/player_presence_tracker.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **broadcast_connection_message_impl()** (12 connections) — `server/realtime/player_presence_tracker.py`
- **age_off_disconnected_sessions()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_broadcast_player_entered_game()** (10 connections) — `server/realtime/player_connection_setup.py`
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- *... and 199 more nodes in this community*

## Relationships

- [[NPC Admin API]] (22 shared connections)
- [[Look Command Helpers]] (18 shared connections)
- [[Room Occupant Events]] (14 shared connections)
- [[Rest Command Flow]] (5 shared connections)
- [[Combat Player Broadcasts]] (5 shared connections)
- [[SQLAlchemy Model Base]] (3 shared connections)
- [[Player Respawn Events]] (2 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)
- [[Async Persistence Layer]] (1 shared connections)
- [[Distributed Event Bus]] (1 shared connections)
- [[Room Occupancy Class]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_connection_setup.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/realtime/player_presence_tracker.py`
- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 882 (100%)
- INFERRED: 3 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
