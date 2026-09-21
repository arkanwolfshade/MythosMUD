# test_look_room.py

> 146 nodes

## Key Concepts

- **test_look_room.py** (40 connections) — `server/tests/unit/commands/test_look_room.py`
- **look_room.py** (33 connections) — `server/commands/look_room.py`
- **format_room_drop_lines()** (24 connections) — `server/utils/room_renderer.py`
- **test_look_room_helpers.py** (21 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **_handle_room_look()** (19 connections) — `server/commands/look_room.py`
- **_filter_other_players()** (17 connections) — `server/commands/look_room.py`
- **asyncio** (17 connections)
- **get_hallucinated_exits()** (16 connections) — `server/services/exit_hallucination.py`
- **test_exit_hallucination.py** (12 connections) — `server/tests/unit/services/test_exit_hallucination.py`
- **_format_items_section()** (11 connections) — `server/commands/look_room.py`
- **_format_npcs_section()** (11 connections) — `server/commands/look_room.py`
- **Any** (11 connections)
- **_format_containers_section()** (10 connections) — `server/commands/look_room.py`
- **_format_exits_list()** (10 connections) — `server/commands/look_room.py`
- **_get_room_description()** (10 connections) — `server/commands/look_room.py`
- **_get_room_id()** (10 connections) — `server/commands/look_room.py`
- **exit_hallucination.py** (10 connections) — `server/services/exit_hallucination.py`
- **room_renderer.py** (10 connections) — `server/utils/room_renderer.py`
- **_format_players_section()** (9 connections) — `server/commands/look_room.py`
- **_handle_direction_look()** (9 connections) — `server/commands/look_room.py`
- **_try_lookup_phantom_implicit()** (9 connections) — `server/commands/look_room.py`
- **seed_from()** (7 connections) — `server/services/exit_hallucination.py`
- **mulberry32()** (5 connections) — `server/services/exit_hallucination.py`
- **_classify_containers_and_corpses()** (4 connections) — `server/commands/look_room.py`
- **test_filter_other_players()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- *... and 121 more nodes in this community*

## Relationships

- [test_room_renderer.py](test_room_renderer.py.md) (22 shared connections)
- [look_command.py](look_command.py.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [test_look_player.py](test_look_player.py.md) (7 shared connections)
- [CorruptionTier](CorruptionTier.md) (3 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (3 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (3 shared connections)
- [get_viewer_phantom_names](get_viewer_phantom_names.md) (3 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (1 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/services/exit_hallucination.py`
- `server/tests/unit/commands/test_look_room.py`
- `server/tests/unit/commands/test_look_room_helpers.py`
- `server/tests/unit/services/test_exit_hallucination.py`
- `server/utils/room_renderer.py`

## Audit Trail

- EXTRACTED: 319 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*