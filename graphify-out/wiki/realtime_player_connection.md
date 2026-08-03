# realtime player connection

> 40 nodes

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
- **_update_player_last_active()** (6 connections) — `server/realtime/player_connection_setup.py`
- **Any** (6 connections)
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
- **Update last_active timestamp in database when player connects.      Args:** (1 connections) — `server/realtime/player_connection_setup.py`
- **Return stable room id for quest_offers lookup; strip instance_<uuid>_ prefix if** (1 connections) — `server/realtime/player_connection_setup.py`
- *... and 15 more nodes in this community*

## Relationships

- [player presence tracker](player_presence_tracker.md) (9 shared connections)
- [npc populate databases](npc_populate_databases.md) (7 shared connections)
- [grace period disconnect](grace_period_disconnect.md) (6 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [grace period login](grace_period_login.md) (3 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (2 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)
- [quest service game](quest_service_game.md) (1 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)

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