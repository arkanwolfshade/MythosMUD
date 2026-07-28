# Disconnect Grace Period

> 40 nodes · cohesion 0.09

## Key Concepts

- **player_connection_setup.py** (24 connections) — `server/realtime/player_connection_setup.py`
- **handle_new_connection_setup()** (17 connections) — `server/realtime/player_connection_setup.py`
- **player_presence_utils.py** (16 connections) — `server/realtime/player_presence_utils.py`
- **extract_player_name()** (16 connections) — `server/realtime/player_presence_utils.py`
- **_broadcast_player_entered_game()** (9 connections) — `server/realtime/player_connection_setup.py`
- **_trigger_quests_for_room_on_spawn()** (8 connections) — `server/realtime/player_connection_setup.py`
- **UUID** (7 connections)
- **_send_room_occupants_update_after_connection()** (7 connections) — `server/realtime/player_connection_setup.py`
- **get_player_position()** (7 connections) — `server/realtime/player_presence_utils.py`
- **Any** (6 connections)
- **_update_player_last_active()** (6 connections) — `server/realtime/player_connection_setup.py`
- **_add_player_to_room_silently()** (5 connections) — `server/realtime/player_connection_setup.py`
- **_get_name_from_user()** (5 connections) — `server/realtime/player_presence_utils.py`
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
- **Broadcast a structured entry event to other occupants (excluding the newcomer).** (1 connections) — `server/realtime/player_connection_setup.py`
- **Send room_occupants update so other players see the new occupant.      Args:** (1 connections) — `server/realtime/player_connection_setup.py`
- *... and 15 more nodes in this community*

## Relationships

- [Container Loot Helpers](Container_Loot_Helpers.md) (12 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (7 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (6 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (3 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (3 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (2 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (1 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (1 shared connections)
- [Player Service Tests](Player_Service_Tests.md) (1 shared connections)

## Source Files

- `server/realtime/player_connection_setup.py`
- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`

## Audit Trail

- EXTRACTED: 172 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*