# GameStateProvider

> 47 nodes

## Key Concepts

- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (14 connections)
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (9 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_data_for_client()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._convert_player_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (5 connections)
- **server/realtime/integration/__init__.py** (5 connections) — `server/realtime/integration/__init__.py`
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **_not_configured_async()** (3 connections) — `server/realtime/nats_message_handler.py`
- **Any** (2 connections)
- *... and 22 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (9 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (4 shared connections)
- [real_time.py](real_time.py.md) (3 shared connections)
- [test_game_state_provider.py](test_game_state_provider.py.md) (2 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [quest_service](quest_service.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)
- [test_connection_manager_api.py](test_connection_manager_api.py.md) (1 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (1 shared connections)
- [NATSError](NATSError.md) (1 shared connections)

## Source Files

- `server/realtime/integration/__init__.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 105 (91%)
- INFERRED: 11 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*