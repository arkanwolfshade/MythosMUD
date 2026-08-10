# Room Look Formatting

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

- [Look Player Command](Look_Player_Command.md) (7 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (5 shared connections)
- [Look Display Helpers](Look_Display_Helpers.md) (4 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (3 shared connections)
- [Spell Effects Tests](Spell_Effects_Tests.md) (3 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (2 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (1 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (1 shared connections)

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