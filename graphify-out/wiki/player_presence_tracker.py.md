# player_presence_tracker.py

> 116 nodes · cohesion 0.03

## Key Concepts

- **test_look_room.py** (45 connections) — `server/tests/unit/commands/test_look_room.py`
- **look_room.py** (44 connections) — `server/commands/look_room.py`
- **_handle_room_look()** (25 connections) — `server/commands/look_room.py`
- **test_look_room_helpers.py** (21 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **asyncio** (18 connections)
- **_filter_other_players()** (17 connections) — `server/commands/look_room.py`
- **_format_containers_section()** (11 connections) — `server/commands/look_room.py`
- **_format_items_section()** (11 connections) — `server/commands/look_room.py`
- **_format_exits_list()** (10 connections) — `server/commands/look_room.py`
- **_format_npcs_section()** (10 connections) — `server/commands/look_room.py`
- **_get_room_description()** (10 connections) — `server/commands/look_room.py`
- **_get_room_id()** (10 connections) — `server/commands/look_room.py`
- **Any** (10 connections)
- **_format_players_section()** (9 connections) — `server/commands/look_room.py`
- **_handle_direction_look()** (9 connections) — `server/commands/look_room.py`
- **_try_lookup_phantom_implicit()** (9 connections) — `server/commands/look_room.py`
- **_npc_section_lines()** (5 connections) — `server/commands/look_room.py`
- **test_format_npcs_section_includes_viewer_phantom()** (5 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_format_npcs_section_with_npcs()** (5 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_handle_direction_look_success()** (5 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_handle_room_look_hallucinates_exits_for_deranged_viewer()** (5 connections) — `server/tests/unit/commands/test_look_room.py`
- **test_handle_room_look_success()** (5 connections) — `server/tests/unit/commands/test_look_room.py`
- **_classify_containers_and_corpses()** (4 connections) — `server/commands/look_room.py`
- **test_filter_other_players()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- **test_filter_other_players_all_filtered()** (4 connections) — `server/tests/unit/commands/test_look_room_helpers.py`
- *... and 91 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (17 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (7 shared connections)
- [_RecordingRoom](_RecordingRoom.md) (7 shared connections)
- [SystemAdminChannelStrategy](SystemAdminChannelStrategy.md) (7 shared connections)
- [test_logout_commands.py](test_logout_commands.py.md) (4 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (3 shared connections)
- [required](required.md) (3 shared connections)
- [ChatLogger](ChatLogger.md) (3 shared connections)
- [security.ts](security.ts.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [real_time.py](real_time.py.md) (1 shared connections)

## Source Files

- `server/commands/look_room.py`
- `server/tests/unit/commands/test_look_room.py`
- `server/tests/unit/commands/test_look_room_helpers.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 277 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*