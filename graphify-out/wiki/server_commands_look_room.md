# server commands look room

> 91 nodes

## Key Concepts

- **test_look_room.py** (36 connections) — `server/tests/unit/commands/test_look_room.py`
- **look_room.py** (26 connections) — `server/commands/look_room.py`
- **test_look_room_helpers.py** (22 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **_filter_other_players()** (17 connections) — `server/commands/look_room.py`
- **_handle_room_look()** (16 connections) — `server/commands/look_room.py`
- **asyncio** (13 connections)
- **_format_items_section()** (11 connections) — `server/commands/look_room.py`
- **_format_exits_list()** (10 connections) — `server/commands/look_room.py`
- **_get_room_description()** (10 connections) — `server/commands/look_room.py`
- **_format_containers_section()** (9 connections) — `server/commands/look_room.py`
- **_format_players_section()** (9 connections) — `server/commands/look_room.py`
- **_get_room_id()** (9 connections) — `server/commands/look_room.py`
- **_format_npcs_section()** (8 connections) — `server/commands/look_room.py`
- **Any** (8 connections)
- **_handle_direction_look()** (7 connections) — `server/commands/look_room.py`
- **test_filter_other_players()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_all_filtered()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_includes_player_without_websocket()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_excludes_current()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_filter_other_players_no_name_attribute()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_empty()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_no_persistence()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_no_room_id()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_with_containers()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_npcs_section_empty()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- *... and 66 more nodes in this community*

## Relationships

- [server commands look helpers get](server_commands_look_helpers_get.md) (7 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (4 shared connections)
- [server realtime occupant display](server_realtime_occupant_display.md) (3 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (3 shared connections)
- [server commands look npc get](server_commands_look_npc_get.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (1 shared connections)
- [server commands exploration commands](server_commands_exploration_commands.md) (1 shared connections)
- [server commands look npc](server_commands_look_npc.md) (1 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/tests/unit/commands/test_look_room.py`
- `server/tests/unit/commands/test_look_room_helpers.py`

## Audit Trail

- EXTRACTED: 205 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*