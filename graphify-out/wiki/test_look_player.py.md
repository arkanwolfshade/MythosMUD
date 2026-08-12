# test_look_player.py

> 99 nodes

## Key Concepts

- **test_look_player.py** (32 connections) — `server/tests/unit/commands/test_look_player.py`
- **look_player.py** (26 connections) — `server/commands/look_player.py`
- **_format_player_look_display()** (22 connections) — `server/commands/look_player.py`
- **_select_target_player()** (17 connections) — `server/commands/look_player.py`
- **_handle_player_look()** (13 connections) — `server/commands/look_player.py`
- **asyncio** (13 connections)
- **test_visual_indicator.py** (13 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
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
- **test_handle_player_look_success()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_handle_player_look_with_instance_number()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- *... and 74 more nodes in this community*

## Relationships

- [test_look_helpers.py](test_look_helpers.py.md) (11 shared connections)
- [look_command.py](look_command.py.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [test_look_room.py](test_look_room.py.md) (5 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (4 shared connections)
- [is_player_in_grace_period](is_player_in_grace_period.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_filter_other_players_adds_linkdead_indicator](test_filter_other_players_adds_linkdead_indicator.md) (2 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (1 shared connections)

## Source Files

- `server/commands/look_helpers.py`
- `server/commands/look_player.py`
- `server/tests/unit/commands/test_look_player.py`
- `server/tests/unit/commands/test_look_player_helpers.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 210 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*