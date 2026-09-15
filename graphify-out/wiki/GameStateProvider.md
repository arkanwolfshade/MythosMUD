# GameStateProvider

> 63 nodes

## Key Concepts

- **GameStateProvider** (30 connections) — `server/realtime/integration/game_state_provider.py`
- **.send_initial_game_state()** (14 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (14 connections)
- **Any** (13 connections)
- **test_game_state_provider_hallucination.py** (11 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
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
- **.get_player()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **test_send_initial_game_state_hallucinates_exits_for_deranged_viewer()** (5 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **test_send_initial_game_state_includes_viewer_phantom()** (5 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **Player** (5 connections)
- **fixture** (5 connections)
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 38 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (8 shared connections)
- [game_state_provider.py](game_state_provider.py.md) (5 shared connections)
- [.state](state.md) (3 shared connections)
- [test_game_state_provider.py](test_game_state_provider.py.md) (2 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (2 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (1 shared connections)
- [get_hallucinated_exits](get_hallucinated_exits.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`

## Audit Trail

- EXTRACTED: 130 (92%)
- INFERRED: 12 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*