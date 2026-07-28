# Server Commands (17)

> 84 nodes

## Key Concepts

- **test_look_player.py** (32 connections) — `server/tests/unit/commands/test_look_player.py`
- **look_player.py** (23 connections) — `server/commands/look_player.py`
- **_format_player_look_display()** (23 connections) — `server/commands/look_player.py`
- **_select_target_player()** (17 connections) — `server/commands/look_player.py`
- **_handle_player_look()** (13 connections) — `server/commands/look_player.py`
- **_try_lookup_player_implicit()** (12 connections) — `server/commands/look_player.py`
- **test_look_player_helpers.py** (12 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **_get_players_in_room()** (11 connections) — `server/commands/look_player.py`
- **_find_matching_players()** (9 connections) — `server/commands/look_player.py`
- **Any** (6 connections)
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
- **test_format_player_look_display_no_equipment()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_handle_player_look_success()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- *... and 59 more nodes in this community*

## Relationships

- [Server Commands (11)](Server_Commands_%2811%29.md) (7 shared connections)
- [Server Realtime (8)](Server_Realtime_%288%29.md) (6 shared connections)
- [Server Commands](Server_Commands.md) (5 shared connections)
- [Server Realtime (62)](Server_Realtime_%2862%29.md) (4 shared connections)
- [Server Commands (13)](Server_Commands_%2813%29.md) (3 shared connections)
- [Server Realtime (20)](Server_Realtime_%2820%29.md) (2 shared connections)
- [Server Commands (50)](Server_Commands_%2850%29.md) (2 shared connections)
- [Server Realtime (3)](Server_Realtime_%283%29.md) (1 shared connections)

## Source Files

- `server/commands/look_player.py`
- `server/tests/unit/commands/test_look_player.py`
- `server/tests/unit/commands/test_look_player_helpers.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 298 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*