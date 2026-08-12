# player_connection_setup.py

> 26 nodes

## Key Concepts

- **player_connection_setup.py** (24 connections) — `server/realtime/player_connection_setup.py`
- **handle_new_connection_setup()** (17 connections) — `server/realtime/player_connection_setup.py`
- **_broadcast_player_entered_game()** (8 connections) — `server/realtime/player_connection_setup.py`
- **_trigger_quests_for_room_on_spawn()** (8 connections) — `server/realtime/player_connection_setup.py`
- **UUID** (7 connections)
- **_send_room_occupants_update_after_connection()** (6 connections) — `server/realtime/player_connection_setup.py`
- **Any** (6 connections)
- **_add_player_to_room_silently()** (5 connections) — `server/realtime/player_connection_setup.py`
- **_update_player_last_active()** (5 connections) — `server/realtime/player_connection_setup.py`
- **test_player_connection_setup_grace_period.py** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_reconnection_cancels_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_reconnection_no_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **_stable_room_id_for_quest()** (3 connections) — `server/realtime/player_connection_setup.py`
- **Player** (2 connections)
- **asyncio** (2 connections)
- **Player connection setup functions. This module handles the setup tasks when a…** (1 connections) — `server/realtime/player_connection_setup.py`
- **Broadcast a structured entry event to other occupants (excluding the newcomer).…** (1 connections) — `server/realtime/player_connection_setup.py`
- **Send room_occupants update so other players see the new occupant. Args:…** (1 connections) — `server/realtime/player_connection_setup.py`
- **Handle setup tasks for a new player connection. Args: player_id: The player's…** (1 connections) — `server/realtime/player_connection_setup.py`
- **Update last_active timestamp in database when player connects. Args: player_id:…** (1 connections) — `server/realtime/player_connection_setup.py`
- **Return stable room id for quest_offers lookup; strip instance_<uuid>_ prefix if…** (1 connections) — `server/realtime/player_connection_setup.py`
- **On spawn, explicitly start quests offered by this room (e.g. Leave the…** (1 connections) — `server/realtime/player_connection_setup.py`
- **Add player to the Room object without triggering PlayerEnteredRoom. Movement…** (1 connections) — `server/realtime/player_connection_setup.py`
- **Unit tests for player connection setup grace period integration. Tests that…** (1 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **Test that reconnection cancels grace period.** (1 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- *... and 1 more nodes in this community*

## Relationships

- [disconnect_grace_period.py](disconnect_grace_period.py.md) (6 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/realtime/player_connection_setup.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`

## Audit Trail

- EXTRACTED: 114 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*