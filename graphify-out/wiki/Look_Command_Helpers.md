# Look Command Helpers

> 43 nodes · cohesion 0.10

## Key Concepts

- **.state()** (36 connections) — `server/realtime/connection_state_machine.py`
- **GameStateProvider** (27 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (15 connections)
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (8 connections) — `server/realtime/nats_message_handler.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._convert_player_uuids_to_names()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_room_occupants()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (5 connections)
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **Current FSM state as a single State.          Narrows base class type (Any | Mut** (1 connections) — `server/realtime/connection_state_machine.py`
- **Get NPC names for multiple NPCs in a batch operation.          Args:** (1 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 18 more nodes in this community*

## Relationships

- [Game Mechanics Service](Game_Mechanics_Service.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (5 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (3 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (3 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Commands Inventory Item](Commands_Inventory_Item.md) (2 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (2 shared connections)
- [WebSocket Player Helpers](WebSocket_Player_Helpers.md) (2 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (2 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (2 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 188 (80%)
- INFERRED: 47 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*