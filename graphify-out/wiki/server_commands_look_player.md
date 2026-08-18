# server commands look player

> 89 nodes

## Key Concepts

- **test_look_player.py** (33 connections) — `server/tests/unit/commands/test_look_player.py`
- **look_player.py** (26 connections) — `server/commands/look_player.py`
- **_format_player_look_display()** (22 connections) — `server/commands/look_player.py`
- **_select_target_player()** (17 connections) — `server/commands/look_player.py`
- **_handle_player_look()** (13 connections) — `server/commands/look_player.py`
- **asyncio** (13 connections)
- **_try_lookup_player_implicit()** (12 connections) — `server/commands/look_player.py`
- **test_look_player_helpers.py** (12 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **_get_players_in_room()** (11 connections) — `server/commands/look_player.py`
- **_find_matching_players()** (9 connections) — `server/commands/look_player.py`
- **Any** (8 connections)
- **_apply_grace_period_labels()** (6 connections) — `server/commands/look_player.py`
- **_player_id_uuid()** (4 connections) — `server/commands/look_player.py`
- **test_find_matching_players_no_match()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_find_matching_players_success()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_empty()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_invalid_uuid()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_non_iterable()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_success()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_handle_player_look_multiple_matches()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_handle_player_look_not_found()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_handle_player_look_success()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_handle_player_look_with_instance_number()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_try_lookup_player_implicit_multiple_matches()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_try_lookup_player_implicit_not_found()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- *... and 64 more nodes in this community*

## Relationships

- [claude rules pytest](claude_rules_pytest.md) (8 shared connections)
- [server commands look helpers](server_commands_look_helpers.md) (7 shared connections)
- [server commands look command](server_commands_look_command.md) (5 shared connections)
- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (3 shared connections)
- [server realtime integration game state](server_realtime_integration_game_state.md) (3 shared connections)
- [server commands look room](server_commands_look_room.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)

## Source Files

- `server/commands/look_player.py`
- `server/tests/unit/commands/test_look_player.py`
- `server/tests/unit/commands/test_look_player_helpers.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 189 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*