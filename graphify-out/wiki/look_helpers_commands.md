# look helpers commands

> 356 nodes

## Key Concepts

- **AttributeError** (45 connections)
- **websocket_room_updates.py** (36 connections) — `server/realtime/websocket_room_updates.py`
- **test_look_room.py** (35 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_websocket_room_updates.py** (32 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **look_room.py** (28 connections) — `server/commands/look_room.py`
- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **broadcast_room_update()** (26 connections) — `server/realtime/websocket_room_updates.py`
- **test_player_occupant_processor.py** (26 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_rest_and_grace_period.py** (24 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **test_look_room_helpers.py** (20 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **room_occupant_manager.py** (19 connections) — `server/realtime/room_occupant_manager.py`
- **_filter_other_players()** (17 connections) — `server/commands/look_room.py`
- **_handle_room_look()** (17 connections) — `server/commands/look_room.py`
- **test_disconnect_grace_period.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **player_name_utils.py** (13 connections) — `server/realtime/player_name_utils.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **test_visual_indicator.py** (13 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- *... and 331 more nodes in this community*

## Relationships

- [command utility models](command_utility_models.md) (29 shared connections)
- [models npc rationale](models_npc_rationale.md) (18 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (14 shared connections)
- [combat services turn](combat_services_turn.md) (12 shared connections)
- [NATS Messaging](NATS_Messaging.md) (12 shared connections)
- [room renderer functions](room_renderer_functions.md) (9 shared connections)
- [rest grace period](rest_grace_period.md) (9 shared connections)
- [combat services messaging](combat_services_messaging.md) (8 shared connections)
- [room websocket updates](room_websocket_updates.md) (8 shared connections)
- [player presence tracker](player_presence_tracker.md) (6 shared connections)
- [connection realtime statistics](connection_realtime_statistics.md) (5 shared connections)
- [emote game service](emote_game_service.md) (5 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_name_utils.py`
- `server/realtime/player_occupant_processor.py`
- `server/realtime/room_occupant_manager.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/auth/test_auth_utils.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/commands/test_look_room.py`
- `server/tests/unit/commands/test_look_room_helpers.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_player_name_utils.py`
- `server/tests/unit/realtime/test_player_occupant_processor.py`
- `server/tests/unit/realtime/test_visual_indicator.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 1249 (96%)
- INFERRED: 55 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*