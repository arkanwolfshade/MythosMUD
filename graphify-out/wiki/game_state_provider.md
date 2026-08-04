# game state provider

> 78 nodes

## Key Concepts

- **test_game_state_provider.py** (41 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **game_state_provider()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **mock_room_manager()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **mock_get_async_persistence()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **mock_send_personal_message()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **mock_get_app()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_player()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_players_batch()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_players_batch_empty()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_players_batch_no_persistence()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_players_batch_player_not_found()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_npcs_batch()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_npcs_batch_empty()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_convert_room_uuids_to_names()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_room_occupants()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_send_initial_game_state()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_player_not_found()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_npcs_batch_none_ids()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_convert_room_uuids_to_names_empty_room_data()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_convert_room_uuids_to_names_no_player_ids()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_convert_room_uuids_to_names_invalid_uuid()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_convert_room_uuids_to_names_player_not_found()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_room_occupants_empty_online_players()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_room_occupants_with_online_players()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_send_initial_game_state_no_player()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- *... and 53 more nodes in this community*

## Relationships

- [nats services metrics](nats_services_metrics.md) (2 shared connections)
- [combat services turn](combat_services_turn.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Audit Trail

- EXTRACTED: 157 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*