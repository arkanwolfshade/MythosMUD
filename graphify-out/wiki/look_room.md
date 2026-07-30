# look room

> 100 nodes

## Key Concepts

- **test_look_room.py** (35 connections) — `server/tests/unit/commands/test_look_room.py`
- **look_room.py** (28 connections) — `server/commands/look_room.py`
- **test_look_room_helpers.py** (20 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **_filter_other_players()** (17 connections) — `server/commands/look_room.py`
- **_handle_room_look()** (17 connections) — `server/commands/look_room.py`
- **_format_items_section()** (11 connections) — `server/commands/look_room.py`
- **_get_room_description()** (10 connections) — `server/commands/look_room.py`
- **_format_exits_list()** (10 connections) — `server/commands/look_room.py`
- **_format_containers_section()** (9 connections) — `server/commands/look_room.py`
- **_format_players_section()** (9 connections) — `server/commands/look_room.py`
- **_get_room_id()** (9 connections) — `server/commands/look_room.py`
- **_handle_direction_look()** (9 connections) — `server/commands/look_room.py`
- **Any** (8 connections)
- **_format_npcs_section()** (8 connections) — `server/commands/look_room.py`
- **test_format_items_section_empty()** (3 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_items_section_with_items()** (3 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_no_room_id()** (3 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_no_persistence()** (3 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_with_containers()** (3 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_empty()** (3 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_npcs_section_no_room_id()** (3 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_npcs_section_with_npcs()** (3 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_npcs_section_empty()** (3 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_filter_other_players_excludes_current()** (3 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_filter_other_players_no_name_attribute()** (3 connections) — `server/tests/unit/commands/test_look_room.py`
- *... and 75 more nodes in this community*

## Relationships

- [look player](look_player.md) (7 shared connections)
- [login grace period](login_grace_period.md) (6 shared connections)
- [look helpers](look_helpers.md) (5 shared connections)
- [test build room drop summary](test_build_room_drop_summary.md) (4 shared connections)
- [Tests for handle special command](Tests_for_handle_special_command.md) (2 shared connections)
- [command admin](command_admin.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (1 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/tests/unit/commands/test_look_room.py`
- `server/tests/unit/commands/test_look_room_helpers.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 360 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*