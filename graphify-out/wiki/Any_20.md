# Any

> 25 nodes

## Key Concepts

- **player_connection_setup.py** (24 connections) — `server/realtime/player_connection_setup.py`
- **handle_new_connection_setup()** (17 connections) — `server/realtime/player_connection_setup.py`
- **_broadcast_player_entered_game()** (9 connections) — `server/realtime/player_connection_setup.py`
- **_trigger_quests_for_room_on_spawn()** (8 connections) — `server/realtime/player_connection_setup.py`
- **UUID** (7 connections)
- **_send_room_occupants_update_after_connection()** (7 connections) — `server/realtime/player_connection_setup.py`
- **_update_player_last_active()** (6 connections) — `server/realtime/player_connection_setup.py`
- **Any** (6 connections)
- **_add_player_to_room_silently()** (5 connections) — `server/realtime/player_connection_setup.py`
- **test_player_connection_setup_grace_period.py** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **_stable_room_id_for_quest()** (3 connections) — `server/realtime/player_connection_setup.py`
- **test_reconnection_cancels_grace_period()** (3 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_reconnection_no_grace_period()** (3 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **Player** (2 connections)
- **Player connection setup functions.  This module handles the setup tasks when a p** (1 connections) — `server/realtime/player_connection_setup.py`
- **Update last_active timestamp in database when player connects.      Args:** (1 connections) — `server/realtime/player_connection_setup.py`
- **Return stable room id for quest_offers lookup; strip instance_<uuid>_ prefix if** (1 connections) — `server/realtime/player_connection_setup.py`
- **On spawn, explicitly start quests offered by this room (e.g. Leave the Tutorial)** (1 connections) — `server/realtime/player_connection_setup.py`
- **Add player to the Room object without triggering PlayerEnteredRoom.      Movemen** (1 connections) — `server/realtime/player_connection_setup.py`
- **Broadcast a structured entry event to other occupants (excluding the newcomer).** (1 connections) — `server/realtime/player_connection_setup.py`
- **Send room_occupants update so other players see the new occupant.      Args:** (1 connections) — `server/realtime/player_connection_setup.py`
- **Handle setup tasks for a new player connection.      Args:         player_id: Th** (1 connections) — `server/realtime/player_connection_setup.py`
- **Unit tests for player connection setup grace period integration.  Tests that rec** (1 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **Test that reconnection cancels grace period.** (1 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **Test that reconnection does nothing if player not in grace period.** (1 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`

## Relationships

- [real time](real_time.md) (5 shared connections)
- [Any](Any.md) (5 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (3 shared connections)
- [login grace period](login_grace_period.md) (3 shared connections)
- [player presence tracker](player_presence_tracker.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [notify quest abandoned()](notify_quest_abandoned%28%29.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)

## Source Files

- `server/realtime/player_connection_setup.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`

## Audit Trail

- EXTRACTED: 110 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*