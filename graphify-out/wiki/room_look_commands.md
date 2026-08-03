# room look commands

> 96 nodes

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
- *... and 71 more nodes in this community*

## Relationships

- [grace period disconnect](grace_period_disconnect.md) (6 shared connections)
- [look command commands](look_command_commands.md) (5 shared connections)
- [room renderer functions](room_renderer_functions.md) (4 shared connections)
- [player look commands](player_look_commands.md) (4 shared connections)
- [look helpers commands](look_helpers_commands.md) (3 shared connections)
- [grace period login](grace_period_login.md) (3 shared connections)
- [command parser rationale](command_parser_rationale.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [npc look commands](npc_look_commands.md) (1 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/tests/unit/commands/test_look_room.py`
- `server/tests/unit/commands/test_look_room_helpers.py`

## Audit Trail

- EXTRACTED: 352 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*