# combat services turn

> 90 nodes

## Key Concepts

- **test_look_player.py** (32 connections) — `server/tests/unit/commands/test_look_player.py`
- **look_player.py** (23 connections) — `server/commands/look_player.py`
- **_format_player_look_display()** (23 connections) — `server/commands/look_player.py`
- **_select_target_player()** (17 connections) — `server/commands/look_player.py`
- **_handle_player_look()** (13 connections) — `server/commands/look_player.py`
- **_try_lookup_player_implicit()** (12 connections) — `server/commands/look_player.py`
- **test_look_player_helpers.py** (12 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **_get_visible_equipment()** (11 connections) — `server/commands/look_helpers.py`
- **_get_players_in_room()** (11 connections) — `server/commands/look_player.py`
- **_find_matching_players()** (9 connections) — `server/commands/look_player.py`
- **Any** (6 connections)
- **test_warded_indicator_in_look_player()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_get_players_in_room_success()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_empty()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_invalid_uuid()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_non_iterable()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_find_matching_players_success()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_find_matching_players_no_match()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_select_target_player_single_match()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_select_target_player_no_matches()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_select_target_player_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_select_target_player_instance_number_out_of_range()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_select_target_player_multiple_matches()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_format_player_look_display_basic()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_format_player_look_display_with_equipment()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- *... and 65 more nodes in this community*

## Relationships

- [look command commands](look_command_commands.md) (18 shared connections)
- [player occupant processor](player_occupant_processor.md) (7 shared connections)
- [command utility models](command_utility_models.md) (4 shared connections)
- [grace period disconnect](grace_period_disconnect.md) (3 shared connections)
- [look helpers commands](look_helpers_commands.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)

## Source Files

- `server/commands/look_helpers.py`
- `server/commands/look_player.py`
- `server/tests/unit/commands/test_look_player.py`
- `server/tests/unit/commands/test_look_player_helpers.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 315 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*