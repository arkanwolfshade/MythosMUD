# test_look_room.py

> 145 nodes

## Key Concepts

- **test_look_room.py** (40 connections) — `server/tests/unit/commands/test_look_room.py`
- **look_room.py** (33 connections) — `server/commands/look_room.py`
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
- **_format_players_section()** (9 connections) — `server/commands/look_room.py`
- **_handle_direction_look()** (9 connections) — `server/commands/look_room.py`
- **_try_lookup_phantom_implicit()** (9 connections) — `server/commands/look_room.py`
- **seed_from()** (7 connections) — `server/services/exit_hallucination.py`
- **mulberry32()** (5 connections) — `server/services/exit_hallucination.py`
- **_classify_containers_and_corpses()** (4 connections) — `server/commands/look_room.py`
- **test_filter_other_players()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_all_filtered()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_includes_player_without_websocket()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- *... and 120 more nodes in this community*

## Relationships

- [websocket_room_updates.py](websocket_room_updates.py.md) (9 shared connections)
- [test_look_player.py](test_look_player.py.md) (7 shared connections)
- [look_command.py](look_command.py.md) (7 shared connections)
- [test_room_renderer.py](test_room_renderer.py.md) (4 shared connections)
- [format_occupant_display_name](format_occupant_display_name.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/services/exit_hallucination.py`
- `server/tests/unit/commands/test_look_room.py`
- `server/tests/unit/commands/test_look_room_helpers.py`
- `server/tests/unit/realtime/test_visual_indicator.py`
- `server/tests/unit/services/test_exit_hallucination.py`

## Audit Trail

- EXTRACTED: 295 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*