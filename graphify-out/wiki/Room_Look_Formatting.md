# Room Look Formatting

> 98 nodes · cohesion 0.03

## Key Concepts

- **test_look_room.py** (35 connections) — `server/tests/unit/commands/test_look_room.py`
- **look_room.py** (28 connections) — `server/commands/look_room.py`
- **test_look_room_helpers.py** (20 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **_filter_other_players()** (17 connections) — `server/commands/look_room.py`
- **_handle_room_look()** (17 connections) — `server/commands/look_room.py`
- **_format_items_section()** (11 connections) — `server/commands/look_room.py`
- **_format_exits_list()** (10 connections) — `server/commands/look_room.py`
- **_get_room_description()** (10 connections) — `server/commands/look_room.py`
- **_format_containers_section()** (9 connections) — `server/commands/look_room.py`
- **_format_players_section()** (9 connections) — `server/commands/look_room.py`
- **_get_room_id()** (9 connections) — `server/commands/look_room.py`
- **_handle_direction_look()** (9 connections) — `server/commands/look_room.py`
- **_format_npcs_section()** (8 connections) — `server/commands/look_room.py`
- **Any** (8 connections)
- **_get_npcs_in_room()** (7 connections) — `server/commands/look_npc.py`
- **test_filter_other_players()** (3 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_all_filtered()** (3 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_format_exits_list()** (3 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_format_exits_list_empty()** (3 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_format_items_section()** (3 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_format_items_section_empty()** (3 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_format_players_section()** (3 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_format_players_section_empty()** (3 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_get_room_description()** (3 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_get_room_description_fallback()** (3 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- *... and 73 more nodes in this community*

## Relationships

- [Look Player Command](Look_Player_Command.md) (7 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (6 shared connections)
- [Async Persistence Core](Async_Persistence_Core.md) (5 shared connections)
- [Room Drop Renderer](Room_Drop_Renderer.md) (4 shared connections)
- [Look NPC Command](Look_NPC_Command.md) (3 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (1 shared connections)
- [Logging Implementation Summary](Logging_Implementation_Summary.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/commands/look_room.py`
- `server/tests/unit/commands/test_look_room.py`
- `server/tests/unit/commands/test_look_room_helpers.py`

## Audit Trail

- EXTRACTED: 360 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*