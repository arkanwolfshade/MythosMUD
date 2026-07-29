# Any

> 38 nodes

## Key Concepts

- **player_connection_setup.py** (23 connections) — `server/realtime/player_connection_setup.py`
- **handle_new_connection_setup()** (15 connections) — `server/realtime/player_connection_setup.py`
- **extract_player_name()** (13 connections) — `server/realtime/player_presence_utils.py`
- **_broadcast_player_entered_game()** (9 connections) — `server/realtime/player_connection_setup.py`
- **_trigger_quests_for_room_on_spawn()** (8 connections) — `server/realtime/player_connection_setup.py`
- **UUID** (7 connections)
- **_send_room_occupants_update_after_connection()** (7 connections) — `server/realtime/player_connection_setup.py`
- **_update_player_last_active()** (6 connections) — `server/realtime/player_connection_setup.py`
- **Any** (6 connections)
- **_add_player_to_room_silently()** (5 connections) — `server/realtime/player_connection_setup.py`
- **_get_name_from_user()** (5 connections) — `server/realtime/player_presence_utils.py`
- **get_player_position()** (5 connections) — `server/realtime/player_presence_utils.py`
- **test_player_connection_setup_grace_period.py** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **_is_valid_name()** (4 connections) — `server/realtime/player_presence_utils.py`
- **_stable_room_id_for_quest()** (3 connections) — `server/realtime/player_connection_setup.py`
- **_is_uuid_string()** (3 connections) — `server/realtime/player_presence_utils.py`
- **Player** (3 connections)
- **UUID** (3 connections)
- **test_reconnection_cancels_grace_period()** (3 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_reconnection_no_grace_period()** (3 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **Player** (2 connections)
- **Player connection setup functions.  This module handles the setup tasks when a p** (1 connections) — `server/realtime/player_connection_setup.py`
- **Update last_active timestamp in database when player connects.      Args:** (1 connections) — `server/realtime/player_connection_setup.py`
- **Return stable room id for quest_offers lookup; strip instance_<uuid>_ prefix if** (1 connections) — `server/realtime/player_connection_setup.py`
- **On spawn, explicitly start quests offered by this room (e.g. Leave the Tutorial)** (1 connections) — `server/realtime/player_connection_setup.py`
- *... and 13 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (16 shared connections)
- [disconnect grace period](disconnect_grace_period.md) (5 shared connections)
- [login grace period](login_grace_period.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [test quest service](test_quest_service.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/realtime/player_connection_setup.py`
- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`

## Audit Trail

- EXTRACTED: 147 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*