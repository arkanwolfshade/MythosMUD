# asyncio

> 19 nodes

## Key Concepts

- **asyncio** (23 connections)
- **test_convert_room_uuids_to_names()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_convert_room_uuids_to_names_empty_room_data()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_convert_room_uuids_to_names_player_not_found()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_player()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_player_data_for_client_with_service()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_players_batch_no_persistence()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_players_batch_player_not_found()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_process_occupants_with_grace_periods()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_send_initial_game_state()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_players_batch() handles player not found.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test convert_room_uuids_to_names() converts UUIDs to names.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test send_initial_game_state() sends initial state.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test convert_room_uuids_to_names() with empty room_data.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test convert_room_uuids_to_names() when player not found.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test _process_occupants_with_grace_periods() splits players and NPCs.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test _get_player_data_for_client() uses PlayerService when available.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_player() retrieves player from persistence.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_players_batch() returns empty dict when persistence is None.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Relationships

- [test_game_state_provider.py](test_game_state_provider.py.md) (9 shared connections)
- [test_convert_room_uuids_to_names_invalid_uuid](test_convert_room_uuids_to_names_invalid_uuid.md) (1 shared connections)
- [test_convert_room_uuids_to_names_no_player_ids](test_convert_room_uuids_to_names_no_player_ids.md) (1 shared connections)
- [test_convert_room_uuids_with_npcs](test_convert_room_uuids_with_npcs.md) (1 shared connections)
- [test_get_following_for_client](test_get_following_for_client.md) (1 shared connections)
- [test_get_player_not_found](test_get_player_not_found.md) (1 shared connections)
- [test_get_players_batch](test_get_players_batch.md) (1 shared connections)
- [test_get_players_batch_empty](test_get_players_batch_empty.md) (1 shared connections)
- [test_get_quest_log_for_client](test_get_quest_log_for_client.md) (1 shared connections)
- [test_get_room_data_with_conversion](test_get_room_data_with_conversion.md) (1 shared connections)
- [test_get_room_occupants](test_get_room_occupants.md) (1 shared connections)
- [test_get_room_occupants_empty_online_players](test_get_room_occupants_empty_online_players.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*