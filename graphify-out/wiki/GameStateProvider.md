# GameStateProvider

> 59 nodes

## Key Concepts

- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **NATSMessageHandler** (25 connections) — `server/realtime/nats_message_handler.py`
- **UUID** (14 connections)
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (9 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_data_for_client()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **._convert_player_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (5 connections)
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_standardized_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- *... and 34 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [.state](state.md) (3 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (2 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (2 shared connections)
- [realtime/conftest.py](realtime-conftest.py.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (2 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (2 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (2 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 131 (88%)
- INFERRED: 18 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*