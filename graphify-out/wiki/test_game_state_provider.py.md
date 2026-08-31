# test_game_state_provider.py

> 22 nodes

## Key Concepts

- **test_game_state_provider.py** (42 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_add_grace_period_indicators()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_fallback_player_data_json_stats()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_fallback_player_data_with_get_stats()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_login_grace_period_status()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_npcs_batch()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_npcs_batch_empty()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_npcs_batch_exception_fallback()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_npcs_batch_none_ids()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_npcs_batch_with_lifecycle_manager()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_player_name_with_grace_periods()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Unit tests for game state provider. Tests the GameStateProvider class.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_npcs_batch() returns NPC names.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_npcs_batch() returns empty dict for empty input.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_npcs_batch() handles None in NPC IDs list.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test _get_fallback_player_data() uses get_stats when available.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test _get_fallback_player_data() parses JSON stats string.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test _get_player_name_with_grace_periods() returns name with grace indicators.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_npcs_batch() resolves names from active NPCs.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_npcs_batch() falls back to ID-derived names on service error.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test _add_grace_period_indicators() appends linkdead marker.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test _get_login_grace_period_status() returns active grace period info.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Relationships

- [asyncio](asyncio.md) (9 shared connections)
- [fixture](fixture.md) (5 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_convert_room_uuids_to_names](test_convert_room_uuids_to_names.md) (1 shared connections)
- [test_get_room_occupants](test_get_room_occupants.md) (1 shared connections)
- [test_get_player_not_found](test_get_player_not_found.md) (1 shared connections)
- [test_convert_room_uuids_to_names_no_player_ids](test_convert_room_uuids_to_names_no_player_ids.md) (1 shared connections)
- [test_convert_room_uuids_to_names_invalid_uuid](test_convert_room_uuids_to_names_invalid_uuid.md) (1 shared connections)
- [test_get_room_occupants_empty_online_players](test_get_room_occupants_empty_online_players.md) (1 shared connections)
- [test_get_room_occupants_with_online_players](test_get_room_occupants_with_online_players.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Audit Trail

- EXTRACTED: 52 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*