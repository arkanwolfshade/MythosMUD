# Look Player Command

> 78 nodes · cohesion 0.04

## Key Concepts

- **test_look_player.py** (31 connections) — `server/tests/unit/commands/test_look_player.py`
- **_format_player_look_display()** (23 connections) — `server/commands/look_player.py`
- **_select_target_player()** (17 connections) — `server/commands/look_player.py`
- **_handle_player_look()** (13 connections) — `server/commands/look_player.py`
- **_try_lookup_player_implicit()** (12 connections) — `server/commands/look_player.py`
- **_get_players_in_room()** (11 connections) — `server/commands/look_player.py`
- **test_look_player_helpers.py** (11 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **_find_matching_players()** (9 connections) — `server/commands/look_player.py`
- **Any** (6 connections) — `server/commands/look_player.py`
- **Try to find and display an NPC in implicit lookup.** (3 connections) — `server/commands/look_npc.py`
- **test_format_player_look_display()** (3 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **test_format_player_look_display_no_equipment()** (3 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **test_format_player_look_display_unknown_name()** (3 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **test_select_target_player_instance_number_out_of_range()** (3 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **test_select_target_player_multiple_matches()** (3 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **test_select_target_player_no_match()** (3 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **test_select_target_player_single_match()** (3 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **test_select_target_player_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **test_find_matching_players_no_match()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_find_matching_players_success()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_format_player_look_display_basic()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_format_player_look_display_no_equipment()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_format_player_look_display_with_equipment()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_empty()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_invalid_uuid()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- *... and 53 more nodes in this community*

## Relationships

- [[Look Command Helpers]] (11 shared connections)
- [[Look NPC Command]] (3 shared connections)
- [[Look Display Helpers]] (3 shared connections)
- [[Realtime Visual Indicator]] (3 shared connections)
- [[Look Item Commands]] (2 shared connections)
- [[Alias Expansion Logic]] (2 shared connections)
- [[Commands Command Look]] (2 shared connections)
- [[Room Look Formatting]] (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/commands/look_player.py`
- `server/tests/unit/commands/test_look_item.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_player.py`
- `server/tests/unit/commands/test_look_player_helpers.py`

## Audit Trail

- EXTRACTED: 269 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
