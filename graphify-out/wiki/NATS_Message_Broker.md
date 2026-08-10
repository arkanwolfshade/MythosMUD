# NATS Message Broker

> 201 nodes

## Key Concepts

- **test_player_presence_tracker.py** (37 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **player_presence_tracker.py** (31 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (29 connections) — `server/realtime/player_presence_tracker.py`
- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **player_disconnect_handlers.py** (26 connections) — `server/realtime/player_disconnect_handlers.py`
- **player_connection_setup.py** (24 connections) — `server/realtime/player_connection_setup.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_new_connection_setup()** (17 connections) — `server/realtime/player_connection_setup.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **player_presence_utils.py** (16 connections) — `server/realtime/player_presence_utils.py`
- **extract_player_name()** (16 connections) — `server/realtime/player_presence_utils.py`
- **track_player_connected_impl()** (15 connections) — `server/realtime/player_presence_tracker.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **age_off_disconnected_sessions()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **_broadcast_player_entered_game()** (9 connections) — `server/realtime/player_connection_setup.py`
- **Any** (9 connections)
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_trigger_quests_for_room_on_spawn()** (8 connections) — `server/realtime/player_connection_setup.py`
- **UUID** (7 connections)
- *... and 176 more nodes in this community*

## Relationships

- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (19 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (15 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (15 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (10 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (7 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (3 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (3 shared connections)
- [Spell Effects Tests](Spell_Effects_Tests.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Look Player Command](Look_Player_Command.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_connection_setup.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/realtime/player_presence_tracker.py`
- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 769 (98%)
- INFERRED: 19 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*