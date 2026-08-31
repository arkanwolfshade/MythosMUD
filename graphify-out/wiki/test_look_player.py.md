# test_look_player.py

> 122 nodes

## Key Concepts

- **test_look_player.py** (33 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_look_helpers.py** (31 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **look_player.py** (26 connections) — `server/commands/look_player.py`
- **_format_player_look_display()** (22 connections) — `server/commands/look_player.py`
- **_get_health_label()** (17 connections) — `server/commands/look_helpers.py`
- **_get_lucidity_label()** (17 connections) — `server/commands/look_helpers.py`
- **_select_target_player()** (17 connections) — `server/commands/look_player.py`
- **_handle_player_look()** (13 connections) — `server/commands/look_player.py`
- **asyncio** (13 connections)
- **_try_lookup_player_implicit()** (12 connections) — `server/commands/look_player.py`
- **test_look_player_helpers.py** (12 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **_get_visible_equipment()** (11 connections) — `server/commands/look_helpers.py`
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
- *... and 97 more nodes in this community*

## Relationships

- [look_helpers.py](look_helpers.py.md) (29 shared connections)
- [look_command.py](look_command.py.md) (9 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (4 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (3 shared connections)
- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)

## Source Files

- `server/commands/look_helpers.py`
- `server/commands/look_player.py`
- `server/tests/unit/commands/test_look_helpers.py`
- `server/tests/unit/commands/test_look_player.py`
- `server/tests/unit/commands/test_look_player_helpers.py`

## Audit Trail

- EXTRACTED: 266 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*