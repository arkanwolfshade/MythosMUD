# Container Persistence Queries

> 131 nodes

## Key Concepts

- **websocket_room_updates.py** (32 connections) — `server/realtime/websocket_room_updates.py`
- **look_room.py** (28 connections) — `server/commands/look_room.py`
- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **test_rest_and_grace_period.py** (24 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **game_state_provider.py** (21 connections) — `server/realtime/integration/game_state_provider.py`
- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **_filter_other_players()** (17 connections) — `server/commands/look_room.py`
- **test_disconnect_grace_period.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_visual_indicator.py** (13 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **get_player_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **test_both_linkdead_and_warded_indicators()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **test_warded_indicator_in_player_occupant_processor()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **UUID** (4 connections)
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- *... and 106 more nodes in this community*

## Relationships

- [Player Respawn Events](Player_Respawn_Events.md) (24 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (19 shared connections)
- [Client Event Store](Client_Event_Store.md) (16 shared connections)
- [Look Player Command](Look_Player_Command.md) (12 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (11 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (9 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (9 shared connections)
- [Look Display Helpers](Look_Display_Helpers.md) (8 shared connections)
- [Chat Rate Limiter](Chat_Rate_Limiter.md) (6 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (6 shared connections)
- [Game State Provider](Game_State_Provider.md) (6 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (6 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/realtime/disconnect_grace_period.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/player_occupant_processor.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_player_occupant_processor.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 565 (100%)
- INFERRED: 2 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*