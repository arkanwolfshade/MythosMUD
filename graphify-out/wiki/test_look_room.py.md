# test_look_room.py

> 138 nodes

## Key Concepts

- **test_look_room.py** (36 connections) — `server/tests/unit/commands/test_look_room.py`
- **look_room.py** (26 connections) — `server/commands/look_room.py`
- **test_room_renderer.py** (25 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **format_room_drop_lines()** (24 connections) — `server/utils/room_renderer.py`
- **test_look_room_helpers.py** (22 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **_filter_other_players()** (17 connections) — `server/commands/look_room.py`
- **_handle_room_look()** (17 connections) — `server/commands/look_room.py`
- **asyncio** (13 connections)
- **_format_items_section()** (11 connections) — `server/commands/look_room.py`
- **occupant_display.py** (11 connections) — `server/realtime/occupant_display.py`
- **_format_exits_list()** (10 connections) — `server/commands/look_room.py`
- **_get_room_description()** (10 connections) — `server/commands/look_room.py`
- **format_occupant_display_name()** (10 connections) — `server/realtime/occupant_display.py`
- **room_renderer.py** (10 connections) — `server/utils/room_renderer.py`
- **_format_containers_section()** (9 connections) — `server/commands/look_room.py`
- **_format_players_section()** (9 connections) — `server/commands/look_room.py`
- **_get_room_id()** (9 connections) — `server/commands/look_room.py`
- **_handle_direction_look()** (9 connections) — `server/commands/look_room.py`
- **_format_npcs_section()** (8 connections) — `server/commands/look_room.py`
- **Any** (8 connections)
- **_apply_grace_badges()** (6 connections) — `server/realtime/occupant_display.py`
- **test_filter_other_players()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_all_filtered()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_includes_player_without_websocket()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_excludes_current()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- *... and 113 more nodes in this community*

## Relationships

- [clone_room_drops](clone_room_drops.md) (20 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [look_command.py](look_command.py.md) (6 shared connections)
- [test_look_player.py](test_look_player.py.md) (5 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [test_filter_other_players_adds_linkdead_indicator](test_filter_other_players_adds_linkdead_indicator.md) (2 shared connections)
- [_get_lifecycle_manager](_get_lifecycle_manager.md) (2 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (1 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (1 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/realtime/occupant_display.py`
- `server/tests/unit/commands/test_look_room.py`
- `server/tests/unit/commands/test_look_room_helpers.py`
- `server/tests/unit/utils/test_room_renderer.py`
- `server/utils/room_renderer.py`

## Audit Trail

- EXTRACTED: 295 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*