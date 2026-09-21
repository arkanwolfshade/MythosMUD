# test_game_state_provider.py

> 24 nodes

## Key Concepts

- **test_game_state_provider.py** (46 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_player_name_with_grace_periods_falls_back_to_user()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_player_name_with_grace_periods_no_name_no_user()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_player_name_with_grace_periods_rejects_uuid_shaped_name()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_fallback_player_data_json_stats()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_fallback_player_data_with_get_stats()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_login_grace_period_status()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_npcs_batch()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_npcs_batch_exception_fallback()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_npcs_batch_none_ids()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_npcs_batch_with_lifecycle_manager()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_player_name_with_grace_periods()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Unit tests for game state provider. Tests the GameStateProvider class.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_npcs_batch() returns NPC names.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_npcs_batch() handles None in NPC IDs list.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test _get_fallback_player_data() uses get_stats when available.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test _get_fallback_player_data() parses JSON stats string.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test _get_player_name_with_grace_periods() returns name with grace indicators.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_npcs_batch() resolves names from active NPCs.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test get_npcs_batch() falls back to ID-derived names on service error.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test _get_login_grace_period_status() returns active grace period info.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **A UUID-shaped 'name' is never a real display name, even with an otherwise valid…** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **No usable player.name falls back to player.user.username.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Neither a usable name nor a user relation yields None, not a crash.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Relationships

- [asyncio](asyncio.md) (10 shared connections)
- [fixture](fixture.md) (5 shared connections)
- [GameStateProvider](GameStateProvider.md) (4 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (1 shared connections)
- [test_get_players_batch_player_not_found](test_get_players_batch_player_not_found.md) (1 shared connections)
- [test_get_npcs_batch_empty](test_get_npcs_batch_empty.md) (1 shared connections)
- [test_get_player_not_found](test_get_player_not_found.md) (1 shared connections)
- [test_convert_room_uuids_to_names_empty_room_data](test_convert_room_uuids_to_names_empty_room_data.md) (1 shared connections)
- [test_convert_room_uuids_to_names_no_player_ids](test_convert_room_uuids_to_names_no_player_ids.md) (1 shared connections)
- [test_get_room_occupants_empty_online_players](test_get_room_occupants_empty_online_players.md) (1 shared connections)
- [test_send_initial_game_state_no_player](test_send_initial_game_state_no_player.md) (1 shared connections)
- [test_send_initial_game_state_send_fails](test_send_initial_game_state_send_fails.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Audit Trail

- EXTRACTED: 57 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*