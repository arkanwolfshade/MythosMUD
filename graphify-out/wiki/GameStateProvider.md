# GameStateProvider

> 73 nodes

## Key Concepts

- **GameStateProvider** (41 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (17 connections)
- **.send_initial_game_state()** (14 connections) — `server/realtime/integration/game_state_provider.py`
- **Any** (12 connections)
- **test_game_state_provider_hallucination.py** (11 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **._apply_grace_period_suffixes()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._build_client_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._convert_player_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (6 connections)
- **.get_player()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **test_send_initial_game_state_hallucinates_exits_for_deranged_viewer()** (5 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **test_send_initial_game_state_includes_viewer_phantom()** (5 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **fixture** (5 connections)
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 48 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_game_state_provider.py](test_game_state_provider.py.md) (4 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (4 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [fixture](fixture.md) (1 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (1 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (1 shared connections)
- [test_get_player_data_for_client_app_state_fallback](test_get_player_data_for_client_app_state_fallback.md) (1 shared connections)
- [test_get_player_data_for_client_dict_fallback](test_get_player_data_for_client_dict_fallback.md) (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`

## Audit Trail

- EXTRACTED: 149 (91%)
- INFERRED: 15 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*