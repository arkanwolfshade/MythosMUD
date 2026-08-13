# UUID

> 38 nodes

## Key Concepts

- **UUID** (14 connections)
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (9 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_data_for_client()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._convert_player_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (5 connections)
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **setter** (1 connections)
- **Get NPC names for multiple NPCs in a batch operation. Args: npc_ids: List of…** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get player name and add grace period indicators if applicable.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Convert player UUIDs to names in room_data.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Convert player UUIDs and NPC IDs in room_data to names. CRITICAL: NEVER send…** (1 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 13 more nodes in this community*

## Relationships

- [connection_initialization.py](connection_initialization.py.md) (17 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [.state](state.md) (3 shared connections)
- [is_player_in_grace_period](is_player_in_grace_period.md) (2 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [quest_service](quest_service.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 87 (90%)
- INFERRED: 10 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*