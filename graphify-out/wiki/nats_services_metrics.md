# nats services metrics

> 46 nodes

## Key Concepts

- **.state()** (36 connections) — `server/realtime/connection_state_machine.py`
- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (15 connections)
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (9 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._convert_player_uuids_to_names()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (5 connections)
- **.get_room_occupants()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **_not_configured_async()** (3 connections) — `server/realtime/nats_message_handler.py`
- **Any** (2 connections)
- *... and 21 more nodes in this community*

## Relationships

- [command utility models](command_utility_models.md) (8 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (5 shared connections)
- [combat commands handler](combat_commands_handler.md) (2 shared connections)
- [rate limiter services](rate_limiter_services.md) (2 shared connections)
- [command helpers functions](command_helpers_functions.md) (2 shared connections)
- [npc combat base](npc_combat_base.md) (2 shared connections)
- [connection state machine](connection_state_machine.md) (2 shared connections)
- [player presence tracker](player_presence_tracker.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (2 shared connections)
- [services npc startup](services_npc_startup.md) (2 shared connections)
- [game state provider](game_state_provider.md) (2 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (2 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 193 (80%)
- INFERRED: 48 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*