# test_look_room.py

> 98 nodes

## Key Concepts

- **test_look_room.py** (35 connections) — `server/tests/unit/commands/test_look_room.py`
- **look_room.py** (28 connections) — `server/commands/look_room.py`
- **test_look_room_helpers.py** (20 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **_filter_other_players()** (17 connections) — `server/commands/look_room.py`
- **_handle_room_look()** (17 connections) — `server/commands/look_room.py`
- **asyncio** (13 connections)
- **_format_items_section()** (11 connections) — `server/commands/look_room.py`
- **_format_exits_list()** (10 connections) — `server/commands/look_room.py`
- **_get_room_description()** (10 connections) — `server/commands/look_room.py`
- **_format_containers_section()** (9 connections) — `server/commands/look_room.py`
- **_format_players_section()** (9 connections) — `server/commands/look_room.py`
- **_get_room_id()** (9 connections) — `server/commands/look_room.py`
- **_handle_direction_look()** (9 connections) — `server/commands/look_room.py`
- **_format_npcs_section()** (8 connections) — `server/commands/look_room.py`
- **Any** (8 connections)
- **test_filter_other_players()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_all_filtered()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_excludes_current()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_filter_other_players_no_name_attribute()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_empty()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_no_persistence()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_no_room_id()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_with_containers()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_npcs_section_empty()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_npcs_section_no_room_id()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- *... and 73 more nodes in this community*

## Relationships

- [test_look_player.py](test_look_player.py.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [look_command.py](look_command.py.md) (5 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (4 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (3 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/tests/unit/commands/test_look_room.py`
- `server/tests/unit/commands/test_look_room_helpers.py`

## Audit Trail

- EXTRACTED: 382 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*