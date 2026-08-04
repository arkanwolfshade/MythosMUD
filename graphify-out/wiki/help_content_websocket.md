# help content websocket

> 52 nodes

## Key Concepts

- **player_connection_setup.py** (25 connections) — `server/realtime/player_connection_setup.py`
- **extract_player_name()** (22 connections) — `server/realtime/player_presence_utils.py`
- **test_player_presence_utils.py** (18 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **handle_new_connection_setup()** (17 connections) — `server/realtime/player_connection_setup.py`
- **player_presence_utils.py** (17 connections) — `server/realtime/player_presence_utils.py`
- **get_player_position()** (11 connections) — `server/realtime/player_presence_utils.py`
- **_broadcast_player_entered_game()** (9 connections) — `server/realtime/player_connection_setup.py`
- **_trigger_quests_for_room_on_spawn()** (8 connections) — `server/realtime/player_connection_setup.py`
- **UUID** (7 connections)
- **_send_room_occupants_update_after_connection()** (7 connections) — `server/realtime/player_connection_setup.py`
- **_update_player_last_active()** (6 connections) — `server/realtime/player_connection_setup.py`
- **Any** (6 connections)
- **_is_valid_name()** (6 connections) — `server/realtime/player_presence_utils.py`
- **_add_player_to_room_silently()** (5 connections) — `server/realtime/player_connection_setup.py`
- **_is_uuid_string()** (5 connections) — `server/realtime/player_presence_utils.py`
- **_get_name_from_user()** (5 connections) — `server/realtime/player_presence_utils.py`
- **test_player_connection_setup_grace_period.py** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **_stable_room_id_for_quest()** (3 connections) — `server/realtime/player_connection_setup.py`
- **Player** (3 connections)
- **UUID** (3 connections)
- **test_reconnection_cancels_grace_period()** (3 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_reconnection_no_grace_period()** (3 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_extract_player_name_user_access_error()** (3 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **test_get_player_position_stats_error()** (3 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **Player** (2 connections)
- *... and 27 more nodes in this community*

## Relationships

- [player disconnect handlers](player_disconnect_handlers.md) (12 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (9 shared connections)
- [combat services turn](combat_services_turn.md) (6 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [room look commands](room_look_commands.md) (3 shared connections)
- [command utility models](command_utility_models.md) (3 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [tsconfig build {ts,tsx}](tsconfig_build_%7Bts%2Ctsx%7D.md) (1 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (1 shared connections)
- [quest service game](quest_service_game.md) (1 shared connections)
- [commands communication channels](commands_communication_channels.md) (1 shared connections)

## Source Files

- `server/realtime/player_connection_setup.py`
- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- `server/tests/unit/realtime/test_player_presence_utils.py`

## Audit Trail

- EXTRACTED: 228 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*