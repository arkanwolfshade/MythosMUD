# GameStateProvider

> 90 nodes

## Key Concepts

- **GameStateProvider** (41 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (17 connections)
- **.send_initial_game_state()** (14 connections) — `server/realtime/integration/game_state_provider.py`
- **Any** (12 connections)
- **resolve_connection_manager()** (11 connections) — `server/realtime/connection_manager.py`
- **resolve_connection_manager()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **test_game_state_provider_hallucination.py** (11 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **.connection_manager()** (10 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **._apply_grace_period_suffixes()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **connection_manager_utils.py** (8 connections) — `server/realtime/connection_manager_utils.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
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
- *... and 65 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (6 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (6 shared connections)
- [test_game_state_provider.py](test_game_state_provider.py.md) (4 shared connections)
- [send_game_event](send_game_event.md) (4 shared connections)
- [.state](state.md) (4 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [HealthStatus](HealthStatus.md) (2 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [fixture](fixture.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_utils.py`
- `server/realtime/integration/__init__.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`

## Audit Trail

- EXTRACTED: 189 (91%)
- INFERRED: 19 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*