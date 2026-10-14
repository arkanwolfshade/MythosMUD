# GameStateProvider

> 64 nodes

## Key Concepts

- **GameStateProvider** (45 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (18 connections)
- **.send_initial_game_state()** (15 connections) — `server/realtime/integration/game_state_provider.py`
- **Any** (12 connections)
- **._process_occupants_with_grace_periods()** (10 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (10 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **._apply_grace_period_suffixes()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._build_client_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._convert_player_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (6 connections)
- **._get_lucidity_for_client()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 39 more nodes in this community*

## Relationships

- [test_game_state_provider.py](test_game_state_provider.py.md) (10 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (9 shared connections)
- [test_game_state_provider_hallucination.py](test_game_state_provider_hallucination.py.md) (4 shared connections)
- [.state](state.md) (4 shared connections)
- [NpcDisposition](NpcDisposition.md) (4 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (2 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (1 shared connections)
- [_AsyncPersistenceLike](_AsyncPersistenceLike.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 138 (84%)
- INFERRED: 26 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*