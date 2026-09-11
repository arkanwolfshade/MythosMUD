# test_look_room.py

> 110 nodes

## Key Concepts

- **test_look_room.py** (40 connections) — `server/tests/unit/commands/test_look_room.py`
- **look_room.py** (32 connections) — `server/commands/look_room.py`
- **test_look_room_helpers.py** (21 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **_handle_room_look()** (19 connections) — `server/commands/look_room.py`
- **_filter_other_players()** (17 connections) — `server/commands/look_room.py`
- **asyncio** (17 connections)
- **_format_items_section()** (11 connections) — `server/commands/look_room.py`
- **_format_npcs_section()** (11 connections) — `server/commands/look_room.py`
- **_format_exits_list()** (10 connections) — `server/commands/look_room.py`
- **_get_room_description()** (10 connections) — `server/commands/look_room.py`
- **_get_room_id()** (10 connections) — `server/commands/look_room.py`
- **Any** (10 connections)
- **_format_containers_section()** (9 connections) — `server/commands/look_room.py`
- **_format_players_section()** (9 connections) — `server/commands/look_room.py`
- **_handle_direction_look()** (9 connections) — `server/commands/look_room.py`
- **_try_lookup_phantom_implicit()** (9 connections) — `server/commands/look_room.py`
- **test_filter_other_players()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_all_filtered()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_includes_player_without_websocket()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_excludes_current()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_filter_other_players_no_name_attribute()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_empty()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_no_persistence()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_no_room_id()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_containers_section_with_containers()** (4 connections) — `server/tests/unit/commands/test_look_room.py`
- *... and 85 more nodes in this community*

## Relationships

- [look_command.py](look_command.py.md) (7 shared connections)
- [PlayerOccupantProcessor](PlayerOccupantProcessor.md) (4 shared connections)
- [test_room_renderer.py](test_room_renderer.py.md) (4 shared connections)
- [CorruptionTier](CorruptionTier.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [room_update_event_builder.py](room_update_event_builder.py.md) (3 shared connections)
- [test_look_player.py](test_look_player.py.md) (3 shared connections)
- [_get_lifecycle_manager](_get_lifecycle_manager.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [LucidityTierCache](LucidityTierCache.md) (1 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (1 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/tests/unit/commands/test_look_room.py`
- `server/tests/unit/commands/test_look_room_helpers.py`

## Audit Trail

- EXTRACTED: 238 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*