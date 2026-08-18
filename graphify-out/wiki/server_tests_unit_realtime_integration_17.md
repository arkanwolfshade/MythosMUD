# server tests unit realtime integration

> 16 nodes

## Key Concepts

- **asyncio** (23 connections)
- **test_convert_room_uuids_to_names_empty_room_data()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_convert_room_uuids_to_names_invalid_uuid()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_player()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_player_not_found()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_players_batch()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_players_batch_empty()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_room_occupants_empty_online_players()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_room_occupants_with_online_players()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_room_occupants() with empty online_players.** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_player() returns None when player not found.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test convert_room_uuids_to_names() with empty room_data.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test convert_room_uuids_to_names() handles invalid UUID strings.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_player() retrieves player from persistence.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_players_batch() retrieves multiple players.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_players_batch() returns empty dict for empty input.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Relationships

- [server tests unit realtime integration](server_tests_unit_realtime_integration.md) (23 shared connections)

## Source Files

- `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*